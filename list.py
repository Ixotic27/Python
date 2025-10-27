li = ["b", "a", "c", "f", "d", "e", "g"]

#Original lsit
print(f"Original List:{li}")

# Sort the list
li.sort()
print(f"Sorted list: {li}")

# Reverse the list
li.reverse()
print(f"Reversed list: {li}")

# Append an element to the list
li.append("h")  # Assuming "h" is the value to append
print(f"Appended list: {li}")

# Pop an element from the list
popped_element = li.pop(1)  # Pop the element at index 1
print(f"Popped list: {li}, Popped element: {popped_element}")

# Remove an element from the list
li.remove("h")  # Remove the first occurrence of "h"
print(f"Removed list: {li}")

# Insert an element into the list
li.insert(1, "Ishant")  # Insert "Ishant" at index 1
print(f"Added list: {li}")

tu=("a", "b", "c", "d", "e")
print(f"Original tuple: {tu}")
print(f"Count a: {tu.count("a")}")
print(f"Index of e: {tu.index("e")}")