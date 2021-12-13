##import packages and files to create colourPicker.py##
import numpy as np
import cv2
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os.path


###class
##class ColourPicker:

#create init function?
#add comments
#change variable names
#Do we need a window that asks for file input?
#If so we should try to fix the fileInput code and use that:
##current issue in fileInput is not being able to use the img_path in fileExist 
#only way to exit the loop right now is to press the ESC button, include in the READ.me

#def fileInput():
    #window = Tk()
    #window.title("Choose image file")
    #window.geometry("400x400")
    #img_path = StringVar()
    #Entry(window, textvariable = img_path).pack()
    #Label(window, text = "Enter the filename for the image:").pack()
    #Button(window, text = "Open", command = fileExists).pack()

##define a function that checks whether the file exists or not##
def fileExists():
  #img_path = img_filepath.get()
    img_path = input("Enter the filename for the image: ")
    if os.path.isfile((img_path)): ##checks if the file name entered by the user is a valid file##
        openCVWindow(img_path) ##runs the openCVWindow function if file can be opened##
    else:
        messagebox.showerror('File Error', 'This image path is invalid') ##if the file isn't valid, a message box with an error pops up##

##define a function that reads and opens the file in a window##
def openCVWindow(img_path):
    global img ##creates a global var for the image##
    print("in opencv")
    img = cv2.imread(img_path, -1) ##uses open cv to read the file input by user ##
    img = cv2.resize(img, (400,400)) ##uses open cv to resize the image to window size ##

    
## define a function which can identify the users click location using (x, y) coordinate system ##
def pixel_Location(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: ## when user left clicks ##
        global clicked, xpostion, yposition, B, G, R ## creating all required global variables together ##
        clicked = True ## clicked becomes true in event of left button down ##
        xposition = x  ## x from the attributes in the function ##
        yposition = y  ## y from the attributes in the function ##
        print("Click x & y Location:", xposition,yposition) 
        B,G,R = img[y,x] ## define variables R,G,B according to the (x, y) position of the click on the image ##
        print("BGR colours:", B,G,R)
        B = int(B) ## convert value to int ##
        G = int(G) ## convert value to int ##
        R = int(R) ## convert value to int ##
        print(B)
        print(G)
        print(R)
        print("******")

        getColourName(R,G,B) ## runs the function to get the name of the colour within the pixel location function ##
        
def getColourName(R,G,B): ## creates a function that retrieves the name of the colour from the database ##
    print(B)
    print(G)
    print(R)
    minimum = 10000
    for i in range(len(coloursDF)): ##loop through entire length of the colours database ##
        dist = abs(R - int(coloursDF.loc[i,"Red"])) + abs(G - int(coloursDF.loc[i,"Green"]))+ abs(B - int(coloursDF.loc[i,"Blue"])) #finds how close clicked position is to a colour
        if dist <= minimum:
            minimum = dist  ## and returns the one wuth the minimum distance ##
            colourname = coloursDF.loc[i,"Colour Name"] 
    print(colourname)
    return colourname


#***Beginning of test execution. To be updated when GUI is completed***

dataset_path = "Colours.csv" ##set the path for the dataset as the colours csv file ##
labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"] ##creates a list of labels for use in executing the code ##
coloursDF = pd.read_csv(dataset_path, names=labels, header=None) ## uses pandas to read the colours csv stored in the dataset_path variable, using labels list created ##

## sets default values for variables ##
R = 0 
G = 0
B = 0
xpostion = 0
yposition = 0
clicked = False

#fileInput()
## Run the function that begins execution of code ##
fileExists()

img = img
cv2.namedWindow("Colour Detection") ## naming the window in which the image opens ##
#cv2.imshow("Colour Detection", img)
cv2.setMouseCallback("Colour Detection", pixel_Location) ## runs specified function in response to mouse click ##



##running a while loop that displays updated name and RGB values for users click position on a coloured rectangle label ##
while(1) : 
    cv2.imshow("Colour Detection", img)
    if(clicked): ## if user clicks ##
        cv2.rectangle(img, (10, 10), (375, 50), (B, G, R), -1) ## create a rectangle on the image and fill it with the colour the user clicked on ##
        text = getColourName(R, G, B) + " Red= " + str(R) + " Green= " + str(G) + " Blue= " + str(B) ## variable that stores the name of the colour and each RGB as text on the rectangle ##
        cv2.putText(img, text, (15, 25), 2, 0.4, (255, 255, 255), 1, cv2.LINE_AA) ## displays the text on the image in white ##
        if (R + G + B >= 600):  ## for colours that are too light##
            cv2.putText(img, text, (15, 25), 2, 0.4, (0, 0, 0), 1, cv2.LINE_AA) ## display the text on the image in black to allow readability ##
        clicked = False ## reset clicked to end loop ##
    if cv2.waitKey(20) & 0xFF == 27: ## if the user clicks the ESC key the program stops running and ends ##
        break
cv2.destroyAllWindows() ## closes the window once while loop ends ##

