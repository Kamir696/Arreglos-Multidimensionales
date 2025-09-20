import numpy as np

#Ponemos la dimensión del espacio 3D
dim = 3

# Usamos un array de objetos para almacenar diccionarios
fluido = np.empty((dim, dim, dim), dtype=object)

# Comenzamos el estado del fluido
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            fluido[i, j, k] = {
                'presion': 1.0,  # presión inicial uniforme
                'temperatura': 300.0,  # temperatura constante (K)
                'velocidad': np.array([0.0, 0.0, 0.0])  # velocidad inicial cero
            }

# Introducimos una perturbación de presión en el centro
fluido[1, 1, 1]['presion'] = 10.0

def vecinos(i, j, k, dim):
    #Devuelve las coordenadas de los vecinos inmediatos (6 vecinos) dentro del rango.
    vecinos = []
    if i > 0: vecinos.append((i-1, j, k))
    if i < dim-1: vecinos.append((i+1, j, k))
    if j > 0: vecinos.append((i, j-1, k))
    if j < dim-1: vecinos.append((i, j+1, k))
    if k > 0: vecinos.append((i, j, k-1))
    if k < dim-1: vecinos.append((i, j, k+1))
    return vecinos

def actualizar_presion(fluido, dim, alpha=0.5):
    #Actualiza la presión en cada celda en función de la presión de sus vecinos
    nuevo_estado = np.empty((dim, dim, dim), dtype=object)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                p_actual = fluido[i, j, k]['presion']
                vecinos_coords = vecinos(i, j, k, dim)
                p_vecinos = [fluido[x, y, z]['presion'] for (x, y, z) in vecinos_coords]
                # Promedio de presión vecinos
                p_promedio = np.mean(p_vecinos) if p_vecinos else p_actual
                # Actualización simple: mezcla entre presión actual y promedio vecinos
                p_nueva = (1 - alpha) * p_actual + alpha * p_promedio

                # Copiamos temperatura y velocidad sin cambios
                nuevo_estado[i, j, k] = {
                    'presion': p_nueva,
                    'temperatura': fluido[i, j, k]['temperatura'],
                    'velocidad': fluido[i, j, k]['velocidad']
                }
    return nuevo_estado

# Simulación de propagación de ondas de presión
pasos = 5
print("Presión inicial en el centro:", fluido[1,1,1]['presion'])
for paso in range(pasos):
    fluido = actualizar_presion(fluido, dim)
    print(f"Paso {paso+1}, presión en el centro: {fluido[1,1,1]['presion']:.3f}")

# Mostrar presión final en toda la matriz
print("\nPresión final en cada celda:")
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            print(f"({i},{j},{k}): {fluido[i,j,k]['presion']:.3f}", end="  ")
        print()
    print()
