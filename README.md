# AngryGrannyAI
<h1 align="center"><project-name></h1>

<p align="center"><project-description></p>

## Descrption:
  - A CNN model to play the "Angry Granny Run" desktop version of the game
  - The model is trained using Tensorflow consist of 3 Sets of Conv and Max Pooling followedby Densly Connected Layer and Output Layer
  - Input image is of 180x180 rgb. 
  - The train accuracy is 94%  and test acuracy is of 81%. 
  - Around 5000 records are used for training and 1500 records for validating 
  - To make each prediction approximate time take by the model is 0.3 sec(on GPU version)
  - The model sometimes unable to recognize the hat like objects
  - The focus is on distance rather than coin collection 
  - Codes are commented for reference purposes
  
## Python Modules Used:

- tensorflow(version above 2.2)
- pyautogui
- keyboard
- pillow

## Dependencies


 - pip install tensorflow-gpu=2.6

 - pip install pyautogui

 - pip install keyboard

## Usage
  
  - For Data Collection
    - If one wish to collect your own data, use the Datacollector.py(in DataCollection Folder)
    - Run the Datacollector.py, the script will automatically will take screenshots and store it in the necessary folder
    - There are 7 classes namely "a","d","right","left","up","down","noop" for the sake of simpliciry both "a" class and "right" are merged in final version likewise for "d" and "right"
    - One can use the other scripts like Duplicator.py(Just to Duplicate Images), Flipper.py(For flippin left to right as part of  Data-agumentaion),Resizer.py(Just to resize the image)
    - To get the better understanding of the traing process view the 2nd link in link section
  
    - ```Note that input.txt is necessary for the proper functioning and to quite the data collection press 'q' ```
    - ```A folder of name "data" having "a","d","down","up","right","left","noop" as sub directories should be created manually ```
    - ```no-op should be taken manually.Press "space" for taking noop screenshots. ```

 - For Making CNN Play the Game
    - Just run the Gameplay.py(present in Model'n'GamePlay) model to let the CNN play the game
    - It is supposed to work out of box
    - Because of the failproof mechanism of the pyautogui, when ever the cursor is moved to the corner of the screen the code will auto-terminate
  
 

## Links

- [Angry Granny Game](https://www.microsoft.com/en-us/p/angry-gran-run/9wzdncrfhmvn?activetab=pivot:overviewtab)

- [Tensorflow Example Used](https://www.tensorflow.org/tutorials/load_data/images)
  
- [Inspiration-1 Subway Surfer AI](https://www.youtube.com/watch?v=ZVSmPikcIP4)
  
- [Inspiration-2 Temple Run AI](https://www.youtube.com/watch?v=jr0P_gGrkPk)




##Credit
  - [Marty's Coding Palace](https://www.youtube.com/channel/UCq1NfsnK6fKMFnBOQfNLsCw)
  
  - [Tensorflow Example Used](https://www.tensorflow.org/tutorials/load_data/images)

  
  
## 🤝 Support

Contributions, issues, and feature requests are welcome!

