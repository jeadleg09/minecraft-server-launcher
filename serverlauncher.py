import tkinter as tk  # This is the GUI library
import subprocess      # This runs external commands

# ---- Define your functions ----

# Start the Minecraft server
def start_server():
    try:
        subprocess.Popen(
            ["/bin/bash", "-c", "/Users/jeadycelegrand/Documents/ServerCommands/StartServer.command"],
            shell=False
        )
    except Exception as e:
        print("Failed to start server:", e)

# Start the Playit tunnel
def start_tunnel():
    try:
        subprocess.Popen(
            ["/bin/bash", "-c", "/Users/jeadycelegrand/Documents/ServerCommands/StartPlayit.command"],
            shell=False
        )
    except Exception as e:
        print("Failed to start tunnel:", e)

# ---- Set up the GUI window ----

root = tk.Tk()
root.title("Minecraft Server Launcher")     # Title bar
root.geometry("300x200")                    # Size of the window

# ---- Add GUI widgets ----

title_label = tk.Label(root, text="Minecraft Server Launcher", font=("Helvetica", 16))
title_label.pack(pady=10)

server_button = tk.Button(root, text="Start Server", command=start_server, width=20)
server_button.pack(pady=10)

tunnel_button = tk.Button(root, text="Start Playit Tunnel", command=start_tunnel, width=20)
tunnel_button.pack(pady=10)

# ---- Start the GUI loop ----

root.mainloop()
