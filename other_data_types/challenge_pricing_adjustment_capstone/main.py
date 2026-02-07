grocery_inventory = {
    "Milk":("Dairy",3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)
}
info_eggs = grocery_inventory["Eggs"]
print(info_eggs)

if (info_eggs[1] > 5):
   # print("Eggs are too expensive, reducing the price by $1")
    myList = list(info_eggs)
    myList[1] -= 1
    info_eggs = tuple(myList)
    grocery_inventory["Eggs"] = info_eggs
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)

info_milk = grocery_inventory["Milk"]

if (info_milk[2] < 10):
    print("Milk needs to be restocked. Increasing stock by 20 units.") 
    myList = list(info_milk)
    myList[2] += 20
    info_milk = tuple(myList)
    grocery_inventory["Milk"] = info_milk
   # print(grocery_inventory)
else:
    print("Milk has sufficient stock.")
if (grocery_inventory["Apples"][1] > 2):
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory", grocery_inventory)