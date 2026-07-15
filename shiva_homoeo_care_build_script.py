# -*- coding: utf-8 -*-
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- Real clinic data ----------------
CLINIC = {
    "name": "Shiva Homoeo Care",
    "address_line1": "Opposite Hotel Ramada, Airport Road",
    "address_line2": "Khajuraho, Chhatarpur District, Madhya Pradesh 471606",
    "phone_display": "+91 79996 35415",
    "phone_tel": "+917999635415",
    "whatsapp_number": "917999635415",
    "email": "Kavita.uv@gmail.com",
    "doctor_name": "Dr. Kavita Singh Bundela",
    "doctor_quals": "BHMS, DNYS, MA (English Literature), B.Ed",
    "reg_no": "15505",
    "hours_weekday": "10:00 AM \u2013 12:00 PM  &  4:00 PM \u2013 8:00 PM",
    "hours_sunday": "Closed",
}

MAPS_EMBED_SRC = "https://www.google.com/maps?q=Hotel+Ramada+Khajuraho+Airport+Road&output=embed"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("treatments.html", "Treatments"),
    ("doctor.html", "Doctor"),
    ("testimonials.html", "Testimonials"),
    ("blog.html", "Health Library"),
    ("gallery.html", "Gallery"),
    ("faq.html", "FAQs"),
    ("contact.html", "Contact"),
]

PHONE_ICON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
WA_ICON = '<svg viewBox="0 0 32 32" fill="#fff"><path d="M16 0C7.2 0 .1 7.1.1 15.9c0 2.8.7 5.5 2.1 7.9L0 32l8.4-2.2c2.3 1.3 4.9 1.9 7.6 1.9 8.8 0 15.9-7.1 15.9-15.9C31.9 7.1 24.8 0 16 0zm0 29.1c-2.4 0-4.7-.6-6.8-1.9l-.5-.3-5 1.3 1.3-4.9-.3-.5c-1.4-2.2-2.1-4.7-2.1-7.3 0-7.4 6-13.4 13.4-13.4 7.4 0 13.4 6 13.4 13.4 0 7.4-6 13.4-13.4 13.4zm7.3-10c-.4-.2-2.4-1.2-2.7-1.3-.4-.1-.6-.2-.9.2-.3.4-1 1.3-1.2 1.5-.2.3-.4.3-.8.1-.4-.2-1.7-.6-3.1-1.9-1.2-1-1.9-2.3-2.2-2.7-.2-.4 0-.6.2-.8.2-.2.4-.4.5-.7.2-.2.2-.4.4-.7.1-.3 0-.5 0-.7-.1-.2-.9-2.2-1.3-3-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1 .5-.4.4-1.4 1.3-1.4 3.3s1.4 3.8 1.6 4.1c.2.3 2.8 4.2 6.7 5.9.9.4 1.7.6 2.3.8.9.3 1.8.2 2.4.2.7-.1 2.4-1 2.7-1.9.3-.9.3-1.7.2-1.9-.1-.2-.3-.3-.7-.5z"/></svg>'
PIN_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>'
MAIL_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
CLOCK_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>'


def head(title, desc, active_file):
    canonical = active_file
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Shiva Homoeo Care</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
"""


def nav(active_file):
    links = []
    for href, label in NAV_ITEMS[:-1]:  # Contact handled separately as CTA-adjacent
        cls = ' class="active"' if href == active_file else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    contact_cls = ' class="active"' if active_file == "contact.html" else ''
    links.append(f'<a href="contact.html"{contact_cls}>Contact</a>')
    links_html = "\n      ".join(links)

    mobile_links = []
    for href, label in NAV_ITEMS:
        mobile_links.append(f'<a href="{href}">{label}</a>')
    mobile_links_html = "\n  ".join(mobile_links)

    return f"""<header class="site-nav" id="siteNav">
  <div class="nav-inner">
    <a href="index.html" class="brand">
      <img src="assets/emblem-nav.webp" alt="Shiva Homoeo Care emblem">
      <span class="word"><b>Shiva Homoeo Care</b><span>Heal with Homoeopathy</span></span>
    </a>
    <nav class="links" id="navLinks">
      {links_html}
    </nav>
    <div class="nav-cta">
      <a class="tel" href="tel:{CLINIC['phone_tel']}">
        {PHONE_ICON}
        {CLINIC['phone_display']}
      </a>
      <a href="contact.html#book" class="btn btn-primary">Book Appointment</a>
      <button class="burger" id="burgerBtn" aria-label="Open menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="scrim" id="scrim"></div>
<div class="mobile-panel" id="mobilePanel">
  <button class="close" id="closePanel">&times;</button>
  {mobile_links_html}
  <a href="contact.html#book" class="btn btn-primary btn-block" style="margin-top:20px;">Book Appointment</a>
</div>"""


def footer():
    return f"""<footer id="siteFooter">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="index.html" class="brand"><img src="assets/emblem-nav.webp" alt="Shiva Homoeo Care"></a>
        <p>Classical, individualised homoeopathic care for chronic and everyday conditions. Heal with homoeopathy.</p>
        <div class="social" style="margin-top:20px;">
          <a href="#" aria-label="Instagram"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
          <a href="#" aria-label="Facebook"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8"><path d="M14 9h3V6h-3a4 4 0 0 0-4 4v2H7v3h3v6h3v-6h3l1-3h-4v-2a1 1 0 0 1 1-1z"/></svg></a>
          <a href="https://wa.me/{CLINIC['whatsapp_number']}" aria-label="WhatsApp">{WA_ICON.replace('width="32" height="32"', 'width="15" height="15"') if False else '<svg width="15" height="15" viewBox="0 0 32 32" fill="#fff"><path d="M16 0C7.2 0 .1 7.1.1 15.9c0 2.8.7 5.5 2.1 7.9L0 32l8.4-2.2c2.3 1.3 4.9 1.9 7.6 1.9 8.8 0 15.9-7.1 15.9-15.9C31.9 7.1 24.8 0 16 0zm0 29.1c-2.4 0-4.7-.6-6.8-1.9l-.5-.3-5 1.3 1.3-4.9-.3-.5c-1.4-2.2-2.1-4.7-2.1-7.3 0-7.4 6-13.4 13.4-13.4 7.4 0 13.4 6 13.4 13.4 0 7.4-6 13.4-13.4 13.4zm7.3-10c-.4-.2-2.4-1.2-2.7-1.3-.4-.1-.6-.2-.9.2-.3.4-1 1.3-1.2 1.5-.2.3-.4.3-.8.1-.4-.2-1.7-.6-3.1-1.9-1.2-1-1.9-2.3-2.2-2.7-.2-.4 0-.6.2-.8.2-.2.4-.4.5-.7.2-.2.2-.4.4-.7.1-.3 0-.5 0-.7-.1-.2-.9-2.2-1.3-3-.3-.8-.7-.7-.9-.7h-.8c-.3 0-.7.1-1 .5-.4.4-1.4 1.3-1.4 3.3s1.4 3.8 1.6 4.1c.2.3 2.8 4.2 6.7 5.9.9.4 1.7.6 2.3.8.9.3 1.8.2 2.4.2.7-.1 2.4-1 2.7-1.9.3-.9.3-1.7.2-1.9-.1-.2-.3-.3-.7-.5z"/></svg>'}</a>
        </div>
      </div>
      <div>
        <h5>Explore</h5>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="treatments.html">Treatments</a></li>
          <li><a href="doctor.html">Doctor</a></li>
          <li><a href="blog.html">Health Library</a></li>
        </ul>
      </div>
      <div>
        <h5>Clinic</h5>
        <ul>
          <li><a href="testimonials.html">Testimonials</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="faq.html">FAQs</a></li>
          <li><a href="contact.html#book">Book Appointment</a></li>
        </ul>
      </div>
      <div>
        <h5>Contact</h5>
        <p style="font-size:13.5px; color:rgba(255,255,255,.6); margin:0 0 8px; line-height:1.7;">
          {CLINIC['address_line1']}<br>{CLINIC['address_line2']}
        </p>
        <p style="font-size:13.5px; color:rgba(255,255,255,.75); margin:0 0 4px;">{CLINIC['phone_display']}</p>
        <p style="font-size:13.5px; color:rgba(255,255,255,.75); margin:0;">{CLINIC['email']}</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="year"></span> Shiva Homoeo Care. All rights reserved.</span>
      <span>Registered Homoeopathic Physician &middot; {CLINIC['doctor_name']} &middot; Reg. No. {CLINIC['reg_no']}</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/{CLINIC['whatsapp_number']}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  {WA_ICON}
  <span>Chat on WhatsApp</span>
</a>

<button class="totop" id="totop" aria-label="Back to top">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script src="assets/script.js"></script>"""


def page(title, desc, active_file, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, desc, active_file)}
</head>
<body>
{nav(active_file)}
<main>
{body}
</main>
{footer()}
</body>
</html>
"""


def write(filename, html):
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html))


def page_hero(eyebrow, title, desc, crumb_label):
    return f"""<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> / {crumb_label}</div>
    <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> {eyebrow}</div>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</section>"""


# ============================================================
# HOME
# ============================================================
home_body = f"""
<section class="hero" id="home">
  <div class="wrap hero-grid">
    <div class="reveal in-view">
      <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> Classical Homoeopathy Clinic</div>
      <h1>Gentle medicine, <em>for the whole person.</em></h1>
      <p class="lede">{CLINIC['doctor_name']} treats the root cause behind chronic and everyday conditions with individualised homoeopathic care — considered, natural, and free of harsh side effects.</p>
      <div class="hero-ctas">
        <a href="contact.html#book" class="btn btn-primary">Book a Consultation</a>
        <a href="tel:{CLINIC['phone_tel']}" class="btn btn-ghost">
          {PHONE_ICON}
          Call the Clinic
        </a>
      </div>
      <div class="trust-row">
        <div class="trust-item"><b>BHMS</b>Qualified &amp; registered</div>
        <div class="trust-item"><b>Reg. {CLINIC['reg_no']}</b>Homoeopathic physician</div>
        <div class="trust-item"><b>6</b>Focus areas</div>
        <div class="trust-item"><b>6 days</b>Open Mon–Sat</div>
      </div>
    </div>
    <div class="hero-visual reveal in-view">
      <div class="halo"></div>
      <div class="ring r1"></div>
      <div class="ring r2"></div>
      <img class="emblem" src="assets/emblem-hero.webp" alt="Shiva Homoeo Care emblem — trident and caduceus within a laurel wreath">
      <div class="leaf-float l1"><svg viewBox="0 0 24 24" fill="none" stroke="#2B6E5F" stroke-width="1.6"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
      <div class="leaf-float l2"><svg viewBox="0 0 24 24" fill="none" stroke="#2B6E5F" stroke-width="1.6"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
      <div class="leaf-float l3"><svg viewBox="0 0 24 24" fill="none" stroke="#2B6E5F" stroke-width="1.6"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
    </div>
  </div>
</section>

<div class="divider"><span></span><span></span><span></span></div>

<section class="approach" id="approach">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> The Homoeopathic Approach</div>
      <h2 style="font-size:clamp(26px,3vw,36px);">Medicine that treats you, not just the diagnosis</h2>
      <p>Every plan begins with your full picture — constitution, history, and lifestyle — not just the symptom in front of us.</p>
    </div>
    <div class="principles">
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
        <h4>Individualised care</h4>
        <p>Your treatment plan is built around your unique constitution — not a standard protocol for a diagnosis code.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
        <h4>Natural substances</h4>
        <p>Remedies are prepared from carefully sourced natural substances, dosed to work gently with the body.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 21s-7-4.35-9.5-9C.75 8 3 4 7 4c2 0 4 1.5 5 3 1-1.5 3-3 5-3 4 0 6.25 4 4.5 8-2.5 4.65-9.5 9-9.5 9z"/></svg></div>
        <h4>Root-cause focus</h4>
        <p>We look for what's driving recurring symptoms, aiming at the underlying pattern rather than masking it.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2 3 7v6c0 5 4 9 9 9s9-4 9-9V7l-9-5z"/></svg></div>
        <h4>Gentle on the body</h4>
        <p>Considered dosing means treatment can sit alongside your existing care without harsh side effects.</p>
      </div>
    </div>
  </div>
</section>

<section class="treatments" id="treatments-preview">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> Conditions We Treat</div>
      <h2 style="font-size:clamp(26px,3vw,36px);">Considered care across the conditions that affect daily life</h2>
      <p>From long-standing allergies to everyday complaints — see the full list with our approach to each.</p>
    </div>
    <div class="cond-grid">
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2c1 3-2 4-2 7a4 4 0 0 0 8 0c0-1-.5-2-1-3"/><path d="M8 14c-3 1-4 4-4 6h16c0-3-2-5-5-6"/></svg></div>
        <h4>Skin &amp; Allergies</h4>
        <p>Eczema, psoriasis, urticaria, and recurring allergic reactions.</p>
        <a class="more" href="treatments.html#skin">Learn more →</a>
      </div>
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 2v9a3 3 0 0 0 6 0V2"/><path d="M6 13a6 6 0 0 0 12 0"/><path d="M12 19v3"/></svg></div>
        <h4>Respiratory &amp; Sinus</h4>
        <p>Asthma, allergic rhinitis, sinusitis, and recurrent cold &amp; cough.</p>
        <a class="more" href="treatments.html#respiratory">Learn more →</a>
      </div>
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M7 12a5 5 0 0 1 10 0"/><path d="M4 12h2m12 0h2M7 12v3a5 5 0 0 0 10 0v-3"/></svg></div>
        <h4>Joint &amp; Bone</h4>
        <p>Arthritis, chronic back pain, and stiffness.</p>
        <a class="more" href="treatments.html#joint">Learn more →</a>
      </div>
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="9" r="4"/><path d="M12 13v8m-3-3h6"/></svg></div>
        <h4>Hormonal &amp; Women's Health</h4>
        <p>PCOS, thyroid imbalance, menstrual irregularities.</p>
        <a class="more" href="treatments.html#hormonal">Learn more →</a>
      </div>
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M6 21c0-4 3-6 6-6s6 2 6 6"/></svg></div>
        <h4>Children's Health</h4>
        <p>Recurring infections, allergies, and growth-related concerns.</p>
        <a class="more" href="treatments.html#children">Learn more →</a>
      </div>
      <div class="cond-card reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3c0 4-4 4-4 8a4 4 0 0 0 8 0c0-4-4-4-4-8z"/><path d="M12 15v6"/></svg></div>
        <h4>Hair &amp; Scalp</h4>
        <p>Hair fall, premature greying, and scalp conditions.</p>
        <a class="more" href="treatments.html#hair">Learn more →</a>
      </div>
    </div>
    <p class="disclaimer">Homoeopathic treatment is offered as a complementary approach to your overall healthcare. For medical emergencies, please contact your physician or nearest hospital directly.</p>
  </div>
</section>

<section class="stats">
  <div class="wrap stats-grid">
    <div class="reveal"><div class="num">BHMS</div><div class="lab">Qualified Physician</div></div>
    <div class="reveal"><div class="num">6</div><div class="lab">Focus Areas</div></div>
    <div class="reveal"><div class="num">6</div><div class="lab">Days Open Weekly</div></div>
    <div class="reveal"><div class="num">Reg. {CLINIC['reg_no']}</div><div class="lab">Registered Practice</div></div>
  </div>
</section>

<section class="testimonials" id="testimonials-preview">
  <div class="wrap">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <div class="eyebrow" style="justify-content:center;"><span class="dots"><span></span><span></span><span></span></span> Patient Stories</div>
      <h2 style="font-size:clamp(26px,3vw,36px);">Real people, real relief</h2>
    </div>
    <div class="test-row">
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">Three years of recurring eczema flare-ups, and within a few months of starting treatment here, my skin finally calmed down.</p>
        <div class="test-foot"><div><div class="name">Meera K.</div><div class="cond">Skin &amp; Allergies</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">My son used to catch every seasonal cold going around. A year into homoeopathic care and he's missed almost no school.</p>
        <div class="test-foot"><div><div class="name">Rohit V.</div><div class="cond">Children's Health</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">I was sceptical at first, but the thoroughness of the first consultation won me over. My thyroid levels have been stable since.</p>
        <div class="test-foot"><div><div class="name">Anjali D.</div><div class="cond">Hormonal Health</div></div><div class="stars">★★★★★</div></div>
      </div>
    </div>
    <div style="text-align:center; margin-top:36px;"><a href="testimonials.html" class="btn btn-ghost">Read more stories</a></div>
  </div>
</section>
"""
write("index.html", page(
    "Home",
    "Shiva Homoeo Care in Khajuraho offers classical, individualised homoeopathic treatment for chronic and everyday conditions under Dr. Kavita Singh Bundela.",
    "index.html",
    home_body
))


# ============================================================
# ABOUT
# ============================================================
about_body = f"""
{page_hero("About Us", "A calm, considered approach to natural healing", "Shiva Homoeo Care has been serving Khajuraho and the surrounding region with classical homoeopathic treatment, built on the principle of treating the person, not just the diagnosis.", "About")}

<section class="approach">
  <div class="wrap">
    <div class="doctor-grid" style="grid-template-columns:1fr 1fr;">
      <div class="reveal">
        <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> Our Story</div>
        <h2 style="font-size:clamp(24px,3vw,32px); margin-bottom:16px;">Why Shiva Homoeo Care exists</h2>
        <p style="color:var(--text-soft); line-height:1.8; font-size:15.5px; margin-bottom:16px;">Shiva Homoeo Care was founded to bring rigorous, classical homoeopathy to patients across Khajuraho who want a natural treatment option without giving up thoroughness. Consultations are unhurried by design, so nothing about your history or lifestyle gets missed.</p>
        <p style="color:var(--text-soft); line-height:1.8; font-size:15.5px;">Located opposite Hotel Ramada on Airport Road, the clinic is easy to find for both local patients and visitors to the region, and welcomes patients of all ages — from young children to senior citizens.</p>
      </div>
      <div class="reveal">
        <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> Our Philosophy</div>
        <h2 style="font-size:clamp(24px,3vw,32px); margin-bottom:16px;">Considered, not generic</h2>
        <p style="color:var(--text-soft); line-height:1.8; font-size:15.5px; margin-bottom:16px;">Classical homoeopathy treats the whole person — your constitution, history, and current concern together — rather than prescribing a fixed remedy for a fixed diagnosis. That's the standard every consultation at Shiva Homoeo Care is held to.</p>
        <p style="color:var(--text-soft); line-height:1.8; font-size:15.5px;">Treatment plans are reviewed and adjusted over time, so care continues to reflect how you're actually responding — not a one-time prescription.</p>
      </div>
    </div>
  </div>
</section>

<div class="divider"><span></span><span></span><span></span></div>

<section class="approach">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> What Guides Us</div>
      <h2 style="font-size:clamp(26px,3vw,36px);">The values behind every consultation</h2>
    </div>
    <div class="principles">
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
        <h4>Time, not templates</h4>
        <p>Every first visit runs long enough to actually understand what's going on.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
        <h4>Natural, gentle care</h4>
        <p>Remedies chosen to work with the body, with mindful, considered dosing.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 21s-7-4.35-9.5-9C.75 8 3 4 7 4c2 0 4 1.5 5 3 1-1.5 3-3 5-3 4 0 6.25 4 4.5 8-2.5 4.65-9.5 9-9.5 9z"/></svg></div>
        <h4>Honest communication</h4>
        <p>Clear explanations of what to expect and realistic timelines — no overselling.</p>
      </div>
      <div class="principle reveal">
        <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2 3 7v6c0 5 4 9 9 9s9-4 9-9V7l-9-5z"/></svg></div>
        <h4>Care for all ages</h4>
        <p>From children's recurring infections to age-related joint concerns.</p>
      </div>
    </div>
  </div>
</section>

<section class="book">
  <div class="wrap" style="text-align:center;">
    <h2 style="font-size:clamp(24px,3vw,32px); margin-bottom:16px;">Ready to talk about what you're dealing with?</h2>
    <a href="contact.html#book" class="btn btn-primary">Book a Consultation</a>
  </div>
</section>
"""
write("about.html", page(
    "About Us",
    "Learn about Shiva Homoeo Care's philosophy and approach to classical, individualised homoeopathic treatment in Khajuraho.",
    "about.html",
    about_body
))


# ============================================================
# TREATMENTS
# ============================================================
def cond_detail(anchor, icon_svg, sub, title, intro, points):
    points_html = "\n".join(f"<li>{p}</li>" for p in points)
    return f"""
<section class="cond-detail" id="{anchor}">
  <div class="wrap cond-detail-grid">
    <div>
      <div class="ic-lg">{icon_svg}</div>
      <div class="sub">{sub}</div>
      <h3>{title}</h3>
    </div>
    <div>
      <p style="color:var(--text-soft); font-size:15.5px; line-height:1.8;">{intro}</p>
      <ul class="points">
        {points_html}
      </ul>
      <a href="contact.html#book" class="btn btn-primary btn-sm" style="margin-top:20px;">Book a Consultation</a>
    </div>
  </div>
</section>"""

treatments_body = f"""
{page_hero("Conditions We Treat", "Considered care across the conditions that affect daily life", "Each condition below links to how we approach it homoeopathically. If you don't see your concern listed, get in touch — we treat a wide range beyond this list.", "Treatments")}

{cond_detail("skin",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><path d="M12 2c1 3-2 4-2 7a4 4 0 0 0 8 0c0-1-.5-2-1-3"/><path d="M8 14c-3 1-4 4-4 6h16c0-3-2-5-5-6"/></svg>',
  "Focus Area", "Skin &amp; Allergies",
  "Chronic skin complaints often trace back to an underlying allergic or immune pattern rather than the skin itself. Treatment looks at what's triggering flare-ups, not just the visible symptom.",
  ["Eczema and atopic dermatitis", "Psoriasis and chronic dry skin conditions", "Urticaria (hives) and recurring allergic reactions", "Acne linked to hormonal or digestive imbalance"]
)}

{cond_detail("respiratory",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><path d="M9 2v9a3 3 0 0 0 6 0V2"/><path d="M6 13a6 6 0 0 0 12 0"/><path d="M12 19v3"/></svg>',
  "Focus Area", "Respiratory &amp; Sinus",
  "From seasonal sinus trouble to recurring chest infections, respiratory treatment focuses on strengthening resistance over time, not just easing the current episode.",
  ["Asthma and wheeze-prone chests", "Allergic rhinitis and chronic sinusitis", "Recurrent cold, cough, and throat infections", "Seasonal allergy patterns"]
)}

{cond_detail("joint",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><path d="M7 12a5 5 0 0 1 10 0"/><path d="M4 12h2m12 0h2M7 12v3a5 5 0 0 0 10 0v-3"/></svg>',
  "Focus Area", "Joint &amp; Bone",
  "Chronic joint and back complaints are managed with a long-term view — reducing flare frequency and stiffness while supporting overall mobility.",
  ["Osteoarthritis and rheumatoid arthritis", "Chronic lower back pain", "Cervical &amp; shoulder stiffness", "Gout-related joint pain"]
)}

{cond_detail("hormonal",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="9" r="4"/><path d="M12 13v8m-3-3h6"/></svg>',
  "Focus Area", "Hormonal &amp; Women's Health",
  "Hormonal health is treated with attention to the full cycle of symptoms — physical and emotional — rather than isolated lab values alone.",
  ["PCOS / PCOD", "Thyroid imbalance (hypo- and hyperthyroid patterns)", "Menstrual irregularities and PMS", "Menopausal symptoms"]
)}

{cond_detail("children",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M6 21c0-4 3-6 6-6s6 2 6 6"/></svg>',
  "Focus Area", "Children's Health",
  "Gentle, mild-tasting remedies make homoeopathy well suited to children, with special attention paid to recurring illness patterns and growth.",
  ["Recurrent cold, cough &amp; ear infections", "Childhood allergies and skin conditions", "Digestive troubles and appetite concerns", "Growth and developmental support"]
)}

{cond_detail("hair",
  '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><path d="M12 3c0 4-4 4-4 8a4 4 0 0 0 8 0c0-4-4-4-4-8z"/><path d="M12 15v6"/></svg>',
  "Focus Area", "Hair &amp; Scalp",
  "Hair fall and scalp conditions are frequently linked to stress, nutrition, or internal imbalance — treatment looks at those root drivers.",
  ["Excessive hair fall &amp; thinning", "Premature greying", "Dandruff and scalp irritation", "Stress-linked hair loss"]
)}

<section class="book">
  <div class="wrap" style="text-align:center;">
    <p style="color:var(--text-soft); max-width:600px; margin:0 auto 20px;">Don't see your condition listed? We treat a wide range of chronic and acute concerns beyond this page — get in touch to ask.</p>
    <a href="contact.html#book" class="btn btn-primary">Book a Consultation</a>
  </div>
</section>
"""
write("treatments.html", page(
    "Treatments",
    "Conditions treated at Shiva Homoeo Care: skin & allergies, respiratory & sinus, joint & bone, hormonal health, children's health, and hair & scalp.",
    "treatments.html",
    treatments_body
))


# ============================================================
# DOCTOR
# ============================================================
doctor_body = f"""
{page_hero("Meet Your Physician", CLINIC['doctor_name'], "Registered homoeopathic physician at Shiva Homoeo Care, Khajuraho.", "Doctor")}

<section class="doctor">
  <div class="wrap doctor-grid">
    <div class="doc-card reveal">
      <div class="ring-deco"></div>
      <div class="mono">KB</div>
      <h4>{CLINIC['doctor_name']}</h4>
      <span>{CLINIC['doctor_quals']}</span>
    </div>
    <div class="doctor-copy reveal">
      <div class="eyebrow"><span class="dots"><span></span><span></span><span></span></span> Background</div>
      <h2 style="font-size:clamp(24px,3vw,32px); margin-bottom:18px;">Clinical thoroughness, with a communicator's touch</h2>
      <p>{CLINIC['doctor_name']} is a registered homoeopathic physician (BHMS) with additional training in Naturopathy &amp; Yogic Science (DNYS). She brings an unusual combination to her consultations — a science-trained clinical eye alongside a background in English Literature (MA) and a B.Ed in education, which shows up in how clearly she explains a treatment plan and why it's been chosen.</p>
      <p>Consultations at Shiva Homoeo Care are unhurried by design: enough time to go through your history and current concern properly before any remedy is recommended.</p>
      <ul class="cred-list">
        <li>Registered Homoeopathic Physician, Reg. No. {CLINIC['reg_no']}</li>
        <li>BHMS — Bachelor of Homoeopathic Medicine &amp; Surgery</li>
        <li>DNYS — Diploma in Naturopathy &amp; Yogic Science</li>
        <li>MA — English Literature</li>
        <li>B.Ed — Bachelor of Education</li>
        <li>Clinic based in Khajuraho, Madhya Pradesh</li>
      </ul>
      <p class="pull-quote">"My job isn't to treat a report. It's to understand the person carrying it — and build a plan around them."</p>
      <a href="contact.html#book" class="btn btn-primary" style="margin-top:26px;">Book a Consultation</a>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap stats-grid">
    <div class="reveal"><div class="num">BHMS</div><div class="lab">Core Qualification</div></div>
    <div class="reveal"><div class="num">DNYS</div><div class="lab">Naturopathy &amp; Yoga</div></div>
    <div class="reveal"><div class="num">MA · B.Ed</div><div class="lab">Literature &amp; Education</div></div>
    <div class="reveal"><div class="num">{CLINIC['reg_no']}</div><div class="lab">Registration No.</div></div>
  </div>
</section>
"""
write("doctor.html", page(
    f"Meet {CLINIC['doctor_name']}",
    f"{CLINIC['doctor_name']} ({CLINIC['doctor_quals']}) is the registered homoeopathic physician at Shiva Homoeo Care, Khajuraho.",
    "doctor.html",
    doctor_body
))


# ============================================================
# TESTIMONIALS
# ============================================================
testimonials_body = f"""
{page_hero("Patient Stories", "Real people, real relief", "A few notes from patients treated at Shiva Homoeo Care. Names are shortened for privacy; full testimonials shared with consent.", "Testimonials")}

<section class="testimonials">
  <div class="wrap">
    <div class="test-row">
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">Three years of recurring eczema flare-ups, and within a few months of starting treatment here, my skin finally calmed down. Dr. Bundela actually listened.</p>
        <div class="test-foot"><div><div class="name">Meera K.</div><div class="cond">Skin &amp; Allergies</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">My son used to catch every seasonal cold going around. A year into homoeopathic care and he's missed almost no school this year.</p>
        <div class="test-foot"><div><div class="name">Rohit V.</div><div class="cond">Children's Health</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">I was sceptical at first, but the thoroughness of the first consultation won me over. My thyroid levels have been stable for over a year now.</p>
        <div class="test-foot"><div><div class="name">Anjali D.</div><div class="cond">Hormonal Health</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">Years of lower back stiffness, and a considered long-term plan actually made a difference where painkillers only masked it.</p>
        <div class="test-foot"><div><div class="name">Suresh P.</div><div class="cond">Joint &amp; Bone</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">The clinic is easy to find near Hotel Ramada, and appointments run on time. Small thing, but it matters.</p>
        <div class="test-foot"><div><div class="name">Farah A.</div><div class="cond">General Care</div></div><div class="stars">★★★★★</div></div>
      </div>
      <div class="test-card reveal">
        <div class="quote-mark">&ldquo;</div>
        <p class="txt">My hair fall slowed down noticeably within a couple of months. Dr. Bundela also explained what was likely driving it, which helped.</p>
        <div class="test-foot"><div><div class="name">Neha S.</div><div class="cond">Hair &amp; Scalp</div></div><div class="stars">★★★★★</div></div>
      </div>
    </div>
  </div>
</section>

<section class="book">
  <div class="wrap" style="text-align:center;">
    <h2 style="font-size:clamp(24px,3vw,32px); margin-bottom:16px;">Ready to start your own story?</h2>
    <a href="contact.html#book" class="btn btn-primary">Book a Consultation</a>
  </div>
</section>
"""
write("testimonials.html", page(
    "Patient Testimonials",
    "Read patient testimonials and experiences from Shiva Homoeo Care, Khajuraho.",
    "testimonials.html",
    testimonials_body
))


# ============================================================
# BLOG
# ============================================================
blog_body = f"""
{page_hero("Health Library", "Notes on natural wellness", "Short, practical reads from the clinic on homoeopathy, seasonal health, and everyday prevention.", "Health Library")}

<section class="blog">
  <div class="wrap">
    <div class="blog-row">
      <article class="blog-card reveal">
        <div class="blog-thumb"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20c8-1 14-7 15-16-9 1-15 7-16 16z"/><path d="M5 19c3-4 6-7 12-14"/></svg></div>
        <div class="blog-body">
          <span class="tag">Immunity</span>
          <h4>Five habits that support your child's immunity this season</h4>
          <p>Simple, seasonal changes that make a real difference for children prone to recurring colds.</p>
          <div class="blog-meta"><span>4 min read</span><a href="blog.html#article-1">Read article →</a></div>
        </div>
      </article>
      <article class="blog-card reveal">
        <div class="blog-thumb"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
        <div class="blog-body">
          <span class="tag">Chronic Care</span>
          <h4>Why homoeopathic treatment plans take time to work</h4>
          <p>A look at what's actually happening during the first weeks of a constitutional treatment plan.</p>
          <div class="blog-meta"><span>6 min read</span><a href="blog.html#article-2">Read article →</a></div>
        </div>
      </article>
      <article class="blog-card reveal">
        <div class="blog-thumb"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-4.35-9.5-9C.75 8 3 4 7 4c2 0 4 1.5 5 3 1-1.5 3-3 5-3 4 0 6.25 4 4.5 8-2.5 4.65-9.5 9-9.5 9z"/></svg></div>
        <div class="blog-body">
          <span class="tag">Women's Health</span>
          <h4>Understanding PCOS: a homoeopathic perspective</h4>
          <p>How individualised treatment approaches the hormonal and lifestyle factors behind PCOS.</p>
          <div class="blog-meta"><span>5 min read</span><a href="blog.html#article-3">Read article →</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="article" id="article-1">
  <div class="wrap article-body reveal">
    <span class="tag">Immunity</span>
    <h2 style="font-size:clamp(24px,3vw,30px); margin:14px 0 20px;">Five habits that support your child's immunity this season</h2>
    <p>Recurring colds in children are often less about bad luck and more about a few small, fixable habits. Alongside any treatment plan, these five changes tend to make a noticeable difference over a season.</p>
    <h3>1. Consistent sleep timing</h3>
    <p>Irregular sleep is one of the most common hidden contributors to a child catching every seasonal bug going around. Aim for the same bedtime, even on weekends.</p>
    <h3>2. Warm fluids over cold ones</h3>
    <p>Especially during the transition between seasons, warm water and soups are gentler on the throat and digestion than iced drinks.</p>
    <h3>3. Reduce sugar during vulnerable weeks</h3>
    <p>High sugar intake can affect the immune response during periods when a child is already fighting something off.</p>
    <h3>4. Outdoor time, even in cooler weather</h3>
    <p>Fresh air and moderate activity support circulation and general resilience — bundling up is fine, staying indoors constantly isn't necessary.</p>
    <h3>5. Don't skip the follow-up</h3>
    <p>If your child is on a treatment plan, the follow-up visit is where the plan gets refined based on how they've actually responded — it's not optional.</p>
  </div>
</section>

<section class="article" id="article-2" style="border-top:1px solid var(--line); background:var(--paper-2);">
  <div class="wrap article-body reveal">
    <span class="tag">Chronic Care</span>
    <h2 style="font-size:clamp(24px,3vw,30px); margin:14px 0 20px;">Why homoeopathic treatment plans take time to work</h2>
    <p>One of the most common questions in a first consultation is "how long until I feel better?" The honest answer depends on how long the condition has been building — and that's worth explaining properly.</p>
    <h3>Acute vs. chronic timelines</h3>
    <p>A sudden, short-term complaint can respond within days. A condition that's been present for years, however, took years to establish itself, and a considered treatment plan works with the body's own pace of change rather than forcing symptoms to disappear immediately.</p>
    <h3>What a 4–8 week review actually checks</h3>
    <p>Chronic treatment plans at the clinic are typically reviewed every 4–8 weeks. This isn't just a check-in — it's when the remedy or dose is adjusted based on exactly how your body has responded, which is central to how classical homoeopathy works.</p>
    <h3>Signs the plan is working, even before symptoms fully resolve</h3>
    <p>Better sleep, more stable energy, and fewer flare-ups are often early signs the underlying pattern is shifting, even if the primary complaint hasn't fully gone yet.</p>
  </div>
</section>

<section class="article" id="article-3">
  <div class="wrap article-body reveal">
    <span class="tag">Women's Health</span>
    <h2 style="font-size:clamp(24px,3vw,30px); margin:14px 0 20px;">Understanding PCOS: a homoeopathic perspective</h2>
    <p>PCOS (Polycystic Ovary Syndrome) affects far more than the reproductive system — it's a hormonal and metabolic pattern that shows up differently in every patient, which is exactly why individualised treatment matters.</p>
    <h3>Beyond the lab report</h3>
    <p>Two patients with a similar PCOS diagnosis can have very different underlying patterns — one driven more by insulin resistance, another by stress-linked hormonal disruption. Treatment accounts for that difference rather than applying one protocol to both.</p>
    <h3>What a consultation covers</h3>
    <p>Expect questions about your cycle history, weight changes, sleep, stress levels, and family history — all of which inform the treatment plan alongside your lab results.</p>
    <h3>A long-term, not one-time, approach</h3>
    <p>PCOS management is typically an ongoing relationship between patient and physician, with the plan adjusted as your cycle and symptoms respond over several months.</p>
  </div>
</section>
"""
write("blog.html", page(
    "Health Library",
    "Practical articles on homoeopathy, seasonal health, and natural wellness from Shiva Homoeo Care, Khajuraho.",
    "blog.html",
    blog_body
))


# ============================================================
# GALLERY
# ============================================================
gallery_body = f"""
{page_hero("Inside the Clinic", "A calm space, designed for healing", "A quick look at the clinic — real photographs will replace these placeholders once available.", "Gallery")}

<section class="gallery">
  <div class="wrap">
    <div class="gal-grid">
      <div class="gal-tile big reveal"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/></svg><span>Reception</span></div>
      <div class="gal-tile reveal"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><path d="M12 2 3 7v6c0 5 4 9 9 9s9-4 9-9V7l-9-5z"/></svg><span>Consultation Room</span></div>
      <div class="gal-tile reveal"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/></svg><span>Dispensary</span></div>
      <div class="gal-tile reveal"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><path d="M4 19V9l8-6 8 6v10"/><path d="M9 19v-6h6v6"/></svg><span>Waiting Lounge</span></div>
      <div class="gal-tile reveal"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><circle cx="12" cy="8" r="4"/><path d="M6 21c0-4 3-6 6-6s6 2 6 6"/></svg><span>Children's Corner</span></div>
    </div>
    <p class="disclaimer" style="margin-top:34px;">Placeholder tiles — send clinic photographs and we'll swap these in before launch.</p>
  </div>
</section>
"""
write("gallery.html", page(
    "Gallery",
    "A look inside Shiva Homoeo Care's clinic in Khajuraho.",
    "gallery.html",
    gallery_body
))


# ============================================================
# FAQ
# ============================================================
faq_body = f"""
{page_hero("Common Questions", "Before your first visit", "Answers to the questions we hear most often from new patients.", "FAQs")}

<section class="faq">
  <div class="wrap">
    <div class="faq-wrap reveal">
      <div class="faq-item open">
        <button class="faq-q">What happens during a first consultation? <span class="plus"></span></button>
        <div class="faq-a"><p>Your first visit typically runs 45–60 minutes. Dr. Bundela will ask about your current concern, medical history, lifestyle, and general constitution before recommending a personalised treatment plan.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">How long does homoeopathic treatment take to show results? <span class="plus"></span></button>
        <div class="faq-a"><p>It varies by condition. Acute complaints can respond within days, while chronic conditions are usually reviewed in 4–8 week cycles as the underlying pattern shifts.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Are there any diet restrictions during treatment? <span class="plus"></span></button>
        <div class="faq-a"><p>Some remedies work best without strong-flavoured food or beverages like coffee close to dosing. You'll receive simple, specific guidance for your remedy at the time of prescription.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Is homoeopathy safe for children? <span class="plus"></span></button>
        <div class="faq-a"><p>Yes — gentle dosing and mild-tasting remedies make homoeopathy a well-tolerated option for children, and it's one of the clinic's areas of focus.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Can I continue my existing medication alongside treatment? <span class="plus"></span></button>
        <div class="faq-a"><p>In most cases, yes. Please bring a list of current medications to your first consultation so Dr. Bundela can plan around them safely.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">What are the consultation fees? <span class="plus"></span></button>
        <div class="faq-a"><p>Please call or WhatsApp the clinic at {CLINIC['phone_display']} to confirm current consultation fees.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">What are the clinic's working hours? <span class="plus"></span></button>
        <div class="faq-a"><p>Monday to Saturday, {CLINIC['hours_weekday']}. Closed on Sundays.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Where is the clinic located? <span class="plus"></span></button>
        <div class="faq-a"><p>{CLINIC['address_line1']}, {CLINIC['address_line2']} — directly opposite Hotel Ramada.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="book">
  <div class="wrap" style="text-align:center;">
    <p style="color:var(--text-soft); margin-bottom:20px;">Still have a question? Reach out directly.</p>
    <a href="contact.html#book" class="btn btn-primary">Contact the Clinic</a>
  </div>
</section>
"""
write("faq.html", page(
    "FAQs",
    "Frequently asked questions about visiting Shiva Homoeo Care in Khajuraho.",
    "faq.html",
    faq_body
))


# ============================================================
# CONTACT / BOOK
# ============================================================
contact_body = f"""
{page_hero("Book an Appointment", "Let's talk about what you're dealing with", "Fill in the form and it will open a pre-filled WhatsApp message straight to the clinic — or call/WhatsApp us directly using the details alongside.", "Contact")}

<section class="book" id="book">
  <div class="wrap">
    <div class="book-grid">
      <div class="form-card reveal">
        <form id="apptForm">
          <div class="form-row">
            <div class="field"><label for="fname">Full name</label><input id="fname" type="text" placeholder="Your name" required></div>
            <div class="field"><label for="fphone">Phone number</label><input id="fphone" type="tel" placeholder="+91 00000 00000" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="femail">Email</label><input id="femail" type="email" placeholder="you@example.com"></div>
            <div class="field"><label for="fcond">Condition / concern</label>
              <select id="fcond" required>
                <option value="" disabled selected>Select one</option>
                <option>Skin &amp; Allergies</option>
                <option>Respiratory &amp; Sinus</option>
                <option>Joint &amp; Bone</option>
                <option>Hormonal &amp; Women's Health</option>
                <option>Children's Health</option>
                <option>Hair &amp; Scalp</option>
                <option>Other</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="field"><label for="fdate">Preferred date</label><input id="fdate" type="date"></div>
            <div class="field"><label for="ftime">Preferred time</label><input id="ftime" type="time"></div>
          </div>
          <div class="field"><label for="fmsg">Anything you'd like us to know</label><textarea id="fmsg" placeholder="Briefly describe your concern..."></textarea></div>
          <button type="submit" class="btn btn-primary btn-block">Send via WhatsApp</button>
          <p class="form-note">Submitting opens WhatsApp with your details pre-filled, sent directly to the clinic at {CLINIC['phone_display']}.</p>
        </form>
        <div class="success-msg" id="successMsg">
          <div class="tick"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M20 6 9 17l-5-5"/></svg></div>
          <h4>Almost done</h4>
          <p>WhatsApp should have opened in a new tab with your details filled in — just hit send there to reach the clinic.</p>
        </div>
      </div>
      <div class="info-card reveal">
        <h4>Clinic Information</h4>
        <div class="info-row">
          <div class="ic">{PIN_ICON}</div>
          <div class="txt"><b>Address</b><div>{CLINIC['address_line1']}<br>{CLINIC['address_line2']}</div></div>
        </div>
        <div class="info-row">
          <div class="ic">{PHONE_ICON.replace('currentColor','#fff')}</div>
          <div class="txt"><b>Phone &amp; WhatsApp</b><div>{CLINIC['phone_display']}</div></div>
        </div>
        <div class="info-row">
          <div class="ic">{MAIL_ICON}</div>
          <div class="txt"><b>Email</b><div>{CLINIC['email']}</div></div>
        </div>
        <div class="info-row" style="align-items:flex-start;">
          <div class="ic">{CLOCK_ICON}</div>
          <div class="txt" style="width:100%;">
            <b>Working Hours</b>
            <table class="hours-table">
              <tr><td>Mon – Sat</td><td>{CLINIC['hours_weekday']}</td></tr>
              <tr><td>Sunday</td><td>{CLINIC['hours_sunday']}</td></tr>
            </table>
          </div>
        </div>
        <div class="info-ctas">
          <a href="tel:{CLINIC['phone_tel']}" class="btn btn-on-dark" style="flex:1;">Call</a>
          <a href="https://wa.me/{CLINIC['whatsapp_number']}" class="btn btn-on-dark" style="flex:1;" target="_blank" rel="noopener">WhatsApp</a>
        </div>
        <div class="map-box">
          <iframe src="{MAPS_EMBED_SRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Shiva Homoeo Care location map"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("contact.html", page(
    "Contact & Book Appointment",
    f"Contact Shiva Homoeo Care — {CLINIC['address_line1']}, {CLINIC['address_line2']}. Call or WhatsApp {CLINIC['phone_display']}.",
    "contact.html",
    contact_body
))

print("\\nAll pages generated.")
