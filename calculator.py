import math
from time import sleep

def areaoftriangle():
    base = int(input("Enter base length of the triangle: "))
    height = int(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    print("Area of triangle is", area, "metres squared")

def perimeteroftriangle():
    a= int(input("Enter side a:"))
    b= int(input("Enter side b:"))
    c= int(input("Enter side c:"))
    perimeter= a+ b + c
    print("Perimeter of triangle is", perimeter, "metres")

def areaofrectangle():
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    area = length * width
    print("Area of rectangle is", area, "metres squared")

def perimeterofrectangle():
    length = int(input("Enter length of the rectangle: "))
    width = int(input("Enter width of the rectangle: "))
    perimeter= 2 *(length + width)
    print("Perimeter of rectangle is", perimeter, "metres")

def areaofcircle():
    radius = int(input("Enter radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of circle is", area, "metres squared")

def circumferenceofcircle():
    radius = int(input("Enter radius of the circle: "))
    circumference =2 * math.pi * radius
    print("Circumference of circle is", circumference, "metres ")

def slope():
    x1 = int(input("Enter first x coordinate: "))
    y1 = int(input("Enter first y coordinate: "))
    x2 = int(input("Enter second x coordinate: "))
    y2 = int(input("Enter second y coordinate: "))
    m = (y2 - y1) / (x2 - x1)
    print("Slope of line is", m, "units")

def pointdistance():
    x1 = int(input("Enter first x coordinate: "))
    y1 = int(input("Enter first y coordinate: "))
    x2 = int(input("Enter second x coordinate: "))
    y2 = int(input("Enter second y coordinate: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Distance between", x1,",",y1, " and", x2,",",y2," is", distance, "units")


def main():
    print("1.Area of triangle")
    sleep(3)
    print("2.Perimeter of triangle")
    sleep(3)
    print("3.Area of rectangle")
    sleep(3)
    print("4.Perimeter of rectangle")
    sleep(3)
    print("5.Area of circle")
    sleep(3)
    print("6.Circumference of circle")
    sleep(3)
    print("7.Slope of two points")
    sleep(3)
    print("8.Euclidean distance")
    sleep(3)
    task0 = int(input("Enter task nnumber: "))
    if task0 == 1:
        areaoftriangle()
    elif task0 == 2:
        perimeteroftriangle()
    elif task0 == 3:
        areaofrectangle()
    elif task0 == 4:
       perimeterofrectangle()
    elif task0 == 5:
        areaofcircle()
    elif task0 == 6:
        circumferenceofcircle()
    elif task0 == 7:
        slope()
    elif task0 == 8:
        pointdistance()
    else:
        print("Invalid Input")
        sleep(3)
    repetea= input("Do you want to calculate again?(yes/no)")
    if repetea == "yes":
        main()
    elif repetea == "no":
        print("Goodbye")

print("WELCOME TO TEHILAS CALCULATOR")
sleep(3)

main()
