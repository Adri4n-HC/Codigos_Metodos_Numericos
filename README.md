# Proyecto: Métodos Numéricos (Raíces de Ecuaciones)

Este repositorio contiene una colección de herramientas en **Python** para resolver ecuaciones no lineales. Fue desarrollado como parte de la materia de "Métodos Numéricos".

# Métodos Implementados

El proyecto incluye los 5 algoritmos principales para encontrar raíces (f(x) = 0):

* **Bisección (`Biseccion.py`):** Método cerrado que divide el intervalo sistemáticamente.
* **Falsa Posición (`Falsa_Posicion.py`):** Utiliza interpolación lineal para una convergencia más rápida que la bisección.
* **Newton-Raphson (`Newton_Raphson.py`):** Método abierto de alto rendimiento que usa **derivadas automáticas** (SymPy).
* **Secante (`Secante.py`):** Una alternativa a Newton que no requiere conocer la derivada de la función.
* **Punto Fijo (`Punto_Fijo.py`):** Basado en la iteración de la forma despejada $x = g(x)$.

#  Requisitos e Instalación

Para que el método de **Newton-Raphson** funcione correctamente, necesitas la librería **SymPy**:
