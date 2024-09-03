FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# The port where the flask application will run
EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
