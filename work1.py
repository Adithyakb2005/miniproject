name=[]
while True:
    print("\n 1.add","\n 2.display","\n 3.update","\n 4.delete","\n 5.exit")
    a=int(input("enter your choice:"))
    if a==1:
        b=int(input("enter how many student:"))
        for i in range(b):
            c=input("name:")
            name.append(c)
        print(name)
    elif a==2:
        for i in name:
            print(i)
    elif a==3:
       a_name=input("enter the name:")
       if a_name in name:
            new=input("enter the new name:")
            pos=name.index(a_name)
            name[pos]=new
       else:
            print("no")

    elif a==4:
        d=input('enter the name:')
        if d in name:
            name.remove(d)
        else:
            print("no")
    
    elif a==5:
        break