.. _th_viscoelastic_derivation:

Viscoelasticity Theory & Derivation
====================================

.. raw:: html

   <span class="module-path">theory.</span>
   <div class="api-title">viscoelastic</div>

.. contents::
   :local:
   :depth: 1

Motivation
----------

Viscoelastic models describe materials that exhibit both elastic and time-dependent (viscous) behavior, such as polymers, biological tissues, and rubbers under long-term loading. These models capture phenomena like stress relaxation, creep, and hysteresis.

Kinematics & Constitutive Laws
------------------------------

Viscoelasticity is often modeled using combinations of springs (elastic elements) and dashpots (viscous elements), leading to classic models such as Maxwell, Kelvin–Voigt, and Standard Linear Solid. The constitutive equations relate stress, strain, and their time derivatives.

Example: Generalized Maxwell Model
----------------------------------

The stress evolution is governed by:

.. math::
   \sigma(t) + \sum_{i=1}^N \tau_i \frac{d\sigma}{dt} = \sum_{i=0}^N E_i \left( \varepsilon(t) + \tau_i \frac{d\varepsilon}{dt} \right)

where :math:`E_i` are elastic moduli and :math:`\tau_i` are relaxation times.

Time-Domain Response
--------------------

* **Creep:** Strain response to a constant applied stress.
* **Stress relaxation:** Stress response to a constant applied strain.
* **Hysteresis:** Energy dissipation under cyclic loading.

Frequency-Domain Response
-------------------------

* **Storage modulus** and **loss modulus** describe the elastic and viscous response under oscillatory loading.

Further reading
---------------

* L. E. Nielsen & R. F. Landel, *Mechanical Properties of Polymers and Composites*, 2nd Ed.
* J. D. Ferry, *Viscoelastic Properties of Polymers*, 3rd Ed.

----

.. hint::

   Jump back to the :doc:`User-guide overview <../../user_guide/index>` for practical code examples, or see the :doc:`material models list <../material_models>` for closed-form expressions. 