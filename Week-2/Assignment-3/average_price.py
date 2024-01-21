# Complete the function below by Python which can calculate the average price of all the products.
# print the average price of all products (round to 3 decimal)

# {"products": [
#     {"name": "Product 1", "price": 100},
#     {"name": "Product 2", "price": 700},
#     {"name": "Product 3", "price": 300}
# ]}
# 思路：先拆解一下題目給的資料，這是一個字典裡面包字典（也就是有key, value 對應）的結構。第一層的字典是 "products" 對應到一個陣列，這個陣列包含三個字典元素。
# 第二層字典是每個字典元素都有兩個 key-value pair，"name" 對應到商品名稱的字串，"price" 對應到商品價格的數字。
# 要計算所有商品價格的平均值，我需要先取得所有商品的價格總和，然後除以商品總數。


def avg(data):
    products = data["products"]    #從字典 data 中取出鍵為 "products" 的值，以 "products" 是 key，取得字典 data 中對應的值
    total_price = 0

    # 遍歷每個商品，取得價格
    for product in products:
        total_price += product["price"]  #從名為 product 的字典中取得鍵為 "price" 的值
        # print(product["price"])

    # 計算平均價格
    average_price = total_price / len(products)
    # print(len(products))

    # 四捨五入到三位小數
    rounded_average = round(average_price, 3)

    return rounded_average


print(avg({"products": [{ "name": "Product 1","price": 100},{"name": "Product 2","price": 700},{"name": "Product 3","price": 300}]}))






    