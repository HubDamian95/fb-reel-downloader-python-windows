import os
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Function to download Facebook Reel
def download_facebook_reel(url, output_folder="downloads"):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # YT-DLP options for downloading as MP4
    ydl_opts = {
        'format': 'mp4/best',  # Automatically selects a single MP4 format
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"✅ Reel downloaded successfully to: {os.path.abspath(output_folder)}")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to download reel: {e}")

# Function to handle button click
def on_download_button_click():
    reel_url = url_entry.get().strip()  # Get the URL from the input field
    if reel_url:
        download_facebook_reel(reel_url)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid Facebook Reel URL.")

# Set up the main window
root = tk.Tk()
root.title("Facebook Reel Downloader")
root.geometry("400x200")

# Create the URL entry field and button
url_label = tk.Label(root, text="Enter Facebook Reel URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Reel", command=on_download_button_click)
download_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
