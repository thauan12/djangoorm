# Generated by Django 4.2.4 on 2023-08-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='dtnasc',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
    ]
