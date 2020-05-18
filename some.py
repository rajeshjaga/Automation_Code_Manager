# #this for flutter
import os
import asyncio as asyn
import text as tan
import main as m



mainPath='''C:/Users/hp/Documents/github/Flutter'''
class flutter:
    def  __init__(self, path, name):
        self.path = path
        self.name = name
    def creating_projects(self):
        os.chdir(self.path)
        print(os.getcwd())
        try:
            global projectsPath
            projectsPath=os.path.join(self.path,self.name)
            os.chdir(projectsPath)
            print(os.getcwd())
            print('This directory exits do you want to open')
            if(tan.main3()==True):
                openProjects(self,projectsPath,self.name)
                print('Opening in vs code')
        except OSError as error:
            print(error)
            print('Do you want to create the folder and create the project')
            if(tan.main3()==True):
                asyn.run(callingForActualcommand(self,projectsPath,self.name))
            elif(tan.main3()==False):
                asyn.run(callingForActcommand(self,projectsPath,self.name))
            else:
                pass
                
                
    
def openProjects(self,path,nameFolder):
    self.path=path
    self.nameFolder=nameFolder
    self.projectsPath=os.path.join(projectsPath,nameFolder)
    os.chdir(projectsPath)
    os.system('code .')
    exit()
    





async def callingForActcommand(self,path,nameFolder):
    self.path=path
    self.nameFolder=nameFolder
    print(f'creating the project {projectsPath}')
    print(objectOne.path)
    os.system(f'flutter create {nameFolder}')
    await asyn.sleep(3)
    try:
        self.projectsPath=projectsPath
        os.chdir(projectsPath)
        print("opening in vs code")
        os.system('code .')
    except OSError as error:
        print(error)
        pass
        
async def callingForActualcommand(self,path,nameFolder):
    self.path=path
    self.nameFolder=nameFolder
    print(f'creating the project {projectsPath}')
    print(objectOne.path)
    os.mkdir(path)
    os.system(f'flutter create {nameFolder}')
    await asyn.sleep(3)
    try:
        self.projectsPath=os.path.join(projectsPath,nameFolder)
        os.chdir(projectsPath)
        print("opening in vs code")
        os.system('code .')
    except OSError as error:
        print(error)
        pass
        
        
        
        

def git(folderName):
    def_path = "c:/users/hp/documents/github/Flutter"
    myPath = os.path.join(def_path, folderName,folderName)
    os.chdir(myPath)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "initial commit"')
    print("git init done")


def mainOp(option):

    projectName=input('Enter the name of flutter project you  want to create\n')
    global objectOne
    objectOne=flutter(mainPath,projectName)
        
    if option == 1 or option == 9:
        objectOne.creating_projects()
        if option==9:
            git(projectName)
    elif option ==4:
        #this is archive
        m.archiveFlutter()
    elif option==2:
        cdir = input("Mention the project name (to say i dont recommend this option)")
        def_path = '''c:/users/hp/documents/github/flutter'''
        try:
            mypath = def_path
            os.chdir(mypath)
            print(os.getcwd())
            os.system(f"rd {cdir} /s")
        except OSError as Error:
            print(Error)
            print(f"the project mention {cdir} doesn't exist")
            pass
            
                


