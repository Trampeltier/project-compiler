<details open>
<summary>📁 Project Structure</summary>

```
├── compile.py (11 KB, 310 lines)
├── README.md (0 KB, 12 lines)
├── gui_launcher.py (9 KB, 269 lines)
└── compiler_config.json (0 KB, 10 lines)
```
</details>


<details>
<summary><a name="compile-py"></a>`compile.py` (11 KB, 310 lines)</summary>

````python
import os
import json
import shutil

INCLUDE_EXTENSIONS = {
    ".py", ".ipynb", ".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".rst",
    ".cpp", ".h", ".hpp", ".c", ".java", ".js", ".ts"
}
INCLUDE_FILENAMES = {
    "README", "README.md", "requirements.txt", "pyproject.toml", ".env", "setup.py", "Dockerfile" "Makefile"
}
EXCLUDE_DIRS = {
    ".git", "__pycache__", "venv", "env", "node_modules", ".idea", ".vscode", ".mypy_cache", ".pytest_cache"
}

EXT_TO_LANG = {
    ".py": "python",
    ".ipynb": "json",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".toml": "toml",
    ".ini": "ini",
    ".cfg": "ini",
    ".md": "markdown",
    ".txt": "",
    ".rst": "rst",
    ".js": "javascript",
    ".ts": "typescript",
    ".cpp": "cpp",
    ".c": "c",
    ".h": "cpp",
    ".hpp": "cpp",
    ".java": "java"
}

def is_included_file(filename):
    """
    Check if a file is included in the project summary.

    A file is included if its extension is in INCLUDE_EXTENSIONS or if its name starts with any of the
    strings in INCLUDE_FILENAMES (case-insensitive).

    Args:
        filename (str): The path to the file to check.

    Returns:
        bool: True if the file is included, False otherwise.
    """
    base = os.path.basename(filename)
    ext = os.path.splitext(base)[1]
    return (
        ext.lower() in INCLUDE_EXTENSIONS or
        any(base.lower().startswith(name.lower()) for name in INCLUDE_FILENAMES)
    )
    
    
import re
from collections import defaultdict

def slugify(text):
    """
    Slugify a string by replacing all non-alphanumeric characters with hyphens and lowercasing it.
    
    >>> slugify("Hello World!")
    'hello-world'
    >>> slugify("Foo-Bar?Baz")
    'foo-barbaz'
    """
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip("-")

def build_file_tree_with_info(paths, base_dir):
    """
    Build a nested dictionary representing a file tree structure and collect file information.

    Args:
        paths (list of str): List of file paths relative to the base directory.
        base_dir (str): The base directory to which the paths are relative.

    Returns:
        tuple: A tuple containing:
            - A nested dictionary representing the file tree structure.
            - A dictionary with file information where keys are file paths and values are
              dictionaries containing file size in kilobytes and line count.
    """

    tree = lambda: defaultdict(tree)
    file_info = {}

    root = tree()
    for rel_path in paths:
        abs_path = os.path.join(base_dir, rel_path)
        try:
            size = os.path.getsize(abs_path)
            with open(abs_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            line_count = len(lines)
        except:
            size = 0
            line_count = 0

        file_info[rel_path] = {
            "size_kb": size // 1024,
            "line_count": line_count
        }

        parts = rel_path.split(os.sep)
        current = root
        for part in parts:
            current = current[part]

    return root, file_info

def render_tree_markdown(tree_dict, file_info, prefix="", path_parts=[]):
    """
    Recursively render a file tree structure as a nested Markdown list.

    Args:
        tree_dict (defaultdict): A nested dictionary representing the file tree structure.
        file_info (dict): A dictionary with file information where keys are file paths and values are
                          dictionaries containing file size in kilobytes and line count.
        prefix (str, optional): An optional prefix to add to each line. Defaults to "".
        path_parts (list of str, optional): An optional list of path parts to build up the full path.
                                           Defaults to [].

    Returns:
        list of str: A list of strings representing the rendered file tree.
    """
    lines = []
    entries = list(tree_dict.items())
    for i, (key, subtree) in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        indent = prefix + connector
        path_parts_new = path_parts + [key]
        rel_path = os.path.join(*path_parts_new)

        if not subtree:  # it's a file
            info = file_info.get(rel_path, {})
            size = f"{info.get('size_kb', 0)} KB"
            lines_ = f"{info.get('line_count', 0)} lines"
            lines.append(f"{indent}{key} ({size}, {lines_})")
        else:  # it's a folder
            lines.append(f"{indent}{key}/")
            sub_prefix = prefix + ("    " if is_last else "│   ")
            lines.extend(render_tree_markdown(subtree, file_info, sub_prefix, path_parts_new))
    return lines




def compile_project(directory, output_filename="compiled_project.txt", as_markdown=False, include_tree=True, max_size=2_000_000, min_lines=0, normalize_eol=False):
    output_lines = []
    included_files = []
    file_info = {}
    
    # First pass: walk files and collect included ones
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for file in files:
            if file.startswith('.'):
                continue
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, directory)
            rel_path = rel_path.replace("\\", "/")

            
            if is_included_file(filepath):
                included_files.append(rel_path)

                # Precompute file info
                try:
                    size = os.path.getsize(filepath)
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    file_info[rel_path] = {
                        "size_kb": size // 1024,
                        "line_count": len(lines),
                        "content": "".join(lines)
                    }
                except Exception as e:
                    print(f"Skipping {rel_path} due to error: {e}")
        
    # Generate and prepend tree
    if include_tree and as_markdown:
        tree_data, file_info = build_file_tree_with_info(included_files, directory)
        tree_lines = render_tree_markdown(tree_data, file_info)
        tree_block = [
            "<details open>",
            "<summary>📁 Project Structure</summary>",
            "",
            "```",
            *tree_lines,
            "```",
            "</details>",
            ""
        ]
        output_lines = tree_block + output_lines

    # Second pass: walk files and collect content, with optional markdown formatting.
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for file in files:
            if file.startswith('.'):
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, directory)
            if is_included_file(filepath):
                
                try:
                    size = os.path.getsize(filepath)
                    if size > max_size:
                        print(f"Skipping content of {filepath} due to size being bigger than {max_size} bytes")
                        continue

                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    if args.normalize_eol:
                        content = content.replace('\r\n', '\n').replace('\r', '\n')


                    if as_markdown:
                        ext = os.path.splitext(file)[1].lower()
                        lang = EXT_TO_LANG.get(ext, "")

                        def get_safe_fence(content: str) -> str:
                            import re
                            matches = re.findall(r"`{3,}", content)
                            max_len = max((len(m) for m in matches), default=2)
                            return "`" * (max_len + 1)

                        fence = get_safe_fence(content)
                        slug = slugify(rel_path)
                        info = file_info.get(rel_path, {})
                        size = f"{info.get('size_kb', 0)} KB"
                        lines_ = f"{info.get('line_count', 0)} lines"
                        if info.get('line_count', 0) < min_lines:
                            print(f"Skipping {filepath} due to having fewer than {min_lines} lines")
                            continue
                        
                        output_lines.append(
                            f"\n<details>\n<summary><a name=\"{slug}\"></a>`{rel_path}` ({size}, {lines_})</summary>\n\n"
                            f"{fence}{lang}\n{content}\n{fence}\n</details>\n"
                        )

                    else:
                        output_lines.append(f"\n\n# === {rel_path} ===\n{content}")
                except Exception as e:
                    print(f"Skipping {rel_path} due to error: {e}")

    
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(output_lines))
        print(f"Compiled {len(included_files)} files into {output_filename}")



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compile human-readable project files into one summary file.")
    parser.add_argument("directory", help="Path to the root of the project directory")
    parser.add_argument("--output", default="compiled_project.txt", help="Output filename")
    parser.add_argument("--no_markdown", action="store_true", help="Disables the default, which is to format output as Markdown with code blocks, for better human readability.")
    parser.add_argument("--no_tree", action="store_true", help="Disable project structure tree at top of output file.")
    parser.add_argument("--max_size", type=int, default=2_000_000, help="Max file size (in bytes) to include. Default: 2MB.")
    parser.add_argument("--min_lines", type=int, default=0, help="Min number of lines to include file.")
    parser.add_argument("--open", action="store_true", help="Open the output file after generation.")
    parser.add_argument("--normalize_eol", action="store_true", help="Convert all line endings to LF (\\n). Useful if you're operating between Windows and Linux.")
    parser.add_argument("--config_file", help="Path to a JSON config file containing include/exclude rules.", default="compiler_config.json")

    args = parser.parse_args()
    
    if args.config_file:
        try:
            with open(args.config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
            INCLUDE_EXTENSIONS = set(config.get("include_extensions", list(INCLUDE_EXTENSIONS)))
            INCLUDE_FILENAMES = set(config.get("include_filenames", list(INCLUDE_FILENAMES)))
            EXCLUDE_DIRS = set(config.get("exclude_dirs", list(EXCLUDE_DIRS)))
            print(f"Loaded filters from config: {args.config_file}")
        except Exception as e:
            print(f"Failed to load config file: {e}")
        
        
        
    if not args.no_markdown and not args.output.endswith(".md"):
        args.output += ".md"
    compile_project(args.directory, args.output, as_markdown=not args.no_markdown, include_tree=not args.no_tree,
                    max_size=args.max_size, min_lines=args.min_lines, normalize_eol=args.normalize_eol)
    
    # After writing the file:
    if args.open:
        if shutil.which("code") or os.name == "nt":  # lenient check
            try:
                import subprocess
                subprocess.run(["code", args.output], check=True)
            except Exception as e:
                print("Could not open in VS Code. Falling back to web browser.")
                import webbrowser
                webbrowser.open(args.output)
        else:
            print("VS Code CLI not found. Falling back to web browser.")
            import webbrowser
            webbrowser.open(args.output)

        


````
</details>


<details>
<summary><a name="readme-md"></a>`README.md` (0 KB, 12 lines)</summary>

````markdown
This repo provides a simple tool to compile all important files in your project into a single Markdown or text file — perfect for sharing with an LLM.

It includes a visual structure tree and collapsible code sections for easy navigation.

Use the CLI (`compile.py`) or the convenient GUI (`gui_launcher.py`) which wraps it.

As an example, see `this_repo.md`, which showcases this tool applied this very repo itself.

Just clone the repo and run:
```bash
python3 gui_launcher.py
```
````
</details>


<details>
<summary><a name="gui-launcher-py"></a>`gui_launcher.py` (9 KB, 269 lines)</summary>

```python
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
```
</details>


<details>
<summary><a name="compiler-config-json"></a>`compiler_config.json` (0 KB, 10 lines)</summary>

```json
{
  "project_dir": "/home/vinci/Documents/Repos/project-compiler/",
  "output_file": "/home/vinci/Documents/Repos/project-compiler/this_repo.md",
  "markdown": true,
  "tree": true,
  "open": true,
  "normalize_eol": false,
  "max_size": 2000000,
  "min_lines": 0
}
```
</details>
