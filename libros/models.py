from django.db import models

# Create your models here.


class Libro(models.Model):
    author = models.CharField(max_length=50)
    tittle = models.CharField(max_length=50)
    date = models.DateField()
    editorial = models.CharField(max_length=50)

    def __str__(self):
        return self.name