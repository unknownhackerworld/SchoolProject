from pyfiglet import Figlet
import random

ids=[]
  # Figlet
inputs = ["Name","Age","DOB","Contact No","Emergency Contact"]
infos = {}

def cntn():

    print("\n")
    yn = input("Press Enter To Continue")
    if yn == "":
        pass
    else:
        exit()

def fig(text):
    print(Figlet(font="doom").renderText(text))

def newAdmission():
    single = {}
    rand = random.randrange(1, 999)
    ids.append(rand)
    single["ID"] = str(rand)
    print("Enter Details")
    for info in inputs:
        if info == "DOB":
            a = str(input('Enter Your DOB (DD/MM/YYYY): '))
        else:
            a = str(input(f'Enter Your {info}: '))

        single[info] = a
    
    infos.update({rand: single})
    print(f"\nYour ID is {rand}")


def bookAppointment():
    id = int(input("Please Enter Your ID: "))
    if id in ids:
        prob = str(
            input("Enter A Brief Explanation Of Your Problem: "))
        time_slot = input("Enter Time Slot (Today) HH:MM: ")
        infos[id]["problems"] = prob
        infos[id]["time"] = time_slot

    else:
        print("Please Create Admission")

def checkAppointment():
    id = int(input("Please Enter Your ID: "))
    print("\n")
    try:
        if id in ids:
            print("Problems\t\tTime Slot")
            print(infos[id]["problems"], "\t\t\t", infos[id]["time"],"\n\n")
        else:
            print("Please Create Admission\n\n")
    except KeyError:
        print("No Appointment Record\n\n")

def deleteUser():
    id = int(input("Please Enter Your ID: "))
    if id in ids:
        con = str(
            input("Are You Sure You Wanna Delete Your Account? (Y/N)")).upper()
        if con == "Y":
            del infos[id]
            ids.remove(id)
            print("Record Deleted!")
        else:
            pass

    else:
        print("Please Create Admission")

def viewDetails():
    id = int(input("Please Enter Your ID: "))
    print("\n")
    if id in ids:
        for iD, info in infos.items():
            if iD == id:
                for key in info:
                    print(key + ':', info[key])
                print()    
    else:
        print("Please Create Admission")        
    

def viewAllDetails():
    for key,value in infos.items():
        for key in value:
            print(key + ':', value[key])
        print()    

def viewAppointments():
    if infos:
        try:
            for key in infos.keys():
                print(infos[key]["problems"])
        except KeyError:
            print("No Records")
    else:
        print("No Records")            


def admin():
    
    fig("Admin Panel")
    password = str(input("Enter Password: "))
    if password == "SSM":
        while True:
            print("\n")
            print("Welcome To ADMIN Panel!!\n")
            print("1.No Of Patients\n2.Patients Details\n3.Check Appointment\n4.Delete User\n5.View Patient Info\n6.Patients Panel\n")
            try:
                ch = int(input("Enter Your Choice: "))
            except ValueError:
                print("Enter Valid Option")

            if (ch==1):
                print("No Of Patients: ",len(infos))

            elif (ch==2):
                viewAllDetails()

            elif (ch==3):
                viewAppointments()

            elif (ch==4):
                deleteUser()

            elif (ch==5):
                viewDetails()

            elif (ch==6):
                patient() 

            else:
                print("Enter Valid Option")
            cntn()    
    else:
        print("Incorrect Password")
        admin()

def patient():
    while True:
        fig("Patients Panel")
        print("1.New Admission\n2.Book Appointment\n3.Check Appointment\n4.Delete User\n5.View Patient Details\n6.Go To Admin\n")
        try:
            ch = int(input("Enter Your Choice: "))
        except ValueError:
            print("Enter Valid Option")       
        print("\n")
        
        try:
            if (ch == 1):
                newAdmission()

            elif (ch == 2):
                bookAppointment()

            elif (ch == 3):
                checkAppointment()
            elif (ch == 4):
                deleteUser()
            elif (ch == 5):
                viewDetails()
            elif (ch == 6):
                admin()
            else:
                print("Enter Valid Option")
        except UnboundLocalError:
            pass                  
        cntn()     

while True:
    fig("Hospital Management")
    print("1.Patient\n2.Admin")
    try:
        user = int(input("Enter Your Choice: "))
    except ValueError:
        print("Enter Valid Option\n")

    if user == 1:
        print()
        patient()
    elif user ==2:
        print()
        admin()        
    else:
        print("Enter Valid Option\n")    