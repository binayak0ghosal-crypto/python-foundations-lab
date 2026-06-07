import pickle
##
##def read():
##    f=open('Text.dat','rb')
##    try:
##        while True:
##            x=pickle.load(f)
##            print(x)
##    except EOFError:
##            f.close()
##
###main
##read()
##import pickle

def search_student(rno):
    f = open("Text.dat", "rb")
    found = False
    try:
        while True:
            rec = pickle.load(f)
            if rec[0] == rno:   # roll number match
                print("Record found:", rec)
                found = True
                break
    except EOFError:
        f.close()
    if not found:
        print("Record not found.")

# Example
search_student(2)
