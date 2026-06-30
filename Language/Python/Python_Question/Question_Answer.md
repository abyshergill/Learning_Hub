## Beginner Questions

These focus on basic syntax, loops, and conditional logic.
* Check for Even or Odd: Write a program to check if a number is even or odd
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

* Calculate Factorial: Write a function to find the factorial of a given number.
```python
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
```
* Reverse a String: How can you reverse a string using slicing?
```python
def reverse_string(s):
    return s[::-1]
```
## Intermediate Questions
These involve data structures like lists, dictionaries, and more complex logic.
* Find Second Largest Number: Identify the second largest value in a list.
```python
def second_largest(numbers):
    unique_numbers = list(set(numbers)) # Remove duplicates
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
```
* Check for Palindrome: Check if a string reads the same forward and backward.
```python
def is_palindrome(s):
    return s == s[::-1]
```
* Merge Two Dictionaries: Combine two dictionaries into one.
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
```