# Generated by Django 4.0.1 on 2022-02-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='Code/Projet Django/monprojet/chicks/'),
        ),
    ]