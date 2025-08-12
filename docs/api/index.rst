.. _api_reference:

API Reference
=============

.. contents::
   :local:
   :depth: 1

This section is your go-to for the core modules in libela. Each link below opens the
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


Quick Example
-------------
.. code-block:: python

    from libela.hyperelastic import neohookean
    model = neohookean(mu=1.0, lam=1.0)
    stress = model.stress(F)

See Also
--------

- :doc:`/user_guide/getting_started`
- :doc:`/theory/material_models`
- `GitHub Repository <https://github.com/yourorg/yourrepo>`__
- `Report an Issue <https://github.com/yourorg/yourrepo/issues>`__