# Generated by Django 3.0.7 on 2020-06-08 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontaktinfo',
            name='adresse',
        ),
    ]
