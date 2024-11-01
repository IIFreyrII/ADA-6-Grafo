# ADA-6-Grafo

Este programa es básicamente una simulación de rutas entre estados, donde cada estado está conectado a otros con un costo. Cada estado es un "nodo" y cada conexión entre estados es una "arista" con un precio que representa el costo de ir de un lugar a otro. El programa hace varias cosas: recorre estos caminos en diferentes modos, dibuja el grafo para verlo visualmente y muestra todas las conexiones en un formato de texto.

El grafo es un diccionario donde cada estado tiene una lista de conexiones. Cada conexión indica a qué otro estado puedes ir desde el estado actual y cuánto cuesta llegar. Esto permite ver claramente todas las rutas y sus costos, como un mapa donde puedes ver todas las posibles direcciones y distancias.

Función recorrer_sin_repetir:

Esta función recorre los estados sin repetir. Usa un método llamado DFS (básicamente, una exploración de nodos en profundidad) para avanzar de un estado a otro sin volver a pasar por los ya visitados. Tiene una lista de "visitados" donde va marcando los estados que ya pasó para no caer en ciclos y una lista recorrido para guardar el camino que siguió. También va acumulando el costo total de todas las conexiones que hace. Esto es útil cuando quieres ver un recorrido único por el grafo sin repetir estados.

Función recorrer_con_repetir:

Esta función recorre el grafo permitiendo pasar por algunos estados más de una vez, lo que ayuda a explorar rutas adicionales. Sin embargo, se asegura de no quedarse atrapada en un ciclo infinito, ya que si el recorrido crece demasiado, el programa detiene la exploración. Aquí también se acumula el costo de las conexiones, y el recorrido final puede incluir revisitas, lo cual es útil para ver rutas más largas y no tan estrictas.

Función dibujar_grafo:

Esta función crea una imagen del grafo usando networkx, que es una biblioteca especializada en grafos. Lo que hace es transformar el diccionario de conexiones en un gráfico visual. Cada estado se convierte en un punto, y cada conexión se dibuja como una línea con su costo marcado, como un mapa de rutas. Esto te permite ver de un vistazo las conexiones entre estados y cómo están distribuidos en el espacio.

Función mostrar_relaciones:

Finalmente, esta función imprime cada estado junto con sus conexiones y costos de una forma entendible en texto. Si prefieres una salida en texto en lugar de un gráfico, esta función es perfecta. Simplemente muestra todas las conexiones estado por estado, lo cual ayuda a verificar rápidamente la estructura y relaciones en el grafo.

Ejecución del Programa
El programa arranca en un estado inicial que definimos (en este caso, 'Aguascalientes'). A partir de ahí, usa las funciones de recorrido para explorar rutas con y sin repeticiones, calcula el costo total de cada una, dibuja el grafo y finalmente imprime las relaciones en texto. Así puedes ver claramente no sólo los recorridos y sus costos, sino también cómo están conectados visualmente los estados y cuál es la estructura general del grafo.
