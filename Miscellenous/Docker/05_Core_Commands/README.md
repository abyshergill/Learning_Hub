To talk to Docker, we use a special text window on our computer called the **Terminal** or **Command Prompt**. Think of it like a magical walkie-talkie that connects you directly to the Docker Genie.

---

## Chapter 6: Your First Magic Spells (The Core Commands)

When you type these commands, the Docker Genie will instantly run around and do the heavy lifting for you.

### Spell 1: Waking Up the Genie (`docker run`)

The most famous first command in the universe is the "Hello World" test. It’s how we make sure the magic is working.

Type this into your walkie-talkie and press Enter:
`docker run hello-world`

**What just happened behind the scenes?**

1. **The Search:** The Docker Genie looked inside your own computer's toy box to see if you already had the `hello-world` recipe (Image).
2. **The Trip to the Store:** You didn't have it! So, the Genie flew up to the internet cloud (**Docker Hub**), found the recipe, and downloaded it to your computer.
3. **Baking the Cake:** The Genie used that recipe to build a brand-new, tiny container box, opened it up, and shouted "Hello from Docker!" on your screen.
4. **The Nap:** Once the container finished saying hello, it automatically went to sleep so it wouldn't waste your computer's energy.

---

### Spell 2: Checking Your Toy Boxes (`docker ps`)

What if you have boxes running right now and you don't know it? You can ask the Genie to show you a list of all your active, running containers.

Type this command:
`docker ps`

If nothing shows up, it means all your boxes are currently asleep. If you want to see *every* box you've ever created (even the sleeping ones), add a `-a` (which stands for **all**):

`docker ps -a`

This will show you a neat little chart of your boxes, their secret ID numbers, and when they were created.

---

### Spell 3: Cleaning Up the Room (`docker rm`)

Imagine you played with 20 Lego sets and left them all over your bedroom floor. Your parents wouldn't be happy! Computer memory can get cluttered too.

To throw away a container box you don't need anymore, you tell the Genie its Container ID (which you found using `docker ps -a`) and say remove:

`docker rm <YOUR_CONTAINER_ID>`

> 🧹 **The Golden Cleanup Rule:** Cleaning up old, sleeping containers keeps your computer running fast and clean, leaving plenty of room for your next big project!

---