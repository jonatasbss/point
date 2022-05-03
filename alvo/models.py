from django.db import models

# Create your models here.

class Alvo(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    data_expiracao = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'Alvo'