def rem_dup(d):
    list=[]
    for i in d:
        if (i not in list):
            list.append(i)
    return list
        
def CB(cr,bd):
    print("...")
    cp=[]
    for st in cr:
        if st in bd:
            cp.append(st)
    print("Student plays cricket and Badminton",cp)

def eCoB(cr,bd):
    print("....")
    cp=[]
    for st in cr:
        if st not in bd:
            cp.append(st)
    for st in bd:
        if st not in cr:
            cp.append(st)
    print("Student plays either play cricket or Badminton but not both",cp)
    
    
def nCnB(cr,bd):
    print("....")
    cp=[]
    for st in ft:
        if st not in cr and st not in bd:
            cp.append(st)
    print("Student plays neither cricket nor Badminton ",cp)
    
    
def CFnB(cr,ft,bd):
    print("....")
    cp=[]
    for st in cr:
        if st in ft and st not in bd:
            cp.append(st)
    print("Student plays cricket or football but not Badminton ",cp)   

seco=[]
n=int(input("Enter number of stud.."))
print("Enter name of stud....")
for i in range(0,n):
    name=input()
    seco.append(name)


cr=[]
n=int(input("Enter number of stud plays cricket.."))
print("Enter name of stud....")
for i in range(0,n):
    name=input()
    cr.append(name)



ft=[]
n=int(input("Enter number of stud plays football.."))
print("Enter name of stud....")
for i in range(0,n):
    name=input()
    ft.append(name)


bd=[]
n=int(input("Enter number of stud plays badminton.."))
print("Enter name of stud....")
for i in range(0,n):
    name=input()
    bd.append(name)

print("student list...",seco)
print("student list who plays cricket",cr)
print("student list who plays football",ft)
print("student list who plays badminton",bd)


ch='y'
while(ch!='n'):
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CB(cr,bd))

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCoB(cr,bd))

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(seco,cr,bd))

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CFnB(cr,ft,bd))

    else:
        print("wrong choice..")
        
        
    print("do you want to continue......")
    ch=input()
    

