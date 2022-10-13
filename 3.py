num = int(input('你想输出多少行呢？'))
for i in range(1,num+1,2):
    print(' '*int(((num-i)/2)),'*'*i,' '*int(((num-i)/2)))

for i in range(num-2,0,-2):
    print(' ' * int(((num - i) / 2)), '*' * i, ' ' * int(((num - i) / 2)))