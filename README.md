# Akhil Azad — Portfolio

A fast, dependency-free personal portfolio for a Software Developer / AI-ML Engineer.
Static HTML, CSS and vanilla JavaScript — no build step, QR- and deploy-friendly.

## Files
- `index.html` — page structure and content
- `styles.css` — refined dark theme (one restrained cool accent), full responsive design
- `script.js` — mobile menu, scroll reveals, active-section nav (progressive enhancement)
- `assets/akhil-profile.jpg` — profile photo
- `assets/favicon.svg` — monogram favicon
- `assets/Akhil-Azad-Resume.pdf` — downloadable one-page resume

## Design
- Fonts: Space Grotesk (display), Inter (body), JetBrains Mono (indices), loaded via Google Fonts with system fallbacks.
- Accent: a single cool periwinkle blue used only for signal (availability, focus, active nav, hero glow).
- Accessible: keyboard focus states, skip link, reduced-motion support, and full content visible even with JavaScript disabled.

## Run locally
Any static server works, e.g.:
```
python3 -m http.server 8000
```
Then open http://localhost:8000

## Deploy
Push this folder to GitHub and deploy with Vercel or GitHub Pages. Point the QR code at the
permanent domain, not a temporary preview URL.

## Updating the resume PDF
The PDF is generated from a small reportlab script. Re-run it after editing your details to
regenerate `assets/Akhil-Azad-Resume.pdf`.
