import json
from .models import Workshop
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail

# Create your views here.

def envia_mensagem(request):
    message = request.POST['mensagem']
    email = request.POST['email']
    send_mail(
        'Contato - Sustanaible Fun',
        message,
        email,
        ['rodrigo.pereira@isemear.org.br'],
        fail_silently=False)

def cria_forms():
    return ContactForm(None)

testimonials = [
    {'nome': 'Nome aaaaaaaaaaa',
     'proficao': 'Profição 1',
     'numero': 0,
     'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(30).jpg',
     'depoimento': 'Lorem ipsum dolccccccccccor sit amet, consectetur adipisicing elit. Quod eos id officiis hic  1'
    },
    {'nome': 'Nome sssssssssss',
     'proficao': 'Profição ddddddddd1',
     'numero': 1,
     'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(31).jpg',
     'depoimento': 'Lorem ipsum dolosssssssssssr sit amet, consectetur adipisicing elit. Quod eos id officiis hic  1'
    },
    {'nome': 'Nome ddddddddddd',
     'proficao': 'Profição wwwwwwww1',
     'numero': 2,
     'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(32).jpg',
     'depoimento': 'Lorem ipsum dolmmmmmmmmmmor sit amet, consectetur adipisicing elit. Quod eos id officiis hic  1'
    }
]

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'\
        ' Nullam enim enim, semper sit amet maximus vitae, hendrerit sed elit.'
cardinais = ['First', 'Second', 'Third']
icones = ['images/006-graduate.png', 'images/018-elearning.png', 'images/010-creative.png']
reasons = [
    {'icone': icone, 'titulo': '{} reason:'.format(card), 'descricao': texto}\
    for icone, card in zip(icones, cardinais)\
]

def index(request):
    context = {
        'reasons': reasons,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'conteudo/index.html', context)

def workshops(request):
    workshops = Workshop.objects.all().order_by('nome')

    context = {
        'workshops': workshops,
        'form': contact_form
    }
    return render(request, 'conteudo/workshops.html', context)

def mostra_workshop(request, workshop_slug):
    "Função que retorna o conteudo da página de um workshop a partir de seu slug"
    workshop = get_object_or_404(Workshop, slug=workshop_slug)
    atividades = workshop.atividade_set.filter(publicado=True).values().order_by('numero')

    context = {
        'workshop': workshop,
        'atividades': atividades,
        'form': contact_form
    }
    return render(request, 'conteudo/mostra_workshop.html', context)

def secformscontato(request):
    if request.method == 'POST':
        context = {
            "nome":contact_form.nome,
            "email":contact_form.email,
            "mensagem":contact_form.mensagem,
            "form":contact_form
        }
        envia_mensagem(request)
        return HttpResponse(json.dumps({'msg': 'Sua mensagem foi enviada com sucesso!'}), mimetype='application/json')
    return index(request)

def slider(request):
    context = {}
    return render(request, 'conteudo/slider.html', context)

def aboutus(request):
    context = {
        "form":contact_form
    }
    return render(request,'conteudo/aboutus.html', context)

def testimonials(request):
    context = {
        'testimonials': testimonials
    }
    return render(request,'conteudo/testimonials.html', context)
