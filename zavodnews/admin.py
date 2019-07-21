from django.contrib import admin

from zavodnews.models import Allnews, Keywords

admin.site.register(Allnews)
admin.site.register(Keywords)

# class GalleryInline(admin.TabularInline):
#     fk_name = 'news'
#     model = Gallery
#
#
# @admin.register(Allnews)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [GalleryInline]
