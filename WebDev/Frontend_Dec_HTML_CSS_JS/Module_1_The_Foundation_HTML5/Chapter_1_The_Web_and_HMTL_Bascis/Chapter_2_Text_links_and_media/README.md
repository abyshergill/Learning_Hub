Welcome to **Chapter 2: Text, Links, and Media**.

Now that you have your master HTML boilerplate set up in VS Code, it is time to start putting actual content inside the `<body>` tags.

In this chapter, we are going to learn how to write text properly, how to link different pages together, and how to display images. Along the way, you will learn a critical programming concept: **HTML Attributes**.

---

## ✍️ 1. Headings & Paragraphs

Search engines like Google read your website like a newspaper. They look for big headlines to figure out what the page is about, and they look for paragraphs for the actual story.

### Headings (`<h1>` to `<h6>`)

HTML gives you 6 levels of headings. `<h1>` is the most important (the main title), and `<h6>` is the least important.

```html
<h1>Main Website Title (Only use one per page!)</h1>
<h2>Sub-heading (Like a chapter title)</h2>
<h3>Sub-sub-heading (Like a section title)</h3>
<h4>Getting smaller...</h4>
<h5>Almost tiny...</h5>
<h6>The smallest heading.</h6>

```

> **Pro Tip:** Never use headings just to make text look big or bold. Use them to create a logical outline of your page. We will use CSS later to change exactly how big they look!

### Paragraphs (`<p>`)

For regular text, sentences, and paragraphs, we wrap the text in a `<p>` tag.

```html
<p>This is a standard paragraph of text. Browsers will automatically add a little bit of space above and below this block to keep it easy to read.</p>

```

### Line Breaks and Horizontal Rules

Sometimes you want to force the text to jump to the next line without starting a whole new paragraph, or you want to draw a dividing line across the screen. These tags are special because they are **self-closing** (they don't need a back bun!).

* **`<br>` (Break):** Forces a line break.
* **`<hr>` (Horizontal Rule):** Draws a horizontal dividing line.

---

## 🔗 2. The Anchor Tag and "Attributes"

The web is called a "web" because pages are linked together. We use the **Anchor tag (`<a>`)** to create clickable links.

But just typing `<a>Click Me</a>` isn't enough. The browser needs to know *where* to go. To tell it, we use an **Attribute**. Attributes are extra pieces of information added *inside* the opening tag.

```html
<a href="https://www.google.com">Take me to Google!</a>

```

* **`href` (Hypertext Reference):** This is the attribute. It stores the destination URL.

### Opening in a New Tab

If you don't want visitors to leave your website when they click a link, you can add a second attribute called `target="_blank"`. This tells the browser to open the link in a brand new tab!

```html
<a href="https://www.wikipedia.org" target="_blank">Read Wikipedia in a new tab</a>

```

---

## 🖼️ 3. Images and File Paths

To add pictures to your site, we use the `<img>` tag. Just like `<br>` and `<hr>`, the image tag is **self-closing**.

It requires two very important attributes to work properly:

1. **`src` (Source):** Where the image file is located.
2. **`alt` (Alternative Text):** A description of the image. If the image fails to load, or if a visually impaired user is reading your site with a screen reader, this text will be read to them.

```html
<img src="https://images.unsplash.com/photo-1561948955-570b270e7c36" alt="A fluffy orange cat sitting on a keyboard">

```

### Local Images vs. Web Images

You don't always have to link to images on other websites. Usually, you will save an image directly inside your project folder.

* **Web Image:** `src="https://..."`
* **Local Image:** If you save a picture called `logo.png` in the exact same folder as your `index.html` file, your path becomes very simple: `src="logo.png"`.

---

## 🛠️ Putting It All Together

Open your `index.html` file in VS Code. Delete the old "Hello World" line inside your `<body>` tags and replace it with this real-world example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Developer Blog</title>
</head>
<body>
    
    <h1>Welcome to My Developer Blog</h1>
    <p>Documenting my journey from beginner to Full Stack Developer.</p>

    <hr> <h2>Today's Progress</h2>
    <p>I just learned how to use headings, paragraphs, and attributes!</p>
    
    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=500" alt="A laptop on a desk with code on the screen">
    
    <br><br> <a href="https://code.visualstudio.com/" target="_blank">Click here to get VS Code</a>

</body>
</html>

```

Save the file. If your Live Server is running, your browser will instantly update to show a fully structured, multi-media webpage!