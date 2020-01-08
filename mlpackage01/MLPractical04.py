import numpy
filename = 'indians-diabetes.data.csv'
raw_data = open(filename, 'r')
data = numpy.loadtxt(raw_data, delimiter=",")
print("Numpy loadtxt : ", data.shape)
raw_data.close()
print("\n\n\n")

print(data)
print("\n\n\n")
print("-*-"*30)
print("\n\n\n")
for l in data :
    print(l)