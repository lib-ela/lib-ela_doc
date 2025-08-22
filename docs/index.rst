.. _home:

Welcome to **lib-ela**'s documentation!
========================================

.. raw:: html

   <section class="hero-banner" role="banner" aria-label="lib-ela hero">
     <div class="hero-bg" aria-hidden="true"></div>

     <div class="hero-inner">
       <p class="hero-eyebrow">Open-source • Python • Solid Mechanics</p>
       <h2 class="hero-title">Build symbolic solid mechanics in Python</h2>
       <p class="hero-tagline">
         Hyperelastic, viscoelastic, and multiphysics models with ready-to-run examples.
       </p>

       <div class="hero-ctas">
         <a href="user_guide/index.html" class="btn btn-primary"
            aria-label="Open the quick-start guide">Quick-start guide</a>
         <a href="api/index.html" class="btn btn-primary" aria-label="Browse API reference">Browse API</a>
       </div>

       <div class="hero-ctas">
         <a class="btn btn-primary"><code>pip install lib-ela</code></a>
       </div>
       
       <div class="hero-meta">v1.0.0 · Updated 2025-08-20</div>
     </div>
   </section>

Get Started
-----------

.. grid:: 3 3 3 3
   :gutter: 2
   :class-container: grid-home

   .. grid-item-card:: Theory Reference
      :shadow: md
      :class-card: card-mint

      .. raw:: html

         <img src="_static/icons/build.svg" alt="Theory icon" style="width:64px;height:64px;display:block;margin:0 auto 0.5rem auto;"/>

      Derivations, material models, and background formulas for solid mechanics.
      
      +++
      .. button-link:: theory/index.html
         :color: primary
         :expand:

         To the theory pages

   .. grid-item-card:: API Reference
      :shadow: md
      :class-card: card-mint

      .. raw:: html

         <img src="_static/icons/api.svg" alt="API icon" style="width:64px;height:64px;display:block;margin:0 auto 0.5rem auto;"/>

      Documentation of every public module, class, and function.
      
      +++
      .. button-link:: api/index.html
         :color: primary
         :expand:

         To the API guide

   .. grid-item-card:: Developer Guide
      :shadow: md
      :class-card: card-mint

      .. raw:: html

         <img src="_static/icons/dev.svg" alt="Dev icon" style="width:64px;height:64px;display:block;margin:0 auto 0.5rem auto;"/>

      Contribution guidelines, coding style, roadmap, and citation info.

      +++
      .. button-link:: development/index.html
         :color: primary
         :expand:

         To the dev guide    

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   user_guide/index
   theory/tutorials/index
   theory/index
   api/index
   development/index
   