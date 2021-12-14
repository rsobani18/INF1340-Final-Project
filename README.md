# INF1340-Final-Project
## Description
Our group chose a color detection app as our project. Color detection is the process of finding and naming any color selected by a user. This is a simple task for us humans as our brain and eyes work together to convert light into color. However, for computers, this task is much more difficult. Our program allows users to get the name and the RGB value of a colour by clicking on it, in a picture. The project uses a data set that contains a wide range of RGB values with the name of the colours and its respective values. The program uses tkinter to implement the GUI and pandas and numpy to retrieve colour values and execute the code. The input is defined by the users' mouse click on the picture, and the output is a data label filled with the chosen colour, the name of the colour and its RGB values, on the top left corner of the screen. The distance is also computed between each color to accurately choose the one with the smallest distance. 

## Colour Picker Demo
### 1. Run the python file and input the file name in the window
<img src= "https://github.com/rsobani18/INF1340-Final-Project/blob/8fa0a29e4cabc87aaac175f0f10556973c5d922a/Demo1.PNG" width= "440" height="250">

### 2. Click 'Open' to open the file in the OpenCV window
<img src= "https://github.com/rsobani18/INF1340-Final-Project/blob/adb7db192e16a5e97fd7123878628b17b6b6c903/Demo2.PNG" width= "400" height="400">

### 3. Click on any part of the picture to get the colour name and RGB values displayed on a label at the top left
<img src= "https://github.com/rsobani18/INF1340-Final-Project/blob/adb7db192e16a5e97fd7123878628b17b6b6c903/Demo3.png" width = "400" height= "400">

### 4. Press the ESC button on your keyboard to exit the program

## Installation 

### 1. <img width="479" alt="Screen Shot 2021-12-13 at 9 20 57 PM" src="https://user-images.githubusercontent.com/95595459/145921454-653f5257-ed36-478b-9648-6950a032f536.png">
The library installs numpy as a python package. 

### 2. <img width="228" alt="Screen Shot 2021-12-13 at 9 21 04 PM" src="https://user-images.githubusercontent.com/95595459/145921473-983d9872-95b5-4a56-b9f2-a797d3b99ca7.png">
The library installs OpenCV as a python package 

### 3. <img width="198" alt="Screen Shot 2021-12-13 at 9 21 19 PM" src="https://user-images.githubusercontent.com/95595459/145921486-c7f115de-f9b3-44fc-858b-43c4488ef4c8.png">
The library installs pandas into python script. 

### 4. <img width="211" alt="Screen Shot 2021-12-13 at 9 21 23 PM" src="https://user-images.githubusercontent.com/95595459/145921491-d34bd697-78bb-4e63-83fc-0406659879bd.png">
The library imports every exposed object in Tkinter into current namespace 

### 5. <img width="273" alt="Screen Shot 2021-12-13 at 9 21 27 PM" src="https://user-images.githubusercontent.com/95595459/145921498-57914391-5033-4583-b3a9-fcde0375f86d.png">
The library imports messagebox module to display message boxes in the python application. 

### 6. <img width="168" alt="Screen Shot 2021-12-13 at 9 21 32 PM" src="https://user-images.githubusercontent.com/95595459/145921511-46989ef3-e600-444a-b832-be9bba164cbf.png">
The library imports os.path as a path module suitable for the operating system 

## References
- https://data-flair.training/blogs/project-in-python-colour-detection/#google_vignette
- https://github.com/naitik2314/Color-Detection-Python-GUI
- https://github.com/shreyashc01/Object-detection-and-color-identification/blob/main/open-cv%20intern.py
- https://www.delftstack.com/howto/python-tkinter/how-to-set-font-of-tkinter-text-widget/#:~:text=Set%20Font%20for%20Tkinter%20Text%20Widget%20import%20tkinter,be%20Courier%2C%20italic%20with%20the%20size%20of%2016.
- https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html


