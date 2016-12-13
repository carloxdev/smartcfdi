# -*- coding: utf-8 -*-

# Librerias Python:
import os
from datetime import datetime

# Librerias de Terceros
from celery import task

# Librerias Propias:
from core.tecnology import Cfdineitor


@task
def obtener_facturas(_empresa_clave, _fecha_inicio, _fecha_final):

    print _empresa_clave
    print _fecha_inicio
    fecha_inicio = datetime.strptime(_fecha_inicio, "%Y-%m-%d")
    fecha_final = datetime.strptime(_fecha_final, "%Y-%m-%d")

    run_path = os.path.abspath(
        os.path.join(os.getcwd(), os.pardir, 'Sitio')
    )
    app = Cfdineitor("PRODUCCION", run_path)
    app.get_Invoices_ByRange(
        _empresa_clave,
        fecha_inicio,
        fecha_final
    )
