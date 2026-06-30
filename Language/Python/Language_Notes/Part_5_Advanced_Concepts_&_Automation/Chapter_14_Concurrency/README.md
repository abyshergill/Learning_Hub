Welcome to the Grand Finale! You have made it to **Chapter 14: Concurrency**.

Up to this point, your Python programs have executed sequentially—one line runs, the computer waits for it to finish, and then it moves to the next line. But what if you need to download 100 images from the internet? Waiting for them to download one by one would take forever.

In this final chapter, we will learn how to make Python do multiple things at the exact same time using Threads, Processes, and Asynchronous programming.

---

## ⚡ Chapter 14: Concurrency

### 1. Multithreading (For I/O-Bound Tasks)

A **Thread** is a separate flow of execution. Multithreading allows you to spin up multiple workers within the *same* program memory.

Because of a quirk in Python called the Global Interpreter Lock (GIL), multiple threads cannot actually process heavy math at the exact same millisecond. However, threads are absolutely perfect for **I/O-bound tasks**—tasks where the computer is just sitting around waiting for something else (like waiting for a file to download, or waiting for a database to respond).

```python
import threading
import time

def download_file(file_name):
    print(f"Starting download: {file_name}...")
    time.sleep(2)  # Simulating the time it takes to download a file
    print(f"Finished downloading: {file_name}!")

# If we ran these normally, it would take 4 seconds total (2 seconds + 2 seconds).
# Let's run them in separate threads!
thread1 = threading.Thread(target=download_file, args=("Image_A.jpg",))
thread2 = threading.Thread(target=download_file, args=("Image_B.jpg",))

# Start the threads simultaneously
thread1.start()
thread2.start()

# .join() tells the main program to wait here until both threads finish
thread1.join()
thread2.join()

print("All downloads complete in just 2 seconds!")

```

### 2. Multiprocessing (For CPU-Bound Tasks)

What if you need to do heavy mathematical calculations, like rendering a 3D video or processing millions of rows of data? Threads won't help you here because of Python's GIL.

Instead, we use **Multiprocessing**. This spins up completely separate, independent Python programs behind the scenes. Each process gets its own memory and runs on a totally different core of your computer's CPU.

We can use the modern `concurrent.futures` module to make this incredibly easy:

```python
import concurrent.futures
import time

def heavy_computation(name):
    print(f"Task {name} starting...")
    # A heavy math task
    result = sum(i * i for i in range(10_000_000))
    return f"Task {name} complete!"

# In Windows, multiprocessing MUST be wrapped in the __main__ idiom!
if __name__ == "__main__":
    start_time = time.time()
    
    # We create a pool of CPU workers
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # executor.map automatically splits the tasks across your CPU cores
        tasks = ["A", "B", "C", "D"]
        results = executor.map(heavy_computation, tasks)
        
        for result in results:
            print(result)
            
    print(f"Total time taken: {time.time() - start_time} seconds")

```

### 3. AsyncIO (The Modern Standard for Web Apps)

**Asynchronous I/O** is the newest and most popular way to handle concurrency in modern Python, especially for building high-performance web servers (like FastAPI or Discord bots).

Unlike threading (where the operating system constantly juggles workers), AsyncIO uses a single thread and an **Event Loop**. It relies on two keywords:

* **`async`**: Used to define an asynchronous function.
* **`await`**: Tells Python, *"This task is going to take a while. Pause this function, go do something else, and come back when this is ready."*

```python
import asyncio
import time

# We use 'async def' to create an asynchronous function
async def fetch_data(user_id):
    print(f"Requesting data for User {user_id}...")
    # asyncio.sleep is a non-blocking wait. 
    # It completely frees up Python to go run other code while it waits!
    await asyncio.sleep(2) 
    print(f"Data received for User {user_id}!")

async def main():
    # asyncio.gather runs multiple async tasks at the exact same time
    await asyncio.gather(
        fetch_data(101),
        fetch_data(102),
        fetch_data(103)
    )

# You must use asyncio.run() to start the event loop
start = time.time()
asyncio.run(main())
print(f"AsyncIO finished in {time.time() - start} seconds!")

```

---
