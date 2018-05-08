import numpy as np
import random
import cv2
import keras
import matplotlib.pyplot as plt
from keras.utils import to_categorical
import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist

np.random.seed(0)
random.seed(0)
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
dir='/Users/ashishrawat/Desktop/flower17_2/'
fixed_size = (100,100)
file = '/Users/ashishrawat/Desktop/flower17_2/bluebell/image_1.jpg'
images_per_class = 80
input_layer_size = fixed_size[0]*fixed_size[1]
# print(input_layer_size)
train_labels = os.listdir(dir)
train_labels.sort()
# print(train_labels)
# exit(0)
train_labels = train_labels[1:]
# image = cv2.imread(file)
# image = cv2.resize(image, fixed_size)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(image)
# plt.show()
#
# print(image.shape)
# xx = image.reshape((1,-1))
#
# print(xx.shape)
# print(xx)

image_data = []
labels = []
g_cnt = 0
for idx,folder in enumerate(train_labels):
    local_dir = os.path.join(dir, folder)
    print("hello",folder,local_dir, end=" ")
    for x in range(1, images_per_class+1):
        img = local_dir + "/image_" + str(x) + ".jpg"
        # print("LL",img)
        sample = cv2.imread(img)
        sample = cv2.resize(sample, fixed_size)
        # plt.imshow(sample)
        # plt.show()
        '''
        b, g, r = cv2.split(sample)
        # print(b.shape,g.shape,r.shape)
        b = b.reshape((1,-1))
        g = g.reshape((1,-1))
        r = r.reshape((1,-1))
        # print(b.shape, g.shape, r.shape)
        
        mm = np.hstack((b,g,r))
        mm = mm[0]
        # print("a",mm.shape)
        sample = mm
        '''
        # train_x_orig.reshape(train_x_orig.shape[0], -1).T
        # print(sample.shape)
        # sample = sample.reshape(1,-1)
        # print(sample.shape)
        sample = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
        sample = sample.reshape((1,-1 ))[0]
        # sample = sample[0]
        # print(sample.shape)

        # print(sample.shape)
        # sample = sample.astype('float32')
        # print(sample.shape)
        # sample = sample.flatten('C')
        # print(sample.shape)
        # exit(0)
        image_data.append(sample)
        # print(image_data[g_cnt].shape)
        # exit(0)
        labels.append((idx))
        # print(labels[g_cnt],end='')
        g_cnt +=1
        # break
    # break
    # g_cnt+=1
    # if g_cnt==2:
    #     break;

# exit(0)
# print(image_data)
# print(labels)







image_data = np.asarray(image_data)
# print(image_data[1].shape)
# exit(0)
labels = np.asarray(labels)

image_data = image_data.astype('float32')
labels = labels.astype('float32')
image_data /= 255
# labels_one_hot = to_categorical(labels)
# labels_one_hot = labels_one_hot[:, 1:]
# all_labels = len(set(labels))
# print(len(all_labels))
num_of_classes = len(set(labels))
print()
print(num_of_classes)
# exit(0)

# print(labels_one_hot[70:90])


# exit(0)

shuffleidx = np.random.permutation(image_data.shape[0])
shuffled_data = image_data[shuffleidx]
shuffled_labels = labels[shuffleidx]
shuffled_labels = to_categorical(shuffled_labels)
# print(shuffled_labels.shape)
# exit(0)
'''
shuffled_data = image_data
shuffled_labels = labels_one_hot
'''
train_data = shuffled_data[:1355]
train_labels = shuffled_labels[:1355]
test_data = shuffled_data[1355:]
test_labels = shuffled_labels[1355:]
#
# train_data = shuffled_data[:130]
# train_labels = shuffled_labels[:130]
# test_data = shuffled_data[130:]
# test_labels = shuffled_labels[130:]
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
# print(train_labels.shape)
# print(test_labels.shape)
# exit(0)


print(train_data.shape, train_labels.shape, test_data.shape, test_labels.shape)
# exit(0)


# mnist data
'''
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
classes = np.unique(train_labels)
nClasses = len(classes)
dimData = np.prod(train_images.shape[1:])
print(dimData)

train_data = train_images.reshape(train_images.shape[0], dimData)
test_data = test_images.reshape(test_images.shape[0], dimData)
train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
train_data /= 255
test_data /= 255
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)



model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(512, activation='relu'))
model.add(Dense(nClasses, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=20, verbose=1,
                   validation_data=(test_data, test_labels_one_hot))
# mnist data end here
'''
# exit(0)

# model = Sequential()
# model.add(Dense(512, activation='relu', input_shape=(input_layer_size,)))
# model.add(Dense(512, activation='relu'))
# model.add(Dense(num_of_classes, activation='softmax'))


model = Sequential()
model.add(Dense(50, activation='relu', input_shape=(input_layer_size,)))
model.add(Dense(50, activation='relu'))
model.add(Dense(num_of_classes, activation='softmax'))
# print("num_classes",num_of_classes)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels, batch_size=50, epochs=10, verbose=1,
                   validation_data=(test_data, test_labels))

#
# print("-----")
# print(model.predict_classes(train_data[[1],:]))
# print("ActualClass: ", train_labels[1])
#
# print(model.predict_classes(train_data[[88],:]))
# print("ActualClass: ", train_labels[99])