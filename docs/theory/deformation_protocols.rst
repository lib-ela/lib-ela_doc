.. _theory_deformation_protocols:

Deformation Protocols
=====================

This page defines the reference deformation gradients :math:`\mathbf{F}` used in
**lib-ela** for evaluating hyperelastic stress responses and generating
synthetic data.  Each protocol includes:

* physical description,
* analytic deformation-gradient tensor,
* volume ratio :math:`J = \det \mathbf{F}`,
* code block showing how to call :py:meth:`libela.hyperelastic.HyperelasticBase.stress`.

If you implement new materials, they will *automatically* work with every
protocol listed here.

.. contents::
   :local:
   :depth: 1


Protocol summary
----------------

.. list-table::
   :header-rows: 1
   :class: sd-table

   * - **Protocol**
     - **Primary stretches**
     - **F-matrix**
     - **Volume change** :math:`J`
   * - Uniaxial
     - :math:`\lambda, \lambda^{-1/2}, \lambda^{-1/2}`
     - :math:`\operatorname{diag}(\lambda, \lambda^{-1/2}, \lambda^{-1/2})`
     - :math:`1`
   * - Planar Biaxial
     - :math:`\lambda_1, \lambda_2, (\lambda_1\lambda_2)^{-1}`
     - :math:`\operatorname{diag}(\lambda_1,\lambda_2,(\lambda_1\lambda_2)^{-1})`
     - :math:`1`
   * - Simple Shear
     - :math:`\gamma` (engineering shear)
     - :math:`\begin{bmatrix}1&\gamma&0\\0&1&0\\0&0&1\end{bmatrix}`
     - :math:`1`

(For the initial public release only *uniaxial*, *biaxial*, and *simple shear*
are implemented.)

Uniaxial Loading
----------------

In uniaxial extension/compression one axis stretches by :math:`\lambda` while the
lateral axes contract to preserve volume (**incompressible** assumption):

.. math::

   \mathbf{F}_{\text{uniax}} =
   \begin{bmatrix}
   \lambda & 0 & 0 \\
   0 & \lambda^{-1/2} & 0 \\
   0 & 0 & \lambda^{-1/2}
   \end{bmatrix},\qquad J = 1.

**Example**

.. code-block:: python

   import numpy as np, matplotlib.pyplot as plt
   from libela.hyperelastic import NeoHookean

   MU, K = 700.0, 2500.0
   model = NeoHookean(mu=MU, k=K)

   lam = np.linspace(0.6, 1.4, 50)
   sigma = model.stress(lam, params=[MU, K],
                        protocol="uniaxial", stress_type="cauchy")

   plt.plot(lam, sigma); plt.xlabel("λ"); plt.ylabel("σ₁₁ [kPa]")
   plt.title("Uniaxial Cauchy stress"); plt.show()

Planar Biaxial Loading
----------------------

Planar biaxial tests pull the sheet independently along two orthogonal axes:

.. math::

   \mathbf{F}_{\text{biax}} =
   \operatorname{diag}\!\bigl(\lambda_1,\; \lambda_2,\; (\lambda_1\lambda_2)^{-1}\bigr).

*For nearly-incompressible cases* :math:`J \neq 1`, lib-ela includes the volumetric
penalty via **K** automatically.

.. code-block:: python

   lam1 = lam2 = np.linspace(0.8, 1.3, 60)
   lam_grid = np.stack( np.meshgrid(lam1, lam2) )  # shape (2, N, N)

   sigma, J = model.stress(lam_grid, params=[MU, K],
                            protocol="biaxial", stress_type="cauchy",
                            return_volume=True)

   # sigma is a 3×N×N array; show σ11 contour
   plt.contourf(lam1, lam2, sigma[0], 20); plt.colorbar()
   plt.xlabel("λ₁"); plt.ylabel("λ₂"); plt.title("σ₁₁ (biaxial)"); plt.show()

Simple Shear
------------

Simple shear of magnitude :math:`\gamma` has a deformation gradient

.. math::

   \mathbf{F}_{\text{shear}} =
   \begin{bmatrix}
   1 & \gamma & 0 \\
   0 & 1 & 0 \\
   0 & 0 & 1
   \end{bmatrix},\qquad J = 1.

.. code-block:: python

   gamma = np.linspace(0, 1.0, 50)
   tau12 = model.stress(gamma, params=[MU, K],
                        protocol="shear", stress_type="kirchhoff")

   plt.plot(gamma, tau12); plt.xlabel("γ"); plt.ylabel("τ₁₂ [kPa]")
   plt.title("Simple-shear Kirchhoff stress"); plt.show()

Hydrostatic (Volumetric) Test
-----------------------------

**Coming soon** – reserved for compressible materials where bulk modulus **K**
is a primary calibration parameter.

Implementation details
----------------------

All protocol helpers live in
:py:func:`deformation_gradient_matrix`.

Feel free to add new protocols by contributing additional analytic **F**
tensors and registering them in the `PROTOCOLS` map.
