# bigbuzz/django

## 1- Acesse a raiz do projeto para executar esses comandos.

## 2- Construir a imagem do Django:
## *OBS*- Esse comando deve ser executado a primeira vez que se for executar a imagem, ou quando for atualizado o dockerfile ou requirements.txt da respectiva imagem
```
  docker build -t "bigbuzz/django" ./sustainablefun
```

## 3- Executando a imagem e virtualizando a pasta local:
- Ambientes Linux
```
  docker run -it --net=host --rm -v `pwd`/sustainablefun:/var/www/sustainablefun bigbuzz/django bash
```
- Ambientes Windows
```
  docker run -it --rm -p 8000:8000 -v %cd%/sustainablefun:/var/www/sustainablefun bigbuzz/django bash
```

## 4- Comandos para ser rodado da primeira vez que executar a imagem
```
  python manage.py createsuperuser
```
-- Informar os dados do superusuario padrão do site (login 'admin' com senha 'testeteste')

## 5- Comandos que devem sempre ser executados:
```
  ./run.sh docker
```

# Comandos úteis:

### docker ps -a

  --[Lista todas as imagens ativas no docker, inclusive imagens que estão paradas/inoperantes]
  -- EX:
```
  docker ps -a
```

### docker volume ls

  --[Lista todos os volumes virtualizados do docker]
  -- EX:
```
  docker volume ls
```

### docker image ls

  --[Lista todos as imagens montadas existentes no docker]
  -- EX:
```
  docker image ls
```

### docker exec -it <nome ou id do container> <comando inicial>

  --[Executa em modo iterativo o container ja´em execução, a entrada é realizada através do comando inicial indicado. Você pode, por exemplo, acessar o psql de um container com postgres para checar seus bancos e tabelas.]
  --EX:
```
docker run -d -p 5432:5432 -v pgdata:/var/lib/postgresql/data --name pgserver postgres
docker exec -it pgserver psql -U postgres -W
```
  --[Você pode também acessar o shell de um container (que tenha shell) através do bash]
  --EX:
```
docker exec -it pgserver bash
```

### docker stop <nome ou id do container>

  --[Para o container em execução, se a flag --rm foi adicionada ao comando run, o container será automaticamente apagado, juntamente com seus volumes não mapeados.]
  -- EX:
```
  docker stop pgserver
```

### docker volume rm <nome ou id do volume>

  --[Remove o volume virtual criado. Muitas imagens utilizam volumes digitais para manter seus dados, esses são apagados automaticamente quando o container é encerrado se a flag --rm foi utilizada no run. Serve principalmente para remover volumes que foram mapeados intencionalmente ou de imagens que não utilizaram a flag --rm no run.]
  --EX:
```
  docker volume rm pgdata
```
