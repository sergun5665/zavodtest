# Generated by Django 2.2.2 on 2019-07-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavodnews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text_news', models.CharField(max_length=60)),
                ('tag_news', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='All_news',
        ),
    ]
