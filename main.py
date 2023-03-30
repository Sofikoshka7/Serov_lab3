import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np

A = np.array([[-1, -1], [1, -2], [-3, 2], [-1, 0],[1, 0], [0, -1],[0, 1],[-1,-1],[-1,3]])
b = np.array([-26, 13, 26, 0,52,0,39,-65,78])
c = np.array([3, -1])
res = linprog(c, A_ub=A, b_ub=b)

print('Оптимальное решение:', round(res.fun*-1, ndigits=2),
      '\nХ:', res.x)

fig = plt.figure()
grid1 = plt.grid(True)
plt.xlabel("x1")
plt.ylabel("x2")
plt.text(30, 26, "0<=x1<=52", color='blue', fontsize=10)
plt.text(30, 24, "x1-3x2>=-78", color='orange', fontsize=10)
plt.text(30, 22, "x1+x2>=65", color='green', fontsize=10)
plt.text(30, 20, "x1-2x2<=13", color='red', fontsize=10)
plt.text(30, 18, "0<=x2<=39", color='purple', fontsize=10)

plt.text(45.2, 30.5, "D",fontsize=35)
plt.text(45.2, 32.5, "~",fontsize=32)

graph1 = plt.plot([52,52], [39,19.5], color='blue') # синий
graph2 = plt.plot([29.3,39], [35.8,39], color='orange') # оранжевый
graph3 = plt.plot([29.3,47.7], [35.8,17.3], color='green') # зеленый
graph4 = plt.plot([47.7,52], [17.3,19.5], color='red') # красный
graph5 = plt.plot([39,52], [39,39], color='purple') #фиолетовый

plt.show()
