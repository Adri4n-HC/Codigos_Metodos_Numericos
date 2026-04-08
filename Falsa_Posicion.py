import math

def falsa_posicion():
    print("--- Método de Falsa Posición ---")
    print("Instrucciones: Introduce f(x) usando 'x'. Ejemplo: x**2 - 5, exp(x) - 4")
    
    func_str = input("f(x) = ").replace('^', '**')
    
    def f(x):
        contexto = {
            "x": x, "e": math.e, "exp": math.exp, "pi": math.pi,
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt
        }
        return eval(func_str, {"__builtins__": None}, contexto)

    try:
        a = float(input("Límite inferior (a): "))
        b = float(input("Límite superior (b): "))
        tol = float(input("Tolerancia: "))
        max_iter = int(input("Máximo de iteraciones: "))

        if f(a) * f(b) >= 0:
            print("\n[!] Error: No hay cambio de signo en el intervalo.")
            return

        print(f"\n{'Iter':<5} | {'xr':<10} | {'f(xr)':<10} | {'Error':<10}")
        print("-" * 50)

        xr_vieja = a
        for i in range(1, max_iter + 1):
            # Fórmula de Falsa Posición (Intersección de la secante)
            fa, fb = f(a), f(b)
            xr = b - (fb * (a - b)) / (fa - fb)
            fxr = f(xr)
            
            # Error relativo aproximado
            error = abs((xr - xr_vieja) / xr) * 100 if xr != 0 else 0
            
            print(f"{i:<5} | {xr:<10.6f} | {fxr:<10.6f} | {error:<10.4f}%")

            if abs(fxr) < tol or error < (tol * 100):
                print("-" * 50)
                print(f"Raíz encontrada: {xr:.6f}")
                return

            # Decidir nuevo subintervalo
            if fa * fxr < 0:
                b = xr
            else:
                a = xr
            
            xr_vieja = xr
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    falsa_posicion()
