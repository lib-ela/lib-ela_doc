.. _tut_hyperelastic_biaxial_inflation:

Biaxial Inflation
=================

This tutorial demonstrates how to simulate the inflation of a thin spherical membrane 
using an incompressible Neo-Hookean material model, a classic problem in nonlinear 
continuum mechanics with applications in biomechanics and soft robotics.

.. contents::
   :local:
   :depth: 2
   :class: tutorial-toc

.. container:: tutorial-section
   
   .. rubric:: Learning Objectives
      :class: tutorial-section__title
   
   By the end of this tutorial, you will be able to:
   
   * Model biaxial inflation of a spherical membrane
   * Compute in-plane Cauchy stress for a Neo-Hookean material
   * Convert membrane tension to internal pressure–stretch relationships
   * Understand thin-walled assumptions in membrane theory

.. container:: tutorial-prerequisites
   
   .. rubric:: Prerequisites
      :class: tutorial-section__title
   
   .. container:: tutorial-prerequisites__content
      
      * Basic knowledge of continuum mechanics
      * Familiarity with Python and NumPy
      * Completion of the :doc:`Uniaxial Neo-Hookean Demo <hyperelastic_uniaxial_demo>` tutorial
   
   .. container:: tutorial-prerequisites__install
      
      .. rubric:: Installation
      
      .. code-block:: bash
         
         pip install lib-ela matplotlib numpy

.. container:: tutorial-section
   
   .. _inflation-intro:
   
   .. rubric:: Introduction
      :class: tutorial-section__title
   
   Inflation experiments are a gold standard for calibrating hyperelastic soft-tissue models 
   because they load the specimen biaxially while recording readily-measurable pressure.
   
   In this tutorial, we will:
   
   1. Prescribe equal meridional stretches :math:`\lambda_1 = \lambda_2 = \lambda`
   2. Compute the in-plane Cauchy stress :math:`\sigma_{\theta\theta}`
   3. Convert membrane tension to **internal pressure–stretch** curves
   4. Discuss thin-walled assumptions and their implications

.. container:: tutorial-section
   
   .. _inflation-setup:
   
   .. rubric:: Step 1: Set Up the Model and Geometry
      :class: tutorial-section__title
   
   Let's start by importing the required libraries and setting up our material model and geometry:
   
.. code-block:: python
   :linenos:
   
   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import NeoHookean
   
   # Material properties (in SI units)
   MU = 50.0 * 1e3  # Shear modulus: 50 kPa → 50,000 Pa
   model = NeoHookean(mu=MU)  # Create incompressible Neo-Hookean material
   
   # Geometry: initial radius R0 and thickness t0 (in meters)
   R0 = 10e-3    # Initial radius: 10 mm
   t0 = 0.5e-3   # Initial thickness: 0.5 mm

.. container:: tutorial-section
   
   .. _inflation-stretch:
   
   .. rubric:: Step 2: Define the Stretch Schedule
      :class: tutorial-section__title
   
   We'll analyze the inflation from the undeformed state up to 60% stretch in the surface directions. 
   This range covers the typical operating range for many soft materials.
   
   .. code-block:: python
      :linenos:
      
      # Create a range of stretch values (from 0% to 60% stretch)
      lam = np.linspace(1.00, 1.60, 120)  # Surface stretch λ
      
      # Create a grid for biaxial loading (λ1 = λ2 = λ)
      lam_grid = np.stack([lam, lam])     # Results in shape (2, 120)
      
      # Note: The first dimension corresponds to the two in-plane directions
      #       The second dimension contains the stretch values

.. container:: tutorial-section
   
   .. _inflation-stress:
   
   .. rubric:: Step 3: Compute Membrane Stress
      :class: tutorial-section__title
   
   For a thin spherical membrane under biaxial loading, the stress state is equi-biaxial, 
   meaning the two in-plane principal stresses are equal (:math:`\sigma_{11} = \sigma_{22}`).
   
   .. code-block:: python
      :linenos:
      
      # Compute Cauchy stress for biaxial loading
      # The result is a 3×N array where the first row contains σ11 = σθθ = σφφ
      # We only need the first principal stress component for our analysis
      sigma = model.stress(
          lam_grid, 
          params=[MU], 
          protocol="biaxial",
          stress_type="cauchy"
      )[0]  # Take only the first principal stress component

.. container:: tutorial-section
   
   .. _inflation-pressure:
   
   .. rubric:: Step 4: Apply Thin-Wall Pressure Formula
      :class: tutorial-section__title
   
   For a thin spherical membrane under internal pressure, we can relate the membrane stress to the internal pressure using the following thin-wall approximation:
   
   .. math::
      
      P = \frac{2 t \sigma_{\theta\theta}}{R}
   
   Where:
   
   * :math:`P` is the internal pressure
   * :math:`t = t_0/\lambda^2` is the current thickness (from volume conservation)
   * :math:`\sigma_{\theta\theta}` is the circumferential stress
   * :math:`R = \lambda R_0` is the current radius
   
   Substituting the geometric relationships, we get:
   
   .. math::
      
      P = \frac{2 t_0 \sigma_{\theta\theta}}{R_0 \lambda^3}
     = \frac{2 t_0}{R_0} \frac{\sigma_{\theta\theta}}{\lambda^3}.

   Let's implement this in code to compute the internal pressure for each stretch value:

   .. code-block:: python
      :linenos:
      
      # Compute internal pressure using the thin-wall formula
      # Convert from Pa to kPa for better readability
      P = 2 * t0 / R0 * sigma / lam**3  # [Pa]
      P_kPa = P / 1e3  # Convert to kPa

.. container:: tutorial-section
   
   .. _inflation-plot:
   
   .. rubric:: Step 5: Plot the Pressure–Stretch Response
      :class: tutorial-section__title
   
   Now, let's visualize the relationship between internal pressure and stretch:
   
   .. code-block:: python
      :linenos:
      
      # Set up the plot with a modern style
      plt.style.use('seaborn-v0_8')
      
      # Create figure and axis
      plt.figure(figsize=(8, 5))
      
      # Plot pressure vs. stretch
      plt.plot(lam, P_kPa, 
              linewidth=2.5, 
              color='#1f77b4',
              label='Theoretical Response')
      
      # Add labels and title
      plt.xlabel("Stretch $\\lambda$ (–)", fontsize=12)
      plt.ylabel("Internal Pressure (kPa)", fontsize=12)
      plt.title("Pressure–Stretch Response of a Spherical Membrane", 
                fontsize=14, pad=15)
      
      # Add grid and legend
      plt.grid(True, linestyle='--', alpha=0.7)
      plt.legend(fontsize=10, frameon=True, framealpha=0.9)
      
      # Adjust layout and display
      plt.tight_layout()
      plt.show()

.. container:: tutorial-section
   
   .. _inflation-interpretation:
   
   .. rubric:: Interpretation of Results
      :class: tutorial-section__title
   
   The pressure-stretch curve reveals several important characteristics of the material's behavior:
   
   * **Initial Response**: At low stretches, the pressure increases gradually with stretch.
   * **Stiffening**: The curve rises steeply once :math:`\lambda \approx 1.3`, reflecting significant material stiffening at large biaxial strains.
   * **Material Parameter Sensitivity**: The shear modulus :math:`\mu` (MU) scales the pressure almost linearly in the low-stretch regime, which is useful for fitting experimental data.
   * **Geometric Effects**: The pressure is directly proportional to the thickness-to-radius ratio :math:`t_0/R_0`.

.. container:: tutorial-section
   
   .. _inflation-conclusion:
   
   .. rubric:: Conclusion
      :class: tutorial-section__title
   
   In this tutorial, we've demonstrated how to model the inflation of a thin spherical membrane using an incompressible Neo-Hookean material model. The analysis shows the characteristic J-shaped pressure-stretch curve typical of soft biological tissues and elastomers under biaxial loading.

.. container:: tutorial-section
   
   .. _inflation-next-steps:
   
   .. rubric:: Next Steps
      :class: tutorial-section__title
   
   To extend this analysis, you might want to:
   
   * **Explore Different Material Models**: Try other hyperelastic models like Mooney-Rivlin or Ogden by replacing :class:`NeoHookean <libela.hyperelastic.NeoHookean>` with other material classes.
   * **Investigate Geometric Effects**: Study how changes in the initial thickness-to-radius ratio affect the pressure-stretch response.
   * **Compare with Experimental Data**: Load and compare your experimental data with the theoretical predictions.
   * **Advanced Analysis**: Consider implementing finite strain shell elements for more accurate modeling of thicker membranes.

.. container:: tutorial-section
   
   .. rubric:: References
      :class: tutorial-section__title
   
   * Holzapfel, G. A. (2000). *Nonlinear Solid Mechanics: A Continuum Approach for Engineering*. John Wiley & Sons.
   * Ogden, R. W. (1997). *Non-linear Elastic Deformations*. Dover Publications.
   * Humphrey, J. D. (2002). *Cardiovascular Solid Mechanics: Cells, Tissues, and Organs*. Springer.

.. container:: tutorial-section
   
   .. rubric:: Need Help?
      :class: tutorial-section__title
   
   If you have questions or run into issues, please refer to the :doc:`/user_guide/getting_started` guide or open an issue on our `GitHub repository <https://github.com/your-org/your-repo>`.
