# Generated by Django 3.0.7 on 2020-06-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0004_remove_kontaktinfo_facebook_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontaktinfo',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Facebook Link'),
        ),
    ]
