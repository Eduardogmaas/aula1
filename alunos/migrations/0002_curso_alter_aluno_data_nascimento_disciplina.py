# Generated by Django 5.0.3 on 2024-03-22 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=6, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.curso')),
            ],
        ),
    ]
