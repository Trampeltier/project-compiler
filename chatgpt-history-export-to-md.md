<details open>
<summary>📁 Project Structure</summary>

```
├── README.md (4 KB, 88 lines)
├── pyproject.toml (1 KB, 60 lines)
├── playground.ipynb (6 KB, 218 lines)
├── tests/
│   ├── __init__.py (0 KB, 1 lines)
│   ├── test_conversation.py (2 KB, 101 lines)
│   ├── test_mapping.py (0 KB, 29 lines)
│   ├── test_message.py (1 KB, 42 lines)
│   └── mocks.py (2 KB, 120 lines)
├── js/
│   ├── how_to_use.md (1 KB, 30 lines)
│   ├── script.js (5 KB, 180 lines)
│   └── bookmarklet.js (4 KB, 1 lines)
├── demo/
│   └── Fibonacci.md (3 KB, 134 lines)
└── convoviz/
    ├── __init__.py (0 KB, 5 lines)
    ├── cli.py (3 KB, 99 lines)
    ├── long_runs.py (2 KB, 93 lines)
    ├── configuration.py (3 KB, 125 lines)
    ├── utils.py (6 KB, 274 lines)
    ├── __main__.py (0 KB, 5 lines)
    ├── data_analysis.py (3 KB, 119 lines)
    ├── assets/
    │   └── colormaps.txt (0 KB, 16 lines)
    └── models/
        ├── _conversation_set.py (6 KB, 191 lines)
        ├── __init__.py (0 KB, 8 lines)
        ├── _conversation.py (8 KB, 289 lines)
        ├── _message.py (2 KB, 89 lines)
        └── _node.py (2 KB, 74 lines)
```
</details>


<details>
<summary><a name="readme-md"></a>`README.md` (4 KB, 88 lines)</summary>

````markdown
# Convoviz 📊: Visualize your entire ChatGPT data !

Convert your ChatGPT history into well-formatted Markdown files. Additionally, visualize your data with word clouds 🔡☁️, view your prompt history graphs 📈, and access all your custom instructions 🤖 in a single location.

![GitHub last commit](https://img.shields.io/github/last-commit/mohamed-chs/chatgpt-history-export-to-md)
![GitHub issues](https://img.shields.io/github/issues/mohamed-chs/chatgpt-history-export-to-md)

## Features

- **YAML Headers**: Optional and included by default.
- **Track message versions**: prompt/response edits included.
- **Code Interpreter**: Environment code blocks and execution results.
- **Data Visualizations**: Word clouds, graphs, and more.
- **Custom Instructions**: All your custom instructions in one JSON file.

See examples [here](demo).

## How to Use 📖

### 1. Export Your ChatGPT Data 🗂

- Sign in at [chat.openai.com](https://chat.openai.com).
- Navigate: Profile Name (bottom left) -> **Settings** -> **Data controls** -> **Export** -> **Confirm export**.
- Await email from OpenAI and download the `.zip` file.

### 2. Install the tool 🛠

Open a terminal or command prompt and run:

```bash
pip install convoviz
```

to install the package.

### 3. Run the Script 🏃‍♂️

With the package installed, run the following command in your terminal:

```bash
python -m convoviz
```

Next, follow the instructions displayed and choose your desired options, the script will handle the rest.

### 4. Check the Output 🎉

And that's it! After running the script, head over to the output folder to see your nice word clouds, graphs, and neatly formatted Markdown files. Enjoy !

**Tweet Your Discoveries**:

[![Tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fyourusername%2Fyourrepository)](https://twitter.com/intent/tweet?text=So%2C%20this%20is%20what%20my%20entire%20ChatGPT%20history%20looks%20like%20...%0D%0A%0D%0Ahttp%3A%2F%2Fbit.ly%2F3ZuHCCK)

### How to add new conversations ➕

See [How to use the JS script](js/how_to_use.md) for instructions on how to download new conversations.

## Share Your Feedback! 💌

I hope you find this tool useful. I'm continuously looking to improve on this, but I need your help for that.

Whether you're a tech wizard or you're new to all this (especially if you're new to all this), I'd love to hear about your journey with the tool. Found a quirk? Have a suggestion? Or just want to send some good vibes? I'm all ears!

**Here's how you can share your thoughts:**

1. **GitHub Issues**: For more specific feedback or if you've stumbled upon a bug, please open an [issue](https://github.com/mohamed-chs/chatgpt-history-export-to-md/issues). This helps me track and address them effectively.

2. **GitHub Discussions**: If you just want to share your general experience, have a suggestion, or maybe a cool idea for a new feature, jump into the [discussions](https://github.com/mohamed-chs/chatgpt-history-export-to-md/discussions) page. It's a more casual space where we can chat.

And if you've had a great experience, consider giving the project a star ⭐. It keeps me motivated and helps others discover it!

Thank you for being awesome! 🌟

## Notes

This project requires Python 3.8.7 or higher if on Windows. See [known issue](https://github.com/prompt-toolkit/python-prompt-toolkit/issues/1023#issue-534396318)

This is just a small thing I coded to help me see my convos in beautiful markdown, in [Obsidian](https://obsidian.md/) (my go-to note-taking app).

I wasn't a fan of the clunky, and sometimes paid, browser extensions.

It was also a great opportunity to learn more about Python and type annotations. I had mypy, pyright, and ruff all on strict mode, 'twas fun.

It also works as package, so you can **import** it in your own projects, and use the models and functions as you wish. I need to add more documentation for that tho. Feel free to reach out if you need help.

I'm working on automating it to add new conversations and updating old ones. Had some luck with a JavaScript bookmarklet, still ironing it out tho. Shouldn't take long.

> for an older version with zero dependencies, see https://github.com/mohamed-chs/chatgpt-history-export-to-md/tree/fe13a701fe8653c9f946b1e12979ce3bfe7104b8.

````
</details>


<details>
<summary><a name="pyproject-toml"></a>`pyproject.toml` (1 KB, 60 lines)</summary>

```toml
[tool.poetry]
name = "convoviz"
version = "0.1.7"
description = "Get analytics and visualizations on your ChatGPT data !"
authors = ["Mohamed Cheikh Sidiya <mohamedcheikhsidiya77@gmail.com>"]
license = "MIT"
readme = "README.md"
repository = "https://github.com/mohamed-chs/chatgpt-history-export-to-md"
keywords = [
    "markdown",
    "advanced-data-analysis",
    "json",
    "zip",
    "openai",
    "chatgpt",
    "bookmarklet",
    "obsidian-md",
    "code-interpreter",
]

[tool.poetry.dependencies]
python = "^3.9"
questionary = "^2.0.1"
tqdm = "^4.66.1"
matplotlib = "^3.8.1"
nltk = "^3.8.1"
wordcloud = "^1.9.2"
pydantic = "^2.4.2"
orjson = "^3.9.10"

[tool.poetry.group.dev.dependencies]
ruff = "^0.1.4"
pytest = "^7.4.3"
mypy = "^1.6.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.ruff]
select = ["ALL"]
ignore = [
    "ANN101", # missing-type-self
    "ANN102", # missing-type-cls
    "TD002",  # missing-todo-author
    "TD003",  # missing-todo-link
]
extend-include = ["*.ipynb"]

[tool.ruff.per-file-ignores]
"convoviz/cli.py" = ["T201"]   # print
"*.ipynb" = ["T201"]           # print
"tests/*" = ["S101", "SLF001"] # assert , private-member-access


[tool.mypy]
strict = true
enable_incomplete_feature = ["Unpack"]

```
</details>


<details>
<summary><a name="playground-ipynb"></a>`playground.ipynb` (6 KB, 218 lines)</summary>

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Testing Playground\n",
    "\n",
    "You've probably noticed this project lacks a unit testing set-up. Honestly, I found unit testing tricky for this and felt visual inspections of outputs, like markdowns or visualizations, were generally more trustworthy.\n",
    "\n",
    "But I get the worry of accidentally breaking things when contributing code. So, I made this notebook to help with that. It's a work in progress, aimed at letting you easily see specific outputs of interest for smoother development.\n",
    "\n",
    "Previously, my basic testing meant using a `test.py` file to generate a few markdowns and then checking them manually. Or, for a deeper look, I'd run the `cli.py` and wait a while to see everything, which isn't quick on my laptop.\n",
    "\n",
    "This notebook aims to streamline that process, letting you test and inspect targeted parts of the output without the fear of breaking things.\n",
    "\n",
    "**Before you begin, it's recommended that you put the `conversations.json` file close by, like in a `./data/` folder.**\n",
    "\n",
    "**Make sure to restart the kernel and clear all outputs before committing changes, to ensure personal data isn't accidentally included.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"Playground for testing and debugging.\"\"\"\n",
    "\n",
    "from __future__ import annotations\n",
    "\n",
    "from pathlib import Path\n",
    "from random import choice\n",
    "from typing import Callable\n",
    "\n",
    "from convoviz.models import Conversation, ConversationSet\n",
    "from convoviz.utils import colormaps, font_names\n",
    "\n",
    "convos_path = Path(\"data\") / \"conversations.json\"  # adjust path if needed\n",
    "output_path = Path(\"output\")\n",
    "output_path.mkdir(exist_ok=True)\n",
    "\n",
    "collection = ConversationSet.from_json(convos_path)\n",
    "\n",
    "\n",
    "def clear_output() -> None:\n",
    "    \"\"\"Clear output folder.\"\"\"\n",
    "    for file in output_path.glob(\"*\"):\n",
    "        file.unlink()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "clear_output()  # run this whenever you want to clear the output folder"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Markdown"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Utility function to get statistics and print conversations based on a criteria\n",
    "def get_top_convos(\n",
    "    attr_func: Callable[[Conversation], int],\n",
    "    description: str,\n",
    "    count: int = 5,\n",
    ") -> None:\n",
    "    \"\"\"Get statistics and save top conversations based on a criteria.\"\"\"\n",
    "    stats = [attr_func(c) for c in collection.array]\n",
    "    avg_stat = sum(stats) / len(stats)\n",
    "    median_stat = sorted(stats)[len(stats) // 2]\n",
    "    max_stat = max(stats)\n",
    "\n",
    "    print(\n",
    "        f\"Average {description}: {avg_stat}\\n\"\n",
    "        f\"Median {description}: {median_stat}\\n\"\n",
    "        f\"Max {description}: {max_stat}\\n\",\n",
    "    )\n",
    "\n",
    "    sorted_convos = sorted(\n",
    "        collection.array,\n",
    "        key=attr_func,\n",
    "        reverse=True,\n",
    "    )\n",
    "\n",
    "    for convo in sorted_convos[:count]:\n",
    "        print(\n",
    "            f\"id: {convo.conversation_id}\\n\"\n",
    "            f\"title: {convo.title}\\n\"\n",
    "            f\"{description}: {attr_func(convo)}\\n\",\n",
    "        )\n",
    "        file_path = output_path / f\"{convo.title}.md\"\n",
    "        convo.save(file_path)\n",
    "        print(f\"saved to '{file_path}'\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_top_convos(lambda c: c.leaf_count, \"leaf count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_top_convos(lambda c: c.message_count(\"assistant\"), \"message count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_top_convos(lambda c: len(c.content_types), \"content type count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_top_convos(lambda c: len(c.plugins), \"plugin count\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Visualization"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Word Clouds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "week_groups = collection.group_by_week()\n",
    "week = choice(list(week_groups.keys()))\n",
    "\n",
    "sample_conv_set = week_groups[week]\n",
    "\n",
    "font_name = choice(font_names())\n",
    "font_path = f\"convoviz/assets/fonts/{font_name}.ttf\"\n",
    "colormap = choice(colormaps())\n",
    "print(f\"font: {font_name}\\ncolormap: {colormap}\\n\")\n",
    "\n",
    "img = sample_conv_set.wordcloud(font_path=font_path, colormap=colormap)\n",
    "img.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Graphs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = sample_conv_set.week_barplot(\"Prompts per day\")\n",
    "fig.savefig(output_path / \"week_barplot.png\")  # pyright: ignore[reportUnknownMemberType]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

```
</details>


<details>
<summary><a name="tests-init-py"></a>`tests/__init__.py` (0 KB, 1 lines)</summary>

```python
"""Tests for the project."""

```
</details>


<details>
<summary><a name="tests-test-conversation-py"></a>`tests/test_conversation.py` (2 KB, 101 lines)</summary>

```python
"""Tests for the Conversation class."""

# pyright: reportUnknownVariableType=false
# pyright: reportGeneralTypeIssues=false

from __future__ import annotations

from convoviz.models import Conversation

from .mocks import (
    ASSISTANT_MESSAGE_TEXT_111,
    CONVERSATION_111,
    CONVERSATION_ID_111,
    DATETIME_111,
    MESSAGE_COUNT_111,
    TITLE_111,
    USER_MESSAGE_TEXT_111,
)

conversation = Conversation(**CONVERSATION_111)


def test_leaf_count() -> None:
    """Test leaf_count method."""
    assert conversation.leaf_count == 1


def test_chat_link() -> None:
    """Test chat_link method."""
    assert conversation.url == f"https://chat.openai.com/c/{CONVERSATION_ID_111}"


def test_content_types() -> None:
    """Test content_types method."""
    assert set(conversation.content_types) == {"text"}


def test_message_count() -> None:
    """Test message_count method."""
    assert conversation.message_count("user", "assistant") == MESSAGE_COUNT_111


def test_entire_author_text() -> None:
    """Test entire_author_text method."""
    assert conversation.plaintext("user") == USER_MESSAGE_TEXT_111
    assert conversation.plaintext("assistant") == ASSISTANT_MESSAGE_TEXT_111


def test_author_message_timestamps() -> None:
    """Test author_message_timestamps method."""
    assert conversation.timestamps("user") == [
        DATETIME_111.timestamp(),
    ]


def test_model_slug() -> None:
    """Test model_slug method."""
    assert conversation.model == "gpt-4"


def test_used_plugins() -> None:
    """Test used_plugins method."""
    assert len(conversation.plugins) == 0


def test_yaml_header() -> None:
    """Test yaml_header method."""
    yaml_header = conversation.yaml
    assert "---" in yaml_header
    assert f"title: {TITLE_111}" in yaml_header


def test_to_markdown() -> None:
    """Test to_markdown method."""
    markdown = conversation.markdown
    assert "---" in markdown
    assert "# Me" in markdown
    assert USER_MESSAGE_TEXT_111 in markdown
    assert "# ChatGPT" in markdown
    assert ASSISTANT_MESSAGE_TEXT_111 in markdown


def test_start_of_year() -> None:
    """Test start_of_year method."""
    assert conversation.year_start.year == DATETIME_111.year
    assert conversation.year_start.month == 1
    assert conversation.year_start.day == 1


def test_start_of_month() -> None:
    """Test start_of_month method."""
    assert conversation.month_start.year == DATETIME_111.year
    assert conversation.month_start.month == DATETIME_111.month
    assert conversation.month_start.day == 1


def test_start_of_week() -> None:
    """Test start_of_week method."""
    assert conversation.week_start.year == DATETIME_111.year
    assert conversation.week_start.month == DATETIME_111.month
    assert conversation.week_start.day == DATETIME_111.day - DATETIME_111.weekday()

```
</details>


<details>
<summary><a name="tests-test-mapping-py"></a>`tests/test_mapping.py` (0 KB, 29 lines)</summary>

```python
"""Tests for the Node class."""

# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false

from __future__ import annotations

from convoviz.models import Conversation

from .mocks import CONVERSATION_111

nodes = Conversation(**CONVERSATION_111).node_mapping


def test_nodes_from_mapping() -> None:
    """Test nodes_from_mapping method."""
    assert "user_node_111" in nodes
    assert "assistant_node_111" in nodes
    assert nodes["root_node_111"].children_nodes[0] == nodes["system_node_111"]


def test_header_with_root_sys_and_user() -> None:
    """Test header method with root, system and user nodes."""
    user_node = nodes["user_node_111"]
    header = user_node.header

    assert "user_node_111" in header
    assert "parent ⬆️" in header
    assert "# Me" in header

```
</details>


<details>
<summary><a name="tests-test-message-py"></a>`tests/test_message.py` (1 KB, 42 lines)</summary>

```python
"""Tests for the Message class."""

# pyright: reportGeneralTypeIssues=false
# pyright: reportUnknownVariableType=false

from __future__ import annotations

from convoviz.models import Message

from .mocks import ASSISTANT_MESSAGE_111, USER_MESSAGE_111

user_message = Message(**USER_MESSAGE_111)
assistant_message = Message(**ASSISTANT_MESSAGE_111)


def test_author_role() -> None:
    """Test author_role method."""
    assert user_message.author.role == "user"


def test_author_header() -> None:
    """Test author_header method."""
    assert user_message.header == "# Me"

    assert assistant_message.header == "# ChatGPT"


def test_content_text() -> None:
    """Test content_text method."""
    assert user_message.text == "user message 111"

    assert assistant_message.text == "assistant message 111"


def test_content_type() -> None:
    """Test content_type method."""
    assert user_message.content.content_type == "text"


def test_model_slug() -> None:
    """Test model_slug method."""
    assert assistant_message.metadata.model_slug == "gpt-4"

```
</details>


<details>
<summary><a name="tests-mocks-py"></a>`tests/mocks.py` (2 KB, 120 lines)</summary>

```python
"""Mocks for testing."""

# pyright: reportUnknownVariableType=false

from __future__ import annotations

from datetime import datetime, timedelta, timezone

DATETIME_111 = datetime(
    year=2023,
    month=7,
    day=29,
    hour=8,
    minute=0,
    second=0,
    tzinfo=timezone.utc,
)

DATETIME_112 = DATETIME_111 + timedelta(minutes=5)

SYSTEM_MESSAGE_111 = {
    "id": "system_node_111",
    "author": {"role": "system", "metadata": {}},
    "create_time": DATETIME_111.timestamp(),
    "update_time": DATETIME_111.timestamp(),
    "content": {"content_type": "text", "parts": ["system message 111"]},
    "status": "finished_successfully",
    "end_turn": True,
    "weight": 1.0,
    "metadata": {"model_slug": "gpt-4"},
    "recipient": "all",
}

USER_MESSAGE_TEXT_111 = "user message 111"

USER_MESSAGE_111 = {
    "id": "user_node_111",
    "author": {"role": "user", "metadata": {}},
    "create_time": DATETIME_111.timestamp(),
    "update_time": DATETIME_111.timestamp(),
    "content": {"content_type": "text", "parts": [USER_MESSAGE_TEXT_111]},
    "status": "finished_successfully",
    "end_turn": True,
    "weight": 1.0,
    "metadata": {"model_slug": "gpt-4"},
    "recipient": "all",
}

ASSISTANT_MESSAGE_TEXT_111 = "assistant message 111"

ASSISTANT_MESSAGE_111 = {
    "id": "assistant_node_111",
    "author": {"role": "assistant", "metadata": {}},
    "create_time": DATETIME_112.timestamp(),
    "update_time": DATETIME_112.timestamp(),
    "content": {"content_type": "text", "parts": [ASSISTANT_MESSAGE_TEXT_111]},
    "status": "finished_successfully",
    "end_turn": True,
    "weight": 1.0,
    "metadata": {"model_slug": "gpt-4"},
    "recipient": "all",
}


ROOT_NODE_111 = {
    "id": "root_node_111",
    "message": None,
    "parent": None,
    "children": ["system_node_111"],
}

SYSTEM_NODE_111 = {
    "id": "system_node_111",
    "message": SYSTEM_MESSAGE_111,
    "parent": None,
    "children": ["user_node_111"],
}

USER_NODE_111 = {
    "id": "user_node_111",
    "message": USER_MESSAGE_111,
    "parent": None,
    "children": ["assistant_node_111"],
}

ASSISTANT_NODE_111 = {
    "id": "assistant_node_111",
    "message": ASSISTANT_MESSAGE_111,
    "parent": None,
    "children": [],
}

MAPPING_111 = {
    "root_node_111": ROOT_NODE_111,
    "system_node_111": SYSTEM_NODE_111,
    "user_node_111": USER_NODE_111,
    "assistant_node_111": ASSISTANT_NODE_111,
}

TITLE_111 = "conversation 111"
CONVERSATION_ID_111 = "conversation_111"
TEMPLATE_ID_111 = "template_111"
PLUGIN_IDS_111 = []
MODERATION_RESULTS_111 = []

CONVERSATION_111 = {
    "title": TITLE_111,
    "create_time": DATETIME_111.timestamp(),
    "update_time": DATETIME_112.timestamp(),
    "mapping": MAPPING_111,
    "moderation_results": MODERATION_RESULTS_111,
    "current_node": ASSISTANT_NODE_111["id"],
    "plugin_ids": PLUGIN_IDS_111,
    "conversation_id": CONVERSATION_ID_111,
    "conversation_template_id": TEMPLATE_ID_111,
    "id": CONVERSATION_ID_111,
}

# based on the above
MESSAGE_COUNT_111 = 2

```
</details>


<details>
<summary><a name="js-how-to-use-md"></a>`js/how_to_use.md` (1 KB, 30 lines)</summary>

```markdown
## How to use the JS script

- Go to the [ChatGPT website](https://chat.openai.com/)
- Open the browser developer console (F12 on Chrome, Ctrl+Shift+I on Firefox)
- Then, copy-paste [this code](script.js) and hit 'Enter'
- A small UI widget should pop up in the bottom right, choose the number of conversations you want to download and click "Start Download". Now wait for the download to finish.

Now your conversations should be in a JSON file named something like "chatgpt_bookmarklet_download.json".

Alternatively, you can create a bookmarklet with the code in [this file](bookmarklet.js) and click it when you're on the ChatGPT website. It will do the same thing as the above steps.

(You should refresh the page after the download finishes, to clear the UI widget and the console logs.)

Now, if you run the `cli.py` script, it should recognize the new downloaded json file and add the conversations to the ones from the OpenAI export, that way ALL the conversations are converted to markdown files, as well as the other data visualizations stuff.

This is a very rudimentary js script, and it needs more error handling. I've tried it on Chrome, and it works so far.
Could break at anytime if OpenAI changes their data permissions or the `/backend-api/` API.

Feel free to modify the script to your liking. Would also appreciate sharing the modified version with others here via a PR.

### still working on

- [x] add support to add new conversations to the Markdown output folder
- [x] update old ones
- [ ] more seamless api rate limit handling (currently just pauses for a minute after ~50 chat downloads)
- [ ] update the data analysis and visualization
- [ ] better widget UI (add error messages and progress and such,
      so you can close the dev console and still be kept informed on the download process)
- [ ] add instructions on how to create a bookmarklet
- [ ] more todos ...

```
</details>


<details>
<summary><a name="js-script-js"></a>`js/script.js` (5 KB, 180 lines)</summary>

```javascript
// --- CSS / UI definitions ---

const styles = {
  toggleUI: `
      position: fixed; 
      bottom: 20px; 
      right: 20px; 
      padding: 10px; 
      background-color: #007BFF; 
      border: none; 
      border-radius: 50%; 
      color: white; 
      font-weight: bold; 
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25); 
      cursor: pointer; 
      z-index: 10000;
  `,
  downloadWidget: `
      position: fixed;
      bottom: 10px;
      right: 10px;
      background: #fff;
      border: 1px solid #ccc;
      padding: 20px;
      border-radius: 10px;
      z-index: 9999;
      width: 300px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  `,
};

const toggleUIHTML = `
<button id="toggle-openai-ui" style="${styles.toggleUI}">⏬</button>
`;

const uiHTML = `
<div id="openai-download-widget" style="${styles.downloadWidget}">
  <div style="margin-bottom: 15px">
    <label for="numConversations" style="display: block; margin-bottom: 5px; font-weight: 600">Number of conversations:</label>
    <input type="number" id="numConversations" value="50" style="width: 100%; padding: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" />
  </div>
  <div style="margin-bottom: 15px">
    <label for="openai-download-progress" style="display: block; margin-bottom: 5px; font-weight: 600">Download Progress:</label>
    <progress id="openai-download-progress" value="0" max="100" style="width: 100%; height: 15px; border-radius: 5px"></progress>
  </div>
  <div style="text-align: left">
    <button id="openai-start-download" style="padding: 10px 15px; background-color: #007bff; color: #fff; border: none; border-radius: 5px; cursor: pointer;">Start Download</button>
  </div>
</div>
`;

// Append UI components
document.body.insertAdjacentHTML("beforeend", toggleUIHTML + uiHTML);

// --- Utility functions ---

const toggleUIVisibility = () => {
  const uiWidget = document.getElementById("openai-download-widget");
  uiWidget.style.display = uiWidget.style.display === "none" ? "block" : "none";
};

function constructUrlWithParams(baseUrl, params) {
  const url = new URL(baseUrl);
  Object.keys(params).forEach((key) =>
    url.searchParams.append(key, params[key])
  );
  return url.toString();
}

// --- Event Listeners ---

document
  .getElementById("toggle-openai-ui")
  .addEventListener("click", toggleUIVisibility);
document
  .getElementById("openai-start-download")
  .addEventListener("click", async () => {
    const numConversations = parseInt(
      document.getElementById("numConversations").value,
      10
    );

    if (numConversations && numConversations > 0) {
      document.getElementById("openai-start-download").disabled = true;
      try {
        await downloadConversationsAsJson(numConversations);
        console.log("Download completed.");
      } catch (error) {
        console.error("An error occurred:", error);
      }
      document.getElementById("openai-start-download").disabled = false;
    } else {
      alert("Please enter a valid number of conversations.");
    }
  });

// --- Main functionality ---

const conversationsPerRequest = 50;
const delay = 63000;

async function fetchData(url, headers = {}) {
  try {
    const response = await fetch(url, { headers });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error fetching data from ${url}:`, error);
    throw error;
  }
}

async function fetchAccessToken() {
  const data = await fetchData("https://chat.openai.com/api/auth/session");
  return data.accessToken;
}

async function fetchConversationsData(accessToken, limit, offset) {
  const baseUrl = "https://chat.openai.com/backend-api/conversations";
  const url = constructUrlWithParams(baseUrl, {
    offset: offset,
    limit: limit,
    order: "updated",
  });
  const data = await fetchData(url, { Authorization: `Bearer ${accessToken}` });
  return data.items;
}

async function fetchConversationData(accessToken, conversationId) {
  const url = `https://chat.openai.com/backend-api/conversation/${conversationId}`;
  return fetchData(url, { Authorization: `Bearer ${accessToken}` });
}

async function downloadConversationsAsJson(numConversations) {
  const conversationsArray = [];
  const accessToken = await fetchAccessToken();

  const numRequests = Math.ceil(numConversations / conversationsPerRequest);
  for (let i = 0; i < numRequests; i++) {
    const offset = i * conversationsPerRequest;
    const limit =
      i === numRequests - 1
        ? numConversations - offset
        : conversationsPerRequest;

    const conversationsData = await fetchConversationsData(
      accessToken,
      limit,
      offset
    );
    for (let j = 0; j < conversationsData.length; j++) {
      const conversation = conversationsData[j];
      const conversationData = await fetchConversationData(
        accessToken,
        conversation.id
      );
      conversationsArray.push(conversationData);

      const progress =
        ((i * conversationsPerRequest + j + 1) / numConversations) * 100;
      document.getElementById("openai-download-progress").value = progress;
    }

    if (i < numRequests - 1) {
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }

  const content = new Blob([JSON.stringify(conversationsArray)], {
    type: "application/json",
  });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(content);
  a.download = "chatgpt_bookmarklet_download.json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

```
</details>


<details>
<summary><a name="js-bookmarklet-js"></a>`js/bookmarklet.js` (4 KB, 1 lines)</summary>

```javascript
javascript:const styles={toggleUI:"\n      position: fixed; \n      bottom: 20px; \n      right: 20px; \n      padding: 10px; \n      background-color: #007BFF; \n      border: none; \n      border-radius: 50%; \n      color: white; \n      font-weight: bold; \n      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25); \n      cursor: pointer; \n      z-index: 10000;\n  ",downloadWidget:"\n      position: fixed;\n      bottom: 10px;\n      right: 10px;\n      background: #fff;\n      border: 1px solid #ccc;\n      padding: 20px;\n      border-radius: 10px;\n      z-index: 9999;\n      width: 300px;\n      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);\n  "},toggleUIHTML=`\n<button id="toggle-openai-ui" style="${styles.toggleUI}">⏬</button>\n`,uiHTML=`\n<div id="openai-download-widget" style="${styles.downloadWidget}">\n  <div style="margin-bottom: 15px">\n    <label for="numConversations" style="display: block; margin-bottom: 5px; font-weight: 600">Number of conversations:</label>\n    <input type="number" id="numConversations" value="50" style="width: 100%; padding: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" />\n  </div>\n  <div style="margin-bottom: 15px">\n    <label for="openai-download-progress" style="display: block; margin-bottom: 5px; font-weight: 600">Download Progress:</label>\n    <progress id="openai-download-progress" value="0" max="100" style="width: 100%; height: 15px; border-radius: 5px"></progress>\n  </div>\n  <div style="text-align: left">\n    <button id="openai-start-download" style="padding: 10px 15px; background-color: #007bff; color: #fff; border: none; border-radius: 5px; cursor: pointer;">Start Download</button>\n  </div>\n</div>\n`;document.body.insertAdjacentHTML("beforeend",toggleUIHTML+uiHTML);const toggleUIVisibility=()=>{const o=document.getElementById("openai-download-widget");o.style.display="none"===o.style.display?"block":"none"};function constructUrlWithParams(o,e){const t=new URL(o);return Object.keys(e).forEach((o=>t.searchParams.append(o,e[o]))),t.toString()}document.getElementById("toggle-openai-ui").addEventListener("click",toggleUIVisibility),document.getElementById("openai-start-download").addEventListener("click",(async()=>{const o=parseInt(document.getElementById("numConversations").value,10);if(o&&o>0){document.getElementById("openai-start-download").disabled=!0;try{await downloadConversationsAsJson(o),console.log("Download completed.")}catch(o){console.error("An error occurred:",o)}document.getElementById("openai-start-download").disabled=!1}else alert("Please enter a valid number of conversations.")}));const conversationsPerRequest=50,delay=63e3;async function fetchData(o,e={}){try{const t=await fetch(o,{headers:e});if(!t.ok)throw new Error(`HTTP error! status: ${t.status}`);return await t.json()}catch(e){throw console.error(`Error fetching data from ${o}:`,e),e}}async function fetchAccessToken(){return(await fetchData("https://chat.openai.com/api/auth/session")).accessToken}async function fetchConversationsData(o,e,t){const n=constructUrlWithParams("https://chat.openai.com/backend-api/conversations",{offset:t,limit:e,order:"updated"});return(await fetchData(n,{Authorization:`Bearer ${o}`})).items}async function fetchConversationData(o,e){return fetchData(`https://chat.openai.com/backend-api/conversation/${e}`,{Authorization:`Bearer ${o}`})}async function downloadConversationsAsJson(o){const e=[],t=await fetchAccessToken(),n=Math.ceil(o/conversationsPerRequest);for(let a=0;a<n;a++){const r=a*conversationsPerRequest,s=a===n-1?o-r:conversationsPerRequest,i=await fetchConversationsData(t,s,r);for(let n=0;n<i.length;n++){const r=i[n],s=await fetchConversationData(t,r.id);e.push(s);const d=(a*conversationsPerRequest+n+1)/o*100;document.getElementById("openai-download-progress").value=d}a<n-1&&await new Promise((o=>setTimeout(o,delay)))}const a=new Blob([JSON.stringify(e)],{type:"application/json"}),r=document.createElement("a");r.href=URL.createObjectURL(a),r.download="chatgpt_bookmarklet_download.json",document.body.appendChild(r),r.click(),document.body.removeChild(r)}
```
</details>


<details>
<summary><a name="demo-fibonacci-md"></a>`demo/Fibonacci.md` (3 KB, 134 lines)</summary>

````markdown
---
title: Fibonacci with Matrix Exponentiation
chat_link: https://chat.openai.com/c/089bac9a-6e5f-4a64-8b77-a3ec7ef6e58c
create_time: Sun Sep 17 04:13:00 2023
update_time: Sun Sep 17 04:13:34 2023
model: gpt-4-code-interpreter
used_plugins: []
message_count: 4
content_types: ['code', 'execution_output', 'text']
custom_instructions: {'about_user_message': "I'm a math and CS student, and I like simple and clever solutions.", 'about_model_message': "You're a proficient and helpful AI programming and research assistant."}
---

###### ffae223b-5aa7-4600-a02f-39899749df8c
### System

[child ⬇️](#16322b04-e350-41fd-8f9f-6d4ef757fa7c)

---

###### 16322b04-e350-41fd-8f9f-6d4ef757fa7c
[parent ⬆️](#ffae223b-5aa7-4600-a02f-39899749df8c)
### System

[child ⬇️](#aaa21886-05e4-4f31-9d8c-9bd901197c99)

---

###### aaa21886-05e4-4f31-9d8c-9bd901197c99
[parent ⬆️](#16322b04-e350-41fd-8f9f-6d4ef757fa7c)
# Me

Wuddup code interpreter being.
Pick a complex math problem and solve it using fine logic and some python.
Write the math in beautiful latex. Be quick with it, I want it to fit in a screenshot.

[child ⬇️](#8ca84c64-f6b2-4604-84a6-52abe4a33101)

---

###### 8ca84c64-f6b2-4604-84a6-52abe4a33101
[parent ⬆️](#aaa21886-05e4-4f31-9d8c-9bd901197c99)
# ChatGPT

Sure thing! Let's consider a problem involving the computation of the \(n\)-th Fibonacci number using matrix exponentiation. This approach utilizes a neat mathematical trick and can compute Fibonacci numbers very quickly, even for large values of \(n\).

### Problem Statement

Find the \(n\)-th Fibonacci number where the Fibonacci sequence is defined as:

\[
F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2)
\]

We will use matrix exponentiation to find \(F(n)\) in \(O(\log n)\) time complexity.

### Solution

We will use the following matrix relation, which holds true for the Fibonacci sequence:

\[
\begin{bmatrix} F(n) \\ F(n-1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} F(n-1) \\ F(n-2) \end{bmatrix}
\]

Thus, we can write:

\[
\begin{bmatrix} F(n) \\ F(n-1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^n \begin{bmatrix} F(1) \\ F(0) \end{bmatrix}
\]

Now, let's proceed to compute \(F(n)\) for a given \(n\) using Python and the numpy library to handle matrix operations:

[child ⬇️](#99e1efbe-6c7b-487f-8227-27cae1702925)

---

###### 99e1efbe-6c7b-487f-8227-27cae1702925
[parent ⬆️](#8ca84c64-f6b2-4604-84a6-52abe4a33101)
# ChatGPT

```python
import numpy as np



# Define the function to find the nth Fibonacci number using matrix exponentiation

def fib_matrix(n):

    F = np.array([[1, 1], [1, 0]], dtype=object)

    return np.linalg.matrix_power(F, n)[0, 1]



# Let's find the 10th Fibonacci number as an example

n = 10

fib_matrix(n)
```

[child ⬇️](#d432834e-63c7-4efe-b66e-26faba815f64)

---

###### d432834e-63c7-4efe-b66e-26faba815f64
[parent ⬆️](#99e1efbe-6c7b-487f-8227-27cae1702925)
### Tool output

```python
55
```

[child ⬇️](#09faa857-7541-4e22-a987-cf90a5a80e74)

---

###### 09faa857-7541-4e22-a987-cf90a5a80e74
[parent ⬆️](#d432834e-63c7-4efe-b66e-26faba815f64)
# ChatGPT

Using the matrix exponentiation method, we found that the 10th Fibonacci number is \(55\).

In this approach, we utilized the following matrix to represent the recurrence relation of the Fibonacci sequence:

\[
\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^n \begin{bmatrix} F(1) \\ F(0) \end{bmatrix} = \begin{bmatrix} F(n) \\ F(n-1) \end{bmatrix}
\]

And by applying matrix exponentiation, we obtained \(F(n)\) efficiently in \(O(\log n)\) time complexity.

Feel free to take a screenshot! If you have any other questions or need further clarification, let me know.

---

````
</details>


<details>
<summary><a name="convoviz-init-py"></a>`convoviz/__init__.py` (0 KB, 5 lines)</summary>

```python
"""Main convoviz package."""

from . import configuration, data_analysis, long_runs, models, utils

__all__ = ["models", "utils", "data_analysis", "configuration", "long_runs"]

```
</details>


<details>
<summary><a name="convoviz-cli-py"></a>`convoviz/cli.py` (3 KB, 99 lines)</summary>

```python
"""Main file for running the program from the command line."""

from __future__ import annotations

from pathlib import Path
from shutil import rmtree

from .configuration import UserConfigs
from .long_runs import (
    generate_week_barplots,
    generate_wordclouds,
)
from .models import ConversationSet
from .utils import latest_bookmarklet_json


def main() -> None:
    """Run the program."""
    print(
        "Welcome to ChatGPT Data Visualizer ✨📊!\n\n"
        "Follow the instructions in the command line.\n\n"
        "Press 'ENTER' to select the default options.\n\n"
        "If you encounter any issues 🐛, please report 🚨 them here:\n\n"
        "➡️ https://github.com/mohamed-chs/chatgpt-history-export-to-md/issues/new/choose"
        " 🔗\n\n",
    )

    user = UserConfigs()

    user.prompt()

    print("\n\nAnd we're off! 🚀🚀🚀\n")

    user.set_model_configs()

    print("Loading data 📂 ...\n")

    entire_collection = ConversationSet.from_zip(user.configs["zip_filepath"])

    bkmrklet_json = latest_bookmarklet_json()
    if bkmrklet_json:
        print("Found bookmarklet download, loading 📂 ...\n")
        bkmrklet_collection = ConversationSet.from_json(bkmrklet_json)
        entire_collection.update(bkmrklet_collection)

    output_folder = Path(user.configs["output_folder"])

    # overwrite the output folder if it already exists (might change this in the future)
    if output_folder.exists() and output_folder.is_dir():
        rmtree(output_folder)

    output_folder.mkdir(parents=True, exist_ok=True)

    markdown_folder = output_folder / "Markdown"

    entire_collection.save(markdown_folder, progress_bar=True)

    print(f"\nDone ✅ ! Check the output 📄 here : {markdown_folder.as_uri()} 🔗\n")

    graph_folder = output_folder / "Graphs"
    graph_folder.mkdir(parents=True, exist_ok=True)

    generate_week_barplots(
        entire_collection,
        graph_folder,
        **user.configs["graph"],
        progress_bar=True,
    )

    print(f"\nDone ✅ ! Check the output 📈 here : {graph_folder.as_uri()} 🔗\n")
    print("(more graphs 📈 will be added in the future ...)\n")

    wordcloud_folder = output_folder / "Word Clouds"
    wordcloud_folder.mkdir(parents=True, exist_ok=True)

    generate_wordclouds(
        entire_collection,
        wordcloud_folder,
        **user.configs["wordcloud"],
        progress_bar=True,
    )

    print(f"\nDone ✅ ! Check the output 🔡☁️ here : {wordcloud_folder.as_uri()} 🔗\n")

    print("Writing custom instructions 📝 ...\n")

    cstm_inst_filepath = output_folder / "custom_instructions.json"

    entire_collection.save_custom_instructions(cstm_inst_filepath)

    print(f"\nDone ✅ ! Check the output 📝 here : {cstm_inst_filepath.as_uri()} 🔗\n")

    print(
        "ALL DONE 🎉🎉🎉 !\n\n"
        f"Explore the full gallery 🖼️ at: {output_folder.as_uri()} 🔗\n\n"
        "I hope you enjoy the outcome 🤞.\n\n"
        "If you appreciate it, kindly give the project a star 🌟 on GitHub :\n\n"
        "➡️ https://github.com/mohamed-chs/chatgpt-history-export-to-md 🔗\n\n",
    )

```
</details>


<details>
<summary><a name="convoviz-long-runs-py"></a>`convoviz/long_runs.py` (2 KB, 93 lines)</summary>

```python
"""Module for various processes that are used in the controllers."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from tqdm import tqdm

if TYPE_CHECKING:
    from typing_extensions import Unpack

    from .models import ConversationSet
    from .utils import GraphKwargs, WordCloudKwargs


def generate_week_barplots(
    conv_set: ConversationSet,
    dir_path: Path | str,
    *,
    progress_bar: bool = False,
    **kwargs: Unpack[GraphKwargs],
) -> None:
    """Create the weekwise graphs and save them to the folder."""
    dir_path = Path(dir_path)

    month_groups = conv_set.group_by_month()
    year_groups = conv_set.group_by_year()

    for month in tqdm(
        month_groups.keys(),
        "Creating monthly weekwise graphs 📈 ",
        disable=not progress_bar,
    ):
        title = month.strftime("%B '%y")
        month_groups[month].week_barplot(title, **kwargs).savefig(  # pyright: ignore [reportUnknownMemberType]
            dir_path / f"{month.strftime('%Y %B')}.png",
        )

    for year in tqdm(
        year_groups.keys(),
        "Creating yearly weekwise graphs 📈 ",
        disable=not progress_bar,
    ):
        title = year.strftime("%Y")
        year_groups[year].week_barplot(title, **kwargs).savefig(  # pyright: ignore [reportUnknownMemberType]
            dir_path / f"{year.strftime('%Y')}.png",
        )


def generate_wordclouds(
    conv_set: ConversationSet,
    dir_path: Path | str,
    *,
    progress_bar: bool = False,
    **kwargs: Unpack[WordCloudKwargs],
) -> None:
    """Create the wordclouds and save them to the folder."""
    dir_path = Path(dir_path)

    week_groups = conv_set.group_by_week()
    month_groups = conv_set.group_by_month()
    year_groups = conv_set.group_by_year()

    for week in tqdm(
        week_groups.keys(),
        "Creating weekly wordclouds 🔡☁️ ",
        disable=not progress_bar,
    ):
        week_groups[week].wordcloud(**kwargs).save(
            dir_path / f"{week.strftime('%Y week %W')}.png",
            optimize=True,
        )

    for month in tqdm(
        month_groups.keys(),
        "Creating monthly wordclouds 🔡☁️ ",
        disable=not progress_bar,
    ):
        month_groups[month].wordcloud(**kwargs).save(
            dir_path / f"{month.strftime('%Y %B')}.png",
            optimize=True,
        )

    for year in tqdm(
        year_groups.keys(),
        "Creating yearly wordclouds 🔡☁️ ",
        disable=not progress_bar,
    ):
        year_groups[year].wordcloud(**kwargs).save(
            dir_path / f"{year.strftime('%Y')}.png",
            optimize=True,
        )

```
</details>


<details>
<summary><a name="convoviz-configuration-py"></a>`convoviz/configuration.py` (3 KB, 125 lines)</summary>

```python
"""Module for handling user configuration and updating the models."""

from __future__ import annotations

from questionary import (
    Choice,
    Style,
    checkbox,
    select,
)
from questionary import (
    path as qst_path,
)
from questionary import (
    text as qst_text,
)

from .models import Conversation, Message
from .utils import (
    DEFAULT_USER_CONFIGS,
    colormaps,
    font_names,
    font_path,
    stem,
    validate_header,
    validate_zip,
)

CUSTOM_STYLE = Style(
    [
        ("qmark", "fg:#34eb9b bold"),
        ("question", "bold fg:#e0e0e0"),
        ("answer", "fg:#34ebeb bold"),
        ("pointer", "fg:#e834eb bold"),
        ("highlighted", "fg:#349ceb bold"),
        ("selected", "fg:#34ebeb"),
        ("separator", "fg:#eb3434"),
        ("instruction", "fg:#eb9434"),
        ("text", "fg:#b2eb34"),
        ("disabled", "fg:#858585 italic"),
    ],
)


class UserConfigs:
    """Class for handling user configuration."""

    def __init__(self) -> None:
        """Initialize UserConfigs object."""
        self.configs = DEFAULT_USER_CONFIGS.copy()

        # will implement a way to read from a config file later ...

    def prompt(self) -> None:
        """Prompt the user for input and update the configs."""
        lookup = self.configs

        lookup["zip_filepath"] = qst_path(
            "Enter the path to the zip file :",
            lookup["zip_filepath"],
            validate=validate_zip,
            style=CUSTOM_STYLE,
        ).ask()

        lookup["output_folder"] = qst_path(
            "Enter the path to the output folder :",
            lookup["output_folder"],
            style=CUSTOM_STYLE,
        ).ask()

        for author_role in lookup["message"]["author_headers"]:
            lookup["message"]["author_headers"][author_role] = qst_text(
                f"Enter the message header (#) for messages from '{author_role}' :",
                lookup["message"]["author_headers"][author_role],
                validate=validate_header,
                style=CUSTOM_STYLE,
            ).ask()

        lookup["conversation"]["markdown"]["latex_delimiters"] = select(
            "Select the LaTeX math delimiters you want to use :",
            ["default", "dollars"],
            lookup["conversation"]["markdown"]["latex_delimiters"],
            style=CUSTOM_STYLE,
        ).ask()

        yaml_choices = [
            Choice(title=header, checked=value)
            for header, value in lookup["conversation"]["yaml"].items()
        ]

        selected_headers = checkbox(
            "Select the YAML metadata headers you want to include :",
            yaml_choices,
            style=CUSTOM_STYLE,
        ).ask()

        for header in lookup["conversation"]["yaml"]:
            lookup["conversation"]["yaml"][header] = header in selected_headers

        font_name: str = select(
            "Select the font you want to use for the word clouds :",
            font_names(),
            stem(lookup["wordcloud"].get("font_path") or ""),
            style=CUSTOM_STYLE,
        ).ask()

        lookup["wordcloud"]["font_path"] = str(font_path(font_name))

        lookup["wordcloud"]["colormap"] = select(
            "Select the color theme you want to use for the word clouds :",
            colormaps(),
            lookup["wordcloud"].get("colormap"),
            style=CUSTOM_STYLE,
        ).ask()

        lookup["wordcloud"]["custom_stopwords"] = qst_text(
            "Enter custom stopwords (separated by commas) :",
            lookup["wordcloud"].get("custom_stopwords", ""),
            style=CUSTOM_STYLE,
        ).ask()

    def set_model_configs(self) -> None:
        """Set the configuration for all models."""
        Message.update_configs(self.configs["message"])
        Conversation.update_configs(self.configs["conversation"])

```
</details>


<details>
<summary><a name="convoviz-utils-py"></a>`convoviz/utils.py` (6 KB, 274 lines)</summary>

````python
"""Utility functions for the project."""

from __future__ import annotations

from pathlib import Path
from re import compile as re_compile
from re import sub as re_sub
from typing import Any, Literal, TypedDict
from zipfile import ZipFile

DOWNLOADS = Path.home() / "Downloads"


def latest_zip() -> Path:
    """Path to the most recently created zip file in the Downloads folder."""
    zip_files = list(DOWNLOADS.glob("*.zip"))

    if not zip_files:
        err_msg = f"No zip files found in {DOWNLOADS}"
        raise FileNotFoundError(err_msg)

    return max(zip_files, key=lambda x: x.stat().st_ctime)


def latest_bookmarklet_json() -> Path | None:
    """Path to the most recent JSON file in Downloads with 'bookmarklet' in the name."""
    bkmrklet_files = [x for x in DOWNLOADS.glob("*.json") if "bookmarklet" in x.name]

    if not bkmrklet_files:
        return None

    return max(bkmrklet_files, key=lambda x: x.stat().st_ctime)


def sanitize(filename: str) -> str:
    """Sanitized title of the conversation, compatible with file names."""
    anti_pattern = re_compile(r'[<>:"/\\|?*\n\r\t\f\v]+')

    return anti_pattern.sub("_", filename.strip()) or "untitled"


def close_code_blocks(text: str) -> str:
    """Ensure that all code blocks are closed."""
    # A code block can be opened with triple backticks, possibly followed by a lang name
    # It can only be closed however with triple backticks, with nothing else on the line

    open_code_block = False

    lines = text.split("\n")

    for line in lines:
        if line.startswith("```") and not open_code_block:
            open_code_block = True
            continue

        if line == "```" and open_code_block:
            open_code_block = False

    if open_code_block:
        text += "\n```"

    return text


def replace_latex_delimiters(text: str) -> str:
    """Replace all the LaTeX bracket delimiters in the string with dollar sign ones."""
    text = re_sub(r"\\\[", "$$", text)
    text = re_sub(r"\\\]", "$$", text)
    text = re_sub(r"\\\(", "$", text)

    return re_sub(r"\\\)", "$", text)


def stem(path: Path | str) -> str:
    """Return the `stem` of the given path."""
    return Path(path).stem


def root_dir() -> Path:
    """Path to the root directory of the project.

    might change when refactoring, currently it's `convoviz/`
    """
    return Path(__file__).parent


def font_names() -> list[str]:
    """List of font names in the `assets/fonts` folder."""
    fonts_path = root_dir() / "assets" / "fonts"
    return [font.stem for font in fonts_path.iterdir()]


def font_path(font_name: str) -> Path:
    """Path to the given font in the `assets/fonts` folder.

    `font_name` should be the stem of the font file, without the extension
    """
    return root_dir() / "assets" / "fonts" / f"{font_name}.ttf"


def default_font_path() -> Path:
    """Path to the default font in the `assets/fonts` folder."""
    return font_path("RobotoSlab-Thin")


def colormaps() -> list[str]:
    """List of colormaps in the `assets/colormaps.txt` file."""
    colormaps_path = root_dir() / "assets" / "colormaps.txt"
    with colormaps_path.open(encoding="utf-8") as file:
        return file.read().splitlines()


def validate_header(text: str) -> bool:
    """Return True if the given text is a valid markdown header."""
    max_header_level = 6
    return (
        1 <= text.count("#") <= max_header_level
        and text.startswith("#")
        and text[len(text.split()[0])] == " "
    )


def validate_zip(filepath: str | Path) -> bool:
    """Return True if the given path is a zip file with a `conversations.json` file."""
    filepath = Path(filepath)
    if not filepath.is_file() or filepath.suffix != ".zip":
        return False
    with ZipFile(filepath) as zip_ref:
        if "conversations.json" in zip_ref.namelist():
            return True
    return False


def get_archive(filepath: Path | str) -> Path:
    """Extract the zip and return the path to the extracted folder."""
    filepath = Path(filepath)
    folder = filepath.with_suffix("")

    with ZipFile(filepath) as file:
        file.extractall(folder)

    return folder


def code_block(text: str, lang: str = "python") -> str:
    """Wrap the given string in a code block."""
    return f"```{lang}\n{text}\n```"


# default configs


class AuthorHeaders(TypedDict):
    """Type hint for the author headers configs."""

    system: str
    user: str
    assistant: str
    tool: str


class MessageConfigs(TypedDict):
    """Type hint for the message configs."""

    author_headers: AuthorHeaders


DEFAULT_MESSAGE_CONFIGS: MessageConfigs = {
    "author_headers": {
        "system": "### System",
        "user": "# Me",
        "assistant": "# ChatGPT",
        "tool": "### Tool output",
    },
}


class MarkdownConfigs(TypedDict):
    """Type hint for the markdown configs."""

    latex_delimiters: Literal["default", "dollars"]


class YAMLConfigs(TypedDict):
    """Type hint for the yaml configs."""

    title: bool
    tags: bool
    chat_link: bool
    create_time: bool
    update_time: bool
    model: bool
    used_plugins: bool
    message_count: bool
    content_types: bool
    custom_instructions: bool


class ConversationConfigs(TypedDict):
    """Type hint for the conversation configs."""

    markdown: MarkdownConfigs
    yaml: YAMLConfigs


DEFAULT_CONVERSATION_CONFIGS: ConversationConfigs = {
    "markdown": {"latex_delimiters": "default"},
    "yaml": {
        "title": True,
        "tags": False,
        "chat_link": True,
        "create_time": True,
        "update_time": True,
        "model": True,
        "used_plugins": True,
        "message_count": True,
        "content_types": True,
        "custom_instructions": True,
    },
}


class GraphKwargs(TypedDict, total=False):
    """Type hint for the graph configs."""


class WordCloudKwargs(TypedDict, total=False):
    """Type hint for the wordcloud configs."""

    font_path: str
    colormap: str
    custom_stopwords: str
    background_color: str | None
    mode: Literal["RGB", "RGBA"]
    include_numbers: bool
    width: int
    height: int


DEFAULT_WORDCLOUD_CONFIGS: WordCloudKwargs = {
    "font_path": str(default_font_path()),
    "colormap": "prism",
    "custom_stopwords": "use, file, ",
    "background_color": None,
    "mode": "RGBA",
    "include_numbers": False,
    "width": 1000,
    "height": 1000,
}


class AllConfigs(TypedDict):
    """Type hint for the user config JSON file."""

    zip_filepath: str
    output_folder: str
    message: MessageConfigs
    conversation: ConversationConfigs
    wordcloud: WordCloudKwargs
    graph: GraphKwargs
    node: dict[str, Any]
    conversation_set: dict[str, Any]


DEFAULT_USER_CONFIGS: AllConfigs = {
    "zip_filepath": str(latest_zip()),
    "output_folder": str(Path.home() / "Documents" / "ChatGPT Data"),
    "message": DEFAULT_MESSAGE_CONFIGS,
    "conversation": DEFAULT_CONVERSATION_CONFIGS,
    "wordcloud": DEFAULT_WORDCLOUD_CONFIGS,
    "graph": {},
    "node": {},
    "conversation_set": {},
}

````
</details>


<details>
<summary><a name="convoviz-main-py"></a>`convoviz/__main__.py` (0 KB, 5 lines)</summary>

```python
"""Run convoviz as a module."""

from .cli import main

main()

```
</details>


<details>
<summary><a name="convoviz-data-analysis-py"></a>`convoviz/data_analysis.py` (3 KB, 119 lines)</summary>

```python
"""Module for all the data visualizations.

Should ideally only return matplotlib objects, and not deal with the filesystem.
"""

# pyright: reportUnknownMemberType = false

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from matplotlib.figure import Figure
from nltk import download as nltk_download  # type: ignore[import-untyped]
from nltk.corpus import stopwords as nltk_stopwords  # type: ignore[import-untyped]
from nltk.data import find as nltk_find  # type: ignore[import-untyped]
from wordcloud import WordCloud  # type: ignore[import-untyped]

from .utils import DEFAULT_WORDCLOUD_CONFIGS

if TYPE_CHECKING:
    from PIL.Image import Image
    from typing_extensions import Unpack

    from .utils import GraphKwargs, WordCloudKwargs


def generate_week_barplot(
    timestamps: list[float],
    title: str,
    **kwargs: Unpack[GraphKwargs],
) -> Figure:
    """Create a bar graph from the given timestamps, collapsed on one week."""
    dates = [datetime.fromtimestamp(ts, timezone.utc) for ts in timestamps]

    weekday_counts: defaultdict[str, int] = defaultdict(int)
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for date in dates:
        weekday_counts[days[date.weekday()]] += 1

    x = days
    y = [weekday_counts[day] for day in days]

    fig = Figure(dpi=300)
    ax = fig.add_subplot()

    ax.bar(x, y)
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Prompt Count")

    ax.set_title(title)

    ax.set_xticks(x)
    ax.set_xticklabels(x, rotation=45)
    fig.tight_layout()

    return fig


# Ensure that the stopwords are downloaded
def _load_nltk_stopwords() -> set[str]:
    """Load nltk stopwords."""
    try:
        nltk_find("corpora/stopwords")
    except LookupError:
        nltk_download("stopwords")

    languages = [
        "arabic",
        "english",
        "french",
        "german",
        "spanish",
        "portuguese",
    ]  # add more languages here ...

    return {word for lang in languages for word in nltk_stopwords.words(fileids=lang)}


def generate_wordcloud(
    text: str,
    **kwargs: Unpack[WordCloudKwargs],
) -> Image:
    """Create a wordcloud from the given text."""
    configs = DEFAULT_WORDCLOUD_CONFIGS.copy()
    configs.update(kwargs)

    nltk_stopwords = _load_nltk_stopwords()

    custom_stopwords = configs.get("custom_stopwords")
    custom_stopwords_list = custom_stopwords.split(sep=",") if custom_stopwords else []
    custom_stopwords_list = [
        word.strip().lower() for word in custom_stopwords_list if word.strip()
    ]

    stopwords = nltk_stopwords.union(set(custom_stopwords_list))

    wordcloud = WordCloud(
        font_path=configs.get("font_path"),
        width=configs.get("width"),  # pyright: ignore[reportGeneralTypeIssues]
        height=configs.get("height"),  # pyright: ignore[reportGeneralTypeIssues]
        stopwords=stopwords,  # pyright: ignore[reportGeneralTypeIssues]
        background_color=configs.get("background_color"),  # pyright: ignore[reportGeneralTypeIssues]
        mode=configs.get("mode"),  # pyright: ignore[reportGeneralTypeIssues]
        colormap=configs.get("colormap"),
        include_numbers=configs.get("include_numbers"),  # pyright: ignore[reportGeneralTypeIssues]
    ).generate(text)

    return wordcloud.to_image()

```
</details>


<details>
<summary><a name="convoviz-assets-colormaps-txt"></a>`convoviz/assets/colormaps.txt` (0 KB, 16 lines)</summary>

```
viridis
plasma
inferno
magma
cividis
Blues
Greens
YlGnBu
YlOrRd
RdYlBu
Spectral
coolwarm
terrain
ocean
prism
flag

```
</details>


<details>
<summary><a name="convoviz-models-conversation-set-py"></a>`convoviz/models/_conversation_set.py` (6 KB, 191 lines)</summary>

```python
"""ConversationSet class to model a set of conversations.

Groups conversations by week, month, and year, etc.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

from orjson import OPT_INDENT_2, dumps, loads
from pydantic import BaseModel
from tqdm import tqdm

from convoviz.data_analysis import generate_week_barplot, generate_wordcloud
from convoviz.utils import get_archive, sanitize

from ._conversation import Conversation  # noqa: TCH001

if TYPE_CHECKING:
    from datetime import datetime

    from matplotlib.figure import Figure
    from PIL.Image import Image
    from typing_extensions import Unpack

    from convoviz.utils import GraphKwargs, WordCloudKwargs

    from ._message import AuthorRole


class ConversationSet(BaseModel):
    """Stores a set of conversations."""

    array: list[Conversation]

    @property
    def index(self) -> dict[str, Conversation]:
        """Get the index of conversations."""
        return {convo.conversation_id: convo for convo in self.array}

    @classmethod
    def from_json(cls, filepath: Path | str) -> ConversationSet:
        """Load from a JSON file, containing an array of conversations."""
        filepath = Path(filepath)
        with filepath.open(encoding="utf-8") as file:
            return cls(array=loads(file.read()))

    @classmethod
    def from_zip(cls, filepath: Path | str) -> ConversationSet:
        """Load from a ZIP file, containing a JSON file."""
        filepath = Path(filepath)
        convos_path = get_archive(filepath) / "conversations.json"

        return cls.from_json(convos_path)

    @property
    def last_updated(self) -> datetime:
        """Return the timestamp of the last updated conversation in the list."""
        return max(conversation.update_time for conversation in self.array)

    def update(self, conv_set: ConversationSet) -> None:
        """Update the conversation set with the new one."""
        if conv_set.last_updated <= self.last_updated:
            return
        self.index.update(conv_set.index)
        self.array = list(self.index.values())

    def save(self, dir_path: Path | str, *, progress_bar: bool = False) -> None:
        """Save the conversation set to the directory."""
        dir_path = Path(dir_path)
        dir_path.mkdir(parents=True, exist_ok=True)

        for conversation in tqdm(
            self.array,
            "Writing Markdown 📄 files",
            disable=not progress_bar,
        ):
            filepath = dir_path / sanitize(f"{conversation.title}.md")
            conversation.save(filepath)

    @property
    def custom_instructions(self) -> list[dict[str, Any]]:
        """Get a list of all custom instructions, in all conversations in the set."""
        custom_instructions: list[dict[str, Any]] = []

        for conversation in self.array:
            if not conversation.custom_instructions:
                continue

            instructions_info = {
                "chat_title": conversation.title,
                "chat_link": conversation.url,
                "time": conversation.create_time,
                "custom_instructions": conversation.custom_instructions,
            }

            custom_instructions.append(instructions_info)

        return custom_instructions

    def save_custom_instructions(self, filepath: Path | str) -> None:
        """Save the custom instructions to the file."""
        filepath = Path(filepath)
        with filepath.open("w", encoding="utf-8") as file:
            file.write(dumps(self.custom_instructions, option=OPT_INDENT_2).decode())

    def timestamps(
        self,
        *authors: AuthorRole,
    ) -> list[float]:
        """Get a list of all message timestamps, in all conversations in the list."""
        timestamps: list[float] = []

        for conversation in self.array:
            timestamps.extend(conversation.timestamps(*authors))

        return timestamps

    def week_barplot(
        self,
        title: str,
        *authors: AuthorRole,
        **kwargs: Unpack[GraphKwargs],
    ) -> Figure:
        """Create a bar graph from the given conversation set."""
        if len(authors) == 0:
            authors = ("user",)
        timestamps = self.timestamps(*authors)
        return generate_week_barplot(timestamps, title, **kwargs)

    def plaintext(
        self,
        *authors: AuthorRole,
    ) -> str:
        """Get a string of all text, in all conversations in the list."""
        return "\n".join(
            conversation.plaintext(*authors) for conversation in self.array
        )

    def wordcloud(
        self,
        *authors: AuthorRole,
        **kwargs: Unpack[WordCloudKwargs],
    ) -> Image:
        """Create a wordcloud from the given conversation set."""
        if len(authors) == 0:
            authors = ("user", "assistant")
        text = self.plaintext(*authors)
        return generate_wordcloud(text, **kwargs)

    def add(self, conv: Conversation) -> None:
        """Add a conversation to the dictionary and list."""
        self.index[conv.conversation_id] = conv
        self.array.append(conv)

    def group_by_week(self) -> dict[datetime, ConversationSet]:
        """Get a dictionary of conversations grouped by the start of the week."""
        grouped: dict[datetime, ConversationSet] = {}

        for conversation in self.array:
            week_start = conversation.week_start
            if week_start not in grouped:
                grouped[week_start] = ConversationSet(array=[])
            grouped[week_start].add(conversation)

        return grouped

    def group_by_month(self) -> dict[datetime, ConversationSet]:
        """Get a dictionary of conversations grouped by the start of the month."""
        grouped: dict[datetime, ConversationSet] = {}

        for conversation in self.array:
            month_start = conversation.month_start
            if month_start not in grouped:
                grouped[month_start] = ConversationSet(array=[])
            grouped[month_start].add(conversation)

        return grouped

    def group_by_year(self) -> dict[datetime, ConversationSet]:
        """Get a dictionary of conversations grouped by the start of the year."""
        grouped: dict[datetime, ConversationSet] = {}

        for conversation in self.array:
            year_start = conversation.year_start
            if year_start not in grouped:
                grouped[year_start] = ConversationSet(array=[])
            grouped[year_start].add(conversation)

        return grouped

```
</details>


<details>
<summary><a name="convoviz-models-init-py"></a>`convoviz/models/__init__.py` (0 KB, 8 lines)</summary>

```python
"""Models for the application."""

from ._conversation import Conversation
from ._conversation_set import ConversationSet
from ._message import Message
from ._node import Node

__all__ = ["Conversation", "ConversationSet", "Message", "Node"]

```
</details>


<details>
<summary><a name="convoviz-models-conversation-py"></a>`convoviz/models/_conversation.py` (8 KB, 289 lines)</summary>

```python
"""Conversation model. Represents a single ChatGPT chat.

object path : conversations.json -> conversation (one of the list items)
"""

from __future__ import annotations

from datetime import datetime, timedelta
from os import utime as os_utime
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

from orjson import loads
from pydantic import BaseModel

from convoviz.data_analysis import generate_wordcloud
from convoviz.utils import (
    DEFAULT_CONVERSATION_CONFIGS,
    ConversationConfigs,
    WordCloudKwargs,
    close_code_blocks,
    replace_latex_delimiters,
    sanitize,
)

from ._node import Node

if TYPE_CHECKING:
    from PIL.Image import Image
    from typing_extensions import Unpack

    from ._message import AuthorRole


class Conversation(BaseModel):
    """Wrapper class for a `conversation` in _a_ `json` file."""

    __configs: ClassVar[ConversationConfigs] = DEFAULT_CONVERSATION_CONFIGS

    title: str
    create_time: datetime
    update_time: datetime
    mapping: dict[str, Node]
    moderation_results: list[Any]
    current_node: str
    plugin_ids: list[str] | None = None
    conversation_id: str
    conversation_template_id: str | None = None
    id: str | None = None  # noqa: A003

    @classmethod
    def update_configs(cls, configs: ConversationConfigs) -> None:
        """Set the configuration for all conversations."""
        cls.__configs.update(configs)

    @classmethod
    def from_json(cls, filepath: Path | str) -> Conversation:
        """Load the conversation from a JSON file."""
        filepath = Path(filepath)

        with filepath.open(encoding="utf-8") as file:
            return cls(**loads(file.read()))

    @property
    def node_mapping(self) -> dict[str, Node]:
        """Return a dictionary of connected Node objects, based on the mapping."""
        return Node.mapping(self.mapping)

    @property
    def _all_message_nodes(self) -> list[Node]:
        """List of all nodes that have a message, including all branches."""
        return [node for node in self.node_mapping.values() if node.message]

    def _author_nodes(
        self,
        *authors: AuthorRole,
    ) -> list[Node]:
        """List of all nodes with the given author role (all branches)."""
        if len(authors) == 0:
            authors = ("user",)
        return [
            node
            for node in self._all_message_nodes
            if node.message and node.message.author.role in authors
        ]

    @property
    def leaf_count(self) -> int:
        """Return the number of leaves in the conversation."""
        return sum(1 for node in self._all_message_nodes if not node.children_nodes)

    @property
    def url(self) -> str:
        """Chat URL."""
        return f"https://chat.openai.com/c/{self.conversation_id}"

    @property
    def content_types(self) -> list[str]:
        """List of all content types in the conversation (all branches)."""
        return list(
            {
                node.message.content.content_type
                for node in self._all_message_nodes
                if node.message
            },
        )

    def message_count(
        self,
        *authors: AuthorRole,
    ) -> int:
        """Return the number of 'user' and 'assistant' messages (all branches)."""
        if len(authors) == 0:
            authors = ("user",)
        return len(self._author_nodes(*authors))

    @property
    def model(self) -> str | None:
        """ChatGPT model used for the conversation."""
        assistant_nodes: list[Node] = self._author_nodes("assistant")
        if not assistant_nodes:
            return None

        message = assistant_nodes[0].message

        return message.metadata.model_slug if message else None

    @property
    def plugins(self) -> list[str]:
        """List of all ChatGPT plugins used in the conversation."""
        return list(
            {
                node.message.metadata.invoked_plugin["namespace"]
                for node in self._author_nodes("tool")
                if node.message and node.message.metadata.invoked_plugin
            },
        )

    @property
    def custom_instructions(self) -> dict[str, str]:
        """Return custom instructions used for the conversation."""
        system_nodes = self._author_nodes("system")
        if len(system_nodes) < 2:
            return {}

        context_message = system_nodes[1].message
        if context_message and context_message.metadata.is_user_system_message:
            return context_message.metadata.user_context_message_data or {}

        return {}

        # TODO: check if this is the same for conversations from the bookmarklet

    @property
    def yaml(self) -> str:
        """YAML metadata header for the conversation."""
        yaml_config = self.__configs["yaml"]

        yaml_map = {
            "title": self.title,
            "chat_link": self.url,
            "create_time": self.create_time,
            "update_time": self.update_time,
            "model": self.model,
            "used_plugins": self.plugins,
            "message_count": self.message_count("user", "assistant"),
            "content_types": self.content_types,
            "custom_instructions": self.custom_instructions,
        }

        yaml = ""

        for key, value in yaml_map.items():
            if yaml_config.get(key, True):
                yaml += f"{key}: {value}\n"

        if not yaml:
            return ""

        return f"---\n{yaml}---\n"

    @property
    def markdown(self) -> str:
        """Return the full markdown text content of the conversation."""
        markdown_config = self.__configs["markdown"]
        latex_delimiters = markdown_config["latex_delimiters"]

        markdown = self.yaml

        for node in self._all_message_nodes:
            if node.message:
                content = close_code_blocks(node.message.text)
                # prevent empty messages from taking up white space
                content = f"\n{content}\n" if content else ""
                if latex_delimiters == "dollars":
                    content = replace_latex_delimiters(content)
                markdown += f"\n{node.header}{content}{node.footer}\n---\n"

        return markdown

    def save(self, filepath: Path | str) -> None:
        """Save the conversation to the file, with added modification time."""
        filepath = Path(filepath)
        base_file_name = sanitize(filepath.stem)

        counter = 0
        while filepath.exists():
            counter += 1
            filepath = filepath.with_name(
                f"{base_file_name} ({counter}){filepath.suffix}",
            )

        with filepath.open("w", encoding="utf-8") as file:
            file.write(self.markdown)

        os_utime(filepath, (self.update_time.timestamp(), self.update_time.timestamp()))

    def timestamps(
        self,
        *authors: AuthorRole,
    ) -> list[float]:
        """List of all message timestamps from the given author role (all branches).

        Useful for generating time graphs.
        """
        if len(authors) == 0:
            authors = ("user",)
        return [
            node.message.create_time.timestamp()
            for node in self._author_nodes(*authors)
            if node.message and node.message.create_time
        ]

    def plaintext(
        self,
        *authors: AuthorRole,
    ) -> str:
        """Entire plain text from the given author role (all branches).

        Useful for generating word clouds.
        """
        if len(authors) == 0:
            authors = ("user",)
        return "\n".join(
            node.message.text for node in self._author_nodes(*authors) if node.message
        )

    def wordcloud(
        self,
        *authors: AuthorRole,
        **kwargs: Unpack[WordCloudKwargs],
    ) -> Image:
        """Generate a wordcloud from the conversation."""
        if len(authors) == 0:
            authors = ("user",)
        text = self.plaintext(*authors)
        return generate_wordcloud(text, **kwargs)

    @property
    def week_start(self) -> datetime:
        """Return the monday of the week the conversation was created in."""
        start_of_week = self.create_time - timedelta(
            days=self.create_time.weekday(),
        )

        return start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

    @property
    def month_start(self) -> datetime:
        """Return the first of the month the conversation was created in."""
        return self.create_time.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    @property
    def year_start(self) -> datetime:
        """Return the first of January of the year the conversation was created in."""
        return self.create_time.replace(
            month=1,
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

```
</details>


<details>
<summary><a name="convoviz-models-message-py"></a>`convoviz/models/_message.py` (2 KB, 89 lines)</summary>

```python
"""Represents a single message in a conversation. It's contained in a Node object.

object path : conversations.json -> conversation -> mapping -> mapping node -> message
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal

from pydantic import BaseModel, ConfigDict

from convoviz.utils import DEFAULT_MESSAGE_CONFIGS, MessageConfigs, code_block

if TYPE_CHECKING:
    from datetime import datetime

AuthorRole = Literal["user", "assistant", "system", "tool"]


class MessageAuthor(BaseModel):
    """Type of the `author` field in a `message`."""

    role: AuthorRole
    name: str | None = None
    metadata: dict[str, Any]


class MessageContent(BaseModel):
    """Type of the `content` field in a `message`."""

    content_type: str
    parts: list[str] | None = None
    text: str | None = None
    result: str | None = None


class MessageMetadata(BaseModel):
    """Type of the `metadata` field in a `message`."""

    model_slug: str | None = None
    invoked_plugin: dict[str, Any] | None = None
    is_user_system_message: bool | None = None
    user_context_message_data: dict[str, Any] | None = None

    model_config = ConfigDict(protected_namespaces=())


class Message(BaseModel):
    """Wrapper class for the `message` field in a `node`.

    see `MessageJSON` and `models.Node` for more details
    """

    __configs: ClassVar[MessageConfigs] = DEFAULT_MESSAGE_CONFIGS

    id: str  # noqa: A003
    author: MessageAuthor
    create_time: datetime | None = None
    update_time: datetime | None = None
    content: MessageContent
    status: str
    end_turn: bool | None = None
    weight: float
    metadata: MessageMetadata
    recipient: str

    @classmethod
    def update_configs(cls, configs: MessageConfigs) -> None:
        """Set the configuration for all messages."""
        cls.__configs.update(configs)

    @property
    def header(self) -> str:
        """Get the title header of the message based on the configs."""
        return self.__configs["author_headers"][self.author.role]

    @property
    def text(self) -> str:
        """Get the text content of the message."""
        if self.content.parts is not None:
            return str(self.content.parts[0])
        if self.content.text is not None:
            return code_block(self.content.text)
        if self.content.result is not None:
            return self.content.result

        # this error caught some hidden bugs in the data. need more of these
        err_msg = f"No valid content found in message: {self.id}"
        raise ValueError(err_msg)

```
</details>


<details>
<summary><a name="convoviz-models-node-py"></a>`convoviz/models/_node.py` (2 KB, 74 lines)</summary>

```python
"""Node class and methods for the node object in a conversation.

object path : conversations.json -> conversation -> mapping -> mapping node

will implement methods to handle conversation branches, like
counting the number of branches,
get the branch of a given node,
and some other version control stuff
"""

from __future__ import annotations

from pydantic import BaseModel

from ._message import Message  # noqa: TCH001


class Node(BaseModel):
    """Wrapper class for a `node` in the `mapping` field of a `conversation`."""

    id: str  # noqa: A003
    message: Message | None = None
    parent: str | None = None
    children: list[str]
    parent_node: Node | None = None
    children_nodes: list[Node] = []

    def add_child(self, node: Node) -> None:
        """Add a child to the node."""
        self.children_nodes.append(node)
        node.parent_node = self

    @classmethod
    def mapping(cls, mapping: dict[str, Node]) -> dict[str, Node]:
        """Return a dictionary of connected Node objects, based on the mapping."""
        # Initialize connections
        for node in mapping.values():
            node.children_nodes = []  # Ensure list is empty to avoid duplicates
            node.parent_node = None  # Ensure parent_node is None

        # Connect nodes
        for node in mapping.values():
            for child_id in node.children:
                child_node = mapping[child_id]
                node.add_child(child_node)

        return mapping

    @property
    def header(self) -> str:
        """Get the header of the node message, containing a link to its parent."""
        if self.message is None:
            return ""

        parent_link = (
            f"[parent ⬆️](#{self.parent_node.id})\n"
            if self.parent_node and self.parent_node.message
            else ""
        )
        return f"###### {self.id}\n{parent_link}{self.message.header}\n"

    @property
    def footer(self) -> str:
        """Get the footer of the node message, containing links to its children."""
        if len(self.children_nodes) == 0:
            return ""
        if len(self.children_nodes) == 1:
            return f"\n[child ⬇️](#{self.children_nodes[0].id})\n"

        footer = "\n" + " | ".join(
            f"[child {i+1} ⬇️](#{child.id})"
            for i, child in enumerate(self.children_nodes)
        )
        return footer + "\n"

```
</details>
