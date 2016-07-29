#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from zope.dottedname.resolve import resolve

# -- General configuration ------------------------------------------------

extensions = []
templates_path = ['_templates']


source_parsers = {
    '.md': resolve('recommonmark.parser.CommonMarkParser'),
    }
source_suffix = ['.rst', '.md']

source_suffix = '.rst'
master_doc = 'index'
project = 'uniondrive'
copyright = '2016, TakesxiSximada'
author = 'TakesxiSximada'

release = resolve('{}.__version__'.format(project))
version = '.'.join(release.split('.')[:2])
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'uniondrivedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

latex_documents = [
    (master_doc, 'uniondrive.tex', 'uniondrive Documentation',
     'TakesxiSximada', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'uniondrive', 'uniondrive Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'uniondrive', 'uniondrive Documentation',
     author, 'uniondrive', 'One line description of project.',
     'Miscellaneous'),
]
