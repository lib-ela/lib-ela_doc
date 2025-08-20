.. _ug_hyperelastic_overview:

Hyperelastic Overview
======================

.. contents::
   :local:
   :depth: 1

Summary
-------

The **hyperelastic** sub-package in *lib-ela* models large-strain, rate-independent
behaviour of rubber-like solids.  It defines a strain-energy density
:math:`W(\mathbf C)` (or :math:`\Psi(\mathbf F)`) and differentiates it to obtain
stresses.  Inspired by *FEniCS* / *SfePy* but staying fully **symbolic** (via
**SymPy**), you can

* inspect analytical expressions,
* *lambdify* them to fast NumPy / JAX kernels,
* export to LaTeX, and
* embed them in custom boundary-value problems.

A gentle derivation of these equations is collected in the
:doc:`theory reference <../../theory/index>`.

Quick-start
-----------

.. code-block:: python

   from libela.hyperelastic import NeoHookean

   # plane-stress Neo-Hookean sheet (E, nu)
   mat = NeoHookean(E=10e6, nu=0.45)

   lam = 1.20      # 20 % uniaxial stretch
   sigma = mat.stress(lam, protocol="uniaxial", stress_type="cauchy")
   print(f"Cauchy stress at 20 % stretch = {sigma/1e6:.2f} MPa")

Material families
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 15 25

   * - **Model**
     - **Symbol**
     - **Compressibility**

   * - Neo-Hookean
     - :math:`NH`
     - ✔︎ / – (toggle with *K*)

   * - Mooney–Rivlin
     - :math:`MR_{p,q}`
     - ✔︎ / –

   * - Ogden
     - :math:`Og_N`
     - ✔︎ / –

   * - Gent
     - :math:`G_{J_m}`
     - incompressible

   * - Arruda–Boyce
     - :math:`AB`
     - incompressible

Any model can be converted to the classical **volumetric–isochoric split**
for nearly incompressible materials by mixing-in
:class:`libela.hyperelastic.NearlyIncompressibleMixin`
(see.)

Mathematical background
-----------------------

The Cauchy stress is obtained from the second Piola–Kirchhoff stress via the
push-forward

.. math::

   \boldsymbol\sigma
   \;=\;
   \tfrac{1}{J}\,
   \mathbf F\,
   \Bigl( 2\,\partial_{\mathbf C} W(\mathbf C) \Bigr)\,
   \mathbf F^{\mathsf T},

where :math:`\mathbf C = \mathbf F^{\mathsf T}\mathbf F` is the right
Cauchy–Green tensor and :math:`J = \det\mathbf F`.
A detailed comparison of incompressible versus nearly incompressible
formulations is given in :doc:`../../theory/hyperelastic_materials/hyperelastic`.

Protocols & helpers
-------------------

`libela.hyperelastic.operations` provides ready-made deformation gradients,
root-finding utilities, and plotting helpers:

.. code-block:: python

   from libela.hyperelastic.operations import uniaxial_protocol

   lam_range, sigma = mat.stress_range(
       lam_min=1.0, lam_max=2.0, n=50,
       protocol="uniaxial",
       stress_type="pk2"
   )

   mat.plot(lam_range, sigma, protocol="uniaxial")

Further reading
---------------

* R. W. Ogden, *Non-Linear Elastic Deformations*, Dover, 1997.  
* G. A. Holzapfel, *Nonlinear Solid Mechanics*, Wiley, 2000.  
* P. Steinmann, “Formulations of finite element problems in nonlinear solid
  mechanics,” *Encyclopedia of Computational Mechanics* (2017),
  doi:`10.1002/9781119176817 <https://doi.org/10.1002/9781119176817>`_
