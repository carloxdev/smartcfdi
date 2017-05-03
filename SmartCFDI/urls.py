# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

# API Rest
from rest_framework import routers

# Mis API Views:
from facturas.views import FacturaProveedorAPI
from facturas.views import FacturaProveedorTodosAPI
from facturas.views import FacturaClienteAPI
from facturas.views import FacturaClienteTodosAPI
from facturas.views import ComprobanteEmpleadoAPI
from facturas.views import ComprobanteEmpleadoTodosAPI
from facturas.views import LogAPI
from facturas.views import ResumenAPI

from configuracion.views import EmpresaAPI

router = routers.DefaultRouter()

router.register(
    r'facturas_proveedor',
    FacturaProveedorAPI,
    'facturas_proveedor'
)
router.register(
    r'facturas_proveedor_todos',
    FacturaProveedorTodosAPI,
    'facturas_proveedor_todos'
)
router.register(
    r'facturas_cliente',
    FacturaClienteAPI,
    'facturas_cliente'
)
router.register(
    r'facturas_cliente_todos',
    FacturaClienteTodosAPI,
    'facturas_cliente_todos'
)
router.register(
    r'comprobantes_empleado',
    ComprobanteEmpleadoAPI,
    'comprobantes_empleado'
)
router.register(
    r'comprobantes_empleado_todos',
    ComprobanteEmpleadoTodosAPI,
    'comprobantes_empleado_todos'
)
router.register(
    r'logs',
    LogAPI,
    'logs'
)
router.register(
    r'resumenes',
    ResumenAPI,
    'resumenes'
)
router.register(
    r'empresas',
    EmpresaAPI,
    'empresas'
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'', include('home.urls', namespace="home")),
    url(r'', include('seguridad.urls', namespace="seguridad")),
    url(r'', include('configuracion.urls', namespace="configuracion")),
    url(r'', include('facturas.urls', namespace="facturas")),
    url(r'', include('dashboards.urls', namespace="dashboards")),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),  # admin site
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
