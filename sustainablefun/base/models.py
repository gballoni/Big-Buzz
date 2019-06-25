# import os
from django.db import models
from util.funcoes import string_to_path, object_file_path, generate_object_slug
from ckeditor.fields import RichTextField
# from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Banner(models.Model):
    nome = models.CharField(verbose_name="Nome do Banner", max_length=30)
    slug = models.SlugField(verbose_name="Apelido do Banner", unique=True, blank=True, max_length=30)
    link = models.CharField(verbose_name="Link do Banner (com http)", max_length=100, blank=True, null=True)
    publicado = models.BooleanField(default=False, verbose_name='Publicado?')
    # meta_detalhe = models.ForeignKey('MetaDetalhe', verbose_name="Meta-Detalhe", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=object_file_path, verbose_name="Imagem para ser utilizada no Banner")

    # Método de "limpeza" para ser executado antes de salvar um modelo (muito útil para tratamento de campos)
    def clean(self):
        temp = string_to_path(self.slug)
        if temp == '':
            temp = generate_object_slug(Banner, self.nome)
        if self._state.adding and Banner.objects.filter(slug=temp).exists():
            temp = generate_object_slug(Banner, temp)
        self.slug = temp
        return super().clean()

    def __str__(self):
        return self.slug

class Workshop(models.Model):
    nome = models.CharField(verbose_name="Nome do Workshop", max_length=125)
    slug = models.SlugField(verbose_name="Apelido do Workshop", unique=True, blank=True, max_length=125)
    resumo = models.CharField(verbose_name="Resumo do Workshop", max_length=255)
    publicado = models.BooleanField(default=False, verbose_name='Publicado?')
    imagem = models.ImageField(upload_to=object_file_path, verbose_name="Imagem para ser utilizada no Workshop")
    tempo_necessario = models.CharField(verbose_name="Tempo previsto para o Workshop", max_length=255)
    conteudo = RichTextField(verbose_name="Conteúdo do Workshop")

    # Método de "limpeza" para ser executado antes de salvar um modelo (muito útil para tratamento de campos)
    def clean(self):
        temp = string_to_path(self.slug)
        if temp == '':
            temp = generate_object_slug(Workshop, self.nome)
        if self._state.adding and Workshop.objects.filter(slug=temp).exists():
            temp = generate_object_slug(Workshop, temp)
        self.slug = temp
        return super().clean()

    def __str__(self):
        return self.slug

class Atividade(models.Model):
    class Meta:
        unique_together = ("workshop", "numero")
    numero = models.PositiveIntegerField(verbose_name='Número da atividade')
    nome = models.CharField(max_length=125)
    workshop = models.ForeignKey('workshop', on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False, verbose_name='Publicado?')
    tempo_necessario = models.CharField(verbose_name="Tempo previsto para a Atividade", max_length=255)
    # TODO: Transformar materiais em outro objeto? Ou um conjunto de arquivos?
    material = RichTextField(verbose_name="Materiais para a Atividade", null=True, blank=True)
    descricao = RichTextField(verbose_name="Descrição da Atividade")

    def __str__(self):
        return f"{self.workshop} - {self.numero}/{self.nome}"
