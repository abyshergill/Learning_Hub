# Tuple in python

A tuple in Python is a built-in collection data type used to store an ordered, immutable, and indexed sequence of objects. Unlike lists, which use square brackets [] and can be changed, tuples use parentheses () and cannot be altered after they are created.

## Core Characteristics
* Ordered: Items maintain a defined, unchanging sequence.
* Immutable: Elements cannot be added, removed, or modified once assigned.
* Heterogeneous: A single tuple can contain multiple data types simultaneously (e.g., strings, integers, lists).
* Indexed: Items are accessed via a zero-based index system.
* Allows Duplicates: Because items are accessed by position, identical values can coexist

## 1. Creating Tuples
You can define a tuple using traditional parentheses, structural constructors, or implicit comma separation.

```python
# Standard creation
coordinates = (40.7128, -74.0060)

# Without parentheses (Tuple Packing)
person = "Alice", 30, "Engineer"

# Single-element tuple (Crucial: requires a trailing comma)
single_item = ("Apple",) 
not_a_tuple = ("Apple")  # This resolves to a regular string

# Empty tuple
empty_tuple = ()

# Converting from another iterable
numbers_list = [1, 2, 3]
converted_tuple = tuple(numbers_list)
```

## 2. Accessing and Slicing Tuple Elements
Tuples share the same indexing rules as Python strings and lists.

```python
alphabets = ('a', 'b', 'c', 'd', 'e')

# Positive indexing (Starts at 0)
print(alphabets[0])   # Output: 'a'

# Negative indexing (Starts from the end)
print(alphabets[-1])  # Output: 'e'

# Slicing [start:stop:step] (Stop index is excluded)
print(alphabets[1:4]) # Output: ('b', 'c', 'd')
print(alphabets[::-1]) # Output: ('e', 'd', 'c', 'b', 'a') (Reversed)
```

## 3. Tuple Unpacking
Tuple unpacking allows you to assign elements of a tuple directly to individual variables.
```python
user = ("John", "Doe", 25)
first_name, last_name, age = user

# Using the asterisk (*) operator to collect remaining items
scores = (90, 85, 77, 92, 88)
highest, *middle_scores, lowest = scores
# highest = 90, middle_scores = [85, 77, 92], lowest = 88
```
## 4. Built-in Methods and Functions
Because tuples are immutable, they only feature two built-in methods. However, they work seamlessly with several global Python functions.
### Methods
- `count(value):` Returns the frequency of a specified 
- `item.index(value):` Returns the first index where the item appears

```python
data = (1, 2, 3, 2, 4)
print(data.count(2))  # Output: 2
print(data.index(3))  # Output: 2
```

### Global Functions
* len(tuple): Returns the total item count.
* max(tuple) / min(tuple): Returns the maximum or minimum value.
* sum(tuple): Calculates the mathematical total of numerical elements.

## 5. Important Nuance: 
Mutability Within ImmutabilityWhile the tuple itself cannot be resized or reassigned, if it contains a mutable object (like a list), that nested object can still be modified in place
```python

nested_tuple = (1, 2, [3, 4])
# nested_tuple[0] = 5 <-- Raises a TypeError

# Modifying the list inside the tuple is completely valid
nested_tuple[2].append(5)
print(nested_tuple)  # Output: (1, 2, [3, 4, 5])

```
