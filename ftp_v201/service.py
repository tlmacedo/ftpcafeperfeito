import io
from base64 import b64encode


def blob2base64(image_data):
    return b64encode(image_data).decode('ascii')


def bytes2image(bytes):
    print('tentando abrir imagem')


def image2bytes():
    img_bytes = io.BinaryIO()
