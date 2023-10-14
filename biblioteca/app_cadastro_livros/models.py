from django.db import models

class Livros(models.Model):
    id_livros = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=255)
    autor = models.TextField(max_length=255)
    quantidade = models.IntegerField()