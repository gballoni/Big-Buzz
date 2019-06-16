FROM python:3.7.3-slim-stretch
MAINTAINER BigBuzz
ENV TZ America/Sao_Paulo

# Setup do ambiente (atualiza o SO, acerta o timezone e adiciona o sudo).
ENV PYTHONUNBUFFERED 1
RUN echo $TZ > /etc/timezone \
  && rm /etc/localtime \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y sudo

# Instalando pacotes
RUN sudo apt-get install -y --no-install-recommends gcc git build-essential python3 python3-pip libpq-dev python3-dev curl gettext-base nginx
RUN sudo -H pip3 install --upgrade pip
RUN sudo -H pip3 install -U pip setuptools

# Dependências do Python
RUN sudo -H pip3 install pypandoc virtualenv virtualenvwrapper

# Comandos só executados no Docker (não fazem sentido em ambientes reais)
ENV VIRTUALENVWRAPPER_PYTHON /usr/bin/python3
ENV WORKON_HOME ~/Env
ENV VIRTUALENVWRAPPER_VIRTUALENV /usr/local/bin/virtualenv

# Atualizando tudo que foi instalado
RUN sudo apt-get update
RUN sudo apt-get upgrade -y
RUN sudo apt-get clean

# Copiar dependências do projeto
COPY ./requirements.txt /opt/requirements.txt

RUN cd ~
# Normalmente criaríamos virtualenvs para o projeto, para então instalar dependências,
# porém o Docker não é lá muito amigo dos venvs. Como estamos em um sandbox, podemos
# instalar as dependências globalmente sem medo, já que esse será o único projeto do ambiente.
RUN sudo pip3 install --no-cache-dir -r /opt/requirements.txt

EXPOSE 8000

# Pasta "opt" é uma pasta para "instalação de pacotes adicionais de aplicações" do UNIX
WORKDIR /var/www/sustainablefun

# Comando base para executar ao entrar na imagem, caso nenhum comando seja informado
CMD ./run.sh docker
