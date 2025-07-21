"""
Hyperelastic sub-package
========================
Large-strain, path-independent constitutive models.
"""

# --- Re-export core symbols ------------------------------------
from .hyperelastic import (
    neohookean,
    mooneyrivlin,
    klosnersegal,
    yeoh,
    polynomial,
)
from . import operations as ops        # module alias, not symbol
# Convenience aliases
neo_hookean       = neohookean
neo_hookean_comp  = neohookean(compressible=True)
mooney_rivlin     = mooneyrivlin

__all__ = [
    "neohookean", "mooneyrivlin", "klosnersegal", "yeoh", "polynomial",
    "ops", "neo_hookean", "neo_hookean_comp", "mooney_rivlin"
]
