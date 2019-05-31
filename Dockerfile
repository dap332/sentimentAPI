FROM python:3.7
RUN apt-get update -y

COPY ./app/* .
RUN pip3 install keras
RUN pip3 install tensorflow
RUN pip3 install flask
EXPOSE 8080
CMD python3 index.py