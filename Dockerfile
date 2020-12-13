FROM python:3.7-buster

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pandas

COPY ./scripts/* /usr/local/bin/
COPY . /app
WORKDIR /app

# The http port
EXPOSE 4242

CMD ls

CMD ["/.venv/Scripts/python.exe", "manage.py --dev run"]
