Welcome to **Part 3, Chapter 7: Scope & Virtual Environments**!

As you start building larger applications, your code will get split across multiple files, and you will start downloading code written by other people (packages).

In this chapter, we will learn the rules of where variables "live" (Scope), how to isolate your projects so they don't break each other (Virtual Environments), and a secret Python idiom that every professional developer uses when importing files.

---

## 🌐 Chapter 7: Scope & Virtual Environments

### 1. Local vs. Global Scope

Imagine you have a variable named `x`. If you create `x` inside a function, can you print it outside the function? No! This concept is called **Scope**.

* **Global Variables:** Variables created *outside* of any function. They can be read by anyone, anywhere in the file.
* **Local Variables:** Variables created *inside* a function. They are destroyed the exact second the function finishes running.

```python
x = 10 # This is a GLOBAL variable

def my_function():
    y = 5 # This is a LOCAL variable
    print("Inside function, x is:", x) # We can READ global variables inside
    print("Inside function, y is:", y)

my_function()

# print(y) <-- THIS WILL CAUSE AN ERROR! 'y' no longer exists out here.

```

**The `global` Keyword:**
If you want to actually *change* a global variable from inside a function, Python will normally stop you and just create a new local variable with the same name instead. To fix this, you must explicitly use the `global` keyword.

```python
score = 0

def increase_score():
    global score  # Tells Python: "I want to modify the global 'score', don't make a local one!"
    score = score + 1

increase_score()
print("Final Score:", score) # Output: 1

```

*(Pro-tip: While `global` is useful, using too many global variables is considered bad practice because it makes your code unpredictable. It's usually better to `return` values instead).*

### 2. Virtual Environments (`venv`)

When you build a Python project, you will eventually use `pip` to install third-party packages (like Django for web development or Pandas for data science).

By default, Python installs these globally on your computer. **This is a massive problem.** What if Project A needs Django version 2.0, but Project B needs Django version 4.0? If they share the global installation, one of your projects will break!

The solution is **Virtual Environments**. A virtual environment creates an isolated "room" for your project. Any packages you install inside this room stay in this room.

**How to use it (in your terminal):**

1. **Create the environment:** ```bash
python -m venv myenv
```
*(This creates a folder named `myenv` in your project).*

```


2. **Activate the environment:**
* **Windows:** `myenv\Scripts\activate`
* **Mac/Linux:** `source myenv/bin/activate`


3. **Install isolated packages:**
```bash
pip install requests

```


*(Notice your terminal prompt will now say `(myenv)` at the beginning!)*

### 3. Importing and the `__main__` Idiom

As your code grows, you will want to split it into multiple files. Let's say you create a file called `math_tools.py` with some useful functions, and you want to use them in `main.py`.

**The Problem:** When you import a file in Python, Python actually *runs* the entire file top-to-bottom instantly. If `math_tools.py` has a bunch of `print()` statements testing the code at the bottom, those will print out in your main program!

**The Solution:** The `if __name__ == "__main__":` idiom.

**In `math_tools.py`:**

```python
def add(a, b):
    return a + b

# Python assigns the secret variable __name__ the value "__main__" ONLY if 
# you run THIS file directly. If this file is IMPORTED, it is given the file's name instead.
if __name__ == "__main__":
    # This code ONLY runs if you execute math_tools.py directly.
    # It will be completely ignored if someone imports this file!
    print("Testing the add function:", add(2, 2))

```

**In `main.py`:**

```python
import math_tools

# We can use the function safely, and the test print statement from the other file won't run!
result = math_tools.add(10, 5)
print(result)

```

---

You now know how to manage memory scope, isolate your project dependencies like a professional, and build multi-file programs safely.