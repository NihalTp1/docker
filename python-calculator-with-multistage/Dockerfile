
FROM python:3.9-slim AS builder
WORKDIR /app

COPY /APP/calculator.py .

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /app/calculator.py .
  
CMD ["python3", "calculator.py"]
