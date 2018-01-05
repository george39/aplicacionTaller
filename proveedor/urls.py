from django.conf.urls import url, include
from proveedor.views import index, distri_view, DistriUpdate, ConsultaProveedor

urlpatterns = [
url(r'^$', index, name='index_distri'),
url(r'^proveedor$', distri_view, name='index_view'),
url(r'^buscarProveedor$', ConsultaProveedor.as_view(), name='buscarProveedor'),

url(r'^editar/(?P<pk>\d+)/$', DistriUpdate.as_view(), name='distri_editar'),
]