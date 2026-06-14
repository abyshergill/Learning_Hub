Welcome to **Module 2: The Styling (CSS3)**.

If HTML is the skeleton and raw structure of our webpage, CSS (Cascading Style Sheets) is the skin, the clothes, and the makeup. It is what transforms a boring, black-and-white word document into a beautiful, modern website.

Let's dive right into **Chapter 6: CSS Basics & Selectors**.

---

## 🎨 1. The Three Ways to Add Paint

Before we write any CSS, we have to tell the HTML file where to find our style instructions. There are three ways to do this, but only one is used by real professionals.

### A. Inline CSS (The Quick & Dirty Way)

You actually saw this briefly in our old treehouse! You slap a `style` attribute directly onto the HTML brick.

```html
<h1 style="color: blue;">This is a blue heading.</h1>

```

* **Verdict:** ❌ Bad for real websites. It makes your HTML incredibly messy and hard to read.

### B. Internal CSS (The Sandbox Way)

You can write CSS directly inside your HTML file by adding a `<style>` tag inside the `<head>` brain box.

```html
<head>
    <style>
        h1 { color: blue; }
    </style>
</head>

```

* **Verdict:** ⚠️ Okay for tiny, one-page tests, but terrible if you have a website with 50 different pages.

### C. External CSS (The Professional Way)

We create a brand new, completely separate file just for our styles (e.g., `style.css`). Then, we use a `<link>` tag inside the HTML `<head>` to connect them.

* **Verdict:** ✅ The industry standard. You can style 1,000 HTML pages perfectly using just one single `.css` file!

---

## 🧩 2. The CSS Syntax

Writing CSS is like giving instructions to an artist. You have to tell the artist **who** to paint (the Selector), **what** part of them to paint (the Property), and **how** to paint it (the Value).

Here is the exact recipe:

```css
selector {
    property: value;
}

```

* **Selector:** The HTML element you want to target (like `h1` or `p`).
* **Curly Braces `{ }`:** This is the box where your style rules live.
* **Property & Value:** What you want to change (e.g., `color: red;`). Always end with a semicolon `;`!

---

## 🎯 3. The Big Three Selectors

If you have 10 paragraphs on your website, but you only want to turn *one* of them red, how do you target it? We use Selectors.

### 1. The Tag Selector (Targets Everything)

If you just write the name of the HTML tag, it will change *every single one* of those tags on your whole page.

```css
/* This makes EVERY paragraph on the page gray */
p {
    color: gray;
}

```

### 2. The Class Selector (The VIP Club)

This is the most common selector. You give specific HTML elements a `class="some-name"` attribute. Then, in your CSS, you target that class using a **dot** (`.`). Multiple elements can share the same class!

```html
<p class="warning-text">Be careful!</p>

```

```css
/* CSS */
.warning-text {
    color: red;
    background-color: yellow;
}

```

### 3. The ID Selector (The Unique Fingerprint)

An ID is like a fingerprint. You give an HTML element an `id="some-name"` attribute. You can only use an ID name **once per page**. In CSS, you target it using a **hashtag** (`#`).

```html
<h1 id="main-logo">CodeWithHarry</h1>

```

```css
/* CSS */
#main-logo {
    font-size: 50px;
    color: blue;
}

```

---

## 🛠️ Putting It All Together in VS Code

Let's set up a professional workflow.

**Step 1:** In your VS Code project folder, create a brand new file and name it `style.css`.
**Step 2:** Paste this code into `style.css`:

```css
/* This is our style.css file */

/* 1. Tag Selector: Changes the whole page background */
body {
    background-color: #f4f4f4; /* A soft light gray */
}

/* 2. ID Selector: Targets just the main title */
#main-title {
    color: darkblue;
    text-align: center; /* Centers the text perfectly */
}

/* 3. Class Selector: Targets our special buttons */
.magic-btn {
    background-color: green;
    color: white;
    font-weight: bold;
}

```

**Step 3:** Open your `index.html` file and link the two files together:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 6: CSS</title>
    
    <link rel="stylesheet" href="style.css">
    
</head>
<body>

    <h1 id="main-title">Learning CSS is Fun!</h1>
    
    <p>This is a normal paragraph.</p>
    
    <button class="magic-btn">Click Me!</button>
    <button class="magic-btn">No, Click Me!</button>

</body>
</html>

```

Save both files, look at your Live Server, and watch your website come to life with actual colors and formatting!

---

## 🧠 Chapter 6 Cheat-Sheet

| Selector Type | CSS Symbol | HTML Attribute | Usage |
| --- | --- | --- | --- |
| **Tag Selector** | `tagname` | None | Targets all matching tags (e.g., all `<h1>`). |
| **Class Selector** | `.classname` | `class=""` | Targets a group of specific elements. |
| **ID Selector** | `#idname` | `id=""` | Targets one highly specific, unique element. |

---
