import csv
f=open(r"C:\Users\ADMIN\Desktop\Corona_Updated.csv",'w',newline='')
FH=csv.writer(f)
X=[['name','roll','clas'],
    ['GG','22','X']]
FH.writerows(X)
print(FH)

