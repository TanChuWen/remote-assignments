def find_max(numbers):
    if not numbers:
        return None  # Handle empty array
    
    max_value = numbers[0] #假設最大值是 numbers[0]
    for num in numbers[1:]: #拿第二個數字和後面的數字，一起跟第一個數字比較起來
        if num > max_value: #如果該數字比 max_value 大，那它就變成最大值
            max_value = num

    return max_value  #最後找到最大值

def find_position(numbers, target): #這裡會想到用 enumerate()是因為他本身可以帶出某item在陣列中的位子，如果沒有特別設定，起始值從 0 開始
    for i, num in enumerate(numbers): #enumerate()會傳回一對數字，前面是序號，後面是 item
        if num == target:
            return i
    return -1

#另外一種用 for 的寫法
def find_position(numbers, target):
    idx = 0
    for each in numbers:
        if target == each:
            return idx
    return -1