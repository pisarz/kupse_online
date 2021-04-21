FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Kupse/requirements.txt /code/
RUN pip install -r requirements.txt
COPY Kupse/ /code/