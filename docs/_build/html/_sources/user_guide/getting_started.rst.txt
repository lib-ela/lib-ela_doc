.. _getting_started:

Quick Start Guide
=================

This short tutorial shows how to:

1.  pip install **lib-ela** and its dependencies,
2.  create a **Neo-Hookean** material,
3.  compute Cauchy stress in *uniaxial* and *shear* protocols, and
4.  plot stress–strain curves.

.. note::

   A more thorough walkthrough of lib-ela's core features is available as a Jupyter notebook:

    - :doc:`Read the Getting Started Walkthrough online <getting_started_notebook>`

   .. raw:: html

        <a class="sd-btn sd-btn-primary" href="getting_started_notebook.ipynb" download style="margin:0.5em 0;display:inline-block;">⬇️ Download the Jupyter Notebook Walkthrough</a>
  

.. contents:: On this page
   :local:
   :depth: 1

Install
-------

Create a fresh virtual environment and grab the latest release plus the
optional Jupyter extras:

.. code-block:: console

   python -m pip install --upgrade pip
   python -m pip install lib-ela matplotlib

Imports & constants
-------------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   # Core lib-ela pieces
   from libela.hyperelastic import NeoHookean

   MU  = 700.0  # shear modulus [ kPa ]
   K   = 2500.0 # bulk modulus  [ kPa ]  (ignored for fully incompressible)

Create the model
----------------

.. code-block:: python

   neo = NeoHookean(mu=MU, k=K)      # Nearly-incompressible by default
   neo_i = NeoHookean(mu=MU)         # Fully incompressible (no K supplied)

Generate strain arrays
----------------------

.. code-block:: python

   # Stretch λ ranging 0.6 → 1.4 (compression → tension)
   lam = np.linspace(0.6, 1.4, 50)

   # Engineering shear γ
   gamma = np.linspace(0.0, 1.0, 50)

Compute stress
--------------

.. code-block:: python

   # Uniaxial Cauchy stress
   σ_uniax = neo.stress(lam, params=[MU, K], protocol="uniaxial",
                        stress_type="cauchy")

   # Simple-shear Kirchhoff stress τ12 (first return)
   τ_shear = neo.stress(gamma, params=[MU, K], protocol="shear",
                        stress_type="kirchhoff")

Plot the curves
---------------

.. code-block:: python

   fig, ax = plt.subplots(figsize=(6,4))
   ax.plot(lam, σ_uniax, label=r"$\sigma_{11}$ (uniaxial)")
   ax.set_xlabel("Stretch λ")
   ax.set_ylabel("Cauchy stress [kPa]")
   ax.set_title("Neo-Hookean uniaxial response")
   ax.grid(True)
   ax.legend()

   fig2, ax2 = plt.subplots(figsize=(6,4))
   ax2.plot(gamma, τ_shear, label=r"$\tau_{12}$ (shear)")
   ax2.set_xlabel("Engineering shear γ")
   ax2.set_ylabel("Kirchhoff stress [kPa]")
   ax2.set_title("Neo-Hookean simple-shear response")
   ax2.grid(True)
   ax2.legend()
   plt.show()

Next steps
----------
* Explore *biaxial* loading with ``protocol="biaxial"``.
* Try other stress measures (e.g. ``kirchhoff``, ``first_pk``, ``second_pk``).  
* Try other materials (e.g. ``MooneyRivlin``) as they are added.
* Explore other tutorials in the
  :doc:`/theory/tutorials/index`.
* Dive into the mathematical background in
  :doc:`/theory/hyperelastic_materials/hyperelastic`.
* Dive into the material model catalogue in
  :doc:`/theory/material_models`.
* Explore deformation protocols in
    :doc:`/theory/deformation_protocols`.
    
* :doc:`/theory/index` – tensor notation, invariants, derivations  
* :doc:`/api/index` – full class-by-class API reference  
* :doc:`/development/roadmap` – upcoming features beyond hyperelasticity
