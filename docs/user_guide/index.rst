.. _user_guide:

.. role:: small-caps
   :class: small-caps

.. role:: highlight
   :class: highlight

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: User Guide
   
   getting_started
   getting_started_notebook
   hyperelastic_overview

User Guide
==========

*lib‑ela* is your comprehensive toolkit for computational solid mechanics in Python.
Get started with our interactive tutorials or dive deep into the theory and implementation details.

.. grid:: 1 1 2 3
   :gutter: 2
   :margin: 2 0 2 0
   :class-container: user-guide-grid

   .. grid-item-card:: Quick Start
      :link: getting_started
      :link-type: doc
      :shadow: md
      :text-align: left
      :class-card: sd-bg-muted sd-rounded-2 sd-shadow-sm

      New to *lib-ela*? Follow our step-by-step guide to run your first simulation in minutes.

   .. grid-item-card:: Tutorials
      :link: /theory/tutorials/index
      :link-type: doc
      :shadow: md
      :text-align: left
      :class-card: sd-bg-muted sd-rounded-2 sd-shadow-sm

      Explore practical examples and learn how to implement various material models.

   .. grid-item-card:: API Reference
      :link: /api/index
      :link-type: doc
      :shadow: md
      :text-align: left
      :class-card: sd-bg-muted sd-rounded-2 sd-shadow-sm

      Detailed documentation of all classes, methods, and functions in the library.


.. container:: motivation-hero
   
  Programming is now at the heart of modern science and engineering. *lib-ela* bridges the gap between traditional solid mechanics and modern computational tools, providing an open, extensible platform for research and education.


Introduction
=============

.. grid:: 1 2 2 2
   :gutter: 3
   :class-container: mb-5
   
   .. grid-item::
      
      **The Python Ecosystem for Solid Mechanics**
      
      Python has emerged as the lingua franca of scientific computing, with a rich ecosystem of tools for numerical analysis, machine learning, and high-performance computing. *lib-ela* is designed to integrate seamlessly with this ecosystem, from NumPy and SciPy to JAX and PyTorch.
   
   .. grid-item::
      
      **Beyond Traditional FEA**
      
      While commercial FEA packages have their place, they often create silos that limit innovation. *lib-ela* provides direct access to constitutive models, enabling new workflows that combine traditional mechanics with modern data science and machine learning approaches.

Our Mission
-----------

*lib-ela* was born from a simple idea: **what if every researcher and engineer had easy access to the building blocks of solid mechanics?** 

Our goal is to create an open, community-driven library that:

- Provides :highlight:`symbolic implementations` of constitutive models
- Enables :highlight:`seamless integration` with the Python data science stack
- Supports :highlight:`automatic differentiation` for gradient-based optimization
- Facilitates :highlight:`reproducible research` through open-source development

What We're Building
-------------------

- **Symbolic models** (via SymPy) for hyperelastic, viscoelastic, and multiphysics materials
- **Automatic derivation** of stresses and tangents (:math:`\boldsymbol{P} = \frac{\partial W}{\partial \boldsymbol{F}}`, :math:`\mathbb{C} = \frac{\partial^2 W}{\partial \boldsymbol{E}^2}`)
- **Interoperability** with NumPy / JAX / PyTorch for FEA, PINNs, GNNs, and UQ
- **Open, hackable, testable** code paths for research and production

.. graphviz::
   
   digraph G {
     rankdir=LR;
     node [fontname="Helvetica,Arial,sans-serif"];
     
     // Styling
     graph [bgcolor="transparent"];
     node [style=filled, fontsize=12, shape=box, fontname="Helvetica,Arial,sans-serif"];
     edge [fontsize=10, arrowsize=0.7];
     
     // Main nodes with colors
     node [fillcolor="#4e79a7", fontcolor=white, style="filled,rounded", color="#2d5985", penwidth=1.5];
     { node [label="Constitutive Models", shape=ellipse, fillcolor="#e15759", width=2.5, height=1.2] Models; }
     
     // Sub-models
     node [fillcolor="#f28e2b", width=2.5];
     "Hyperelastic" "Viscoelastic" "Multiphysics";
     
     // Processing steps
     node [fillcolor="#59a14f"];
     "SymPy\nRepresentation";
     
     node [fillcolor="#edc948"];
     "Auto-diff\n& Codegen";
     
     node [fillcolor="#76b7b2"];
     "NumPy / JAX\n/ PyTorch";
     
     node [fillcolor="#b07aa1", shape=ellipse, width=3];
     "Applications:\nFEA / PINNs / GNNs / UQ";
     
     // Connections
     Models -> { "Hyperelastic" "Viscoelastic" "Multiphysics" } [style=invis];
     Models -> "SymPy\nRepresentation" [penwidth=2];
     "SymPy\nRepresentation" -> "Auto-diff\n& Codegen";
     "Auto-diff\n& Codegen" -> "NumPy / JAX\n/ PyTorch";
     "NumPy / JAX\n/ PyTorch" -> "Applications:\nFEA / PINNs / GNNs / UQ";
     
     // Invisible edges for alignment
     { rank=same; "Hyperelastic" "Viscoelastic" "Multiphysics" }
     edge [style=invis];
     "Hyperelastic" -> "Viscoelastic" -> "Multiphysics";
   }


Key Features
-------------

.. grid:: 1 2 2 2
   :gutter: 2
   :class-container: mb-5
   
   .. grid-item::
      :class: feature-card
      
      .. image:: /_static/icons/api.svg
         :width: 48px
         :align: left
         :class: feature-icon
      
      **Comprehensive API**
      
      Intuitive Python interface with detailed documentation and type hints for better IDE support.
   
   .. grid-item::
      :class: feature-card
      
      .. image:: /_static/icons/build.svg
         :width: 48px
         :align: left
         :class: feature-icon
      
      **Extensible Architecture**
      
      Easily implement custom material models and integrate with existing workflows.
   
   .. grid-item::
      :class: feature-card
      
      .. image:: /_static/icons/dev.svg
         :width: 48px
         :align: left
         :class: feature-icon
      
      **Modern Tooling**
      
      Built with modern Python features and best practices, including comprehensive testing and CI/CD.
   
   .. grid-item::
      :class: feature-card
      
      .. image:: /_static/icons/api.svg
         :width: 48px
         :align: left
         :class: feature-icon
      
      **Performance Optimized**
      
      Leverages NumPy and Numba for high-performance numerical computations.

Solid mechanics at a glance
---------------------------

.. math::
   :nowrap:

   \begin{align*}
   \textbf{Kinematics:} \quad
   \boldsymbol{F} &= \frac{\partial \boldsymbol{\varphi}}{\partial \boldsymbol{X}}, &
   J &= \det \boldsymbol{F}, &
   \boldsymbol{C} &= \boldsymbol{F}^\top \boldsymbol{F} \\[1em]
   \textbf{Hyperelastic energy (Neo-Hookean, nearly incompressible):} \quad
   W &= \frac{\mu}{2}\,\left(\bar{I}_1 - 3\right) + \frac{K}{2}\,\left(J - 1\right)^2, &
   \bar{I}_1 &= J^{-2/3}\,\mathrm{tr}(\boldsymbol{C}) \\[1em]
   \textbf{Stresses:} \quad
   \boldsymbol{P} &= \frac{\partial W}{\partial \boldsymbol{F}}, &
   \boldsymbol{\sigma} &= \frac{1}{J}\,\boldsymbol{P}\,\boldsymbol{F}^\top
   \end{align*}

.. note::

   The *nearly incompressible* form lets us tune bulk response via :math:`K`, while keeping the deviatoric response governed by :math:`\mu`. This mirrors how many rubbers, soft tissues, and gels are modeled in practice.

Quick visuals
-------------

.. plot::
   :context: reset
   :include-source: false
   :caption: **Uniaxial Cauchy stress** for incompressible Neo-Hookean: :math:`\sigma(\lambda)=\mu(\lambda^2-\lambda^{-1})` for several :math:`\mu`.
   :align: center

   import numpy as np
   import matplotlib.pyplot as plt
   
   plt.style.use('seaborn-v0_8-pastel')
   
   # Generate data
   lmbda = np.linspace(0.6, 2.0, 400)
   mus = [50e3, 100e3, 200e3]  # Pa
   
   # Create figure with better styling
   plt.figure(figsize=(8, 5), dpi=100)
   
   # Plot with improved styling
   for mu in mus:
       sigma = mu * (lmbda**2 - 1.0/lmbda)
       plt.plot(lmbda, sigma, linewidth=2.5, 
               label=f"μ = {mu/1000:.0f} kPa",
               alpha=0.9)
   
   # Enhanced plot styling
   plt.grid(True, linestyle='--', alpha=0.7)
   plt.xlabel("Stretch λ", fontsize=12, fontweight='bold')
   plt.ylabel("Cauchy stress σ (Pa)", fontsize=12, fontweight='bold')
   plt.title("Uniaxial Neo-Hookean Response (Incompressible)", 
            fontsize=13, pad=15)
   plt.legend(fontsize=10, framealpha=1, shadow=True)
   plt.tight_layout()

.. plot::
   :context: close-figs
   :include-source: false
   :caption: **Energy landscape** :math:`W(\\lambda_1,\\lambda_2)` for incompressible Neo-Hookean with :math:`\\lambda_3=(\\lambda_1\\lambda_2)^{-1}`, :math:`W=\\tfrac{\\mu}{2}(I_1-3)`.
   :align: center

   from mpl_toolkits.mplot3d import Axes3D
   from matplotlib import cm
   
   # Set up the figure with better styling
   plt.style.use('default')
   plt.rcParams['font.family'] = 'sans-serif'
   plt.rcParams['axes.edgecolor'] = '#333F4B'
   
   # Generate data
   lam1 = np.linspace(0.6, 1.8, 100)
   lam2 = np.linspace(0.6, 1.8, 100)
   L1, L2 = np.meshgrid(lam1, lam2)
   L3 = 1.0 / (L1 * L2)  # det F = 1
   mu = 100e3  # Pa
   
   I1 = L1**2 + L2**2 + L3**2
   W = 0.5 * mu * (I1 - 3.0) / 1e3  # Convert to kJ/m³ for better scale
   
   # Create 3D plot with better styling
   fig = plt.figure(figsize=(10, 7), dpi=100)
   ax = fig.add_subplot(111, projection="3d")
   
   # Create surface plot with better colormap
   surf = ax.plot_surface(L1, L2, W, 
                         cmap=cm.viridis,
                         linewidth=0, 
                         antialiased=True,
                         alpha=0.9,
                         rstride=2,
                         cstride=2)
   
   # Add color bar
   cbar = fig.colorbar(surf, shrink=0.7, aspect=10, pad=0.1)
   cbar.set_label('Energy (kJ/m³)', fontsize=10, labelpad=10)
   
   # Set labels and title with better styling
   ax.set_xlabel("λ₁", fontsize=12, fontweight='bold', labelpad=10)
   ax.set_ylabel("λ₂", fontsize=12, fontweight='bold', labelpad=10)
   ax.set_zlabel("Energy (kJ/m³)", fontsize=12, fontweight='bold', labelpad=10)
   
   # Adjust view angle and layout
   ax.view_init(elev=30, azim=45)
   plt.tight_layout()


Get involved
------------

- Contribute new models and tests: :doc:`/theory/index`
- Help wire up JAX/PyTorch backends: :doc:`/development/contributing`
- Add tutorial notebooks and benchmarks: :doc:`/theory/tutorials/index`



     
