from django.db import models

class Pomen(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя кого-то')
    pomen = models.CharField(max_length=100, verbose_name='Поменял кого-то')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Помен'
        verbose_name_plural = 'Помени'
