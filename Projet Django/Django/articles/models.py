from django.db import models

# Create your models here.
class Article(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.FloatField()
    note = models.PositiveSmallIntegerField()
    img = models.ImageField(upload_to="static/images/articles/")
    description = models.CharField(max_length=500)