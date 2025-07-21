/**
 * lib-ela docs – small enhancements
 * - Open external links in a new tab only on subpages
 * - Show a "Copied!" toast after copy-button click
 * - Enable smooth scrolling for in-page anchors
 */


  /* 2 & 4 ── Copy-button toast and Ripple effect */
  document.addEventListener("click", function (ev) {
    const target = ev.target;

    // Copy-button toast
    if (target.classList.contains("copybtn")) {
      const toast = document.createElement("div");
      toast.textContent = "Copied!";
      Object.assign(toast.style, {
        position: "fixed",
        bottom: "1.5rem",
        right: "1.5rem",
        padding: ".4rem .8rem",
        background: getComputedStyle(document.documentElement).getPropertyValue('--brand-primary').trim() || '#37C46C', // Fallback color
        color: "#fff",
        borderRadius: "4px",
        opacity: "0",
        transition: "opacity .2s ease",
        zIndex: "9999"
      });
      document.body.appendChild(toast);
      requestAnimationFrame(() => (toast.style.opacity = "1"));
      setTimeout(() => (toast.style.opacity = "0"), 900);
      setTimeout(() => toast.remove(), 1200);
    }

    // Ripple effect on .sd-btn
    const btn = target.closest(".sd-btn");
    if (btn) {
      btn.classList.add("ripple");
      const animationDuration = 450; // Matches CSS animation duration
      setTimeout(() => {
        btn.classList.remove("ripple");
      }, animationDuration);
    }
  });

  /* 3 ── Smooth scroll for in-page anchors */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      const href = this.getAttribute("href");
      const target = href ? document.querySelector(href) : null;
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth" });
        history.pushState(null, "", href);
      } else {
        console.warn(`Smooth scroll target not found for href: ${href}`);
      }
    });
  });

/* Note: Ripple animation is handled in CSS, no additional JS needed here */