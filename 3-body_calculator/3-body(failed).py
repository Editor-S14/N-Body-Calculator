import math
G = 6.674e-11   # Gravitational constant
m1 = float(input("Enter The Mass of Object 1: "))
m2 = float(input("Enter The Mass of Object 2: "))
m3 = float(input("Enter The Mass of Object 3: "))
Par1= input("Enter The Coordinates of Object 1(Seperated by Comas): ")
Par2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
Par3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
Value1=Par1.split(",")
aX=int(Value1[0])
aY=int(Value1[1])
Value2=Par2.split(",")
bX=int(Value2[0])
bY=int(Value2[1])
Value3=Par3.split(",")
cX=int(Value3[0])
cY=int(Value3[1])
AB=math.sqrt(((bX-aX)**2)+((bY-aY)**2))
BC=math.sqrt(((cX-bX)**2)+((cY-bY)**2))
AC=math.sqrt(((cX-aX)**2)+((cY-aY)**2))
force1 = G * (m1 * m2) / (AB**2)
force2 = G * (m2 * m3) / (BC**2)
force3 = G * (m1 * m3) / (AC**2)
par1F= force1+force3
par2F= force1+force2
par3F= force2+force3
print(f"Object 1 is Experiencing {par1F} N")
print(f"Object 2 is Experiencing {par2F} N")
print(f"Object 3 is Experiencing {par3F} N")