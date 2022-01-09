FROM python:3.10.1-buster

ENV PYTHONUNBUFFERED=1

ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/local/app
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app"]
