echo "Starting cron..."
cron

echo "Starting Django..."
cd /app/webscraper
python manage.py runserver 0.0.0.0:8000

echo "Tailing logs..."
tail -f /var/log/cron.log