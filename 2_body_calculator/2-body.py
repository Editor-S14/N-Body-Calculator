import math
G = 6.674e-11   # Gravitational constant
m1 = float(input("Enter The Mass of Object 1: "))
m2 = float(input("Enter The Mass of Object 2: "))
Par1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
Par2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
ValueX=Par1.split(",")
Par1X=int(ValueX[0])
Par1Y=int(ValueX[1])
ValueY=Par2.split(",")
Par2X=int(ValueY[0])
Par2Y=int(ValueY[1])
Xd=Par2X-Par1X
Yd=Par2Y-Par1Y
r=math.sqrt((Xd**2)+(Yd**2))
force = G * (m1 * m2) / (r**2)
unit_vecAX=(Xd/r)
unit_vecAY=(Yd/r)
unit_vecBX=(Xd*-1)/r
unit_vecBY=(Yd*-1)/r
accel1=force/m1
accel2=force/m2
print("The exact gravitational force:", force, "N")
print("The Speed of Object 1:",accel1)
print("The Speed of Object 2:",accel2,"units/s")
print("The Direction of Object 1:","[",unit_vecAX,",",unit_vecAY,"]")
print("The Direction of Object 2:","[",unit_vecBX,",",unit_vecBY,"]")
