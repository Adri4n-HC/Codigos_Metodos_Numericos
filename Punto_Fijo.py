import math

def punto_fijo():
    print("--- Método de Iteración de Punto Fijo ---")
    print("Instrucciones: Despeja 'x' de tu función original f(x)=0 para obtener x = g(x)")
    print("Ejemplo: Para f(x) = x^2 - x - 2, una g(x) puede ser sqrt(x + 2)")
    
    # Reemplazamos ^ por ** por si el usuario usa notación de calculadora
    g_str = input("\ng(x) = ").replace('^', '**')
    
    def g(x_val):
        # Definimos el contexto matemático para el eval
        contexto = {
            "x": x_val, 
            "math": math, 
            "exp": math.exp, 
            "e": math.e, 
            "sin": math.sin, 
            "cos": math.cos, 
            "sqrt": math.sqrt, 
            "log": math.log,
            "pi": math.pi
        }
        return eval(g_str, {"__builtins__": None}, contexto)

    try:
        x0 = float(input("Punto inicial (x0): "))
        tol = float(input("Tolerancia (ej. 0.001): "))
        max_iter = int(input("Máximo de iteraciones: "))

        print(f"\n{'Iter':<5} | {'xi':<12} | {'g(xi)':<12} | {'Error (%)':<12}")
        print("-" * 60)

        xi = x0
        for i in range(1, max_iter + 1):
            try:
                # Calculamos el siguiente valor
                nuevo_xi = g(xi)
            except (OverflowError, ValueError):
                print(f"[!] Error en la iteración {i}: El cálculo falló (posible divergencia o número imaginario).")
                return

            # Cálculo del error relativo porcentual
            if nuevo_xi != 0:
                error = abs((nuevo_xi - xi) / nuevo_xi) * 100
            else:
                error = 0
            
            # Imprimimos la fila de la tabla
            print(f"{i:<5} | {xi:<12.6f} | {nuevo_xi:<12.6f} | {error:<12.4f}%")

            # Condición de parada (si el error es menor a la tolerancia)
            if error < (tol * 100):
                print("-" * 60)
                print(f"Punto fijo (raíz) encontrado: {nuevo_xi:.6f}")
                return
            
            # Actualizamos xi para la siguiente vuelta
            xi = nuevo_xi

        print("-" * 60)
        print("Se alcanzó el límite de iteraciones. Revisa si el despeje g(x) es convergente.")

    except Exception as e:
        print(f"\n[!] Error en la entrada de datos: {e}")

if __name__ == "__main__":
    punto_fijo()
