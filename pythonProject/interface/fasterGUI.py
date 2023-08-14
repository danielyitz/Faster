import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry
import os
import shutil
from fasterFunctions import *


class FasterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Video Backup and Metadata Tool")

        # Change window size
        self.root.geometry("400x400")  # Width x Height

        # Change window background color
        self.root.configure(bg="lightblue")

        self.bride_label = tk.Label(self.root, text="Enter the name of the bride:", bg="lightblue")
        self.bride_entry = tk.Entry(self.root)

        self.groom_label = tk.Label(self.root, text="Enter the name of the groom:", bg="lightblue")
        self.groom_entry = tk.Entry(self.root)

        self.date_label = tk.Label(self.root, text="Select the date:", bg="lightblue")
        self.date_entry = DateEntry(self.root, date_pattern="dd_mm_yyyy")

        self.dest_label = tk.Label(self.root, text="Select Destination Directory:", bg="lightblue")
        self.dest_button = tk.Button(self.root, text="Browse", command=self.select_dest_directory, bg="lightblue")
        self.dest_entry = tk.Entry(self.root, width=35, borderwidth=5)

        self.backup_button = tk.Button(self.root, text="Backup and Copy Metadata", command=self.backup_and_copy,
                                       bg="lightblue")

        self.bride_label.pack(pady=10, padx=10)
        self.bride_entry.pack(pady=10, padx=10)

        self.groom_label.pack(pady=10, padx=10)
        self.groom_entry.pack(pady=10, padx=10)

        self.date_label.pack(pady=10, padx=10)
        self.date_entry.pack(pady=10, padx=10)

        self.dest_label.pack()
        self.dest_button.pack()
        self.dest_entry.pack()

        self.backup_button.pack()

    def select_dest_directory(self):
        dest_dir = filedialog.askdirectory()
        # print(dest_dir)

        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, dest_dir)

    def backup_and_copy(self):
        bride = self.bride_entry.get()
        groom = self.groom_entry.get()
        date = self.date_entry.get()
        dest_dir = self.dest_entry.get()

        nameOfCouple = bride + " and " + groom + " " + date
        create_dest_folder(dest_dir, nameOfCouple)

        current_path = os.path.join(dest_dir, nameOfCouple)
        # os.makedirs(curren_path)

        for subdir, origin_path in paths.items():
            create_dest_folder(current_path, subdir)
            subdir_path = os.path.join(current_path, subdir)
            # os.makedirs(subdir_path)

            try:
                amount_of_files = str(copy_files(origin_path, subdir_path))
                label = tk.Label(self.root,
                                 text=amount_of_files
                                      + " files were copied successfully from the "
                                      + subdir,
                                 bg="lightblue"
                                 )
                label.pack()
                # Using the function from functions.py

            except OSError:
                print("Missing", subdir)
                os.rmdir(subdir_path)
                messagebox.showerror("Error", "Missing " + subdir)

    def start(self):
        self.root.mainloop()


# Your existing paths dictionary
paths = {
    "main camera": "C:\\Users\\danie\\Desktop\\exampleSrc\\1",
    "hupa camera": "C:\\Users\\danie\\Desktop\\exampleSrc\\2",
    "drone": "C:\\Users\\danie\\Desktop\\exampleSrc\\3",
    "sound": "C:\\Users\\danie\\Desktop\\exampleSrc\\4"

    # "main camera": "G:\\PRIVATE\\M4ROOT\\CLIP",
    # "hupa camera": "D:\\PRIVATE\\M4ROOT\\CLIP",
    # "drone": "H:\\DCIM\\100MEDIA",
    # "sound": "F:\\MUSIC"

}

# Create an instance of FasterGUI
app = FasterGUI()

# Start the GUI event loop using the start() method
app.start()
