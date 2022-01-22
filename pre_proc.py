import os
import xml.etree.ElementTree as ET
import random
from shutil import copyfile
annot = "Dataset/annotation/"
path = "Dataset/rename/"
gtvalues=[[],[],[],[],[]]
with open("annotation.txt", "w+") as f:
    
    for e,i in enumerate(os.listdir(annot)):
        try:
            filename = i.split(".")[0]+".png"
            #print(e,filename)
            tree = ET.parse(annot+i)
            root = tree.getroot()
            for p in root[2]:
                setPx = lambda px: px*3.7795275591
                if(p.attrib['id'].startswith('imag')):
                    x_loss = float(p.attrib['x'])
                    y_loss = float(p.attrib['y'])
                getx = lambda x: (x-x_loss) * 3.7795275591/32
                gety = lambda y: (y-y_loss) * 3.7795275591/24
                if(p.attrib['id'].startswith('rec')):
                    _x=getx(float(p.attrib['x']))
                    _y=gety(float(p.attrib['y']))
                    _w=setPx(float(p.attrib['width']))/32
                    _h=setPx(float(p.attrib['height']))/24
                    x_min = _x
                    y_min = _y
                    x_max = _x + _w
                    y_max = _y + _h
                    file_path = '/home/lordcocoro2004/SC_dataset/jupyternotebooks/Dataset/train'
                    fileName = os.path.join(file_path, filename)
                    if(p.attrib['class'].startswith('gas')):
                        gtvalues[0].append(filename)
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'gas' + '\n')
                    if(p.attrib['class'].startswith('mineral')):
                        gtvalues[1].append(filename)
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'mineral' + '\n')
                    if(p.attrib['class'].startswith('proto')):
                        gtvalues[2].append(filename)
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'protobase' + '\n')
                    if(p.attrib['class'].startswith('zerg')):
                        gtvalues[3].append(filename)
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'zergbase' + '\n')
                    if(p.attrib['class'].startswith('terran')):
                        gtvalues[4].append(filename)
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'terranbase' + '\n')
        except Exception as e:
            print(e)
            print("error in "+filename)
            continue
    print(len(gtvalues[0]),len(gtvalues[1]),len(gtvalues[2]),len(gtvalues[3]),len(gtvalues[4]))
train_path = 'Dataset/train'
test_path = 'Dataset/test'
classes=['gas','mineral','protobase','zergbase','terranbase']
# random.seed(1)

# for i in range(len(classes)):
#     all_imgs = gtvalues[i]
#     all_imgs = [f for f in all_imgs if not f.startswith('.')]
#     random.shuffle(all_imgs)
    
#     limit = int(len(gtvalues[i])*0.8)

#     train_imgs = all_imgs[:limit]
#     test_imgs = all_imgs[limit:]
    
#     # copy each classes' images to train directory
#     for j in range(len(train_imgs)):
#         original_path = os.path.join(path, train_imgs[j])
#         new_path = os.path.join(train_path, train_imgs[j])
#         copyfile(original_path, new_path)
    
#     # copy each classes' images to test directory
#     for j in range(len(test_imgs)):
#         original_path = os.path.join(path, test_imgs[j])
#         new_path = os.path.join(test_path, test_imgs[j])
#         copyfile(original_path, new_path)