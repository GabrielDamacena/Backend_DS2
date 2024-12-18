# Generated by Django 5.1.3 on 2024-11-11 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios/')),
            ],
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_long', models.CharField(max_length=50)),
                ('data_hora', models.DateTimeField()),
                ('status', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]
