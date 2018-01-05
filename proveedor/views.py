# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from proveedor.form import DistriForm
from django.views.generic import ListView, CreateView, UpdateView 
from django.core.urlresolvers import reverse_lazy
from proveedor.models import Proveedor
from django.template import RequestContext
from django.contrib import messages

def index(request):
	return render(request, 'cesar/inicio/index.html')
# Create your views here.

def distri_view(request):
	nombre = False
	dic = {
			'nombre': nombre }
	if request.method == 'POST':
		form = DistriForm(request.POST)
		
		if form.is_valid():
			
			#instance = form.save(commit=False)
			nombre = form.cleaned_data.get('nombre_proveedor')
			form.save()
			#nombre = True
			dic = {
			'nombre': 'El proveedor %s fue guardado exitosamente' %(nombre) 

		}
		
			form = DistriForm()
			
			#messages.success(request, "Voto registrado")
			return render(request, 'proveedor/proveedor_form.html', dic)
		#return redirect('proveedor:index_view')
	else:
		form = DistriForm()
	return render(request, 'proveedor/proveedor_form.html', {'form':form})


class DistriUpdate(UpdateView):
	model = Proveedor
	form_class = DistriForm
	template_name = 'proveedor/registro_form.html'
	success_url = reverse_lazy('proveedor:index_view')


class ConsultaProveedor(ListView):
	model = Proveedor 
	template_name = 'proveedor/consulta.html'



