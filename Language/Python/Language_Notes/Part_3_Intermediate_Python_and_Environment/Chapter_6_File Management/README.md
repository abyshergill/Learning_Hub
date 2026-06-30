Welcome to **Part 3, Chapter 6: File Management**!

Up until now, every time you run a Python script, any data you create (like variables or lists) is stored in the computer's temporary memory (RAM). The second the program finishes running, that data vanishes forever.

In this chapter, we will learn how to make data permanent by teaching Python how to create, read, and modify actual files on your computer's hard drive.

---

## 📁 Chapter 6: File Management

### 1. File I/O (Opening, Reading, and Writing)

To interact with a file, you must first `open()` it. When opening a file, you have to tell Python exactly what you want to do with it by specifying a **mode**:

* **`'r'` (Read):** Opens a file to read its contents. (This is the default mode).
* **`'w'` (Write):** Opens a file to write data. **Warning:** This will instantly erase everything currently in the file and overwrite it!
* **`'a'` (Append):** Opens a file and adds new data to the very end without erasing what is already there.

Here is how you handle files using the modern `with` statement. The `with` block is a "Context Manager"—its superpower is that it automatically closes the file for you when the block ends, preventing memory leaks!

```python
# 1. WRITING to a file
# If "data.txt" doesn't exist, Python will create it automatically.
with open("data.txt", "w") as file:
    file.write("Hello! This is the first line.\n")
    file.write("This is the second line.\n")

# 2. APPENDING to a file
with open("data.txt", "a") as file:
    file.write("This line is appended to the end!\n")

# 3. READING from a file
with open("data.txt", "r") as file:
    # Read the entire file content into a string
    content = file.read()
    print("--- File Contents ---")
    print(content)

```

### 2. Seek and Tell (Moving the File Cursor)

When Python reads or writes a file, it uses an invisible "cursor" (just like the blinking line when you type in a word processor).

If you read a file, the cursor moves to the very end. If you try to read it again immediately, you will get blank text because the cursor is already at the finish line!

* **`tell()`:** Tells you exactly which byte the cursor is currently sitting at.
* **`seek()`:** Moves the cursor to a specific byte in the file.

```python
with open("data.txt", "r") as file:
    print("Cursor starts at byte:", file.tell())  # Output: 0
    
    # Read the first 5 characters
    first_five = file.read(5)
    print("First 5 characters:", first_five)
    
    print("Cursor is now at byte:", file.tell())  # Output: 5
    
    # Move the cursor back to the very beginning!
    file.seek(0)
    print("Reading again:", file.read(5))         # Output: Hello

```

### 3. The OS Module (Controlling Your Computer)

Python isn't just for math and web servers; it is a powerful tool for automating your operating system. The built-in `os` module allows Python to interact with your computer's file system—creating folders, deleting files, and renaming directories in bulk.

Imagine you need to create 100 folders for a massive project. Doing that by right-clicking "New Folder" 100 times would take forever. Python can do it in 3 lines of code.

```python
import os

# Create a new directory (folder)
if not os.path.exists("My_Project_Folder"):
    os.mkdir("My_Project_Folder")
    print("Folder created successfully!")

# Bulk create 5 folders inside the main folder
for i in range(1, 6):
    folder_name = f"My_Project_Folder/Day_{i}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

# List everything inside a specific directory
contents = os.listdir("My_Project_Folder")
print("Folders inside My_Project_Folder:", contents)

# Deleting a file (Be careful with this!)
# os.remove("some_old_file.txt") 

```