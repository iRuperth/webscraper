FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    cron \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cron setup
RUN mkdir -p /var/run /var/log && \
    touch /var/log/cron.log

COPY cronfile /etc/cron.d/scrape-cron
RUN chmod 0644 /etc/cron.d/scrape-cron && \
    crontab /etc/cron.d/scrape-cron

# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["/entrypoint.sh"]
