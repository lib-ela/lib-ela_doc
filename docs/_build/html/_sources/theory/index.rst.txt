.. _theory_index:

Theory
=======
.. contents::
   :local:
   :depth: 2

The *Theory* section gathers background material that underpins **lib-ela**.  
It blends concise derivations with hands-on code so you can move seamlessly from
equations to executable examples. 
Use this section when you need to check a tensor identity, confirm a stress measure, or dig into an energy function.

Hyperelasticity
---------------

Kinematics, strain-energy functions, stress measures, and consistent tangents
for large-strain elasticity.

**→ Read the guide:** :doc:`hyperelastic_materials/hyperelastic`

Viscoelasticity
---------------

Time-dependent material behavior, relaxation functions, and viscoelastic constitutive models for rate-dependent materials.

**→ Read the guide:** :doc:`viscoelastic/viscoelastic`

Multiphysics
------------

Coupled physical phenomena including thermoelasticity, poroelasticity, and electroelasticity in large deformations.

**→ Read the guide:** :doc:`multiphysics/multiphysics`

Material-Model Catalogue
------------------------

Closed-form expressions, parameter lists, and validity ranges for every energy
model implemented in *lib-ela*.

**→ Browse models:** :doc:`material_models`

Deformation Protocols
---------------------

Most constitutive tests reduce to a handful of canonical load cases—
**uniaxial**, **biaxial**, **simple shear**, and **volumetric/hydrostatic**.  
We formalise each as a *deformation protocol* with an analytic deformation-gradient
tensor :math:`\mathbf{F}`.

**→ Browse tests:** :doc:`deformation_protocols`

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:
   :caption: Theory

   hyperelastic_materials/hyperelastic
   viscoelastic/viscoelastic
   multiphysics/multiphysics
   material_models
   deformation_protocols
