from .models import Workshop, Atividade

def add_or_update_workshop(slug, **kwargs):
    """Cria uma tupla workshop no BD, caso uma já não exista, baseado no slug informado.
    Um workshop deve ter as chaves 'nome', 'slug', 'publicado', 'imagem', 'tempo_necessario'
    e 'conteúdo'. Retorna o objeto que representa a tupla."""
    n = kwargs.get('nome', None)
    p = kwargs.get('publicado', None)
    i = kwargs.get('imagem', None)
    t = kwargs.get('tempo_necessario', None)
    c = kwargs.get('conteudo', None)
    w = Workshop.objects.filter(slug=slug).all()
    if not w.exists():
        Workshop.objects.get_or_create(
            nome=n,
            slug=slug,
            publicado=p,
            imagem=i,
            tempo_necessario=t,
            conteudo=c)
    else:
        w.update(
            nome=n,
            publicado=p,
            imagem=i,
            tempo_necessario=t,
            conteudo=c)
    return Workshop.objects.get(slug=slug)

def add_or_update_atividade(workshop, numero, **kwargs):
    """Cria uma atividade à um workshop existente no BD, caso esssa não exista. Recebe como parâmetros
    o objeto workshop, o número que representa a atividade, e as chaves 'nome', 'publicado',
    'material', 'tempo_necessário' e 'descrição'. Retorna o objeto que representa a atividade."""
    n = kwargs.get('nome', None)
    p = kwargs.get('publicado', None)
    t = kwargs.get('tempo_necessario', None)
    m = kwargs.get('material', None)
    d = kwargs.get('descricao', None)
    a = Atividade.objects.filter(workshop=workshop, numero=numero).all()
    if not a.exists():
        Atividade.objects.get_or_create(
            numero=numero,
            nome=n,
            workshop=workshop,
            publicado=p,
            tempo_necessario=t,
            material=m,
            descricao=d)
    else:
        a.update(
            nome=n,
            publicado=p,
            tempo_necessario=t,
            material=m,
            descricao=d)
    return Atividade.objects.get(workshop=workshop, numero=numero)

def add_work_atividade(numero, atividades):
    """Cria uma tupla workshop genérica no BD, caso uma já não exista, baseada no número passado
    e já adiciona N atividades à essa tupla. Retorna o objeto que representa o workshop criado."""
    w = add_or_update_workshop(
        'teste' + str(numero),
        nome = f'Workshop {str(numero)} Sustainability, what is the fuss all about?',
        publicado = True,
        imagem = 'workshops/teste' + str(numero) +'/workshop_teste0' + str(numero) + '.jpg',
        tempo_necessario = "50-60 min",
        conteudo = "<p> Teacher’s notes \n" +
        "•	 Read thoroughly the introduction and material provided in the previuos chapters;\n" +
        "•	 Explanation and introduction to the concept of Circular Economy which is\n" +
        "favoured by the United Nations as ideal alternative to sustainable development;\n" +
        "•	 Consider maybe watching “The true cost” to understand the scenario better.\n" +
        "Learning objectives\n" +
        "•	 Initial and broad introduction to the subject of the workshop to students;\n" +
        "•	 Introduction to the tripod and general concepts through a word search;\n" +
        "•	 Explanation of the competition (which can be adapted as please). </p>")
    for i in range(atividades):
        add_or_update_atividade(
            w[0],
            i,
            nome = 'Atividade Teste' + str(i),
            publicado = True,
            tempo_necessario = str(120/atividades) + ' min',
            material = "<p>Url talvez?</p>",
            descricao = "Atividade de teste")
    return w

def deleta_workshop(workshop_slug, **kwargs):
    "Remove um workshop do BD baseado em seu nome e slug. Retorna True se o workshop foi removido com sucesso."
    _workshop = Workshop.objects.filter(slug=workshop_slug).all()
    if not _workshop.exists():
        return False
    # Slug é único, portanto não teremos mais que 1 workshop com o mesmo slug e nome
    _atividades = _workshop[0].atividade_set.all()
    for _atividade in _atividades:
        _atividade.delete()
    _workshop[0].delete()
    return True

def populate():
    _workshops = [
        {'nome': 'Workshop 1. Sustainability, what is the fuss all about?',
        'slug': 'workshop1',
        'publicado': True,
        'imagem': 'workshops/workshop1/workshop1_main.jpg',
        'tempo_necessario': 'c. 50-60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>Read thoroughly the introduction and material provided in the previuos chapters;</li>
                        <li>Explanation and introduction to the concept of Circular Economy which is favoured by
                        the United Nations as ideal alternative to sustainable development;</li>
                        <li>Consider maybe watching “The true cost” to understand the scenario better.</li>
                    </ul>
                    <p class="m-0">
                        <b>Learning objectives:</b>
                    </p>
                    <ul>
                        <li>Initial and broad introduction to the subject of the workshop to students;</li>
                        <li>Introduction to the tripod and general concepts through a word search;</li>
                        <li>Explanation of the competition (which can be adapted as please).</li>
                    </ul>''',
        'atividades': [
            {'numero': 1,
            'nome':  'Introduction',
            'publicado': True,
            'tempo_necessario': '15 minutes',
            'material': '''<a
                            href="/media/materiais/activity_anex_1.pdf"
                            alt="Activity Anex 1"
                            target="_blank"
                        >
                            Activity annex 1
                        </a>
                        - Introduction slides 1 (on request).''',
            'descricao': '''<p>The slides contain a broad explanation of concepts surrounding sustainability
                            which will be sufficient for the word search and which will be explored in-depth
                            during the other activities.</p>'''},
            {'numero': 2,
            'nome':  'Sustainability word search',
            'publicado': True,
            'tempo_necessario': '15 minutes',
            'material': '''<a
                            href="/media/materiais/appendix_1.pdf"
                            alt="Appendix 1"
                            target="_blank"
                        >
                            Word search (Appendix 1, p. 44)
                        </a>''',
            'descricao': '''<p>The slides contain a broad explanation of concepts surrounding sustainability
                            which will be sufficient for the word search and which will be explored in-depth
                            during the other activities.</p>'''},
            {'numero': 3,
            'nome':  'The Bear’s Cave',
            'publicado': True,
            'tempo_necessario': '10 minutes',
            'material': '''Slides and the show’s Vignette
                        <a
                            href="https://www.youtube.com/watch?v=dclj3xTvmts"
                            alt="Slides and the show’s Vignette"
                            target="_blank"
                        >
                            (https://www.youtube.com/watch?v=dclj3xTvmts)
                        </a>''',
            'descricao': '''<p>Based on the Dragon’s Den TV show the Bear’s cave is a competition between
                            business propositions which will be developed by the students either during the
                            full extent of the programme or during the simplified version.
                            The choice for the bear is due to the animal’s strength and at the same time
                            vulnerability to environmental changes.</p>
                            <p class="m-0">
                                <b>Competition’s rules:</b>
                            </p>
                            <ul>
                                <li>Divide the class in pairs or groups according to the number of students.
                                From the time they are divided all the following activities will be done together, as
                                a team. This is important because this programme can be seen as a 6 or 8 days
                                competition and many of the activities will generate points towards the final score
                                and ‘prize’.</li>
                                <li>The students must use the Circular Economy principles (explained in the
                                next activity) to create a fashion related company which embraces the three main
                                aspects of sustainability: social, economic and environmental.</li>
                                <li>They can choose any part of the value or supply chain of the textile industry
                                as long as they remember to have answers for the for the points you you can see
                                in the diagram in following page.</li>
                                <li>This will be the closing activity of the programme and will account for
                                100 points (to be added to the points from the other activities), being judged by
                                teachers or personal available.</li>
                            </ul>'''},
            {'numero': 4,
            'nome':  'Circular economy',
            'publicado': True,
            'tempo_necessario': '10 minutes',
            'material': '''Circular and linear economy diagrams
                        <a
                            href="/media/materiais/appendix_2.pdf"
                            alt="Appendix 2"
                            target="_blank"
                        >
                            (Appendix 2, p. 45)
                        </a>,
                        <a
                            href="/media/materiais/key_business_plan_elements.jpg"
                            alt="Key Business Plan Elements Image"
                        >
                            Key Business Plan Elements Image
                        </a>''',
            'descricao': '''<p>After analysing the diagram the students should start thinking about what they
                            will develop for their ‘Bear’s Cave’ businesses and how they could possibly use
                            circular economy.<br>Remember to leave some time for Q&A</p>
                            <p>
                                <b>Expected outcome:</b>
                                <br>
                                From this introduction, students are expected to start evaluating companies
                                surrounding them and how they function, where their production plants are
                                based, if they have a corporate social responsibility or any kind of sustainability
                                department, etc.
                            </p>
                            <img
                                src="/media/materiais/key_business_plan_elements.jpg"'''}
        ]},

        {'nome': 'Workshop 2. Green Quiz',
        'slug': 'workshop2',
        'publicado': True,
        'imagem': 'workshops/workshop2/workshop2_main.jpg',
        'tempo_necessario': 'c. 50-60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>This day is expected to be a fun day in which students start practicing some of
                        their ideas about sustainability and are introduced to other new concepts. </li>
                        <li>As said before, the students will be working in teams
                        and will be competing against the other teams for points.</li>
                    </ul>
                    <p class="m-0">
                        <b>Learning objectives:</b>
                    </p>
                    <ul>
                        <li>This explicit method of ‘layered game’ was developed to expose basic
                        sustainability aspects which are already imprinted in most students around the UK,
                        bringing them to use in an affordable, easy and fun manner.</li>
                    </ul>''',
        'atividades': [
            {'numero': 1,
            'nome':  'Introduction',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''<a
                            href="/media/materiais/activity_anex_2.pdf"
                            alt="Activity Anex 2"
                            target="_blank"
                        >
                            Activity annex 2
                        </a>
                        - Introduction slides 2 (on request).''',
            'descricao': '''<p>Pulling back from concepts explored on the first day the students (organised
                            into their ‘Dragon’s Den’s groups) will compete for the overall performance in the
                            GREEN QUIZ which is composed of 6 activities to be developed with the following
                            55 minutes.</p>'''},
            {'numero': 2,
            'nome':  'Human Photocopy',
            'publicado': True,
            'tempo_necessario': '10 minutes',
            'material': '''United Nations Sustainable Development Goals
                        <a
                            href="/media/materiais/appendix_3.pdf"
                            alt="Appendix 3"
                            target="_blank"
                        >
                            (Appendix 3, p. 46)
                        </a>''',
            'descricao': '''<ol>
                                <li>Each team will be given one sheet of paper;</li>
                                <li>The image to be photocopied will be placed centrally
                                and equally distant from all the groups; </li>
                                <li>One member of each group will have 30 seconds to see the image and
                                memorise it. Without touching or bringing the image back to the group;</li>
                                <li>Once the 30 seconds are finished this student will return to its
                                team 20 Sustainability: turning knowledge into action and draw as much
                                information as he/she can remember during other 30 seconds; </li>
                                <li>Once this time is finished, another member of the team will do
                                the same: look at the image for 30 second and draw for other 30;</li>
                                <li>This alternation will go on for 5 minutes;</li>
                                <li>By the end of the 5 minutes each team will bring their drawing
                                forth to be evaluated. The pointing should be assessed as:
                                    <ol>
                                        <li>Overall layout: 10 points</li>
                                        <li>Drawings: points each</li>
                                        <li>Writings: points each</li>
                                    </ol>
                                </li>
                            </ol>
                            <p>The slides contain a broad explanation of concepts surrounding sustainability
                            which will be sufficient for the word search and which will be explored in-depth
                            during the other activities.</p>'''},
            {'numero': 3,
            'nome':  'Fast find',
            'publicado': True,
            'tempo_necessario': '10 minutes',
            'material': '''Images by theme
                        <a
                            href="/media/materiais/appendix_4.pdf"
                            alt="Appendix 4"
                            target="_blank"
                        >
                            (Appendix 4, p. 47)
                        </a>''',
            'descricao': '''<ol>
                                <li>Before class the facilitator should distribute the cards around the room.</li>
                                <li>The facilitator should then write on the board (or
                                any visible place) the 3 categories of the cards.</li>
                                <li>The student will have 8 minutes to find and organise
                                the images according to the categories.</li>
                                <li>Each image found and rightly identified is worth 1 point.</li>
                            </ol>'''},
            {'numero': 4,
            'nome':  'Hot seat',
            'publicado': True,
            'tempo_necessario': '10 minutes',
            'material': '''Production description
                        <a
                            href="/media/materiais/appendix_5.pdf"
                            alt="Appendix 5"
                            target="_blank"
                        >
                            (Appendix 5, p. 50)
                        </a>''',
            'descricao': '''<ol>
                                <li>One student from each team will have 2 minutes to read
                                the description of the production of a product (provided);</li>
                                <li>This student will then have other 2 minutes
                                to explain the process to the team;</li>
                                <li>The team will then have 5 minutes to draw and
                                find the flaws or advantages of the method described;</li>
                                <li>The best and more comprehensive solution wins 5 points.</li>
                            </ol>'''},
            {'numero': 5,
            'nome':  'Back to Back drawing',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''Figures
                        <a
                            href="/media/materiais/appendix_6.pdf"
                            alt="Appendix 6"
                            target="_blank"
                        >
                            (Appendix 6, p. 55)
                        </a>''',
            'descricao': '''<ol>
                                <li>To be developed by one pair of students per team;</li>
                                <li>One student will be the narrator and the other the artist;</li>
                                <li>The students must sit back to back and they will have 2
                                minutes for the narrator to explain the image and the artist
                                to draw (without asking the narrator for explanations).</li>
                                <li>After that time, the artist will have 1 minute to
                                check with the narrator its doubts.</li>
                                <li>The most accurate drawing wins.</li>
                            </ol>'''},
            {'numero': 6,
            'nome':  'Quiz (90s to answer)',
            'publicado': True,
            'tempo_necessario': '15 minutes',
            'material': '''Quiz me!
                        <a
                            href="/media/materiais/appendix_7.pdf"
                            alt="Appendix 7"
                            target="_blank"
                        >
                            (Appendix 7, p. 56)
                        </a>''',
            'descricao': '''<ol>
                                <li>To be developed by one pair of students per team;</li>
                                <li>One student will be the narrator and the other the artist;</li>
                                <li>The students must sit back to back and they will have 2
                                minutes for the narrator to explain the image and the artist
                                to draw (without asking the narrator for explanations).</li>
                                <li>After that time, the artist will have 1 minute to
                                check with the narrator its doubts.</li>
                                <li>The most accurate drawing wins.</li>
                            </ol>'''},
            {'numero': 7,
            'nome':  'Plenary',
            'publicado': True,
            'tempo_necessario': 'Remaining',
            'descricao': '''<p>During the plenary the facilitator will count each team’s
                            points and write them down to be used in the future activities</p>
                            <p>
                                <b>Expected outcome:</b>
                                <br>
                                Learn varied concepts, objects and practices involved
                                in sustainability through the games in an interactive way.
                            </p>'''}
        ]},
        {'nome': 'Workshop 3. Social Development',
        'slug': 'workshop3',
        'publicado': True,
        'imagem': 'workshops/workshop3/workshop3_main.jpg',
        'tempo_necessario': 'c. 50-60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>Student might consider the material strong in some of the videos, hence its implementation through a quiz;</li>
                        <li>It’s essential to know that raw materials are generally planted or produced
                            in underdeveloped countries and that work condition in these countries can be
                            deplorable due to poor legislation, labour laws and enforcement;</li>
                        <li>Labour can be considered the most negative aspect of the textile industry as
                            cheap labour tends to increase profit;</li>
                        <li>The supply chain reflects the need for cheaper materials and labour, so
                            consequently the products have to ‘travel’ longer distance from the production plant
                            to the market.</li>
                    </ul>
                    <p class="m-0">
                        <b>Learning objectives:</b>
                    </p>
                    <ul>
                        <li>ntroduce the students to the global production environment in which their
                            clothes are inserted;</li>
                        <li>Initial understanding of the concept of globalization and the production
                            pipeline’s needs;</li>
                        <li>Understanding of the lengths a garment might ‘travel’.</li>
                    </ul>''',
        'atividades': [
            {'numero': 1,
            'nome':  'Do you agree or disagree (and why?)',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''set of questions
                        <a
                            href="/media/materiais/appendix_8.pdf"
                            alt="Appendix 9"
                            target="_blank"
                        >
                            (Appendix 8, p. 59)
                        </a>
                        ''',
            'descricao': '''<ol>
                                <li>The instructor/teacher will start this activity with a set of questions which are   
                                    intended to facilitate the discussion that will follow</li>
                                <li>The students should decide if they agree, disagree or are unsure</li>
                                <li>The students are then expected to interact and try to change their</li>
                                <li>colleagues’ minds defending their point of view.</li>
                                <li>Give the students around 5 minutes per topic (also depending on their
                                    participation level) and then recount who agrees or disagrees, always trying to     
                                    motivate them to discuss the topics.</li>
                            </ol>'''},

                            

            {'numero': 2,
            'nome':  'T-shirt price breakdown',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''Sketch of a t-shirt cost break
                        <a
                            href="/media/materiais/appendix_9.pdf"
                            alt="Appendix 9"
                            target="_blank"
                        >
                            Word search (Appendix 9, p. 60)
                        </a>''',
                        'descricao': '''<p>After answering the ‘agree or disagree’ questions the students will be separated         
                                into their teams and given a t-shirt breakdown chart for discussion about the       
                                distribution of the price, ideally comparing the retail margin to the worker’s.</p>'''},
            {'numero': 3,
            'nome':  'General introduction - videoquiz',
            'publicado': True,
            'tempo_necessario': '30 minutes',
            'material': '''<ol>
                            <li> a. Links to open-source videos online:
                                <ol>
                                <li>‘The toxic price of leather’ Sean Gallagher (https://vimeo.com/88261827)</li>
                                <li>‘Fair Trade: Improving lives’ – The Fairtrade Foundation (https://www.youtube.com/watch?v=4tvLHDxv4B4)</li>
                                </ol>
                            <li> b. 2 sets of questions for the quiz (1 per video);</li>
                            </ol>
                       <a
                            href="/media/materiais/appendix_10.pdf"
                            alt="Appendix 10"
                            target="_blank"
                        >
                            Word search (Appendix 10, p. 61)
                        </a>''',
                         'descricao': '''<p>Even though these videos can be considered harsh they portrait very clearly
                                            the intrinsic connection between the social aspects of production and the
                                            environmental, which tends to be the most recognised consequence of production.
                                            Doing this with a quiz guarantees that the students will pay more attention to the
                                            content of the video in order to make more points.</p>'''},
            {'numero': 4,
            'nome':  'Where do your clothes come from?',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''Where your clothes come from maps - Labour, Production,Consumers.
                        <a
                            href="/media/materiais/appendix_11.pdf"
                            alt="Appendix 11"
                            target="_blank"
                        >
                            Word search (Appendix 11, p. 62)
                        </a> This should also help:''',
            'descricao': '''<p>Once the students have heard of the critical situations in India, Uganda, etc. It
                                is essential for them to learn where those countries are, giving the facilitator an
                                opportunity to teach some historical events which might have led to this, such as:</p>
                            <p>
                                <ol>
                                <li>Colonialism;</li>
                                <li>The crusades and the “discovery of the east”;</li>
                                <li>The silk roads;</li>
                                <li>The goods triangle between cotton produced in the USA, manufactured goods from the UK and slaves from African countries;</li>
                                <li>Neo-colonialism;</li>
                                <li>The industrial revolution, and others.</li>
                                </ol>
                            </p>
                            <img
                                src="/media/materiais/Global_citizenship_is.jpg"'''},
         
            {'numero': 5,
            'nome':  'So what? (solutions for the Dragon’s Den)',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': ''' ''',
                'descricao': '''<p>After learning more about these issues the teams are going to work together
								towards their ‘Bear’s Cave’ projects. They are expected to discuss how they will
								approach social aspects in their projects and how consumers could be involved in
								the improvement of lives around the world.</p>
                            	<p class="m-0">
                        		<b>Expected outcome:</b>
                    			</p>
                            
                            	<ul>
                                	<li>Students will understand the association of quality of life, income and the
										globalised textile industry;</li>
                                	<li>Initial conceptualisation of how something as simple as clothing can be</li>
                                	<li>Start shaping their project proposition into a possible instrument for change.</li>
                            	</ul>
                            </p>
                            <img
                                src="/media/materiais/So_What.jpg"'''}
            ]},
         {'nome': 'Workshop 4. Environmental development',
        'slug': 'workshop4',
        'publicado': True,
        'imagem': 'workshops/workshop4/workshop4_main.jpg',
        'tempo_necessario': 'As this can be a very hands-on set of activities, it might be wise to distribute them over more than one hour, possibly, 50 to 60 minutes per activity',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>This is a very ‘hand-on’ class so depending on the number of students it
                            might be the case to do a demonstration class, leaving more time for the paper
                            recycling activity which is easy for pupils from a varied range of ages.</li>
                    </ul>
                    <p class="m-0">
                    <b>Resources</b>
                    </p>
                    <ul>
                        <li>Step by step description of how to recycle paper:</li>
                        <li>SList of possible alternative for things found in the waste (this activity could
                            either be carried out by the facilitator, seeking to engage the students as much as
                        possible, or by the Students with the due attention to possible hazard);</li>
                        <li>Thick gloves and tarp for the waste bins’ analysis (not provided).</li>
                    </ul>
                    <p class="m-0">
                    <b>Learning objectives</b>
                    </p>
                    <ul>
                        <li>Understand how simple sustainability processes happen and how students
                        could possibly replicate them at home;</li>
                        <li>Show in a very ‘shocking’ way how things could be reprocessed if they don’t
                        get thrown on regular garbage.</li>
                    </ul>''',
        'atividades': [
            {'numero': 1,
            'nome':  'Intro',
            'publicado': True,
            'tempo_necessario': '5 minutes',
            'material': '''<a>
                            Activity annex 3 - Introduction slides 3 (on request).
                        </a>
                        ''',
            'descricao': '''<p>Environmental development focusses on concepts to which students are usually
                            aware of and might carry them out on a daily basis.</p>'''},
            {'numero': 2,
            'nome':  'Waste audit',
            'publicado': True,
            'tempo_necessario': 'up to 20-25 minutes',
            'material': '''thick gloves, tarp, one of the school’s trash bins and the
                            provided extra material
                        <a
                            href="/media/materiais/appendix_12.pdf"
                            alt="Appendix 12"
                            target="_blank"
                        >
                            (Appendix 12, p. 71)
                        </a>''',
            'descricao': '''<p>the facilitator will (using the due safety gear) empty
                            one of the school’s general waste bin on the tarp. The activity relies on examining
                            the contents and make divide the waste in different material categories (such as paper, plastic, cartons, cans, etc). After defining all the waste that could have been
                            recycled in the proper recycling bin, the teacher will ask the students to come up (in
                            groups) with alternative ends to the materials removed from the bins. The facilitator
                            will be provided with an extensive list of alternative ends to a wide range of waste,
                            this way, students will be introduced to different alternatives than the most used.</p>'''},
            {'numero': 3,
            'nome':  'Paper recycling',
            'publicado': True,
            'tempo_necessario': '50-60 minutes',
            'material': '''How to recycle paper
                        <a>
                            href="/media/materiais/appendix_13.pdf"
                            alt="Appendix 13"
                            target="_blank"
                        
                            (Appendix 13, p. 76)
                        </a>''',
            'descricao': '''<p>The facilitator and students should follow the instructions from the card, using
                                paper found in the classroom’s scrap paper tray.
                                Student can also use materials for decoration (such as seeds, dried leaves or
                                flowers, glitters).
                                The facilitator has to discuss about the 3Rs, Reduce, Reuse, Recycle.
                                These are the key points of the discussion with the students:</p>
                            <ol>
                                <li>The facilitator should ask the students where does the paper come from and
                                what needs to be made. The discussion should be about reducing the amout of
                                tree cut to produce paper and cardboard. Motivate the students to Reduce their waste: “Do I really need to use a sheet of
                                paper/do I really need to print a document or can I read it from my laptop?</li>
                                <li>If they really need to use some paper, the facilitator should motivate them to
                                Reuse that paper, telling the students to always put the paper in the classroom’s
                                scrap paper tray in order to write on the opposite side.</li>
                                <li>When the paper is written on both sides, students can throw it in the paper
                                recycling bin in order to make new paper and avoiding to cut more trees.</li>
                                <li>The facilitator should them motivate the students to buy recycled paper,
                                otherwise if no one buys recycled paper, there is no point in doing it.
                                The facilitator should tell the student that they can recognize recycled paper by
                                findind on the paper the logo below.</li>
                            </ol>
                            <ul>
                                <li>Students are expected to interact differently with waste and see it as an
                                input to something else than the landfill; they should also remember well the 3Rs
                                whenever they use or buy something with the grownups.</li>
                                <li>To give students a different perspective this workshop emphasises changes
                                students could do to improve their carbon footprint.</li>
                            </ul>'''}
        ]},

        {'nome': 'Workshop 5. Economic development',
        'slug': 'workshop5',
        'publicado': True,
        'imagem': 'workshops/workshop5/workshop5_main.jpg',
        'tempo_necessario': 'c. 60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>TThe economic aspects of sustainability are one of the most complicated
                        factors to be understood as it tends to be secondary to most people. The general
                        idea behind it is that sustainable development cannot rely on economic disparity.</li>
                        <li>In order to achieve an universal improvement the wealth needs to be spread.</li>
                        <li>In simple terms: It is much harder to think about cleaning industrial waste
                        when the population can barely feed itself.</li>
                        <li>In order to explain this we decided to develop mind maps like the one bellow:</li>
                    </ul>
                    <p class="m-0">
                    <b>Resources</b>
                    </p>
                    <ul>
                        <li>Step by step description of how to recycle paper:</li>
                        <li>SList of possible alternative for things found in the waste (this activity could
                            either be carried out by the facilitator, seeking to engage the students as much as
                        possible, or by the Students with the due attention to possible hazard);</li>
                        <li>Thick gloves and tarp for the waste bins’ analysis (not provided).</li>
                    </ul>
                    <p class="m-0">
                    <b>Learning objectives</b>
                    </p>
                    <ul>
                        <li>Understand the importance of economic development;</li>
                        <li>Educate about the extensions of pollution within a developed and
                            underdeveloped community.</li>
                    </ul>
                    <a>
                            href="/media/materiais/the_conscious_consumer.jpg"
                            alt="The Conscious Consumer"
                        
                            The Conscious Consumer Image
                    </a>''',

            'atividades': [
            {'numero': 1,
            'nome':  'WORKSHOP DESCRIPTION',
            'publicado': True,
            'tempo_necessario': '60 minutes',
            'material': '''<a>
                        </a>
                        ''',
            'descricao': '''<p>
                            <ul>Environmental development focusses on concepts to which students are usually
                            aware of and might carry them out on a daily basis.
                            <li>Students will be provided with backup information for two case studies and
                            they should analyse (Appendix 14, p. 78):
                            <ol>
                                <li>How the cases describe being fair;</li>
                                <li>How the cases portray their profits;</li>
                                <li>How do the companies satisfy their customer’s demands?</li>
                            </ol></li>
                            <li>Once these points are analysed the students are expected to develop an
                            idealised map in which they evaluate (locally and globally) the benefits from each
                            company.</li>
                            <li>Once done so, they can discuss how to improve those points on their Bear’s
                            Cave proposal.</li>                            
                            </ul></p>
                            <p class="m-0">
                            <b>Expected outcome</b>
                            </p>
                            <p>
                                <ul>
                                    <li>Even though this activity might be considered too advanced for some
                                    students, the idea here is mainly: how can a company profit, be fair and satisfy their
                                    customer’s demands at the same time;</li>
                                    <li>If deemed too complicated, students can also go through the global
                                    citizenship slides to analyse the differences between countries in regards to
                                    development and sustainability. Trying to answer the following questions:
                                        <ol>
                                        <li>Why is it harder for underdeveloped countries to impose stricter labour
                                        and environmental legislations?</li>
                                        <li>The Kyoto protocol also evaluates the differences in development
                                        when considering each country’s emissions. This way, countries that started
                                        developing their industries later have space to grow. Do you think this measure is
                                        adequate?</li>
                                        </ol>
                                    </li>

                                </ul>
                            </p>'''}
        ]},


        {'nome': 'Workshop 6. Debate',
        'slug': 'workshop6',
        'publicado': True,
        'imagem': 'workshops/workshop6/workshop6_main.jpg',
        'tempo_necessario': 'c. 60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>In this case it might be good to read all the debate cards in order to
                        understand the topic or maybe research points you might not be too clear about.</li>
                    </ul>
                    <p class="m-0">
                    <b>Learning objectives</b>
                    </p>
                    <ul>
                        <li>Argue a point of view, even if you disagree with it.</li>
                    </ul>''',

            'atividades': [
            {'numero': 1,
            'nome':  'WORKSHOP DESCRIPTION',
            'publicado': True,
            'tempo_necessario': '60 minutes',
            'material': '''debate cards <a
                            href="/media/materiais/appendix_15.pdf"
                            alt="Appendix 15"
                            target="_blank">
                            Word search (Appendix 15, p. 82)
                        </a>''',
            'descricao': '''<p>
                            <ul>
                            <li>Attached to this guide there are 6 different topic propositions, depending on
                                the size of the group one or more topics should be chosen;</li>
                            <li>Students should be divided between ‘For’, ‘Against’ and judges;</li>
                            <li>Students should read the cards and think about how the issues on the card
                            can motivate their discussion.</li>
                            <li>Instigate discussion to motivate them to think about the sentences and ideas
                            proposed on the card.</li>
                            <li>Student will then have 10 to 15 minutes to create an argument to be
                            presented to the judges.</li>
                            <li><As in any other debate there should be time for both participants to present
                            their case, be cross-examined and rebut. Finally being evaluated by the judges./li>
                            <p class="m-0">
                            <b>Expected outcome</b>
                            </p>
                                <ul>
                                    <li>Depending on the student’s year it is important (and a part of the curriculum)
                                        that they clearly understand the concept behind arguing their point of view. This
                                        activity is key to ensure they understood the concepts studied thus far and to
                                        motivate them to discuss and develop an argument wisely.</li>
                                    <li>Besides making the students discuss and defend their ‘actor’s’ point of view,
                                        the students will hear the other perspectives;</li>
                                </ul>
                            </p>'''}
        ]},

        {'nome': 'Workshop 7. Upcycling',
        'slug': 'workshop7',
        'publicado': True,
        'imagem': 'workshops/workshop7/workshop7_main.jpg',
        'tempo_necessario': 'c. 60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>This very hands-on activity is another attempt to motivate students to
                        generate goods of materials considered waste;</li>
                        <li>This should be advertised before the workshop to ensure students bring
                        material from home, such as old clothes, toilet and kitchen rolls, etc;</li>
                        <li>Please beware of possible threats like needles.</li>
                    </ul>
                    <p class="m-0">
                    <b>Learning objectives</b>
                    </p>
                    <ul>
                        <li>Learn how to deal with waste in a sustainable and fun manner</li>
                    </ul>''',

            'atividades': [
            {'numero': 1,
            'nome':  'Activity description',
            'publicado': True,
            'tempo_necessario': '60 minutes',
            'material': '''This guide provides <a
                            href="/media/materiais/appendix_16.pdf"
                            alt="Appendix 16"
                            target="_blank">
                            Word search (Appendix 16, p. 92)
                        </a> different ways to produce the following:''',
            'descricao': '''<p>
                            <ul>
                            <li>Toilet roll mobile holder;</li>
                            <li>Jeans utility belt;</li>
                            <li>Water filter;</li>
                            <li>IMobile speakers;</li>
                            <li>Notebook cover;</li>
                            <li>Necklaces made of t-shirts;</li>
                            <li>Pencil cases;</li>
                            <li>T-shirt carrier bag;</li>
                            <li>Glasses case.</li>
                            </ul>
                            </p>
                            <p>All the material and steps are provided on each upcycling cards, but feel free to
                            search for more activities.
                            </p>
                            <p class="m-0">
                            <b>Expected outcome</b>
                            </p>
                            <p>
                            Once more students are expected to be creative and provide an alternative end to
                            the simple materials, easily found at home.
                            </p>'''}
        ]},

         {'nome': 'Workshop 8. The Bear’s cave - Final',
        'slug': 'workshop8',
        'publicado': True,
        'imagem': 'workshops/workshop8/workshop8_main.jpg',
        'tempo_necessario': 'c.50 - 60 minutes',
        'conteudo': '''<p class="m-0">
                        <b>Teacher’s notes:</b>
                    </p>
                    <ul>
                        <li>There is a cycle of different levels of pressure towards higher profits as well
                            as towards sustainability. In order to satisfy all the actors this forces should be able
                            to balance each other.</li>
                        <li>This final activity is targeted at evaluating how the students absorbed the
                            information from the previous workshops and used it towards their own business
                            proposition.</li>
                    </ul>
                    <p class="m-0">
                    <b>Resources</b>
                    </p>
                    <ul>
                        <li>In the appendix 17 (p. 103) there are three cards to help on the assessment:
                            a Gantt chart to understand the level of organisation the students achieved, a
                            scorecard with the essential information they should provide, and a project charter
                            for clearer understanding of the whole picture.</li>
                    </ul>
                    <p class="m-0">
                    <b>Learning objectives</b>
                    </p>
                    <ul>
                        <li>This activity was developed to evaluate the programme as a whole with
                            all its activities and to observe how the students adapted to the concepts and
                            incorporated them into their business and daily perceptions.</li>
                    </ul>''',

            'atividades': [
            {'numero': 1,
            'nome':  'Activity description',
            'publicado': True,
            'tempo_necessario': '60 minutes',
            'material': ''' ''',
            'descricao': '''<p>
                            <ul>
                            <li>Each group will be given 10 minutes to present their business plan.</li>
                            <li>The judging panel will have 5 minutes for questions and answers, followed
                            by 5 minutes of questions and answers from their colleagues.</li>
                            <li>After all groups presented the judges will have about 10 minutes to compare
                            propositions and chose the most adequate regarding: chances of success,
                            coherence, sustainable impact, etc</li>
                            </ul>
                            </p>
                            <p class="m-0">
                            <b>Expected outcome</b>
                            </p>
                            <p>
                            <ul>
                            <li>After the full workshops students are expected to have a broader and
                            more useful understanding of sustainability, distancing it from only recycling.
                            The students are also expected to improve their understanding of how they can
                            improve their behaviour as well as that from their friends and family.</li>
                            <li>If interested in more activities, please see extension activities bellow.</li>
                            </ul>
                            </p>'''}
            ]}
    ]
    
    print('Populando Banco de Dados...')
    for _workshop in _workshops:
        w = add_or_update_workshop(**_workshop)
        for _atividade in _workshop.get('atividades', []):
            add_or_update_atividade(w, **_atividade)
    print('Populamento do app Site terminado com sucesso!')

def populate_test():
    populate()
