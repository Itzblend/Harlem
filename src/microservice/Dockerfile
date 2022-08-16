# microservice Dockerfile

FROM python:3.10.0-slim

WORKDIR /src/microservice
COPY . /src

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]