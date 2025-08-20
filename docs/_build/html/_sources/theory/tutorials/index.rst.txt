.. _tutorials_index:

Tutorials
=========

Step-by-step, runnable examples you can copy-paste into a notebook or script.
Each tutorial focuses on one concrete task and can be executed in any Jupyter
notebook or plain Python file.

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:
   :caption: Tutorials

   hyperelastic_uniaxial_demo
   hyperelastic_incompressible_vs_nearly
   hyperelastic_biaxial_inflation

.. grid:: 1 1 2 3
   :gutter: 2
   :class-container: tut-grid

   .. grid-item-card:: Uniaxial Neo-Hookean
      :link: hyperelastic_uniaxial_demo
      :link-type: doc
      :shadow: md
      :class-card: tut-card
      :text-align: left

      Learn how to instantiate a Neo-Hookean material, compute Cauchy stress under uniaxial stretch, and plot the stress–stretch curve.

      :doc:`Start tutorial → <hyperelastic_uniaxial_demo>`

   .. grid-item-card:: Incompressible vs Nearly Incompressible
      :link: hyperelastic_incompressible_vs_nearly
      :link-type: doc
      :shadow: md
      :class-card: tut-card
      :text-align: left

      Compare two Neo-Hookean models to understand how **lib-ela** handles compressibility.

      :doc:`Start tutorial → <hyperelastic_incompressible_vs_nearly>`

   .. grid-item-card:: Biaxial Inflation
      :link: hyperelastic_biaxial_inflation
      :link-type: doc
      :shadow: md
      :class-card: tut-card
      :text-align: left

      Explore balloon-type loading and analyze pressure–stretch curves for biaxial deformation.

      :doc:`Start tutorial → <hyperelastic_biaxial_inflation>`

----

Coming Soon
-----------

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card:: Simple Shear
      :shadow: sm
      :class-card: tut-card tut-disabled
      :text-align: left

      Shear modulus extraction and analysis of off-axis stresses in different material orientations.

   .. grid-item-card:: Viscoelastic Creep
      :shadow: sm
      :class-card: tut-card tut-disabled
      :text-align: left

      Time-dependent compliance analysis using the Generalised-Maxwell model for viscoelastic materials.
