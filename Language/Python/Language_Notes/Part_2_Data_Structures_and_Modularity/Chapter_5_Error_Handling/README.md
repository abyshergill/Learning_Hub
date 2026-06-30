Welcome to **Chapter 5: Error Handling**!

Up until now, if you made a mistake in your code, or if a user typed a word when your program asked for a number, Python would throw a massive red error message and the entire program would instantly crash.

In the real world, you cannot let your application crash just because a user made a typo. In this chapter, we will learn how to intercept those errors, handle them gracefully, and keep the program running.

---

## 🛡️ Chapter 5: Error Handling

### 1. Exception Handling (`try` and `except`)

When Python encounters an error, it raises an "Exception" (like a `ValueError` if data types are wrong, or a `ZeroDivisionError` if you divide by zero).

To stop the crash, we wrap our risky code inside a `try` block. If an error happens, Python immediately abandons the `try` block and jumps into the `except` block, allowing the program to survive.

```python
# A program that asks for a number and prints its multiplication table
try:
    user_input = input("Enter a number: ")
    number = int(user_input) # RISKY: If they type "Apple", this crashes!
    
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

except ValueError:
    # This block ONLY runs if a ValueError occurs in the try block
    print("Invalid input! You must type an actual number, not text.")

except Exception as e:
    # This acts as a catch-all for any other unexpected errors
    print(f"An unknown error occurred: {e}")

print("The program has successfully finished running.") # This will print even if there was an error!

```

### 2. The `finally` Keyword

Sometimes, you have a piece of code that **must** execute regardless of whether an error happened or not. For example, if you open a connection to a database, you must close it when you are done, even if the database query crashed.

We use the `finally` block for this. It runs no matter what—even if the `try` block succeeds, or if the `except` block catches a bug.

```python
def fetch_data():
    try:
        print("Opening database connection...")
        # Simulating a crash by dividing by zero
        result = 10 / 0 
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    finally:
        # This will print no matter what happens above!
        print("Closing database connection...")

fetch_data()

```

### 3. Raising Custom Errors (`raise`)

Sometimes, Python doesn't think there is an error, but *your specific business logic* says there is.

For example, if you are writing a script that accepts ages for a voting application, someone entering `-5` or `300` isn't technically a Python error (they are valid integers), but it makes no sense for your program. You can forcefully trigger an error using the `raise` keyword.

```python
age = int(input("Enter your age to vote: "))

if age < 0 or age > 150:
    # We forcefully stop the program and throw a custom error
    raise ValueError("Invalid age provided. Age must be between 0 and 150.")

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are too young to vote.")

```

---

You now know how to write bulletproof code! By utilizing `try`, `except`, and `raise`, you can ensure your applications run smoothly and provide helpful feedback to users instead of terrifying red crash logs.