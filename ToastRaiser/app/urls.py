
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaprincipal, name='paginaprincipal'),
    path('about/', views.about, name='about'),
    path('download/', views.download, name='download')
]
