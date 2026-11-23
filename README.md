# EDO separable — Solución exacta vs Método de Euler

## Problema

Se resuelve la ecuación diferencial separable:

$$
\frac{dy}{dt} = -2\,t\,y, \qquad y(0) = 1
$$

en el intervalo $t \in [0, 1]$ con paso $h = 0.2$.

## Solución analítica (separación de variables)

$$
\frac{dy}{y} = -2t\,dt
\;\Longrightarrow\;
\ln|y| = -t^2 + C
\;\Longrightarrow\;
y(t) = C\,e^{-t^2}
$$

Con $y(0)=1$ se obtiene $C=1$:

$$
\boxed{y(t) = e^{-t^2}}
$$

## Método de Euler

$$
y_{i+1} = y_i + h\,(-2\,t_i\,y_i), \qquad y_0 = 1,\; h = 0.2
$$

## Resultados

| t    | Euler    | Exacta   | Error abs |
|------|----------|----------|-----------|
| 0.0  | 1.000000 | 1.000000 | 0.000000  |
| 0.2  | 1.000000 | 0.960789 | 0.039211  |
| 0.4  | 0.920000 | 0.852144 | 0.067856  |
| 0.6  | 0.772800 | 0.697676 | 0.075124  |
| 0.8  | 0.588993 | 0.527292 | 0.061700  |
| 1.0  | 0.399935 | 0.367879 | 0.032055  |

El error máximo es ≈ **0.075** en $t \approx 0.6$. Como Euler es de orden 1,
el error es proporcional a $h$; reducirlo a $h=0.1$ lo disminuiría a la mitad
aproximadamente.

## Estructura
.
├── euler_edo.py # Código principal
├── euler_solution.png # Gráfica generada
└── README.md


## Requisitos y ejecución

```bash
pip install numpy matplotlib
python euler_edo.py

