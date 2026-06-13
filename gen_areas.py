#!/usr/bin/env python3
"""Generate individual service-area pages for Ojai Landscape Solutions"""
import os

AREAS = [
    {
        "slug": "ojai",
        "name": "Ojai",
        "meta_title": "Landscaping in Ojai, CA | Ojai Landscape Solutions",
        "meta_desc": "Professional landscaping, lawn care, irrigation, tree trimming, and fire clearance in Ojai, CA. Locally owned, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Our home base. Full-service landscaping for residential and commercial properties throughout downtown Ojai and the surrounding neighborhoods.",
        "p1": "Ojai is where it all started for us back in 2009, and it's still the heart of everything we do. From the historic homes along Ojai Avenue to the estates tucked into the East End, we know this town's soil, light, and seasonal rhythms better than anyone.",
        "p2": "Whether you manage a downtown storefront, a boutique inn, or a family home in the foothills, our local crews deliver dependable, water-smart landscaping that keeps your property looking its best all year long.",
        "services_intro": "Everything your Ojai property needs, from weekly upkeep to a complete landscape transformation.",
        "cta_heading": "Ready to Transform Your Ojai Property?",
        "cta_text": "Tell us about your project and we'll get back to you within 24 hours with a free, no-obligation estimate.",
    },
    {
        "slug": "meiners-oaks",
        "name": "Meiners Oaks",
        "meta_title": "Landscaping in Meiners Oaks, CA | Ojai Landscape Solutions",
        "meta_desc": "Lawn care, tree trimming, and landscape design in Meiners Oaks, CA. Local, licensed & insured Ojai Valley landscapers. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Lawn care, tree trimming, and custom landscape design for this charming community just west of Ojai.",
        "p1": "Meiners Oaks has a relaxed, tree-lined character all its own, and we love working here. Our crews care for the mature oaks, sycamores, and citrus that give the neighborhood its shade and personality.",
        "p2": "From tidy front-yard maintenance to full backyard redesigns with drought-tolerant natives, we help Meiners Oaks homeowners get the most out of their properties without fighting the local climate.",
        "services_intro": "Reliable, neighborly landscaping tailored to Meiners Oaks homes and lots.",
        "cta_heading": "Let's Make Your Meiners Oaks Yard Shine",
        "cta_text": "Request a free estimate and we'll be in touch within 24 hours.",
    },
    {
        "slug": "oak-view",
        "name": "Oak View",
        "meta_title": "Landscaping in Oak View, CA | Ojai Landscape Solutions",
        "meta_desc": "Full-service landscaping and maintenance in Oak View, CA and along Highway 33. Locally owned, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Full-service landscaping and maintenance for homes in Oak View and along the Highway 33 corridor.",
        "p1": "Oak View sits right between Ojai and the coast, and its properties range from compact suburban lots to larger parcels backing up to open space. We tailor our work to each, keeping things clean, healthy, and easy to maintain.",
        "p2": "Regular lawn care, irrigation tune-ups, tree work, and hardscape projects — our Oak View clients count on us to show up on time and leave the property better than we found it.",
        "services_intro": "Dependable landscaping for Oak View's homes and neighborhoods.",
        "cta_heading": "Get Started on Your Oak View Project",
        "cta_text": "Send us a few details and receive a free estimate within 24 hours.",
    },
    {
        "slug": "casitas-springs",
        "name": "Casitas Springs",
        "meta_title": "Landscaping in Casitas Springs, CA | Ojai Landscape Solutions",
        "meta_desc": "Lawn maintenance, cleanups, and hardscape work in Casitas Springs, CA near Lake Casitas. Local, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Lawn maintenance, cleanups, and hardscape work for properties along the lower valley near Lake Casitas.",
        "p1": "Casitas Springs is a quiet, close-knit community in the lower Ojai Valley, and its properties often blend manicured yards with the surrounding natural landscape. We help homeowners strike that balance beautifully.",
        "p2": "From routine mowing and seasonal cleanups to new patios and pathways, our crews bring the same care and reliability to every Casitas Springs property, large or small.",
        "services_intro": "Practical, polished landscaping for the lower valley corridor.",
        "cta_heading": "Improve Your Casitas Springs Property",
        "cta_text": "Reach out for a free, no-pressure estimate — we respond within 24 hours.",
    },
    {
        "slug": "upper-ojai",
        "name": "Upper Ojai",
        "meta_title": "Landscaping & Fire Clearance in Upper Ojai, CA | Ojai Landscape Solutions",
        "meta_desc": "Rural property maintenance, brush clearing, fire clearance, and irrigation in Upper Ojai, CA. Local, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Rural property maintenance, brush clearing, fire clearance, and irrigation for hillside and ranch-style homes.",
        "p1": "Upper Ojai's ranches, orchards, and hillside homes come with their own set of needs — and their own fire-season realities. We specialize in keeping large rural properties healthy, productive, and defensible.",
        "p2": "Defensible-space brush clearing, weed abatement, hillside irrigation, and tree work are everyday jobs for our Upper Ojai crews. We know the terrain, the regulations, and what it takes to protect a property out here.",
        "services_intro": "Specialized rural and fire-conscious landscaping for the upper valley.",
        "cta_heading": "Protect and Beautify Your Upper Ojai Property",
        "cta_text": "Ask about fire clearance and rural maintenance — free estimate within 24 hours.",
    },
    {
        "slug": "lake-casitas",
        "name": "Lake Casitas",
        "meta_title": "Water-Wise Landscaping near Lake Casitas, CA | Ojai Landscape Solutions",
        "meta_desc": "Water-wise landscape design and maintenance near Lake Casitas and Casitas Municipal Water District. Local, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Water-wise landscape design and maintenance for properties near the lake and Casitas Municipal Water District service areas.",
        "p1": "Living near Lake Casitas means being especially mindful of how every drop is used. We design and maintain landscapes that stay beautiful while respecting the area's water resources and district guidelines.",
        "p2": "From efficient drip irrigation and smart controllers to drought-tolerant native plantings, our Lake Casitas clients enjoy lush, low-water yards that look great and keep utility bills down.",
        "services_intro": "Beautiful, water-smart landscaping for the Lake Casitas area.",
        "cta_heading": "Create a Water-Wise Landscape You'll Love",
        "cta_text": "Get a free estimate for water-smart design and maintenance within 24 hours.",
    },
    {
        "slug": "matilija-canyon",
        "name": "Matilija Canyon",
        "meta_title": "Hillside & Native Landscaping in Matilija Canyon | Ojai Landscape Solutions",
        "meta_desc": "Rural and hillside landscaping, erosion control, and native planting in Matilija Canyon. Local, licensed & insured. Call 805-500-2384 for a free estimate.",
        "hero_sub": "Specialty rural and hillside landscaping, erosion control, and native planting for this scenic canyon corridor.",
        "p1": "Matilija Canyon is one of the most beautiful — and most challenging — places to maintain a property in the valley. Steep slopes, native chaparral, and seasonal water all call for a careful, experienced hand.",
        "p2": "We focus on erosion control, native and fire-resistant planting, brush management, and the kind of low-impact landscaping that works with the canyon rather than against it.",
        "services_intro": "Thoughtful, terrain-aware landscaping for canyon properties.",
        "cta_heading": "Care for Your Matilija Canyon Property",
        "cta_text": "Tell us about your site and we'll send a free estimate within 24 hours.",
    },
]

# Dropdown links shared by all pages (sibling pages live in the same folder)
DROPDOWN = [
    ("ojai.html", "Ojai"),
    ("meiners-oaks.html", "Meiners Oaks"),
    ("oak-view.html", "Oak View"),
    ("casitas-springs.html", "Casitas Springs"),
    ("upper-ojai.html", "Upper Ojai"),
    ("lake-casitas.html", "Lake Casitas"),
    ("matilija-canyon.html", "Matilija Canyon"),
]

SERVICES = [
    ("Lawn Mowing &amp; Maintenance",
     "Regular mowing, edging, blowing, and trimming to keep your lawn clean and healthy through every season."),
    ("Landscape Design &amp; Installation",
     "Custom designs that complement Ojai's natural terrain, from drought-tolerant natives to lush ornamental gardens."),
    ("Irrigation &amp; Drip Systems",
     "Water-smart irrigation installation and repair tailored to the valley's warm, dry climate and water restrictions."),
    ("Tree Trimming &amp; Removal",
     "Safe, professional pruning and removal of oaks, citrus, eucalyptus, and more. ISA-certified arborist on staff."),
    ("Hardscape &amp; Outdoor Living",
     "Patios, pathways, retaining walls, and outdoor living spaces built for the valley's rustic aesthetic."),
    ("Fire Clearance &amp; Brush Removal",
     "Pre-fire season brush clearing, weed abatement, and defensible space maintenance for hillside and rural properties."),
]


def dropdown_html(current_slug):
    items = []
    for href, label in DROPDOWN:
        aria = ' aria-current="page"' if href == current_slug + ".html" else ""
        items.append(
            '              <li><a href="%s" class="nav__sublink"%s>%s</a></li>' % (href, aria, label)
        )
    return "\n".join(items)


def services_html():
    cards = []
    for title, desc in SERVICES:
        cards.append(
            "          <article class=\"card area-feature fade-in\">\n"
            "            <h3 class=\"service-card__title\">%s</h3>\n"
            "            <p class=\"service-card__desc\">%s</p>\n"
            "            <a href=\"#contact\" class=\"card__link\">Get a Quote &rarr;</a>\n"
            "          </article>" % (title, desc)
        )
    return "\n".join(cards)


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>@@META_TITLE@@</title>
  <meta name="description" content="@@META_DESC@@">
  <meta property="og:title" content="@@META_TITLE@@">
  <meta property="og:description" content="@@META_DESC@@">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://www.ojaivalleylandscaping.com/areas/@@SLUG@@.html">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>

  <!-- ============================= HEADER ============================= -->
  <header id="header">
    <div class="container header__inner">
      <a href="../index.html" class="logo" aria-label="Ojai Landscape Solutions home">
        <svg class="logo__leaf" viewBox="0 0 32 32" width="28" height="28" aria-hidden="true">
          <path d="M16 2C9 7 4 13 4 21c0 5 4 9 9 9 8 0 15-7 15-18 0-4-1-7-2-10-3 3-6 4-10 4-2 0-3-2-0-4z" fill="var(--color-sage)"/>
          <path d="M14 28C14 20 18 12 26 6" fill="none" stroke="var(--color-sage-dark)" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
        <span class="logo__text">Ojai Landscape Solutions</span>
      </a>

      <nav class="nav" id="nav" aria-label="Main navigation">
        <ul class="nav__list">
          <li><a href="../index.html#hero" class="nav__link">Home</a></li>
          <li><a href="../index.html#services" class="nav__link">Services</a></li>
          <li><a href="../index.html#gallery" class="nav__link">Our Work</a></li>
          <li><a href="../index.html#why-us" class="nav__link">About Us</a></li>
          <li class="nav__item nav__item--dropdown">
            <a href="../index.html#service-areas" class="nav__link nav__dropdown-toggle" aria-haspopup="true" aria-expanded="false">Service Areas <span class="nav__caret" aria-hidden="true">&#9662;</span></a>
            <ul class="nav__dropdown">
@@DROPDOWN@@
            </ul>
          </li>
          <li><a href="../index.html#testimonials" class="nav__link">Testimonials</a></li>
          <li><a href="#contact" class="nav__link">Contact</a></li>
          <li class="nav__cta-item"><a href="#contact" class="btn btn--terracotta nav__cta">Get a Free Quote</a></li>
        </ul>
      </nav>

      <a href="tel:+18055002384" class="header__phone">805-500-2384</a>

      <button class="hamburger" id="hamburger" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="nav">
        <span class="hamburger__line"></span>
        <span class="hamburger__line"></span>
        <span class="hamburger__line"></span>
      </button>
    </div>
  </header>

  <main>

    <!-- ============================= AREA HERO ============================= -->
    <section class="hero area-hero fade-in">
      <div class="hero__overlay"></div>
      <div class="container hero__content">
        <p class="eyebrow eyebrow--gold">SERVICE AREA</p>
        <h1 class="hero__title">Landscaping Services in @@NAME@@</h1>
        <p class="hero__subtitle">@@HERO_SUB@@</p>
        <div class="hero__buttons">
          <a href="#contact" class="btn btn--terracotta btn--lg">Get a Free Estimate</a>
          <a href="../index.html#services" class="btn btn--outline btn--lg">See All Services</a>
        </div>
      </div>
    </section>

    <!-- ============================= INTRO ============================= -->
    <section class="section section--cream fade-in">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../index.html">Home</a> &rsaquo; <a href="../index.html#service-areas">Service Areas</a> &rsaquo; <span>@@NAME@@</span>
        </nav>
        <div class="section__head">
          <p class="eyebrow eyebrow--terracotta">LOCAL LANDSCAPING</p>
          <h2 class="section__title">Your @@NAME@@ Landscaping Team</h2>
        </div>
        <div class="area-intro">
          <p>@@P1@@</p>
          <p>@@P2@@</p>
        </div>
      </div>
    </section>

    <!-- ============================= SERVICES IN AREA ============================= -->
    <section class="section section--white fade-in">
      <div class="container">
        <div class="section__head">
          <p class="eyebrow eyebrow--terracotta">WHAT WE DO</p>
          <h2 class="section__title">Services We Provide in @@NAME@@</h2>
          <p class="section__subtitle">@@SERVICES_INTRO@@</p>
        </div>
        <div class="grid grid--3">
@@SERVICES@@
        </div>
      </div>
    </section>

    <!-- ============================= LOCAL CTA ============================= -->
    <section class="section section--olive fade-in">
      <div class="container area-cta">
        <p class="eyebrow eyebrow--gold">FREE ESTIMATE</p>
        <h2 class="section__title section__title--light">@@CTA_HEADING@@</h2>
        <p>@@CTA_TEXT@@</p>
        <a href="#contact" class="btn btn--terracotta btn--lg">Request Your Free Estimate</a>
      </div>
    </section>

    <!-- ============================= CONTACT ============================= -->
    <section id="contact" class="contact fade-in">
      <div class="contact__inner">

        <div class="contact__info">
          <p class="eyebrow eyebrow--gold">GET IN TOUCH</p>
          <h2 class="section__title section__title--light">Get Your Free @@NAME@@ Estimate</h2>
          <p class="contact__subtext">Serving @@NAME@@ and the entire Ojai Valley. Contact us today and we'll get back to you within 24 hours.</p>

          <ul class="contact__details">
            <li class="contact__detail">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6 3a2 2 0 0 0-2 2c0 8 7 15 15 15a2 2 0 0 0 2-2v-3a1 1 0 0 0-.8-1l-4-1a1 1 0 0 0-1 .3l-1.4 1.4a13 13 0 0 1-5.5-5.5l1.4-1.4a1 1 0 0 0 .3-1l-1-4A1 1 0 0 0 8 3z" fill="none" stroke="var(--color-gold)" stroke-width="1.8" stroke-linejoin="round"/></svg>
              <a href="tel:+18055002384">805-500-2384</a>
            </li>
            <li class="contact__detail">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="var(--color-gold)" stroke-width="1.8"/><path d="M4 7l8 6 8-6" fill="none" stroke="var(--color-gold)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <a href="mailto:info@ojaivalleylandscaping.com">info@ojaivalleylandscaping.com</a>
            </li>
            <li class="contact__detail">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 2C8 2 5 5 5 9c0 5 7 13 7 13s7-8 7-13c0-4-3-7-7-7z" fill="none" stroke="var(--color-gold)" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="9" r="2.5" fill="none" stroke="var(--color-gold)" stroke-width="1.8"/></svg>
              <span>Serving @@NAME@@, CA</span>
            </li>
            <li class="contact__detail">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="var(--color-gold)" stroke-width="1.8"/><path d="M12 7v5l3 2" fill="none" stroke="var(--color-gold)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span>Mon–Fri 7am–6pm | Sat 8am–4pm | Sun: Emergency calls only</span>
            </li>
          </ul>

          <p class="contact__license">CA Contractor's License #XXXXXX | Licensed &amp; Insured</p>
        </div>

        <div class="contact__form-panel">
          <form class="form" id="estimate-form" novalidate>
            <div class="form__group">
              <label for="name" class="form__label">Full Name <span class="req">*</span></label>
              <input type="text" id="name" name="name" class="form__input" required>
              <span class="form__error" data-error-for="name"></span>
            </div>

            <div class="form__group">
              <label for="phone" class="form__label">Phone Number <span class="req">*</span></label>
              <input type="tel" id="phone" name="phone" class="form__input" required>
              <span class="form__error" data-error-for="phone"></span>
            </div>

            <div class="form__group">
              <label for="email" class="form__label">Email Address <span class="req">*</span></label>
              <input type="email" id="email" name="email" class="form__input" required>
              <span class="form__error" data-error-for="email"></span>
            </div>

            <div class="form__group">
              <label for="address" class="form__label">Service Address / City <span class="req">*</span></label>
              <input type="text" id="address" name="address" class="form__input" required>
              <span class="form__error" data-error-for="address"></span>
            </div>

            <div class="form__group">
              <label for="service" class="form__label">Service Needed <span class="req">*</span></label>
              <select id="service" name="service" class="form__input form__select" required>
                <option value="">-- Select a Service --</option>
                <option value="Lawn Mowing &amp; Maintenance">Lawn Mowing &amp; Maintenance</option>
                <option value="Landscape Design &amp; Installation">Landscape Design &amp; Installation</option>
                <option value="Irrigation &amp; Drip Systems">Irrigation &amp; Drip Systems</option>
                <option value="Tree Trimming &amp; Removal">Tree Trimming &amp; Removal</option>
                <option value="Hardscape &amp; Outdoor Living">Hardscape &amp; Outdoor Living</option>
                <option value="Fire Clearance &amp; Brush Removal">Fire Clearance &amp; Brush Removal</option>
                <option value="Other / Not Sure Yet">Other / Not Sure Yet</option>
              </select>
              <span class="form__error" data-error-for="service"></span>
            </div>

            <div class="form__group">
              <label for="message" class="form__label">Message / Additional Details</label>
              <textarea id="message" name="message" class="form__input form__textarea" rows="5"></textarea>
            </div>

            <button type="submit" class="btn btn--terracotta form__submit">Request My Free Estimate</button>
          </form>

          <div class="form__success" id="form-success" hidden>
            <span class="form__success-check" aria-hidden="true">&#10003;</span>
            <p>Thank you! We received your request and will be in touch within 24 hours. For urgent needs, call us at <a href="tel:+18055002384">805-500-2384</a>.</p>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- ============================= FOOTER ============================= -->
  <footer class="footer">
    <div class="container footer__grid">

      <div class="footer__col footer__brand">
        <p class="footer__logo">Ojai Landscape Solutions</p>
        <p class="footer__tagline">Rooted in the Valley. Committed to Your Property.</p>
        <p class="footer__license">CA Contractor's License #XXXXXX | Licensed &amp; Insured</p>
      </div>

      <div class="footer__col">
        <h4 class="footer__label">Services</h4>
        <ul class="footer__links">
          <li><a href="../index.html#services">Lawn Mowing &amp; Maintenance</a></li>
          <li><a href="../index.html#services">Landscape Design</a></li>
          <li><a href="../index.html#services">Irrigation &amp; Drip Systems</a></li>
          <li><a href="../index.html#services">Tree Trimming &amp; Removal</a></li>
          <li><a href="../index.html#services">Hardscape &amp; Outdoor Living</a></li>
          <li><a href="../index.html#services">Fire Clearance &amp; Brush Removal</a></li>
        </ul>
      </div>

      <div class="footer__col">
        <h4 class="footer__label">Service Areas</h4>
        <ul class="footer__links">
          <li><a href="ojai.html">Ojai</a></li>
          <li><a href="meiners-oaks.html">Meiners Oaks</a></li>
          <li><a href="upper-ojai.html">Upper Ojai</a></li>
          <li><a href="oak-view.html">Oak View</a></li>
          <li><a href="casitas-springs.html">Casitas Springs</a></li>
          <li><a href="lake-casitas.html">Lake Casitas Area</a></li>
          <li><a href="matilija-canyon.html">Matilija Canyon</a></li>
          <li><a href="../index.html#service-areas">Sulphur Mountain / El Roblar</a></li>
        </ul>
      </div>

      <div class="footer__col">
        <h4 class="footer__label">Contact Us</h4>
        <ul class="footer__contact">
          <li><a href="tel:+18055002384">805-500-2384</a></li>
          <li><a href="mailto:info@ojaivalleylandscaping.com">info@ojaivalleylandscaping.com</a></li>
          <li>Ojai, CA 93023</li>
        </ul>
        <div class="footer__social">
          <a href="#" class="social-icon" aria-label="Facebook">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M14 9h3V5h-3c-2.2 0-4 1.8-4 4v2H7v4h3v6h4v-6h3l1-4h-4V9a1 1 0 0 1 1-1z" fill="currentColor"/></svg>
          </a>
          <a href="#" class="social-icon" aria-label="Instagram">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17" cy="7" r="1.2" fill="currentColor"/></svg>
          </a>
          <a href="#" class="social-icon" aria-label="Nextdoor">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M4 20v-8l8-6 8 6v8h-5v-6h-6v6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>

    </div>

    <div class="footer__bottom">
      <p>&copy; 2025 Ojai Landscape Solutions All Rights Reserved. &nbsp;|&nbsp; <a href="#">Privacy Policy</a> &nbsp;|&nbsp; <a href="#">Terms of Service</a></p>
    </div>
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>
"""

os.makedirs("areas", exist_ok=True)

for area in AREAS:
    html = TEMPLATE
    replacements = {
        "@@META_TITLE@@": area["meta_title"],
        "@@META_DESC@@": area["meta_desc"],
        "@@SLUG@@": area["slug"],
        "@@NAME@@": area["name"],
        "@@HERO_SUB@@": area["hero_sub"],
        "@@P1@@": area["p1"],
        "@@P2@@": area["p2"],
        "@@SERVICES_INTRO@@": area["services_intro"],
        "@@CTA_HEADING@@": area["cta_heading"],
        "@@CTA_TEXT@@": area["cta_text"],
        "@@DROPDOWN@@": dropdown_html(area["slug"]),
        "@@SERVICES@@": services_html(),
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    path = os.path.join("areas", area["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", path)

print("Done.")
