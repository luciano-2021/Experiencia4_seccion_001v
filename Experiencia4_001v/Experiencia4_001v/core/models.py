from django.db import models

class Tipomaterial(models.Model):
    idtipo = models.IntegerField(primary_key=True, verbose_name='id tipo identificacion')
    descripcion = models.CharField(max_length=20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class Proveedores(models.Model):
    ididentificacion = models.IntegerField(primary_key=True, verbose_name='Id identificacion')
    nombrecompleto = models.CharField(max_length=100, verbose_name='Nombre completo')
    Telefono = models.CharField(max_length=150, verbose_name='Telefono')
    direccion = models.CharField(max_length=150, verbose_name='direccion')
    email = models.CharField(max_length=150, verbose_name='email')
    pais = models.CharField(max_length=150, verbose_name='pais')
    monedadepago = models.CharField(max_length=150, verbose_name='monedadepago')
    tipomaterial = models.ForeignKey('Tipomaterial', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrecompleto

