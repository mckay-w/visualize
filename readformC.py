from ctypes import *

class Tree(Structure):
    pass

Tree._fields_=[("value",c_int),
               ("left",POINTER(Tree)),
               ("right",POINTER(Tree))
               ]


def getTree(dllPath):
    #dll=cdll.LoadLibrary('./readfromC/great_module.dll')
    num=10000
    dll=cdll.LoadLibrary(dllPath)
    stru_info= create_string_buffer(sizeof(Tree) * num)
    p_rec = POINTER(Tree)(stru_info)
    info_num = c_int()
    index=0
    nodes=["X" for i in range(num)]
    #readTree(nodes,p_rec,index)
    for i in range(num):
        #print(p_rec[i#print(p_rec[i].value)
        if p_rec[i].value!=0:
            nodes[i]=p_rec[i].value
    return nodes

def readTree(nodes,p_rec,index):
    nodes[index]=p_rec[index]


if __name__=="__main__":
    nodes=getTree('./visualize/avl_tree.dll')
    print(nodes[3])

