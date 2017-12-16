# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Proveedor(models.Model):
	id_proveedor = models.CharField(max_length=50, primary_key=True)
	nombre_proveedor = models.CharField(max_length=50, blank=True, null=True)
	direccion = models.CharField(max_length=50, blank=True, null=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=50,blank=True, null=True)

	def __unicode__(self):
		return '{} - {}'.format(self.id_proveedor, self.nombre_proveedor)


