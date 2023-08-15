# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'InVesalius3'
copyright = '2023, InVesalius'
author = 'InVesalius'
release = '2023-07-03'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence"]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_theme = "pydata_sphinx_theme"
html_logo = "inv_logo.png"

html_theme_options = {
    
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/invesalius/invesalius3",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-github-square",
            # Whether icon should be a FontAwesome class, or a local file
            "type": "fontawesome",  # Default is fontawesome
        }
   ]
   
}
