import os
import stat
import sys
import datetime

def absoluteReturnsMetadata(path):
    try:
        size = os.path.getsize(path)
    except OSError:
        print("La Ruta '%s' no existe o es inaccesible" % path)
        sys.exit()

    print()
    #Imprime todos los metadatos del archivo
    #print(os.stat(path))
    dt_ctime = datetime.datetime.fromtimestamp(os.stat(path).st_ctime)
    dt_mtime = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
    dt_atime = datetime.datetime.fromtimestamp(os.stat(path).st_atime)
    print("El ultimo acceso al directorio fue: " + str(dt_ctime))
    print("La modificación más reciente fue: " + str(dt_mtime))
    print("La acceso más reciente fue: " + str(dt_atime))
    print("El tamaño del archivo es : " + str(os.stat(path).st_size) + " bytes")
    print("El id de grupo del propietario del archivo es: " + str(os.stat(path).st_gid))
    print("El id de usuario del propietario del archivo es: " + str(os.stat(path).st_uid))
    print("El número de enlaces al archivo es: " + str(os.stat(path).st_nlink))
    print("El id del dispositivo en el que reside el archivo es: " + str(os.stat(path).st_dev))
    print("El número de inodo en Unix es: " + str(os.stat(path).st_ino))
    print("Los permisos del archivo son: " + stat.filemode(os.stat(path).st_mode))