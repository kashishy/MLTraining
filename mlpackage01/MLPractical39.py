import matplotlib.pyplot as plt

x1 = [1, 2, 3]
x2 = [1, 2, 3]

y1 = [1, 2, 3]
y2 = [1, 4, 9]

# multiple lines with same formatting in one attempt
plt.plot(x1, y1, x2, y2, linewidth=3)
plt.show()