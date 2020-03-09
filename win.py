import os


def trying(cur_path):
    def_path="c:/users/hp/documents/github/html"
    mypath=os.path.join(def_path,cur_path)
    try:
        os.chdir(mypath)
        print("the folder exists")
    except OSError as Error:
        print("This is new project ")
        print(create(mypath,cur_path))

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
    <link rel="stylesheet" href="./style/style.css">
    <title>{}</title>
</head>
<body>
    
    <script src="./script/app.js">  </script>
</body>
</html>'''.format(cur_path))
    f.write(html)
    f.close()
   
    sceip=os.path.join(mypath,"script")
    os.mkdir(sceip)
    os.chdir(sceip)
    f2=open("app.js","w+")
    if(os.path.exists(mypath)):
        print("done")
    else:
        print("requests rejected")

# optionlios=[2,3]
# option=int(input("\n 1. Create new HTML project \n 2.Flutter \n 3.Python \n 4.Exit \n"))
def opion(optin):
    if(optin==1):
        cre_path=input("Enter the project name :")
        print("Checking if the project exists...")
        trying(cre_path)
    else:
        do=input("Do you want to exit ? :(Y/N)")
        if(do=="y","Y"):
           exit()
        else:
            trying(cre_path)


