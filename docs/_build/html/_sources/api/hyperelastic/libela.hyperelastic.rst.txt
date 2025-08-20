.. raw:: html

   <h1 style="font-size:2.5rem;font-weight:700;margin-bottom:0.2em;">
     
     <span class="module-label">(libela.hyperelastic)</span>
   </h1>

Hyperelastic
=============

Symbolic strain-energy models for hyperelastic materials. Each class defines a strain-energy function :math:`W(I_1, I_2, J, \ldots)` and inherits symbolic stress evaluation from the operations mix-in.

.. note::
   This module relies on :mod:`sympy` for symbolic computation and :mod:`numpy` for numerical operations.
   See the `SymPy documentation <https://docs.sympy.org/latest/>`__ and the `NumPy documentation <https://numpy.org/doc/stable/>`__ for more details.

   See :doc:`/theory/material_models` for mathematical background and :doc:`/user_guide/hyperelastic_overview` for usage examples.

Material Models
---------------

.. list-table::
   :header-rows: 1
   :widths: 12 18 40 30

   * - **Model**
     - **API Reference**
     - **Equation**
     - **Description**
   * - Neo-Hookean
     - :doc:`hyperelastic.neohookean <libela.hyperelastic.neohookean>`
     - :math:`W = \frac{\mu}{2}(I_1-3)`  
       :math:`W_{\mathrm{NI}} = \frac{\mu}{2}(\bar I_1-3) + W_{\mathrm{vol}}`
     - Simple, isotropic, incompressible model for rubber-like materials.
   * - Mooney-Rivlin
     - :doc:`hyperelastic.mooneyrivlin <libela.hyperelastic.mooneyrivlin>`
     - :math:`W = C_1(\bar I_1-3) + C_2(\bar I_2-3) + W_{\mathrm{vol}}`
     - Captures nonlinearity in rubber elasticity.
   * - Yeoh
     - :doc:`hyperelastic.yeoh <libela.hyperelastic.yeoh>`
     - :math:`W = C_1 (\bar I_1-3) + C_2 (\bar I_1-3)^2 + C_3 (\bar I_1-3)^3 + W_{\mathrm{vol}}`
     - Good for modeling large deformations.
   * - Polynomial
     - :doc:`hyperelastic.polynomial <libela.hyperelastic.polynomial>`
     - :math:`W = \sum_{p,q} C_{pq} (\bar I_1-3)^p (\bar I_2-3)^q + W_{\mathrm{vol}}`
     - General, flexible form for fitting experimental data.
   * - Klosner-Segal
     - :doc:`hyperelastic.klosnersegal <libela.hyperelastic.klosnersegal>`
     - :math:`W = c_{11}(I_1-3) + c_{21}(I_2-3) + c_{22}(I_2-3)^2 + c_{23}(I_2-3)^3`
     - Four-term model for advanced fitting.

Functions & Methods
-------------------

.. list-table::
   :header-rows: 1
   :widths: 18 18 45 30

   * - **Function/Method**
     - **API Reference**
     - **Description**
     - **Example**
   * - ``fit``
     - :doc:`hyperelastic.fit <libela.hyperelastic>`
     - Fit model parameters to experimental data.
     - .. code-block:: python

          model.fit(data)
   * - ``stress``
     - :doc:`hyperelastic.stress <libela.hyperelastic>`
     - Compute the Cauchy or 2nd Piola-Kirchhoff stress for a given deformation.
     - .. code-block:: python

          stress = model.stress(F)
   * - ``strain``
     - :doc:`hyperelastic.strain <libela.hyperelastic>`
     - Compute strain invariants or tensors.
     - .. code-block:: python

          I1, I2 = model.strain(F)
   * - ``energy``
     - :doc:`hyperelastic.energy <libela.hyperelastic>`
     - Return the symbolic strain-energy function for the model.
     - .. code-block:: python

          W = model.energy()
   * - ``deformation_protocols``
     - :doc:`hyperelastic.operations <../operations/libela.operations>`
     - Standard loading protocols (uniaxial, biaxial, shear) for stress evaluation.
     - .. code-block:: python

          model.stress(F, protocol="uniaxial")
   * - ``operations``
     - :doc:`hyperelastic.operations <../operations/libela.operations>`
     - All models inherit symbolic and numeric operations from :class:`libela.hyperelastic.operations`.
     - See :doc:`/api/operations/libela.operations`

Example
-------

.. code-block:: python

   from libela.hyperelastic import neohookean
   import numpy as np

   F = np.eye(3)  # Deformation gradient
   model = neohookean(mu=1.0, lam=1.0)
   stress = model.stress(F)
   print(stress)


See Also
--------

- :doc:`/theory/material_models`
- :doc:`/theory/hyperelastic_materials/hyperelastic`
- :doc:`/theory/deformation_protocols`
- :doc:`/user_guide/hyperelastic_overview`
- :doc:`/user_guide/getting_started`

.. toctree::
   :maxdepth: 1
   :hidden:

   libela.hyperelastic.neohookean
   libela.hyperelastic.mooneyrivlin
   libela.hyperelastic.klosnersegal
   libela.hyperelastic.polynomial
   libela.hyperelastic.yeoh