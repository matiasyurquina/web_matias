# Generated by Django 4.0.4 on 2022-05-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_rename_idpersona_persona_idpersona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_registro',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cel',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]