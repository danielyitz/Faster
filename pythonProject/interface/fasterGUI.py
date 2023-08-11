import tkinter as tk
from tkinter import filedialog
import os
import shutil


class FasterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Video Backup and Metadata Tool")

        self.bride_label = tk.Label(self.root, text="Enter the name of the bride:")
        self.bride_entry = tk.Entry(self.root)

        self.groom_label = tk.Label(self.root, text="Enter the name of the groom:")
        self.groom_entry = tk.Entry(self.root)

        self.date_label = tk.Label(self.root, text="Enter the date DDMMYY:")
        self.date_entry = tk.Entry(self.root)

        self.dest_label = tk.Label(self.root, text="Select Destination Directory:")
        self.dest_button = tk.Button(self.root, text="Browse", command=self.select_dest_directory)
        self.dest_entry = tk.Entry(self.root, state="readonly")

        self.backup_button = tk.Button(self.root, text="Backup and Copy Metadata", command=self.backup_and_copy)

        self.bride_label.pack()
        self.bride_entry.pack()

        self.groom_label.pack()
        self.groom_entry.pack()

        self.date_label.pack()
        self.date_entry.pack()

        self.dest_label.pack()
        self.dest_button.pack()
        self.dest_entry.pack()

        self.backup_button.pack()

    def select_dest_directory(self):
        dest_dir = filedialog.askdirectory()
        self.dest_entry.delete(0, tk.END)
        self.dest_entry.insert(0, dest_dir)

    def backup_and_copy(self):
        bride = self.bride_entry.get()
        groom = self.groom_entry.get()
        date = self.date_entry.get()
        dest_dir = self.dest_entry.get()

        nameOfCouple = bride + " and " + groom + " " + date
        curren_path = os.path.join(dest_dir, nameOfCouple)
        os.makedirs(curren_path)

        for subdir, origin_path in paths.items():
            subdir_path = os.path.join(curren_path, subdir)
            os.makedirs(subdir_path)

            try:
                self.move_files(origin_path, subdir_path)
            except OSError:
                print("Missing", subdir)
                os.rmdir(subdir_path)

    def move_files(self, origin_path, dest_path):
        os.chdir(origin_path)
        counter = 0
        for file in os.listdir():
            shutil.copy2(file, dest_path)
            counter += 1
        print(str(counter) + " files have copied to " + dest_path)

    def start(self):
        self.root.mainloop()


# Your existing paths dictionary
paths = {
    "main camera": "G:\\PRIVATE\\M4ROOT\\CLIP",
    "hupa camera": "D:\\PRIVATE\\M4ROOT\\CLIP",
    "drone": "H:\\DCIM\\100MEDIA",
    "sound": "F:\\MUSIC"
}

# Create an instance of FasterGUI
app = FasterGUI()

# Start the GUI event loop using the start() method
app.start()
