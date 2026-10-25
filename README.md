# SD_SAM_APP

A Streamlit text-to-image demonstration using Hugging Face inference.

## Runtime configuration

Install the application's dependencies (`streamlit`, `requests`, and `Pillow`) in your Python environment, then run from the repository root:

```sh
streamlit run main.py
```

Set `HF_TOKEN` in the server's environment **before** launching Streamlit. Use your hosting provider's secret/environment-variable configuration, or a local secret manager. Use a new token with only the permissions required by your inference models.

Do not paste a token into source code, issues, commits, logs, or chat. Avoid commands containing literal tokens, which may remain in shell history. The app stops before an API request if `HF_TOKEN` is missing or blank.

The app reads `os.environ["HF_TOKEN"]`; it does not load `.env` files automatically. Local `.env` and Streamlit secrets files are ignored as a safety precaution, not as a configuration loader.

## Credential incident follow-up

A previously embedded credential was removed from the current source. **Removing it from source does not revoke it or remove it from Git history, forks, caches, or existing deployments.** Its owner must revoke the exposed token in Hugging Face settings and provision a fresh token if the application is still used. Do not reuse the exposed token.

Existing deployed instances may retain old code or configuration until their owner explicitly updates/restarts them. This repository change does not confirm token revocation or deployment updates.
