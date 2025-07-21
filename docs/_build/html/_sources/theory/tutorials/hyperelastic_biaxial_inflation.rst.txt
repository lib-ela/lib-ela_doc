.. _tut_hyperelastic_biaxial_inflation:

Biaxial Inflation: Balloon-Type Loading
=======================================

This tutorial reproduces the classic **sphere / balloon inflation** test for an
incompressible Neo-Hookean membrane.  We will

1. prescribe equal meridional stretches :math:`\lambda_1 = \lambda_2 = \lambda`;
2. compute the in-plane Cauchy stress :math:`\sigma_{\theta\theta}`;
3. convert membrane tension to **internal pressure–stretch** curves; and
4. discuss thin-walled assumptions.

Why care?  Inflation experiments are a gold standard for calibrating
hyperelastic soft-tissue models because they load the specimen biaxially while
recording readily-measurable pressure.

Prerequisites
-------------

.. code-block:: bash

   pip install lib-ela matplotlib

Set-up
------

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import NeoHookean

   MU = 50.0 * 1e3   # 50 kPa  →  50 000 Pa
   model = NeoHookean(mu=MU)          # incompressible

   # Geometry: initial radius R0 and thickness t0
   R0, t0 = 10e-3, 0.5e-3   # [m]

Stretch schedule
----------------

We inflate from the undeformed state to 60 % stretch in surface directions:

.. code-block:: python

   lam = np.linspace(1.00, 1.60, 120)     # surface stretch λ

   # Build λ-grid for planar-biaxial protocol (λ1 = λ2 = λ)
   lam_grid = np.stack([lam, lam])        # shape (2, N)

Compute membrane stress
-----------------------

.. code-block:: python

   # σ is a 3×N array; use first principal σ11 == σθθ == σφφ
   sigma = model.stress(lam_grid, params=[MU], protocol="biaxial",
                        stress_type="cauchy")[0]

Thin-wall pressure formula
--------------------------

For a spherical membrane of current radius :math:`R = \lambda R_0` and current
thickness :math:`t = t_0/\lambda^2` (volume conservation):

.. math::

   P = \frac{2 t \sigma_{\theta\theta}}{R}
     = \frac{2 t_0}{R_0} \frac{\sigma_{\theta\theta}}{\lambda^3}.

.. code-block:: python

   P = 2 * t0 / R0 * sigma / lam**3     # [Pa]

Plot pressure–stretch curve
---------------------------

.. code-block:: python

   plt.figure(figsize=(6,4))
   plt.plot(lam, P / 1e3)               # convert to kPa
   plt.xlabel("Surface stretch λ")
   plt.ylabel("Pressure [kPa]")
   plt.title("Neo-Hookean balloon inflation")
   plt.grid(True)
   plt.show()

Interpretation
--------------

* The curve rises steeply once **λ ≈ 1.3**, reflecting stiffening at large
  biaxial strains.
* Changing **MU** scales the pressure almost linearly in the
  low-stretch regime—use this feature to fit experimental data.

Next steps
~~~~~~~~~~

* Swap ``NeoHookean`` for more complex materials as lib-ela grows.
* Extend the code to **nearly incompressible** models by supplying
  ``k=K`` and using ``params=[MU, K]``.
