# caption
project
#write a Python program which accepts the radius of a circle from the user and computes area.
r = float(input("Enter radius of circle: "))
a = 3.14159 * r * r
print("Area of circle =", a)







#your second task now is to write a Python program to accept a filename from the user and print the extension of that.
fun= input("Enter Filename: ")
f = fun.split(".")
print ("Extension of the file is : " + f[-1])
