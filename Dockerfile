FROM python:3.7-stretch

ADD . /opt/httpmi
RUN pip install -U /opt/httpmi
RUN pip install uwsgi

CMD uwsgi --http 127.0.0.1:5000 \
          --wsgi httpmi.api \
          --callable app \
          --master \
          --http-workers 16
