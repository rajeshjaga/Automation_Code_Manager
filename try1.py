import os
import platform
import win as f
import mac as m

def op():
    path=platform.system()
    option=int(input("\n 1. Create new HTML project(select 9 for git initialization) \n 2.Delete a project \n 3.Open a Project \n 4.Archive \n"))
    osd(option,path)

def osd(option,path):
    if(path=="Windows"):
        f.opion(option)
    elif(path=="Darwin"):
        m.trying(option)
    elif(path=="Linux"):
        m.lint(option)
    
op()