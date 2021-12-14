import numpy as np
import cv2
import pandas as pd
from tkinter import *
from tkinter import messagebox
import os.path


dataset_path = "Colours.csv"
labels = ["Colours","Colour Name","HEX Decimal","Red","Green","Blue"]
coloursDF = pd.read_csv(dataset_path, names=labels, header=None)


def fileExists():
    img_file = img_path.get()
    if os.path.isfile((img_file)):
        window.after(3000,lambda:window.destroy())
        openCVWindow(img_file)
    else:
        messagebox.showerror('File Error', 'This image path is invalid')

window = Tk()
window.title("Choose image file")
window.geometry("440x250")
img_path = StringVar()
Entry(window, textvariable = img_path, width = 30).pack()
Label(window, text = "Enter the filename for the image:").pack()
Button(window, text = "Open",command = fileExists, width = 10).pack()

text = Text(window)
text.pack(ipadx=10, ipady=10,padx=10,pady=10)
text.configure(font=("Arial", 10, "bold"))
text.insert(END,
            "\t\t  Colour Detection Program\n\n")
text.insert(END,
            "Enter the image file path in the textbox above and select OPEN.\n")
text.insert(END,
            "A new window will open and at each click a label with the name and RGB values will appear.\n\n")
text.insert(END,
            "\t          CLICK THE GREY WINDOW TO BEGIN!")



def openCVWindow(img_file):
    global img
    img = cv2.imread(img_file, -1)
    img = cv2.resize(img, (400,400))
    cv2.namedWindow("Colour Detection")
    cv2.setMouseCallback("Colour Detection", pixel_Location)
    

def pixel_Location(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global clicked, xpostion, yposition, B, G, R
        clicked = True
        xposition = x
        yposition = y
        B,G,R = img[y,x]
        B = int(B)
        G = int(G)
        R = int(R)

        getColourName(R,G,B)
        while(1) :
            cv2.imshow("Colour Detection", img)
            if(clicked):
                cv2.rectangle(img, (10, 10), (375, 50), (B, G, R), -1)
                text = getColourName(R, G, B) + " Red= " + str(R) + " Green= " + str(G) + " Blue= " + str(B)
                cv2.putText(img, text, (15, 25), 2, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
                if (R + G + B >= 600):
                    cv2.putText(img, text, (15, 25), 2, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
                clicked = False
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()


        
def getColourName(R,G,B):
    minimum = 10000
    for i in range(len(coloursDF)):
        dist = abs(R - int(coloursDF.loc[i,"Red"])) + abs(G - int(coloursDF.loc[i,"Green"]))+ abs(B - int(coloursDF.loc[i,"Blue"]))
        if dist <= minimum:
            minimum = dist
            colourname = coloursDF.loc[i,"Colour Name"]
    return colourname


window.mainloop()

R = 0
G = 0
B = 0
xpostion = 0
yposition = 0
clicked = False
