import csv

dict_columns = ['Name','MFC','DC','DS','ASE']
dict_rows=[
    {'Name' : 'Abhi' , 'MFC' : 90 , 'DC':95 , 'DS':75 , 'ASE':89},
    {'Name' : 'Akshaya' , 'MFC' : 80 , 'DC':75 , 'DS':95 , 'ASE':99},
    {'Name' : 'Ashik' , 'MFC' : 70 , 'DC':85 , 'DS':95 , 'ASE':69},
    {'Name' : 'Aswadev' , 'MFC' : 80 , 'DC':65 , 'DS':98 , 'ASE':95},
    {'Name' : 'Bharath' , 'MFC' : 68 , 'DC':75 , 'DS':67 , 'ASE':99},
    {'Name' : 'Diya' , 'MFC' : 90 , 'DC':95 , 'DS':95 , 'ASE':99},
    {'Name' : 'Jijo' , 'MFC' : 80 , 'DC':88 , 'DS':87 , 'ASE':88},
    {'Name' : 'Libi' , 'MFC' : 80 , 'DC':89 , 'DS':89 , 'ASE':78},
    {'Name' : 'Nithasha' , 'MFC' : 92 , 'DC':92 , 'DS':98 , 'ASE':99},
    {'Name' : 'Venu' , 'MFC' : 99 , 'DC':99 , 'DS':99 , 'ASE':99},

    ]
with open('marks.csv' , 'w') as csvwrite:
    write = csv.DictWriter(csvwrite , fieldnames = dict_columns)
    write.writeheader()
    write.writerows(dict_rows)

n=0
total=[]
sums=0
percentage=0
mfc=[]
dc=[]
ds=[]
ase=[]
with open('marks.csv') as csvread:
    read = csv.DictReader(csvread)
    for data in read:
        if n == 0:
            print(f'{"  ".join(data)}')
            n=n+1
        print(f'{data["Name"]}  {data["MFC"]} {data["DC"]} {data["DS"]} {data["ASE"]}')
        sums = (int(data["MFC"])+int(data["DC"])+int(data["DS"])+int(data["ASE"]))
        mfc.append(int(data["MFC"]))
        dc.append(int(data["DC"]))
        ds.append(int(data["DS"]))
        ase.append(int(data["ASE"]))
        percentage=(sums/400)*100
        print(f'Total :{sums} Percentage : {percentage}\n')
        total.append(sums)

sums=0
for i in mfc:
    sums=sums+i
print("Average Mark of MFC : ",sums/10)
sums=0
for i in dc:
    sums=sums+i
print("Average Mark of DC : ",sums/10)
sums=0
for i in ds:
    sums=sums+i
print("Average Mark of DS : ",sums/10)
sums=0
for i in ase:
    sums=sums+i
print("Average Mark of ASE : ",sums/10)

        

    
    
