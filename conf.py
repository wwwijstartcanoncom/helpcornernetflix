# Configuration file for the Sphinx documentation builder.
 
import os
import sys
 
# -- Path setup --------------------------------------------------------------
 
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))
 
# -- Project information -----------------------------------------------------
 
project = 'Netflix TV Activation Guide'
copyright = '2025, Netflix'
author = 'Netflix'
 
# The full version, including alpha/beta/rc tags
release = '1.0.0'
 
# -- General configuration ---------------------------------------------------
 
extensions = []
 
# Templates path
templates_path = ['_templates']
 
# Patterns to exclude from documentation build
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
 
# Allow raw HTML blocks in .rst files
rst_prolog = """
.. role:: raw-html(raw)
   :format: html
"""
 
# -- HTML output settings ----------------------------------------------------
 
# Theme (you can change it if you want to use another)
# html_theme = 'sphinx_rtd_theme'
 
# Title shown in browser tab and at the top of HTML pages
html_title = "Activate Netflix on TV via netflix.com/tv2 – Simple Setup Guide"
 
# Optional short title
html_short_title = "Netflix TV Activation"
 
# Hide “View page source” link
html_show_sourcelink = False
 
# Favicon (put favicon.ico in _static or root directory)
html_favicon = 'favicon.ico'
 
# Allow raw HTML in source files
html_allow_unsafe = True
 
# Theme options customization
html_theme_options = {
    'show_powered_by': False,
}
 
# Static files path (uncomment if you add custom CSS/JS/images)
# html_static_path = ['_static']
