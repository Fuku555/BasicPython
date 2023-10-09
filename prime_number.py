def prime_number(n):
        for k in range(2,n):
                if n % k == 0:
                        return False
                        break
        else:
                return True

n=int(input("nの値を入力:"))
result=prime_number(n)
print(result)


# a = int(input("aの値を入力: "))
# b = int(input("bの値を入力: "))

# for k in range(2,a):
#     if a % k == 0:
#         print(f'{a}は{k}を約数にもつから、素数でない')
#         break
# else:
#         print(f'{a}は素数')

# for k in range(2,b):
#     if b % k == 0:
#         print(f'{b}は{k}を約数にもつから、素数でない')
#         break
# else:
#         print(f'{b}は素数！')