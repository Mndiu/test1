FROM python:latest
LABEL maintainer="SAM"
WORKDIR /usr/app/src
RUN pip install flask
COPY api.py ./
EXPOSE 8015
CMD ["python","api.py"]
