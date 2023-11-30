FROM python:3.10.13-alpine3.18
COPY . ./app
WORKDIR /app
RUN pip install -r requirement.txt
ENTRYPOINT ["python", "app.py"]
