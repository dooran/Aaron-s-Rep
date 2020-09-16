#Manuel Duran 1584885
import math #import math package

height = int(input("Enter wall height (feet):\n")) #enter the height

width = int(input("Enter wall width (feet):\n")) #enter the width of wall

wall_area = height * width #calculating wall area

paint_needed = wall_area / 350 #find gallons of paint needed

cans = math.ceil(paint_needed) #find nearest value of cans by ceil function

paint_colors_cost={'red':35,'blue':25,'green':23} #paint colors cost dictionary

print("Wall area: " + str(wall_area) + " square feet") #print wall area

print("Paint needed: {:.2f} gallons".format(paint_needed)) #print paint needed

print("Cans needed: " + str(cans) + " can(s)") #print number of cans needed

color=input("\nChoose a color to paint the wall:\n") #ask user to choose a color

cost=cans * paint_colors_cost[color.lower()] #find the cost

print ("Cost of purchasing " + str(color) + " paint: $" + str(cost)) #print the cost