import pygame
import pygame.font
import time
import rotateImage as rotator

current_y_position = 216
current_x_position = 22

# $ PyGame Initialization
pygame.init()
size = (1262,680)
screen = pygame.display.set_mode(size) # Setting the Screen
clock = pygame.time.Clock()


# $ Display the Background Image

backImg = pygame.image.load("Images/Step Markings2.png")

screen.blit(backImg,(0,0))

pygame.display.update()

#---------------------------------------------------------------------------------------------------------

# $ Display the Bot Image

BotImg = pygame.image.load("Images/Transparent - Bot Image.png")

screen.blit(BotImg,(current_x_position,current_y_position))

pygame.display.update()

#----------------------------------------------------------------------------------------------------------

while True:
    print("")
    print("Enter the movement you want to conduct below. Enter 'U' to move up, 'D' to move down, 'R' ")
    movement_direction = input("Enter the movement you want to conduct: ").lower()
    
    if movement_direction == "x":
        break
        pygame.quit()
    
    if movement_direction == "u":
        movement_value = int(input("Enter the number of steps you want to move up: "))
        
        try:
            movement_value == int
        except:
            pygame.quit()
            
        for x in range (movement_value):
            pygame.display.update()
            screen.blit(backImg,(0,0))
            screen.blit(BotImg,(22,cellY))
            current_y_position = current_y_position-26.5
