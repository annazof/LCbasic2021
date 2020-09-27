a=float(input("Length of the first side"))
b=float(input("Length of the second side"))
y=float(input("Length of the third side"))

x=(a**2+b**2)**0.5
z=(y**2+b**2)**0.5
l=(y**2+a**2)**0.5

threshold = 1e-7
if abs(x-y) < threshold or abs(z-a) < threshold or abs(l-b) < threshold:
    print("TRUE")
else:
    print("FALSE")

