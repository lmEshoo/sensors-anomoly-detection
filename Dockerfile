FROM resin/rpi-raspbian:stretch
#Original version was inherated from: 
#https://github.com/lisaong/stackup-workshops/blob/master/pi-pytorch/docker/Dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev python3-pip python3-setuptools \
        python3-numpy python3-sklearn python3-pandas \
        libopenblas-dev

RUN  apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install torch-raspi
