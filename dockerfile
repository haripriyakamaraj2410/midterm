FROM python:3.11-slim
WORKDIR /app
COPY factorial.py .
CMD ["python", "factorial.py"]