import numpy as np

# Definimos una matriz de fuerzas aplicadas en una estructura simple
# Valores positivos hacia arriba, negativos hacia abajo
fuerzas = np.array([
    [0, -10, 0],
    [-5, 0, -5],
    [0, -10, 0]
])

# Calculamos la suma total de fuerzas para verificar equilibrio
suma_total = np.sum(fuerzas)

print("Matriz de fuerzas aplicadas (N):")
print(fuerzas)

print(f"\nSuma total de fuerzas: {suma_total} N")

# Para equilibrio se puso suma_total debe ser 0
# Si no es 0, calculamos la reacción necesaria para equilibrar
if suma_total != 0:
    # Suponemos que la reacción se aplica en el nodo central (1,1)
    reacciones = np.zeros_like(fuerzas)
    reacciones[1,1] = -suma_total
else:
    reacciones = np.zeros_like(fuerzas)

print("\nReacciones en los nodos para equilibrio (N):")
print(reacciones)

# Fuerzas netas después de aplicar reacciones
fuerzas_net = fuerzas + reacciones

print("\nFuerzas netas en los nodos después de reacciones (N):")
print(fuerzas_net)

print(f"\nSuma total de fuerzas netas: {np.sum(fuerzas_net)} N")
