## Import packages and files to create colourPicker.py ##
import numpy as np
import cv2
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os.path


dataset_path = "Colours.csv" ## set the path for the dataset as the colours csv file ##
labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"] ## creates a list of labels to use with the dataset ##
coloursDF = pd.read_csv(dataset_path, names=labels, header=None) ## uses pandas to read the colours csv stored in the dataset_path variable, using the labels list created ##

## define a function that checks whether the file exists or not ##
def fileExists():
    img_file = img_path.get() ## get the input entered by the user in the Entry text box from the window ##
    if os.path.isfile((img_file)): ##checks if the file name entered by the user is a valid file ##
        window.after(3000,lambda:window.destroy()) ## closes the file input window #
        openCVWindow(img_file) ## if the file can be opened, runs the openCVWindow function ##  
    else:
        messagebox.showerror('File Error', 'This image path is invalid') ## if the file isn't valid a message box with an error pops up ##

window = Tk() ##create a window that asks user to input file name ##
window.title("Choose image file") ## name the window ##
window.geometry("440x250") ## set window dimensions ##
img_path = StringVar() ## create a variable that stores values entered by user in the Entry field ##
Entry(window, textvariable = img_path, width = 30).pack() ## creates an entry field and places it in the window ##
Label(window, text = "Enter the filename for the image:").pack() ## creates a label intructing user for file name and places in it in the window ##
Button(window, text = "Open",command = fileExists, width = 10).pack() ## creates a button to open the file entered by user, using the fileExists function ##

text = Text(window) ## create a textbox within the window ##
text.pack(ipadx=10, ipady=10,padx=10,pady=10) ## places the textbox in the window ##
text.configure(font=("Arial", 10, "bold")) ## formats the font in the text box ##
## inserts text to display in the textbox ##
text.insert(END,
            "\t\t  Colour Detection Program\n\n")
text.insert(END,
            "Enter the image file path in the textbox above and select OPEN.\n")
text.insert(END,
            "A new window will open and at each click a label with the name and RGB values will appear.\n\n")
text.insert(END,
            "\t          CLICK THE GREY WINDOW TO BEGIN!")


## define a function that reads and open the file in a new window ##
def openCVWindow(img_file):
    global img
    img = cv2.imread(img_file, -1) ##reads the image file ##
    img = cv2.resize(img, (400,400))  ## resizes the image window ##
    cv2.namedWindow("Colour Detection") ## naming the window in which the image opens ##
    cv2.setMouseCallback("Colour Detection", pixel_Location) ## runs specified function in response to the mouse click ##
    
## define a function which can identify the users click location using (x, y) coordinate system ##
def pixel_Location(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: ## when user left clicks ##
        global clicked, xpostion, yposition, B, G, R ## creating all required global variables together ##
        clicked = True ##clicked becomes true in event of mouse left click ##
        xposition = x  ## x from the attributes in the function ##
        yposition = y  ## y from the attributes in the function ##
        B,G,R = img[y,x] ## define the variables R,G, B according to the (x, y) position of the click on the image ##
        B = int(B) ## convert value to int ##
        G = int(G) ## convert value to int ##
        R = int(R) ## convert value to int ##

        getColourName(R,G,B) ## runs the function to get the name of the colour within the pizel location function ##
        ## running a while loop that displays the updated name and RGB values for users click position on a coloured rectangle label
        while(1) :
            cv2.imshow("Colour Detection", img)
            if(clicked): ## if user clicks == True ##
                cv2.rectangle(img, (10, 10), (375, 50), (B, G, R), -1)  ##creates a rectangle on the image and fills it with the colour the user clicked on ##
                text = getColourName(R, G, B) + " Red= " + str(R) + " Green= " + str(G) + " Blue= " + str(B) ## variable that stores the name of the colour and each R, G, B as text on the rectangle ##
                cv2.putText(img, text, (15, 25), 2, 0.4, (255, 255, 255), 1, cv2.LINE_AA)  ##displays the text on the image in white ##
                if (R + G + B >= 600): ## for colours that are too light and white text wouldn't show on the label ##
                    cv2.putText(img, text, (15, 25), 2, 0.4, (0, 0, 0), 1, cv2.LINE_AA) ## display the text in black to allow readability ##
                clicked = False ## reset the value of clicked to end the loop ##
            if cv2.waitKey(20) & 0xFF == 27: ## if the user clicks the ESC key the program stops running and ends ##
                break
        cv2.destroyAllWindows() ## closes the window once the loop ends 


## creates a function that retrieves the name of the colour from the database ## 
def getColourName(R,G,B): 
    minimum = 10000
    for i in range(len(coloursDF)): ## loop through the colours database ##
        dist = abs(R - int(coloursDF.loc[i,"Red"])) + abs(G - int(coloursDF.loc[i,"Green"]))+ abs(B - int(coloursDF.loc[i,"Blue"])) ## finds how close the clicked position is to a colour in the database ##
        if dist <= minimum: 
            minimum = dist ## returns the one with the minimum distance ##
            colourname = coloursDF.loc[i,"Colour Name"]
    return colourname ## returns the name of the closest colour ##


window.mainloop() ##keep window running ##

## sets default values for the global variables ##
R = 0
G = 0
B = 0
xpostion = 0
yposition = 0
clicked = False
