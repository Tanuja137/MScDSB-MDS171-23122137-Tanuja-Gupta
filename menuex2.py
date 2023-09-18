#CReate a menu driven program that collects students data
#>name
#>Email
#>PHONE
#[Use dictionary to store student details]

#Menu Options
#1.Create Students
#2.Search for students"3
#3. Print students

StudentDict={}
def createstudent(name,regno,email,phone):
    student={
        "Name": name,
        "Email": email,
        "Phone": phone
    }
    StudentDict[regno]=student
def collectStudentinfo():
    name=input("Enter student name:")
    regno=input("Enter student reg no:")
    email=input("Enter student email:")
    phone=input("Enter student phone no:")
    return name,regno,email,phone
def printStudents():
 print("Regno\tName\tEmail\tPhone")
 for regno in StudentDict.keys():
    print(regno,end='\t')
    for key in StudentDict[regno]:
       print(StudentDict[regno][key],end='\t')
    print()

 while True:
    print("Menu options")
    print("1. Enter student info")
    print("2. List students")
    print("3. Exit")
    choice = input("Enter the choice").strip()
    if choice == "1":
        name, regno, email, phone = collectStudentinfo()
        createstudent(name, regno, email, phone)
    elif choice == "2":
        printStudents()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
    




