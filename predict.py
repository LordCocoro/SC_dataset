import os,cv2,keras
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import xml.etree.ElementTree as ET


# ss_mineral = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
# ss_protos = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
# ss_terran = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
# ss_zerg = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
# ss_arr = [ss_gas,ss_mineral,ss_protos,ss_terran,ss_zerg]
# ss_labels = ['gas','mineral','protobase','terranbase','zergbase']
# def get_iou(bb1, bb2):
#     assert bb1['x1'] < bb1['x2']
#     assert bb1['y1'] < bb1['y2']
#     assert bb2['x1'] < bb2['x2']
#     assert bb2['y1'] < bb2['y2']
#     x_left = max(bb1['x1'], bb2['x1'])
#     y_top = max(bb1['y1'], bb2['y1'])
#     x_right = min(bb1['x2'], bb2['x2'])
#     y_bottom = min(bb1['y2'], bb2['y2'])
#     if x_right < x_left or y_bottom < y_top:
#         return 0.0
#     intersection_area = (x_right - x_left) * (y_bottom - y_top)
#     bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
#     bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])
#     iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
#     assert iou >= 0.0
#     assert iou <= 1.0
#     return iou

# train_images=[]
# train_labels=[]
# annot = "SC_dataset/Dataset/annotation/"
# path = "SC_dataset/Dataset/rename/"
# for e,i in enumerate(os.listdir(annot)):
#     #try:
#     if i.startswith("0"):
#         filename = i.split(".")[0]+".png"
#         #print(e,filename)
#         image = cv2.imread(os.path.join(path,filename))
#         tree = ET.parse(annot+i)
#         root = tree.getroot()
        
#         gtvalues=[]
#         for p in root[2]:
#             setPx = lambda px: px*3.7795275591
#             if(p.attrib['id'].startswith('imag')):
#                 x_loss = float(p.attrib['x'])
#                 y_loss = float(p.attrib['y'])
#             getx = lambda x: (x-x_loss) * 3.7795275591/32
#             gety = lambda y: (y-y_loss) * 3.7795275591/24
#             if(p.attrib['id'].startswith('rec')):
#                 _x=getx(float(p.attrib['x']))
#                 _y=gety(float(p.attrib['y']))
#                 _w=setPx(float(p.attrib['width']))/32
#                 _h=setPx(float(p.attrib['height']))/24
#                 x_min = _x
#                 y_min = _y
#                 x_max = _x + _w
#                 y_max = _y + _h
#                 if(p.attrib['class']==ss_labels[g]):
#                     #print(x_min,x_max,y_min,y_max)
#                     gtvalues.append({"x1":x_min,"x2":x_max,"y1":y_min,"y2":y_max})
#         #print(len(gtvalues))
#         if(len(gtvalues)>0):
#             print(e,filename)
#             ss_gas.setBaseImage(image)
#             ss_gas.switchToSelectiveSearchFast()
#             ssresults = ss_gas.process()
#             imout = image.copy()
#             counter = 0
#             falsecounter = 0
#             flag = 0
#             fflag = 0
#             bflag = 0
#             for e,result in enumerate(ssresults):
#                 if e < 2000 and flag == 0:
#                     for gtval in gtvalues:
#                         x,y,w,h = result
#                         iou = get_iou(gtval,{"x1":x,"x2":x+w,"y1":y,"y2":y+h})
#                         if counter < 30:
#                             if iou > 0.70:
#                                 timage = imout[y:y+h,x:x+w]
#                                 resized = cv2.resize(timage, (224,224), interpolation = cv2.INTER_AREA)
#                                 train_images.append(resized)
#                                 train_labels.append(1)
#                                 counter += 1
#                         else :
#                             fflag =1
#                         if falsecounter <30:
#                             if iou < 0.3:
#                                 timage = imout[y:y+h,x:x+w]
#                                 resized = cv2.resize(timage, (224,224), interpolation = cv2.INTER_AREA)
#                                 train_images.append(resized)
#                                 train_labels.append(0)
#                                 falsecounter += 1
#                         else :
#                             bflag = 1
#                     if fflag == 1 and bflag == 1:
#                         print("inside")
#                         flag = 1
            #train_images,train_labels = get_train_values(ss_gas,gtvalues,image) 
                # if(p.attrib['class'].startswith('proto')):
                #     rect = patches.Rectangle((_x,_y),_w,_h, linewidth=1, edgecolor='r', facecolor='none')
                # if(p.attrib['class'].startswith('zerg')):
                #     rect = patches.Rectangle((_x,_y),_w,_h, linewidth=1, edgecolor='r', facecolor='none')
                # if(p.attrib['class'].startswith('terran')):
                #     rect = patches.Rectangle((_x,_y),_w,_h, linewidth=1, edgecolor='r', facecolor='none')
                # if(p.attrib['class'].startswith('gas')):
                #     rect = patches.Rectangle((_x,_y),_w,_h, linewidth=1, edgecolor='g', facecolor='none')
                # if(p.attrib['class'].startswith('min')):
                #     rect = patches.Rectangle((_x,_y),_w,_h, linewidth=1, edgecolor='b', facecolor='none')
            #train_images,train_labels = get_train_values(ss_gas,gtvalues)
                        
    #except Exception as e:
    #    print(e)
    #    print("error in "+filename)
    #   continue
# X_new = np.array(train_images)
# y_new = np.array(train_labels)

from keras.layers import Dense
from keras import Model
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

from keras.applications.vgg16 import VGG16
vggmodel = VGG16(weights='imagenet', include_top=True)

ss_gas = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
for layers in (vggmodel.layers)[:15]:
    print(layers)
    layers.trainable = False
X= vggmodel.layers[-2].output
predictions = Dense(2, activation="softmax")(X)
model_final = Model(vggmodel.input, predictions)
opt = Adam(lr=0.0001)
model_final.compile(loss = keras.losses.categorical_crossentropy, optimizer = opt, metrics=["accuracy"])
model_final.summary()
model_final.load_weights('/home/lordcocoro2004/maestria/SC_dataset/SC_dataset/ieeercnn_vgg16_1gas.h5')

z=0
for e,i in enumerate(os.listdir("Dataset/test")):
    print(i)
    if i.startswith("004"):
        print(i)
        z += 1
        img = cv2.imread(os.path.join("Dataset/test",i))
        ss_gas.setBaseImage(img)
        ss_gas.switchToSelectiveSearchFast()
        ssresults = ss_gas.process()
        imout = img.copy()
        for e,result in enumerate(ssresults):
            if e < 2000:
                x,y,w,h = result
                timage = imout[y:y+h,x:x+w]
                resized = cv2.resize(timage, (224,224), interpolation = cv2.INTER_AREA)
                img = np.expand_dims(resized, axis=0)
                out= model_final.predict(img)
                if out[0][0] > 0.70:
                    cv2.rectangle(imout, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
        plt.figure()
        plt.imshow(imout)
        break