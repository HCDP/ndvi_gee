FROM python:3.10

RUN mkdir /data
RUN mkdir /app
RUN mkdir /certs

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]
