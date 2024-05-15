from django.db import models

# Create your models here.
# resumo/models.py

class Texto(models.Model):
    texto_completo = models.TextField()
    resumo_automatico = models.TextField(blank=True)

