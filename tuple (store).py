inventory=[
    ("Laptop",5,30000.00),
    ("Mouse",15,3000.00),
    ("Keyboard",5,6000.00),
    ("Pendrive",4,5000.00),
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value = quantity*unit_price
    print(f'Item Name:{item_name},the total value is:{stock_value}')
    if stock_value > highest_stock_value:
        highest_stock_value = stock_value
        item_with_highest_stock_value = item_name
print(f'Highest stock value is: {highest_stock_value}')
print(f'Item with highest stock value: {item_with_highest_stock_value}')