from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
