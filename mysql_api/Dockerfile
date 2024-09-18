FROM python:3.9.16-slim-buster
WORKDIR /api
COPY . .
RUN pip install fastapi uvicorn
RUN pip install mysql-connector-python
EXPOSE 5000
CMD [ "uvicorn","main:app" ,"--host","0.0.0.0","--port","8000"]