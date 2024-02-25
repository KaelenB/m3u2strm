FROM ubuntu:latest

# install git and python
RUN apt-get update && apt-get install -y git python3 python3-pip

# install pip wget
RUN pip3 install wget

ARG username=$GIT_USERNAME
ARG password=$GIT_PASSWORD
# clone the repository
RUN git clone https://github.com/KaelenB/m3u2strm.git

WORKDIR /m3u2strm

# create m3u directory
RUN mkdir m3u

# entrypoing main.py
ENTRYPOINT ["python3", "main.py"]


