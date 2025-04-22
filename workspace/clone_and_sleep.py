import subprocess
import time
import os

repo_url = os.getenv("REPO_URL", "https://github.com/octocat/Hello-World.git")
print(f"Cloning repository: {repo_url}")
subprocess.run(["git", "clone", repo_url], check=True)

print("Repository cloned successfully. Keeping container alive...")
while True:
    time.sleep(60)
    print("Still alive...")
