import hashlib


def md5(fich):
    fp = open(fich, "rb")
    buffer = fp.read()
    hashObj = hashlib.md5()
    hashObj.update(buffer)
    lastHash = hashObj.hexdigest().upper()
    md5 = lastHash
    fp.close()
    return fich,md5