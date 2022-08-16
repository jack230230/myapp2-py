FROM python:3.10-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--workers=4", "-b", "0.0.0.0:5000", "app:app"]
