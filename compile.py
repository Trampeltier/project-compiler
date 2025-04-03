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

    # Create directory if it does not exist
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    
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

        

