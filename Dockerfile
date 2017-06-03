FROM python:2.7

EXPOSE 5000


RUN pip install --upgrade pip

WORKDIR /home

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora