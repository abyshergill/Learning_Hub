Welcome to **Chapter 9: Modern Layouts (CSS Grid)**.

In the last chapter, we learned Flexbox. Flexbox is incredible, but it has one major limitation: it is a **1-Dimensional** layout system. It is meant to handle items in a *single row* OR a *single column* (like a navigation bar).

But what if you want to build a complex photo gallery, a Pinterest board, or a dashboard with a sidebar on the left and content on the right? You need to control rows *and* columns at the exact same time.

Enter **CSS Grid**: the ultimate **2-Dimensional** layout system.

---

## 🏁 1. The Grid Container

Just like Flexbox, CSS Grid relies on the **Parent and Child** relationship. You apply the grid rules to the master parent container, and the children automatically snap into place.

To turn the parent into a grid, we use one line of code:

```css
.grid-container {
    display: grid;
}

```

If you just write that, nothing visually changes. That is because you have activated the grid, but you haven't told the browser how many "slices" to cut it into!

---

## 🔪 2. Slicing the Grid (Columns and Rows)

To build our grid, we use two powerful properties: `grid-template-columns` and `grid-template-rows`.

Let's say we have 6 child `<div>` boxes inside our parent, and we want to create a perfect 3-column layout.

```css
.grid-container {
    display: grid;
    /* This creates 3 columns, each exactly 200px wide */
    grid-template-columns: 200px 200px 200px; 
    
    /* This adds space between the grid boxes */
    gap: 20px; 
}

```

**The Magic:** Because we only defined 3 columns, what happens to boxes 4, 5, and 6? CSS Grid is smart. Once it fills up the first 3 columns, it automatically wraps the rest of the items down to a brand new row!

---

## 🍕 3. The Secret Weapon: The `fr` Unit

Using exact pixels (`200px`) is dangerous in modern web design because everyone's screen size is different. If someone views your 600px grid on a tiny 400px mobile phone, it will break.

To fix this, CSS Grid introduced a brand new unit of measurement just for grids: the **Fractional Unit (`fr`)**.

One `fr` basically means *"one piece of the available pie."*

```css
.grid-container {
    display: grid;
    /* This creates 3 columns that share the screen perfectly equally! */
    grid-template-columns: 1fr 1fr 1fr; 
}

```

If you want the middle column to be twice as big as the others, you just change the recipe:

```css
.grid-container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr; 
}

```

> **Pro Tip:** If you want 4 equal columns, typing `1fr 1fr 1fr 1fr` gets annoying. You can use the repeat function: `grid-template-columns: repeat(4, 1fr);`

---

## 🛠️ Putting It All Together: A Photo Gallery

Let's build a clean, modern, 3-column photo gallery.

**HTML (`index.html`):**

```html
<body>
    <h1>My Vacation Gallery</h1>
    
    <div class="gallery">
        <div class="photo">1</div>
        <div class="photo">2</div>
        <div class="photo">3</div>
        <div class="photo">4</div>
        <div class="photo">5</div>
        <div class="photo">6</div>
    </div>
</body>

```

**CSS (`style.css`):**

```css
* {
    box-sizing: border-box;
}

body {
    background-color: #222; /* Dark theme */
    color: white;
    font-family: sans-serif;
    padding: 40px;
}

/* 1. Set up the Grid Parent */
.gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 15px; /* Perfect spacing between photos */
}

/* 2. Style the Grid Children to look like photo cards */
.photo {
    background-color: #ff5722; /* Bright orange */
    height: 200px; /* Force them to be tall */
    
    /* Wait, can we use Flexbox INSIDE a grid child to center the text? YES! */
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    font-weight: bold;
    border-radius: 10px; /* Rounds the harsh corners */
}

```

Save your files and look at the Live Server. You just built a perfectly responsive, professional-grade image gallery layout in less than 20 lines of CSS!

---

## 🧠 Chapter 9 Cheat-Sheet

| CSS Property | What it does | Example |
| --- | --- | --- |
| **`display: grid;`** | Turns the parent container into a 2D Grid. | N/A |
| **`grid-template-columns`** | Defines the number and width of vertical columns. | `1fr 2fr 1fr` |
| **`grid-template-rows`** | Defines the height of horizontal rows (optional, usually automatic). | `200px 400px` |
| **`gap`** | Creates spacing between the rows and columns. | `20px` |
| **`repeat()`** | A shortcut for creating many identical columns/rows. | `repeat(3, 1fr)` |

---