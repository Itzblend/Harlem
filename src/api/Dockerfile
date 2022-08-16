# microservice Dockerfile

FROM python:3.10.0-slim

WORKDIR /src/api
COPY . /src

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

EXPOSE 9999

CMD ["python3", "api.py"]