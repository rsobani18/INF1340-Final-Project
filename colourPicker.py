import numpy as np
import cv2
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os.path


###class
##class ColourPicker:
##    
###init function
##  def __init__(self):
##    window = Tk()
##    window.title("Colour Picker")
##    window.geometry("600x600") 
##
##    #create a square window
##    window.configure(background = 'white')

def fileExists():
  #img_path = img_filepath.get()
    img_path = input("Enter the filename for the image:")
    if os.path.isfile(img_path):
        openCVWindow(img_path)
    else:
        messagebox.showerror('File Error', 'This image path is invalid')

def openCVWindow(img_path):
    global img
    print("in opencv")
    img = cv2.imread(img_path, -1)
    img = cv2.resize(img, (400,400))

def pixel_Location(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global clicked, xpostion, yposition, B, G, R
        clicked = True
        xposition = x
        yposition = y
        print("Click x & y Location:", xposition,yposition)
        B,G,R = img[y,x]
        print("BGR colours:", B,G,R)
        B = int(B)
        G = int(G)
        R = int(R)
        print(B)
        print(G)
        print(R)
        print("******")

        getColourName(R,G,B)
        
def getColourName(R,G,B):
    print(B)
    print(G)
    print(R)
    minimum = 10000
    for i in range(len(coloursDF)):
        dist = abs(R - int(coloursDF.loc[i,"Red"])) + abs(G - int(coloursDF.loc[i,"Green"]))+ abs(B - int(coloursDF.loc[i,"Blue"]))
        if dist <= minimum:
            minimum = dist
            colourname = coloursDF.loc[i,"Colour Name"]
    print(colourname)
    return colourname


#***Beginning of test execution. To be updated when GUI is completed***

dataset_path = "Colours.csv"
labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"]
coloursDF = pd.read_csv(dataset_path, names=labels, header=None)


R = 0
G = 0
B = 0
xpostion = 0
yposition = 0
clicked = False


fileExists()

img = img
cv2.imshow("Colour Detection", img)
cv2.setMouseCallback("Colour Detection", pixel_Location)
cv2.waitKey(0)

cv2.destroyAllWindows()

