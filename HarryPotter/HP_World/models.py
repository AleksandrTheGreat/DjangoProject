from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=50, default='Нет названия') # Название
#     description = models.TextField(default='Нет описания') # Описание
#     year = models.IntegerField(default='Нет даты') # Год выпуска
#     quote = models.CharField(max_length=200, default='Нет цитаты') # Цитата
#     cover = models.ImageField(upload_to='img/Books/') # Обложка книги

class BookCategory(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/')
    release_year = models.IntegerField()
    quote = models.TextField()
    description = models.TextField()

class MovieCategory(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie_images/')
    release_year = models.IntegerField()
    creators = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    description = models.TextField()

class GameCategory(models.Model):
    name = models.CharField(max_length=100)

class Game(models.Model):
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='game_images/')
    release_year = models.IntegerField()
    creators = models.CharField(max_length=200)
    description = models.TextField()