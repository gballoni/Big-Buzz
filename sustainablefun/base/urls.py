from django.urls import path
from . import views

# Um namespace para que as urls sejam chamadas facilmente.
app_name = 'base'

# Caminhos da nossa aplicação que referenciam uma função em views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('pagina', views.pagina, name='pagina'),
    path('workshops/<workshop_slug>', views.mostra_workshop, name='mostra_workshop'),
]
