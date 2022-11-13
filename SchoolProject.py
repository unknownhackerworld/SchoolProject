from pyfiglet import Figlet
import random

ids=[]

fig = Figlet(font="doom").renderText('Hospital Management')  # Figlet
inputs = ["Name","Age","DOB","Contact No","Emergency Contact"]
infos = {}


while True:
    print(fig)
    print("1.Patient\n2.Admin")
    user = int(input("Enter Your Choice: "))
    print("\n"*5)
    while (user==1):
        single = {}
        print("1.New Admission\n2.Book Appointment\n3.Check Appointment\n4.Delete User\n5.View Patient Details\n6.Go To Admin")
        ch = int(input("Enter Your Choice: "))
        print("\n"*3)
        
        if (ch==1):   
            rand = random.randrange(1,999)
            ids.append(rand)
            single["ID"] = str(rand)
            print("Enter Details")
            for info in inputs:
                if info == "DOB":
                    a = str(input('Enter Your DOB (DD/MM/YYYY): '))
                else:
                    a = str(input(f'Enter Your {info}: '))
                    
                single[info] = a
                
            infos.update({rand:single})
            print(f"\nYour ID is {rand}\n")
            cntn = input("Press Enter To Continue")
            if cntn == "":
                pass
            else:
                exit()
            print("\n"*5)
            
        elif (ch==2):
            id = int(input("Please Enter Your ID: "))
            if id in ids:
                prob = str(input("Enter A Brief Explanation Of Your Problem: "))
                time_slot = input("Enter Time Slot (Today) HH:MM: ")
                infos[id]["problems"] = prob
                infos[id]["time"] = time_slot
                

            else:
                print("Please Create Admission")
                print(infos)
            print("\n"*5)

        elif(ch==3):
            id = int(input("Please Enter Your ID: "))
            try:
                if id in ids:
                    print("Problems\t\tTime Slot")
                    print(infos[id]["problems"],"\t\t\t",infos[id]["time"])
                else:
                    print("Please Create Admission")
            except KeyError:
                print("Please Create Admission")
        elif(ch==4):
            id = int(input("Please Enter Your ID: "))
            if id in ids:
                con = str(input("Are You Sure You Wanna Delete Your Account? (Y/N)")).upper()
                if con == "Y":
                    del infos[id]
                    print("Record Deleted!")
                else:
                    pass    
        
            else:
                print("Please Create Admission")
        elif (ch==5):
            id = int(input("Please Enter Your ID: "))
            if id in ids:
                for id, info in infos.items():
                    for key in info:
                        print(key + ':', info[key],"\n\n\n")
            cntn = input("Press Enter To Continue")
            if cntn == "":
                pass
            else:
                exit()
        elif (ch==6):
            check = input("Enter ADMIN Password: ")
            if (check=="SSM"):
                user = 2

    while (user==2):
        password = str(input("Enter Password: "))
        if password == "SSM":
            print("\n"*2)
            print("Welcome To ADMIN Panel!!")
            print("1.No Of Patients\n2.Patients Details\n3.Check Appointment\n4.Delete User\n5.View Patient Details")
            ch = int(input("Enter Your Choice: "))
            if (ch==1):
                print("No Of Patients: ",len(infos))
            if (ch==2):
                for key,value in infos.items():
                    for key in value:
                        print(key + ':', value[key])
            if (ch==3):
                for key in infos.keys():
                    print(infos[key]["problems"])