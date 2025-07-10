import tkinter as tk  # This is the GUI library
import subprocess      # This runs external commands

# ---- Set up the GUI window ----
window = tk.Tk()
window.title("Minecraft Server Launcher")     # Title bar
window.geometry("300x200")                    # Size of the window

# --- add status label to gui ---
from tkinter import messagebox 
status_text = tk.StringVar()
status_text.set("Status: Idle")

# ---- Define your functions ----

# --- Start the Minecraft server ---
def start_server():
    status_text.set("Status: Starting server...")

    try:
        subprocess.Popen(
            ["/bin/bash", "-c", "/Users/jeadycelegrand/Documents/ServerCommands/StartServer.command"],
            shell=False
        )
        status_text.set("Status: Server started!")

    except Exception as e:
        status_text.set("Failed to start server:", e)
        messagebox.showerror("Error", f"Could not start server: {e}")

# --- Start the Playit tunnel ---
def start_tunnel():
    status_text.set("Status: Starting Playit Tunnel...")
    try:
        subprocess.Popen(
            ["/bin/bash", "-c", "/Users/jeadycelegrand/Documents/ServerCommands/StartPlayit.command"],
            shell=False
        )
        status_text.set("Status: Playit Tunnel started!")

    except Exception as e:
        status_text.set("Failed to start tunnel:", e)
        messagebox.showerror("Error" f"Could not start Playit tunnel: {e}")

# ---- Add GUI widgets ----
title_label = tk.Label(window, text="Minecraft Server Launcher", font=("Helvetica", 16))
title_label.pack(pady=10)

server_button = tk.Button(window, text="Start Server", command=start_server, width=20)
server_button.pack(pady=10)

tunnel_button = tk.Button(window, text="Start Playit Tunnel", command=start_tunnel, width=20)
tunnel_button.pack(pady=10)

status_label = tk.Label(window, textvariable=status_text)
status_label.pack(pady=10)

# ---- Start the GUI loop ----
window.mainloop()
