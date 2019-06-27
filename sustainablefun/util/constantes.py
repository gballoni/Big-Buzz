testimonials = [
    {'nome': 'Paula Souza',
    'proficao': 'Teacher',
    'numero': 0,
    'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(30).jpg',
    'depoimento': 'Great fun, my students love it'
    },
    {'nome': 'Tais Silva',
    'proficao': 'Teacher' ,
    'numero': 1,
    'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(31).jpg',
    'depoimento': 'Nothing like learning to care for the environment and having fun at the same time'
    },
    {'nome': 'Rafael Braga',
    'proficao': 'Teacher',
    'numero': 2,
    'imagem': 'https://mdbootstrap.com/img/Photos/Avatars/img%20(32).jpg',
    'depoimento': 'Very educational, easy to apply to any class'
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
