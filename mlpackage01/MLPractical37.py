import matplotlib.pyplot as plt

# Line formatting
# b- = Blue Solid Line ( - for line with '-' and b for color)
# ro = Red Circle Dot ( 0 for dot and r for red color)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')

plt.xlabel("-------Indexes-------")
plt.ylabel("-----some numbers----")

# for marking ticks on axis, first two numbers are for x-axis
# last two number are for y-axis
plt.axis([0, 5, 0, 17])
plt.show()