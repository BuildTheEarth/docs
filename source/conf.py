# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Build The Earth'
copyright = '2020, Build The Earth Contributors'
author = 'Build The Earth Contributors'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Internationalisation Options --------------------------------------------
language = 'en'
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'stylesheets/override.css',
    'stylesheets/textstyles.css'
]

# This is sorta like a header, but for reST across the entire docs.
rst_prolog = """
.. include:: /.textstyles.rst
"""

rst_epilog = """
.. include:: /.links.rst
"""

# -- Material theme options (see theme.conf for more information)-------------
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Build The Earth Guide',

    # Styling Options
    'color_primary': 'blue',
    'color_accent': 'light-blue',
    # Turns out this option is only implemented in apple-touch-icon unmodified,
    # decided to use it everywhere instead
    'touch_icon': 'img/BTELogo.gif',

    # Specify a base_url used to generate sitemap.xml. If not specified, then
    # no sitemap will be built.
    'base_url': 'https://bteguide.readthedocs.io/en/latest/', 

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/EzraEn1/bteguide/',
    'repo_name': 'Build The Earth Guide',

    # Uncomment these options in production. Debug options only.
    #'html_minify': True,
    #'css_minify': True,

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,

    # For future versioning, should be handled thru tags
    'version_dropdown': False,
    'version_json': 'versions.json'

    # Set your GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',
}