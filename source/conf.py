# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime as dt
from datetime import timezone as tz

n = dt.now(tz.utc)

project = "brain"
copyright = "{}, serverhorror <serverhorror@users.noreply.github.com>".format(n.year)
author = "serverhorror <serverhorror@users.noreply.github.com>"
release = "0.0.{}{}{}{}{}{}".format(
    n.year,
    n.month,
    n.day,
    n.hour,
    n.minute,
    n.second,
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    # we want todo items to be shown
    "sphinx.ext.todo",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# make sure the todo items are not shown
todo_include_todos = True

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = f"{project}"
html_theme = "furo"
html_static_path = ["_static"]
