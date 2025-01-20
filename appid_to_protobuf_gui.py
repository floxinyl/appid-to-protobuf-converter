import base64
import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

def encode_appid_to_protobuf(appid):
    """Encodes an AppID into a protobuf message and returns the base64 representation."""
    try:
        appid = int(appid)
        protobuf_bytes = b'\x08'
        value = appid
        while value > 0x7F:
            protobuf_bytes += bytes([(value & 0x7F) | 0x80])
            value >>= 7
        protobuf_bytes += bytes([value & 0x7F])
        protobuf_bytes += b'\x10\x01'
        return base64.b64encode(protobuf_bytes).decode("utf-8")
    except ValueError:
        return None

def fetch_game_name(appid):
    """Fetches the game name using the Steam Store API."""
    try:
        url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
        response = requests.get(url)
        data = response.json()
        if data and str(appid) in data and data[str(appid)]["success"]:
            return data[str(appid)]["data"]["name"]
        else:
            return "Unknown Game"
    except Exception:
        return "Unknown Game"

def convert_appid():
    """Handle the conversion when the button is clicked."""
    appid = appid_entry.get()
    if not appid.isdigit():
        messagebox.showerror("Error", "Please enter a valid numeric APPID.")
        return
    protobuf_value = encode_appid_to_protobuf(appid)
    if protobuf_value:
        game_name = fetch_game_name(appid)
        output_label.config(
            text=f"Game: {game_name}\nProtobuf Value: {protobuf_value}", fg="#ffffff"
        )
        root.clipboard_clear()
        root.clipboard_append(protobuf_value)
        root.update()
        show_copy_notification()
    else:
        messagebox.showerror("Error", "Failed to encode the APPID.")

def show_copy_notification():
    """Show a green notification for a successful copy."""
    copy_notification_label.config(text="Copied to clipboard!", fg="#32cd32")
    root.after(10000, lambda: copy_notification_label.config(text=""))

def open_github():
    """Open the GitHub repository in the browser."""
    webbrowser.open_new("https://github.com/floxinyl/appid-to-protobuf-converter")

# Set up the GUI
root = tk.Tk()
root.title("AppID to Protobuf Converter")

# Aesthetic colors and fonts
root.geometry("450x350")
root.configure(bg="#1c1f26")  # Dark grey background

# Set font
font_regular = ("Helvetica", 12)
font_bold = ("Helvetica", 14, "bold")

# Input Label
appid_label = tk.Label(
    root, text="Enter APPID:", bg="#1c1f26", fg="#ffffff", font=font_bold
)
appid_label.pack(pady=10)

# Input Entry
appid_entry = tk.Entry(
    root, width=30, bg="#2b2f38", fg="#ffffff", insertbackground="#ffffff", font=font_regular, relief="flat"
)
appid_entry.pack(pady=5)

# Convert Button
convert_button = tk.Button(
    root,
    text="Convert",
    command=convert_appid,
    bg="#007acc",
    fg="#ffffff",
    font=font_regular,
    relief="flat",
    bd=0,
    padx=10,
    pady=5,
    highlightthickness=0,
)
convert_button.pack(pady=10)
convert_button.configure(
    highlightbackground="#005f99",
    activebackground="#005f99",
    highlightcolor="#005f99",
)

# Output Label
output_label = tk.Label(root, text="", bg="#1c1f26", fg="#ffffff", font=font_regular, wraplength=400, justify="center")
output_label.pack(pady=10)

# Copy Notification Label
copy_notification_label = tk.Label(root, text="", font=font_regular, bg="#1c1f26")
copy_notification_label.pack(pady=5)

# GitHub Button
github_button = tk.Button(
    root,
    text="GitHub",
    command=open_github,
    bg="#2b2f38",
    fg="#ffffff",
    font=font_regular,
    relief="flat",
    bd=0,
    padx=5,
    pady=2,
    highlightthickness=0,
)
github_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
github_button.configure(
    highlightbackground="#005f99",
    activebackground="#005f99",
    highlightcolor="#005f99",
)

# Run the application
root.mainloop()