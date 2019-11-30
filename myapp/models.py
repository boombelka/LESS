from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Опубликовано')
    rublic = models.ForeignKey('Rublic', null=True, on_delete = models.PROTECT, verbose_name='Рублика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']


class Rublic(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рублика'
        verbose_name_plural = 'Рублики'
        ordering = ['name']


# Create your models here.
