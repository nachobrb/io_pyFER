# ======== IMPORTS ========
import cv2
from os import listdir
from os.path import isfile, join, isdir
import re


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
                            data_label.append(txt_content)
                    
                    #print(elems_tmp)
                    #print(txt_content)

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



# ========= MAIN ==========
data_train, data_label, data_test = load_data()
print(data_train, data_label, data_test)
