import math

def biseccion():
    print("--- Método de Bisección ---")
    
    # 1. Entrada de la función y parámetros
    func_str = input("Introduce f(x) (ejemplo: x**3 + 4*x**2 - 10): ").replace('^', '**')
    
    def f(x):
        # Permite usar funciones de math como sin, cos, exp, etc.
        return eval(func_str, {"x": x, "__builtins__": None}, {
            "sin": math.sin, "cos": math.cos, "exp": math.exp, 
            "log": math.log, "sqrt": math.sqrt, "tan": math.tan
        })

    try:
        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))
        tol = float(input("Margen de error (tolerancia): "))
        max_iter = int(input("Máximo de iteraciones: "))

        # 2. Validación del Teorema de Bolzano
        if f(a) * f(b) >= 0:
            print("\n[!] Error: f(a) y f(b) no tienen signos opuestos.")
            print("No se garantiza una raíz en este intervalo.")
            return

        # 3. Encabezado de la tabla de resultados
        print(f"\n{'Iter':<5} | {'a':<10} | {'b':<10} | {'m':<10} | {'f(m)':<10} | {'Error':<10}")
        print("-" * 75)

        # 4. Ciclo de iteraciones
        for i in range(1, max_iter + 1):
            m = (a + b) / 2
            fm = f(m)
            error = abs(b - a) / 2 # Error absoluto máximo
            
            print(f"{i:<5} | {a:<10.6f} | {b:<10.6f} | {m:<10.6f} | {fm:<10.6f} | {error:<10.6f}")

            # Condición de parada
            if error < tol or abs(fm) < 1e-15:
                print("-" * 75)
                print(f"Raíz aproximada encontrada en x = {m:.6f}")
                return

            # Decidir el nuevo intervalo
            if f(a) * fm < 0:
                b = m
            else:
                a = m
        
        print("-" * 75)
        print("Aviso: Se alcanzó el máximo de iteraciones.")

    except Exception as e:
        print(f"\n[!] Error en los datos: {e}")

if __name__ == "__main__":
    biseccion()
