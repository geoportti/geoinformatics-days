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

# _templates holds edited copies of some Shibuya theme templates (used instead of the theme's).
# When upgrading Shibuya, compare them with the new version's files.
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
    # Planned announcements: keep one line active and comment out the rest (add/remove "# ").
    'announcement': 'The Call for Sessions opens soon!',
    # 'announcement': 'Call for sessions open until 27 November 2026',          # from 28 Oct 2026
    # 'announcement': 'Abstract submission opens 9 December 2026',              # from 4 Dec 2026
    # 'announcement': 'Abstract submission open until 8 February 2027',         # from 9 Dec 2026
    # 'announcement': 'Registration opens 8 March 2027',                        # from 9 Feb 2027
    # 'announcement': 'Registration open until 26 April 2027',                  # from 8 Mar 2027
    # 'announcement': 'Presenters: please register by 2 April 2027',            # from 8 Mar 2027
    # 'announcement': '',                                                       # after 26 Apr 2027
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
# as a drawer from an icon: in the top bar on mid-size screens, in the bar under the header on phones.
html_sidebars = {
    "**": ["sidebars/localtoc.html"],
}

# --------> static files (images, custom CSS)
html_static_path = ['_static']

html_css_files = ["custom.css"]
