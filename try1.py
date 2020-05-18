import os
import platform
import win as f
import mac as m
import some as s




def op():
    path=platform.system()
    option=int(input("\n 1. Create new HTML project(select 9 for git initialization) \n 2.Delete a project \n 3.Open a Project \n 4.Archive \n"))
    osd(option,path)
def opFlutter():
    path=platform.system()
    opn=int(input("\n 1. Create new FLUTTER project(select 9 for git initialization) \n 2.Delete a project \n 3.Archive \n"))
    osf(opn,path)

def osd(option,path):
    if(path=="Windows"):
        f.opion(option)
    elif(path=="Darwin"):
        m.trying(option)
    elif(path=="Linux"):
        m.lint(option)
    
def osf(tion,path):
    if(path=="Windows"):
        s.mainOp(tion)
    # elif(path=="Darwin"):
    #     m.trying(option)
    # elif(path=="Linux"):
    #     m.lint(option)
    else:
        print('requested os is yet in development')
        print('pls contribute if you can https://www.github.com/rajeshjaga/Html_helper')
    
def welcome(ch):
    if ch=='f' or ch=='F':
        opFlutter()
    elif ch=='h' or ch=='H':
        op()
    else:
        pass
    
    
    
    
print('Welcome to Projects manager')
print('What do you can I do to day')
choice=input('Flutter(f) or Html(h)')
welcome(choice)


