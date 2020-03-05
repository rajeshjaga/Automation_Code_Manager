import os

def trying(cur_path):
    def_path="c:/users/hp/documents/github/html"
    mypath=os.path.join(def_path,cur_path)
    try:
        os.chdir(mypath)
        print("the folder exists")
    except OSError as Error:
        print("This is new project ")
        create(mypath,cur_path)

def create(mypath,cur_path):
    os.mkdir(mypath)
    asstes=os.path.join(mypath,"assests")
    os.mkdir(asstes)
    os.chdir(mypath)
    f=open("index.html","w+")    
    stylepath=os.path.join(mypath,"style")
    os.mkdir(stylepath)
    os.chdir(stylepath)
    f2=open("style.css","w+")
    css=('''*{
    margin:0;
    padding: 0;
    box-sizing: border-box;
}''')
    f2.write(css)
    f2.close
    html=('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
</head>
<body>
    
</body>
</html>'''.format(cur_path))
    f.write(html)
    f.close()

    if(os.path.exists(mypath)):
        print("done")
    else:
        print("requests rejected")


 
cre_path=input("Enter the project name ")
print("Checking if the project exists :")
trying(cre_path)