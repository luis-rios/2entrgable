from django.db import models

# Create your models here.


class Editorial(models.Model):
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    web = models.CharField(max_length=50)

    def __str__(self):
        return self.name
