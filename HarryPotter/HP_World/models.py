from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, default='Нет названия') # Название
    description = models.TextField(default='Нет описания') # Описание
    year = models.IntegerField(default='Нет даты') # Год выпуска
    quote = models.CharField(max_length=200, default='Нет цитаты') # Цитата
    cover = models.ImageField(upload_to='img/Books/')