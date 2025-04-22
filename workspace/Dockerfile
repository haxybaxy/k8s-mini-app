FROM python:3.10-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY clone_and_sleep.py /app/clone_and_sleep.py
WORKDIR /app
CMD ["python", "clone_and_sleep.py"]
