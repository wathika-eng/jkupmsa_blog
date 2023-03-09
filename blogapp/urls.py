from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('<str:slug>', views.blog_detailView, name='blog_detail'),
]

