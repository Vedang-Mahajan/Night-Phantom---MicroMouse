"""
Created on Wed Jun 10 17:58:41 2020

@author: Vedang Mahajan
"""

p = 3.14

Step_Angle = float(input("Enter the step angle(cm): "))
print("")

Dist_Trav = float(input("Enter the distance to be travelled(cm): "))
print("")

Wheel_Diam = float(input("Enter the diameter of the wheel(cm): "))
print("")

Cir = (Wheel_Diam*22)/7.0

Total_Steps = 360/Step_Angle

Dist_One_Step = Cir/Total_Steps

Number_of_steps = Dist_Trav/Dist_One_Step

print("You will travel " +str(Dist_One_Step) +" cm in one step, and you will need " +str(Number_of_steps) +" steps to travel " +str(Dist_Trav) +" cm.")
