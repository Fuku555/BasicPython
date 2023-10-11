def prime_number(n):
        for k in range(2,n):
                if n % k == 0:
                        return False
                        break
        else:
                return True

n = float(input("nの値を入力: "))
if not n.is_integer() or n<=0:
        print("error")
else:
        result=prime_number(int(n))
        print(result)
