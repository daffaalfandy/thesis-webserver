FROM python:3.6

EXPOSE 5000
WORKDIR /home/app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt

COPY app.py /home/app
CMD ["python", "app.py"]