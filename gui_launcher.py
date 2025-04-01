import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os, sys
import json


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.tooltip_window or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=4, ipady=2)

    def hide(self, event=None):
        tw = self.tooltip_window
        self.tooltip_window = None
        if tw:
            tw.destroy()




CONFIG_FILENAME = "compiler_config.json"

def get_config_path():
    return os.path.join(os.path.dirname(__file__), CONFIG_FILENAME)

def load_config():
    try:
        with open(get_config_path(), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_config(data):
    try:
        with open(get_config_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("Failed to save config:", e)


def browse_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        project_dir_var.set(dir_path)

def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md"), ("All files", "*.*")])
    if file_path:
        output_file_var.set(file_path)

def run_compilation():
    directory = project_dir_var.get()
    output = output_file_var.get()

    if not os.path.isdir(directory):
        messagebox.showerror("Error", "Please select a valid project directory.")
        return

    cmd = [sys.executable, "compile.py", directory]

    # cmd = ["python", "compile.py", directory]

    cmd += ["--output", output]
    
    cmd += ["--config_file", get_config_path()]


    if not markdown_var.get():
        cmd += ["--no_markdown"]
    if not tree_var.get():
        cmd += ["--no_tree"]
    if open_var.get():
        cmd += ["--open"]
    if normalize_eol_var.get():
        cmd += ["--normalize_eol"]

    try:
        max_size = int(max_size_var.get())
        cmd += ["--max_size", str(max_size)]
    except ValueError:
        messagebox.showerror("Error", "Max size must be an integer.")
        return

    try:
        min_lines = int(min_lines_var.get())
        cmd += ["--min_lines", str(min_lines)]
    except ValueError:
        messagebox.showerror("Error", "Min lines must be an integer.")
        return

    print("Running:", " ".join(cmd))

    try:
        include_extensions = get_extensions()
        include_filenames = get_filenames()
        exclude_dirs = get_exclude_dirs()

        config_data = {
            "project_dir": directory,
            "output_file": output,
            "markdown": markdown_var.get(),
            "tree": tree_var.get(),
            "open": open_var.get(),
            "normalize_eol": normalize_eol_var.get(),
            "max_size": max_size,
            "min_lines": min_lines
        }

        if not is_extensions_default():
            config_data["include_extensions"] = get_extensions()
        if not is_filenames_default():
            config_data["include_filenames"] = get_filenames()
        if not is_exclude_default():
            config_data["exclude_dirs"] = get_exclude_dirs()

        save_config(config_data)
        
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", "Project compiled successfully!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Something went wrong during compilation.")

# === GUI Layout ===
root = tk.Tk()
root.title("Project Compiler GUI")

# Vars
config = load_config()

default_extensions = [".py", ".ipynb", ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".rst", ".cpp", ".h", ".hpp", ".c", ".java", ".js", ".ts"]
default_filenames = ["README", "README.md", "requirements.txt", "pyproject.toml", ".env", "setup.py", "Dockerfile", "Makefile"]
default_exclude_dirs = [".git", "__pycache__", "venv", "env", "node_modules", ".idea", ".vscode", ".mypy_cache", ".pytest_cache"]

include_extensions = config.get("include_extensions", default_extensions)
include_filenames = config.get("include_filenames", default_filenames)
exclude_dirs = config.get("exclude_dirs", default_exclude_dirs)


project_dir_var = tk.StringVar(value=config.get("project_dir", ""))
default_output = os.path.join(os.getcwd(), "project.md" if config.get("markdown", True) else "project.txt")
output_file_var = tk.StringVar(value=config.get("output_file", default_output))



# === ArgumentParser for extracting help. We create argparse here just for convenience of copy pasting any changes from compile.py ===
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--no_markdown", help="Disables the default, which is to format output as Markdown with code blocks, for better human readability.")
parser.add_argument("--no_tree", help="Disable project structure tree at top of output file.")
parser.add_argument("--open", help="Open the output file after generation.")
parser.add_argument("--normalize_eol", help="Convert all line endings to LF (\\n). Useful if you're operating between Windows and Linux.")
parser.add_argument("--max_size", help="Max file size (in bytes) to include. Default: 2MB.")
parser.add_argument("--min_lines", help="Min number of lines to include file.")

# === GUI State Variables ===
markdown_var = tk.BooleanVar(value=config.get("markdown", True))
tree_var = tk.BooleanVar(value=config.get("tree", True))
open_var = tk.BooleanVar(value=config.get("open", True))
normalize_eol_var = tk.BooleanVar(value=config.get("normalize_eol", False))
max_size_var = tk.StringVar(value=str(config.get("max_size", 2000000)))
min_lines_var = tk.StringVar(value=str(config.get("min_lines", 0)))

# === GUI Layout with Tooltips ===
tk.Label(root, text="Project Directory:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=project_dir_var, width=100).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_directory).grid(row=0, column=2)

tk.Label(root, text="Output File:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=output_file_var, width=100).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_output_file).grid(row=1, column=2)

cb1 = tk.Checkbutton(root, text="Markdown Format", variable=markdown_var)
cb1.grid(row=2, column=0, sticky="w")
Tooltip(cb1, parser._option_string_actions["--no_markdown"].help)

cb2 = tk.Checkbutton(root, text="Include Tree", variable=tree_var)
cb2.grid(row=2, column=1, sticky="w")
Tooltip(cb2, parser._option_string_actions["--no_tree"].help)

cb3 = tk.Checkbutton(root, text="Open in VSCode after", variable=open_var)
cb3.grid(row=3, column=0, sticky="w")
Tooltip(cb3, parser._option_string_actions["--open"].help)

cb4 = tk.Checkbutton(root, text="Normalize EOL (\\n)", variable=normalize_eol_var)
cb4.grid(row=3, column=1, sticky="w")
Tooltip(cb4, parser._option_string_actions["--normalize_eol"].help)

tk.Label(root, text="Max File Size (bytes):").grid(row=4, column=0, sticky="w")
entry1 = tk.Entry(root, textvariable=max_size_var)
entry1.grid(row=4, column=1)
Tooltip(entry1, parser._option_string_actions["--max_size"].help)

tk.Label(root, text="Min Lines:").grid(row=5, column=0, sticky="w")
entry2 = tk.Entry(root, textvariable=min_lines_var)
entry2.grid(row=5, column=1)
Tooltip(entry2, parser._option_string_actions["--min_lines"].help)

tk.Button(root, text="Compile Project", command=run_compilation, bg="green", fg="white").grid(row=6, column=0, columnspan=3, pady=10)


def create_editable_list(parent, label_text, items, default_items):
    frame = tk.LabelFrame(parent, text=label_text)
    listbox = tk.Listbox(frame, height=30, width=30)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack(side="left")

    control_frame = tk.Frame(frame)
    control_frame.pack(side="left", padx=5)

    entry = tk.Entry(control_frame, width=20)
    entry.pack()

    def add_item():
        val = entry.get().strip()
        if val and val not in listbox.get(0, tk.END):
            listbox.insert(tk.END, val)
            entry.delete(0, tk.END)

    def remove_selected():
        selection = listbox.curselection()
        for i in reversed(selection):
            listbox.delete(i)

    def reset_list():
        listbox.delete(0, tk.END)
        for item in default_items:
            listbox.insert(tk.END, item)

    tk.Button(control_frame, text="+", command=add_item).pack()
    tk.Button(control_frame, text="–", command=remove_selected).pack()
    tk.Button(control_frame, text="Reset", command=reset_list).pack(pady=(10, 0))

    return frame, lambda: list(listbox.get(0, tk.END)), lambda: listbox.get(0, tk.END) == tuple(default_items)


# Now build the 3 editable lists
edit_frame = tk.LabelFrame(root, text="Advanced: File Filters")
edit_frame.grid(row=7, column=0, columnspan=3, pady=10)

ext_frame, get_extensions, is_extensions_default = create_editable_list(edit_frame, "Include Extensions", include_extensions, default_extensions)
file_frame, get_filenames, is_filenames_default = create_editable_list(edit_frame, "Include Filenames", include_filenames, default_filenames)
dir_frame, get_exclude_dirs, is_exclude_default = create_editable_list(edit_frame, "Exclude Directories", exclude_dirs, default_exclude_dirs)
ext_frame.grid(row=0, column=0, padx=10)
file_frame.grid(row=0, column=1, padx=10)
dir_frame.grid(row=0, column=2, padx=10)




root.mainloop()