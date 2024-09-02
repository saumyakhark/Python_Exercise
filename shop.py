item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity

print(f"The total price for {item} with price/piece ${price} for {quantity} is ${total}")