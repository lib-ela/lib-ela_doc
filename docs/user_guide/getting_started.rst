.. _getting_started:

Getting Started
===============

This quick-start takes you from **pip install** to your first
stress–strain plot in under a minute.

.. note::

   This walkthrough is available as both a Jupyter notebook (for interactive use) and a web-friendly page (for quick reading):

   - .. raw:: html

        <a class="sd-btn sd-btn-primary" href="getting_started_notebook.ipynb" download style="margin:0.5em 0;display:inline-block;">⬇️ Download the Jupyter Notebook Walkthrough</a>

   - :doc:`Read the Getting Started Walkthrough online <getting_started_notebook>`

.. contents:: On this page
   :local:
   :depth: 1

Install
-------

Create a fresh virtual environment and grab the latest release plus the
optional Jupyter extras:

.. code-block:: console

   python -m pip install --upgrade pip
   python -m pip install "lib-ela[notebook]"

Hello, Neo-Hookean
------------------

Paste the snippet below into a Python prompt or notebook cell:

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from libela.hyperelastic import neohookean

   # material parameters (Pa)
   MU, K = 1.2e6, 2.4e6
   model = neohookean(compressible=True)

   lam   = np.linspace(1.0, 1.5, 100)                 # uniaxial stretch
   sigma = model.stress(lam, params=[K, MU], protocol="uniaxial")

   plt.plot(lam, sigma)
   plt.xlabel(r"$\lambda$")
   plt.ylabel(r"$\sigma_{11}$ [Pa]")
   plt.show()

Next steps
----------

* :doc:`/theory/index` – tensor notation, invariants, derivations  
* :doc:`/api/index` – full class-by-class API reference  
* :doc:`/development/roadmap` – upcoming features beyond hyperelasticity
