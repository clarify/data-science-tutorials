FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt clarify-credentials.json app.py ./

RUN pip3 install -r requirements.txt

CMD gunicorn --workers 1 --threads 8 --timeout 0 app:app