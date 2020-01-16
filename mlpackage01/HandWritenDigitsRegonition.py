# Standard scientific Python import
import matplotlib.pyplot as plt
# import dataset, classifier and performance matrix
from sklearn import datasets, svm
import warnings

from sklearn.externals._pilutil import imresize, bytescale, imread

warnings.filterwarnings(action='ignore')

# The digits dataset, images are of 8*8 dimensions in this data set present in sklearn datasets
digits = datasets.load_digits()

print("digits : ", digits.keys())

print("digits.target---- : ", digits.target)

images_and_labels = list(zip(digits.images, digits.target))

print("len(images_and_labels) ", len(images_and_labels))

# for binding 1st five rows with index
for index, [image, label] in enumerate(images_and_labels[:5]):
    print("index : ", index, "image : \n", image, " label : ", label)
    plt.subplot(2, 5, index+1)
    plt.axis('on')
    # interpolation not required in new versions
    # for images, cmap for gray scale conversion, interpolation for smooth boundary
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training : %i ' % label)

# plt.show()

# images and targets from data set headings
n_samples = len(digits.images)
print("n_samples : ", n_samples)

# for changing dimension of images for using in model, -1 for reducing one dimension
imageData = digits.images.reshape((n_samples, -1))

# number of columns in a row, after reshaped
print("After Reshaped : len(imageData[0] ) ", len(imageData[0]))

# gamma is learning rate, and loading code of svm
classifier = svm.SVC(gamma=0.001)

# 50% data used for training
classifier.fit(imageData[: n_samples//2], digits.target[: n_samples//2])

# original target of images after 50% data
originalY = digits.target[n_samples//2:]

# testing model with last 50% data
predictedY = classifier.predict(imageData[n_samples//2:])

# combining images and their predicted target
images_and_predictions = list(zip(digits.images[n_samples//2:], predictedY))

# plotting 1st five images and their predicted target
for index, [image, prediction] in enumerate(images_and_predictions[:5]):
    plt.subplot(2, 5, index+6) # dividing plotting space into 2 rows and 5 column, and plotting graph in 2nd row
    plt.axis('on') # ticks
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction : %i' % prediction)

# original target values of images plotted in graph
print("Original Values: ", digits.target[n_samples//2: (n_samples//2)+5])
# plt.show()

# from scipy.misc import imread, imresize, bytescale
# from matplotlib.pyplot import imread

img = imread("FourC.jpeg")
# resizing images to required dimension
img = imresize(img, (8, 8))

classifier = svm.SVC(gamma=0.001)
classifier.fit(imageData[:], digits.target[:])

# making type of images same as earlier(data set of sklearn)
img = img.astype(digits.images.dtype)
img = bytescale(img, high=16.0, low=0)

print("img.shape : ", img.shape)
print("\n", img)

x_testData = []

for row in img:
    for col in row:
        x_testData.append(sum(col)/3.0)
        # for converting RGB to gray and to required format to process image

print("x_testData : \n", x_testData)

print("len(x_testData): ", len(x_testData))

x_testData = [x_testData]
print("len(x_testData) : ", len(x_testData))

result = classifier.predict(x_testData)
print("Machine Output = ", result)

plt.show()