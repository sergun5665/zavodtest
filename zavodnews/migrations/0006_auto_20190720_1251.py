# Generated by Django 2.2.2 on 2019-07-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavodnews', '0005_auto_20190720_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allnews',
            name='image_news',
            field=models.ImageField(blank=True, null=True, upload_to='static/', verbose_name='Изображение'),
        ),
    ]