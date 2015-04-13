from django.db import models

class Sugerencia(models.Model): 
    Usuiario = models.CharField(max_length=34)
    Sugerencia = models.TextField(blank=True)

    def __unicode__(self):
        return self.Sugerencia
    