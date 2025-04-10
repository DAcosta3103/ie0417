# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Añadimos el directorio donde se encuentra el código Python al sys.path
sys.path.insert(0, os.path.abspath('../Python'))  # Cambia '../Python' por el directorio correcto

# -- Project information -----------------------------------------------------
project = 'Cuenta Bancaria'
copyright = '2025, Diego Acosta'
author = 'Diego Acosta'
release = '1'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc']  # Autodocumentación para C++

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Puedes cambiar el tema si lo prefieres
html_static_path = ['_static']
