import os
from slugify import slugify
from base.forms import ContactForm
from django.core.mail import send_mail

# Funções utilitárias que serão utilizadas em vários módulos

def envia_mensagem(request):
    assunto = 'Contato - Sustanaible Fun'
    mensagem = 'De: ' + request.POST.get('nome') + '\n' +\
        'Telefone: ' + request.POST.get('telefone') + '\n' +\
        'Mensagem: ' + request.POST.get('mensagem')
    email = request.POST.get('email')
    para = ['rodrigo.pereira@isemear.org.br']
    send_mail(
        assunto,
        mensagem,
        email,
        para,
        fail_silently=False)

def cria_forms():
    return ContactForm(None)

def custom_errors(nome, campo):
    "Mensagens de erro customizadas para serem utilizadas em formulários diversos."
    try:
        nome_campo = campo.label
    except (ValueError, AttributeError):
        nome_campo = nome
    return {
        'unique': f"Já existe um cadastro de '{nome_campo}' com o valor informado",
        'invalid': f"Campo '{nome_campo}' com valor inválido",
        'required': f"Campo '{nome_campo}' é obrigatório",
        'max_value': f"Campo '{nome_campo}' não deve possuir valor maior que %(limit_value)d",
        'min_value': f"Campo '{nome_campo}' não deve possuir valor menor que %(limit_value)d",
        'max_length': f"Campo '{nome_campo}' deve possuir, no máximo, %(limit_value)d caracteres.",
        'min_length': f"Campo '{nome_campo}' deve possuir, no mínimo, %(limit_value)d caracteres.",
        'apenas_letras': f"Campo '{nome_campo}' só aceita letras",
        'apenas_numeros': f"Campo '{nome_campo}' só aceita valores numéricos",
        'alpha_numerico': f"Campo '{nome_campo}' só aceita valores alpha-numéricos",
    }

def string_to_path(string):
    "Transforma uma string qualquer em uma string adequada para ser utilizada em url's"
    return slugify(str.lower(string))

def generate_object_slug(_model, string):
    """Retorna o slug de um objeto baseado na string passada. Caso já exista o
    slug dentre os objetos do modelo informado, concatena um numeral ao slug."""
    slug = string_to_path(string)
    counter = 1
    temp = slug
    while _model.objects.filter(slug=temp).exists():
        temp = slug + str(counter)
        counter += 1
        if counter > 999 and slug != 'none':
            slug = 'none'
            temp = slug
            counter = 1
    return temp

def object_file_path(instance, filename):
    "Retorna o caminho correto para salvar um arquivo associado à uma instância de um objeto baseado no seu slug"
    slug = string_to_path(instance.slug)
    # Se o slug for vazio retorna usa o gerador de slug a partir do campo 'nome', assume-se que o campo 'nome' existe no objeto
    if slug == '':
        slug = generate_object_slug(instance.__class__, instance.nome)
    # Se instância estiver sendo criada e o slug já existir usa o gerador de slug a partir do slug atual
    # pylint: disable=protected-access
    if instance._state.adding and instance.__class__.objects.filter(slug=slug).exists():
        slug = generate_object_slug(instance.__class__, slug)
    return os.path.join(str(instance.__class__._meta.verbose_name_plural), slug, filename)

def trim(string):
    """Remove espaços em excesso à esquerda e à direita de um objeto caso ele
    possua os métodos necessários, caso contrário retorna o próprio objeto."""
    lstrip = getattr(string, "lstrip", None)
    rstrip = getattr(string, "rstrip", None)
    if callable(lstrip) and callable(rstrip):
        return string.lstrip().rstrip()
    return string

def rawToList(rawquery):
    """Transforma uma rawquery (query literal) em uma lista de dicionarios com os
    valores de seus campos. Útil para transformação de querys complexas em listas."""
    rows = list()
    for row in rawquery:
        dic = {}
        for method_name in rawquery.columns:
            dic[method_name] = getattr(row, method_name)
        rows.append(dic)
    return rows

def queryToDict(query, campo):
    """Transforma uma query em um dicionário, sendo sua chave o valor do campo informado na
    chamada da função e seu valor o dicionário formado pelos valores dos outros campos"""
    dic = {}
    query_vals = query.values()
    for row in query_vals:
        nome = row.get(campo, '')
        if nome != '':
            row.pop(campo, None)
            dic[nome] = row
    return dic
