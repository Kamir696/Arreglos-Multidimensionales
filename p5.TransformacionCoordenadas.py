import numpy as np
import matplotlib.pyplot as plt

# Definimos un conjunto de puntos (x, y)
puntos = np.array([
    [1, 1],
    [2, 1],
    [3, 1],
    [1, 2],
    [2, 2],
    [3, 2]
])

# Ángulo de rotación en grados
angulo_grados = 45
angulo_rad = np.deg2rad(angulo_grados)

# Matriz de rotación 2x2
matriz_rotacion = np.array([
    [np.cos(angulo_rad), -np.sin(angulo_rad)],
    [np.sin(angulo_rad),  np.cos(angulo_rad)]
])

# Aplicamos la transformación (rotación)
puntos_transformados = puntos @ matriz_rotacion.T  # multiplicación matricial

# Visualización
plt.figure(figsize=(8, 8))
plt.scatter(puntos[:, 0], puntos[:, 1], color='blue', label='Original')
plt.scatter(puntos_transformados[:, 0], puntos_transformados[:, 1], color='red', label='Rotados')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title(f'Rotación de puntos {angulo_grados}°')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
