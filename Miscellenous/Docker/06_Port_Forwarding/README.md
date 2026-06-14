Since you're ready for the grand tour, let's build something you can actually see and show off: **Your very own mini website running inside a magic box!**



To do this, we need to learn a cool trick called **Port Forwarding**.



---



## Chapter 7: The Secret Hallway (Port Forwarding)



Imagine your computer is a giant castle. Inside this castle, Docker builds a tiny, closed room for our website container. The website is up and running inside that room, but if you walk up to the castle gates, you can't see it because it's hidden deep inside!



To see the website from the outside world, we have to build a **Secret Hallway** from the castle's front gate directly to the container's door. In computer language, these gates and doors are called **Ports**.



### The Magic Spell: `docker run -d -p`



Let's use a super famous pre-made website image called **Nginx** (pronounced "Engine-X"). Type this long spell into your walkie-talkie:



`docker run -d -p 8080:80 nginx`



Whoa, that had a lot of secret modifiers! Let's decode what you just told the Docker Genie to do:



* **`-d` (The Invisibility Cloak):** This stands for *detached*. It tells the container to run quietly in the background. Instead of taking over your whole terminal screen, the Genie hands you back your walkie-talkie so you can keep typing other commands while the website runs.

* **`-p 8080:80` (The Secret Hallway):** This connects Gate `8080` on your actual computer to Door `80` inside the container.

* **`nginx`:** The name of the pre-made website box.



---