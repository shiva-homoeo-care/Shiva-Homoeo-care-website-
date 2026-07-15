# Shiva Homoeo Care — Website

Static multi-page website for Shiva Homoeo Care, Khajuraho. Ready to deploy on Vercel as-is — no build step required.

## Pages
- `index.html` — Home
- `about.html` — About Us
- `treatments.html` — Conditions treated (with individual condition sections)
- `doctor.html` — Meet Dr. Kavita Singh Bundela
- `testimonials.html` — Patient stories
- `blog.html` — Health Library (3 sample articles)
- `gallery.html` — Clinic gallery (placeholder tiles — swap for real photos)
- `faq.html` — Frequently asked questions
- `contact.html` — Contact details + appointment form (id="book")

## Assets
- `assets/styles.css` — all site styling
- `assets/script.js` — mobile menu, FAQ accordion, scroll reveal, and the appointment form logic
- `assets/emblem-nav.webp`, `assets/emblem-hero.webp` — logo emblem images

## Deploying to Vercel
1. Install the Vercel CLI if you don't have it: `npm i -g vercel`
2. From inside this folder, run: `vercel` (first time) or `vercel --prod` (production deploy)
3. Follow the prompts — no framework/build settings needed, this is a static site.

Or: drag-and-drop this whole folder into the Vercel dashboard ("Add New… → Project → deploy a folder").

## How the appointment form works right now
The form on `contact.html` does **not** send email or hit a server. On submit, it builds a pre-filled
WhatsApp message from the form fields and opens `https://wa.me/917999635415?text=...` in a new tab —
the patient then taps "send" in WhatsApp themselves. This requires no backend, no API costs, and works
immediately. The WhatsApp number is set once, in `assets/script.js` at the top (`CLINIC_WHATSAPP`).

**Limitation:** this only works if the visitor has WhatsApp installed (desktop or mobile) and manually
taps send — it is not a guaranteed delivery. If you want submissions to arrive automatically without
the patient needing to press send (e.g. via email or a database), that requires a small backend — a
Vercel Serverless Function is a natural fit since you're already on Vercel. Happy to build that next if wanted.

## Editing content
All page content is written directly in the HTML files — open any `.html` file in a text editor and
edit the text directly. If you'd rather regenerate pages from a single source (e.g. after changing
clinic details in one place), `build.py` (kept separately, not part of the deployed site) regenerates
every page from shared templates — useful if the address, phone, or doctor details ever change.

## Still using placeholders — replace before public launch
- Google Maps embed on `contact.html` uses a generic search query, not a verified pinned location —
  replace with the exact Google Maps embed link for the clinic.
- Gallery images are illustrated placeholders, not real clinic photos.
- Blog articles are original starter content — replace or expand as needed.
- Testimonials are sample text — replace with real, consented patient testimonials.
- No custom domain is connected yet — Vercel will assign a `*.vercel.app` URL until one is added.
