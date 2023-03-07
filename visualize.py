import numpy as np #1
import cv2 #2
from ctypes import *
from tkinter import * 
import handler




if __name__=="__main__":
    nodes=[]
    # getTree(nodes)
    #nodes=input().split()
    for i in range(2000):
        nodes.append(i)
    nodes.append("end")
    height=800
    width=1400
    canvas=handler.canvasInit(width,height)
    #handler.drawTree(canvas,nodes,width,height)
    #handler.drawPath(nodes,1723,canvas,width,height)
    handler.drawTree(canvas,nodes,width,height)
    print(canvas.size)
    #print(canvas)
    #canvas.resize(canvas,(2,4))
    res = cv2.resize(canvas, dsize=(height*3, width*3), interpolation=cv2.INTER_LANCZOS4)

    #scaled_canvas=canvas.copy()
    #scaled_canvas.thumbnail(target_size,)
    cv2.imshow("Canvas", res) #10
    cv2.waitKey(0) #11
    cv2.destroyAllWindows()