Let's build a hands-on project: **A Single-Container Flask Website**.

Flask is a popular Python tool used to build websites. We will create a simple page, package it inside our magic Docker box, and launch it so anyone on your local network can visit it.

---

## Step 1: Set Up Your Workshop (Folder Structure)

First, create a new folder on your computer named `flask-site`. Inside that folder, create a subfolder named `templates`.

Your project folder layout should look exactly like this:

```text
flask-site/
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── index.html

```

---

## Step 2: Create the Project Files

Open your favorite text editor (like Notepad or VS Code) and create the following four files inside your new folders.

### 1. `templates/index.html`

This is the visual face of your website. It uses standard HTML to draw a simple, clean greeting card.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Dockerized Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7f6;
            text-align: center;
            padding: 50px;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 { color: #4f46e5; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Success! Flask is running inside Docker!</h1>
        <p>This entire webpage is being served from inside an isolated container.</p>
    </div>
</body>
</html>

```

### 2. `app.py`

This Python script acts as the brains of your web server. It tells Python to listen for visitors and hand them the `index.html` page when they arrive.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This sends the index.html file to the visitor's browser
    return render_template('index.html')

if __name__ == '__main__':
    # Run the server on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)

```

### 3. `requirements.txt`

This text file acts as a tiny shopping list for Docker. It tells the container exactly what extra Python tools need to be downloaded for our code to work.

```text
Flask==3.0.3

```

### 4. `Dockerfile`

This is your master recipe. It tells Docker how to assemble the whole environment.

```dockerfile
# Step 1: Start with a light version of Python
FROM python:3.10-alpine

# Step 2: Create a workspace folder inside the container
WORKDIR /app

# Step 3: Copy our shopping list over and install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of our website code into the container
COPY . .

# Step 5: Tell the container to open Port 5000 to allow traffic
EXPOSE 5000

# Step 6: Press the start button to run the website
CMD ["python", "app.py"]

```

---

## Step 3: Bake the Image & Run the Container

Now that all your files are ready, open your computer terminal or command prompt, navigate into your main `flask-site` folder, and run these commands.

### 1. Build Your Custom Image

Tell the Docker Genie to read your Dockerfile and compile it into a reusable template named `my-flask-site`:

```bash
docker build -t my-flask-site .

```

### 2. Launch the Container

Now, turn that image into a live, running container box. We will link port **8080** on your real computer to port **5000** inside the container box using the `-p` hallway trick, and run it invisibly in the background with `-d`:

```bash
docker run -d -p 8080:5000 my-flask-site

```

---

## Step 4: View Your Website!

Open your web browser and navigate to this address:

```text
http://localhost:8080

```

**Boom!** You will see your clean white card with the heading: *"Success! Flask is running inside Docker!"* You have successfully built, packaged, and deployed a live Python web server entirely from scratch using a single Docker container.