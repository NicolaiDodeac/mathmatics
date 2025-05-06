# Знайдемо графічно екстремум функції y = x2−3x+5y=x2−3x+5 
# за допомогою бібліотеки sympy та побудуємо графік за допомогою matplotlib.



# Приклад 9

import matplotlib.pyplot as plt
from sympy import diff, symbols


fig, ax = plt.subplots()


# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')


x, y = symbols('x y')
# Задаємо функцію
fx = x*x-3*x+5
# Обраховуємо похідну функції
dx = diff((fx))
k = []
n = []
l = []


for i in range(1000):
    j = (i-300)*0.01
    k.append(j)
    n.append(dx.subs(x,j))
    l.append(fx.subs(x,j))



ax.plot(k,n)
ax.plot(k,l)

# 1. Знаходимо екстремум: f'(x) = 0 → x_ext = 1.5
x_ext = 1.5
y_ext = fx.subs(x, x_ext)  # обчислюємо f(1.5)

# 2. Малюємо червону крапку на графіку функції
ax.plot(x_ext, y_ext, 'ro', label='Екстремум')  # 'ro' = red circle

# 3. Додаємо підпис
ax.annotate(f'Extremum ({x_ext}, {y_ext})',
            xy=(x_ext, y_ext),
            xytext=(x_ext + 0.5, y_ext + 1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10)

# Побудова дотичної в точці x_ext
import numpy as np

# Обчислюємо похідну f'(x_ext)
slope = dx.subs(x, x_ext)

# Створимо x-координати для дотичної (навколо x_ext)
tangent_x = np.linspace(x_ext - 2, x_ext + 2, 100)
# Формула дотичної: y = f(x0) + f'(x0)*(x - x0)
tangent_y = [y_ext + slope*(xi - x_ext) for xi in tangent_x]

# Побудуємо дотичну (зелена пунктирна лінія)
ax.plot(tangent_x, tangent_y, 'g--', label='Дотична в x=1.5')

# Запускаємо малювання графіка
plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
# from sympy import symbols, diff

# # Символічні змінні
# x = symbols('x')

# # Функція та похідна
# fx = x**2 - 3*x + 5
# dfx = diff(fx)

# # Перетворюємо функції на звичайні Python-функції
# f_func = lambda val: val**2 - 3*val + 5
# df_func = lambda val: 2*val - 3

# # Побудова x-координат
# x_vals = np.linspace(-3, 7, 1000)
# f_vals = [f_func(xi) for xi in x_vals]
# df_vals = [df_func(xi) for xi in x_vals]

# # Точка екстремуму
# x_ext = 1.5
# y_ext = f_func(x_ext)
# slope = df_func(x_ext)

# # Побудова дотичної
# tangent_x = np.linspace(x_ext - 2, x_ext + 2, 100)
# tangent_y = y_ext + slope * (tangent_x - x_ext)

# # Побудова графіків
# fig, ax = plt.subplots()
# ax.plot(x_vals, f_vals, label='f(x) = x² - 3x + 5', color='orange')
# ax.plot(x_vals, df_vals, label="f'(x) = 2x - 3", color='blue')
# ax.plot(x_ext, y_ext, 'ro', label='Екстремум f(x)')
# ax.plot(x_ext, 0, 'bo', label="f'(x) = 0")
# ax.plot(tangent_x, tangent_y, 'g--', label='Дотична до f(x)')
# ax.axhline(0, color='gray', linestyle='--', linewidth=1)

# # Анотація
# ax.annotate(f'Extremum ({x_ext}, {y_ext})',
#             xy=(x_ext, y_ext),
#             xytext=(x_ext + 0.5, y_ext + 1),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             fontsize=9)

# # Оформлення
# ax.set_xlabel('x')
# ax.set_ylabel('f(x), f\'(x)')
# ax.legend()
# ax.grid(True, linestyle='-.')
# ax.set_title('Графік функції, її похідної та екстремуму')
# plt.show()
