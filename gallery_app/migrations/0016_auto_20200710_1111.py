# Generated by Django 3.0.7 on 2020-07-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0015_auto_20200629_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilder',
            name='text_1',
            field=models.TextField(blank=True, null=True, verbose_name='Text 1'),
        ),
        migrations.AlterField(
            model_name='bilder',
            name='text_2',
            field=models.TextField(blank=True, null=True, verbose_name='Text 2'),
        ),
    ]
