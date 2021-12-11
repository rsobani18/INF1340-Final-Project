import numpy as np
import cv2
import pandas as pd
from tkinter import *


#class
class ColourPicker:
#init function
  def __init__(self):
    window = Tk()
    window.title("Colour Picker")
    window.geometry("600x600") 

    #create a square window
    window.configure(background = 'white')

# OpenCV Ref Doc: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html

#1.	Get colours dataset & test image – has RGB and hex values - DONE
#2.	User enters image to check colours in Tkinter - Rahima
#3.	Show image selected by user in OpenCV within Tkinter - Rahima
#4.	At click by user show colour details - Rahima
#5. Get click value - Shauna
#6.	Determine right colour based on user selection by choosing between the smallest distance - Shamsa

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
#7. At user click of Esc key kill window - Shamsa

if cv2.waitKey(20) & 0xFF ==27:
        break
#8. Add error message if image path is invalid - Shamsa

try:
    a = int(input()) #not sure what to put here? 
except:
    raise Exception('This image path is invalid')

# Get image file path from user
  img_path = ("Enter the filename for the image:")

  # Assign csv file to panda dataframe
  dataset_path = "Colours.csv"
  labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"]
  coloursDF = pd.read_csv(dataset_path, names=labels, header=None)

  # Function to get pixel location from user's click
  def pixel_Location(event, x, y, param):
        print("Click x & y Location:", x,y)
        B,G,R = img[y,x]
        print("BGR colours:", B,G,R) 

  # OpenCV image 
  img = cv2.imread(img_path, -1)
  img = cv2.resize(img, (400,400))
  img.imshow("Colour Detection", img)
  cv2.setMousecallBack("Colour Detection", pixel_Location)
  img.waitKey(0)
  img.destroyAllWindows()
