# Generated by Django 2.2.2 on 2019-07-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavodnews', '0010_auto_20190720_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eximg', models.ImageField(blank=True, null=True, upload_to='zavod/zavodnews/static/img/')),
            ],
        ),
        migrations.AlterField(
            model_name='allnews',
            name='image_news',
            field=models.ImageField(blank=True, null=True, upload_to='zavod/zavodnews/static/img/', verbose_name='Изображение'),
        ),
    ]