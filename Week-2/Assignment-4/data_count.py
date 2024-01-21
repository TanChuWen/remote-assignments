#  題目： 
# 1. count: return an object which shows the count of each character.
# 2. group_by_key: return an object which shows the summed up value of each key.
# Note:
# 1. The input format is different for these two functions.
# 2. In the second function, the input may have same key but different values, the output should have each key only once.

def count(input): # 資料輸入的格式是陣列，但最後印出來的格式會是一個字典
    data_output = {}  # 所以先創建一個空字典，用來存每個字的次數
    for item in input:
        if item in data_output: # in 的用法是看字典中的 key 有沒有在字典裡面
            data_output[item] += 1 # data_output[item] 是該item對應到的values
        else:
            data_output[item] = 1 # 如果就是只有出現一次，那就回傳一次
    return data_output

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    output_result = {}  
    for eachItem in input: # 取出來的東西都是一個字典
        key = eachItem['key'] # 我想要取 'key' 的 values 也就是 a
        value = eachItem['value'] # 我想要取 'value' 的 values 也就是 3
        if key in output_result: # 檢查字典 output_result 中是否已經存在這個鍵 key
            output_result[key] += value
        else:
            output_result[key] = value
    return output_result
    


input2 = [
        {'key': 'a', 'value': 3},
        {'key': 'b', 'value': 1},
        {'key': 'c', 'value': 2},
        {'key': 'a', 'value': 3},
        {'key': 'c', 'value': 5}
    ]


print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7