FROM python:3.8
LABEL maintainer "Nelson Low"
COPY requirements.txt /tmp/
COPY . /flaskapp
WORKDIR "/flaskapp"
RUN pip3 install -r /tmp/requirements.txt

# EXPOSE 8050

ENTRYPOINT [ "python" ]
CMD [ "wsgi.py" ]
