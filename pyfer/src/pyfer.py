# ======== IMPORTS ========
import cv2
from os import listdir
from os.path import isfile, join, isdir
import re
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.models import Sequential
import numpy as np
import tensorflow as tf
from scipy import misc

# ====== GLOBAL VARS ======

# ======= FUNCTIONS =======
def get_elements(path, type):
    ret = []
    if (type == "file"):
        ret = [f for f in listdir(path) if isfile(join(path, f))]
    if (type == "dir"):
        ret = [f for f in listdir(path) if isdir(join(path, f))]
    return ret

def load_data():
    data_train = []
    data_label = []
    data_test = []


    path_dataset_img = "../../dataset/used/cohn-kanade-images/"
    path_dataset_label = "../../dataset/used/Emotion/"
    path_dataset_test = "../../dataset/used/cohn-kanade-test/"

    dirs_dataset_img = get_elements(path_dataset_img,"dir")
    dirs_dataset_label = get_elements(path_dataset_img,"path_dataset_label")
    dirs_dataset_test = get_elements(path_dataset_img,"path_dataset_label")

    
    for directory in dirs_dataset_img:
        path_tmp_dir = path_dataset_img + directory
        path_tmp_dirs = get_elements(path_tmp_dir,"dir")
        for path in path_tmp_dirs:
            dirs_tmp = get_elements(path_dataset_label + directory,"dir")
            if path in dirs_tmp:
                elems_tmp_path = get_elements(path_dataset_label + directory + "/" + path,"file")
                if len(elems_tmp_path) > 0:
                    # agregar estos a data_train            
                    elems_tmp = get_elements(path_dataset_img + directory + "/" + path,"file")

                    # obtener el valor del txt
                    txt = open(path_dataset_label + directory + "/" + path + "/" + elems_tmp_path[0], "r")
                    txt_content = txt.read();
                    txt_content = re.search('[0-9]+', txt_content).group()
                    txt.close()

                    for element in elems_tmp:
                        if element.endswith(".png"):
                            data_train.append(path_dataset_img + directory + "/" + path + "/" + element)
                            data_label.append(int(txt_content))

                else:
                    elems_tmp = get_elements(path_dataset_img + directory + "/" + path,"file")
                    for element in elems_tmp:
                        if element.endswith(".png"):
                            data_test.append(path_dataset_img + directory + "/" + path + "/" + element)

    # optional
    for directory in dirs_dataset_test:
        dirs_tmp = get_elements(path_dataset_test + "/" + directory,"dir")
        for dirs_sub_tmp in dirs_tmp:
            elems_tmp = get_elements(path_dataset_test + "/" + directory + "/" + dirs_sub_tmp,"dir")
            for element in elems_tmp:
                if element.endswith(".png"):
                    data_test.append(path_dataset_test + "/" + directory + "/" + dirs_sub_tmp + "/" + element)
    return data_train, data_label, data_test



# =========
# MAIN ==========
print("Retrieving data...")
x_file_name, y_labels, data_test = load_data()

from skimage.transform import resize
x=np.empty((0,600,600,3))
y=to_categorical(y_labels)

# for i in range(0,len(x_file_name):
for i in range(0,30):
    img = plt.imread(x_file_name[i])
    img = resize(img,(1,600,600,3))
    x=np.append(x, img,axis=0)



img = plt.imread(x_file_name[60])
# img = resize(img,(1,600,600,3))
# print(type(img))
# test=np.empty((0,300,300,3))
# test=np.append(test, img,axis=0)
# test=np.append(test, img,axis=0)
# print(test.shape)
# print(type(test))
# print(test)
# y=[0,1]
# y = to_categorical(y)
# print(y)
img_r = plt.imshow(img)
plt.show()
# y_train_one_hot = to_categorical(y_train)
# print(np.array(x_train))
# print(x_train.shape)
#x_train = np.divide(x_train,255)

# x_test = np.array(x_train[0:int(len(x_train)*0.1)])
# y_test = y_train_one_hot[0:int(len(y_train_one_hot)*0.1)]

# x_train = np.array(x_train[int(len(x_train)*0.1):])
# y_train = y_train_one_hot[int(len(y_train_one_hot)*0.1):]
#print(x_train)
print("OK")



# Architechture
model = Sequential()

# Conv layer
model.add(Conv2D(32, (5,5), activation='relu', input_shape=(600,600,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (5,5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())

model.add(Dense(1000, activation='relu'))
model.add(Dense(8, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(x[0:30], y[0:30], batch_size=256, epochs=10, validation_split=0.3) 
probs = model.predict(resize(img,(1,600,600,3)))
print(probs)
# model.evaluate(test, y)[1]
# # print(data_train[len(data_train) - 1])
#img = cv2.imread(x_train[0][0])

#print(img)
# img = plt.imshow(x_train[0])
# plt.show()


