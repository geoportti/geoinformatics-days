import os


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Geoinformatics Research Days 2026'
copyright = 'Geoinformatics Research Days 2026 organizers'
author = 'Bryan R Vallejo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.builders.linkcheck',
    'sphinx_togglebutton',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx_design',
    "sphinx_carousel.carousel",
    # 'myst_nb',
    # 'jupyter_sphinx',
    # 'sphinx_tabs.tabs',
    # "sphinx_inline_tabs",
   # 'sphinx_last_updated_by_git'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
html_logo = '_static/grd_menu.png' 
html_title = "Geoinformatics Research Days 2026"

html_static_path = ['_static']

html_context = {
   "default_mode": "light"
}

json_url = '_static\switcher.json'

version_match = "v1.0"

html_theme_options = asdict(theme_options)


# -------> navigation bar elements on left

html_sidebars = {
    "**": [ "sidebar-nav-bs.html"],
}


# --------> custom static files
html_static_path = ['_static']

html_css_files = ["css/gcc.css",]
