def areaOfCircle(d) :
    r = d/2
    area = 3.14*r*r
    return area

daimeter = int(input("Enter Daimeter of Circle to calculate Area: "))
print("Area of this Circle is : ", areaOfCircle(daimeter))