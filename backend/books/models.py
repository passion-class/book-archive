from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=100, blank=True)
    published_date = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True)
    isbn = models.CharField(max_length=20, blank=True, default='unknown')
    publisher = models.CharField(max_length=100, blank=True, default="미상")

    def __str__(self):
        return self.title

