# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from producto.models import Producto 

# Create your models here.
class Venta(models.Model):
	codigo_venta = models.CharField(max_length=50, primary_key=True)
	id_producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
	fecha_venta = models.DateTimeField(auto_now_add=True)
	cantidad = models.IntegerField()
	valor_venta = models.IntegerField()

	def __unicode__(self):
		return '{} - {}'.format(self.codigo_venta, self.id_producto)




