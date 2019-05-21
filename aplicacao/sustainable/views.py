from django.shortcuts import render

# Create your views here.
def index(request):
    exemplo_de_variavel_no_template = "Essa String do botão veio da função 'index' sustainable/views.py"

    context = {
        "texto_qualquer": exemplo_de_variavel_no_template
    }
    return render(request, 'index.html', context)


def pagina(request):
    context = {
        "brendon": "Brendon é um cara legal!"
    }
    return render(request, 'pagina.html', context)

def workshop(request):
    context = {
    }
    return render(request, 'workshop.html', context)

def secformscontato(request):
    context = {}
    return render(request,'secformscontato.html',context)


def slider(request):
    context = {}
    return render(request, 'slider.html', context)
