def EVENDIG():
    f=open("Diary.txt",'r')
    x=f.read()
    sum=0
    for i in x:
        if  i.isdigit():
            if int(i)%2==0:
                print(i)
                sum=sum+int(i)
    print("sum",sum)
    f.close()

EVENDIG()
