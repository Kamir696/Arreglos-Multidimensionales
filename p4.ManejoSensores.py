import numpy as np
import matplotlib.pyplot as plt

# Datos simulados: 5 momentos en el tiempo (filas), 5 sensores (columnas)
np.random.seed(42)
datos = 20 + 5 * np.random.randn(5, 5)  # Temperaturas con media ~20 y ruido

print("Datos de temperatura (°C):")
print(datos)

# Cálculo de promedios y desviaciones estándar por sensor (columnas)
promedios_sensores = np.mean(datos, axis=0)
desv_sensores = np.std(datos, axis=0)

# Cálculo de promedios y desviaciones estándar por momento (filas)
promedios_momentos = np.mean(datos, axis=1)
desv_momentos = np.std(datos, axis=1)

print("\nPromedios por sensor:")
print(promedios_sensores)
print("Desviaciones estándar por sensor:")
print(desv_sensores)

print("\nPromedios por momento:")
print(promedios_momentos)
print("Desviaciones estándar por momento:")
print(desv_momentos)

# Visualización
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Promedio por sensor
axs[0, 0].bar(range(1, 6), promedios_sensores, color='skyblue')
axs[0, 0].set_title('Promedio por sensor')
axs[0, 0].set_xlabel('Sensor')
axs[0, 0].set_ylabel('Temperatura (°C)')
axs[0, 0].set_xticks(range(1, 6))

# Desviación estándar por sensor
axs[0, 1].bar(range(1, 6), desv_sensores, color='salmon')
axs[0, 1].set_title('Desviación estándar por sensor')
axs[0, 1].set_xlabel('Sensor')
axs[0, 1].set_ylabel('Desviación estándar (°C)')
axs[0, 1].set_xticks(range(1, 6))

# Promedio por momento
axs[1, 0].bar(range(1, 6), promedios_momentos, color='lightgreen')
axs[1, 0].set_title('Promedio por momento')
axs[1, 0].set_xlabel('Momento en el tiempo')
axs[1, 0].set_ylabel('Temperatura (°C)')
axs[1, 0].set_xticks(range(1, 6))

# Desviación estándar por momento
axs[1, 1].bar(range(1, 6), desv_momentos, color='orange')
axs[1, 1].set_title('Desviación estándar por momento')
axs[1, 1].set_xlabel('Momento en el tiempo')
axs[1, 1].set_ylabel('Desviación estándar (°C)')
axs[1, 1].set_xticks(range(1, 6))

plt.tight_layout()
plt.show()
