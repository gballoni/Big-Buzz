# Generated by Django 2.2.1 on 2019-06-16 04:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=ckeditor.fields.RichTextField(verbose_name='Descrição da Atividade'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='material',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Materiais para a Atividade'),
        ),
    ]