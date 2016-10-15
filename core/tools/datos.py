# -*- coding: utf-8 -*-

# Librerias Python
import calendar
import time
import os
import re
import shutil
from datetime import datetime

# Librerias Propias
from mistakes import ErrorEjecucion
from mistakes import ErrorValidacion

# An expectation for checking that one of two elements,
# located by locator 1 and locator2, is visible.
# Visibility means that the element is not only
# displayed but also has a height and width that is
# greater than 0.
# returns the WebElement that is visible.


class Visualizador(object):

    def __init__(self, locator1, locator2):
        self.locator1 = locator1
        self.locator2 = locator2

    def __call__(self, driver):
        element1 = driver.find_element(*self.locator1)
        element2 = driver.find_element(*self.locator2)
        return self.is_Visible(element1) or self.is_Visible(element2)

    def is_Visible(self, element):
        return element if element.is_displayed() else False


class Chronos(object):

    @classmethod
    def get_FirstAndLastDay(self, year, month, day=0):
        if day:
            d1 = d2 = '{:02d}/{:02d}/{}'.format(day, month, year)
        else:
            days = calendar.monthrange(year, month)[1]
            d1 = '01/{:02d}/{}'.format(month, year)
            d2 = '{}/{:02d}/{}'.format(days, month, year)

        return d1, d2

    @classmethod
    def sleep(self, sec=1):
        time.sleep(sec)


class Filtro(object):

    def __init__(self, _fecha):
        self.uuid = ''
        self.emisor_rfc = ''
        self.year = _fecha.year
        self.month = _fecha.month
        self.day = _fecha.day
        self.start_hour = '00'
        self.start_minute = '00'
        self.start_second = '00'
        self.end_hour = '23'
        self.end_minute = '59'
        self.end_second = '59'

    def set_ForSeach_ByHour(self, _hora):
        self.start_hour = _hora
        self.start_minute = '00'
        self.end_hour = _hora
        self.end_minute = '59'

    def set_ForSeach_ByMinute(self, _minuto):
        self.start_minute = _minuto
        self.end_minute = _minuto


class Archivo(object):

    def __init__(self, _basepath, _name):
        self.nombre = _name
        self.extension = os.path.splitext(_name)[1]
        self.basepath = _basepath
        self.abspath = os.path.join(self.basepath, self.nombre)
        self.abspath_old = ""

    def move(self, _basepath_new):

        abspath_new = os.path.join(_basepath_new, self.name)

        shutil.move(self.abspath, abspath_new)

        self.abspath_old = self.abspath
        self.abspath = abspath_new

        print "Se movio archivo a: {}".format(abspath_new)


# Estandariazacion de varibales:
# basepath = ruta de un archivo sin el nombre del archivo:  /user/files <--- aqui dentro esta el archivo: ejemplo.xml
# abspath = ruta de un archivo con todo y el nombre: /user/files/ejemplo.xml
# relativepath = ruta relativa de directorio o archivo:  /files


class FileManager(object):

    @classmethod
    def get_Files(self, _abspath, _extension):

        lista_archivos = []

        try:

            if os.path.exists(_abspath):

                archivos = os.walk(_abspath)

                for directorio, subdirectorios, lista_nombreArchivos in archivos:

                    for nombre_archivo in lista_nombreArchivos:
                        (name, ext) = os.path.splitext(nombre_archivo)

                        if ext == _extension:
                            lista_archivos.append(
                                Archivo(directorio, nombre_archivo)
                            )
            else:
                print "El folder no existe: {}".format(_abspath)

            return lista_archivos

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.get_Files()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def delete_DuplicateFiles(self, _abspath, _extension):

        no_eliminados = 0

        try:

            if os.path.exists(_abspath):

                # Se optiene la lista de archivos
                archivos = os.walk(_abspath)

                # Se recorre la lista
                for directorio, subdirectorios, lista_nombreArchivos in archivos:

                    for nombre_archivo in lista_nombreArchivos:

                        # Se separa el nombre y la extension de archivo
                        (name, ext) = os.path.splitext(nombre_archivo)

                        if ext == _extension:

                            if re.search('\(\d+\)$', name):

                                file_abspath = os.path.join(
                                    directorio, nombre_archivo)

                                os.remove(file_abspath)
                                # Eliminar
                                no_eliminados += 1

                print "Eliminar archivos {} repetidos: {}".format(_extension, no_eliminados)

            else:
                print "El folder no existe: {}".format(_abspath)

            return no_eliminados

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.delete_DuplicateFiles()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def create_Folder(self, _abspath):

        try:

            if os.path.exists(_abspath):
                print "El folder ya existe: {}".format(_abspath)
            else:
                code = os.system("mkdir " + _abspath)
                if code == 0:
                    print "Folder creado con exito: {}".format(_abspath)
                else:
                    raise ErrorValidacion(
                        "Creacion de folder finalizo con codigo {}".format(
                            code)
                    )

        except Exception, error:
            raise ErrorEjecucion(
                "FileManager.create_Folder()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def create_Directory(self, _basepath, _newFolders):

        try:
            directory_abspath = os.path.join(_basepath, _newFolders)

            if os.path.exists(directory_abspath):
                print "El directorio ya existe: {}".format(directory_abspath)
            else:

                list_newfolders = _newFolders.split('/')
                folder_abspath = ''

                for folderName in list_newfolders:

                    folder_abspath = os.path.join(
                        _basepath, folder_abspath, folderName)
                    self.create_Folder(folder_abspath)

                print "Directorio creado con exito: {}".format(directory_abspath)

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.create_Directory()",
                type(error).__name__,
                str(error)
            )


class Ruta(object):

    def __init__(self, _run_path, _empresa_clave, _tipo, _fecha):

        self.run_path = _run_path
        self.empresa_clave = _empresa_clave
        self.tipo = _tipo
        self.fecha = _fecha

        self.abspath = self.get_AbsPath()
        self.relativepath = self.get_RelativePath()
        self.urlpath = self.get_UrlPath()

    def get_AbsPath(self):

        abspath = os.path.join(
            self.run_path,
            self.get_RelativePath()
        )

        return abspath

    def get_RelativePath(self):
        directorio = os.path.join(
            "media",
            "facturas",
            self.empresa_clave,
            self.tipo,
            '{:02d}'.format(self.fecha.year),
            '{:02d}'.format(self.fecha.month),
            '{:02d}'.format(self.fecha.day),
        )

        dirs = str(directorio)

        return dirs

    def get_UrlPath(self):
        directorio = os.path.join(
            "facturas",
            self.empresa_clave,
            self.tipo,
            '{:02d}'.format(self.fecha.year),
            '{:02d}'.format(self.fecha.month),
            '{:02d}'.format(self.fecha.day),
        )

        url = str(directorio)

        return url


class Validator(object):

    @classmethod
    def convertToJulianJDE(self, _date):

        jdedate = (1000 * (_date.year - 1900) + int(_date.strftime("%j")))

        return int(jdedate)

    @classmethod
    def convertToInt(self, data, default=0):
        try:
            value = int(data)
        except:
            value = default

        return value

    @classmethod
    def convertToFloat(self, data, default=0.0):
        try:
            value = float(data)
        except:
            value = default

        return value

    @classmethod
    def convertToChar(self, data, default=""):
        if data is None:
            return ""
        else:
            return data.encode("utf-8")

    @classmethod
    def convertToDate(self, data, hora=True):
        if data is None:
            return None
        else:
            if hora:
                return datetime.strptime(
                    data.replace("Z", ""),
                    '%Y-%m-%dT%H:%M:%S'
                )
            else:
                return datetime.strptime(data.replace("Z", ""), '%Y-%m-%d')

    @classmethod
    def convertToUrl(self, ruta, file_name):
        url = os.path.join(ruta, file_name)

        return url.replace("\\", "/")
