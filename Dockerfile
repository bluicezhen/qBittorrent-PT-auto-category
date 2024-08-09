FROM python:3.11.9-alpine

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

USER 1000

CMD [ "python", "main.py" ]