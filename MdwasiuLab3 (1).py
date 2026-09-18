'''
File header
MdwasiuLab3.py
Program Purpose:Finding Perimeter of square,triangle,circle,polygons and rectangle
Program description: Finding Perimeter of a square,triangle,circle,polygons and rectangle
First Created:09/15/2026
Author:Arafat Mdwasiu
Version: 1.0
'''
'''
The following block contains the variables need to calculate the perimeter of a square,rectangle,triangle or polygon and the numbers will be inputed by users
'''
square_side = input("What is one side of the square?")
rectangle_length = input("What is the rectangle length?")
rectangle_width = input("What is the rectangles width?")
triangle_side_a = input("What is the first of the triangle?")
triangle_side_b = input("What is the second side of the triangle?")
triangle_side_c = input("What is the third side of the triangle?")
polygon_number_of_sides = input("How many sides does the polygon have??")
polygon_side_length = input("What is the length of one side of the polygon?")

def square(side):#this will find the perimeter of a square
    perimeter = 4 * float(side)
    return perimeter

def polygon(num_of_sides,side_length):#this will find the perimeter of a polygon
    perimeter = float(num_of_sides) * float(side_length)
    return perimeter

def triangle(a,b,c):#this will find the perimeter of a triangle
    perimeter = float(a) + float(b) + float(c)
    return perimeter

def rectangle(length,width):#this will find the perimeter of a rectangle
    perimeter = 2 * int((length + width))
    return perimeter


'''
The following cold block will print out the results of their designated function, effectively finding the perimeter of each shape based off user entry
'''
perimeter = square(square_side)
print("The perimeter of a square is:", perimeter)

perimeter = rectangle(rectangle_length,rectangle_width)
print("The perimeter of a rectangle is", perimeter)

perimeter = triangle(triangle_side_a,triangle_side_b,triangle_side_c)
print("The perimeter of a triangle is:", perimeter)

perimeter = polygon(polygon_number_of_sides,polygon_side_length)
print("The perimter of a polygon is:", perimeter)



