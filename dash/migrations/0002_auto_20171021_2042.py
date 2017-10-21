# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=45, verbose_name='Nome do palestrante')),
                ('speaker_description', models.TextField(max_length=45, null=True, verbose_name='Sobre o palestrante')),
                ('image', models.ImageField(upload_to='palestrante/%Y')),
            ],
        ),
        migrations.RemoveField(
            model_name='palestra',
            name='speaker_description',
        ),
        migrations.RemoveField(
            model_name='palestra',
            name='speaker_name',
        ),
        migrations.AlterField(
            model_name='palestra',
            name='talk_description',
            field=models.TextField(max_length=90, verbose_name='Descrição da palestra'),
        ),
    ]
