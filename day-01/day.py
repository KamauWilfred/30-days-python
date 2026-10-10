print("======RECEIPT======")
Item_name = input("Item")
Item_price = float(input("Price"))
Item_quantity = int(input("Quantity"))
Total = Item_price*Item_quantity
print("Total:", Total)
Amount_payed = float(input("Amount"))
Balance = Amount_payed-Total
if(Balance==0):
    print("No balance")
elif(Balance<0):
    print("Insufficient Funds")
else:
    print("Balance is:", Balance)
print("=====================")
