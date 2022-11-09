str_input = input("")
str_set = set()


def func(cur_str, surplus):
    str_set.add(cur_str)
    for j in range(len(surplus)):
        cur_str += surplus[j]
        str_set.add(cur_str)


for i in range(len(str_input)):
    func(str_input[i], surplus=str_input[i+1:]+str_input[:i])

print(len(str_set))