.. _tut_hyperelastic_uniaxial_demo:

Uniaxial Neo-Hookean Demo
=========================

This tutorial demonstrates how to use **lib-ela** to model the uniaxial 
deformation of a Neo-Hookean material, a classic example in nonlinear 
elasticity.


.. contents::
   :local:
   :depth: 2
   :class: tutorial-toc

.. container:: tutorial-section
   
   .. rubric:: Learning Objectives
      :class: tutorial-section__title
   
   By the end of this tutorial, you will be able to:
   
   * Instantiate a **Neo-Hookean** material from *lib-ela*
   * Compute the **Cauchy stress** as the uniaxial stretch λ increases
   * Plot the stress–stretch curve and mark the tangent modulus
   * Interpret the mechanical response of the material

.. container:: tutorial-prerequisites
   
   .. rubric:: Prerequisites
      :class: tutorial-section__title
   
   .. container:: tutorial-prerequisites__content
      
      * Basic knowledge of Python programming
      * Familiarity with Jupyter Notebooks (recommended)
      * Basic understanding of continuum mechanics concepts
   
   .. container:: tutorial-prerequisites__install
      
      .. rubric:: Installation
      
      .. code-block:: bash
         
         pip install lib-ela matplotlib numpy

.. container:: tutorial-section
   
   .. _tutorial-uniaxial-setup:
   
   .. rubric:: Step 1: Set Up the Environment
      :class: tutorial-section__title
   
   .. container:: tutorial-note
      
      .. rubric:: Note
      
      This tutorial assumes you have a working Python environment. We recommend using 
      `Jupyter Lab <https://jupyter.org/install>`_ or 
      `Google Colab <https://colab.research.google.com>`_ for an interactive experience.
   
   Let's start by importing the required libraries and setting up our material model:
   
   .. code-block:: python
      :linenos:
      :emphasize-lines: 1-3, 6-7
      
      import numpy as np
      import matplotlib.pyplot as plt
      from libela.hyperelastic import NeoHookean
      
      # Material properties (SI units: Pa, -)
      E, nu = 10e6, 0.45  # Young's modulus and Poisson's ratio
      
      # Create the Neo-Hookean material model
      mat = NeoHookean(E=E, nu=nu)

.. container:: tutorial-section
   
   .. rubric:: Step 2: Generate a Stretch Range
      :class: tutorial-section__title
   
   Next, we'll create a range of uniaxial stretches to analyze the material's response:
   
   .. code-block:: python
      :linenos:
      
      lam = np.linspace(1.00, 2.00, 61)          # 0 % … 100 % engineering strain
      sigma = mat.stress(
          lam,
          protocol="uniaxial",
          stress_type="cauchy",                  # returns array
      )

.. container:: tutorial-section
   
   .. rubric:: Step 3: Plot and Annotate
      :class: tutorial-section__title
   
   Now, let's visualize the stress–stretch curve and mark the tangent modulus:
   
   .. code-block:: python
      :linenos:
      
      plt.figure(figsize=(6, 4))
      plt.plot(lam, sigma / 1e6, label="Neo-Hookean")
      plt.xlabel("Stretch λ (–)")
      plt.ylabel("Cauchy stress (MPa)")
      plt.title("Uniaxial tension")
      plt.grid(True)

      # tangent modulus at λ = 1.2
      idx = np.searchsorted(lam, 1.2)
      plt.scatter(lam[idx], sigma[idx] / 1e6, c="k")
      plt.text(
          lam[idx] + 0.02,
          sigma[idx] / 1e6,
          f"Tangent ≈ {mat.tangent(lam[idx]):.1f} MPa",
          va="center",
      )

      plt.legend()
      plt.show()

.. container:: tutorial-section
   
   .. rubric:: Step 4: Compare with a Nearly-Incompressible Variant
      :class: tutorial-section__title
   
   Finally, let's compare the compressible Neo-Hookean material with a nearly-incompressible variant:
   
   .. code-block:: python
      :linenos:
      
      from libela.hyperelastic import NearlyIncompressibleMixin

      class NH_NI(NearlyIncompressibleMixin, NeoHookean):
          """Neo-Hookean with volumetric penalty."""

      mat_ni = NH_NI(E=E, nu=0.49, K=8 * E)      # large bulk modulus

      sigma_ni = mat_ni.stress(lam, protocol="uniaxial", stress_type="cauchy")

      plt.figure(figsize=(6, 4))
      plt.plot(lam, sigma / 1e6,     label="Compressible (ν = 0.45)")
      plt.plot(lam, sigma_ni / 1e6, label="Nearly incompressible (ν = 0.49)")
      plt.xlabel("Stretch λ (–)")
      plt.ylabel("σ (MPa)")
      plt.legend()
      plt.grid(True)
      plt.show()

.. container:: tutorial-section
   
   .. rubric:: Next Steps
      :class: tutorial-section__title
   
   * Dive into the mathematical background in
     :doc:`/theory/hyperelastic_materials/hyperelastic`.
