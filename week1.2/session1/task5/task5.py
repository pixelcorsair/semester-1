# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database

rivers["Patna"] = "Ganaga"
rivers["Delhi"] = "Yamuna"


# Display all the keys

keys = rivers.keys()
print(keys)
# Display all the values

values = rivers.values()
print(values)


# Display all the key:value pairs, as tuples

pairs = rivers.items()
print(pairs)

# Delete an entry from the rivers database

rivers.pop("Leeds")
print(rivers)