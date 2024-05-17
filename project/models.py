# models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics', blank=True, null=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
