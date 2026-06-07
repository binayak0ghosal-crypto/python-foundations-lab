import pickle

def read():
    f=open('Text.dat','rb')
    x=int(input("Enter the roll no::"))
    flag=False
    try:
        while True:
            y=pickle.load(f)
            if y[0]==x:
                print(y)
                flag=True
                break
    except EOFError:
        f.close()
    if not flag:
        print("Record not found")
#Main
read()
        

