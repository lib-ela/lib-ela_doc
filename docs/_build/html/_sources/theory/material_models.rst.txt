.. _material_models:

Material Model Catalogue
========================

All closed-form constitutive functions available (or planned) in **lib-ela**.
Use this page when selecting or fitting a model to experimental data.

.. contents::
   :local:
   :depth: 1


Hyperelastic
------------
*Strain–energy forms available in* **lib-ela**

.. list-table::
   :header-rows: 1
   :widths: 22 52 26
   :class: sd-table

   * - **Model**
     - **Energy density** :math:`W`
     - **Parameters**

   * - **Neo-Hookean** *(C / NI)*
     - :math:`W = \frac{\mu}{2}(I_1-3)`  
       :math:`W_{\mathrm{NI}} = \frac{\mu}{2}(\bar I_1-3) + W_{\mathrm{vol}}`
     - :math:`\mu`, :math:`K`

   * - **Mooney–Rivlin** *(C / NI)*
     - :math:`W = C_1(\bar I_1-3) + C_2(\bar I_2-3) + W_{\mathrm{vol}}`
     - :math:`C_1`, :math:`C_2`, :math:`K`

   * - **Ogden** *N-term* *(C / NI)*
     - :math:`W = \sum_{i=1}^{N} \frac{\mu_i}{\alpha_i} \left(\lambda_1^{\alpha_i} + \lambda_2^{\alpha_i} + \lambda_3^{\alpha_i} - 3\right) + W_{\mathrm{vol}}`
     - :math:`\mu_i`, :math:`\alpha_i`, :math:`K`

   * - **Yeoh** *p = 3* *(C / NI)*
     - :math:`W = \sum_{i=1}^{3} C_i (\bar I_1-3)^i + W_{\mathrm{vol}}`
     - :math:`C_1`, :math:`C_2`, :math:`C_3`, :math:`K`

   * - **Polynomial** *(general, C / NI)*
     - :math:`W = \sum_{p,q} C_{pq} (\bar I_1-3)^p (\bar I_2-3)^q + W_{\mathrm{vol}}`
     - :math:`C_{pq}`, :math:`K`

.. admonition:: Symbols & notation

   * :math:`I_1 = \mathrm{tr}\,\mathbf{C}`, :math:`\bar I_k` are isochoric invariants  
   * :math:`\bar{\mathbf{C}} = J^{-2/3}\,\mathbf{C}`, :math:`J = \det\mathbf{F}`  
   * Volumetric term: :math:`W_{\mathrm{vol}} = \frac{K}{2}(J-1)^2`  
   * **C** = compressible form (no :math:`K`), **NI** = nearly-incompressible (:math:`K \gg \mu`; typically :math:`K \approx 100\mu`)

Viscoelastic — *beta*
---------------------

These models combine a hyperelastic spring with rheological dashpots.
The symbolic core is stable; parameter-fitting utilities are still under
active development.

.. list-table::
   :header-rows: 1
   :widths: 25 55 20

   * - **Model**
     - **Constitutive idea**
     - **Status**

   * - Generalised-Maxwell (Prony-series)
     - Instantaneous hyperelastic spring in parallel with :math:`n` Maxwell
       elements → hereditary integral in stress
     - *beta*

   * - Standard Linear Solid (SLS)
     - Hyperelastic spring in parallel with a spring–dashpot Maxwell branch
     - *beta*

Multiphysics — *coming soon*
----------------------------

Coupled formulations that add temperature, diffusion, or electric-field
effects to the mechanical response. Symbolic infrastructure is designed;
numerical validation is in progress.

.. list-table::
   :header-rows: 1
   :widths: 25 55 20

   * - **Model**
     - **Coupled fields**
     - **Status**

   * - Thermo-hyperelastic
     - Temperature-dependent :math:`W(T,\mathbf{C})`
     - *coming soon*

   * - Electro-active elastomers
     - Electric enthalpy :math:`\Psi(\mathbf{C},\mathbf{E})`
     - *coming soon*

   * - Diffusion-deformation
     - Chemical potential and swelling strains
     - *coming soon*

Choosing a model
----------------
* **Rubbers (λ ≲ 1.5)** → Mooney–Rivlin (two parameters).  
* **Large strains (λ ≳ 2)** → Yeoh p = 3 or Ogden 3-term.  
* **Rate effects** → Generalised-Maxwell (**beta**).  
* **Actuated / smart materials** → Multiphysics (coming soon).

Fitting tips
------------
* Start from the **small-strain shear modulus** :math:`\mu = G_0`.  
* For NI data fix :math:`K` (e.g. :math:`100\mu`) to reduce correlations.  
* Use ``libela.fitting.hyper_elastic_fit`` (trust-region core, error bars).

External resources
------------------
* Boyce & Ogden (2020) — *Prog. Mater. Sci.* **113**, 100703.  
* Gent (1996) — *Rubber Chem. Technol.* **69**, 59–61.

---

† *Nearly-incompressible* versions use a volumetric–isochoric split and are
enabled automatically by mixing in
:class:`libela.hyperelastic.NearlyIncompressibleMixin`.