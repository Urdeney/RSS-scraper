from hashlib import md5
from computedfields.models import ComputedFieldsModel, computed
from django.db import models
from django.db.utils import IntegrityError

# Create your models here.


class Article(ComputedFieldsModel):
    id: int
    link: str = models.CharField(max_length=100)
    title: str = models.CharField(max_length=100)
    description: str = models.TextField(null=True)

    @computed(models.CharField(max_length=32, unique=True), depends=[('self', ['title'])])
    def hash(self) -> str:
        return md5(self.title.encode('utf8')).hexdigest()

    def __str__(self) -> str:
        return f"'{self.title}' ({self.id})"
    
    class Meta:
        abstract = True


class SfeduArticle(Article):
    date = models.DateTimeField(auto_now_add=True)
    imageurl: str = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            pass

