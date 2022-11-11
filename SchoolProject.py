inputs = ["Donor ID","Name","Age","DOB","Contact No","Emergency Contact"]
print("Enter Details")
infos = dict()
while True:
    for info in inputs:
        a = str(input(f'Enter Your {info}: '))
        b =a 
        infos[info] = b

    print(infos)