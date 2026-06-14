Welcome to **Chapter 1: The Web & HTML Basics**.

In the real world, web developers don't use basic text editors like Notepad, and they definitely don't write everything from memory. Today, we are going to set up your computer exactly like a professional software engineer's and write your first real code.

---

## 🌐 1. How the Internet Actually Works

Before we write code, you need to understand what happens when you type a website name into Google Chrome. The internet is basically a massive conversation between two types of computers: **Clients** and **Servers**.

* **The Client (You):** This is your web browser (Chrome, Safari, Firefox) on your phone or laptop. When you click a link, your client sends a **Request** out into the internet asking for a file.
* **The Server (The Host):** This is a powerful, specialized computer sitting in a massive warehouse somewhere. Its only job is to stay online 24/7, hold onto website files (HTML, CSS, JS), and send them back to Clients as a **Response**.

Right now, your computer is about to become both the client *and* a local server so you can test your own code!

---

## 🛠️ 2. Equipping Your Tools: VS Code & Live Server

To write code fast and efficiently, we need a code editor. The absolute industry standard is **Visual Studio Code (VS Code)**.

### Step 1: Download VS Code

Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the free installer for your operating system. Install it just like any normal program.

### Step 2: Install the "Live Server" Extension

If you just open an HTML file normally, you have to click "Refresh" on your browser every single time you make a change. Let's fix that.

1. Open VS Code.
2. On the far-left menu, click the icon that looks like four blocks (Extensions).
3. Search for **Live Server** (by Ritwick Dey).
4. Click **Install**.

Now, whenever you save your code, your browser will automatically update instantly!

---

## 🧱 3. The HTML Boilerplate (Your First Code)

Create a new folder on your computer's desktop and call it `My First Website`. Drag and drop that folder into VS Code to open it.

Create a new file inside that folder and name it `index.html`.

### The Pro-Developer Shortcut

You do not need to type the HTML skeleton out manually. VS Code has a built-in assistant called **Emmet**.

1. Open your blank `index.html` file.
2. Type a single exclamation mark `!`
3. Press the **Tab** or **Enter** key.

BOOM! VS Code will instantly generate the standard HTML5 Boilerplate:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <h1>Hello World! I am learning to code.</h1>

</body>
</html>

```

### Breaking Down the Boilerplate:

* **`<!DOCTYPE html>`:** Tells the browser to use the newest version of HTML (HTML5).
* **`<html lang="en">`:** The master box for the whole page. It also tells Google this page is in English.
* **`<head>`:** The brain. The user doesn't see what's in here.
* **`<meta charset="UTF-8">`:** Allows your website to display all characters, including emojis! 🚀
* **`<meta name="viewport" ...>`:** Crucial for making your website responsive so it looks good on mobile phones.
* **`<title>`:** The text that shows up on the browser tab at the very top of your screen.


* **`<body>`:** The physical page. Everything you want the user to see goes here.

---
