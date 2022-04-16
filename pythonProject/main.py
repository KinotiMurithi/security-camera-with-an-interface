import tkinter
from tkinter import filedialog
import cv2
import winsound
import sys
import time


top = tkinter.Tk()
top.title('Eye of God')
top.geometry('800x500')
top.tk_setPalette('black')

def start_serveillance():

    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)

            def systemexit():
                system = sys.exit()

            if cv2.waitKey(10) == ord('q'):
                 break
            cv2.imshow('Eye of God', frame1)




def openfile():
    filepath = filedialog.askopenfile()


my_Canvas = tkinter.Canvas (top,height = 300,width = 300, bg= 'blue')
my_Canvas.pack()


button1 = tkinter.Button(top, text = "start all cameras", bg = 'grey',width= 13, command = start_serveillance)
button2 = tkinter.Button(top, text = "data base", bg = 'grey',width= 13, command = openfile)
button3 = tkinter.Button(top, text = "image analysis", bg = 'grey', width= 13)
button4 = tkinter.Button(top, text = "pattern matching", bg = 'grey', width= 13)
button5 = tkinter.Button(top, text = "exit camera", bg = 'grey', width= 13, command = sys.exit)

button1.place(x=370, y=10)
button2.place(x=370, y=40)
button3.place(x=370, y=70)
button4.place(x=370, y=100)
button5.place(x=370, y=130)
top.mainloop()
