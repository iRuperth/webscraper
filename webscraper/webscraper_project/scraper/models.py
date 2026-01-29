from django.db import models

class ScrapedData(models.Model):
    text = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    author_url = models.URLField(null=True, blank=True)
    page_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text or 'No text'} - {self.author or 'Unknown'}"
