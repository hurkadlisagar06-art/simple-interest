
p=int(input("Enter the principal amount:"))
t=int(input("Enter the time taken:"))
r=int(input("Enter rate of interest:"))
n = int(input("Enter the number of times interest is compounded per year: "))

si=(p*t*r)/100

print("Simple interest is:",si)


amount = p * (1 + r / (100 * n)) ** (n * t)
compound_interest = amount - p
