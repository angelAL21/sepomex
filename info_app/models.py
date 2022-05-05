from django.db import models

#info class to get the information of queries.
class Info(models.Model):
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    
    def __str__(self):
        return self.municipio
    