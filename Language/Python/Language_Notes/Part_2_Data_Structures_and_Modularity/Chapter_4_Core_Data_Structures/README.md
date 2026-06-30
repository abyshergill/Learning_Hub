Welcome to **Chapter 4: Core Data Structures**!

So far, every variable we have created only holds a single piece of data (like `age = 25`). But what if you are building an app for a school and need to store the names of 500 students? You can't create 500 separate variables!

In this chapter, we will learn how to group large amounts of data together using Python's four built-in data structures: **Lists, Tuples, Dictionaries, and Sets**.

---

## 📚 Chapter 4: Core Data Structures

### 1. Lists (The Flexible Array)

A List is an ordered collection of data. It is **mutable**, which is a fancy programming word meaning *it can be changed* after it is created. You can add items, remove items, and sort them.

Lists are created using square brackets `[]`.

```python
# Creating a list (it can hold mixed data types!)
student_data = ["Harry", 25, True, 95.5]

# Accessing items using their index (remember, counting starts at 0)
print(student_data[0])  # Prints "Harry"

# Modifying an item
student_data[1] = 26    # Changes 25 to 26

# List Methods (Adding and Removing)
fruits = ["apple", "banana"]
fruits.append("orange")    # Adds "orange" to the end of the list
fruits.remove("apple")     # Removes "apple" from the list
fruits.insert(1, "grape")  # Inserts "grape" at index 1

print(fruits) # Output: ['banana', 'grape', 'orange']

```

### 2. Tuples (The Locked List)

A Tuple is almost exactly like a list, but it is **immutable** (it *cannot* be changed). Once you create a tuple, you cannot add, remove, or modify its contents.

Why use a tuple instead of a list? Because they are locked, they take up less memory and are processed slightly faster by the computer. They are perfect for data that should never change, like days of the week or GPS coordinates.

Tuples are created using parentheses `()`.

```python
# Creating a tuple
coordinates = (10.5, 20.0)

# You can access them just like lists
print("X coordinate:", coordinates[0])

# THIS WILL CAUSE AN ERROR! You cannot change a tuple.
# coordinates[0] = 15.0  <-- Python will crash if you do this!

```

### 3. Dictionaries (Key-Value Pairs)

If you want to find a word in a real dictionary, you don't look for "Word number 45"—you look up the *word* to get the *definition*.

Python Dictionaries work the exact same way. Instead of using numbered indexes (0, 1, 2), you use **Keys** to look up **Values**. This is the most important data structure for web development, as it directly mirrors how data is sent across the internet (JSON).

Dictionaries use curly braces `{}` and a colon `:` to separate the key from the value.

```python
# Creating a dictionary
user = {
    "username": "Aby Shergill",
    "email": "harry@example.com",
    "subscribers": 5000000
}

# Accessing data using the Key
print(user["username"])  # Prints "Aby Shergill"

# Adding a new key-value pair
user["language"] = "Python"

# Updating an existing value
user["subscribers"] = 5000001

print(user)

```

### 4. Sets (The Unique Collection)

A Set is a collection of items that is **unordered** and **unindexed**. Its superpower is that **it cannot contain duplicate values**.

If you have a massive list of email addresses and want to instantly remove all the duplicates, you just convert it into a Set!

Sets also use curly braces `{}`, but they don't have colons (no key-value pairs).

```python
# Creating a set
unique_numbers = {1, 2, 3, 3, 3, 4, 5, 5}

# Python automatically removes the duplicates!
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Adding and removing items
unique_numbers.add(6)
unique_numbers.remove(1)

# Because they are unordered, you CANNOT use indexes!
# print(unique_numbers[0]) <-- THIS WILL CAUSE AN ERROR

```

---

You now possess the tools to store and manipulate massive amounts of information efficiently!
