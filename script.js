/* ============================================================
   AKHIL AZAD — PORTFOLIO
   Navigation · Scroll reveal · Active section
   ============================================================ */

(function () {

  "use strict";


  /* ================= REDUCED MOTION ================= */

  var reduceMotion =
    window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;


  /* ================= FOOTER YEAR ================= */

  var yearEl =
    document.getElementById("footerYear");

  if (yearEl) {

    yearEl.textContent =
      "© " +
      new Date().getFullYear() +
      " Akhil Azad";

  }


  /* ================= HEADER ================= */

  var header =
    document.getElementById("siteHeader");


  function onScroll() {

    if (!header) return;

    header.classList.toggle(
      "scrolled",
      window.scrollY > 12
    );

  }


  onScroll();

  window.addEventListener(
    "scroll",
    onScroll,
    { passive: true }
  );


  /* ================= MOBILE MENU ================= */

  var toggle =
    document.getElementById("navToggle");

  var mobileNav =
    document.getElementById("mobileNav");


  function closeMenu() {

    if (!toggle || !mobileNav) return;

    toggle.setAttribute(
      "aria-expanded",
      "false"
    );

    toggle.setAttribute(
      "aria-label",
      "Open menu"
    );

    mobileNav.classList.remove("open");

    document.body.classList.remove(
      "menu-open"
    );

  }


  function openMenu() {

    if (!toggle || !mobileNav) return;

    toggle.setAttribute(
      "aria-expanded",
      "true"
    );

    toggle.setAttribute(
      "aria-label",
      "Close menu"
    );

    mobileNav.classList.add("open");

    document.body.classList.add(
      "menu-open"
    );

  }


  if (toggle && mobileNav) {

    toggle.addEventListener(
      "click",
      function () {

        var isOpen =
          toggle.getAttribute(
            "aria-expanded"
          ) === "true";

        if (isOpen) {
          closeMenu();
        } else {
          openMenu();
        }

      }
    );


    mobileNav
      .querySelectorAll("a")
      .forEach(function (link) {

        link.addEventListener(
          "click",
          closeMenu
        );

      });


    document.addEventListener(
      "keydown",
      function (event) {

        if (event.key === "Escape") {
          closeMenu();
        }

      }
    );


    window.addEventListener(
      "resize",
      function () {

        if (window.innerWidth > 760) {
          closeMenu();
        }

      }
    );

  }


  /* ================= SCROLL REVEAL ================= */

  var revealEls =
    Array.prototype.slice.call(
      document.querySelectorAll(".reveal")
    );


  if (
    reduceMotion ||
    !("IntersectionObserver" in window)
  ) {

    revealEls.forEach(
      function (el) {
        el.classList.add("in");
      }
    );

  } else {

    var revealObserver =
      new IntersectionObserver(

        function (entries) {

          entries.forEach(
            function (entry) {

              if (!entry.isIntersecting) {
                return;
              }

              entry.target.classList.add("in");

              revealObserver.unobserve(
                entry.target
              );

            }
          );

        },

        {
          rootMargin:
            "0px 0px -8% 0px",

          threshold: .12
        }

      );


    revealEls.forEach(
      function (el) {

        var parent =
          el.parentElement;

        if (parent) {

          var siblings =
            Array.prototype.slice.call(
              parent.children
            ).filter(
              function (child) {
                return (
                  child.classList &&
                  child.classList.contains("reveal")
                );
              }
            );

          var index =
            siblings.indexOf(el);

          if (index > 0) {

            el.style.transitionDelay =
              Math.min(
                index * 70,
                320
              ) + "ms";

          }

        }

        revealObserver.observe(el);

      }
    );

  }


  /* ================= ACTIVE NAV ================= */

  var sections =
    Array.prototype.slice.call(
      document.querySelectorAll(
        "main section[id]"
      )
    );


  var navLinks =
    Array.prototype.slice.call(
      document.querySelectorAll(
        ".primary-nav a"
      )
    );


  var linkById = {};


  navLinks.forEach(
    function (link) {

      var href =
        link.getAttribute("href");

      if (!href) return;

      var id =
        href.replace("#", "");

      linkById[id] = link;

    }
  );


  if (
    "IntersectionObserver" in window &&
    sections.length
  ) {

    var current = null;


    var spyObserver =
      new IntersectionObserver(

        function (entries) {

          entries.forEach(
            function (entry) {

              if (!entry.isIntersecting) {
                return;
              }

              var id =
                entry.target.id;

              if (id === current) {
                return;
              }

              current = id;


              navLinks.forEach(
                function (link) {

                  link.classList.remove(
                    "active"
                  );

                }
              );


              if (linkById[id]) {

                linkById[id]
                  .classList
                  .add("active");

              }

            }
          );

        },

        {
          rootMargin:
            "-45% 0px -50% 0px",

          threshold: 0
        }

      );


    sections.forEach(
      function (section) {

        spyObserver.observe(section);

      }
    );

  }


})();