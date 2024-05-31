import tkinter as tk
from tkinter import messagebox
import pytube
import os

def download_video():
    url = url_entry.get()
    try:
        video = pytube.YouTube(url)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid URL: {e}")
        return

    download_folder = "C:\moordex\code\YTDownloader\Pobrane"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    if format_var.get() == 1:
        video_title = video.title
        video_stream = video.streams.get_highest_resolution()
        try:
            video_stream.download(output_path=download_folder, filename=f"{video_title}.mp4")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {e}")
        else:
            messagebox.showinfo("Success", f"{video_title} downloaded successfully.")

    elif format_var.get() == 2:
        video_title = video.title
        audio_stream = video.streams.filter(only_audio=True).first()
        try:
            audio_stream.download(output_path=download_folder, filename=f"{video_title}.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {e}")
        else:
            messagebox.showinfo("Success", f"{video_title} downloaded successfully in MP3 format.")
            
root = tk.Tk()
root.title("YouTube Video Downloader")

tk.Label(root, text="Enter video URL:").pack()
url_entry = tk.Entry(root)
url_entry.pack()

root.geometry("800x400")
tk.Label(root, text="Choose format:").pack()
format_var = tk.IntVar()
tk.Radiobutton(root, text="MP4", value=1, variable=format_var).pack()
tk.Radiobutton(root, text="MP3", value=2, variable=format_var).pack()

tk.Button(root, text="Download", command=download_video).pack()

root.mainloop()