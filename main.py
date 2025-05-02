from lvm_to_graph import lvm_to_graph
from detect_with_yolo import detect_with_yolo
from image_to_base64 import image_to_base64

def main():
    # Configuraciones
    ruta_lvm = 'ruta a tu lvm'  # Ajusta tu ruta
    imagen_salida = 'ruta donde se guardara la grafica generada con el LVM'
    modelo_yolo = 'ruta a carpeta modelo, usar \\best.pt de la carpeta'
    imagen_detectada = 'ruta donde se guardara la imagen con las detecciones del modelo'
    archivo_base64 = 'ruta donde se guardara el txt con la grafica en base64'
    
    # Paso 1: LVM ➔ Imagen
    lvm_to_graph(ruta_lvm, imagen_salida)
    print("[INFO] Gráfica creada.")

    # Paso 2: Imagen ➔ Detección YOLO
    detect_with_yolo(modelo_yolo, imagen_salida, imagen_detectada)
    print("[INFO] Detección realizada.")

    # Paso 3: Imagen ➔ Base64
    base64_resultado = image_to_base64(imagen_detectada) 
    print("[INFO] Imagen convertida a Base64.")

    # Paso 4: Guardar Base64 en archivo
    with open(archivo_base64, 'w') as f:
        f.write(base64_resultado)
    print(f"[INFO] Base64 guardado en {archivo_base64}")

    return base64_resultado

if __name__ == "__main__":
    main()
