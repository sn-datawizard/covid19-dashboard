FROM python:3.8-bullseye

RUN apt update -y
RUN apt install -y python3-pip

RUN pip3 install pandas
RUN pip3 install sqlalchemy
RUN pip3 install mysql-connector-python
RUN pip3 install fsspec
RUN pip3 install gcsfs

WORKDIR /app

ADD app.py /app
ADD sns-covid-gcp-b6475c6924f9.json /app

CMD ["python3", "./app.py"]