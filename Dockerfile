FROM python:3.10.13-alpine3.17 as base

RUN mkdir /svc
COPY . /svc
WORKDIR /svc

RUN apk update && apk add make python3-dev gcc libc-dev libffi-dev openssl-dev musl-dev cargo    

RUN pip wheel . --wheel-dir=/svc/wheels

FROM python:3.10.13-alpine3.17

COPY --from=base /svc /svc

WORKDIR /svc

RUN pip install --no-index --find-links=/svc/wheels -r requirement.txt

ENTRYPOINT ["python", "app.py"]
