# LOCAL PORT FORWARDING

To keep the web GUI running exactly as you are used to—but make it completely invisible to hackers—you will use SSH to create a "Local Port Forward." This creates an encrypted tunnel from your computer's web browser directly into the VPS.

Here is exactly how to lock it down and access the GUI:

1. **Bind pgAdmin to Localhost:** docker-compose.yml.
On your VPS, edit your Docker compose file so the pgAdmin port only listens internally. Change your `ports` section to include `127.0.0.1:`

```yaml
ports:
  - "127.0.0.1:5050:80"
```


2. **Restart the Container:**
Apply the changes by running this on your VPS:

```bash
docker-compose down
docker-compose up -d

```

*At this point, if you try to visit `http://your_vps_ip:5050` in your browser, it will fail. Your database is now hidden from the internet.*


3. **Open the Secure SSH Tunnel:**
Open your **local computer's** terminal (PowerShell, Command Prompt, or Mac Terminal) and run this exact command:

```bash
ssh -L 5050:127.0.0.1:5050 root@your_vps_ip

```

Log in with the password you just created. Leave this terminal window open. As long as it is open, the secure tunnel is active.


4. **Access pgAdmin in your Browser:**
Open your web browser (Chrome, Edge, Safari) and go to:
**`http://localhost:5050`**


Your browser will securely route the traffic through the SSH tunnel to your VPS. It looks and acts exactly like it did before, but now zero traffic is exposed to the public web. When you are done working with the database, just close the terminal window to shut down the tunnel.