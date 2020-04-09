import os
 
def di():
    cdir=input("Mention the project name to archive")
    def_path="c:/users/hp/documents/github/html"
    arpath=r'C:\Users\hp\Documents\github\archive\htmls'
    try:
        mypath=os.path.join(def_path,cdir)
        print(os.getcwd())      
        os.chdir(arpath)
        print(os.getcwd())
        os.system(f'mv {mypath} {arpath}')
    except OSError as Error:
        print('error')
        
    #os.chdir('c:users/hp/documents/github/archive/htmls/')
    
    
    # os.chdir(arpath)
    # os.mkdir(cdir)  
    # os.system('dir')
    