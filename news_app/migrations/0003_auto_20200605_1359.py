# Generated by Django 3.0.7 on 2020-06-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_newsmodel_text_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='text_1',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='text_2',
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text 1'),
        ),
    ]
