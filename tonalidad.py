import cv2
import numpy as np

# Leer imagen en escala de grises
gris = cv2.imread("lenna_libre - copia.bmp", cv2.IMREAD_GRAYSCALE)

if gris is None:
    raise FileNotFoundError("No se encontro la imagen")

alto, ancho = gris.shape

# Convertir gris a una base a color
# Aqui usamos el gris como luz, pero ajustamos cada canal para que se vea mas viva
b = np.clip(gris * 0.90, 0, 255).astype(np.uint8)
g = np.clip(gris * 1.00, 0, 255).astype(np.uint8)
r = np.clip(gris * 1.15, 0, 255).astype(np.uint8)

# OpenCV guarda en BGR
img_color = cv2.merge([b, g, r])

# -----------------------------
# Toque rosado en la parte superior
# -----------------------------
overlay1 = img_color.copy()
cv2.ellipse(
    overlay1,
    (int(ancho * 0.42), int(alto * 0.18)),
    (int(ancho * 0.22), int(alto * 0.15)),
    0, 0, 360,
    (170, 140, 210),   # BGR rosado suave
    -1
)

img_color = cv2.addWeighted(img_color, 0.88, overlay1, 0.12, 0)

# -----------------------------
# Toque azul suave en el fondo
# -----------------------------
overlay2 = img_color.copy()
cv2.rectangle(
    overlay2,
    (0, 0),
    (ancho, alto),
    (210, 190, 160),   # BGR azul/gris suave
    -1
)

img_color = cv2.addWeighted(img_color, 0.90, overlay2, 0.10, 0)

# -----------------------------
# Un poco mas de color con HSV
# -----------------------------
hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

# subir saturacion
hsv[:, :, 1] = np.clip(hsv[:, :, 1].astype(np.float32) * 1.35, 0, 255).astype(np.uint8)

# mantener brillo bonito
hsv[:, :, 2] = np.clip(hsv[:, :, 2].astype(np.float32) * 1.00, 0, 255).astype(np.uint8)

final = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Guardar resultado final
cv2.imwrite("imagen_final_color.png", final)

print("Proceso terminado")
