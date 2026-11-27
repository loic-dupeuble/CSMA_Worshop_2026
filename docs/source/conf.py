# Configuration file for the Sphinx documentation builder.
import os
import sys

import myst_nb
sys.path.insert(0, os.path.abspath('../../'))

# Project information
project   = 'beamsolve'
copyright = '2025, Dupeuble Loïc'
author    = 'Dupeuble Loïc'
release   = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    "sphinx_thebe",
    "myst_parser",
    'myst_nb',
]

thebe_config = {
    "repository_url": "https://github.com/loic-dupeuble/CSMA_Worshop_2026",
    "repository_branch": "main",
}

# Template configuration
templates_path   = ['_templates']
exclude_patterns = []

# Generate autosummary
autosummary_generate         = True
autosummary_imported_members = True

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}

autodoc_typehints = "description" # None
autodoc_member_order = "bysource"

# Configuration des notebooks
nb_execution_mode = "force"

# Intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy':  ('https://numpy.org/doc/stable/', None),
}

# Enable math support in MyST
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "deflist",
]

# Options for HTML output
html_theme        = "furo" # sphinx_rtd_theme
html_static_path  = ['_static']
# html_theme_options = {
#     'navigation_depth': 6,
# }