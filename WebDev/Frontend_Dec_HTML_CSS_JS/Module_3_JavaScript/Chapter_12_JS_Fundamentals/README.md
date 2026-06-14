Welcome to **Module 3: The Brain (JavaScript)**!

You are now entering the final and most powerful stage of web development. HTML built the skeleton, CSS painted the skin, but **JavaScript (JS)** is the brain. It is what makes your website think, remember things, do math, and react when a user clicks a button.

Today, in **Chapter 12: JS Fundamentals**, we are going to learn how to connect this brain to your website and how to teach it to remember basic information.

---

## 🔌 1. Linking the Brain to the Body

Just like we had to link our CSS file to our HTML, we have to link our JavaScript file. But there is a very specific rule for *where* we put this link.

In VS Code, create a brand new file called `script.js`.

Now, open your `index.html`. Instead of putting the link in the `<head>` brain box (like we did with CSS), we put the JavaScript link at the **very bottom** of the `<body>`, right before it closes.

```html
<body>
    <h1>My Interactive Website</h1>
    <p>This page can think!</p>

    <script src="script.js"></script>
</body>

```

> **Why at the bottom?** The browser reads code from top to bottom. If it loads a massive JavaScript brain first, the user will just stare at a blank white screen while it loads. By putting it at the bottom, the user sees the HTML and CSS instantly, and the "brain" secretly boots up in the background!

---

## 📻 2. The Secret Developer Walkie-Talkie

When you write JavaScript, it doesn't automatically show up on the actual webpage. To test if our brain is working, we use a secret walkie-talkie that only developers can see called the **Console**.

In your `script.js` file, type this exact line:

```javascript
console.log("Hello, world! I am alive!");

```

**How to find the Console:**

1. Open your Live Server webpage in Google Chrome.
2. **Right-click** anywhere on the screen and click **Inspect**.
3. A scary-looking developer panel will slide out. Look at the top tabs and click **Console**.
4. You will see your secret message printed right there!

---

## 📦 3. Variables (Digital Storage Boxes)

To make a computer "think," it first needs to be able to remember things. We do this using **Variables**.

Think of a variable as a cardboard box. You write a name on the outside of the box with a marker, and you put data inside the box.

In modern JavaScript, we have two main ways to create these boxes: `let` and `const`.

### The `let` Box (Things that change)

If you are storing something that might change later (like a player's score in a game, or a user's age), you use the word `let`.

```javascript
// We created a box named 'score' and put the number 0 inside it.
let score = 0;

// Later in the game, the player gets a point! We can change the box:
score = 1; 

```

### The `const` Box (Things that NEVER change)

If you are storing something permanent (like your birth date, or gravity), you use `const` (Constant). If you try to change a `const` box later, the computer will throw an angry red error and crash!

```javascript
const birthYear = 1995;

// birthYear = 1996; <-- THIS WOULD CRASH THE PROGRAM!

```

---

## 🧬 4. Data Types (What goes in the box?)

Computers are very strict. They need to know exactly *what kind* of data you are putting inside your storage boxes. Here are the "Big 3" data types you will use every single day:

### 1. Strings (Text)

A string is just standard text. To tell the computer it is text (and not code), you **must** wrap it in quotation marks `" "` or `' '`.

```javascript
let playerName = "Harry";
let secretMessage = 'Welcome to the matrix!';

```

### 2. Numbers (Math)

Numbers are just regular numbers. **Do not use quotation marks!** If you put quotes around a number, the computer thinks it's a word and refuses to do math with it.

```javascript
let playerAge = 25;
let temperature = 98.6; // Decimals work perfectly fine!

```

### 3. Booleans (Light Switches)

A boolean is the simplest data type in the world. It can only ever be one of two things: `true` or `false`. Think of it like a digital light switch.

```javascript
let isGameOver = false; // The game is currently playing
let hasKey = true;      // The player picked up the secret key

```

---

## 🧠 Chapter 12 Cheat-Sheet

| JS Concept | What it does | Real-World Analogy |
| --- | --- | --- |
| **`<script src="...">`** | Links your HTML to your JS file. | Plugging the brain into the skeleton. |
| **`console.log()`** | Prints secret messages for the developer. | A hidden walkie-talkie. |
| **`let`** | A variable box whose contents can change later. | A whiteboard you can erase and rewrite. |
| **`const`** | A variable box whose contents are locked forever. | A stone tablet carved with a chisel. |
| **String** | Text data wrapped in `" "`. | A nametag. |
| **Number** | Mathematical data without quotes. | A calculator input. |
| **Boolean** | `true` or `false` value. | A light switch (On/Off). |