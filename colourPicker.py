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

#1.	Get colours dataset – has RGB and hex values - DONE
#2.	User enters image to check colours in Tkinter
#3.	Show image selected by user in OpenCV within Tkinter
#4.	At click by user show colour details
#5. Get click value - DONE
#6.	Determine right colour based on user selection by choosing between the smallest distance


# Get image file path from user
  img_path = ("Enter the filename for the image:")

  # Assign csv file to panda dataframe
  dataset_path = "Colours.csv"
  labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"]
  coloursDF = pd.read_csv(dataset_path, names=labels, header=None)

  # Function to get pixel location from user's click
  def pixel_Location(event, x, y, param):
    if event == cv2.EVENT_LBUTTONDOWN:
      print(x,y) 

  # OpenCV image 
  img = cv2.imread(img_path, -1)
  img = cv2.resize(img, (400,400))
  img.imshow("Colour Detection", img)
  cv2.setMousecallBack("Colour Detection", pixel_Location)
  img.waitKey(0)
  img.destroyAllWindows()
