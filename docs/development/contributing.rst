.. _contributing:

Contributing
=============

Whether you want to fix a typo or implement an entire material model, this 
page will help you get started. Please read the guidelines below before 
submitting a pull request.


1. Workflow overview
--------------------

#. **Fork** the repository on GitHub and create a topic branch:

   .. code-block:: console

      git checkout -b feat/new-material

#. **Develop** and keep the code **black**-formatted:

   .. code-block:: console

      pip install -e .[dev]          # installs lib-ela plus dev tools
      pre-commit install             # auto-runs black, isort, flake8

#. **Test**:

   .. code-block:: console

      pytest -q
      python -m pip install -r docs/requirements.txt
      make -C docs html

#. **Commit** using Conventional Commits:

   *feat(material): add compressible Ogden model*

#. **Open a pull-request** and fill in the PR template.
   GitHub Actions will run the unit tests and build the docs.


2. Code style
-------------

* **PEP 8** + **black** + **isort**.
* Type-hints **everywhere**.  Sphinx shows them via
  ``sphinx_autodoc_typehints``.
* Public functions/classes need a **NumPy docstring** (see existing
  hyperelastic modules for examples).


3. Directory layout
-------------------

::

    libela/
      hyperelastic/            # finished
      viscoelastic/            # WIP – leave a TODO stub
      multiphysics/
    tests/
      hyperelastic/ …
    docs/
      <rst + notebooks>

Use a **sub-package per physics domain** and keep helpers that cross
domains (e.g. tensor utilities) in ``libela/core``.


4. Adding a new material model
------------------------------

1. Create ``libela/hyperelastic/<model_name>.py``.
2. Sub-class :class:`libela.hyperelastic.operations.operations`.
3. Implement ``energy(self)`` and, if needed, override ``stress()``.
4. Add **pytest** file in ``tests/hyperelastic/`` covering:

   * Incompressible limit
   * Compressible curve vs. literature values

5. Document the model under
   ``docs/theory/material_models/<model_name>.rst`` and update the
   toctree.


5. Writing documentation
------------------------

* Use **reStructuredText**; Markdown is fine for quick notes but convert
  to ``.rst`` before merging.
* Inline math: ``:math:`...````, display math: ``.. math::``.
* Screenshots or diagrams → ``docs/_static``.
* Build locally via ``make -C docs html``; the **Furo** theme reloads
  automatically.


6. Running the test-suite
-------------------------

.. code-block:: console

   pytest -q
   # Run a single file
   pytest tests/hyperelastic/test_neohookean.py -vv

CI uses Python 3.10 → 3.13 on Ubuntu and macOS.  Keep tests under
10 seconds each.


7. Communication
----------------

* **Bug & feature requests** – open a GitHub *Issue*.
* Quick questions – start a **GitHub Discussion**.
* Security reports – e-mail the maintainers (see ``AUTHORS``).

Happy coding – and thank you for improving **lib-ela**!
