FROM python:3.11.0b3

COPY requirements-freeze.txt .
RUN pip install -r requirements-freeze.txt

RUN useradd -m app
COPY --chown=app src /app
COPY --chown=app speedtest /app
RUN chmod +x /app/speedtest
WORKDIR /app
USER app

CMD ["/app/serve.py"]
