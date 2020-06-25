FROM python:3.7-alpine

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

WORKDIR /code

ADD . /code

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile