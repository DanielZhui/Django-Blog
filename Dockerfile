FROM python:3.7-alpine

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

WORKDIR /code

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install pipenv -i https://pypi.douban.com/simple

COPY Pipfile /code/Pipfile

COPY Pipfile.lock /code/Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

ADD . /code
