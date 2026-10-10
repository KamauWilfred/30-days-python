def calculate_total(price, quantity):
    return price * quantity

print("================RECEIPT===========")
gross_total = 0
items = []
while True:
    item = input("Item (type done to finish): ").lower()

    if item == "done":
        break
    price = int(input("price: "))
    quantity = int(input("quantity: "))
    total = calculate_total(price, quantity)
    gross_total += total
    purchase = {
            "name": item,
            "price": price,
            "quantity": quantity,
            "total": total
        }

    items.append(purchase)

print("================================================================")
amount_paid = int(input("Amount_paid: "))
balance = amount_paid - gross_total
for purchase in items:
    print(f"Item_name: {purchase['name']} | price: {purchase['price']} | quantity: {purchase['quantity']} | total: {purchase['total']}")
print("-----------------------------------------------------------------") 
print("Gross_total: ", gross_total)
if balance == 0:
    print("No balance")
elif balance < 0:
    print("insufficient amount, add: ",gross_total - amount_paid)
else:
    print("Balance: ", balance)
print("====================================================================")
