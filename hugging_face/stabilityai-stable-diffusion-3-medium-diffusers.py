#!/opt/conda/bin/python

# Before running:
#   pip install diffusers
#   pip install sentencepiece

import torch
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained(
  "stabilityai/stable-diffusion-3-medium-diffusers", 
  torch_dtype=torch.float16
)

pipe.to('cuda')

while True:
  prompt = input("prompt> ")
  image = pipe(
    prompt=prompt,
    negative_prompt="",
    num_inference_steps=28,
    height=1024, width=1024,
    guidance_scale=7.0,
  ).images[0]
  image.save("sd3_generated_image.png")
