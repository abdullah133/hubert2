# Generated by Django 2.2.9 on 2020-06-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0006_kategorien_title_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilder',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
