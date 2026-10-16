import math

def get_number(prompt):
    """Take numeric input safely, allows decimals too."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_choice(prompt, valid_choices):
    """Take integer menu choice, re-ask if invalid."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
        except ValueError:
            pass
        print(f"Please enter a valid option {valid_choices}.")


def rectangle():
    length = get_number("Enter the length of rectangle: ")
    width = get_number("Enter the width of rectangle: ")

    area = length * width
    perimeter = 2 * (length + width)
    diagonal = math.sqrt(length**2 + width**2)

    print("1.Area  2.Perimeter  3.Diagonal")
    choice = get_choice("Choose what you want to calculate: ", [1, 2, 3])

    result = {1: area, 2: perimeter, 3: diagonal}[choice]
    print(round(result, 2))


def square():
    side = get_number("Enter the side length of the square: ")

    area = side ** 2
    perimeter = 4 * side
    diagonal = math.sqrt(2) * side

    print("1.Area  2.Perimeter  3.Diagonal")
    choice = get_choice("Choose what you want to calculate: ", [1, 2, 3])

    result = {1: area, 2: perimeter, 3: diagonal}[choice]
    print(round(result, 2))


def four_walls():
    length = get_number("Enter the length of the room: ")
    width = get_number("Enter the width of the room: ")
    height = get_number("Enter the height of the room: ")

    area = 2 * (length + width) * height  # fixed: was length+length before
    print("The area of 4 walls is:", round(area, 2))


def circle():
    radius = get_number("Enter the radius of the circle: ")

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    print("1.Diameter  2.Circumference  3.Area")
    choice = get_choice("Choose what you want to calculate: ", [1, 2, 3])

    result = {1: diameter, 2: circumference, 3: area}[choice]
    print(round(result, 2))


def main():
    print("1.Rectangle")
    print("2.Square")
    print("3.4 Walls")
    print("4.Circle")

    shape = get_choice("Choose the shape: ", [1, 2, 3, 4])

    shape_functions = {
        1: rectangle,
        2: square,
        3: four_walls,
        4: circle,
    }
    shape_functions[shape]()


if __name__ == "__main__":
    main()