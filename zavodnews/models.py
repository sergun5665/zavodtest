from django.db import models


class Keywords(models.Model):
    name = models.CharField(max_length=360, unique=True, verbose_name='теги')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Allnews(models.Model):
    title = models.CharField(max_length=360)
    text_news = models.CharField(max_length=360)
    image_news = models.ImageField(null=True, blank=True, upload_to="zavodnews/static/img/",
                                   verbose_name=u'Изображение', )
    keywords = models.ManyToManyField(Keywords, related_name="keywords", related_query_name="keyword",
                                      verbose_name='теги')

    def __str__(self):
        return 'Новость: Загаловок--({})'.format(self.title)

    def bit(self):
        if self.image_news:
            return u'<img src="%s"/>' % self.image_news
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True

# class Gallery(models.Model):
#     image = models.ImageField(upload_to='/img')
#     news = models.ForeignKey(Allnews, on_delete=models.CASCADE, related_name='images')
