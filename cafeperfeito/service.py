import io
from base64 import b64encode

from PIL import Image, ImageGrab


def blob2base64(image_data):
    return b64encode(image_data).decode('ascii')


def bytes2image(bytes):
    print('tentando abrir imagem')
    Image.open(io.BytesIO(bytes))


def image2bytes():
    img = ImageGrab.grabclipboard()

    # Store the bytes in a byte stream
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    print(img_bytes.getvalue())
    return img_bytes.getvalue()
    # return img_bytes.getbuffer()
