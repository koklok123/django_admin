# Generated by Django 5.1.2 on 2024-10-16 10:19

import apps.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('logo', models.ImageField(upload_to=apps.utils.custom_upload_path)),
                ('instagram', models.URLField(verbose_name='Ссылка на instagram')),
                ('facebook', models.URLField(verbose_name='Ссылка на facebook')),
                ('youtube', models.URLField(verbose_name='Ссылка на youtube')),
            ],
            options={
                'verbose_name': 'Основная настройка',
                'verbose_name_plural': 'Основные настроки',
            },
        ),
    ]
