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
    for i in range(0, len(data_train)):
        data_train[i] = cv2.imread(data_train[i])
    return data_train, data_label, data_test



# ========= MAIN ==========
print("Retreiving data...")
x_train, y_train, data_test = load_data()
y_train_one_hot = to_categorical(y_train)
x_train = np.divide(x_train,255)

x_test = np.array(x_train[0:int(len(x_train)*0.1)])
y_test = y_train_one_hot[0:int(len(y_train_one_hot)*0.1)]

x_train = np.array(x_train[int(len(x_train)*0.1):])
y_train = y_train_one_hot[int(len(y_train_one_hot)*0.1):]
#print(x_train)
print("OK")



# Architechture
model = Sequential()

# Conv layer
model.add(Conv2D(32, (5,5), activation='relu', input_shape=(32,32,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(32, (5,5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())

model.add(Dense(1000, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(x_train, y_train, batch_size=256, epochs=10, validation_split=0.3) 
model.evaluate(x_test, y_test)[1]
# # print(data_train[len(data_train) - 1])
#img = cv2.imread(x_train[0][0])

#print(img)
# img = plt.imshow(x_train[0])
# plt.show()


