def euclid(a,b):
    if a>=b:
        while b!=0:
            a,b = b,a%b
        return a
    else:
        while a!=0:
            b,a = a,b%a
        return b

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

gcd=euclid(a,b)
print(gcd)

#ここから問４
def coprime(gcd):
    if gcd==1:
        return True
    else:
        return False

result=coprime(gcd)
print(result)

