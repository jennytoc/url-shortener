from django.db import models

class Link(models.Model):
    original_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)

    def __str__(self):
        return f"Original URL: {self.original_url}, Short URL: {self.short_url}"