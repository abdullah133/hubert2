# Generated by Django 3.0.7 on 2020-07-14 08:38

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0012_auto_20200713_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='bild',
            field=stdimage.models.StdImageField(blank=True, upload_to='news/bilder/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='pdf',
            field=models.FileField(blank=True, upload_to='news/pdf/'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='schrift_farbe',
            field=models.CharField(choices=[('SCHWARZ', 'Schwarz'), ('WEISS', 'Weiß')], max_length=9, verbose_name='Schriftfarbe'),
        ),
    ]