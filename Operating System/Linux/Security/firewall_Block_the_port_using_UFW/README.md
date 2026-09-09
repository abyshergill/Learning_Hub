*** Block the port using UFW (Uncomplicated Firewall)**
If your VPS is running Ubuntu or Debian, UFW is the standard tool. This will block outside attackers from even reaching the port, while allowing your local applications to connect.

Run these commands in your terminal:

1. **Allow SSH so you don't get locked out:**
```bash
sudo ufw allow ssh

```


2. **Deny external access to port 5050:**
```bash
sudo ufw deny 5050

```


3. **Enable the firewall:**
```bash
sudo ufw enable

```


4. **Verify the status:**
```bash
sudo ufw status

```