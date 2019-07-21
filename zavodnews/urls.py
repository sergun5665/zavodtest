from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('allnews/', views.allnews.as_view()),
    path('news/', views.news.as_view()),
    path('tagnews/', views.tagnews),

]
