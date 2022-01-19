import os
import shutil 
from os import listdir
from os.path import isfile, join
p = os.path.join('Dataset/', 'rename')
    
if not os.path.exists(p):
    os.makedirs(p)
onlyfiles = [f for f in listdir('Dataset/images_4') if isfile(join('Dataset/images_4', f))]

onlyfiles = sorted(onlyfiles)
for e in range(len(onlyfiles)):
    print(onlyfiles[e])
    desde = 'Dataset/images_4/'+onlyfiles[e]
    if(e<9):
        hasta = 'Dataset/rename/00'+str(e+1)+'.png'
    else:
        hasta = 'Dataset/rename/0'+str(e+1)+'.png'
    shutil.copyfile(desde,hasta)
# for k in imdata:
#     desde = realdir+'/images/'+imdata[k].name
#     hasta = realdir+'/rename/'+imdata[k].name
#     shutil.copyfile(desde,hasta)