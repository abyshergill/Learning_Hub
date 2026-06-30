Welcome to the most important section of the entire journey: **Part 4: Object-Oriented Programming (OOP)**.

Up to this point, you have been writing "procedural" code—a top-to-bottom list of instructions. But what if you are building a video game with 50 different enemies on screen? Trying to manage 50 sets of variables for health, speed, and attacks using just lists and basic functions would be a nightmare.

OOP solves this by allowing you to bundle data (variables) and behavior (functions) together into a single, organized unit called an **Object**. Let's dive into **Chapter 9: OOP Basics**.

---

## 🏗️ Chapter 9: OOP Basics

### 1. Classes and Objects (The Blueprint and the House)

The core of OOP revolves around two concepts: Classes and Objects.

* **Class:** The blueprint. It defines what properties and actions something *should* have. (e.g., A blueprint for a "Car" says it should have wheels, a color, and a drive function).
* **Object:** The actual, physical thing built from the blueprint. (e.g., Your specific red Honda Civic).

We use the `class` keyword to define a blueprint.

```python
# 1. Defining the Blueprint (Class names usually start with a capital letter)
class Employee:
    company = "TechCorp" # This is a "Class attribute" shared by all employees
    
    def display_info(self):
        # We will explain 'self' in the next section!
        print("This is an employee.")

# 2. Creating an Object (Instantiating the class)
emp1 = Employee()
emp2 = Employee()

# We can access properties and run functions using dot notation (.)
print(emp1.company)
emp1.display_info()

```

### 2. Constructors and `self` (The `__init__` Method)

If you create two employees using the code above, they are identical. In the real world, employees have unique names and salaries.

To give an object its unique data the exact moment it is created, we use a **Constructor**. In Python, this is a special "magic" method named `__init__`. It runs automatically whenever you create a new object.

**What is `self`?** Whenever an object runs a function inside a class, Python secretly passes the object *itself* into the function as the first argument. We call this `self`. It allows the object to access its own specific data.

```python
class Employee:
    # The constructor: Runs automatically when a new Employee is created
    def __init__(self, name, salary):
        # We attach the passed-in data to the specific object using 'self'
        self.name = name
        self.salary = salary

    def get_details(self):
        # Now the object can remember its own name and salary!
        print(f"Employee {self.name} makes ${self.salary} a year.")

# We pass the unique data directly into the parentheses when creating the object
emp1 = Employee("Harry", 85000)
emp2 = Employee("Alice", 92000)

# Each object remembers its own state!
emp1.get_details() # Outputs: Employee Harry makes $85000 a year.
emp2.get_details() # Outputs: Employee Alice makes $92000 a year.

```

### 3. Decorators (Modifying Behavior Dynamically)

A **Decorator** is an advanced Python feature that allows you to take an existing function, wrap it inside another function, and modify how it behaves *without actually changing its code*.

You use the `@` symbol to apply a decorator. They are heavily used in web frameworks like Flask and Django (which you saw in the web development course!).

Here is how you build a simple decorator that logs when a function is running:

```python
# 1. Create the decorator function
def logger_decorator(func):
    def wrapper():
        print("--- STARTING FUNCTION ---")
        func() # Run the original function
        print("--- FUNCTION FINISHED ---")
    return wrapper

# 2. Apply it using the @ symbol
@logger_decorator
def say_hello():
    print("Hello, world!")

# When we call say_hello, it will automatically run the wrapper code around it!
say_hello()

```

**Output:**

```text
--- STARTING FUNCTION ---
Hello, world!
--- FUNCTION FINISHED ---

```

CodeWithHarry also introduces built-in decorators like `@property`, which allows you to access a method exactly like an attribute (without using parentheses), making your code much cleaner when getting or setting hidden data.