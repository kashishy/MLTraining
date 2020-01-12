import matplotlib.pyplot as plt

# plot is used for drawing line, it required array of minimum two dimension,
# if only one dimension array passed then passed array is considered as coordinate of y
# it will add values starting from 0 for x coordinate
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.xlabel("-------Indexes------->")
plt.ylabel("-----some numbers---->")
plt.show()