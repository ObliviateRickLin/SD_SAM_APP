import requests
import streamlit as st
from PIL import Image
import io
import requests
import base64
import os

os.environ['CURL_CA_BUNDLE'] = ''

st.set_page_config(
    page_title="Text-to-Image Diffusion",
    initial_sidebar_state="expanded",
)
def add_bg_with_opacity(image_file, opacity = 1):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            opacity: {opacity};
            -webkit-opacity: {opacity};
            -moz-opacity: {opacity};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_with_opacity('bg.jpg') 

st.title("Text-to-Image Diffusion")

MODELS = {
    #"Model 1 db": "https://api-inference.huggingface.co/models/JerryMo/db-simpsons",
    "Model 2 db ": "https://api-inference.huggingface.co/models/JerryMo/db-simpsons-asim-style",
    "Model 3 Lora ": "https://api-inference.huggingface.co/models/Foxintohumanbeing/simpson-lora"# for Lora
    # Add more models here
}
with st.expander("A brief introduction and announcement"):
    st.text_area(label = "",value="""Our team at CUHKSZ, Original Logic, has developed this application as a sub-project for our coursework. It is important to note that this app is not intended for commercial use, but is rather a demonstration of our project. The app is built on a free cloud service and utilizes cloud CPUs to obtain our results. As a result, the processing time for a single image ranges from a few seconds to two or three minutes, depending on the resources and speed of our cloud infrastructure. If processing time exceeds three minutes, it is likely due to other users currently occupying the relevant facilities. You may wish to try a different model or prompt temporarily, or return at a later time.
    The app integrates three different models, each utilizing different fine-tuning methods. This allows you to experiment with different models and prompts, providing a deeper understanding of our models. We welcome any suggestions you may have regarding our work, and are interested in exploring opportunities to upgrade our cloud services or deploy the application to GPUs. Please feel free to leave us a message if you have any feedback or ideas.
    """,disabled = True, label_visibility="collapsed")
    st.text_area(label = "",value = """
    Why does the API run slowly? That might be caused by the following resons:

    1. Someone else is using the model and you are in queue.
    2. The model is using a free device like a CPU instead of a GPU.

    Please note that our app is not a commercial application, it is developed solely to help you better understand our project. The app runs on a free cloud service, and we use cloud CPUs to obtain our results. Generally, the processing time for a single image ranges from a few seconds to two or three minutes, which is determined by the resources and speed of our cloud infrastructure. If the processing time exceeds three minutes, it often means that other users are currently occupying the relevant facilities. You can try other models temporarily, or come back later. Have fun:)
    """,disabled = True, label_visibility="collapsed")
selected_model = st.selectbox("choose your model：", list(MODELS.keys()))

API_URL = MODELS[selected_model]
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def text_to_image(text):
    response = query({
        "inputs": text,
        "options": {
            "wait_for_model": True
        }
    })
    try:
        image = Image.open(io.BytesIO(response))
        return image
    except IOError:
        st.error("Can not generate api, please check your input")
        st.write("Calling API：")
        st.write(response)
        return None
    
c1,c2 = st.columns((1,2))

with c1:
    input_text = st.text_area("Input your prompt for image generation","Astronaut riding a horse",height=450,max_chars=150, help="Please enter ctrl+enter to apply")

with c2: 
    if input_text:
        st.caption("The generated image：")
        input_text += ". asim style."
        with st.spinner("Generally, the processing time for a single image ranges from a few seconds to two or three minutes."):
            generated_image = text_to_image(input_text)
        if generated_image is not None:
            st.image(generated_image, use_column_width=True)
            img_data = io.BytesIO()
            generated_image.save(img_data, format="PNG")
            img_data.seek(0)
            st.download_button(
            label="download your image",
            data=img_data,
            file_name="generated_image.png",
            mime="image/png",
            )
        else:
            st.write("Can not generate image because of some errors")
    else:
        st.write("write your description")
