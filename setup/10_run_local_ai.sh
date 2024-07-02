#!/bin/bash

docker run \
  --gpus all \
	-p 8080:8080 \
	--name local-ai \
	-ti -v $PWD/models:/build/models \
  localai/localai:latest-aio-gpu-nvidia-cuda-12

