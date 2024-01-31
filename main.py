import numpy as np
import matplotlib.pyplot as plt


# Функция для вычисления первой производной от sin(x)
def f(x):
    return np.sin(x)


# Функция для вычисления приближенной аналитической формулы первой производной (нашла ее в лекции стр. 54 формула 8.1)
def derivative_lagrange_analytical(xi, yi, x):
    n = len(xi)
    result = 0.0

    for j in range(n):
        term = yi[j]
        factor = 0.0

        for k in range(n):
            if k != j:
                product = 1.0
                for i in range(n):
                    if i != j and i != k:
                        product *= (x - xi[i]) / (xi[j] - xi[i])
                factor += 1 / (xi[j] - xi[k]) * product

        term *= factor
        result += term

    return result


# Вычисление точной производной функции sin(x) в точке x=0
exact_derivative = np.cos(0)

# Расчет ошибок вычисления производной delta_f'(0) от числа n
n_values = np.arange(2, 32, 1)  # Значения n от 2 до 32 с шагом 1
errors_analytical = []

for n in n_values:
    xi = np.linspace(-np.pi, np.pi, n)
    yi = f(xi)

    # Аналитический метод
    interpolated_derivative_analytical = derivative_lagrange_analytical(xi, yi, 0)
    error_analytical = abs(interpolated_derivative_analytical - exact_derivative)
    errors_analytical.append(error_analytical)

# График зависимости ошибок от числа n
plt.figure(figsize=(8, 6))
plt.plot(n_values, errors_analytical, marker='o', linestyle='-', color='red')
plt.xlabel('Число узлов (n)')
plt.ylabel('Ошибка в вычислении производной')
plt.title('Зависимость ошибок от числа узлов')
plt.grid(True)
plt.show()
