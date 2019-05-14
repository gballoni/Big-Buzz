from django.urls import path

from . import views

# Caminhos da nossa aplicação que referenciam uma função em views.py
urlpatterns = [
    path('', views.index, name='index'),
]