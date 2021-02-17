# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import recommonmark
from recommonmark.transform import AutoStructify


'''PROJECT INFORMATION'''
project = 'Build The Earth: Guide'
author = 'BTE Contributors'
copyright = '2021, BTE Contributors'

release = '2.0.0'
## The full version, including alpha/beta/rc tags


'''GENERAL CONFIGURATION'''
templates_path = ['../common/_templates']
## Add any paths that contain templates here, relative to this directory.

#exclude_patterns = ['.textstyles.rst']
## List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
## This pattern also affects html_static_path and html_extra_path.




'''INTERNATIONALIZATION OPTIONS'''
language = 'en'

#locale_dirs = ['locale/']   # path is example but recommended.
#gettext_compact = False     # optional.
## Deprecated due to custom language handling.


'''HTML OUTPUT OPTIONS'''
html_theme = 'sphinx_rtd_theme'
## The theme to use for HTML and HTML Help pages. See the documentation for a list of builtin themes.


html_static_path = ['../common/_static']
## Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
## They are copied after the builtin static files, so a file named "default.css" will overwrite the built-in "default.css".

html_css_files = [
    'css/textstyles.css',
    'css/custom.css'
]

html_favicon = '../common/_static/img/BTELogo.gif'
html_title = "Build The Earth Guide"
html_short_title = "BTEGuide"
html_last_updated_fmt = ""


'''rST BUILD OPTIONS'''
rst_prolog = """
.. include:: ../common/.textstyles.rst
"""
## rST Header include. 
## Messes with warning output far too much right now to be justifiable until the right suppress_warnings option is available.

'''GENERAL BUILD OPTIONS'''
keep_warnings = True
suppress_warnings = [
    #'ref.ref'
]

'''EXTENSION CONFIGURATION'''
extensions = [
    'recommonmark',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx_markdown_tables'
]
## Add any Sphinx extension module names here, as strings. They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

todo_include_todos = True
todo_emit_warnings = True
extlinks = {
    'bte': ('https://buildtheearth.net/%s', 'Website ')
}
autosectionlabel_prefix_document = True
## Extension Options.

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
# Sets AutoStructify up, enables a lot of great features not present in CommonMark (but present in ReCommonMark).