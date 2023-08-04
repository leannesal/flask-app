FROM python:3.9-slim-buster

LABEL Name="Python Flask App" Version=1.4.2

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install -r requirements.txt

COPY $srcDir .

EXPOSE 5000

CMD python main.py