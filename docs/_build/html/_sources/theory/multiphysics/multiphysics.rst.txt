.. _th_multiphysics_derivation:

Multiphysics Theory & Derivation
================================

.. contents::
   :local:
   :depth: 1

Motivation
----------

Multiphysics models describe materials and systems where mechanical behavior is coupled with other physical fields, such as temperature (thermoelasticity), electric field (electroelasticity), or moisture (poroelasticity). These models are essential for smart materials, sensors, and biological tissues.

Kinematics & Coupled Fields
---------------------------

The deformation gradient :math:`\mathbf{F}` is coupled with additional field variables, e.g., temperature :math:`T`, electric displacement :math:`\mathbf{D}`, or chemical potential :math:`\mu`.

Example: Thermoelasticity
-------------------------

The free energy depends on both strain and temperature:

.. math::
   \Psi(\mathbf{F}, T) = W(\mathbf{F}) - \eta(T) T

where :math:`W` is the strain energy and :math:`\eta` is the entropy.

Example: Electroelasticity
--------------------------

The free energy includes electric field effects:

.. math::
   \Psi(\mathbf{F}, \mathbf{E}) = W(\mathbf{F}) - \frac{1}{2} \epsilon |\mathbf{E}|^2

where :math:`\epsilon` is the permittivity and :math:`\mathbf{E}` is the electric field.

Coupled Constitutive Laws
-------------------------

Constitutive equations are derived by differentiating the free energy with respect to all relevant variables, yielding coupled stress, heat flux, and electric displacement relations.

Further reading
---------------

* A. Eringen, *Nonlinear Theory of Continuous Media*, McGraw-Hill, 1962.
* R. W. Ogden, *Non-Linear Elastic Deformations*, Dover 1997.

----

.. hint::

   Jump back to the :doc:`User-guide overview <../../user_guide/index>` for practical code examples, or see the :doc:`material models list <../material_models>` for closed-form expressions. 