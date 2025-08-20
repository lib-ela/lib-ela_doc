.. _tut_hyperelastic_incompressible_vs_nearly:

Working with Compressibility
============================

 This tutorial highlights how **lib-ela** handles material compressibility by comparing 
 the behavior of incompressible and nearly-incompressible Neo-Hookean models under uniaxial loading.

.. contents::
   :local:
   :depth: 2
   :class: tutorial-toc

.. container:: tutorial-section
   
   .. rubric:: Learning Objectives
      :class: tutorial-section__title
   
   By the end of this tutorial, you will be able to:
   
   * Understand the difference between incompressible and nearly-incompressible material models
   * Implement both models using **lib-ela**'s Neo-Hookean material
   * Compare their stress-stretch responses
   * Interpret the role of bulk modulus in material behavior

.. container:: tutorial-prerequisites
   
   .. rubric:: Prerequisites
      :class: tutorial-section__title
   
   .. container:: tutorial-prerequisites__content
      
      * Basic knowledge of hyperelasticity
      * Familiarity with Python and NumPy
      * Completion of the :doc:`Uniaxial Neo-Hookean Demo <hyperelastic_uniaxial_demo>` tutorial
   
   .. container:: tutorial-prerequisites__install
      
      .. rubric:: Installation
      
      .. code-block:: bash
         
         pip install lib-ela matplotlib numpy

.. container:: tutorial-section
   
   .. _incompressible-intro:
   
   .. rubric:: Introduction
      :class: tutorial-section__title
   
   In continuum mechanics, many materials are modeled as incompressible when their volume changes 
   are negligible compared to their shape changes. However, true incompressibility can lead to 
   numerical challenges in finite element analysis. A common approach is to use a nearly-incompressible 
   formulation with a large bulk modulus.
   
   In this tutorial, we'll compare:
   
   1. A fully incompressible Neo-Hookean model (no bulk modulus)
   2. A nearly-incompressible Neo-Hookean model (with large bulk modulus)

.. container:: tutorial-section
   
   .. _incompressible-setup:
   
   .. rubric:: Step 1: Set Up the Models
      :class: tutorial-section__title
   
   Let's start by importing the required libraries and setting up both material models:
   
   .. code-block:: python
      :linenos:
      :emphasize-lines: 1-3, 6-9
      
      import numpy as np
      import matplotlib.pyplot as plt
      from libela.hyperelastic import NeoHookean
      
      # Material parameters (MPa)
      MU = 0.7  # Shear modulus in GPa (700 MPa)
      K = 2.5   # Bulk modulus in GPa (2500 MPa)
      
      # Create material models
      model_incomp = NeoHookean(mu=MU)  # Incompressible
      model_nearinc = NeoHookean(mu=MU, k=K)  # Nearly-incompressible

.. container:: tutorial-section
   
   .. _incompressible-stretch:
   
   .. rubric:: Step 2: Define the Stretch Range
      :class: tutorial-section__title
   
   We'll analyze the material response over a range of stretches:
   
   .. code-block:: python
      :linenos:
      
      # Create a range of stretch values (60% compression to 40% tension)
      lam = np.linspace(0.6, 1.4, 50)

.. container:: tutorial-section
   
   .. _incompressible-compute:
   
   .. rubric:: Step 3: Compute Stress Response
      :class: tutorial-section__title
   
   Now, let's compute the Cauchy stress for both models:
   
   .. code-block:: python
      :linenos:
      
      # Compute Cauchy stress for both models
      sigma_incomp = model_incomp.stress(
          lam, 
          params=[MU], 
          protocol="uniaxial", 
          stress_type="cauchy"
      )
      
      sigma_nearinc = model_nearinc.stress(
          lam, 
          params=[MU, K], 
          protocol="uniaxial", 
          stress_type="cauchy"
      )

.. container:: tutorial-section
   
   .. _incompressible-plot:
   
   .. rubric:: Step 4: Visualize the Results
      :class: tutorial-section__title
   
   Let's plot and compare the stress-stretch responses:
   
   .. code-block:: python
      :linenos:
      
      import matplotlib as mpl
      
      # Enable math text rendering
      mpl.rcParams["axes.formatter.use_mathtex"] = True
      
      # Create figure
      plt.figure(figsize=(8, 5))
      
      # Plot stress-stretch curves
      plt.plot(lam, sigma_incomp, 
              label="Incompressible ($K = \\infty$)", 
              linewidth=2.5)
              
      plt.plot(lam, sigma_nearinc, 
              '--', 
              label=f"Nearly-incompressible ($K = {K:.1f}$ GPa)",
              linewidth=2.5)
      
      # Add labels and grid
      plt.xlabel("Stretch $\\lambda$ (–)", fontsize=12)
      plt.ylabel("Cauchy stress $\\sigma$ (MPa)", fontsize=12)
      plt.title("Comparison of Incompressible vs Nearly-Incompressible Response", 
                fontsize=14, pad=15)
      
      # Add legend and grid
      plt.legend(fontsize=10, frameon=True, framealpha=0.9)
      plt.grid(True, linestyle='--', alpha=0.7)
      
      # Adjust layout and display
      plt.tight_layout()

.. container:: tutorial-section
   
   .. _incompressible-conclusion:
   
   .. rubric:: Discussion and Conclusion
      :class: tutorial-section__title
   
   The plot clearly shows the difference between the incompressible and nearly-incompressible models:
   
   - The incompressible model (solid line) enforces zero volume change exactly
   - The nearly-incompressible model (dashed line) allows for small volume changes
   - The difference is most noticeable in compression where volume changes are more significant
   
   In practice, nearly-incompressible formulations are often preferred for their better numerical properties in finite element analysis.

.. container:: tutorial-section
   
   .. rubric:: Next Steps
      :class: tutorial-section__title
   
   * Explore how the choice of bulk modulus affects the solution accuracy and convergence
   * Learn about more advanced material models in the :doc:`/theory/hyperelastic_materials/hyperelastic` section
   * Try modifying the material parameters and observe their effects on the stress-stretch response

.. code-block:: python
   :linenos:

   # Create a grid of biaxial stretch values
   lam1 = lam2 = np.linspace(0.8, 1.3, 60)
   lam_grid = np.stack(np.meshgrid(lam1, lam2))
   
   # Compute biaxial stress response
   sigma_biax = model_nearinc.stress(
       lam_grid, 
       params=[MU, K], 
       protocol="biaxial", 
       stress_type="cauchy"
   )

   # Plot the results
   plt.figure(figsize=(8, 6))
   cs = plt.contourf(lam1, lam2, sigma_biax[0], 20, cmap='viridis')
   plt.colorbar(cs, label=r"$\sigma_{11}$ (MPa)")
   plt.xlabel(r'$\lambda_1$', fontsize=12)
   plt.ylabel(r'$\lambda_2$', fontsize=12)
   plt.title('Biaxial Stress Response (MPa)', fontsize=14)
   plt.grid(True, linestyle='--', alpha=0.7)
   plt.tight_layout()
   plt.show()

.. container:: tutorial-section
   
   .. _incompressible-explore:
   
   .. rubric:: Further Exploration
      :class: tutorial-section__title
   
   Now that you've seen the basic comparison, here are some ways to explore further:
   
   * Try different loading protocols (e.g., "shear", "planestrain") to see how the models behave under various deformation modes
   * Investigate how the choice of bulk modulus :math:`K` affects the stress response and numerical stability
   * Compare the computational performance between the two formulations for different problem sizes
   * Explore the effect of material parameters on the stress-stretch response

.. container:: tutorial-section
   
   .. rubric:: References
      :class: tutorial-section__title
   
   * Holzapfel, G. A. (2000). *Nonlinear Solid Mechanics: A Continuum Approach for Engineering*. John Wiley & Sons.
   * Bonet, J., & Wood, R. D. (2008). *Nonlinear Continuum Mechanics for Finite Element Analysis* (2nd ed.). Cambridge University Press.

.. container:: tutorial-section
   
   .. rubric:: Need Help?
      :class: tutorial-section__title
   
   If you have questions or run into issues, please refer to the :doc:`/user_guide/getting_started` guide or open an issue on our `GitHub repository <https://github.com/your-org/your-repo>`_.
