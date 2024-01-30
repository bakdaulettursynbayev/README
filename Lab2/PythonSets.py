#ex1 Check if "apple" is present in the fruits set
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex2 Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#ex3 Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#ex4 Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#ex5 Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
