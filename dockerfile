FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    cron \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/screenshots && chmod 777 /app/screenshots

COPY . .

# Cron setup
RUN mkdir -p /var/run /var/log && \
    touch /var/log/cron.log && chmod 666 /var/log/cron.log

COPY cronfile /etc/cron.d/scrape-cron
RUN chmod 0644 /etc/cron.d/scrape-cron

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/app/screenshots"]

EXPOSE 8000

CMD ["/entrypoint.sh"]
