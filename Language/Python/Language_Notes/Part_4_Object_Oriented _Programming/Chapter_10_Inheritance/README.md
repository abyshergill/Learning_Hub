Welcome to **Chapter 10: Inheritance**!

In the last chapter, you learned how to create a class from scratch. But what if you want to build a new class that is almost exactly like an existing one, just with a few extra features?

Instead of copying and pasting the entire original class, OOP allows you to use **Inheritance**. You can create a "Child" class that automatically inherits all the variables and methods of a "Parent" class.

---

## 🧬 Chapter 10: Inheritance

### 1. Basic Inheritance (Parent and Child)

Let's say you have a basic `Animal` class. You want to create a `Dog` class. Since a dog *is* an animal, it should automatically be able to do everything a standard animal can do (like eat and sleep).

To inherit from a class, you simply put the parent class's name inside parentheses when defining the child class.

```python
# The Parent Class
class Animal:
    def eat(self):
        print("This animal is eating.")
        
    def sleep(self):
        print("This animal is sleeping.")

# The Child Class (Inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Let's test it out
my_dog = Dog()

# The dog can use its own methods...
my_dog.bark()

# ...AND it automatically has access to the parent's methods!
my_dog.eat()

```

### 2. Types of Inheritance

Python is extremely flexible and allows for several different architectural designs when inheriting classes.

* **Single Inheritance:** One child inherits from one parent (like the `Animal` -> `Dog` example above).
* **Multiple Inheritance:** One child inherits from *two or more* parents. (e.g., A `FlyingCar` class inherits from both a `Car` class and an `Airplane` class).
* **Multilevel Inheritance:** A child inherits from a parent, and then a *grandchild* inherits from that child. (e.g., `Animal` -> `Dog` -> `GoldenRetriever`).

**Example of Multiple Inheritance:**

```python
class Employee:
    def work(self):
        print("Working on tasks.")

class Gamer:
    def play(self):
        print("Playing video games.")

# This class inherits from BOTH!
class Programmer(Employee, Gamer):
    pass # 'pass' means we don't want to add any new code right now

harry = Programmer()
harry.work() # Inherited from Employee
harry.play() # Inherited from Gamer

```

### 3. Access Modifiers (Public, Protected, and Private)

When you inherit classes or build complex systems, you sometimes want to hide sensitive data (like a bank account balance) so it cannot be accidentally changed from outside the class.

Unlike Java or C++, Python doesn't have strict security blocks, but it uses **naming conventions** to tell other developers how a variable should be treated.

* **Public:** By default, all variables and methods in Python are public. Anyone can read or change them.
* **Protected (`_name`):** If you put a *single underscore* before a variable, it is a gentleman's agreement meaning: "Please only use this variable inside this class or its children."
* **Private (`__name`):** If you put a *double underscore* before a variable, Python performs "Name Mangling." It actively changes the variable's name behind the scenes to make it very difficult (though not impossible) to access from outside the class.

```python
class BankAccount:
    def __init__(self):
        self.owner = "Harry"       # PUBLIC: Anyone can access this
        self._branch = "Main"      # PROTECTED: Should only be used internally
        self.__balance = 5000      # PRIVATE: Highly restricted

account = BankAccount()

print(account.owner)   # Works perfectly
print(account._branch) # Works, but violates Python community rules!

# print(account.__balance) <-- THIS WILL CAUSE AN ERROR! 
# Python hides it to protect the data.

```

---

Inheritance is what makes Object-Oriented Programming so powerful for large-scale software. It saves you from rewriting code and creates a beautiful, logical hierarchy for your applications.
