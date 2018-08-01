FROM ubuntu:latest
RUN apt-get update -y
RUN apt install python3-pip -y
COPY . ./app
WORKDIR ./app
RUN pip3 install keras
RUN pip3 install tensorflow
RUN pip3 install flask
CMD python3 index.py