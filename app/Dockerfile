FROM python:3.6

# EXPOSE 5000
EXPOSE 80
WORKDIR /home/app

COPY requirements.txt /home/app
RUN pip install -r requirements.txt

COPY app.py /home/app
CMD ["gunicorn", "-w", "3", "-t", "60", "-b", "0.0.0.0:80", "app:app"]