#Read two Numbers and print their sum, difference, product, quotient, and remainder 
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print(f"sum: {num1+num2}")
print(f"difference: {num1-num2}")
print(f"product: {num1*num2}")

if num2!=0:
    print(f"quotient: {num1/num2}")
    print(f"remainder: {num1%num2}")

else:
    print("Quotient: Cannot be divided by 0")
    print("Remainder: Cannot be divided by 0")