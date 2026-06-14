import sys
import numpy as np
G=6.674e-11
m2 = float(input("Enter The Mass of Body 2:"))
m3 = float(input("Enter The Mass of Body 3:"))
Cord1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
Cord2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
Cord3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
BodyA=np.array([float(Cord1)])
BodyB=np.array([Cord2])
BodyC=np.array([Cord3])
while True:
    m1 = float(input("Enter The Mass of Body 1:"))
    m2 = float(input("Enter The Mass of Body 2:"))
    m3 = float(input("Enter The Mass of Body 3:"))
    Cord1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
    Cord2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
    Cord3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
    Value1=Cord1.split(",")
    Value2=Cord2.split(",")
    Value3=Cord3.split(",")
    if Value1[0]!='' and Value2[0]!='' and Value3[0]!='':
        xA=(Value1[0])
        xB=(Value2[0])
        xC=(Value3[0])
        break
    elif Value1[1]!='' and Value2[1]!='' and Value3[1]!='':
        yA=(Value1[1])
        yB=(Value2[1])
        yC=(Value3[1])
        break
    else:
        print("Error!! Inputted Incorrect Cordinates, Reloading Program")
        continue
    
BodyCords=np.array([[xA,yA],
                    [xB,yB],
                    [xC,yB]])

print(BodyCords)