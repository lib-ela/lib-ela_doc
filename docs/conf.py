# -----------------------------------------------------------------------------
# Sphinx configuration for lib-ela documentation
# -----------------------------------------------------------------------------
#  Requirements
#  ------------
#  * sphinx ≥ 7.2
#  * pydata-sphinx-theme ≥ 0.16 
#  * myst-parser, nbsphinx, sphinx-design, sphinx-copybutton …
# -----------------------------------------------------------------------------
from __future__ import annotations
import datetime
import sys
from pathlib import Path

# -----------------------------------------------------------------
# 1. Path management – make sure libela is importable
# -----------------------------------------------------------------
DOCS_DIR = Path(__file__).resolve().parent  # …/repo/docs
ROOT = DOCS_DIR.parent                      # …/repo
sys.path.insert(0, str(ROOT))  

# -----------------------------------------------------------------
# 2. Project metadata
# -----------------------------------------------------------------
project   = "lib-ela"
author    = "Arya Amiri, Mohamed Hassan, & Contributors"
copyright = f"{datetime.datetime.now().year}, {author}"
release   = "1.0.0"

# -----------------------------------------------------------------
# 3. Extensions
# -----------------------------------------------------------------
extensions: list[str] = [
    # Core
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    # Quality / style
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_design",
    # Notebooks / Markdown
    "nbsphinx",
    "myst_parser",
    # Diagrams
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "matplotlib.sphinxext.plot_directive",
]

graphviz_output_format = "svg" 
# -----------------------------------------------------------------
# 4. Templates & exclude patterns
# -----------------------------------------------------------------
templates_path   = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -----------------------------------------------------------------
# 5. Autosummary / autodoc
# -----------------------------------------------------------------
autosummary_generate = False            # do not auto-generate stubs
autosummary_output_dir = "api/generated"
autosummary_generate_overwrite = False # never clobber hand‑written stubs

add_module_names = False               # keep dotted names compact in signatures
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}


# -----------------------------------------------------------------
# 6. Napoleon
# -----------------------------------------------------------------
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_attr_annotations = True

# -----------------------------------------------------------------
# 7. Intersphinx
# -----------------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "numpy": ("https://numpy.org/doc/stable/", {}),
    "sympy": ("https://docs.sympy.org/latest/", {}),
    "matplotlib": ("https://matplotlib.org/stable/", {}),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", {}),
}

# Example usage in docs:
#   :func:`numpy.add`
#   :class:`matplotlib.pyplot.Figure`
#   :class:`pandas.DataFrame`
#   :class:`sympy.Symbol`
#   :class:`python:dict`
#
# For viewcode, use :source:`libela.hyperelastic.NeoHookean` (autodoc objects get a [source] link)
# For graphviz, use .. graphviz:: or .. graph:: in your .rst files

# -----------------------------------------------------------------
# 8. MathJax 3
# -----------------------------------------------------------------
mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"]],
        "macros": {
            "bm": ["\\boldsymbol{#1}", 1],
            "dd": ["\\,\\mathrm d"],
        },
    }
}

# -----------------------------------------------------------------
# 9. HTML theme — PyData-Sphinx-Theme
# -----------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"

html_theme_options = {
    # ─── Navbar ──────────────────────────────────────────────────────────────
    "logo": {
        "text": "lib‑ela",
        "image_light": "logo.png",  # stored in _static/
        "image_dark": "logo-dark.png",
    },
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],  # Removed theme-switcher
    "navbar_persistent": ["search-field"],
    "show_nav_level": 0,
    # ─── Sidebar ────────────────────────────────────────────────────────────
    "secondary_sidebar_items": [],
    # ─── Repository / edit‑this‑page ─────────────────────────────────────────
    "github_url": "https://github.com/lib-ela/lib-ela",
    "use_edit_page_button": True,
    # ─── Search ─────────────────────────────────────────────────────────────
    "search_bar_text": "Search the docs…",
    # ─── Theme settings ────────────────────────────────────────────────────
    # Default mode and pygments_style removed as they are not supported in this version
    # ─── Footer ─────────────────────────────────────────────────────────────
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"],
}

# -----------------------------------------------------------------------------
# 10. Static assets (CSS / JS / images)
# -----------------------------------------------------------------------------
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/custom.js"]

# -----------------------------------------------------------------------------
# 11. MyST‑Parser & nbsphinx
# -----------------------------------------------------------------------------
myst_enable_extensions = ["amsmath", "dollarmath", "colon_fence"]
nbsphinx_execute = "never"  # skip notebook execution on CI for speed

# -----------------------------------------------------------------
# 12. Copy‑button
# -----------------------------------------------------------------
copybutton_prompt_text = ">>> |\\.\\.\\. "  # strip standard Python prompts


# -----------------------------------------------------------------
# 14. Plotting with Matplotlib
# -----------------------------------------------------------------
plot_html_show_source_link = False
plot_html_show_formats = False
plot_include_source = True         # show the Python that made the plot
plot_formats = [("png", 160)]      # crisp PNGs; add ("svg", 1) if you want SVG too
plot_basedir = "plot_directive"    # where the extension caches outputs

# Pre-imports so your .. plot:: blocks can be concise
plot_pre_code = """
import numpy as np
import matplotlib.pyplot as plt
"""

# A few rcParams for clean docs (tweak as you like)
plot_rcparams = {
    "savefig.bbox": "tight",
    "figure.dpi": 160,
    "axes.grid": True,
    "grid.linewidth": 0.3,
    "axes.titlelocation": "left",
}