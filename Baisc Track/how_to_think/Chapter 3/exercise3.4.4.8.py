a=float(input("Length of the first shorter side"))
b=float(input("Length of the second shorter side"))
y=float(input("Length of the longest side"))

x=(a**2+b**2)**0.5


threshold = 1e-7
if abs(x-y) < threshold:
    print("TRUE")
else:
    print("FALSE")

