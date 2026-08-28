### SSH key Link to Github Profile

If you don't want to deal with tokens expiring or Keychain prompts, configure an SSH key:

1. Generate key:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"

```


2. Copy it:
```bash
pbcopy < ~/.ssh/id_ed25519.pub

```


3. Add it to GitHub (**Settings** $\rightarrow$ **SSH and GPG keys** $\rightarrow$ **New SSH key**).
4. Update remote to SSH:
```bash
git remote set-url origin git@github.com:<user_name>/<repo_name>.git
git push origin <branch_head>

```