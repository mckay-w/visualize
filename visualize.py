import numpy as np #1
import cv2 #2
from ctypes import *



class Tree(Structure):
    _fields_=_fields_list_

_fields_list_=[("value",c_int),
            ("left",Tree),
            ("right",Tree)]


def canvasInit():
    canvas = np.zeros((300, 300, 3), dtype="uint8") #3
    red = (0, 0, 255) #8
    cv2.line(canvas, (300, 0), (0, 300), red, 1) #9
    cv2.imshow("Canvas", canvas) #10
    cv2.waitKey(0) #11

# 开始初始化结构体
a = SN()
a.data = "233333"
a.datalen = len(a.data)
a.datatype = type(a.data)

def drawEdge(canvas,start,end,color,lineWidth):
    cv2.line(canvas, start, end, color, lineWidth) #9
    cv2.imshow("Canvas", canvas) 
    cv2.waitKey(0) # 等待任意按键

def getTree():
    


if __name__=="__main__":
    getTree()
