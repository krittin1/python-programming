 # Is x an Integer



import math

x = float(input())

check = x%1

if check > 0 :

    print("%.1f is not an integer."%x)

else :

    print("%.f is an integer."%x)