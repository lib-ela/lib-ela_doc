.. _tut_hyperelastic_uniaxial:

Uniaxial Neo-Hookean Demo
==========================

.. contents::
   :local:
   :depth: 2

Goals
-----

* Instantiate a **Neo-Hookean** material from *lib-ela*.
* Compute the **Cauchy stress** as the uniaxial stretch λ increases.
* Plot the stress–stretch curve and mark the tangent modulus.

Prerequisites
~~~~~~~~~~~~~

Install the base library plus **matplotlib**:

.. code-block:: bash

   pip install lib-ela matplotlib

Step 1 — Set-up
---------------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import NeoHookean

   E, nu = 10e6, 0.45          # Pa, –
   mat = NeoHookean(E=E, nu=nu)

Step 2 — Generate a stretch range
---------------------------------

.. code-block:: python

   lam = np.linspace(1.00, 2.00, 61)          # 0 % … 100 % engineering strain
   sigma = mat.stress(
       lam,
       protocol="uniaxial",
       stress_type="cauchy",                  # returns array
   )

Step 3 — Plot and annotate
--------------------------

.. code-block:: python

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

Step 4 — Compare with a nearly-incompressible variant
-----------------------------------------------------

.. code-block:: python

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

Next steps
----------

* Dive into the mathematical background in
  :doc:`/theory/hyperelastic_materials/hyperelastic`.
