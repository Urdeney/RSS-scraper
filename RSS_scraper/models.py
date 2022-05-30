from django.db import models

# Create your models here.


class Article:
    date: models.DateTimeField
    link: models.CharField
    title: models.CharField
    description: models.TextField


class SfeduArticle(models.Model, Article):
    date = models.DateTimeField(auto_now_add=True)
    imageurl = models.CharField(null=True, max_length=100)
    link = models.CharField(null=True, max_length=100)
    title = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True)

