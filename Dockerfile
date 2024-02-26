FROM python:3.12.2-slim-bookworm as base

RUN mkdir /svc
COPY . /svc
WORKDIR /svc

RUN apt update && apt install -y make python3-dev gcc libc-dev libffi-dev musl-dev cargo

RUN pip wheel . --wheel-dir=/svc/wheels

FROM python:3.12.2-slim-bookworm

COPY --from=base /svc /svc

ENV SSL_KEY=""
ENV SSL_SERT=""
WORKDIR /svc
RUN mkdir cert && apt update && apt install -y openssh-client
RUN pip install --no-index --find-links=/svc/wheels -r requirements.txt
COPY *.key cert/secret-key.key
COPY *.pem cert/secret-cert.pem
EXPOSE 5000

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 5000 --ssl-keyfile=./cert/secret-key.key --ssl-certfile=./cert/secret-cert.pem --reload
