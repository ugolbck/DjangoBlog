from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    body = models.CharField(max_length=10000)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class CV(models.Model):
    description = models.CharField(max_length=30)
    curriculum = models.FileField()

    def __str__(self):
        return self.description

