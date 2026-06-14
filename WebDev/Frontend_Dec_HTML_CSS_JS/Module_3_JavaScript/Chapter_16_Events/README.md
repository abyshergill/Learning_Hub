Welcome to **Chapter 16: Events**.

In the last chapter, we learned how JavaScript can use the DOM to reach out and change your HTML and CSS. But right now, those changes happen the exact millisecond the page loads.

Real websites wait for the *user* to do something before they react. They wait for a user to click a "Like" button, type a password, or scroll down a page. In JavaScript, these user actions are called **Events**.

---

## 👂 1. What is an Event Listener?

To make our JavaScript wait for a user to do something, we use a tool called an **Event Listener**.

Think of an Event Listener as a tiny security guard that you assign to a specific HTML button. The guard's only job is to stand there and listen. If they hear a "Click!", they press a giant red button that runs your JavaScript function.

### The 3 Steps to Build a Listener:

1. **Grab the element:** Tell JavaScript which HTML tag you want to guard.
2. **Choose the Event:** Tell the guard what to listen for (a click, a hover, a keyboard press).
3. **Write the Function:** Tell the guard exactly what code to run when the event happens.

---

## 🖱️ 2. Writing Your First Click Event (`addEventListener`)

Let's build a button that changes the webpage title when you click it.

**HTML:**

```html
<h1 id="main-title">Hello World!</h1>
<button id="magic-btn">Click to change title!</button>

```

**JavaScript:**

```javascript
// Step 1: Grab the elements
const myButton = document.querySelector("#magic-btn");
const myTitle = document.querySelector("#main-title");

// Step 2 & 3: Attach the Listener and Write the Function
myButton.addEventListener("click", function() {
    
    // Everything inside these curly braces ONLY runs when the button is clicked!
    myTitle.innerText = "You clicked the button! 🎉";
    myTitle.style.color = "blue";
    
});

```

---

## ⌨️ 3. The Secret Event Object (`e`)

When a user triggers an event (like pressing a key on their keyboard), how do you know *which* key they pressed? Was it the Spacebar? Was it the letter 'A'?

Whenever an event happens, the browser secretly creates a file folder containing every detail about that exact moment. It hands this folder directly into your function. Developers usually name this folder **`e`** (short for Event).

Let's listen to the entire webpage (`document`) to see what keys the user is typing!

```javascript
// We attach the listener to the whole document
document.addEventListener("keydown", function(e) {
    
    // The 'e' folder has a property called 'key' that tells us what was pressed
    console.log("You just pressed the key: " + e.key);
    
    // We can use an IF statement to make a secret cheat code!
    if (e.key === "Enter") {
        console.log("Access Granted! 🔓");
    }
    
});

```

---

## 📅 4. The Most Popular Events

There are dozens of events you can listen for, but you will use these four almost every single day:

* **`"click"`:** Fires when the user clicks the element.
* **`"mouseenter"`:** Fires the exact moment the user's mouse pointer touches the element (great for hover effects via JS).
* **`"mouseleave"`:** Fires when the mouse pointer moves away from the element.
* **`"keydown"`:** Fires when a user presses a key on their keyboard.

---

## 🛠️ Putting It All Together: The Dark Mode Toggle

Let's combine everything we have learned in Module 1, 2, and 3 to build a real-world feature: A Dark Mode Toggle button.

When you click it, the page turns dark. When you click it again, the page turns light!

**HTML (`index.html`):**

```html
<body class="light-theme">
    <h1>Welcome to My Blog</h1>
    <button id="theme-btn">Switch to Dark Mode</button>
</body>

```

**CSS (`style.css`):**

```css
/* We create our two themes in CSS */
.light-theme {
    background-color: white;
    color: black;
}

.dark-theme {
    background-color: #333;
    color: white;
}

```

**JavaScript (`script.js`):**

```javascript
// 1. Grab the body and the button
const body = document.querySelector("body");
const themeBtn = document.querySelector("#theme-btn");

// 2. Add the Event Listener to the button
themeBtn.addEventListener("click", function() {
    
    // The `.toggle()` method is a magical DOM trick! 
    // If the class is missing, it adds it. If it is already there, it removes it!
    body.classList.toggle("dark-theme");
    
    // Change the button text based on the current theme
    if (body.classList.contains("dark-theme")) {
        themeBtn.innerText = "Switch to Light Mode";
    } else {
        themeBtn.innerText = "Switch to Dark Mode";
    }
    
});

```

*If you run this code, you will have a fully functioning, professional dark mode switch!*

---

## 🧠 Chapter 16 Cheat-Sheet

| Code | What it does | Real-World Analogy |
| --- | --- | --- |
| **`addEventListener`** | Attaches a listener to an HTML element. | Hiring a security guard to watch a door. |
| **`"click"`** | The most common event type. | The action the guard is waiting for. |
| **`function() { ... }`** | The callback function. | The instructions the guard follows *after* the event. |
| **`e` (Event Object)** | An object containing details about the event. | The security report (who clicked, what key was pressed). |
| **`classList.toggle("...")`** | Adds a CSS class if missing, removes it if present. | Flipping a light switch on and off. |

---