# Generated by Django 2.2.1 on 2019-05-26 05:13

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import util.funcoes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do Banner')),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True, verbose_name='Apelido do Banner')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Link do Banner (com http)')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('imagem', models.ImageField(upload_to=util.funcoes.object_file_path, verbose_name='Imagem para ser utilizada no Banner')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do Workshop')),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True, verbose_name='Apelido do Workshop')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('imagem', models.ImageField(upload_to=util.funcoes.object_file_path, verbose_name='Imagem para ser utilizada no Workshop')),
                ('tempo_necessario', models.CharField(max_length=30, verbose_name='Tempo previsto para o Workshop')),
                ('conteudo', ckeditor.fields.RichTextField(verbose_name='Conteúdo do Workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='Número da atividade')),
                ('nome', models.CharField(max_length=50)),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('tempo_necessario', models.CharField(max_length=30, verbose_name='Tempo previsto para a Atividade')),
                ('material', models.CharField(max_length=30, verbose_name='Materiais para a Atividade')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição da Atividade')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Workshop')),
            ],
            options={
                'unique_together': {('workshop', 'numero')},
            },
        ),
    ]