from django.urls import path
from . import views

# Um namespace para que as urls sejam chamadas facilmente.
app_name = 'base'

# Caminhos da nossa aplicação que referenciam uma função em views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('workshops', views.workshops, name = 'workshops'),
    path('workshops/<workshop_slug>', views.mostra_workshop, name='mostra_workshop'),
    path('slider', views.slider, name='slider'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('infoform', views.secformscontato, name='cadastraformulario'),
]
