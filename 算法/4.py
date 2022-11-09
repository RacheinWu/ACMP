num = int(input('请输入时间：'))

def switch(num,step):
    if num >= step:
        remainder = num % step
        quotient = (num - remainder) / step

        return  int(quotient),int(remainder)
    else:
        return 0, num

time = {
    'year': 0,
    'mouth': 0,
    'day': 0,
    'hour': 0,
    'min': 0,
    'sec': 0
}


m, n = switch(num, 60)  # 分
time['sec'] = n

m, n = switch(m, 60)  # 时
time['min'] = n

m, n = switch(m, 24)  # 天
time['hour'] = n

m, n = switch(m, 30)  # 月
time['day'] = n

m, n = switch(m, 12)  # 年
time['mouth'] = n

time['year'] = m

print('{0}年{1}月{2}天{3}小时{4}分钟{5}秒'.format(time['year'], time['mouth'], time['day'], time['hour'], time['min'], time['sec']))