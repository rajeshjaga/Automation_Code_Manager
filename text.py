import win as w





yes=[
    'y',
    'Y',
    'yes',
    'Yes',
    'YES',
    'YEs',
    'Yes',
    'yES',
    
]
no=[
    'n',
    'N',
    'no',
    'No',
    'NO',
    'nO'  
]


def main(op):
    i =input('Do you want to proceed (Y/n)')
    for c in yes :
        if(i==c):
            w.opion(op)
        else:
            pass
        

def main2():
    i =input('Do you want to proceed (Y/n)')
    for c in yes :
        if(i==c):
            w.deli()
        else:
            pass
        
def main3():
    i =input('Do you want to proceed (Y/n)')
    for c in yes :
        if(i==c):
            return True
        else:
            for x in no:
                if(i==x):
                    return False
                else:
                    pass
            
            
        
def main4(path):
   
    i =input('Do you want to proceed (Y/n)')
    for c in yes :
        if(i==c):
            return True
        else:
            pass
        