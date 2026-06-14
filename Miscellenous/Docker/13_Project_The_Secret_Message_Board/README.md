## Chapter 14: The Graduation Project (The Secret Message Board)

Let's tie everything you've learned into a real project you can run on your computer right now! We are going to build a **Secret Message Board** website using Python and a Redis Database.

Create a brand new folder on your computer named `secret-board` and put these 4 files inside it:

### File 1: `app.py` (The Python App Code)

```python
from flask import Flask, request
import redis

app = Flask(__name__)
# Connects to our database box using its name from the compose file!
db = redis.Redis(host='database-box', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('message')
        db.rpush('messages', msg)
    
    all_msg = db.lrange('messages', 0, -1)
    html_list = "".join([f"<li>{m}</li>" for m in all_msg])
    
    return f'''
        <h1>🇨🇭 The Secret Message Board </h1>
        <form method="POST">
            <input type="text" name="message" placeholder="Type a secret...">
            <button type="submit">Post Secret</button>
        </form>
        <h3>Stored Secrets:</h3>
        <ul>{html_list}</ul>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

### File 2: `Dockerfile` (The Construction Recipe)

```dockerfile
FROM python:3.9-alpine
WORKDIR /app
# Install the database connector tool and web framework
RUN pip install flask redis
COPY . /app
CMD ["python", "app.py"]

```

### File 3: `.dockerignore` (The Trash Filter)

```text
__pycache__/
*.pyc

```

### File 4: `docker-compose.yml` (The Master Orchestration Blueprint)

```yaml
version: '3.8'

services:
  web-app:
    build: .
    ports:
      - "8080:5000"
    depends_on:
      - database-box

  database-box:
    image: redis:alpine

```

### Step-by-Step Execution:

1. Open your terminal window and navigate into your `secret-board` folder.
2. Wave your master conductor baton by typing:
`docker compose up`
3. Watch the logs dance across your screen! Once it settles down, open your web browser and go to: `http://localhost:8080`
4. Type a secret message and click "Post Secret".

**Congratulations, Captain!** Your custom Python app is processing your text, packaging it up, and sending it over a secure virtual network straight into an isolated database container. You have officially mastered Docker from beginner to advanced!