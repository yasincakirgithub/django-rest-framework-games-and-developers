# Generated by Django 3.2.18 on 2023-03-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
