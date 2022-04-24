def square():
    side=float(input())
    area=round(side*side,2)
    print("Measurement of the side is (☞ﾟヮﾟ)☞:",side)
    print ("Area of square 🟥🟦🟧 :",area)
def rectangle():
    length=float(input())
    breadth=float(input())
    area=round(length*breadth,2)
    print ("Measurement of the length is (☞ﾟヮﾟ)☞:",length )
    print ("Measurement of the breadth is (☞ﾟヮﾟ)☞:",breadth )
    print ("Area of reactangle 🟥🟦🟧:",area)
def triangle():
    height=float(input())
    base=float(input())
    area=round(0.5*height*base,2)
    print ("Measurement of the height is (☞ﾟヮﾟ)☞: ",height)
    print ("Measurement of the base is (☞ﾟヮﾟ)☞:",base)
    print ("Area of triangle 🔺🔺🔺:",area)
def circle():
    radius=float(input())
    area=round(3.14*radius*radius,2)
    print ("Measurement of radius is (☞ﾟヮﾟ)☞:",radius )
    print ("Area of circle 🟠🟡🟢 :",area)

Choice=str(input())
print ("U want to find the area of:",Choice  )
if Choice =="square":
    square()
elif Choice =="rectangle":
    rectangle ()
elif Choice =="triangle":
    triangle ()
else:
    circle ()