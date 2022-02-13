from django.db import models

# Create your models here.
class Mails(models.Model):
    mail=models.CharField(max_length=1000)