FROM python:3.10-slim

RUN apt-get update \
    #     && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8003

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]