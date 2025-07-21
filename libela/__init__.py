# libela/__init__.py
# ------------------------------------------------------------
from importlib import metadata

__version__ = metadata.version("libela")

# Public sub-packages
from . import hyperelastic

__all__ = ["hyperelastic"]