from django.shortcuts import render


# Create your views here.
def index(request):
    exemplo_de_variavel_no_template = "Essa String do botão veio da função 'index' sustainable/views.py"

    context = {
        "texto_qualquer": exemplo_de_variavel_no_template
    }
    return render(request, 'index.html', context)
