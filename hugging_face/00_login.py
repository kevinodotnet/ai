#!/opt/conda/bin/python

#
# Use this script to log into HuggingFace (via browser url provided).
# The call to login() then saves the pasted access tokens to the location HF libraries expect to find it
#
# Only required to access models that require authenticated requests
#

from huggingface_hub import hf_hub_download, login
login()

# Your token has been saved to /home/kevino/.cache/huggingface/token

