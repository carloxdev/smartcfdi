# -*- coding: utf-8 -*-

# Librerias Python:
import os
from datetime import date

# Librerias Propias:
from tecnology import Cfdineitor


if __name__ == '__main__':
    run_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    app = Cfdineitor("PRODUCCION", run_path)
    app.get_ByRange('EXSEN', date(2017, 1, 1), date(2017, 1, 5))
