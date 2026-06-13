/* =========================================================
   Ojai Valley Landscaping Co. — main.js
   ========================================================= */

(function () {
  'use strict';

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.addEventListener('DOMContentLoaded', function () {
    initStickyHeader();
    initHamburger();
    initSmoothScroll();
    initActiveNavHighlight();
    initFadeIn();
    initFormValidation();
  });

  /* ---------- 1. Sticky header shadow on scroll ---------- */
  function initStickyHeader() {
    const header = document.getElementById('header');
    if (!header) return;

    function onScroll() {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- 2. Hamburger menu toggle ---------- */
  function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');
    if (!hamburger || !nav) return;

    function closeNav() {
      nav.classList.remove('nav-open');
      hamburger.classList.remove('is-active');
      hamburger.setAttribute('aria-expanded', 'false');
    }

    hamburger.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('nav-open');
      hamburger.classList.toggle('is-active', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });

    // Close nav when any nav link is clicked
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeNav);
    });
  }

  /* ---------- 3. Smooth scroll for in-page anchors ---------- */
  function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(function (link) {
      link.addEventListener('click', function (e) {
        const href = link.getAttribute('href');
        if (!href || href === '#') return;

        const target = document.querySelector(href);
        if (!target) return;

        e.preventDefault();
        target.scrollIntoView({
          behavior: prefersReducedMotion ? 'auto' : 'smooth',
          block: 'start'
        });
      });
    });
  }

  /* ---------- 4. Active nav link highlight ---------- */
  function initActiveNavHighlight() {
    const sections = document.querySelectorAll('main section[id]');
    const navLinks = document.querySelectorAll('.nav__link');
    if (!sections.length || !navLinks.length) return;

    const linkMap = {};
    navLinks.forEach(function (link) {
      const id = link.getAttribute('href').slice(1);
      linkMap[id] = link;
    });

    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(function (l) { l.classList.remove('active'); });
          if (linkMap[id]) linkMap[id].classList.add('active');
        }
      });
    }, { threshold: 0.4 });

    sections.forEach(function (section) { observer.observe(section); });
  }

  /* ---------- 5. Scroll-triggered fade-in animations ---------- */
  function initFadeIn() {
    const elements = document.querySelectorAll('.fade-in');
    if (!elements.length) return;

    // Respect reduced motion: show everything immediately
    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      elements.forEach(function (el) { el.classList.add('visible'); });
      return;
    }

    const observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    elements.forEach(function (el) { observer.observe(el); });
  }

  /* ---------- 6. Contact form validation & submission ---------- */
  function initFormValidation() {
    const form = document.getElementById('estimate-form');
    const success = document.getElementById('form-success');
    if (!form || !success) return;

    const requiredFields = ['name', 'phone', 'email', 'address', 'service'];
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function showError(field, message) {
      field.classList.add('has-error');
      const errorEl = form.querySelector('[data-error-for="' + field.id + '"]');
      if (errorEl) {
        errorEl.textContent = message;
        errorEl.classList.add('is-visible');
      }
    }

    function clearError(field) {
      field.classList.remove('has-error');
      const errorEl = form.querySelector('[data-error-for="' + field.id + '"]');
      if (errorEl) {
        errorEl.textContent = '';
        errorEl.classList.remove('is-visible');
      }
    }

    // Clear an individual field's error as the user corrects it
    requiredFields.forEach(function (id) {
      const field = document.getElementById(id);
      if (!field) return;
      field.addEventListener('input', function () { clearError(field); });
      field.addEventListener('change', function () { clearError(field); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      let valid = true;
      let firstInvalid = null;

      requiredFields.forEach(function (id) {
        const field = document.getElementById(id);
        if (!field) return;
        clearError(field);

        const value = field.value.trim();

        if (!value) {
          showError(field, 'This field is required.');
          valid = false;
          if (!firstInvalid) firstInvalid = field;
        } else if (id === 'email' && !emailRegex.test(value)) {
          showError(field, 'Please enter a valid email address.');
          valid = false;
          if (!firstInvalid) firstInvalid = field;
        }
      });

      if (!valid) {
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      // Success: hide form, show success message, scroll to it
      form.setAttribute('hidden', '');
      success.removeAttribute('hidden');
      success.scrollIntoView({
        behavior: prefersReducedMotion ? 'auto' : 'smooth',
        block: 'center'
      });
    });
  }

})();
