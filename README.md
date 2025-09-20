****EJERCICIO 1****

****Enfoque****

Representación de fuerzas: Usaremos una matriz 3x3 donde cada elemento representa la fuerza aplicada en ese nodo (puede ser positiva o negativa según dirección).

Leyes de la estática: Para un sistema en equilibrio, la suma de fuerzas en cada dirección debe ser cero. Aquí simplificaremos y asumiremos fuerzas solo en una dirección (por ejemplo, vertical).

Reacciones en nodos: Calcularemos las reacciones en los nodos sumando las fuerzas aplicadas y asegurando que la suma total sea cero (equilibrio).


****Explicación de la solución****

Definimos una matriz 3x3 con fuerzas aplicadas en cada nodo.

Sumamos todas las fuerzas para verificar si el sistema está en equilibrio.


Si la suma no es cero, calculamos la reacción necesaria para equilibrar el sistema y la aplicamos en el nodo central.

Finalmente, mostramos las fuerzas netas después de aplicar las reacciones, que deben sumar cero.

****Influencia del enfoque en la eficiencia****

Simplicidad: Usar una matriz para representar fuerzas es intuitivo y permite operaciones vectorizadas con NumPy, lo que es eficiente para cálculos.

Escalabilidad: Para estructuras pequeñas (3x3), este método es muy eficiente y rápido.

Limitaciones: Para estructuras más complejas, este enfoque manual no es práctico. Se requerirían métodos matriciales más avanzados (como el método de elementos finitos), que aunque más complejos, son computacionalmente eficientes para grandes sistemas.


****EJERCICIO 2****

****Enfoque****

Representación del estado del fluido: Usamos un arreglo tridimensional 3x3x3, donde cada celda es un diccionario o estructura que contiene presión, temperatura y velocidad (vector 3D).

Simulación de propagación de ondas: Actualizamos la presión en cada celda como un promedio ponderado de la presión propia y la de sus vecinos inmediatos (6 vecinos en 3D: arriba, abajo, izquierda, derecha, adelante, atrás). Esto simula la difusión o propagación de presión.

Velocidad y temperatura: Para simplificar, mantenemos temperatura y velocidad constantes en esta simulación.

Iteraciones: Repetimos la actualización varias veces para simular la propagación en el tiempo.

****Explicación de la solución****


Inicializamos un espacio 3x3x3 con presión uniforme 1.0, temperatura 300 K y velocidad cero.

Introducimos una perturbación de presión en el centro (valor 10.0).

En cada paso, actualizamos la presión de cada celda como una mezcla entre su presión actual y el promedio de la presión de sus vecinos inmediatos.

La temperatura y velocidad permanecen constantes para simplificar.

La presión en el centro disminuye con el tiempo, mientras que la presión se propaga a las celdas vecinas, simulando una onda de presión.

****Influencia del enfoque en la eficiencia****

Simplicidad y claridad: El uso de un arreglo tridimensional con objetos permite almacenar múltiples propiedades por celda, facilitando la extensión del modelo.

Costo computacional: Para 3x3x3 es muy eficiente, pero el uso de objetos en NumPy no es óptimo para grandes volúmenes, ya que pierde la ventaja de operaciones vectorizadas.

Escalabilidad: Para simulaciones grandes, se recomienda usar arrays separados para cada propiedad (presión, temperatura, velocidad) y aprovechar operaciones vectorizadas y paralelización.

Actualización local: Solo se usan vecinos inmediatos, lo que limita la complejidad por celda a un número fijo de operaciones, ayudando a la eficiencia.

Iteraciones: El costo crece linealmente con el número de pasos de simulación.


****EJERCICIO 3****

****Enfoque****

Representación del volumen: Usamos un arreglo 3D NumPy donde cada "capa" (dimensión 0) es una imagen 2D.

Filtro de promedio: Para cada capa, aplicamos un filtro de convolución 2D con una máscara de promedio (kernel) para suavizar la imagen.

Visualización: Mostramos una capa antes y después del suavizado para evidenciar la mejora.

Eficiencia: Usamos funciones optimizadas de SciPy para convolución, que aprovechan implementaciones rápidas y vectorizadas.

****Explicación de la solución****


Creamos un volumen 3D con ruido aleatorio para simular imágenes médicas.

Definimos un kernel 3x3 de promedio para suavizar.

Aplicamos la convolución 2D en cada capa usando scipy.ndimage.convolve con modo reflect para manejar bordes.

Visualizamos una capa antes y después para mostrar la reducción de ruido.

****Influencia del enfoque en la eficiencia****

Separación por capas: Procesar capa por capa permite usar funciones optimizadas 2D, que son más rápidas y menos costosas que un filtro 3D completo.

Uso de SciPy: La función convolve está implementada en C y es muy eficiente, aprovechando operaciones vectorizadas.

Escalabilidad: Para volúmenes grandes, este enfoque es eficiente y puede paralelizarse fácilmente (procesar capas en paralelo).

Simplicidad: El filtro promedio es simple y rápido, pero puede suavizar detalles importantes. Para mejor calidad se usan filtros más avanzados (Gaussiano, mediana, bilateral).

Memoria: Se crea un nuevo volumen para almacenar el resultado, lo que duplica el uso de memoria temporalmente.


****EJERCICIO 4****

****Enfoque****

Organización de datos: Usamos un arreglo NumPy 2D para almacenar las temperaturas.

Análisis estadístico: Calculamos:

Promedio y desviación estándar por columna (sensor) — análisis por sensor.

Promedio y desviación estándar por fila (momento en el tiempo) — análisis temporal.

Visualización: Usamos gráficos de barras para mostrar promedios y desviaciones estándar de sensores y momentos.

Eficiencia: NumPy permite cálculos vectorizados rápidos sin bucles explícitos, lo que mejora la eficiencia.


****Explicación de la solución****


Creamos un arreglo 5x5 con datos simulados de temperatura.

Calculamos promedios y desviaciones estándar usando np.mean y np.std con axis=0 para columnas y axis=1 para filas.

Visualizamos los resultados con gráficos de barras para facilitar la interpretación.

****Influencia del enfoque en la eficiencia****

Uso de NumPy: Permite cálculos vectorizados, evitando bucles explícitos y acelerando el procesamiento.

Dimensiones pequeñas: Para 5x5, la eficiencia no es crítica, pero el enfoque escala bien para matrices más grandes.

Visualización clara: Separar análisis por filas y columnas facilita la interpretación sin necesidad de cálculos complejos.

Simplicidad: El código es compacto y fácil de mantener, lo que reduce errores y mejora la productividad.


****EJERCICIO 5****

****Enfoque****


Representación de puntos: Usamos un arreglo 2D de forma (n_puntos, 2), donde cada fila es un punto (x, y).

Transformación lineal: Aplicamos una matriz 2x2 de rotación para rotar los puntos alrededor del origen.

Visualización: Graficamos los puntos originales y transformados para comparar.

Eficiencia: El uso de multiplicación matricial vectorizada con NumPy es muy eficiente, evitando bucles y acelerando el cálculo.

****Explicación de la solución****


Creamos un arreglo 2D con puntos en coordenadas cartesianas.

Definimos la matriz de rotación para un ángulo dado.

Multiplicamos todos los puntos por la matriz de rotación usando operaciones vectorizadas.

Graficamos los puntos originales y rotados para visualizar el efecto.


****Influencia del enfoque en la eficiencia****

Vectorización: La multiplicación matricial con NumPy es altamente optimizada, evitando bucles explícitos y acelerando el cálculo.

Escalabilidad: Este método escala muy bien para grandes conjuntos de puntos, ya que la operación es paralelizable y eficiente.

Simplicidad: La representación con matrices facilita la extensión a otras transformaciones lineales (escalado, traslación con coordenadas homogéneas).

Memoria: Se usa memoria contigua para los datos, lo que mejora el acceso y la velocidad.
