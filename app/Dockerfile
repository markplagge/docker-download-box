ARG ARCH=
#FROM ${ARCH}ubuntu:21.10
FROM ${ARCH}python:alpine
ARG DEBIAN_FRONTEND=noninteractive

#RUN apt-get update -y && \
#    apt-get install --no-install-recommends -y python3-pip # python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./flask-reverse-proxy /app/flask-reverse-proxy/

#RUN pip install flask pyyaml pyaml yaml


ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]