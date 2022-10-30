from huggingface_hub import hf_hub_url, hf_hub_download
import os

REPO_ID = "CompVis/stable-diffusion-v-1-4-original"
FILENAME = "sd-v1-4-full-ema.ckpt"

model_url = hf_hub_url(REPO_ID, FILENAME)
model_path = hf_hub_download(
    filename=FILENAME, repo_id=REPO_ID, use_auth_token=os.getenv("HF_ACCESS_TOKEN")
)

os.symlink(model_path, "./models/ldm/stable-diffusion-v1/model.ckpt")
