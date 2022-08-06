FROM python:3.8

WORKDIR /assignment

# COPY requirnments.txt .
ADD . /assignment

RUN pip install -r requirements.txt 

# COPY ./app ./app

CMD ["python", "app.py"]
