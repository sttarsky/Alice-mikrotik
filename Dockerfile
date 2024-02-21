FROM python:3.12.2-slim-bookworm as base

RUN mkdir /svc
COPY . /svc
WORKDIR /svc

#RUN apk update && apk add make python3-dev gcc libc-dev libffi-dev openssl-dev musl-dev cargo

RUN pip wheel . --wheel-dir=/svc/wheels

FROM python:3.12.2-slim-bookworm

COPY --from=base /svc /svc

WORKDIR /svc

RUN pip install --no-index --find-links=/svc/wheels -r requirement.txt

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--ssl-keyfile=./cert/ECC-privkey.pem", "--ssl-certfile=./ECC-cert.pem", "--reload"]
