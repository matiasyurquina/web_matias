# Generated by Django 4.0.4 on 2022-05-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.IntegerField(primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
    ]
