# -*- coding: utf-8 -*-

from django import forms
from proveedor.models import Proveedor 

class DistriForm(forms.ModelForm):

	class Meta:   #para indicar de que modelo se va a crear el formulario
		model = Proveedor

		fields = [
           'id_proveedor',
           'nombre_proveedor',
           'direccion',
           'telefono',
           'email',
           
		]
		labels = {
	        'id_proveedor' : 'Nit o codigo del proveedor',
            'nombre_proveedor' : 'Nombre',
            'direccion' : 'Direccion',
            'telefono' : 'Telefono',
            'email' : 'Email'
	        
		}
		widgets = {
		'id_proveedor': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Digite aqui el codigo'}),
		'nombre_proveedor': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Digite aqui el nombre del proveedor'}),
        'direccion': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite aqui la dirección del proveedor'}),
        'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite aqui el telefono del proveedor'}),
        'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite aqui el email del proveedor'}),
        
        #'nombre_distribuidor': forms.Select(attrs={'class':'form-control'}),

		}