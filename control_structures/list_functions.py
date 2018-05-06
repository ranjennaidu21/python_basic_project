fruits = ["Mango", "Banana", "Orange"]
print(fruits)

#insert element into list (at the end of list automatically)
fruits.append("Apple")
print(fruits)

#insert element into list in a particular position
fruits.insert(2,"PineApple")
print(fruits)

#find the length of the list
print(len(fruits))

#find index/position of particular element in the list
#if not found will give error not in list
print(fruits.index("PineApple"))