/* Ayush Kumar — site interactions */
(() => {
  "use strict";

  /* ------------------------------------------------------------------------
     Light / dark theme
     ------------------------------------------------------------------------ */
  const themeButton = document.getElementById("theme-toggle");

  if (themeButton) {
    const root = document.documentElement;
    const themeColor = document.querySelector('meta[name="theme-color"]');

    const applyTheme = (theme, persist) => {
      root.dataset.theme = theme;
      if (persist) {
        try { localStorage.setItem("theme", theme); } catch {}
      }
      const isLight = theme === "light";
      themeButton.setAttribute("aria-pressed", String(isLight));
      themeButton.setAttribute("aria-label", isLight ? "Switch to dark mode" : "Switch to light mode");
      if (themeColor) themeColor.content = isLight ? "#f7f5f0" : "#000000";
    };

    applyTheme(root.dataset.theme === "light" ? "light" : "dark", false);
    themeButton.addEventListener("click", () => {
      applyTheme(root.dataset.theme === "light" ? "dark" : "light", true);
    });
  }

  /* ------------------------------------------------------------------------
     Dropdown menu
     ------------------------------------------------------------------------ */
  const menu = document.getElementById("site-menu");
  const menuButton = document.getElementById("menu-open");

  if (menu && menuButton) {
    const setMenuOpen = (open) => {
      menu.classList.toggle("is-open", open);
      menu.inert = !open;
      menuButton.setAttribute("aria-expanded", String(open));
      menuButton.setAttribute("aria-label", open ? "Close site menu" : "Open site menu");
    };

    menuButton.addEventListener("click", () => {
      setMenuOpen(!menu.classList.contains("is-open"));
    });

    menu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setMenuOpen(false));
    });

    document.addEventListener("click", (event) => {
      if (!menu.classList.contains("is-open")) return;
      if (menu.contains(event.target) || menuButton.contains(event.target)) return;
      setMenuOpen(false);
    });

    document.addEventListener("keydown", (event) => {
      if (event.key !== "Escape" || !menu.classList.contains("is-open")) return;
      setMenuOpen(false);
      menuButton.focus();
    });
  }

  /* ------------------------------------------------------------------------
     Reveal sections as they enter the viewport
     ------------------------------------------------------------------------ */
  const revealItems = Array.from(document.querySelectorAll(".reveal"));
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!revealItems.length) {
    // nothing to do
  } else if (!("IntersectionObserver" in window) || prefersReducedMotion) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else {
    document.documentElement.classList.add("js");
    const observer = new IntersectionObserver(
      (entries, io) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -7% 0px", threshold: 0.08 }
    );

    revealItems.forEach((item) => observer.observe(item));
  }

  /* ------------------------------------------------------------------------
     Footer year
     ------------------------------------------------------------------------ */
  const year = document.getElementById("year");
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
