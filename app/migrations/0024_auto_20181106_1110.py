# Generated by Django 2.1.1 on 2018-11-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_projeto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nomeUsuario',
            field=models.CharField(max_length=50),
        ),
    ]