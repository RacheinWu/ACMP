num = str(input('请输入一个五位数：'))

for i in range(5):
    print("第" + str(i+1) +"个数字是："+ num[i:i+1])