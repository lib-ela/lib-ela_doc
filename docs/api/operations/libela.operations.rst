Operations
===========

.. raw:: html

   <h1 style="font-size:2.5rem;font-weight:700;margin-bottom:0.2em;">
     <span class="module-label">(libela.operations)</span>
   </h1>

Operations Utilities: Symbolic stress, deformation protocols, and fitting helpers for hyperelastic models.

This module provides symbolic and numeric tools for stress computation, deformation gradient construction, and parameter fitting for all hyperelastic models. It is the core mix-in for all material models in libela.

.. toctree::
   :maxdepth: 1
   :hidden:

   strain_converter
   deformation_gradient_matrix
   uniaxial_solver
   simple_shear_solver
   biaxial_solver

Key Features
------------
- Symbolic stress computation for arbitrary strain-energy functions
- Deformation gradient builders for uniaxial, biaxial, and shear protocols
- Protocol-specific stress solvers
- Parameter fitting (beta)

Classes
--------

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - **Class**
     - **Description & Equation**
     - **API Reference**
   * - operations
     - Core mix-in for symbolic stress, protocol solvers, and fitting utilities for hyperelastic models.

       .. math::

          \boldsymbol\sigma = \frac{2}{J} \left( \frac{\partial W}{\partial I_1} \mathbf{b} - \frac{\partial W}{\partial I_2} \mathbf{b}^{-1} \right) + \text{volumetric terms}
     - :class:`operations`

Functions
----------

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - **Function**
     - **Description & Equation**
     - **API Reference**
   * - strain_converter
     - Converts input strain to principal stretches (λ) for stress evaluation.
     - :func:`strain_converter`
   * - deformation_gradient_matrix
     - Returns symbolic deformation gradient tensor F for a given loading protocol.

       .. math::

          \mathbf{F}_{\text{uniax}} = \begin{bmatrix} \lambda & 0 & 0 \\ 0 & \lambda^{-1/2} & 0 \\ 0 & 0 & \lambda^{-1/2} \end{bmatrix}

       .. math::

          \mathbf{F}_{\text{biax}} = \operatorname{diag}(\lambda_1, \lambda_2, (\lambda_1\lambda_2)^{-1})

       .. math::

          \mathbf{F}_{\text{shear}} = \begin{bmatrix} 1 & \gamma & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
     - :func:`deformation_gradient_matrix`
   * - uniaxial_solver
     - Generates a function to solve for uniaxial stress from a symbolic tensor.
     - :func:`uniaxial_solver`
   * - simple_shear_solver
     - Generates a function to solve for simple shear stress from a symbolic tensor.
     - :func:`simple_shear_solver`
   * - biaxial_solver
     - Generates functions to solve for biaxial stress components from a symbolic tensor.
     - :func:`biaxial_solver`

.. currentmodule:: libela.hyperelastic.operations

.. autoclass:: operations
   :members:
   :show-inheritance:

.. autofunction:: strain_converter
.. autofunction:: deformation_gradient_matrix
.. autofunction:: uniaxial_solver
.. autofunction:: simple_shear_solver
.. autofunction:: biaxial_solver 