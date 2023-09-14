listNames=[]#empty list to store the names
#store a name to list
def storeName(name):
    name=name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True
#list all names
def listNames():
    print("-"*30)
    for name in listNames:
        print(name)
    print("-"*30)
# function to search for a name
def searchName(name):
    name=name.strip().title()
    flag=False
    for item in listNames:
        if name==item:
            flag=True
            break
    if flag==True:
        print("Name exist in the list")
           
    else:
            print("Name not found")
while True:
    print("Menu options")
    print("*"*30)
    print("1,Enter a name")
    print("2,Search a name")
    print("3,List all names")
    print("4,Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        userinp=input("Enter a name")
        retval=storeName(userinp)
        if retval==True:
            print("name added successfully")
        else:
            print("Name exists in the list")
    elif choice==2:
        userinp=input("Enter the name to be searched")
        searchName(userinp)
    elif choice==3:
        listNames()
    elif choice==4:
        exit()
    else:
        print("Invalid option , please choose correct one!")

