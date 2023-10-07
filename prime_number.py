a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

for k in range(2,a):
    if a % k == 0:
        print(f'{a}は{k}を約数にもつから、素数でない')
        break
else:
        print(f'{a}は素数')

for k in range(2,b):
    if b % k == 0:
        print(f'{b}は{k}を約数にもつから、素数でない')
        break
else:
        print(f'{b}は素数！')