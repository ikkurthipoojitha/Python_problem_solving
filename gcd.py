a = float(input(" Enter the First Value a: "))
b = float(input(" Enter the Second Value b: "))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i = i + 1
print("gcd of",a,"and",b,":",gcd)
