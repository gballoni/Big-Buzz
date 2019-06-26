from .models import Workshop
from util.funcoes import envia_mensagem, cria_forms
from util.constantes import testimonials as _testimonials, reasons
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    context = {
        'reasons': reasons,
        'testimonials': testimonials,
        'form': cria_forms()
    }
    return render(request, 'conteudo/index.html', context)

def workshops(request):
    workshops = Workshop.objects.all().order_by('nome')

    context = {
        'workshops': workshops,
        'form': cria_forms()
    }
    return render(request, 'conteudo/workshops.html', context)

def mostra_workshop(request, workshop_slug):
    "Função que retorna o conteudo da página de um workshop a partir de seu slug"
    workshop = get_object_or_404(Workshop, slug=workshop_slug)
    atividades = workshop.atividade_set.filter(publicado=True).values().order_by('numero')

    context = {
        'workshop': workshop,
        'atividades': atividades,
        'form': cria_forms()
    }
    return render(request, 'conteudo/mostra_workshop.html', context)

def secformscontato(request):
    if request.method == 'POST':
        envia_mensagem(request)
        return JsonResponse({'resposta': 'Sua mensagem foi enviada com sucesso!'})
    return index(request)

def slider(request):
    context = {}
    return render(request, 'conteudo/slider.html', context)

def aboutus(request):
    context = {
        "form":cria_forms()
    }
    return render(request,'conteudo/aboutus.html', context)

def testimonials(request):
    context = {
        'testimonials': _testimonials
    }
    return render(request,'conteudo/testimonials.html', context)
