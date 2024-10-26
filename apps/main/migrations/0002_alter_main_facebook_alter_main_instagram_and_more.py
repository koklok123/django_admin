# Generated by Django 5.1.2 on 2024-10-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на facebook'),
        ),
        migrations.AlterField(
            model_name='main',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на instagram'),
        ),
        migrations.AlterField(
            model_name='main',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на youtube'),
        ),
    ]