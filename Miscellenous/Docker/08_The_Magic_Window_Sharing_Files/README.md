Let's learn how to change the words on that website and make it your own! To do this, we need to learn about a superpower called **Bind Mounts** (or as we like to call it, **The Magic Window**).

---

## Chapter 9: The Magic Window (Sharing Files)

Right now, your Nginx website container is like a sealed spaceship. It has its own files inside, and you are looking at them through the browser. But what if you want to swap their boring text file for a cool website you made?

Normally, if you change something *inside* a container and the container turns off, your changes vanish forever. It resets like a video game when you turn off the console.

To fix this, Docker allows you to cut a **Magic Window** through the side of the container box. This window connects a folder on your actual computer directly to a folder inside the container.

### Step 1: Create your webpage

On your actual computer, imagine you create a simple text file named `index.html` inside a folder called `mywebsite`. Inside that file, you type:

```html
<h1>Hello! Welcome to Captain Kid's Secret Coding Club!</h1>

```

### Step 2: Use the `-v` Spell

Now, we tell Docker to launch the website box, but we add the `-v` modifier (which stands for **Volume** or **Video window**).

Type this command (imagining you are inside your website folder):

`docker run -d -p 8080:80 -v ./mywebsite:/usr/share/nginx/html nginx`

Look at that new part: `-v ./mywebsite:/usr/share/nginx/html`

* **Left side (`./mywebsite`):** This is the folder on your real computer where your cool new file lives.
* **Right side (`/usr/share/nginx/html`):** This is the secret folder inside the spaceship where Nginx looks for website files.

### The Magic Result

Now, go back to your browser and refresh `http://localhost:8080`.

**Boom!** The boring "Welcome to nginx" screen is gone, and it now says: **"Hello! Welcome to Captain Kid's Secret Coding Club!"**

Even cooler: if you open that file on your desktop right now and change the words to "Docker is awesome!", the website changes *instantly* without you having to restart the container. You are editing files right through the magic window!

---