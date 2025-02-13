import os
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
from datetime import datetime  # Added import for datetime

# Function to download Facebook Reel
def download_facebook_reel(url, output_folder="downloads"):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Generate current date-time string
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Generate timestamp
    
    # YT-DLP options for downloading as MP4
    ydl_opts = {
        'format': 'mp4/best',
        # Use timestamp in filename instead of title
        'outtmpl': os.path.join(output_folder, f'{current_time}.%(ext)s'),  # Modified filename
        'noplaylist': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"✅ Reel downloaded successfully to: {os.path.abspath(output_folder)}")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to download reel: {e}")

# Rest of the code remains unchanged
def on_download_button_click():
    reel_url = url_entry.get().strip()
    if reel_url:
        download_facebook_reel(reel_url)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid Facebook Reel URL.")

root = tk.Tk()
root.title("Facebook Reel Downloader")
root.geometry("400x200")

url_label = tk.Label(root, text="Enter Facebook Reel URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Reel", command=on_download_button_click)
download_button.pack(pady=20)

root.mainloop()