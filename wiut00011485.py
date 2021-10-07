number = input("enter your number: ")

a = int(number)

binary = bin(a)
binaryOct = oct(a)
binaryHEX = hex(a)

print("your number" ,a, "in binary is ",binary)
print("your number" ,a, "in Octal  is ",binaryOct)
print("your number" ,a, "in Hex  is ",binaryHEX)
