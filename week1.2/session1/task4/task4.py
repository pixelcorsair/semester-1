# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both)

# tomato will be printed here as it is the only item in both sets 

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food)

# because the union of the two sets will contain all unique items from both sets, as tomato is present in both sets it will be counted as one 

# Add an item to fruit
fruit.add("pear")
print(fruit)

# Remove an item from vegetables
vegetables.remove("potato")
print(vegetables)

# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))
