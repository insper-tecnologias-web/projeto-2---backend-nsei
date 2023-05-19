from django.db import models

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)