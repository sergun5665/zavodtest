# Generated by Django 2.2.2 on 2019-07-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavodnews', '0009_auto_20190720_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allnews',
            name='image_news',
            field=models.ImageField(blank=True, null=True, upload_to='zavod/zavodnews/static/img', verbose_name='Изображение'),
        ),
    ]