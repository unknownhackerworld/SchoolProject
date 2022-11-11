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
        print("1.New Admission\n2.Book Appointment\n3.Check Appointment\n4.Delete User")
        ch = int(input("Enter Your Choice: "))
        if (ch==1):    
            print("Enter Details")
            for info in inputs:
                if info == "DOB":
                    a = str(input(f'Enter Your DOB (DD/MM/YYYY): '))
                else:
                    a = str(input(f'Enter Your {info}: '))
                single[info] = a
                infos.update({ single['ID'] : infos })
            print("\n"*5)

        elif (ch==2):
            id = int(input("Please Enter Your Id: "))
            if id in infos:
                prob = str(input("Enter A Brief Explanation Of Your Problem: "))
            else:
                print("Please Create Admission")
            print("\n"*5)


