#! /bin/bash

cd ..
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
export PATH="$(echo ${PWD##*/})/miniconda3/bin:$PATH" >>~/.bash_profile
conda env create -f DSReq.yml -n ds_env
