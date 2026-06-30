Welcome to **Part 2, Chapter 3: Functions & Operations**!

Up to this point, if you wanted to run the same block of code five times in different parts of your script, you had to copy and paste it five times. This violates a core rule of programming: **DRY (Don't Repeat Yourself)**.

In this chapter, we will learn how to package our code into reusable blocks, document them professionally, and format our text like modern Python developers.

---

## 🛠️ Chapter 3: Functions & Operations

### 1. Functions (The Building Blocks of Software)

A function is a named block of code that performs a specific task. You define it once, and then you can "call" it as many times as you want.

We use the `def` keyword to define a function. Functions can take **inputs** (called arguments/parameters) and give back an **output** (using the `return` keyword).

```python
# 1. A simple function with no inputs
def say_hello():
    print("Hello, welcome to the system!")

# Calling (running) the function
say_hello() 
say_hello() # We just ran it twice without rewriting the print statement!


# 2. A function with inputs (parameters) and an output (return)
def add_numbers(num1, num2):
    total = num1 + num2
    return total  # 'return' hands the data back to whoever called it

# We catch the returned data in a new variable
result = add_numbers(10, 15)
print("The sum is:", result)

```

### 2. Docstrings & PEP-8 (Writing Professional Code)

When you write a function, other developers (or you, six months later) need to know what it does without reading every line of code.

While `# comments` are ignored by Python, **Docstrings** are special strings written right under the function definition using triple quotes `"""`. Python actually saves them, and they show up when you hover over the function in your code editor!

```python
def calculate_area(length, width):
    """
    Takes the length and width of a rectangle.
    Returns the total calculated area.
    """
    return length * width

# You can even print the docstring using a special 'dunder' (double underscore) method:
print(calculate_area.__doc__)

```

*Note: CodeWithHarry heavily emphasizes **PEP-8** in this section. PEP-8 is the official style guide for Python. It dictates rules like: always use 4 spaces for indentation, keep lines under 79 characters, and use lowercase letters with underscores for function names (e.g., `calculate_area`, not `CalculateArea`).*

### 3. F-Strings (The Modern Way to Format Text)

In Chapter 1, we learned to combine text and variables using commas or the `+` sign. That gets incredibly messy when you have a lot of variables.

In Python 3.6, **f-strings** (formatted strings) were introduced, and they changed everything. By simply putting an `f` right before the quotes, you can inject variables directly into your text using curly braces `{}`.

```python
name = "Harry"
age = 25
profession = "Programmer"

# The old, messy way (concatenation)
print("My name is " + name + ", I am " + str(age) + " years old, and I am a " + profession + ".")

# The new, modern f-string way!
print(f"My name is {name}, I am {age} years old, and I am a {profession}.")

# You can even do math inside f-strings!
price = 50
print(f"The total with tax is ${price * 1.05}")

```

---

You have just leveled up your code organization. Functions allow you to break massive, complex problems down into small, manageable, and reusable pieces.
