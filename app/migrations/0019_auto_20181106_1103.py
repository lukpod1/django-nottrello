# Generated by Django 2.1.1 on 2018-11-06 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20181106_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
    ]
