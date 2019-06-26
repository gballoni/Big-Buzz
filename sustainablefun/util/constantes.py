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