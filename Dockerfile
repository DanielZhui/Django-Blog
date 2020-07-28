FROM python:3.7-alpine

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

WORKDIR /code

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

ADD . /code
