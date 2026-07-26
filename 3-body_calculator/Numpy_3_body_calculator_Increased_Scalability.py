import numpy as np
G=6.674e-11
while True:
    m1 = input("Enter The Mass of Body 1:")
    m2 = input("Enter The Mass of Body 2:")
    m3 = input("Enter The Mass of Body 3:")
    Cord1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
    Cord2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
    Cord3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
    try:
        m1=float(m1)
        m2=float(m2)
        m3=float(m3)
        
    except ValueError:
        print("One of the Masses aren't a numerical value")
        continue
    try:
        if "," in Cord1 and "," in Cord2 and "," in Cord3:
            Value1=Cord1.split(",")
            Value2=Cord2.split(",")
            Value3=Cord3.split(",")
            if Value1[0]!='' and Value2[0]!='' and Value3[0]!='':
                xA=float(Value1[0])
                xB=float(Value2[0])
                xC=float(Value3[0])
                if Value1[1]!='' and Value2[1]!='' and Value3[1]!='':
                    yA=float(Value1[1])
                    yB=float(Value2[1])
                    yC=float(Value3[1])
                    break
            else:
                print("Error!! Incomplete or Incorrect Coordinates, Reloading Program")
                continue
        else:
            print("Error!! Incomplete or Incorrect Coordinates, Coordinates Doesn't Contain ',' Seperation")
            continue
    except ValueError:
        print("Error!! Incomplete or Incorrect Coordinates, Reloading Program")
        continue
    except:
        print("Error!! Incomplete or Incorrect Coordinates, Reloading Program")
        continue
    
    
BOCO=np.array([[xA,yA],
                    [xB,yB],
                    [xC,yC]])
Vec_AB=BOCO[1]-BOCO[0]
Vec_BC=BOCO[2]-BOCO[1]
Vec_AC=BOCO[2]-BOCO[0]

AB=np.sqrt(np.sum(Vec_AB**2))
BC=np.sqrt(np.sum(Vec_BC**2))
AC=np.sqrt(np.sum(Vec_AC**2))
force_1=G*((m1*m2)/AB**2)
force_2=G*((m3*m2)/BC**2)
force_3=G*((m1*m3)/AC**2)
UV_A=
print(f"{AB} {BC} {AC}")
print(f"{force_1},{force_2},{force_3}")
