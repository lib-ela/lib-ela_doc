.. _tut_hyperelastic_incompressible_vs_nearly:

Incompressible vs Nearly-Incompressible Hyperelasticity
=======================================================

This tutorial highlights how **lib-ela** treats compressibility by comparing two Neo-Hookean models:

1. Fully incompressible (no bulk modulus)
2. Nearly-incompressible (large bulk modulus)

We will plot and compare the stress–stretch response for both.

Set-up
------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import NeoHookean

   MU = 700.0
   K = 2500.0
   model_incomp = NeoHookean(mu=MU)
   model_nearinc = NeoHookean(mu=MU, k=K)

Stretch schedule
----------------

.. code-block:: python

   lam = np.linspace(0.6, 1.4, 50)

Compute stress
--------------

.. code-block:: python

   sigma_incomp = model_incomp.stress(lam, params=[MU], protocol="uniaxial", stress_type="cauchy")
   sigma_nearinc = model_nearinc.stress(lam, params=[MU, K], protocol="uniaxial", stress_type="cauchy")

Plot
----

.. code-block:: python

   import matplotlib as mpl
   mpl.rcParams["axes.formatter.use_mathtext"] = True
   fig, ax = plt.subplots(figsize=(6,4))
   ax.plot(lam, sigma_incomp, label="Incompressible")
   ax.plot(lam, sigma_nearinc, label="Nearly-incompressible")
   ax.set_xlabel("Stretch λ")
   ax.set_ylabel("Cauchy stress [kPa]")
   ax.set_title("Neo-Hookean: Incompressible vs Nearly-incompressible")
   ax.legend()
   ax.grid(True)
   plt.show()

Biaxial comparison
------------------

.. code-block:: python

   lam1 = lam2 = np.linspace(0.8, 1.3, 60)
   lam_grid = np.stack(np.meshgrid(lam1, lam2))
   sigma_biax = model_nearinc.stress(lam_grid, params=[MU, K], protocol="biaxial", stress_type="cauchy")

   import matplotlib.pyplot as plt
   cs = plt.contourf(lam1, lam2, sigma_biax[0], 20)
   plt.colorbar(cs, label=r"$\sigma_{11}$ [kPa]")
   plt.xlabel("λ₁")
   plt.ylabel("λ₂")
   plt.title("Biaxial Cauchy stress (nearly-incompressible)")
   plt.show()

Next steps
----------

* Try other protocols ("shear", "biaxial")
* Explore the effect of varying :math:`K` on the stress response
