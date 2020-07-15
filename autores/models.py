from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
