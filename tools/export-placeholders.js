// Writes a placeholder PNG for every tile/object path in data/art.js (run with the site served on :8765).
// Usage: (cd joetopia-web && python3 -m http.server 8765 &) ; node tools/export-placeholders.js   [needs playwright]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const ROOT = path.join(__dirname, '..');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('http://localhost:8765/index.html'); await p.waitForTimeout(800);
  const ph = await p.evaluate(() => window.__joetopia.placeholders());
  for (const [rel, url] of Object.entries(ph)) {
    const out = path.join(ROOT, rel); if (fs.existsSync(out) && !process.argv.includes('--force')) continue;
    fs.mkdirSync(path.dirname(out), { recursive: true }); fs.writeFileSync(out, Buffer.from(url.split(',')[1], 'base64')); console.log('wrote', rel);
  }
  await b.close();
})();
