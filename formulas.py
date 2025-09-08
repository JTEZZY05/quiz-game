def cal_square(side):
    print(side*side)

def cal_rectangle(length,width):
    print(length*width)
    
def cal_triangle(base,height):
    print((base*height)/2)

def cal_circle(radius):
    print(3.14*(radius**2))

keep_going = True
while keep_going == True:
    area_calculate = input("What area would you like to find? ")
    if area_calculate == "square":
        side = int(input("What is the side of your square "))
        cal_square(side)

    elif area_calculate == "rectangle":
        length = int(input("What is the length of your rectangle? "))
        width = int(input("What is the width of your rectangle? "))
        cal_rectangle(length,width)

    elif area_calculate == "triangle":
        base = int(input("What is the base of your triangle? "))
        height = int(input("What is the height of your triangle? "))
        cal_triangle(base,height)

    elif area_calculate == "circle":
        radius = int(input("What is the radius of your circle? "))
        cal_circle(radius)

    else:
        print("Please enter a valid input ")
    
    find_area = input("Would you like to find another area? ")
    if find_area == "yes":
        keep_going = True
    else:
        keep_going = False
        print("Goodbye, hope I helped! :)")
    