FROM python:3.8.5-slim

LABEL Name="Python Flask App" 

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install -r requirements.txt

COPY $srcDir .

EXPOSE 5000

CMD python main.py