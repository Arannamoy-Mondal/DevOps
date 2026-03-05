FROM python:3.10.20-alpine3.22
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python","main.py" ]