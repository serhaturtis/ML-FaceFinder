FROM ubuntu:focal

EXPOSE 6006

RUN mkdir -p /workspace

VOLUME  /workspace

RUN	apt-get update \
	&& apt-get upgrade -y \
	&& DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y --no-install-recommends software-properties-common build-essential

RUN	add-apt-repository -y ppa:deadsnakes \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y --no-install-recommends python3.8-venv python3.8-dev python3-pip cmake\
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& :

RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH

# OpenCV
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install opencv-contrib-python-headless

# dlib
RUN pip3 install dlib

# Face recognition
RUN pip3 install face_recognition

