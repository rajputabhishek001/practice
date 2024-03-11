def even_odd(a):
    if a & 1 == 0:return True
    else:return False
a = int(input("Enter the number: "))
if even_odd(a):print(f"{a} is a even Number")
else:print(f"{a} is a odd number")