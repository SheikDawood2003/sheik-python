#One way selection

order_price = int(input("Enter the Order price:"))
minimum_order_price = 1000
Delivery_charge = 100


if order_price > minimum_order_price:
    Delivery_charge = 0

Total_price = order_price + Delivery_charge
print(Total_price)

