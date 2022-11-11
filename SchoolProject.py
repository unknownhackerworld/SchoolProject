from pyfiglet import Figlet

fig = Figlet(font="doom").renderText('Hospital Management')  # Figlet
inputs = ["ID","Name","Age","DOB","Contact No","Emergency Contact"]
infos = {}
single = {}


while True:
    print(fig)
    print("1.Patient\n2.Admin")
    user = int(input("Enter Your Choice: "))
    print("\n"*5)
    if (user==1):
        print("1.New Admission\n2.Book Appointment\n3.Check Appointment\n4.Delete User\n5.View Patient Details")
        ch = int(input("Enter Your Choice: "))
        print("\n"*3)
        
        if (ch==1):    
            print("Enter Details")
            for info in inputs:
                if info == "DOB":
                    a = str(input('Enter Your DOB (DD/MM/YYYY): '))
                else:
                    a = str(input(f'Enter Your {info}: '))
                single[info] = a
                infos.update({ single['ID'] : single })
            print("\n"*5)
            
        elif (ch==2):
            id = str(input("Please Enter Your ID: "))
            if id in infos:
                prob = str(input("Enter A Brief Explanation Of Your Problem: "))
                time_slot = input("Enter Time Slot (Today) HH:MM: ")
                infos[id]["problems"] = prob
                infos[id]["time"] = time_slot
                

            else:
                print("Please Create Admission")
            print("\n"*5)

        elif(ch==3):
            id = str(input("Please Enter Your ID: "))
            try:
                if id in infos:
                    print("Problems\t\tTime Slot")
                    print(infos[id]["problems"],"\t\t\t",infos[id]["time"])
                else:
                    print("Please Create Admission")
            except KeyError:
                print("Please Create Admission")
        elif(ch==4):
            id = str(input("Please Enter Your ID: "))
            if id in infos:
                con = str(input("Are You Sure You Wanna Delete Your Account? (Y/N)")).upper()
                if con == "Y":
                    del infos[id]
                    print("Record Deleted!")
                else:
                    pass    

            else:
                print("Please Create Admission")

    elif (user==2):
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
                    print("\nPerson ID:", key)

                    for key in value:
                        print(key + ':', value[key])
            if (ch==3):
                for key in infos.keys():
                    print(infos[key]["problems"])
