import subprocess
import os
import time

# Paths
playit_path = os.path.expanduser("~/playit-agent/target/release/playit-cli")
server_script = os.path.expanduser("~/Documents/ServerCommands/StartServer.command")

# Launch Playit tunnel
subprocess.Popen([playit_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Wait for Playit to finish connecting
time.sleep(2)

# Launch Minecraft server
subprocess.Popen(["bash", server_script])

print("✅ Server and Playit tunnel launched successfully.")
