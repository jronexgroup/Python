# ============================================================
#        CLASS 9 GEOMETRY PROBLEM SOLVER
#        Python Chapter 2 - 8 Practice Project
# ============================================================


# ============================================================
# CHAPTER 2
# Variables, Data Types, Operators, type(), input()
# ============================================================

program_name = "Class 9 Geometry Solver"
version = 1.0
developer = "Student"

print("\n" + "=" * 55)
print(program_name)
print("Version:", version)
print("Made by:", developer)
print("=" * 55)

# Data Types
integer_example = 10
float_example = 10.5
string_example = "Geometry"
boolean_example = True

print("\n--- Data Type Demo ---")
print(type(integer_example))
print(type(float_example))
print(type(string_example))
print(type(boolean_example))


# ============================================================
# CHAPTER 3
# Strings, Slicing, String Functions, Escape Sequences
# ============================================================

title = "GEOMETRY SOLVER"

print("\n--- String Demo ---")

# String slicing
print("First 8 characters:", title[0:8])

# Slicing with skip value
print("Every 2nd character:", title[::2])

# String functions
print("Lowercase:", title.lower())
print("Uppercase:", title.upper())
print("Length:", len(title))

# Escape sequence
print("\n\tWelcome to the Geometry Solver!\n")


# ============================================================
# CHAPTER 4
# Lists and Tuples
# ============================================================

# List
shapes = [
    "Rectangle",
    "Square",
    "4 Walls",
    "Circle",
    "Triangle",
    "Parallelogram",
    "Rhombus",
    "Trapezium"
]

# List indexing
print("--- Available Shapes ---")

for i in range(len(shapes)):
    print(i + 1, ".", shapes[i])

# List methods
shapes_copy = shapes.copy()

shapes_copy.append("Test Shape")
shapes_copy.remove("Test Shape")

print("\nTotal Shapes:", len(shapes_copy))


# Tuple
units = ("cm", "m", "km")

print("\n--- Units ---")
print("First Unit:", units[0])
print("Number of 'm':", units.count("m"))
print("Position of 'km':", units.index("km"))


# ============================================================
# CHAPTER 5
# Dictionary and Sets
# ============================================================

# Dictionary
formulas = {
    "Rectangle Area": "l × w",
    "Rectangle Perimeter": "2(l + w)",
    "Square Area": "a²",
    "Square Perimeter": "4a",
    "Circle Area": "πr²"
}

print("\n--- Formula Dictionary ---")

for name, formula in formulas.items():
    print(name, "=", formula)

# Dictionary methods
print("\nFormula Names:")
print(formulas.keys())

print("\nFormula Values:")
print(formulas.values())

print("\nTotal Formulas:", len(formulas))


# Sets
used_shapes = {"Rectangle", "Square", "Circle"}

available_shapes = {
    "Rectangle",
    "Square",
    "Circle",
    "Triangle",
    "Rhombus"
}

print("\n--- Set Operations ---")

print("Used Shapes:", used_shapes)
print("Available Shapes:", available_shapes)

print("Union:", used_shapes.union(available_shapes))
print("Intersection:", used_shapes.intersection(available_shapes))
print("Difference:", available_shapes.difference(used_shapes))


# ============================================================
# FUNCTIONS
# ============================================================

# Function with arguments
def show_result(name, value, unit=""):
    print("\n" + "-" * 40)
    print(name, "=", value, unit)
    print("-" * 40)


# Function with default parameter
def square_number(number, power=2):
    return number ** power


# ============================================================
# RECURSION
# Used for finding a perfect-square factor
# ============================================================

def find_square_factor(number, divisor=2):

    # Base condition
    if divisor * divisor > number:
        return 1

    if number % (divisor * divisor) == 0:
        return divisor

    return find_square_factor(number, divisor + 1)


# ============================================================
# EXACT SQUARE DIAGONAL
# Example:
# 10 → 10√2
# ============================================================

def square_diagonal_exact(side):

    # d = side√2
    exact_form = str(side) + "√2"

    return exact_form


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("\n")
    print("=" * 55)
    print("              SHAPE SELECTION")
    print("=" * 55)

    # for loop + range()
    for i in range(len(shapes)):
        print(i + 1, ".", shapes[i])

    print("0 . Exit")

    shape_input = input("\nChoose The Shape: ")

    # typecasting
    shape = int(shape_input)

    # ========================================================
    # EXIT
    # ========================================================

    if shape == 0:
        print("\nThank you for using Geometry Solver!")
        break


    # ========================================================
    # RECTANGLE
    # ========================================================

    elif shape == 1:

        print("\n--- RECTANGLE ---")

        length = float(
            input("Enter Length: ")
        )

        width = float(
            input("Enter Width: ")
        )

        print("\n1. Area")
        print("2. Perimeter")
        print("3. Diagonal")

        choice = int(
            input("Choose: ")
        )

        # Operators
        area = length * width

        perimeter = 2 * (length + width)

        diagonal = (
            length ** 2 +
            width ** 2
        ) ** 0.5

        # Logical + relational operators
        if choice >= 1 and choice <= 3:

            if choice == 1:
                show_result(
                    "Area",
                    area,
                    "square units"
                )

            elif choice == 2:
                show_result(
                    "Perimeter",
                    perimeter,
                    "units"
                )

            elif choice == 3:
                show_result(
                    "Diagonal",
                    diagonal,
                    "units"
                )

        else:
            print("Invalid Choice!")


    # ========================================================
    # SQUARE
    # ========================================================

    elif shape == 2:

        print("\n--- SQUARE ---")

        side = float(
            input("Enter Side Length: ")
        )

        print("\n1. Area")
        print("2. Perimeter")
        print("3. Diagonal")

        choice = int(
            input("Choose: ")
        )

        area = square_number(side)

        perimeter = 4 * side

        diagonal = side * (2 ** 0.5)

        if choice == 1:

            show_result(
                "Area",
                area,
                "square units"
            )

        elif choice == 2:

            show_result(
                "Perimeter",
                perimeter,
                "units"
            )

        elif choice == 3:

            # Exact form
            exact = square_diagonal_exact(side)

            print("\nExact Form =", exact)

            # Decimal form
            print(
                "Decimal Form =",
                diagonal
            )

            print(
                "\nBoth forms:"
            )

            print(
                exact,
                "≈",
                diagonal
            )

        else:
            print("Invalid Choice!")


    # ========================================================
    # FOUR WALLS
    # ========================================================

    elif shape == 3:

        print("\n--- FOUR WALLS ---")

        length = float(
            input("Enter Length: ")
        )

        width = float(
            input("Enter Width: ")
        )

        height = float(
            input("Enter Height: ")
        )

        # Formula:
        # Area of 4 walls = 2(l+w)h

        area = 2 * (length + width) * height

        show_result(
            "Area of 4 Walls",
            area,
            "square units"
        )


    # ========================================================
    # CIRCLE
    # ========================================================

    elif shape == 4:

        print("\n--- CIRCLE ---")

        radius = float(
            input("Enter Radius: ")
        )

        pi = 22 / 7

        diameter = 2 * radius

        circumference = 2 * pi * radius

        area = pi * radius ** 2

        print("\n1. Diameter")
        print("2. Circumference")
        print("3. Area")

        choice = int(
            input("Choose: ")
        )

        if choice == 1:

            show_result(
                "Diameter",
                diameter,
                "units"
            )

        elif choice == 2:

            show_result(
                "Circumference",
                circumference,
                "units"
            )

        elif choice == 3:

            show_result(
                "Area",
                area,
                "square units"
            )

        else:
            print("Invalid Choice!")


    # ========================================================
    # TRIANGLE
    # ========================================================

    elif shape == 5:

        print("\n--- TRIANGLE ---")

        base = float(
            input("Enter Base: ")
        )

        height = float(
            input("Enter Height: ")
        )

        area = 0.5 * base * height

        show_result(
            "Area",
            area,
            "square units"
        )


    # ========================================================
    # PARALLELOGRAM
    # ========================================================

    elif shape == 6:

        print("\n--- PARALLELOGRAM ---")

        base = float(
            input("Enter Base: ")
        )

        height = float(
            input("Enter Height: ")
        )

        area = base * height

        show_result(
            "Area",
            area,
            "square units"
        )


    # ========================================================
    # RHOMBUS
    # ========================================================

    elif shape == 7:

        print("\n--- RHOMBUS ---")

        diagonal_1 = float(
            input("Enter First Diagonal: ")
        )

        diagonal_2 = float(
            input("Enter Second Diagonal: ")
        )

        area = (
            diagonal_1 *
            diagonal_2
        ) / 2

        show_result(
            "Area",
            area,
            "square units"
        )


    # ========================================================
    # TRAPEZIUM
    # ========================================================

    elif shape == 8:

        print("\n--- TRAPEZIUM ---")

        parallel_1 = float(
            input("Enter First Parallel Side: ")
        )

        parallel_2 = float(
            input("Enter Second Parallel Side: ")
        )

        height = float(
            input("Enter Height: ")
        )

        area = (
            (parallel_1 + parallel_2)
            * height
        ) / 2

        show_result(
            "Area",
            area,
            "square units"
        )


    # ========================================================
    # INVALID
    # ========================================================

    else:

        print("\nInvalid Shape!")

        # pass statement
        pass


    # ========================================================
    # CONTINUE DEMO
    # ========================================================

    print("\nCalculation completed.")

    again = input(
        "Do you want to calculate another shape? (yes/no): "
    )

    # String function
    again = again.lower()

    if again == "yes":
        continue

    elif again == "no":
        print("\nProgram Finished!")
        break

    else:
        print("Invalid answer.")

        # continue
        continue


# ============================================================
# FOR-ELSE EXAMPLE
# ============================================================

print("\n--- Session Summary ---")

for number in range(1, 4):

    print("Session check:", number)

    if number == 10:
        break

else:
    print("All session checks completed successfully.")


print("\nThank you for using", program_name)