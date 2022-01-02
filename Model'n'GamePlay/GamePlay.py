#This code takes the screeshots of the game repetatvely and save them as screen.jpg
#Uses the trained model in .h5 formate predictions are made
from PIL import Image
from numpy import argmax
from tensorflow.keras.preprocessing.image import img_to_array 
from tensorflow.keras.models import load_model
from datetime import datetime
import pyautogui
import time
import random
model = load_model('angrygrannyai.h5')
choice=0
while True:
    #time.sleep(0.2)
    a = datetime.now()  
    im = pyautogui.screenshot()  #Traking the screenshots
    im.save("./screen.jpg")#Saving them with screen.jpg name
    im = Image.open("./screen.jpg")#Opening the image for resizing
    im = im.resize((180,180))#Resizing to 180 180 
    im = img_to_array(im) #Converting into numpy array
    im = im.reshape( -1,180,180,3)#REshaping it
    predictions = model.predict(im)#Getting the prediction
    choice = argmax(predictions)#Pickcing up the largest val
    print(choice)#Printing it based on the vales pressing the appropriate model
    if(choice == 0 ):
        pyautogui.press('a')
    if(choice == 1 ):
        pyautogui.press('d')
    if(choice == 2 ):
        pyautogui.press('down')
    if(choice == 4 ):
        pyautogui.press('up')#
    print(datetime.now() - a)#Time take for each prediction
