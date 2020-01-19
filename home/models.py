from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    pub_date = models.DateTimeField('Date: ')
    article = models.CharField(max_length=200)
    content = models.TextField(default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.article

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)