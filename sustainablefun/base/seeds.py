from .models import Workshop, Atividade

def add_workshop(**kwargs):
    n = kwargs.get('nome', None)
    s = kwargs.get('slug', None)
    p = kwargs.get('publicado', None)
    f = kwargs.get('imagem', None)
    t = kwargs.get('tempo_necessario', None)
    c = kwargs.get('conteudo', None)
    w = Workshop.objects.get_or_create(
        nome=n,
        slug=s,
        publicado=p,
        imagem=f,
        tempo_necessario=t,
        conteudo=c)
    return w

def add_atividade(workshop, numero, **kwargs):
    n = kwargs.get('nome', None)
    p = kwargs.get('publicado', None)
    t = kwargs.get('tempo_necessario', None)
    m = kwargs.get('material', None)
    d = kwargs.get('descricao', None)
    a = Atividade.objects.get_or_create(
        numero=numero,
        nome=n,
        workshop=workshop,
        publicado=p,
        tempo_necessario=t,
        material=m,
        descricao=d)
    return a

def add_work_atividade(numero, atividades):
    w = add_workshop(
        nome = 'Workshop 1./n Sustainability, what is the fuss all about?',
        slug = 'teste' + str(numero),
        publicado = True,
        imagem = 'workshops/teste' + str(numero) +'/workshop_teste0' + str(numero) + '.jpg',
        tempo_necessario = "50-60 min",
        conteudo = "<p> Teacher’s notes </p>")

    for i in range(atividades):
        add_atividade(
            w[0],
            i,
            nome = 'Atividade Teste' + str(i),
            publicado = True,
            tempo_necessario = str(120/atividades) + ' min',
            material = "<p>Url talvez?</p>",
            descricao = "Atividade de teste")

def populate():
    print('Populando Banco de Dados...')

    add_work_atividade(1, 4)
    add_work_atividade(2, 2)
    add_work_atividade(3, 6)
    add_work_atividade(4, 3)
    add_work_atividade(5, 1)
    add_work_atividade(6, 3)
    add_work_atividade(7, 2)
    add_work_atividade(8, 4)

    print('Populamento do app Site terminado com sucesso!')

def populate_test():
    populate()
