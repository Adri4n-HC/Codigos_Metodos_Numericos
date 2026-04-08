import sympy as sp #es necesario tener instalada la carpeta sympy

def newton_raphson_sympy():
    print("--- Método de Newton-Raphson (Derivada Automática) ---")
    
    # 1. Definir la variable simbólica
    x_sim = sp.Symbol('x')
    
    print("Instrucciones: Introduce f(x) usando 'x'. Ejemplo: x**3 + 4*x**2 - 10")
    func_input = input("f(x) = ").replace('^', '**')

    try:
        # 2. Convertir texto a función simbólica y derivar
        f_simbolica = sp.sympify(func_input)
        df_simbolica = sp.diff(f_simbolica, x_sim)
        
        print(f"\n> Derivada calculada automáticamente: f'(x) = {df_simbolica}")

        # 3. Convertir a funciones numéricas rápidas (lambdify)
        f = sp.lambdify(x_sim, f_simbolica, 'math')
        df = sp.lambdify(x_sim, df_simbolica, 'math')

        # 4. Parámetros del método
        x0 = float(input("\nPunto inicial (x0): "))
        tol = float(input("Tolerancia: "))
        max_iter = int(input("Máximo de iteraciones: "))

        print(f"\n{'Iter':<5} | {'xi':<10} | {'f(xi)':<10} | {'Error':<10}")
        print("-" * 50)

        xi = x0
        for i in range(1, max_iter + 1):
            f_val = f(xi)
            df_val = df(xi)

            if abs(df_val) < 1e-15:
                print("[!] Error: La derivada es cero en este punto.")
                return

            # Fórmula de Newton-Raphson
            nuevo_xi = xi - f_val / df_val
            
            # Error relativo porcentual
            error = abs((nuevo_xi - xi) / nuevo_xi) * 100 if nuevo_xi != 0 else 0
            
            print(f"{i:<5} | {xi:<10.6f} | {f_val:<10.6f} | {error:<10.4f}%")

            if error < (tol * 100) or abs(f_val) < 1e-15:
                print("-" * 50)
                print(f"Raíz encontrada: {nuevo_xi:.6f}")
                return
            
            xi = nuevo_xi

        print("Se alcanzó el límite de iteraciones.")

    except Exception as e:
        print(f"\n[!] Error: Asegúrate de escribir bien la función. Detalle: {e}")

if __name__ == "__main__":
    newton_raphson_automatico()
