# Generated by Django 4.0.4 on 2022-05-29 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_persona_activation_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='activation_code',
        ),
    ]