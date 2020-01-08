import numpy
#for getting data online
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

dataset = numpy.genfromtxt(web_path, delimiter=",")
#generate numpy dataset from the dataset available on given url path

#print data
for l in dataset:
    print(l)

#shape will only tell how much data we recieved, not how much data present on server
print("Shape of Data from url : ", dataset.shape)