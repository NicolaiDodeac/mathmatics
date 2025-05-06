import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # для 3D-графіків

# Створюємо координатну сітку
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Функція багатьох змінних
z = np.sin(x) * np.cos(y)

# Створення графіка
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Побудова поверхні
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Підписи осей
ax.set_title('f(x, y) = sin(x) * cos(y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.colorbar(surf, ax=ax, shrink=0.5, aspect=10)  # кольорова шкала
plt.show()
