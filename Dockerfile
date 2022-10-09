FROM archlinux:base-devel-20221002.0.91257

EXPOSE 14366

# Setting the working directory to /app
WORKDIR /app

# Install requirements
RUN pacman -Sy
RUN pacman -S --needed --noconfirm git python python-pip p7zip micro

# Install requirements for flaskServer.py
RUN pip install flask flask_cors sentencepiece

# Install fairseq
RUN git clone -b v0.12.2 https://github.com/facebookresearch/fairseq.git

# Install fairseq requirements
WORKDIR /app/fairseq
RUN pip install --editable ./

# Copy flask.py and translation files
COPY flaskServer.py /app/fairseq
COPY japaneseModel /app/fairseq/japaneseModel
COPY spmModels /app/fairseq/spmModels

# Copy and extract pretrain
WORKDIR /tmp
COPY ./pretrain /tmp/
RUN 7z x -o/app/fairseq/japaneseModel big.pretrain.7z.001

# Cleanup
RUN pacman -R --noconfirm git p7zip
RUN rm -rf /tmp/*

WORKDIR /app
CMD python ./fairseq/flaskServer.py

ARG IMAGE_SOURCE
#https://github.com/k8s-at-home/template-container-image
LABEL org.opencontainers.image.source $IMAGE_SOURCE
