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

html_theme = "pydata_sphinx_theme"
html_logo = '_static/grd_menu.png' 
html_title = "Geoinformatics Research Days 2024"

html_static_path = ['_static']

html_context = {
   "default_mode": "light"
}

json_url = '_static\switcher.json'

version_match = "v1.0"

html_theme_options = {
    'navbar_align': 'content', 
    'navbar_persistent': [], #'search-field'
    'search_bar_text': '',
    "header_links_before_dropdown": 8,
    'navbar_end': ['navbar-icon-links', 'theme-switcher'], # , 
    'footer_start':['search-field' , "copyright", ], # 
    'footer_end':[ "sphinx-version", "theme-version"], # "version-switcher"
    'pygment_light_style': 'xcode',
    'secondary_sidebar_items': ['page-toc', 'edit-this-page'],
    # 'announcement': 'Submission deadline in Feb 2024!', # to add urgent messages, Deadline extended! Sign up until the 20.09.2023
    'switcher': {
            'json_url': json_url,
            'version_match':version_match
        
    },
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/header-links.html
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/AaltoGIS/geoinformatics-research-days",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ]
                        }


# -------> navigation bar elements on left

html_sidebars = {
    "**": [ "sidebar-nav-bs.html"],
}


# --------> custom static files
html_static_path = ['_static']

html_css_files = ["css/gcc.css",]