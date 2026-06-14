import math
import numpy as np
G=6.674e-11
m1 = float(input("Enter The Mass of Body 1:"))
m2 = float(input("Enter The Mass of Body 2:"))
m3 = float(input("Enter The Mass of Body 3:"))
Cord1= input("Enter The Coordinates of Object 1(Seperated by Commas): ")
Cord2= input("Enter The Coordinates of Object 2(Seperated by Commas): ")
Cord3= input("Enter The Coordinates of Object 3(Seperated by Commas): ")
BodyA=np.array([float(Cord1)])
BodyB=np.array([Cord2])
BodyC=np.array([Cord3])
print(BodyB)