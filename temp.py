# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import CubicSpline
# import math

# #1. Asl funksiyani yasaymi
# def original_functions(x):
#     return x**2+2*x+5

# #2. Ma'lumotlarni tanlaymiz
# x_points = np.array([i for i in range(0,10)])
# y_points = np.array([original_functions(i) for i in range(0,10)])

# #3.Kubik splaynni yaratamiz
# spline_function = CubicSpline(x_points, y_points)

# # 4. Grafik uchun kengaytirilgan x qiymatlari
# x_fine = np.linspace(0, 5, 100)
# # 5. Grafik chizish
# plt.figure(figsize=(14, 8))

# # Asl funksiyani chizish
# plt.plot(x_fine, original_functions(x_fine), 'r-', label='Asl funksiyamiz: $y = x^2 + 2x + 5$')

# # Splayn funksiyasini chizish
# plt.plot(x_fine, spline_function(x_fine), 'b--', label='Kubik splayn interpolyatsiyasi')

# # Splayn uzluksizligini tekshirish uchun birinchi va ikkinchi hosilalarni chizish
# # Birinchi hosila
# plt.plot(x_fine, spline_function(x_fine, 1), 'g-', label="Splayn funksiyadan 1-tartibli hosila")
# # Ikkinchi hosila
# plt.plot(x_fine, spline_function(x_fine, 2), 'm-', label="Splayn funksiya+dan 2-tartibli hosila")

# # Belgilar va jadval
# plt.scatter(x_points, y_points, color='black', label="Ma'lumotlar nuqtalari")
# plt.legend(loc='upper left')
# plt.title("$y = x^2 + 2x + 5$ funksiya uchun Kubik splayn funksiya")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)

# # Grafiklarni ko'rsatish
# plt.show()

# import numpy as np
# from scipy.interpolate import lagrange
# import matplotlib.pyplot as plt

# X = np.array([5, 7, 13, 15, 10, 3])
# Y = np.array([0, 5, 10, 15, 20, 24])

# x=12
# def langranj(item, array1,array2):
#     poly = lagrange(array1,array2)
#     sum=0
#     for i in range(len(array1)-1,-1,-1):
#         sum+=poly[i]*item**i
#     return {
#         "summa":sum,
#         "kuphad":poly
#     }

# plt.xlabel("X data")
# plt.ylabel("Y data")
# plt.title(f"Lagrang ko'phadi: \n\n{langranj(x,X,Y)['kuphad']}\nX={x} bo'lganda yechim: {langranj(x,X,Y)['summa']}")
# plt.plot(X,Y,color='red')
# plt.show() 