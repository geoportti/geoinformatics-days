import os

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Geoinformatics Research Days 2027'
copyright = 'Geoinformatics Research Days 2027 organizers'
author = 'Bryan R Vallejo'
release = '1.0'

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
# not built into the site: the local preview output (_build), and pages kept as drafts.
# To publish a draft, remove it from this list and add it to the page list in index.rst.
exclude_patterns = ['_build', 'pages/parallel_sessions.rst']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Shibuya theme: https://shibuya.lepture.com/customisation/
# Note: theme-specific options (html_theme_options, html_sidebars) differ between
# themes, so they must be updated together with html_theme when switching.
# The theme and Sphinx versions are pinned in requirements.txt (Shibuya needs Sphinx >= 8).
html_theme = "shibuya"
html_logo = '_static/grd_menu.png'
html_title = "Geoinformatics Research Days"

html_theme_options = {
    # to add urgent messages; set to '' to hide
    'announcement': 'Call for sessions open 28 October 2026',
    # accent colors: https://shibuya.lepture.com/customisation/colors/
    'accent_color': 'cyan',
    # links in the top bar; 'url' is the page's file path without .rst.
    # Keep in sync with the page list (toctree) at the bottom of index.rst.
    'nav_links': [
        {'title': 'Home', 'url': 'index'},
        {'title': 'Submissions', 'url': 'pages/submissions'},
        {'title': 'Program', 'url': 'pages/program'},
        {'title': 'Practical Info', 'url': 'pages/practical_information'},
    ],
    'github_url': 'https://github.com/geoportti/geoinformatics-days',
    # hide the theme's "Open in ChatGPT/Claude" page links
    'show_ai_links': False,
    # no left sidebar: pages are in the top bar, sections in the right sidebar
    'page_layout': 'compact',
}

# right sidebar: "On this page" (sections of the current page). Below ~1280px wide it opens
# from the icon in the bar under the header.
html_sidebars = {
    "**": ["sidebars/localtoc.html"],
}

# --------> static files (images, custom CSS)
html_static_path = ['_static']

html_css_files = ["custom.css"]
