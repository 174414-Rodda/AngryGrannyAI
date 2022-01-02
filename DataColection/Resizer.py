#The Default Resolution Is Scaled Down To 720x720 but this code is redundent as the tensorflow has the built in support
from PIL import Image
import numpy
import datetime
import os
from PIL import Image
a = datetime.datetime.now()
cdir = "noop/"#Should be changed based on the need
path_of_the_directory= './data/'+cdir
count = 0
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    print("It is working:",count)
    count+=1
    temp = filename
    f = os.path.join(path_of_the_directory,filename)
    im = Image.open(f)
    im1 = im.resize((720,720))
    

    im1.save("./resized/"+cdir+filename)
    im1.close()