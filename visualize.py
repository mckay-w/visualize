import numpy as np #1
import cv2 #2
from ctypes import *
from tkinter import * 
import handler
import mouse




if __name__=="__main__":
    nodes=[]
    # getTree(nodes)
    #nodes=input().split()
    for i in range(2000):
        nodes.append(i)
    nodes.append("end")
    height=1000
    width=1400
    canvas=handler.canvasInit(width,height)
    #handler.drawTree(canvas,nodes,width,height)
    #handler.drawPath(nodes,1723,canvas,width,height)
    handler.drawTree(canvas,nodes,width,height)
    canvas_show=np.copy(canvas[500:600,:])
    cv2.setMouseCallback('Canvas', mouse.mouse)
    cv2.imshow("Canvas", canvas_show) #10
    cv2.waitKey(0) #11
    cv2.destroyAllWindows()