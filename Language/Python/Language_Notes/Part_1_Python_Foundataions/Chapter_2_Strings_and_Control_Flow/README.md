Welcome to **Chapter 2: Strings & Control Flow**!

Right now, your Python scripts run straight from top to bottom. In this chapter, we are going to give your code a "brain." We will teach it how to read text carefully, make decisions based on different situations, and automatically repeat tedious tasks.

---

## 🔀 Chapter 2: Strings & Control Flow

### 1. String Slicing and Methods

In Python, a string is basically an array (or a train) of characters. Because of this, you can grab specific letters out of a string using **Indexing**.

*Note: In programming, counting almost always starts at `0`, not `1`!*

```python
name = "Kuldeep"

# Indexing: Grabbing a single character
print(name[0])  # Prints 'K'
print(name[1])  # Prints 'u'

# Slicing: Grabbing a chunk [start:stop]
# It grabs from the start index up to, but NOT including, the stop index.
print(name[0:4]) # Prints "kuld"

# String Methods: Built-in tools to modify strings
sentence = "Python is AWESOME"
print(sentence.lower())           # "python is awesome"
print(sentence.upper())           # "PYTHON IS AWESOME"
print(sentence.replace("is", "was")) # "Python was AWESOME"

```

### 2. Conditional Statements (`if`, `elif`, `else`)

How does a website know whether to let you log in or show you an "Invalid Password" error? It uses conditional logic.

In Python, we use `if`, `elif` (else if), and `else`.
**Crucial Rule:** Python uses **indentation** (spaces/tabs) to know which code belongs inside the `if` block. If you forget to indent, Python will crash!

```python
age = int(input("Enter your age: "))

if age >= 18:
    # Notice the 4 spaces before the print statement!
    print("You are legally an adult.")
    print("You can vote.")
elif age == 17:
    print("You are almost an adult!")
else:
    print("You are a minor.")

```

### 3. Match Case (The Modern `switch`)

If you have a menu with 5 different options, writing 5 `elif` statements gets messy. In Python 3.10, they introduced **Match Case**. It checks a variable against multiple "cases" and runs the one that matches.

```python
command = input("Enter a command (start, stop, pause): ")

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Shutting down...")
    case "pause":
        print("System paused.")
    case _: 
        # The underscore _ means "default" (if nothing else matched)
        print("Unknown command!")

```

### 4. Loops (`for` and `while`)

Computers are amazing at doing boring, repetitive tasks instantly. We use loops to tell the computer to repeat a block of code.

**The `for` Loop:**
Use this when you know exactly how many times you want to repeat something, or when you are going through a sequence (like a string or a list). We often use the `range()` function to generate numbers.

```python
# range(5) generates numbers from 0 up to 4
for i in range(5):
    print("Iteration number:", i)

# Looping through a string letter by letter
for letter in "Code":
    print(letter)

```

**The `while` Loop:**
Use this when you want to repeat code *as long as a specific condition is True*. If the condition never becomes False, you will create an "infinite loop" and crash your program!

```python
count = 5

while count > 0:
    print("Countdown:", count)
    count = count - 1  # We must decrease count, or it loops forever!

print("Blastoff!")

```

### 5. Loop Controls (`break` and `continue`)

Sometimes you need to interrupt a loop while it's running.

* **`break`**: Instantly kills the loop and escapes it entirely.
* **`continue`**: Skips the rest of the *current* cycle and instantly jumps to the next cycle.

```python
for i in range(1, 10):
    if i == 3:
        print("Skipping 3!")
        continue  # Skips printing 3 and jumps right to 4
    
    if i == 7:
        print("Stopping at 7!")
        break     # Kills the entire loop, won't print 7, 8, or 9
        
    print("Number:", i)

```

---

You have officially given your code a brain! You can now slice up text, make dynamic decisions, and automate repetitive tasks using loops. This concludes Part 1 of the course.
