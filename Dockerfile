FROM python:3.9

RUN mkdir -p /opt/poll-api
WORKDIR /opt/poll-api
ADD . /opt/poll-api

RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["bash", "run.sh"]