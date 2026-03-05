FROM python:3.10.20-alpine3.22
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /app
ENTRYPOINT [ "python","main.py" ]