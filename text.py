import win as w


yes=[
    'y',
    'Y',
    'yes',
    'Yes',
    'YES',
    'YEs',
    'Yes',
    'yES'
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
        