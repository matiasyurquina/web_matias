# Generated by Django 4.0.4 on 2022-05-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obraSocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrasocial',
            name='obraSocial',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
