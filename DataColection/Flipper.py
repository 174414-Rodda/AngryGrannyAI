#This Code Just Flips The Images Used For Flipping The Left to Make Right For Data Augumentation Purpose
import os
from PIL import Image
path_of_the_directory= './data/left'
st = "right"
count = 226
x = 206
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    print("It is working for "+str(count))
    if(count-x >206):
        break
    f = os.path.join(path_of_the_directory,filename)
    original_img = Image.open(f)
    horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
    horz_img.save("./left/"+st+str(count)+".jpg")
    original_img.close()
    count+=1
    horz_img.close()