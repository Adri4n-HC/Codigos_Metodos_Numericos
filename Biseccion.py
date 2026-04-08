import math

def falsa_posicion():
    print("--- Método de Falsa Posición ---")
    func_str = input("f(x) = ").replace('^', '**')
    
    def f(x):
        return eval(func_str, {"x": x, "math": math, "__builtins__": None}, 
                    {"sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))
    tol = float(input("Tolerancia: "))
    max_iter = int(input("Máximo de iteraciones: "))

    if f(a) * f(b) >= 0:
        print("Error: No hay cambio de signo en el intervalo.")
        return

    print(f"\n{'Iter':<5} | {'a':<10} | {'b':<10} | {'xr':<10} | {'f(xr)':<10}")
    print("-" * 60)

    for i in range(1, max_iter + 1):
        # Fórmula de Falsa Posición
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        fxr = f(xr)
        
        print(f"{i:<5} | {a:<10.6f} | {b:<10.6f} | {xr:<10.6f} | {fxr:<10.6f}")

        if abs(fxr) < tol:
            break
        
        if f(a) * fxr < 0:
            b = xr
        else:
            a = xr

    print(f"\nRaíz aproximada: {xr:.6f}")

if __name__ == "__main__":
    falsa_posicion()
