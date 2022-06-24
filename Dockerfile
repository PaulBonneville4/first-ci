FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3 -y

WORKDIR /home

COPY . .

CMD ["python3", "main.py"]