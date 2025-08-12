Viscoelastic
============

.. raw:: html

   <h1 style="font-size:2.5rem;font-weight:700;margin-bottom:0.2em;">
     
     <span class="module-label">(libela.viscoelastic)</span>
   </h1>

Viscoelastic material models for time-dependent and hereditary effects in soft materials.

Models
------

.. list-table::
   :header-rows: 1
   :widths: 12 18 40 30

   * - **Model**
     - **API Reference**
     - **Equation**
     - **Description**
   * - Maxwell Model
     - :doc:`libela.viscoelastic.maxwell`
     - :math:`\sigma + \lambda \frac{d\sigma}{dt} = E \varepsilon`
     - A classic viscoelastic model combining a spring and dashpot in series. Used for time-dependent stress relaxation and creep.
   * - Prony Series Model
     - :doc:`libela.viscoelastic.prony_series`
     - :math:`G(t) = G_\infty + \sum_{i=1}^N G_i e^{-t/\tau_i}`
     - A generalized Maxwell model using a sum of spring-dashpot elements to capture complex viscoelastic behavior.

.. toctree::
   :maxdepth: 1
   :hidden:

   libela.viscoelastic.maxwell
   libela.viscoelastic.prony_series

.. note::
   These models are under development. API documentation will be added in a future release.

.. automodule:: libela.viscoelastic
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:
