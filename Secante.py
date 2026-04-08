import math

def secante():
    print("--- Método de la Secante ---")
    print("Instrucciones: Introduce f(x) usando 'x'. Ejemplo: exp(3*x) - 4")
    
    func_str = input("f(x) = ").replace('^', '**')
    
    def f(x):
        # Usamos un diccionario para que reconozca funciones matemáticas
        contexto = {
            "x": x, "e": math.e, "exp": math.exp, "pi": math.pi,
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt
        }
        return eval(func_str, {"__builtins__": None}, contexto)

    try:
        # La secante requiere DOS puntos iniciales: x0 y x1
        x0 = float(input("Primer punto inicial (x0): "))
        x1 = float(input("Segundo punto inicial (x1): "))
        tol = float(input("Tolerancia (ej. 0.00001): "))
        max_iter = int(input("Máximo de iteraciones: "))

        print(f"\n{'Iter':<5} | {'xi':<10} | {'f(xi)':<10} | {'Error (%)':<10}")
        print("-" * 55)

        for i in range(1, max_iter + 1):
            f0 = f(x0)
            f1 = f(x1)

            # Evitar división por cero si la pendiente es plana
            if abs(f1 - f0) < 1e-15:
                print("[!] Error: La pendiente es nula, no se puede continuar.")
                return

            # Fórmula de la Secante
            x_nuevo = x1 - (f1 * (x1 - x0)) / (f1 - f0)
            
            # Cálculo del error relativo porcentual
            error = abs((x_nuevo - x1) / x_nuevo) * 100 if x_nuevo != 0 else 0
            
            print(f"{i:<5} | {x1:<10.6f} | {f1:<10.6f} | {error:<10.4f}%")

            # Condición de parada
            if error < (tol * 100) or abs(f1) < 1e-15:
                print("-" * 55)
                print(f"Raíz aproximada encontrada: {x_nuevo:.6f}")
                return
            
            # Actualización de puntos para la siguiente iteración
            x0 = x1
            x1 = x_nuevo

        print("Se alcanzó el límite de iteraciones.")

    except Exception as e:
        print(f"\n[!] Error en los datos: {e}")

if __name__ == "__main__":
    secante()
