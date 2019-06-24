from django.shortcuts import get_object_or_404, render
from .models import Workshop
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

def index(request):
    contact_form = cria_forms()
    texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'\
            ' Nullam enim enim, semper sit amet maximus vitae, hendrerit sed elit.'
    cardinais = ['First', 'Second', 'Third']
    icones = ['images/006-graduate.png', 'images/018-elearning.png', 'images/010-creative.png']
    reasons = [
        {'icone': icone, 'titulo': '{} reason:'.format(card), 'descricao': texto}\
        for icone, card in zip(icones, cardinais)\
    ]

    context = {
        'reasons': reasons,
        'form':contact_form
    }

    if request.method == 'POST':
        envia_mensagem(request)
    return render(request, 'conteudo/index.html', context)

def cria_forms():
    return ContactForm(None)

def envia_mensagem(request):
    message = request.POST['mensagem']
    email = request.POST['email']
    send_mail(
        'Contato - Sustanaible Fun',
        message,
        email,
        ['rodrigo.pereira@isemear.org.br'],
        fail_silently=False)

def workshops(request):
    contact_form = cria_forms()
    workshops = Workshop.objects.all()

    context = {
        'workshops': workshops,
        'form': contact_form
    }
    if request.method == 'POST':
        envia_mensagem(request)
    return render(request, 'conteudo/workshops.html', context)

def mostra_workshop(request, workshop_slug):
    contact_form = cria_forms()
    "Função que retorna o conteudo da página de um workshop a partir de seu slug"
    workshop = get_object_or_404(Workshop, slug=workshop_slug)
    atividades = workshop.atividade_set.filter(publicado=True).values()
    context = {
        'workshop': workshop,
        'atividades': atividades,
        'form': contact_form
    }
    if request.method == 'POST':
        envia_mensagem(request)
    return render(request, 'conteudo/mostra_workshop.html', context)

def secformscontato(request):
    contact_form = cria_forms()
    context = {
        "nome":contact_form.nome,
        "email":contact_form.email,
        "mensagem":contact_form.mensagem,
        "form":contact_form
    }
    if request.method == 'POST':
        envia_mensagem(request)
    return render(request, 'partials/_contatosimples.html', context)

def slider(request):
    context = {}
    return render(request, 'conteudo/slider.html', context)

def aboutus(request):
    contact_form = cria_forms()
    context = {
        'form':contact_form
    }
    if request.method == 'POST':
        envia_mensagem(request)
    return render(request,'conteudo/aboutus.html', context)
