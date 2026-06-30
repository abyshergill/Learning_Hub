Welcome to **Chapter 1: The Starting Line**!

Every great Python developer started exactly where you are right now. In this chapter, we are going to set up your tools, write your first lines of code, and learn how Python stores data in its memory.

Grab your keyboard, and let's get started!

---

## 🏁 Chapter 1: The Starting Line

### 1. Introduction & Setup

To write Python, you need two things:

1. **The Python Interpreter:** The program that reads your code and executes it. (Download this from `python.org`).
2. **A Code Editor:** A workspace to write your code. CodeWithHarry highly recommends **Visual Studio Code (VS Code)**.

Once you have both installed, open VS Code, create a file named `main.py`, and type the following:

```python
print("Hello, World!")
print("Welcome to Day 1 of 100 Days of Code.")

```

* **What is `print()`?** It is a built-in function that displays whatever you put inside the parentheses onto your screen (the console).

### 2. Syntax Basics (Comments and Escape Sequences)

As you write more code, you will need to leave notes for yourself or other developers. You also need to format your text cleanly.

* **Comments:** Use the `#` symbol. Python completely ignores anything on a line after a `#`. It is just for human eyes.
* **Escape Sequences:** Sometimes you want to hit "Enter" and start a new line *inside* a string of text. You use `\n` (newline character) for this.

```python
# This is a comment. Python will ignore this line.
print("Hello!\nI am on a new line.")

# You can also use multiple items in a print statement
# 'sep' changes what separates the words (default is a space)
# 'end' changes what goes at the very end (default is a newline)
print("Harry", "Ron", "Hermione", sep=" ~ ", end="... END OF LIST\n")

```

### 3. Variables & Data Types

Think of a variable as a labeled box where you can store data. In Python, you do not need to announce what kind of data is going into the box; Python is smart enough to figure it out automatically.

Here are the core data types you will use every day:

* **`int` (Integer):** Whole numbers.
* **`float`:** Decimal numbers.
* **`str` (String):** Text, wrapped in quotes.
* **`bool` (Boolean):** True or False.

```python
a = 1          # int
b = True       # bool
c = "Harry"    # str
d = 5.5        # float

print("The value of a is:", a)

# The type() function tells you exactly what kind of data a variable is holding
print("The data type of a is:", type(a))
print("The data type of b is:", type(b))

```

### 4. Typecasting & User Input

What if you want to ask the user for their name or age? You use the `input()` function.

**Crucial Rule:** The `input()` function *always* captures data as a String (`str`). Even if the user types the number `5`, Python sees it as the text `"5"`.

To do math with user input, you must use **Typecasting** (converting data from one type to another) using functions like `int()` or `float()`.

```python
# Asking the user for their name
name = input("Enter your name: ")
print("Hello,", name)

# Asking for numbers (Notice the typecasting!)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# If we just add them normally, Python glues the TEXT together
print("Without typecasting:", num1 + num2) # If they typed 1 and 2, this outputs "12"

# We must cast the strings to integers to do actual math!
print("With typecasting:", int(num1) + int(num2)) # This outputs 3

```

---

You have officially written your first Python script, learned how to leave comments, stored data in variables, and built a mini-calculator using user input!

