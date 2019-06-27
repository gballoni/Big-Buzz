from .models import Workshop, Mensagem
from util.funcoes import cria_forms, get_client_ip
from util.constantes import testimonials as _testimonials, reasons
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail

# Create your views here.

def envia_mensagem(request):
    _assunto = 'Contato - Sustanaible Fun'
    _ip = get_client_ip(request)
    _nome = request.POST.get('nome')
    _telefone = request.POST.get('telefone')
    _mensagem = request.POST.get('mensagem')
    _email = request.POST.get('email')
    _para = ['rodrigo.pereira@isemear.org.br']
    m = Mensagem(
        assunto=_assunto,
        nome=_nome,
        telefone=_telefone,
        email=_email,
        para=_para,
        ip=_ip,
        mensagem=_mensagem)
    m.save()
    mensagem = 'De: ' + _nome + '\n' +\
        'Telefone: ' + _telefone + '\n' +\
        'Mensagem: ' + _mensagem + '\n' +\
        'IP:' + _ip
    send_mail(
        _assunto,
        mensagem,
        _email,
        _para,
        fail_silently=False)

def index(request):
    context = {
        'reasons': reasons,
        'testimonials': _testimonials,
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
