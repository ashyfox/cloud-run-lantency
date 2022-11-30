FROM ubuntu:20.04
FROM python:3.9
WORKDIR ./
COPY . .

RUN apt-get update -y
RUN apt-get update; apt-get install curl
RUN mkdir ./app
ADD ./ ./app

WORKDIR ./app
ENTRYPOINT [ "python3" ]
CMD ["./latency.py"]
