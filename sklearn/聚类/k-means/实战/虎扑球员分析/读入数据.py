import pandas as pd
# 读取网页中的数据表
table = []
for i in range(1,7):
    table.append(pd.read_html('https://nba.hupu.com/stats/players/pts/%d' %i)[0])

# 所有数据纵向合并为数据框
players = pd.concat(table)
# 删除行标签为0的记录
players.drop(0,inplace=True)

# 变量重命名
columns=['排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率','命中-罚球','罚球命中率','场次','上场时间']
players.columns=columns

# 数据类型转换
players.得分 = players.得分.astype('float')
players.命中率 = players.命中率.str[:-1].astype('float')/100
players.三分命中率 = players.三分命中率.str[:-1].astype('float')/100
players.罚球命中率 = players.罚球命中率.str[:-1].astype('float')/100
players.场次 = players.场次.astype('int')
players.上场时间 = players.上场时间.astype('float')


players.head()

# 读入excel中
players.to_excel("data/data.xls")