# Generated by Django 3.2.18 on 2023-03-11 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publication_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
