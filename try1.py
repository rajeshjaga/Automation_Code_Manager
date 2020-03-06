import os
import platform
import win as f
import mac as m

def op():
    path=platform.system()
    option=int(input("\n 1. Create new HTML project \n 2.Flutter \n 3.Python \n 4.Exit \n"))
    osd(option,path)

def osd(option,path):
    if(path=="Windows"):
        f.opion(option)
    elif(path=="Darwin"):
        m.trying(option)
    elif(path=="Linux"):
        m.lint(option)
    
op()