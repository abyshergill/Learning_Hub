
## Chapter 3: Writing the Magic Recipe (The Dockerfile)

How do we make our own cookie cutter? We write a simple text file called a **Dockerfile**. It's just a step-by-step list of instructions telling Docker how to build your box.

Here is what a simple Dockerfile looks like:

```dockerfile
# Step 1: Start with a computer foundation (like choosing a kitchen)
FROM alpine

# Step 2: Put our game files into the magic box
COPY . /mygame

# Step 3: Tell the box what to do when it opens
CMD ["python", "/mygame/play.py"]

```
---


### The 3 Core Instructions:

* **`FROM`**: This tells Docker what basic computer system to start with.
* **`COPY`**: This grabs the toys from your real room and shoves them into the Docker box.
* **`CMD`**: This is the "Start Button." It tells the box what game to turn on the moment it opens.