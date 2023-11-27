from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    year = models.DateField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='media/',
                              verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Serial(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    year = models.DateField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='media/',
                              verbose_name='Изображение')
    count_series = models.PositiveSmallIntegerField(verbose_name='Количество серий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
