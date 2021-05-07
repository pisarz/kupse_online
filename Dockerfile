FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Kupse/requirements.txt /code/
RUN pip install -r requirements.txt
COPY Kupse/entry.sh /entry.sh
COPY Kupse/script.py /script.py
RUN chmod +x /entry.sh
RUN chmod +x /script.py 
COPY Kupse/ /code/
ENTRYPOINT [ "/entry.sh" ]