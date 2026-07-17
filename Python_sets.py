# Difference Between Sets and Dictionaries in Python
# Set	                         Dictionary
# Stores only unique values.	Stores key-value pairs.
# Uses curly braces {}.	        Also uses curly braces {}.
# Elements have no keys.	    Every value has a key.
# Duplicate values are not allowed.	Duplicate keys are not allowed, but values can be duplicated.
# Elements are unordered.	         Stores data as key : value pairs.
# Used for unique collections and set operations.	 Used for storing and retrieving data using keys.
# ==========================================
# Task: Favorite Fruits Using Sets
# ==========================================

# Create two sets
my_fruits = {"Apple", "Banana", "Mango", "Orange"}
friend_fruits = {"Mango", "Orange", "Grapes", "Pineapple"}

# Print both sets
print("My Fruits:", my_fruits)
print("Friend's Fruits:", friend_fruits)

# -------------------------------
# 1. Union (|)
# Combines all unique elements
# -------------------------------
all_fruits = my_fruits | friend_fruits
print("\nUnion:", all_fruits)

# -------------------------------
# 2. Intersection (&)
# Finds common elements
# -------------------------------
common_fruits = my_fruits & friend_fruits
print("Intersection:", common_fruits)

# -------------------------------
# 3. Difference (-)
# Finds elements only in my_fruits
# -------------------------------
my_only_fruits = my_fruits - friend_fruits
print("Difference:", my_only_fruits)