from django.core.management.base import BaseCommand
from scraper.services.scrape import scrape_website
from scraper.models import ScrapedData

class Command(BaseCommand):
    help = "Run the web scraper"

    def handle(self, *args, **kwargs):
        data = scrape_website()
        print("Scraped Data:", data)
        for item in data:
            ScrapedData.objects.create(
                text=item["text"],
                author=item["author"],
                tags=item["tags"],
                author_url=item["author_url"],
                page_url=item["page_url"],
            )
        self.stdout.write(self.style.SUCCESS("Scraping completed!"))
