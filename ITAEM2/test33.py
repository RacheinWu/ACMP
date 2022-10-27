s = input('?')
s = int(s)
if s < 10000 or s > 99999:
    print("error")
else:a:int=int(s/10000)
b:int=int(s/1000%10)

print(b)