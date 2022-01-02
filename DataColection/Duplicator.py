#This Code Just Deplicates the Imaes Present In The Given File
#A New File Names "resized" Should Be Created and The Created File has "up","down","a","d" as Sub Files in it.
import os
from PIL import Image
st = "up"
path_of_the_directory= './resized/'+st

count = 2

print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    if(count==1200):
        print("It Broke")
        break
    print("It is working for "+str(count))
    f = os.path.join(path_of_the_directory,filename)
    original_img = Image.open(f)
    original_img.save("./resized/"+st+"/new"+st+str(count)+".jpg")
    original_img.close()
    count+=1