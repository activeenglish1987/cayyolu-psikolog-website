// Statik site mobil tarayıcı taraması: konsol/JS hatası, yatay taşma, görünür H1, telefon/WhatsApp hedefleri
// Çalıştırma: python3 -m http.server 8771 -d . &  ve  node <bu dosya> . http://127.0.0.1:8771
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [ROOT, BASE] = [process.argv[2], process.argv[3]];
const urls = [];
(function walk(d) {
  for (const f of fs.readdirSync(d, { withFileTypes: true })) {
    if (f.isDirectory()) { if (!['.git', 'node_modules', '_araclar', '_kaynak', 'wp-content', 'assets', 'images'].includes(f.name)) walk(path.join(d, f.name)); }
    else if (f.name === 'index.html') urls.push('/' + path.relative(ROOT, d).split(path.sep).join('/') + (d === ROOT ? '' : '/'));
  }
})(ROOT);
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.route(/^(?!http:\/\/127\.0\.0\.1)/, r => r.abort());   // dış kaynaklar (GTM, font) test ortamında kapalı
  let errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 120)));
  p.on('console', m => { if (m.type() === 'error' && !/Failed to load resource|ERR_/.test(m.text())) errs.push(m.text().slice(0, 120)); });
  const bad = []; let n = 0;
  for (const u of urls.sort()) {
    errs = [];
    try { await p.goto(BASE + u, { waitUntil: 'load', timeout: 20000 }); await p.waitForTimeout(250); } catch (e) { bad.push(u + ' → açılmadı'); continue; }
    n++;
    const r = await p.evaluate(() => ({
      ov: document.documentElement.scrollWidth > innerWidth + 1,
      wide: [...document.querySelectorAll('body *')].filter(e => { const x = e.getBoundingClientRect(); return x.width && x.right > innerWidth + 2 && getComputedStyle(e).position !== 'fixed'; }).slice(0, 2).map(e => e.tagName + '.' + (e.className || '').toString().slice(0, 30)),
      h1: [...document.querySelectorAll('h1')].filter(h => h.offsetParent).length,
      tel: [...new Set([...document.querySelectorAll('a[href^="tel:"]')].map(a => a.getAttribute('href').replace(/\D/g, '')))].filter(t => t !== '905524187973' && t !== '112'),
      wa: [...new Set([...document.querySelectorAll('a[href*="wa.me/"]')].map(a => (a.getAttribute('href').match(/wa\.me\/(\d+)/) || [])[1]))].filter(t => t !== '905524187973'),
      call: [...document.querySelectorAll('a[href^="tel:"]')].some(a => { const x = a.getBoundingClientRect(); return x.width > 0 && x.height > 0; }),
    }));
    const iss = [];
    if (r.ov) iss.push('yatay taşma ' + r.wide.join(','));
    if (r.h1 !== 1) iss.push('görünür H1=' + r.h1);
    if (r.tel.length) iss.push('farklı tel ' + r.tel);
    if (r.wa.length) iss.push('farklı WhatsApp ' + r.wa);
    if (!r.call) iss.push('görünür arama butonu yok');
    if (errs.length) iss.push('JS: ' + [...new Set(errs)].join(' | '));
    if (iss.length) bad.push(u + ' → ' + iss.join('; '));
  }
  console.log(n + '/' + urls.length + ' sayfa açıldı; sorunlu: ' + bad.length); bad.forEach(x => console.log('  ' + x));
  await b.close();
})();
