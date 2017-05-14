FROM hypriot/rpi-python:2.7

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python2", "main.py"]





