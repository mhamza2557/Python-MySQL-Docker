FROM python:3.6

EXPOSE 5000

WORKDIR /application

COPY requirements.txt /application
RUN pip install -r requirements.txt

COPY app.py /application
CMD python app.py

