Multiphysics
============

.. raw:: html

   <h1 style="font-size:2.5rem;font-weight:700;margin-bottom:0.2em;">
     
     <span class="module-label">(libela.multiphysics)</span>
   </h1>

Multiphysics material models for coupled field effects in soft materials.

Models
------

.. list-table::
   :header-rows: 1
   :widths: 12 18 40 30

   * - **Model**
     - **API Reference**
     - **Equation**
     - **Description**
   * - Temperature-Sensitive Hydrogel
     - :doc:`libela.multiphysics.temp_sensitive_hydrogel`
     - :math:`\sigma = f(\varepsilon, T)`
     - A multiphysics model for hydrogels whose mechanical response depends on temperature.
   * - pH-Sensitive Hydrogel
     - :doc:`libela.multiphysics.ph_sensitive_hydrogel`
     - :math:`\sigma = f(\varepsilon, \mathrm{pH})`
     - A multiphysics model for hydrogels whose mechanical response depends on pH.

.. toctree::
   :maxdepth: 1
   :hidden:

   libela.multiphysics.temp_sensitive_hydrogel
   libela.multiphysics.ph_sensitive_hydrogel

.. note::
   These models are under development. API documentation will be added in a future release. 