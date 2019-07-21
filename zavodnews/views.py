from django.shortcuts import render
from django.views.generic import TemplateView

from zavodnews.models import Allnews, Keywords


def index(request):
    return render(request, 'zavodnews/index.html')


class allnews(TemplateView):
    template_name = 'zavodnews/allnews.html'



    def get_context_data(self, **kwargs):
        records = Allnews.objects.all()
        tags = Keywords.objects.all()

        context = dict(records=records,tags=tags)

        return context



# def news(request):
#     return render(request, 'zavodnews/news.html')
class news(TemplateView):
    template_name = 'zavodnews/news.html'



    def get_context_data(self, **kwargs):
        records = Allnews.objects.all()
        tags = Allnews.objects.all()


        context = dict(records=records,tags=tags)

        return context


def tagnews(request):
    return render(request, 'zavodnews/tagnews.html')
