import pygame
import random
import pygame
A=[3,4,15,5,6]
print(A)
def game():
     pygame.init()

# Set the dimensions of the window
     width = 200
     height = 200
     window = pygame.display.set_mode((width, height))
     pygame.display.set_caption("Ball Array")

# Define colors
     BLACK = (0, 0, 0)
     RED = (255, 0, 0)

# Define ball dimensions and spacing
     ball_radius = 20
     ball_spacing = 10

# Define the list of values

# Find the maximum value in the list
     max_value = max(A)

# Create a dictionary to store the counts for each element
     counts = {}

# Count the occurrences of each element in the list
     for element in A:
          counts[element] = A.count(element)

# Find the number of balls needed in each column
     num_balls_per_column = max(counts.values())

# Calculate the total width and height of the ball array
     array_width = (ball_radius * 2 + ball_spacing) * len(counts) - ball_spacing
     array_height = (ball_radius * 2 + ball_spacing) * num_balls_per_column - ball_spacing

# Calculate the starting position for the ball array
     start_x = (width - array_width) // 2
     start_y = (height - array_height) // 2

# Create a list to store the ball positions
     ball_positions = []

# Generate ball positions for the array
     for element, count in counts.items():
          for i in range(count):
               x = start_x + len(ball_positions) * (ball_radius * 2 + ball_spacing) + ball_radius
               y = start_y + i * (ball_radius * 2 + ball_spacing) + ball_radius
               ball_positions.append((x, y))

# Game loop
     running = True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False

    # Fill the window with black color
          window.fill(BLACK)

    # Draw balls in the array
          for position in ball_positions:
               pygame.draw.circle(window, RED, position, ball_radius)

    # Update the display
          pygame.display.update()

# Quit Pygame
     pygame.quit()



f=0
x=0
while(1):
#     game()
    
    fff=0
    for i in A:
         fff+=i
    if fff==0:
         if f==0:print("AI lose")
         else:print("you lose")
    if f==1:
     #    print("Before your move :")
     #    print(A)
        x=int(input("index : "))
        xx=int(input("Value : "))
        x-=1
        while x<0 or x>= len(A) or A[x]<xx or xx==0:
             print("indalid move out of index or not enough ball ")
             x=int(input("index : "))
             xx=int(input("Value : "))
             x-=1
        A[x]-=xx
        if x>=1:A[x-1]+=xx
        
        print("After your move :")
        print(A)
        f=f^1
        continue
    total=0
    if x%2==1:
         A[x-1]-=xx
         if x>=2:A[x-2]+=xx
         print("After AI move: ")
         print(A)
         f=f^1
         continue
    for i in range(len(A)):
         if i%2==1:continue
         else :total^=A[i]
    for i in range(len(A)):
         if i%2==1:continue
         ff=total^A[i]
         flag=0
         for j in range(0,A[i]):
              
              if j^ff==0:
                   flag=1
                   if i!=0: A[i-1]+=A[i]-j
                   A[i]=j
                   
                   break
         if flag==1:break
    print("After AI move: ")
    print(A)
    f=f^1
