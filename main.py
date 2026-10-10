def calculte_change(paid,price):
    change = paid - price
    return change

snack_price=25
print("---SNACK VENDING MACHINE---")
print(f"this snack cost{snack_price}units")
print("accepted coins are 1,5,10,20\n")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input("insert a coin(1,5,10 OR 20): "))
    list=[1,5,10,20]
    if coin not in (list):
        print("invalid coin,try again")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"inserted: {coin}:{total_inserted}\n")
    if total_inserted >= snack_price:
        print("enough money inserted\n")
        break
change_due=calculte_change(total_inserted,snack_price)
print("dispensing snack...")
if change_due==0:
    pass
else:
    print(f"here is your change:{change_due}")