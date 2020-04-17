from base64 import b64encode

# from PIL import Image, ImageGrab


def blob2base64(image_data):
    if image_data is None:
        return None
    return b64encode(image_data).decode('ascii')


def bytes2image(bytes):
    print('tentando abrir imagem')
    # Image.open(io.BytesIO(bytes))


def image2bytes(pathFile):
    with open(pathFile, "rb") as imageFile:
        img_byte = imageFile.read()
        # img.save(img_bytes, format='PNG')
        print(img_byte)
        return img_byte
    # return img_bytes.getbuffer()
