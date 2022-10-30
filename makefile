build:
	conda env create -f environment.yaml
	conda init bash

install-extra-deps:
	conda install -y -n ldm  --update-deps --force-reinstall \
		ipykernel \
		ipywidgets

download-model:
	mkdir -p ./models/ldm/stable-diffusion-v1
	python scripts/download_txt2img_model.py

run:
	python scripts/txt2img.py \
		--plms \
		--prompt "art nuveau style, woman pose study, flowers, 4k, high detail" 
