from django.contrib.auth.models import User
from django.db import models




class Remember(models.Model):
    name = models.CharField('Имя воспоминания', max_length=100)
    comment = models.CharField('Комментарий', max_length=300)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}, {self.comment}'

