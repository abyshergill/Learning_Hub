## Chapter 11: Becoming the Chef (How to Create a Dockerfile)

Up until now, we’ve used pre-made boxes. Now, you are going to invent your own. To do this, you create a blank text file and name it exactly `Dockerfile` (with a capital D and no file extension like `.txt`).

Let's say we want to containerize a simple Python app that tells jokes. Here is how you write the recipe step-by-step:

```dockerfile
# Step 1: Grab a pre-made kitchen with Python already installed
FROM python:3.9-alpine

# Step 2: Create a special folder inside the container for our app
WORKDIR /app

# Step 3: Copy our code from our real computer into that folder
COPY . /app

# Step 4: Run a command to install any extra tools we need
RUN pip install flask

# Step 5: The "Start Button" when the container turns on
CMD ["python", "app.py"]

```

### The Magic Spell: `docker build`

Once you save this file next to your code, you have to tell the Docker Genie to read it and bake it into a fresh, reusable **Image** (cookie cutter).

You open your terminal and type this command:
`docker build -t my-joke-app .`

* **`-t my-joke-app`**: This "tags" your image with a cool, easy-to-remember name.
* **The Dot (`.`)**: Do not forget this! The dot tells Docker: *"Look in the exact folder I am standing in right now to find the Dockerfile."*

