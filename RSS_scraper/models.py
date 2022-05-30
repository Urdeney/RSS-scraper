from django.db import models
from abc import ABC

# Create your models here.


class Article(ABC):
    date: models.DateTimeField
    link: models.CharField
    title: models.CharField
    description: models.TextField


class SfeduArticle(models.Model, Article):
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(null=True)
    title = models.CharField(null=True)
    description = models.TextField(null=True)

