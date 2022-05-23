
#import yaml
#import os 
#import sys


# -- Project information -----------------------------------------------------

project = 'qubes-docs'
copyright = '2022, test'
author = 'test'

title = "Qubes Docs"
html_title = "Qubes Docs"

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

html_static_path = ['../attachment']
extensions = [
        'sphinx.ext.duration',
        'sphinx.ext.doctest',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.intersphinx',
]


source_suffix = {
    '.rst': 'restructuredtext',
}
templates_path = ['_templates']

root_doc = "index"
exclude_patterns = [
            '_dev/*', 
            'attachment/*',
            '**/*.txt'
            ]

html_theme = 'classic'

html_theme_options = {
    'externalrefs': True, 
    'bgcolor': 'white',
    'linkcolor': '#99bfff',
    'textcolor': '#000000',
    'visitedlinkcolor': '#7b7b7b',
    'bodyfont': '"Open Sans", Arial, sans-serif',
    'codebgcolor': '$color-qube-light',
    'codebgcolor': 'grey'
}

gettext_uuid=True
gettext_compact=False


epub_show_urls = 'footnote'
latex_show_urls ='footnote'


locale_dirs = ['../_translated']
