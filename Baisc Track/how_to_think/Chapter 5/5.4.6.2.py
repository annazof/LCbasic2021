#Give the Python interpreter’s response to each of the following from a continuous interpreter session:

dictionary = {"apples": 15, "bananas": 35, "grapes": 12}
dictionary["bananas"]
#35

dictionary["oranges"] = 20
len(dictionary)
#4

"grapes" in dictionary
#TRUE

#dictionary["pears"]
#KeyError: 'pears', no pears item
dictionary.get("pears", 0)
#0

fruits = list(dictionary.keys())
fruits.sort()
print(fruits)
#['apples', 'bananas', 'grapes', 'oranges']

del dictionary["apples"]
"apples" in dictionary
#FALSE

def add_fruit(inventory, fruit, quantity=0):
    inventory={}
    inventory[fruit] = quantity
    return None

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)
