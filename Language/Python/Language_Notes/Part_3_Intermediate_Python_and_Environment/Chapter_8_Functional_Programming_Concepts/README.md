Welcome to the final chapter of Part 3—**Chapter 8: Functional Programming Concepts**!

As you write more Python, you will find yourself writing simple loops over and over again just to modify lists of data. Functional programming provides powerful shortcuts to do these tasks in a single, clean line of code.

Let's learn how to write anonymous functions and manipulate lists like a pro.

---

## ⚙️ Chapter 8: Functional Programming Concepts

### 1. Lambda Functions (Anonymous Functions)

Sometimes you need to write a tiny function that only does one simple calculation, and creating a whole `def` block feels like overkill.

**Lambda functions** are short, one-line functions that don't even have a name (which is why they are called "anonymous"). You use the `lambda` keyword, followed by the inputs, a colon `:`, and the return expression.

```python
# The standard way using 'def'
def double_standard(x):
    return x * 2

# The Lambda way! (One line, no 'return' keyword needed)
double_lambda = lambda x: x * 2

# You can have multiple inputs too
add = lambda x, y: x + y

print("Double of 5 is:", double_lambda(5))
print("Sum of 3 and 4 is:", add(3, 4))

```

*(Note: Lambdas are usually used as quick "throwaway" functions that you pass into other, larger functions).*

### 2. Map, Filter, and Reduce

If you have a list of numbers and want to double all of them, the traditional way is to create an empty list, write a `for` loop, double the number, and append it. `map`, `filter`, and `reduce` do this work for you in a fraction of the time.

* **`map()`:** Applies a function to *every single item* in a list and returns a new list.
* **`filter()`:** Applies a function that returns True/False to a list, and only keeps the items that are `True`.
* **`reduce()`:** Rolls a list up into a *single value* (like summing all numbers together). You must import it from the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1. MAP: Double every number in the list
# We pass our lambda function and our list into map()
doubled = list(map(lambda x: x * 2, numbers))
print("Mapped (Doubled):", doubled)  # [2, 4, 6, 8, 10]

# 2. FILTER: Keep only the even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered (Evens):", evens)    # [2, 4]

# 3. REDUCE: Multiply all the numbers together (1*2*3*4*5)
product = reduce(lambda x, y: x * y, numbers)
print("Reduced (Product):", product) # 120

```

### 3. The `enumerate` Function

How many times have you written a `for` loop and had to create a separate `index = 0` variable just to keep track of which loop iteration you are on?

```python
# The old, messy way
fruits = ["apple", "banana", "mango"]
index = 0
for fruit in fruits:
    print(f"{index}: {fruit}")
    index += 1

```

The **`enumerate()`** function fixes this by automatically returning both the index *and* the value at the same time. It is incredibly clean and "Pythonic."

```python
# The clean, modern Enumerate way
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"Item {index} is {fruit}")

# You can even tell it to start counting from 1 instead of 0!
for index, fruit in enumerate(fruits, start=1):
    print(f"Shopping List #{index}: {fruit}")

```

---

You have officially completed **Part 3**! You now know how to manipulate files, manage your environment scope, and write clean, functional one-liners.
