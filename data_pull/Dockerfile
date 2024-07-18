FROM python:3.10

RUN mkdir /data
RUN mkdir /app

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "fetch-ndvi.py"]