a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
# TODO

if a>=b:
    while b!=0:
        a,b = b,a%b
    print(f"最大公約数は{a}です")
else:
    while a!=0:
        b,a = a,b%a
    print(f"最大公約数は{b}です")