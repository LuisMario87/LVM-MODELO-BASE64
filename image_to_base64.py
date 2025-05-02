import base64

def image_to_base64(ruta_imagen):
    """
    Convierte una imagen en base64 string.
    """
    with open(ruta_imagen, 'rb') as img_file:
        base64_bytes = base64.b64encode(img_file.read())
        base64_string = base64_bytes.decode('utf-8')
    return base64_string

