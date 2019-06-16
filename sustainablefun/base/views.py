from django.shortcuts import get_object_or_404, render
from .models import Workshop
from django.core.mail import send_mail

# Create your views here.

def index(request):
    texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'\
             ' Nullam enim enim, semper sit amet maximus vitae, hendrerit sed elit.'
    cardinais = ['First', 'Second', 'Third']
    icones = ['images/006-graduate.png', 'images/018-elearning.png', 'images/010-creative.png']
    reasons = [{'icone': icone, 'titulo': '{} reason:'.format(card), 'descricao': texto}\
               for icone, card in zip(icones, cardinais)\
              ]
              
    context = {
        'reasons': reasons
    }

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['emailcontato']
        send_mail('Contato - Sustanaible Fun',
                  message,
                  email,
                  ['rodrigo.pereira@isemear.org.br'],
                  fail_silently=False)
    return render(request, 'conteudo/index.html', context)

def workshops(request):
    workshops = [{'titulo': 'Titulo do Workshop {}'.format(i),\
                  'descricao': 'Descrição do Workshop {}'.format(i)\
                 }\
                 for i in range(1, 9)\
                ]

    context = {
        'workshops': workshops
    }

    return render(request, 'conteudo/workshops.html', context)

def mostra_workshop(request, workshop_slug):
    "Função que retorna o conteudo da página de um workshop a partir de seu slug"
    workshop = get_object_or_404(Workshop, slug=workshop_slug)
    atividades = workshop.atividade_set.filter(publicado=True).values()
    context = {
        'workshop': workshop,
        'atividades': atividades,
    }

    return render(request, 'conteudo/mostra_workshop.html', context)

def secformscontato(request):
    context = {}
    return render(request, 'partials/_contatosimples.html', context)

def slider(request):
    context = {}
    return render(request, 'conteudo/slider.html', context)

def aboutus(request):
    context = {}
    return render(request,'conteudo/aboutus.html', context)