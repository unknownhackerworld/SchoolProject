inputs = ["ID","Name","Age","DOB","Contact No","Emergency Contact"]
print("Enter Details")
infos = dict()
single = {}

while True:
    for info in inputs:
        if info == "DOB":
            a = str(input(f'Enter Your DOB (DD/MM/YYYY): '))
        else:
            a = str(input(f'Enter Your {info}: '))
        infos[info] = a
        single.update({ infos['ID'] : infos })
    

