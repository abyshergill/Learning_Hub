Welcome to **Chapter 11: Advanced Class Features**!

Now that you understand the basics of Inheritance, it is time to look at the finer details of Object-Oriented Programming. What happens if a Parent class has a method, but the Child class wants to do it differently? How do you change variables for the *entire* blueprint rather than just one object?

In this chapter, we will unlock the true flexibility of Python classes.

---

## 🛠️ Chapter 11: Advanced Class Features

### 1. Method Overriding

When a Child class inherits a method from a Parent class, it doesn't have to be stuck with it forever. If you redefine a method in the Child class with the exact same name as the Parent's method, the Child's version will **override** the Parent's version.

```python
class Phone:
    def boot_up(self):
        print("Booting up standard operating system...")

class iPhone(Phone):
    # This overrides the boot_up method from the Parent class!
    def boot_up(self):
        print("Showing the Apple Logo...")

my_phone = iPhone()
my_phone.boot_up() # Outputs: Showing the Apple Logo...

```

### 2. The `super()` Keyword

Sometimes, you want to override a method to add new features, but you *still* want to run the original Parent's code so you don't have to rewrite it.

The `super()` function allows a Child class to reach up and temporarily call its Parent's methods.

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, department):
        # We use super() to let the Parent handle the 'name' setup
        super().__init__(name) 
        # Then the Child handles its unique 'department' setup
        self.department = department

boss = Manager("Alice", "IT")
print(f"{boss.name} manages the {boss.department} department.")

```

### 3. Static Methods & Class Methods

Normally, methods inside a class take `self` as the first argument, meaning they are designed to modify a specific *object*. But what if you want a method that belongs to the blueprint itself?

* **`@classmethod`:** Takes `cls` (the class) instead of `self`. It can modify variables that affect the entire blueprint, meaning every object built from it will see the change.
* **`@staticmethod`:** Takes *neither* `self` nor `cls`. It is just a normal, independent function that happens to be grouped inside the class for organization (usually for utility tasks like math calculations).

```python
class Company:
    company_name = "TechCorp" # A class attribute

    @classmethod
    def change_company_name(cls, new_name):
        # This changes the name for the ENTIRE company, not just one employee
        cls.company_name = new_name

    @staticmethod
    def add_numbers(a, b):
        # This doesn't need to know anything about the company or the employees
        return a + b

# Using the class method
Company.change_company_name("GlobalTech")
print(Company.company_name) # Outputs: GlobalTech

# Using the static method directly from the class
result = Company.add_numbers(10, 5)

```

### 4. Magic (Dunder) Methods

You have already used `__init__`, which is a "dunder" (double underscore) method. These are special, hidden methods in Python that customize how built-in Python functions interact with your custom objects.

For example, if you try to `print()` a custom object, Python will usually just output a nasty memory address like `<__main__.Book object at 0x000002A>`. You can use the `__str__` dunder method to tell Python exactly how your object should look when it gets printed!

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    # Customizes what happens when someone calls print() on the object
    def __str__(self):
        return f"'{self.title}'"
        
    # Customizes what happens when someone uses len() on the object
    def __len__(self):
        return self.pages

my_book = Book("Harry Potter", 350)

# Because we defined __str__, this looks beautiful!
print(my_book)        # Outputs: 'Harry Potter'

# Because we defined __len__, we can treat our object like a list!
print(len(my_book))   # Outputs: 350

```

---

You have officially mastered Object-Oriented Programming in Python! You can now build massive, scalable, and professional software architectures using inheritance, method overriding, and magic methods. 