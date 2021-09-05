FROM python:3
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY update_team.py /code/update_team.py
COPY main.py /code/main.py

WORKDIR /code/

ENV EMAIL "kshanbhag231@gmail.com"
ENV PASSWORD "leomessi*01"
ENV USER_ID "1462218"

