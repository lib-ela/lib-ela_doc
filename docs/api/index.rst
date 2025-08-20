.. _api_reference:

API Reference
=============

.. contents::
   :local:
   :depth: 1

This section is your go-to for the core modules in *lib-ela*. Each link below opens the
full, module‑level API page, including classes, functions, and constants.

.. toctree::
   :maxdepth: 4
   :hidden:

   hyperelastic/libela.hyperelastic
   viscoelastic/libela.viscoelastic
   multiphysics/libela.multiphysics
   operations/libela.operations
   fitting/libela.fitting


Package Index
-------------

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - **API Reference**
     - **Sub-package**
     - **What’s inside**

   * - :doc:`Hyperelastic <hyperelastic/libela.hyperelastic>`
     - ``libela.hyperelastic``
     - Symbolic strain-energy models and operations for core hyperelastic materials.
   * - :doc:`Viscoelastic <viscoelastic/libela.viscoelastic>`
     - ``libela.viscoelastic``
     - Core viscoelastic material mode
   * - :doc:`Multiphysics <multiphysics/libela.multiphysics>`
     - ``libela.multiphysics``
     - Core multiphysics material mode
   * - :doc:`Operations <operations/libela.operations>`
     - ``libela.operations``
     - Deformation protocols and stress solvers
   * - :doc:`Fitting <fitting/libela.fitting>`
     - ``libela.fitting``
     - Plotting and Fitting utils

Conventions & Types
-------------------

.. list-table::
   :widths: 26 74
   :header-rows: 1

   * - Symbol / arg
     - Type & meaning
   * - ``lam``
     - float or 1D array of stretches :math:`\lambda` (uniaxial protocols).
   * - ``F``
     - 2×2 or 3×3 deformation gradient (NumPy array), protocol-dependent.
   * - ``params``
     - Material parameters, e.g. ``[mu, K]`` for nearly-incompressible models.
   * - ``stress_type``
     - ``'cauchy'`` | ``'PK1'`` | ``'PK2'``.
   * - ``protocol``
     - ``'uniaxial'``, ``'biaxial'``, or ``'simple_shear'``.

Deformation Protocols
---------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Protocol
     - Solver entry point
   * - Uniaxial
     - :py:func:`libela.operations.uniaxial_solver`
   * - Biaxial
     - :py:func:`libela.operations.biaxial_solver`
   * - Simple shear
     - :py:func:`libela.operations.simple_shear_solver`

Quick Example
-------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import hyperelastic

   model = hyperelastic.neohookean(compressible=True)
   lam = np.linspace(0.7, 1.5, 200)
   mu, K = 1.0, 100.0
   sigma = model.stress(lam, params=[mu, K], protocol='uniaxial', stress_type='cauchy')

   plt.plot(lam, sigma)
   plt.xlabel(r'$\lambda$')
   plt.ylabel('Cauchy stress')
   plt.title('Neo-Hookean: uniaxial')

See Also
--------

- :doc:`/user_guide/getting_started`
- :doc:`/theory/material_models`
- `GitHub Repository <https://github.com/lib-ela/lib-ela>`__
- `Report an Issue <https://github.com/lib-ela/lib-ela/pulls>`__