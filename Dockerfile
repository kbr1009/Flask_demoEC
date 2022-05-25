FROM python:alpine

WORKDIR /app

COPY ./app /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "server:app", "-b", "0.0.0.0:80"]
