import numpy as np
import matplotlib.pyplot as plt

# Definimos la ecuación diferencial: dy/dt = f(t, y)
# En este ejemplo: dy/dt = -2*t*y  (EDO separable)
def f(t, y):
    return -2 * t * y

# Método de Euler
def euler_method(f, t0, y0, t_end, h):
    # Inicializamos listas para almacenar los valores de t y y
    t_values = [t0]
    y_values = [y0]

    # Iteramos desde t0 hasta t_end con pasos de tamaño h
    t = t0
    y = y0
    while t < t_end - 1e-12:          # pequeña tolerancia para evitar un paso extra
        # Fórmula de Euler: y_{n+1} = y_n + h * f(t_n, y_n)
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

# Solución exacta (obtenida por separación de variables): y(t) = e^(-t^2)
def exact_solution(t):
    return np.exp(-(t ** 2))

# Parámetros del problema
t0 = 0        # Tiempo inicial
y0 = 1        # Condición inicial: y(0) = 1
t_end = 1     # Tiempo final (intervalo [0, 1])
h = 0.2       # Tamaño del paso

# Calculamos la solución numérica con el método de Euler
t_values, y_values = euler_method(f, t0, y0, t_end, h)

# Calculamos la solución exacta en los mismos puntos
t_array = np.array(t_values)
y_exact = exact_solution(t_array)

# ---------- Tabla de resultados por consola ----------
print(f"{'t':>6} {'Euler':>12} {'Exacta':>12} {'Error abs':>12}")
print("-" * 46)
for ti, yi, ye in zip(t_array, y_values, y_exact):
    print(f"{ti:6.2f} {yi:12.6f} {ye:12.6f} {abs(yi - ye):12.6f}")

# ---------- Gráfica ----------
plt.figure(figsize=(8, 6))
plt.plot(t_values, y_values, 'bo--', label='Solución numérica (Euler, h=0.2)')
plt.plot(t_values, y_exact, 'r-',  label='Solución exacta: $y(t) = e^{-t^2}$')
plt.title('Método de Euler vs Solución Exacta')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Guardamos y mostramos la gráfica
plt.savefig('euler_solution.png', dpi=150)
plt.show()