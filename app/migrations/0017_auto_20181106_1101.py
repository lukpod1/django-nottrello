# Generated by Django 2.1.1 on 2018-11-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20181106_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='usuario',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
    ]