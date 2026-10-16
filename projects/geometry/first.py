# first Shape Selection
print("1.Rectangle")
print("2.Square")
print("3.4 Walls")
print("4.Circle")
shape = int(input("Choose The Shape: "))

#Rectangle
if shape == 1:
#Rectangle Inputs
    lenth_of_rectangle = int(input("Enter The lenth Of Rectangle: "))
    width_of_rectangle = int(input("Enter The width Of Rectangle: "))
# Rectangle Main formulas
    area_of_rectangle = (lenth_of_rectangle*width_of_rectangle)
    perimeter_of_rectangle = 2*(lenth_of_rectangle+width_of_rectangle)
    diagonal_of_rectangle = ((lenth_of_rectangle*lenth_of_rectangle)+(width_of_rectangle*width_of_rectangle))**0.5
#rectangle intent input
    print("1.Area  2.Perimeter  3.Diagonal ")
    rectangle_intent = int(input("Choose What You Want to calculate: "))
    if rectangle_intent == 1:
        print(area_of_rectangle)
    elif rectangle_intent == 2:
        print(perimeter_of_rectangle)
    elif rectangle_intent == 3:
        print(diagonal_of_rectangle)


#Square
elif shape == 2:
#square input
    side = int(input("Enter The Side Lenth Of The Square: "))
# Square Main formulas
    area_of_square = (side*side)
    perimeter_of_square = (4*side)
    diagonal_of_square = 2**0.5*side
# square intent input
    print("1.Area  2.Perimeter  3.Diagonal ")
    square_intent= int(input("Choose What You Want to calculate: "))
    if square_intent == 1:
        print(area_of_square)
    elif square_intent == 2:
        print(perimeter_of_square)
    elif square_intent == 3:
        print(diagonal_of_square)


#4 wall
elif shape == 3:
#4 wall Input
    lenth_of_4wall = int(input("Enter The lenth Of 4 wall: "))
    width_of_4wall = int(input("Enter The width Of 4 wall: ")) 
    height_of_4wall = int(input("Enter The height Of 4 wall: ")) 
# 4 wall main formula
    area_of_4wall = 2*(lenth_of_4wall+width_of_4wall)*height_of_4wall
    print("The Area Of 4 Wall Is" ,area_of_4wall)


# Circle
elif shape == 4:
# Circle Input
    radius_of_circle = int(input("Enter The Radius Of The Circle: "))
#Circle Formulas
    diameter_of_circle = 2* radius_of_circle
    circumferance_of_circle =  2 * radius_of_circle * (22/7)
    area_of_circle = (22/7)*radius_of_circle*radius_of_circle
#circle intent
    print("1.Diameter 2.Circumferance 3.Area")
    circle_intent = int(input("Choose What You Want to calculate: "))
    if circle_intent == 1:
        print(diameter_of_circle)
    elif circle_intent == 2:
        print(circumferance_of_circle)
    elif circle_intent == 3:
        print(area_of_circle)











