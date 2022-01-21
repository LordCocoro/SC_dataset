import os
import xml.etree.ElementTree as ET

annot = "Dataset/annotation/"
path = "Dataset/rename/"
with open("annotation.txt", "w+") as f:
    for e,i in enumerate(os.listdir(annot)):
        try:
            filename = i.split(".")[0]+".png"
            #print(e,filename)
            tree = ET.parse(annot+i)
            root = tree.getroot()
            gtvalues=[]
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
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'gas' + '\n')
                    if(p.attrib['class'].startswith('mineral')):
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'mineral' + '\n')
                    if(p.attrib['class'].startswith('proto')):
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'protobase' + '\n')
                    if(p.attrib['class'].startswith('zerg')):
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'zergbase' + '\n')
                    if(p.attrib['class'].startswith('terran')):
                        f.write(fileName + ',' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',' + 'terranbase' + '\n')
        except Exception as e:
            print(e)
            print("error in "+filename)
            continue