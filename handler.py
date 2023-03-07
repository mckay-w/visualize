import numpy as np #1
import cv2 #2
from ctypes import *
from tkinter import * 
import math



# colors=[(199, 237, 204),(0,0,0),(250, 249, 222),(220, 226, 241),(253, 230, 224)] # 太浅了
colors=[(7,128,207),(118,80,5),(250,109,29),(14,44,130),(182,181,31),(218,31,24),(112,24,102),(244,122,117)]

def canvasInit(width,height):
    canvas = np.full((height, width, 3), 255,dtype="uint8") #3
    #cv2.namedWindow('Canvas', cv2.WINDOW_NORMAL)
    #cv2.namedWindow('Canvas', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Canvas", canvas) #10
    #cv2.waitKey(0) #11
    return canvas


def drawEdge(canvas,start,end,color,lineWidth):
    cv2.line(canvas, tuple(map(int,start)), tuple(map(int,end)), color, lineWidth) #9
    cv2.imshow("Canvas", canvas) 

    #cv2.waitKey(0) # 等待任意按键


def drawTree(canvas,nodes,width,height):
    index=0
    x=0
    y=height
    pow=0
    xinterval=width/math.ceil(math.log(len(nodes),2))
    yinterval=height/2**(pow+1)
    while nodes[index]!="end":
        y=y-yinterval
        if nodes[index]!="X" or nodes[index]!="x":
            #cv2.putText(canvas,nodes[index],tuple(map(int,(x,y))),cv2.FONT_HERSHEY_SIMPLEX,0.5,(26,73,92))
            cv2.putText(canvas,str(nodes[index]),tuple(map(int,(x,y))),cv2.FONT_HERSHEY_SIMPLEX,0.5,colors[(pow+3)%len(colors)])
            #create_text(x,y,nodes[index])
            if pow!=0:
                drawEdge(canvas,(x-xinterval,y+yinterval/2-(index%2)*yinterval),(x,y),(0, 255, 0),1)
                #cv2.imshow("Canvas", canvas) 
                #drawEdge(canvas,(0,10),(200,20),(0, 0, 255),1)
        index=index+1
        if index==2**(pow+1)-1:
            pow=pow+1 # level+1
            x=x+xinterval
            yinterval=height/(2**pow+1)
            y=height


#find element, if found, return the index of it ,else return -1
def find(nodes,node):
    for i in range(len(nodes)):
        if nodes[i]==node:
            return i
    return -1

def drawPath(nodes,leaf,canvas,width,height):
    index=find(nodes,leaf)
    if index==-1:
        print("no such node in the tree")
    else:
        level=math.ceil(math.log(index,2))
        xinterval=width/(level+1)
        yinterval=height/2**level        
        x=width-xinterval*2
        y=height-yinterval*(index-2**(level-1))
        for i in range(level,0,-1):
            cv2.putText(canvas,str(nodes[index]),tuple(map(int,(x-0.1*xinterval,y))),cv2.FONT_HERSHEY_SIMPLEX,1.2,colors[((i+3) % len(colors))])
            nextx=x
            nexty=y
            x=x-xinterval
            y=y+yinterval/2-(index%2)*yinterval
            drawEdge(canvas,(x,y),(nextx,nexty),colors[i % len(colors)],4)
            yinterval=yinterval*2
            index=index//2
        cv2.putText(canvas,str(nodes[index]),tuple(map(int,(x-0.1*xinterval,y))),cv2.FONT_HERSHEY_SIMPLEX,1.2,colors[(i % len(colors))])
            
    return 0

def getTree(nodes):
    node=input().split()
    while node!="end":
        nodes.append(node)