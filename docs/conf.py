# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'hpsOpenMM'
copyright = u'2022, Quyen Vu'
author = u'Quyen Vu'

# The short X.Y version
version = '2022.0'
# The full version, including alpha/beta/rc tags
release = 'v1.3'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# See: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autodoc_default_options = {
    # 'members': True,
    #'undoc-members': True,
    'private-members': True,
    #'special-members': True,
    #'inherited-members': True,
    #'show-inheritance': True
}

autosummary_generate = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'numpydoc', # automatically includes `sphinx.ext.autosummary`
    'rst2pdf.pdfbuilder',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',    
    'sphinx.ext.githubpages',
]

pdf_documents = [('index', u'rst2pdf', u'hpsOpenMM', u'Quyen Vu'),]


#mathjax_config = {
#    'extensions': ['tex2jax.js'],
#    'jax': ['input/TeX', 'output/HTML-CSS'],
#}

html_sidebars = {
    '**': ['localtoc.html', 'sourcelink.html', 'searchbox.html'],
}



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  # Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    'navigation_depth': 5,
    'collapse_navigation': False,
    'sticky_navigation': False,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/logo.svg"
# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'hpsOpenMMdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'hpsOpenMM.tex', 'hpsOpenMM Documentation',
     'hpsOpenMM', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'hpsOpenMM', 'hpsOpenMM Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'hpsOpenMM', 'hpsOpenMM Documentation',
     author, 'hpsOpenMM', 'Analysis package for all-atom simulations of proteins, with a specific focus on intrinsically disordered proteins.',
     'Miscellaneous'),
]


# -- Extension configuration ------------------------------------------------- 
##########################
# "EDIT ON GITHUB" LINKS #
##########################

############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
    html_context
except NameError:
    html_context = dict()
html_context['display_lower_left'] = True

templates_path = ['_templates']

if 'REPO_NAME' in os.environ:
    REPO_NAME = os.environ['REPO_NAME']
else:
    REPO_NAME = 'hpsOpenMM'

# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
    # get the current_language env var set by buildDocs.sh
    current_language = os.environ['current_language']
else:
    # the user is probably doing `make html`
    # set this build's current language to english
    current_language = 'en'

# tell the theme which language to we're currently building
html_context['current_language'] = current_language

# SET CURRENT_VERSION
from git import Repo

repo = Repo(search_parent_directories=True)

if 'current_version' in os.environ:
    # get the current_version env var set by buildDocs.sh
    current_version = os.environ['current_version']
else:
    # the user is probably doing `make html`
    # set this build's current version by looking at the branch
    current_version = repo.active_branch.name

# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version

# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [('en', '/' + REPO_NAME + '/en/' + current_version + '/')]

# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()

versions = [branch.name for branch in repo.branches]
for version in versions:
    html_context['versions'].append((version, '/' + REPO_NAME + '/' + current_language + '/' + version + '/'))

# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS

# settings for creating PDF with rinoh
rinoh_documents = [(
    master_doc,
    'target',
    project + ' Documentation',
    '© ' + copyright,
)]
today_fmt = "%B %d, %Y"
html_context['display_github'] = True
html_context['github_user'] = 'qvv5013'
html_context['github_repo'] = 'rtd-github-pages'
html_context['github_version'] = 'main'
