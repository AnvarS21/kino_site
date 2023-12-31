# Generated by Django 4.2.7 on 2023-11-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('year', models.DateField(verbose_name='Год выпуска')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('year', models.DateField(verbose_name='Год выпуска')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Изображение')),
                ('count_series', models.PositiveSmallIntegerField(verbose_name='Количество серий')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
    ]
