import os
import absolutePath
import hashMD5

if __name__ == '__main__':
    print()
    name = input("Ingresa la Ruta ")
    absolutePath.absoluteReturnsMetadata(name)
    if (os.path.isfile(name)):
        ruta, lastHash = hashMD5.md5(name)
        print()
        print("Fichero: " + ruta)
        print("MD5: " + lastHash)
    else:
        print()
        print("La ruta ingresada no contiene un archivo, por lo tanto no se puede aplicar el Hash")












