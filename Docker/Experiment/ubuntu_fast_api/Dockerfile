FROM python:3.10.20-alpine3.22
WORKDIR /app
COPY . .
RUN  pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python","main.py" ]