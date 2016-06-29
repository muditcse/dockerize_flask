FROM python:2.7.11
MAINTAINER Smrati <smrati.katiyar@gmail.com>
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
COPY . /apps/hello/
WORKDIR /apps/hello/
EXPOSE 8000
CMD ["uwsgi", "--ini", "hello.ini"]