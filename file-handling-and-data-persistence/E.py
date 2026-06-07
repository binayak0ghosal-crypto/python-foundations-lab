       
import pickle

def update_marks(roll,new_marks):
    roll = int(input("Enter the roll no: "))
    new_marks = float(input("Enter the new marks: "))
    flag = False
    new = [] 
    try:
        f=open('Text.dat','rb')
        while True:
            x = pickle.load(f)
            if x[0] == roll:
                print("Old Record Found:", x)
                x[-1] = new_marks
                flag = True
            new.append(x)
    except EOFError:
        f.close()
    except FileNotFoundError:
        print("File not found.")
        f.close()
    f=open('Text.dat','wb')
    for x in new:
        pickle.dump(x, f)

    if not flag:
        print("Record not found")
    

update_marks(3,99.7)
