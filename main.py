import tkinter as tk
from tkinter import filedialog
import commands


def browse_folder():
    folder_selected = filedialog.askdirectory()
    
    if folder_selected:
        venv_directory.delete(0, tk.END)
        venv_directory.insert(0, folder_selected)

def create():
    if commands.check_execution_policy() not in commands.policies_that_work:
        commands.change_execution_policy()
    commands.create_venv(version.get(version.curselection()), venv_name.get(), f"{venv_directory.get()}")
    label = tk.Label(root, text=f"Created {venv_name.get()} Python version {version.get(version.curselection())} at {venv_directory.get()}")
    label.pack()


root = tk.Tk()
root.title("Python Virtual Environment Maker")
root.geometry("350x500")


frame = tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Store virtual environment in:")
label.pack()
venv_directory = tk.Entry(frame)
venv_directory.pack(side=tk.LEFT)
btn_browse = tk.Button(frame, text="Browse", command=browse_folder)
btn_browse.pack(side=tk.RIGHT)

frame=tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Select Python version:")
label.pack()
version = tk.Listbox(frame)
version.pack()
version.insert(tk.END, *commands.find_python_versions())

frame = tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Name of virtual environment:")
label.pack()
venv_name = tk.Entry(frame)
venv_name.pack()

button = tk.Button(root, text="Create", command=create)
button.pack(pady=10)


root.mainloop()