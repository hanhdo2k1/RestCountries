FROM python:3.9.16-slim-buster
ENV API_URL=http://mysql-api-container:8000
WORKDIR /api
COPY . .
RUN pip install fastapi uvicorn
RUN pip install requests pydantic
EXPOSE 5000
CMD [ "uvicorn","api_craw:app" ,"--host","0.0.0.0","--port","5000"]