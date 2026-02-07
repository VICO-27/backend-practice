from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    enrolled_date = models.DateField()

    def __str__(self):
        return self.fullname