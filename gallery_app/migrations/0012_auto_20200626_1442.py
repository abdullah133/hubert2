# Generated by Django 3.0.7 on 2020-06-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0011_auto_20200626_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bilder',
            old_name='untertitel',
            new_name='text_2',
        ),
        migrations.AddField(
            model_name='bilder',
            name='text_1',
            field=models.TextField(blank=True, null=True, verbose_name='Untertitel'),
        ),
    ]
