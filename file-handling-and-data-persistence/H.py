def A():
    f=open('Diary.txt','r')
    x=f.readlines()
    c=len(x)
    print("The total no of lines in a txt file is",c)
    for i in x:
        y=i.strip()
        if len(y)>0 and y[-1]=="A":
            print(y)
    f.close()


A()
