from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor = models.IntegerField(primary_key=True,verbose_name="Id autor")
    nombre = models.CharField(max_length=250,verbose_name="Nombre autor")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='autores', null=True)
    def __str__(self):
        return  self.nombre
        return  self.historia
        return  self.idAutor
        return  self.img


class Obra(models.Model):
    idObra = models.IntegerField(primary_key=True,verbose_name="Id obra")
    idAutor  = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250,verbose_name="Nombre obra")
    historia = models.TextField(verbose_name="Historia")
    img = models.ImageField(upload_to='obras', null=True)



    def __str__(self):
        return  self.idObra
        return  self.idAutor
        return  self.nombre
        return  self.historia
        return  self.img
