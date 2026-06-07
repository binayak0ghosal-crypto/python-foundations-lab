def ISTOUPPERCOUNT():
    f=open("Diary.txt",'r')
    x=f.read()
    z=x.split()
    c=0
    c1=0
    for i in z:
        if i=="UP":
            c +=1
            print(i)
        elif i=="IS":
            c1 +=1
            print(i)
    print(f"The no of times the word UP is appearing is {c}")
    print(f"The no of times the word IS is appearing is {c1}")
    f.close()
#Main_py
ISTOUPPERCOUNT()   
        
