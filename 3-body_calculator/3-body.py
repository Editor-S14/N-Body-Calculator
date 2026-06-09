import math
G = 6.674e-11   # Gravitational constant
m1 = float(input("Enter The Mass of Object 1: "))
m2 = float(input("Enter The Mass of Object 2: "))
m3 = float(input("Enter The Mass of Object 3: "))
Par1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
Par2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
Par3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
Value1=Par1.split(",")
aX=float(Value1[0])
aY=float(Value1[1])
Value2=Par2.split(",")
bX=float(Value2[0])
bY=float(Value2[1])
Value3=Par3.split(",")
cX=float(Value3[0])
cY=float(Value3[1])
AB=math.sqrt(((bX-aX)**2)+((bY-aY)**2))
BC=math.sqrt(((cX-bX)**2)+((cY-bY)**2))
AC=math.sqrt(((cX-aX)**2)+((cY-aY)**2))
force1 = G * (m1 * m2) / (AB**2)
force2 = G * (m2 * m3) / (BC**2)
force3 = G * (m1 * m3) / (AC**2)

dir_AB_X=(bX-aX)/AB
dir_AB_Y=(bY-aY)/AB
dir_BC_X=(cX-bX)/BC
dir_BC_Y=(cY-bY)/BC
dir_AC_X=(cX-aX)/AC
dir_AC_Y=(cY-aY)/AC
dir_BA_X=dir_AB_X*-1
dir_BA_Y=dir_AB_Y*-1
dir_CB_X=dir_BC_X*-1
dir_CB_Y=dir_BC_Y*-1
dir_CA_X=dir_AC_X*-1
dir_CA_Y=dir_AC_Y*-1
dir_AX=(force1*dir_AB_X)+(force3*dir_AC_X)
dir_AY=(force1*dir_AB_Y)+(force3*dir_AC_Y)
Ra=math.sqrt((dir_AX**2)+(dir_AY**2))
if Ra > 0:
    final_dirA_x=dir_AX/Ra
    final_dirA_y=dir_AY/Ra
else:
    final_dirA_x=0
    final_dirA_y=0

dir_BX=(force1*dir_BA_X)+(force2*dir_BC_X)
dir_BY=(force1*dir_BA_Y)+(force2*dir_BC_Y)
Rb=math.sqrt((dir_BX**2)+(dir_BY**2))
if Rb > 0:
    final_dirB_x=dir_BX/Rb
    final_dirB_y=dir_BY/Rb
else:
    final_dirB_x=0
    final_dirB_y=0

dir_CX=(force2*dir_CB_X)+(force3*dir_CA_X)
dir_CY=(force2*dir_CB_Y)+(force3*dir_CA_Y)
Rc=math.sqrt((dir_CX**2)+(dir_CY**2))
if Rc > 0:
    final_dirC_x=dir_CX/Rc
    final_dirC_y=dir_CY/Rc
else:
    final_dirC_x=0
    final_dirC_y=0

ac1=Ra/m1
ac2=Rb/m2
ac3=Rc/m3
print(f"Object 1 is Experiencing {Ra:.4g} N")
print(f"Object 2 is Experiencing {Rb:.4g} N")
print(f"Object 3 is Experiencing {Rc:.4g} N")
print(f"The Acceleration of Object 1:{ac1:.4g} units/s/s")
print(f"The Acceleration of Object 2:{ac2:.4g} units/s/s")
print(f"The Acceleration of Object 3:{ac3:.4g} units/s/s")
print(f"The Unit Vector of Object 1:[{final_dirA_x:.3f},{final_dirA_y:.3f}]")
print(f"The Unit Vector of Object 2:[{final_dirB_x:.3f},{final_dirB_y:.3f}]")
print(f"The Unit Vector of Object 3:[{final_dirC_x:.3f},{final_dirC_y:.3f}]")