from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    birthdate = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    pages_num = models.IntegerField()
    cover_image = models.ImageField(upload_to='images/')
    authors = models.ManyToManyField(Author)
