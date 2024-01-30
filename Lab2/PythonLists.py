#ex1 Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#ex2 Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0]="Kiwi"

#ex3 Use the append method to add "orange" to the fruits list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#ex4 Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"orange")
#ex5 Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#ex6 Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#ex7 Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#ex8 Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))