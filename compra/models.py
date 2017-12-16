# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto.models import Producto
from proveedor.models import Proveedor

# Create your models here.
class Compra(models.Model):
	codigo_compra = models.CharField(max_length=50, primary_key=True)
	id_proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
	id_producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)
	cantidad = models.IntegerField()
	valor_compra = models.IntegerField()

	def __unicode__(self):
		return '{} - {}'.format(self.id_proveedor, self.id_producto)



