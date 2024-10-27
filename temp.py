import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import math

#1. Asl funksiyani yasaymi
def original_functions(x):
    return x**2+2*x+5

#2. Ma'lumotlarni tanlaymiz
x_points = np.array([i for i in range(0,10)])
y_points = np.array([original_functions(i) for i in range(0,10)])

#3.Kubik splaynni yaratamiz
spline_function = CubicSpline(x_points, y_points)

# 4. Grafik uchun kengaytirilgan x qiymatlari
x_fine = np.linspace(0, 5, 100)
# 5. Grafik chizish
plt.figure(figsize=(14, 8))

# Asl funksiyani chizish
plt.plot(x_fine, original_functions(x_fine), 'r-', label='Asl funksiyamiz: $y = x^2 + 2x + 5$')

# Splayn funksiyasini chizish
plt.plot(x_fine, spline_function(x_fine), 'b--', label='Kubik splayn interpolyatsiyasi')

# Splayn uzluksizligini tekshirish uchun birinchi va ikkinchi hosilalarni chizish
# Birinchi hosila
plt.plot(x_fine, spline_function(x_fine, 1), 'g-', label="Splayn funksiyadan 1-tartibli hosila")
# Ikkinchi hosila
plt.plot(x_fine, spline_function(x_fine, 2), 'm-', label="Splayn funksiyadan 2-tartibli hosila")

# Belgilar va jadval
plt.scatter(x_points, y_points, color='black', label="Ma'lumotlar nuqtalari")
plt.legend(loc='upper left')
plt.title("$y = x^2 + 2x + 5$ funksiya uchun Kubik splayn funksiya")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Grafiklarni ko'rsatish
plt.show()