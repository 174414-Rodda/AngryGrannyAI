#The idea is to collect the necessary screenshots for traing the model
#Whenever the key is pressed the screenshot is taken 
#Based on the key press it is stored to the particular folder 
#Which are Used later for training
import keyboard#Uses This Module To Detect The Key Press 
import pyautogui#USed To Take Screenshots
from re import sub#For Simple String Proecssing
from PIL import Image#For Saving The Image
#Need To add the file saving feature
#where all the current fiel numbers are stored


#Instructions and Cautions:
#This is a global event code so all the key press are capture
#Irrespective of the game is played or not
#Press q to stop capturing
#Press space to take the no-op screenshot
count = [0,0,0,0,0,0,0]
first = 0
def uparrow(key):
    '''
    input: 
            key: the action code 0 for up,1 for down,2for left, 3 for right, 4 for a
                 5 for d 6 for no-op 
    '''
    im = pyautogui.screenshot()
    str1 = ""
    print("It is saving as of now, "+str(sum(count)) )
    count[key]+=1
    if(key ==0):
        str1 = "up"+str(count[0])+".jpg"
        im.save("./data/up/"+str1)
        return
    
    if(key ==1):
        str1 = "down"+str(count[1])+".jpg"
        im.save("./data/down/"+str1)
        return

    if(key ==2):
        str1 = "left"+str(count[2])+".jpg"
        im.save("./data/left/"+str1)
        return

    if(key ==3):
        str1 = "right"+str(count[3])+".jpg"
        im.save("./data/right/"+str1)
        return

    if(key ==5):
        str1 = "d"+str(count[5])+".jpg"
        im.save("./data/d/"+str1)
        return

    if(key ==4):
        str1 = "a"+str(count[4])+".jpg"
        im.save("./data/a/"+str1)
        return
    
    if(key ==6):
        str1 = "noop"+str(count[6])+".jpg"
        im.save("./data/noop/"+str1)
        return


def close():
    '''
    To prevent overwrting of the collect data the current count of the respective
    operation should me maintained
    When q is pressed then this fuction is invoked
    update the input.txt with the latest count 
    '''
    print("in the close")
    file1 = open("input.txt", "w")
    l=""
    for x in count:
        l+=str(x)+","
    file1.write(l)
    file1.close()
    print("Well Done Boss Mang....",sum(count)-first)

    keyboard.press_and_release('ctrl+c')
print("Started...")
 
file1 = open("./input.txt", "r+")
s = str(file1.read())
s = (sub(' +', ' ',s)).split(",")

for x in range(0,7):
    count[x] = int(s[x])
    count[x]+=1
print(count)
first = sum(count)
print("Starting Stuff U have:",first)
#The recommended way to detect the key press as the infinte loop uses 100% CPU
#Lambda is usesless
keyboard.add_hotkey('up', lambda: uparrow(0))
keyboard.add_hotkey('down', lambda: uparrow(1))
keyboard.add_hotkey('left', lambda: uparrow(2))
keyboard.add_hotkey('right', lambda: uparrow(3))
keyboard.add_hotkey('a', lambda: uparrow(4))
keyboard.add_hotkey('d', lambda: uparrow(5))
keyboard.add_hotkey('space', lambda: uparrow(6))
keyboard.add_hotkey('q', lambda: close())

keyboard.wait()
