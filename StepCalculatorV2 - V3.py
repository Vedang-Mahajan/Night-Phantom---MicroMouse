import pygame
import pygame.font
import time
import rotateImage as rotator

# Py Game Initialization
pygame.init()
size = (1262,680)
screen = pygame.display.set_mode(size) # Setting the Screen
clock = pygame.time.Clock()




# Display the Background Image

backImg = pygame.image.load("Images/Step Markings.PNG")

screen.blit(backImg,(0,0))

pygame.display.update()

#--------------------------------------------

#Display the Image of the Wheel at its position
image= pygame.image.load("Images/Stepper Motor Symbol.png")
""" Display Image at Specific Co-Ordinate"""

screen.blit(image,(55,50))
w, h = image.get_size()

image1= pygame.image.load("Images/Stepper Motor Symbol1.png")
""" Display Image at Specific Co-Ordinate"""

screen.blit(image,(300, 300))
w, h = image.get_size()

#----------------------------------------------

angle = 0
done = True

# Take user Input for StepAngle, Diameter & Distance
stepAngle= float(input("Enter the Step Angle: "))
diameter=int(input("Enter the Diameter: "))
distance=int(input("Enter the Distance to be covered: "))
#------------------------------------------------

#Calculations of Dist. in 1 Step and Total number of Steps
distIn1Step = ((3.14*diameter)*stepAngle)/360
print("Distance in One Step: "+str(distIn1Step))
steps = distance / distIn1Step

print("Steps: "+str(steps))
#------------------------------------------------

#Show the Quantities entered by the user on the display for the first wheel

#To Display Text: Step Angle for the first wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render(str(stepAngle), False, (255, 255, 255))

screen.blit(text, (1091, 185))

#To Display Text: Wheel Diameter for the first wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render(str(diameter), False, (255, 255, 255))

screen.blit(text, (1107, 255))

#To Display Text: Wheel Direction for the first wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render("Forward", False, (255, 255, 255))

screen.blit(text, (1062, 324))
#------------------------------------------------------------

#Show the Quantities entered by the user on the display for the second wheel

#To Display Text: Step Angle for the second wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render(str(stepAngle), False, (255, 255, 255))

screen.blit(text, (1091, 489))

#To Display Text: Wheel Diameter for the second wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render(str(diameter), False, (255, 255, 255))

screen.blit(text, (1107, 555))

#To Display Text: Wheel Direction for the second wheel
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render("Forward", False, (255, 255, 255))

screen.blit(text, (1062, 618))
#------------------------------------------------------------

#Display Status as Travelling....

#To Display Text: "Travelling"
font = pygame.font.SysFont('Bauhaus 93', 35)
text = font.render("Travelling...", False, (0, 0, 255))
image1 = pygame.Surface((text.get_width()+1, text.get_height()+1))
pygame.draw.rect(image1, (0, 0, 255), (1, 1, *text.get_size()))
screen.blit(text, (650, 420))

#-------------------------------------------------------------

done = False
count=0

distanceTravelled=0

while not done:
    
   # To Exit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done = True

#------------------------------------------------------     
   

# Check whether stepsCount has reached the number of steps calculated
    if count<steps: # If not reached then Rotate the wheel by 1 step angle
        
        #To Display Text: StepCount
       
        font = pygame.font.SysFont('Bauhaus 93', 35)
       
        text = font.render(str(count+1), False, (255, 255, 255),(85,49,133))
        
        screen.blit(text, (160, 530))
        time.sleep(0.3)
        
        #To Rotate Wheel
        rotator.blitRotate(screen, image,(27,18),  angle)
        
        rotator.blitRotate(screen, image1,(300,300),  angle)
        
        #Update StepAngle , StepCount and Distance Travelled
        angle -= stepAngle
        count+=1
        
        distanceTravelled= distanceTravelled + round(distIn1Step,3)
        
        distanceTravelled=round(distanceTravelled,3)
        
        #To Show Text: Distance Travelled
        font = pygame.font.SysFont('Bauhaus 93', 35)
        text = font.render(str(distanceTravelled), False, (255, 255, 255),(85,49,133))
         
        # # To Clear the previous distance travelled value
        # screen.fill(pygame.Color(85,49,133), (1070,560,*text.get_size()))
        
       
        screen.blit(text, (505, 177))
        pygame.display.flip()
        pygame.display.update()
        time.sleep(0.01)

    else:
        #To Display status as Reached
        
          # To Clear the previous status
        font = pygame.font.SysFont('Bauhaus 93', 35)
        text = font.render("Travelling...", False, (204,204,204))
        
        screen.blit(text, (650, 420))
       
        # #Show the new status as Reached
        text = font.render("Reached", False, (255, 0, 0))
       
        screen.blit(text, (650, 420))
        pygame.display.update()
        time.sleep(1)

pygame.quit()
