## Chapter 5: The Lego Castle (Docker Compose - Advanced Mode)

Now that you are a pro, let's look at a bigger problem. What if you want to build a whole city? You don't just need one house; you need a school, a grocery store, and power lines all talking to each other.

In the coding world, a big application needs a **Website Box**, a **Database Box**, and a **User Login Box** to work together.

Instead of starting all those boxes one by one by hand, we use an advanced tool called **Docker Compose**.

Docker Compose uses a single master blueprint file (usually called `docker-compose.yml`). You write down all the boxes you want, and with one single command, it builds the entire city at once:

`docker-compose up`

Just like that, all your magic boxes wake up, connect their secret walkie-talkies, and start working together perfectly.
