from ultralytics import YOLO
import cv2

def detect_with_yolo(ruta_modelo, ruta_imagen_entrada, ruta_imagen_salida):
    """
    Realiza detección usando un modelo YOLO y guarda la imagen detectada.
    """
    # Cargar el modelo
    model = YOLO(ruta_modelo)

    # Realizar la detección
    results = model(ruta_imagen_entrada)

    for result in results:
        result_image = result.plot()  # Devuelve numpy array de la imagen detectada

    # Guardar la imagen detectada
    cv2.imwrite(ruta_imagen_salida, result_image)

