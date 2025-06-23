from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=100, blank=True)
    published_date = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True)

    def __str__(self):
        return self.title

