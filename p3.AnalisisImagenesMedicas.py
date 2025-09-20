import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Simulamos un volumen 3D: 10 capas de imágenes 2D de 100x100 píxeles con ruido
np.random.seed(0)
volumen = np.random.rand(10, 100, 100) * 255  # valores entre 0 y 255
volumen = volumen.astype(np.float32)

# Kernel de promedio 3x3
kernel = np.ones((3, 3)) / 9

# Función para suavizar cada capa con filtro promedio
def suavizar_volumen(volumen, kernel):
    volumen_suavizado = np.empty_like(volumen)
    for i in range(volumen.shape[0]):
        volumen_suavizado[i] = convolve(volumen[i], kernel, mode='reflect')
    return volumen_suavizado

# Aplicamos suavizado
volumen_suavizado = suavizar_volumen(volumen, kernel)

# Mostrar una capa antes y después
capa = 5
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Capa original")
plt.imshow(volumen[capa], cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Capa suavizada")
plt.imshow(volumen_suavizado[capa], cmap='gray')
plt.axis('off')

plt.show()
