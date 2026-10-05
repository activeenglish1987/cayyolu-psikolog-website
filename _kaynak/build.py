# -*- coding: utf-8 -*-
"""RN Psikoloji Çayyolu – statik site üretici.
Kullanım: python3 _kaynak/build.py
Girdi: _kaynak/icerik.json (extract.py ile WordPress'ten çıkarılır)
Çıktı: depo kökünde her sayfa için /adres/index.html, sitemap.xml, robots.txt, 404.html
"""
import html, json, os, re, shutil
from html.parser import HTMLParser
from urllib.parse import quote
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from landing import LANDINGS, BOOST, EXTRA
from makaleler import MAKALELER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '_kaynak')
SITE = 'https://www.cayyolupsikolog.com.tr'
BRAND = 'RN Psikoloji Çayyolu'
PHONE = '0552 418 79 73'
PHONE_RAW = '+905524187973'
WA_NUM = '905524187973'
EMAIL = 'info@cayyolupsikolog.com.tr'
ADDR = 'Konutkent, Dumlupınar Blv. No:399 Kat:28 Daire:121, 06810 Çankaya / Ankara'
ADDR_SHORT = 'Dumlupınar Blv. No:399 Kat:28 D:121, Konutkent – Yaşamkent'
GEO = (39.8874, 32.6783)
DIR_URL = 'https://www.google.com/maps/dir/?api=1&destination=%s,%s' % GEO
MAP_URL = 'https://www.google.com/maps/search/?api=1&query=' + quote('Dumlupınar Bulvarı No:399 Konutkent Çankaya Ankara')
IG_ROJIN = 'https://www.instagram.com/psikologrojinnazik/'
IG_ELIF = 'https://www.instagram.com/psikolog_eliferdogan/'
GTM = 'GTM-KMR7XRJQ'
ASSET_V = '4'

def wa(msg):
    return 'https://wa.me/%s?text=%s' % (WA_NUM, quote(msg))

def esc(s):
    return html.escape(s or '', quote=True)

# ---------------------------------------------------------------- görseller
OPT_DIR = os.path.join(ROOT, 'assets', 'img', 'opt')

def opt(src_rel, width=1000, name=None, quality=78):
    """Görselin küçültülmüş WebP kopyasını üretir; site içinde bu kopya kullanılır.
    Orijinal dosya eski WordPress adresinde kalır."""
    try:
        from PIL import Image
    except ImportError:
        return '/' + src_rel.lstrip('/')
    src = os.path.join(ROOT, src_rel.lstrip('/'))
    if not os.path.exists(src):
        return '/' + src_rel.lstrip('/')
    base = name or re.sub(r'[^a-z0-9]+', '-', os.path.splitext(os.path.basename(src))[0].lower()).strip('-')
    out_name = '%s-%d.webp' % (base, width)
    dest = os.path.join(OPT_DIR, out_name)
    if not os.path.exists(dest):
        os.makedirs(OPT_DIR, exist_ok=True)
        im = Image.open(src)
        im = im.convert('RGBA') if im.mode in ('P', 'LA') else im
        if im.mode == 'RGBA':
            bg = Image.new('RGB', im.size, (255, 255, 255)); bg.paste(im, mask=im.split()[-1]); im = bg
        elif im.mode != 'RGB':
            im = im.convert('RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(dest, 'WEBP', quality=quality, method=6)
    return '/assets/img/opt/' + out_name

def size_of(url):
    try:
        from PIL import Image
        p = os.path.join(ROOT, url.lstrip('/'))
        with Image.open(p) as im:
            return im.width, im.height
    except Exception:
        return None

def img(url, alt, cls='', eager=False, sizes=None):
    wh = size_of(url)
    dim = ' width="%d" height="%d"' % wh if wh else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    c = ' class="%s"' % cls if cls else ''
    return '<img src="%s" alt="%s"%s%s%s>' % (url, esc(alt), dim, load, c)

# ---------------------------------------------------------------- içerik temizleme
ALLOWED = {'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'b', 'em', 'i', 'a', 'img', 'figure',
           'figcaption', 'blockquote', 'br', 'table', 'thead', 'tbody', 'tr', 'td', 'th'}
RENAME = {'h1': 'h2', 'h5': 'h4', 'h6': 'h4', 'b': 'strong', 'i': 'em'}
DROP_WITH_CONTENT = {'script', 'style', 'svg', 'noscript', 'iframe', 'form', 'button', 'select', 'textarea'}
VOID = {'img', 'br'}

class Clean(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.skip = 0; self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag in DROP_WITH_CONTENT:
            self.skip += 1; return
        if self.skip: return
        tag = RENAME.get(tag, tag)
        if tag not in ALLOWED: return
        a = dict(attrs)
        if tag == 'img':
            src = (a.get('src') or '').replace(SITE, '')
            src = re.sub(r'-\d+x\d+(?=\.\w+$)', '', src)
            if not src or not os.path.exists(os.path.join(ROOT, src.lstrip('/'))):
                return
            self.out.append(img(src, a.get('alt') or '', 'content-img')); return
        if tag == 'a':
            href = (a.get('href') or '').replace(SITE, '') or '#'
            if href.startswith('/') and not href.endswith('/') and '.' not in href.split('/')[-1] and '#' not in href:
                href += '/'
            ext = href.startswith('http')
            self.out.append('<a href="%s"%s>' % (esc(href), ' target="_blank" rel="noopener"' if ext else ''))
        elif tag in VOID:
            self.out.append('<%s>' % tag); return
        else:
            self.out.append('<%s>' % tag)
        self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in DROP_WITH_CONTENT:
            self.skip = max(0, self.skip - 1); return
        if self.skip: return
        tag = RENAME.get(tag, tag)
        if tag not in ALLOWED or tag in VOID: return
        if tag in self.stack:
            while self.stack:
                t = self.stack.pop(); self.out.append('</%s>' % t)
                if t == tag: break
    def handle_data(self, data):
        if self.skip: return
        self.out.append(esc(data).replace('&#x27;', "'"))

def clean_html(raw):
    raw = re.sub(r'<!--.*?-->', '', raw or '', flags=re.S)
    p = Clean(); p.feed(raw); p.close()
    while p.stack: p.out.append('</%s>' % p.stack.pop())
    h = ''.join(p.out)
    h = re.sub(r'[ \t\r\f\v]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    # boş etiketleri temizle
    for _ in range(3):
        h = re.sub(r'<(p|h2|h3|h4|li|strong|em|figure|a[^>]*)>\s*(?:<br>\s*)*</(p|h2|h3|h4|li|strong|em|figure|a)>', '', h)
    # başıboş metin satırlarını paragrafa al
    lines = []
    for line in h.split('\n'):
        s = line.strip()
        if not s: continue
        if re.match(r'^<(p|h2|h3|h4|ul|ol|li|/ul|/ol|figure|blockquote|table|img|/p|/li)', s) or s.startswith('</'):
            lines.append(s)
        else:
            lines.append('<p>%s</p>' % s)
    h = '\n'.join(lines)
    h = re.sub(r'<p>\s*(Previous|Next|Randevu Al)\s*</p>', '', h)
    # başlık içindeki kalın etiketleri kaldır, madde işaretli satırları alt alta al
    h = re.sub(r'<(h[234])>\s*<strong>(.*?)</strong>\s*</\1>', r'<\1>\2</\1>', h)
    h = re.sub(r'(?<!<p>)<strong>\s*•\s*', '<br><strong>• ', h)
    return h

def plain(raw, n=None):
    t = re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style|svg).*?</\1>', ' ', raw or '', flags=re.S))
    t = html.unescape(re.sub(r'\s+', ' ', t)).strip()
    if n and len(t) > n:
        t = t[:n].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return t

# ---------------------------------------------------------------- ortak parçalar
SERVICES = [
    ('/bireysel-danismanlik/', 'Bireysel Danışmanlık', 'Kaygı, stres, özgüven ve yaşam geçişlerinde bire bir destek.', 'Yetişkin'),
    ('/cift-iliski-terapisi/', 'Çift ve İlişki Terapisi', 'İletişim, güven ve yakınlık konularında çift görüşmeleri.', 'Çiftler'),
    ('/cocuk-ergen-danismanligi/', 'Çocuk ve Ergen Danışmanlığı', 'Okul, duygu düzenleme ve gelişim süreçlerinde destek; oyun terapisi.', 'Çocuk · Ergen'),
    ('/aile-terapisi/', 'Aile Terapisi', 'Aile içi iletişim, sınırlar ve kuşak çatışmaları.', 'Aile'),
    ('/evlilik-oncesi-danismanlik/', 'Evlilik Öncesi Danışmanlık', 'Evliliğe hazırlık, beklentiler ve ortak hedefler.', 'Çiftler'),
    ('/bosanma-sonrasi-danismanlik/', 'Boşanma Sonrası Danışmanlık', 'Ayrılık ve boşanma sürecinde duygusal destek.', 'Yetişkin'),
    ('/kaygi-sorunlari/', 'Kaygı Sorunları', 'Yoğun kaygı, panik ve sosyal kaygıda psikolojik destek.', 'Yetişkin'),
    ('/yetiskinler-icin/', 'Yetişkinler İçin', 'Yetişkinlere yönelik bireysel görüşme alanları.', 'Yetişkin'),
    ('/online-terapi/', 'Online Terapi', 'Ankara dışında olanlar için online görüşme seçeneği.', 'Online'),
]
EXPERTS = [
    {'path': '/psikolog-rojin-nazik/', 'name': 'Psikolog Rojin Nazik', 'role': 'Kurucu Psikolog',
     'areas': 'Yetişkin · Bireysel · Çift ve aile', 'img': 'wp-content/uploads/2024/05/Psikolog_Rojin_Nazik.jpg',
     'ig': IG_ROJIN, 'ig_handle': '@psikologrojinnazik'},
    {'path': '/psikolog-elif-erdogan/', 'name': 'Psikolog Elif Erdoğan', 'role': 'Psikolog',
     'areas': 'Yetişkin · Ergen · Çift · Oyun terapisi', 'img': 'assets/img/team-elif-erdogan.webp',
     'ig': IG_ELIF, 'ig_handle': '@psikolog_eliferdogan'},
    {'path': '/psikolog-hazal-aksahin/', 'name': 'Klinik Psikolog Hazal Akşahin', 'role': 'Klinik Psikolog',
     'areas': 'Çocuk · Ergen · Yetişkin', 'img': 'wp-content/uploads/2024/11/hazal-aksahin.jpg',
     'ig': '', 'ig_handle': ''},
]
AREAS = [
    ('Çayyolu', '/'),
    ('Ümitköy', '/umitkoy-psikolog/'),
    ('Yaşamkent', '/yasamkent-psikolog/'),
    ('Konutkent', '/konutkent-psikolog/'),
    ('İncek', '/incek-psikolog/'),
    ('Beysukent', '/beysukent-psikolog/'),
    ('Alacaatlı', '/alacaatli-psikolog/'),
]
FOCUS = [
    ('/cayyolu-cocuk-psikologu/', 'Çocuk ve Ergen Psikoloğu'),
    ('/cayyolu-cift-terapisi/', 'Çift Terapisi'),
    ('/cayyolu-aile-terapisi/', 'Aile Terapisi'),
    ('/cayyolu-psikolojik-danismanlik-merkezi/', 'Psikolojik Danışmanlık Merkezi'),
    ('/cayyolu-psikolog-fiyatlari/', 'Psikolog Fiyatları'),
]

ICON = {
 'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'wa': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M.06 24l1.69-6.16A11.87 11.87 0 0 1 .16 11.9C.16 5.33 5.5 0 12.06 0c3.18 0 6.16 1.24 8.41 3.49a11.82 11.82 0 0 1 3.48 8.41c0 6.56-5.34 11.9-11.9 11.9a11.9 11.9 0 0 1-5.69-1.45L.06 24zm6.6-3.8c1.67.99 3.27 1.59 5.39 1.59 5.45 0 9.89-4.43 9.89-9.88C21.94 6.45 17.53 2.02 12.06 2 6.61 2 2.18 6.43 2.17 11.88c0 2.23.65 3.9 1.75 5.64l-1 3.64 3.74-.97zm11.39-5.47c-.08-.12-.27-.2-.57-.35-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51l-.57-.01c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2.01-1.41.25-.69.25-1.29.17-1.41z"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.1-7-11.5A7 7 0 0 1 19 9.5C19 14.9 12 21 12 21z" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="9.5" r="2.6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
 'car': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 16V11l2-5h10l2 5v5M5 16h14M5 16v2M19 16v2M7.5 13.5h.01M16.5 13.5h.01" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'ig': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.1" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

def btn_call(label='Hemen Ara', cls='btn btn-call'):
    return '<a class="%s" href="tel:%s">%s<span>%s</span></a>' % (cls, PHONE_RAW, ICON['phone'], label)

def btn_wa(msg='Merhaba, randevu bilgisi almak istiyorum.', label="WhatsApp'tan Bilgi Al", cls='btn btn-wa'):
    return '<a class="%s" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a>' % (cls, wa(msg), ICON['wa'], label)

OPEN_STATUS = '<div class="open-status" data-open-status></div>'

def inline_cta(msg='Merhaba, randevu bilgisi almak istiyorum.', title='Randevu için hemen ulaşın'):
    return '<aside class="inline-cta"><p><strong>%s</strong>Pazartesi – Cumartesi 09:00 – 20:00 · Yaşamkent ofisi · Ücretsiz otopark</p><div class="btn-row">%s%s</div></aside>' % (
        esc(title), btn_call(), btn_wa(msg))

def with_mid_cta(body, expert=None):
    """Uzun yazılarda metnin ortasına randevu kutusu ekler."""
    idx = [m.start() for m in re.finditer(r'<h2>', body)]
    if len(idx) < 3:
        return body
    msg = ('Merhaba, %s ile görüşme için randevu bilgisi almak istiyorum.' % expert['name']) if expert else 'Merhaba, randevu bilgisi almak istiyorum.'
    k = idx[len(idx) // 2]
    return body[:k] + inline_cta(msg) + body[k:]

def head(title, desc, path, extra_ld='', og_img='/assets/img/opt/og-1200.webp', noindex=False):
    canon = SITE + path
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large'
    return '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','%(gtm)s');</script>
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="%(robots)s">
<link rel="canonical" href="%(canon)s">
<meta property="og:locale" content="tr_TR">
<meta property="og:type" content="website">
<meta property="og:site_name" content="%(brand)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:image" content="%(site)s%(og)s">
<meta name="theme-color" content="#14264A">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v=%(v)s">
<script src="/assets/js/ads-conversion.js?v=2" defer></script>
<script src="/assets/js/site.js?v=%(v)s" defer></script>
<script src="/assets/js/after-hours.js?v=1" defer></script>
<script src="//code.jivosite.com/widget/qUPsGwSDuo" async></script>
%(ld)s
</head>''' % {'gtm': GTM, 'title': esc(title), 'desc': esc(desc), 'robots': robots, 'canon': canon, 'brand': esc(BRAND),
              'site': SITE, 'og': og_img, 'v': ASSET_V, 'ld': extra_ld}

def nav_html(current):
    svc_links = ''.join('<a href="%s">%s</a>' % (p, esc('Çayyolu ' + t)) for p, t in FOCUS[:3]) + ''.join('<a href="%s">%s</a>' % (p, esc(t)) for p, t, _, _ in SERVICES)
    exp_links = ''.join('<a href="%s">%s</a>' % (e['path'], esc(e['name'])) for e in EXPERTS)
    def cur(p): return ' aria-current="page"' if current == p else ''
    return '''<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%(gtm)s" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="/" aria-label="%(brand)s ana sayfa">
      <span class="logo-mark" aria-hidden="true">RN</span>
      <span class="logo-text"><b>RN Psikoloji</b><small>Çayyolu Şubesi</small></span>
    </a>
    <nav class="main-nav" aria-label="Ana menü" id="ana-menu">
      <div class="nav-group"><a href="/uzmanlarimiz/"%(c_u)s>Uzmanlarımız</a><div class="nav-drop">%(exp)s</div></div>
      <div class="nav-group"><a href="/#hizmetler">Hizmetler</a><div class="nav-drop">%(svc)s</div></div>
      <a href="/basinda-biz/"%(c_b)s>Basında Biz</a>
      <a href="/blog/"%(c_bl)s>Blog</a>
      <a href="/iletisim/"%(c_i)s>İletişim</a>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:%(raw)s">%(ic)s<span>%(phone)s</span></a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="ana-menu" aria-label="Menüyü aç"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="icerik">''' % {'gtm': GTM, 'brand': esc(BRAND), 'exp': exp_links, 'svc': svc_links, 'raw': PHONE_RAW,
                         'phone': PHONE, 'ic': ICON['phone'], 'c_u': cur('/uzmanlarimiz/'), 'c_b': cur('/basinda-biz/'),
                         'c_bl': cur('/blog/'), 'c_i': cur('/iletisim/')}

def footer_html():
    svc = ''.join('<li><a href="%s">%s</a></li>' % (p, esc(t)) for p, t, _, _ in SERVICES[:7])
    exp = ''.join('<li><a href="%s">%s</a></li>' % (e['path'], esc(e['name'])) for e in EXPERTS)
    return '''</main>
<section class="cta-band">
  <div class="wrap cta-band-inner">
    <div><p class="eyebrow light">İlk adım</p><h2>Randevu ve bilgi için bize ulaşın.</h2><p>Pazartesi – Cumartesi 09:00 – 20:00 · Yaşamkent ofisi</p></div>
    <div class="btn-row">%(call)s%(wa)s</div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <a class="logo logo-light" href="/"><span class="logo-mark" aria-hidden="true">RN</span><span class="logo-text"><b>RN Psikoloji</b><small>Çayyolu Şubesi</small></span></a>
      <p>Çayyolu, Ümitköy, Konutkent, Yaşamkent ve İncek'e yakın ofisimizde yüz yüze psikolojik danışmanlık.</p>
      <p class="footer-note">RN Psikoloji Çayyolu şubesinde çalışan uzmanlar klinik tanı veya tedavi hizmeti vermez; günlük yaşamda karşılaşılan zorluklar karşısında psikolojik destek ve danışmanlık hizmeti sunar. Tanı gerektiren durumlarda psikiyatriste yönlendirme yapılır.</p>
    </div>
    <div><h3>Uzmanlarımız</h3><ul>%(exp)s</ul><h3 class="mt">Bölgeler</h3><ul>%(areas)s</ul><h3 class="mt">Kurumsal</h3><ul><li><a href="/hakkimizda/">Hakkımızda</a></li><li><a href="/basinda-biz/">Basında Biz</a></li><li><a href="/kitaplarimiz/">Kitaplarımız</a></li><li><a href="/konferanslar/">Konferanslar</a></li><li><a href="/galeri/">Galeri</a></li><li><a href="/danisanlar-icin-el-kitabi/">Danışanlar İçin El Kitabı</a></li><li><a href="/blog/">Blog</a></li></ul></div>
    <div><h3>Hizmetler</h3><ul>%(svc)s</ul><h3 class="mt">Çayyolu'nda</h3><ul>%(focus)s</ul></div>
    <div><h3>İletişim</h3>
      <p class="footer-line">%(pin)s<span>%(addr)s</span></p>
      <p class="footer-line">%(phone_ic)s<a href="tel:%(raw)s">%(phone)s</a></p>
      <p class="footer-line">%(clock)s<span>Pazartesi – Cumartesi · 09:00 – 20:00</span></p>
      <p class="footer-line">%(ig)s<a href="%(igu)s" target="_blank" rel="noopener">@psikologrojinnazik</a></p>
      <p class="footer-line"><a href="mailto:%(email)s">%(email)s</a></p>
      <a class="text-link light" href="%(dir)s" target="_blank" rel="noopener">Yol tarifi al %(arrow)s</a>
    </div>
  </div>
  <div class="wrap footer-bottom"><span>© 2026 %(brand)s</span><span><a href="https://www.psikologrojinnazik.com/" target="_blank" rel="noopener">psikologrojinnazik.com</a> · <a href="https://www.psikologeliferdogan.com/" target="_blank" rel="noopener">psikologeliferdogan.com</a></span></div>
</footer>
<div class="sticky-bar" role="navigation" aria-label="Hızlı iletişim">%(call2)s%(wa2)s</div>
</body>
</html>''' % {'call': btn_call(), 'wa': btn_wa(), 'svc': svc, 'exp': exp, 'pin': ICON['pin'], 'addr': esc(ADDR),
              'phone_ic': ICON['phone'], 'raw': PHONE_RAW, 'phone': PHONE, 'clock': ICON['clock'], 'ig': ICON['ig'],
              'igu': IG_ROJIN, 'email': EMAIL, 'dir': DIR_URL, 'arrow': ICON['arrow'], 'brand': esc(BRAND),
              'call2': btn_call('Hemen Ara', 'sb-call'), 'wa2': btn_wa(label='WhatsApp', cls='sb-wa'),
              'areas': ''.join('<li><a href="%s">%s Psikolog</a></li>' % (p, esc(a)) for a, p in AREAS),
              'focus': ''.join('<li><a href="%s">Çayyolu %s</a></li>' % (p, esc(t)) for p, t in FOCUS)}

def office_card(compact=False):
    return '''<div class="office-card">
  <div class="office-info">
    <p class="eyebrow">Ofisimiz</p>
    <h3>Yaşamkent / Çayyolu</h3>
    <p class="office-line">%(pin)s<span>%(addr)s</span></p>
    <p class="office-line">%(clock)s<span><b>Pazartesi – Cumartesi</b> · 09:00 – 20:00, randevulu görüşme</span></p>
    <p class="office-line">%(car)s<span>Ücretsiz otopark mevcut</span></p>
    <p class="office-near">Çayyolu, Ümitköy, Konutkent, İncek ve Alacaatlı'ya yakın.</p>
    <div class="btn-row">
      <a class="btn btn-line" href="%(dir)s" target="_blank" rel="noopener">%(pin)s<span>Yol Tarifi</span></a>
      %(wa)s
    </div>
  </div>
</div>''' % {'pin': ICON['pin'], 'addr': esc(ADDR), 'clock': ICON['clock'], 'car': ICON['car'], 'dir': DIR_URL,
             'wa': btn_wa('Merhaba, Yaşamkent ofisiniz için randevu bilgisi almak istiyorum.', 'Randevu Bilgisi Al')}

def expert_cards(exclude=None):
    out = []
    for e in EXPERTS:
        if e['path'] == exclude: continue
        feat = ' expert-card--feature' if e['path'] == '/psikolog-rojin-nazik/' and not exclude else ''
        photo = opt(e['img'], 720, name=re.sub(r'[^a-z]+', '-', e['path'].strip('/')))
        ig = ('<a class="expert-ig" href="%s" target="_blank" rel="noopener">%s<span>%s</span></a>' % (e['ig'], ICON['ig'], e['ig_handle'])) if e['ig'] else ''
        out.append('''<article class="expert-card%(feat)s">
  <a class="expert-photo" href="%(path)s">%(img)s</a>
  <div class="expert-body">
    <p class="expert-role">%(role)s</p>
    <h3><a href="%(path)s">%(name)s</a></h3>
    <p class="expert-areas">%(areas)s</p>
    <div class="expert-actions"><a class="btn btn-line btn-sm" href="%(path)s">Profili İncele</a>%(wa)s</div>
    %(ig)s
  </div>
</article>''' % {'feat': feat, 'path': e['path'], 'img': img(photo, e['name']), 'role': esc(e['role']), 'name': esc(e['name']),
                 'areas': esc(e['areas']), 'ig': ig,
                 'wa': btn_wa('Merhaba, %s ile görüşme için randevu bilgisi almak istiyorum.' % e['name'], 'Randevu', 'btn btn-wa btn-sm')})
    return '<div class="expert-grid">%s</div>' % ''.join(out)

def service_cards():
    return '<div class="svc-grid">' + ''.join('''<a class="svc-card" href="%s"><span class="svc-tag">%s</span><h3>%s</h3><p>%s</p><span class="svc-more">Detaylı bilgi %s</span></a>''' % (
        p, esc(tag), esc(t), esc(d), ICON['arrow']) for p, t, d, tag in SERVICES) + '</div>'

FAQS = [
    ('İlk görüşme nasıl ilerliyor?', 'Telefon veya WhatsApp üzerinden ulaşırsınız; uygun uzman, gün ve saat birlikte belirlenir. İlk görüşmede başvuru nedeniniz, beklentileriniz ve yaşam öykünüz dinlenir; ardından size uygun görüşme planı oluşturulur.'),
    ('Ofisiniz nerede?', 'Ofisimiz Yaşamkent\'te, Konutkent Dumlupınar Bulvarı No:399 Kat:28 Daire:121 adresindedir. Çayyolu, Ümitköy, Konutkent, İncek ve Alacaatlı\'ya yakındır; ücretsiz otopark vardır.'),
    ('Hangi gün ve saatlerde görüşme yapılıyor?', 'Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 saatleri arasında randevu ile yapılır.'),
    ('Hangi uzmanla görüşeceğime nasıl karar verebilirim?', 'Başvuru nedeninizi kısaca paylaşmanız yeterli; çocuk, ergen, yetişkin veya çift görüşmesi olmasına göre size uygun uzman önerilir. Uzmanlarımızın profillerini <a href="/uzmanlarimiz/">Uzmanlarımız</a> sayfasında inceleyebilirsiniz.'),
    ('Ücret bilgisine nasıl ulaşabilirim?', 'Güncel ücret bilgisini WhatsApp\'tan yazarak ya da <a href="tel:%s">%s</a> numarasını arayarak öğrenebilirsiniz.' % (PHONE_RAW, PHONE)),
    ('Randevumu nasıl değiştirebilirim?', 'Randevu değişikliği için WhatsApp\'tan yazabilir ya da <a href="tel:%s">%s</a> numarasını arayabilirsiniz.' % (PHONE_RAW, PHONE)),
]

def faq_html(faqs=FAQS):
    return '<div class="faq">' + ''.join('<details><summary>%s</summary><div class="faq-a"><p>%s</p></div></details>' % (esc(q), a) for q, a in faqs) + '</div>'

def faq_ld(faqs=FAQS):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in faqs]}

def business_ld():
    return {'@type': 'Psychologist', '@id': SITE + '/#isletme', 'name': BRAND, 'url': SITE + '/', 'telephone': PHONE_RAW,
            'email': EMAIL, 'image': SITE + '/assets/img/opt/og-1200.webp', 'priceRange': '₺₺',
            'address': {'@type': 'PostalAddress', 'streetAddress': 'Konutkent, Dumlupınar Blv. No:399 Kat:28 Daire:121',
                        'addressLocality': 'Çankaya', 'addressRegion': 'Ankara', 'postalCode': '06810', 'addressCountry': 'TR'},
            'geo': {'@type': 'GeoCoordinates', 'latitude': GEO[0], 'longitude': GEO[1]},
            'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 'opens': '09:00', 'closes': '20:00'}],
            'areaServed': ['Çayyolu', 'Ümitköy', 'Yaşamkent', 'Konutkent', 'İncek', 'Beysukent', 'Alacaatlı', 'Ankara'],
            'sameAs': [IG_ROJIN],
            'founder': {'@type': 'Person', '@id': 'https://www.psikologrojinnazik.com/#rojin-nazik', 'name': 'Rojin Nazik', 'jobTitle': 'Psikolog',
                        'url': SITE + '/psikolog-rojin-nazik/', 'sameAs': ['https://www.wikidata.org/wiki/Q141626009', 'https://www.psikologrojinnazik.com/rojin-nazik-biyografi/', IG_ROJIN]},
            'employee': [{'@type': 'Person', 'name': 'Elif Erdoğan', 'jobTitle': 'Psikolog', 'url': SITE + '/psikolog-elif-erdogan/',
                          'sameAs': ['https://psikologeliferdogan.com/', IG_ELIF]},
                         {'@type': 'Person', 'name': 'Hazal Akşahin', 'jobTitle': 'Klinik Psikolog', 'url': SITE + '/psikolog-hazal-aksahin/'}]}

def ld(*objs):
    return '<script type="application/ld+json">%s</script>' % json.dumps({'@context': 'https://schema.org', '@graph': list(objs)}, ensure_ascii=False)

def breadcrumb(items):
    lis = ''.join(('<li><a href="%s">%s</a></li>' % (p, esc(t))) if p else ('<li aria-current="page">%s</li>' % esc(t)) for t, p in items)
    data = {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': t, **({'item': SITE + p} if p else {})} for i, (t, p) in enumerate(items)]}
    return '<nav class="crumbs" aria-label="Sayfa yolu"><ol>%s</ol></nav>' % lis, data

def write(path, content):
    dest = os.path.join(ROOT, path.strip('/'), 'index.html') if path != '/' else os.path.join(ROOT, 'index.html')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(content)

# ---------------------------------------------------------------- sayfa şablonları
def side_card(expert=None):
    if expert:
        ig = '<a class="text-link" href="%s" target="_blank" rel="noopener">%s %s</a>' % (expert['ig'], ICON['ig'], expert['ig_handle']) if expert['ig'] else ''
        who = '<p class="side-who">%s ile görüşmek için</p>' % esc(expert['name'])
        msg = 'Merhaba, %s ile görüşme için randevu bilgisi almak istiyorum.' % expert['name']
    else:
        ig = ''; who = '<p class="side-who">Randevu ve bilgi için</p>'; msg = 'Merhaba, randevu bilgisi almak istiyorum.'
    return '''<aside class="side-card">
  %(who)s
  <a class="side-phone" href="tel:%(raw)s">%(phone)s</a>
  %(open)s
  <div class="btn-col">%(call)s%(wa)s</div>
  <p class="office-line small">%(pin)s<span>Yaşamkent ofisi · Pazartesi – Cumartesi 09:00 – 20:00</span></p>
  <a class="text-link" href="%(dir)s" target="_blank" rel="noopener">Yol tarifi al %(arrow)s</a>
  %(ig)s
</aside>''' % {'who': who, 'raw': PHONE_RAW, 'phone': PHONE, 'open': OPEN_STATUS, 'call': btn_call(), 'wa': btn_wa(msg),
               'pin': ICON['pin'], 'dir': DIR_URL, 'arrow': ICON['arrow'], 'ig': ig}

def article_page(rec, body_html, crumbs, kicker='', expert=None, lead='', hero_img=None, extra_after='', extra_ld=None, desc=None, title_tag=None):
    title = rec['title']
    bc_html, bc_ld = breadcrumb(crumbs)
    lds = [business_ld(), bc_ld]
    if rec.get('type') == 'post':
        lds.append({'@type': 'BlogPosting', 'headline': title, 'datePublished': rec['date'], 'dateModified': rec.get('modified') or rec['date'],
                    'author': {'@type': 'Organization', 'name': BRAND}, 'mainEntityOfPage': SITE + rec['path']})
    if extra_ld: lds.extend(extra_ld)
    d = desc or rec.get('seo_desc') or plain(body_html, 155)
    tt = title_tag or rec.get('seo_title') or (title if len(title) > 42 else '%s | %s' % (title, BRAND))
    hero_fig = ('<figure class="article-hero-img">%s</figure>' % img(hero_img, title, eager=True)) if hero_img else ''
    meta = ('<p class="article-meta">%s · %s</p>' % (esc(BRAND), fmt_date(rec['date']))) if rec.get('type') == 'post' else ''
    return head(tt, d, rec['path'], ld(*lds)) + nav_html(rec['path']) + '''
<section class="page-hero">
  <div class="wrap">
    %(bc)s
    %(kicker)s
    <h1>%(title)s</h1>
    %(lead)s
    %(meta)s
    <div class="btn-row hero-btns">%(call)s%(wa)s</div>
    %(open)s
  </div>
</section>
<div class="wrap article-layout">
  <article class="prose">%(fig)s%(body)s</article>
  %(side)s
</div>
%(after)s
''' % {'bc': bc_html, 'kicker': ('<p class="eyebrow">%s</p>' % esc(kicker)) if kicker else '', 'title': esc(title),
       'lead': ('<p class="page-lead">%s</p>' % lead) if lead else '', 'meta': meta, 'call': btn_call(),
       'wa': btn_wa(('Merhaba, %s ile görüşme için randevu bilgisi almak istiyorum.' % expert['name']) if expert else 'Merhaba, randevu bilgisi almak istiyorum.'),
       'open': OPEN_STATUS, 'fig': hero_fig, 'body': body_html, 'side': side_card(expert), 'after': extra_after} + footer_html()

TR_MONTHS = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
def fmt_date(d):
    try:
        y, m, dd = d.split('-'); return '%d %s %s' % (int(dd), TR_MONTHS[int(m) - 1], y)
    except Exception:
        return d

def related_block(title, cards_html):
    return '<section class="section section-alt"><div class="wrap"><div class="section-head"><h2>%s</h2></div>%s</div></section>' % (esc(title), cards_html)

def blog_card(rec):
    th = rec.get('thumb') or ''
    if th and os.path.exists(os.path.join(ROOT, th.lstrip('/'))):
        pic = img(opt(th, 640), rec['title'])
    else:
        pic = '<div class="blog-ph" aria-hidden="true"><span>RN</span></div>'
    return '<a class="blog-card" href="%s"><div class="blog-pic">%s</div><div class="blog-body"><p class="blog-date">%s</p><h3>%s</h3><p>%s</p></div></a>' % (
        rec['path'], pic, fmt_date(rec['date']), esc(rec['title']), esc(plain(rec['html'], 120)))

# ---------------------------------------------------------------- özel içerikler
ELIF_BODY = '''
<h2>Psikolog Elif Erdoğan</h2>
<p>Psikolog Elif Erdoğan, RN Psikoloji Çayyolu şubesinde yetişkin, ergen ve çiftlerle yüz yüze görüşmeler yürütür; çocuklarla oyun terapisi yaklaşımıyla çalışır.</p>
<p>Lisans eğitimini Başkent Üniversitesi Psikoloji Bölümü'nde yüksek şeref derecesiyle tamamlamıştır. Bilişsel ve Davranışçı Terapiler alanındaki eğitimlerini DATEM bünyesinde sürdürmüştür. MMPI başta olmak üzere yetişkin ve çocuk değerlendirme araçlarının uygulayıcısıdır.</p>
<h3>Çalışma alanları</h3>
<ul>
<li>Yetişkinlerde kaygı, stres, duygu düzenleme ve tekrarlayan düşünce örüntüleri</li>
<li>Ergenlerde okul, sınav kaygısı, özgüven ve aile içi iletişim</li>
<li>Çift ve ilişki danışmanlığı</li>
<li>Çocuklarla oyun terapisi</li>
<li>Psikolojik test ve değerlendirme</li>
</ul>
<h3>Çalışma yaklaşımı</h3>
<p>Görüşmelerde bilimsel temelli, yapılandırılmış bir süreç izlenir. İlk görüşmede başvuru nedeni ve beklentiler ele alınır; ardından ihtiyaca göre çalışma hedefleri ve uygun yöntemler birlikte belirlenir.</p>
<p>Psikolog Elif Erdoğan'ın kişisel web sitesi: <a href="https://www.psikologeliferdogan.com/" target="_blank" rel="noopener">psikologeliferdogan.com</a></p>
'''

def section_head(eyebrow, title, lead=''):
    return '<div class="section-head"><p class="eyebrow">%s</p><h2>%s</h2>%s</div>' % (esc(eyebrow), title, ('<p>%s</p>' % lead) if lead else '')

# ---------------------------------------------------------------- ana sayfa
REVIEWS = []

def reviews_html(n=5):
    return '<div class="review-grid">%s</div>' % ''.join('<figure class="review"><blockquote>%s</blockquote><figcaption>%s</figcaption></figure>' % (esc(t), esc(n_)) for t, n_ in REVIEWS[:n])

def home_page(recs, posts):
    home = next(r for r in recs if r['path'] == '/')
    body = clean_html(home['html'])
    # WordPress ana sayfasındaki "Çayyolu'nda psikolog seçimi" rehber metni korunur
    i = body.find("<h2>Çayyolu'nda Psikolog Seçmenin Önemi")
    guide = body[i:] if i >= 0 else ''
    guide = re.sub(r'<p>\s*<a href="tel:[^"]*">\s*</a>\s*</p>', '', guide)
    parts = re.split(r'(?=<h2>)', guide)
    parts = [p for p in parts if p.strip()]
    guide_open = ''.join(parts[:1]); guide_more = ''.join(parts[1:])
    j = body.find('<h2>Danışan Yorumları')
    reviews = []
    if j >= 0:
        seg = body[j:body.find('<h2>', j + 5)]
        ps = [plain(x) for x in re.findall(r'<p>(.*?)</p>', seg, re.S)]
        ps = [x for x in ps if x and x not in ('Previous', 'Next')]
        for k in range(0, len(ps) - 1, 2):
            if len(ps[k]) > 60 and len(ps[k + 1]) < 40:
                reviews.append((ps[k], ps[k + 1]))
    REVIEWS[:] = reviews
    hero_img = opt('assets/img/rojin-nazik-acilis-2.jpg', 840, 'hero-rojin-studyo')
    office1 = opt('wp-content/uploads/2024/05/seans-odasi-1.jpg', 900, 'seans-odasi')
    office2 = opt('wp-content/uploads/2024/05/prev01.webp', 900, 'bekleme-alani')
    press = [('wp-content/uploads/2024/05/cnn-1.png', 'CNN Türk'), ('wp-content/uploads/2024/05/milliyet-1.png', 'Milliyet'),
             ('wp-content/uploads/2024/05/sabah-1.png', 'Sabah'), ('wp-content/uploads/2024/05/posta-1.png', 'Posta'),
             ('wp-content/uploads/2024/05/haberler.com_.png', 'Haberler.com'), ('wp-content/uploads/2024/05/acunn-1.png', 'Acunn')]
    press_html = ''.join('<figure class="press-item">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 560), 'Psikolog Rojin Nazik – ' + n), esc(n)) for p, n in press)
    books = [('wp-content/uploads/2024/05/bir-hayatla-evlenmek.webp', 'Bir Hayatla Evlenmek'), ('wp-content/uploads/2024/05/bir-odanin-otesi-500x500-1.webp', 'Bir Odanın Ötesi'), ('wp-content/uploads/2024/05/dengeyi-yakalamak.webp', 'Dengeyi Yakalamak')]
    books_html = ''.join('<figure class="book">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 420), n + ' – Rojin Nazik'), esc(n)) for p, n in books)
    reviews_html = ''.join('<figure class="review"><blockquote>%s</blockquote><figcaption>%s</figcaption></figure>' % (esc(t), esc(n)) for t, n in reviews[:5])
    areas_html = ''.join('<a class="area-chip" href="%s">%s %s psikolog</a>' % (p, ICON['pin'], esc(a)) for a, p in AREAS if p != '/') + \
        ''.join('<a class="area-chip" href="%s">%s Çayyolu %s</a>' % (p, ICON['arrow'], esc(t)) for p, t in FOCUS)
    latest = ''.join(blog_card(p) for p in posts[:3])
    # WordPress döneminde yıllarca 1. sırada duran başlık korunur (2026-10-05)
    title = 'Çayyolu Psikolog | Ankara Çayyolu Psikolog – RN Psikoloji'
    desc = "Çayyolu psikolog arıyorsanız: RN Psikoloji Çayyolu'nda çocuk, ergen, yetişkin, çift ve aile danışmanlığı. Ümitköy, Yaşamkent, Konutkent ve İncek'e yakın. Randevu: 0552 418 79 73."
    return head(title, desc, '/', ld(business_ld(), {'@type': 'WebSite', 'name': BRAND, 'url': SITE + '/'}, faq_ld())) + nav_html('/') + '''
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">RN Psikoloji · Çayyolu Şubesi</p>
      <h1>Çayyolu Psikolog</h1>
      <p class="hero-lead">Yaşamkent'teki ofisimizde, Çayyolu, Ümitköy, Konutkent ve İncek'e yakın yüz yüze psikolojik danışmanlık. Çocuk, ergen, yetişkin, çift ve aile.</p>
      <div class="btn-row hero-btns">%(call)s%(wa)s</div>
      %(open)s
      <ul class="hero-facts">
        <li>Kurucu: <b>Psikolog Rojin Nazik</b></li>
        <li>Pazartesi – Cumartesi · 09:00 – 20:00</li>
        <li>Ücretsiz otopark</li>
      </ul>
    </div>
    <div class="hero-media">
      <div class="hero-photo">%(hero_img)s</div>
      <a class="hero-badge" href="/psikolog-rojin-nazik/"><span class="hb-k">Kurucu Psikolog</span><b>Rojin Nazik</b><span class="hb-s">AB Psikologlar Derneği Genel Başkanı · 3 kitap · TV programları</span></a>
    </div>
  </div>
</section>
%(trust)s

<section class="section section-tight">
  <div class="wrap office-grid">
    %(office)s
    <div class="office-photos">%(o1)s%(o2)s</div>
  </div>
</section>

<section class="section" id="uzmanlar">
  <div class="wrap">
    %(h_exp)s
    %(experts)s
  </div>
</section>

<section class="section section-alt" id="hizmetler">
  <div class="wrap">
    %(h_svc)s
    %(services)s
    <p class="center-note">Hangi hizmetin size uygun olduğundan emin değil misiniz? <a href="%(wa_help)s" target="_blank" rel="noopener">WhatsApp'tan kısaca yazın</a>, size uygun uzmanı birlikte belirleyelim.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="section-head light"><p class="eyebrow light">Basında Rojin Nazik</p><h2>Ekranda, gazetelerde ve kitaplarda</h2><p>Psikolog Rojin Nazik; TV programları, gazete röportajları ve yayınlanmış üç kitabıyla psikolojiyi anlaşılır kılmak için çalışıyor.</p></div>
    <div class="press-grid">%(press)s</div>
    <div class="books-row">%(books)s<div class="books-cta"><a class="btn btn-light" href="/basinda-biz/">Basında Biz</a><a class="text-link light" href="/kitaplarimiz/">Kitaplarımız %(arrow)s</a></div></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    %(h_rev)s
    <div class="review-grid">%(reviews)s</div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap steps-wrap">
    %(h_steps)s
    <ol class="steps">
      <li><h3>Ulaşın</h3><p>Telefon veya WhatsApp üzerinden kısaca başvuru nedeninizi paylaşın.</p></li>
      <li><h3>Uzman ve saat belirlenir</h3><p>Size uygun uzman, gün ve saat birlikte netleştirilir.</p></li>
      <li><h3>İlk görüşme</h3><p>İhtiyacınız dinlenir, size uygun görüşme planı oluşturulur.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    %(h_area)s
    <div class="area-chips">%(areas)s</div>
  </div>
</section>

<section class="section section-alt" id="sss">
  <div class="wrap narrow">
    %(h_faq)s
    %(faq)s
  </div>
</section>

<section class="section">
  <div class="wrap narrow prose home-guide">
    <p class="eyebrow">Rehber</p>
    %(guide_open)s
    <details class="more"><summary>Rehberin devamını okuyun</summary>%(guide_more)s</details>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    %(h_blog)s
    <div class="blog-grid">%(latest)s</div>
    <p class="center-note"><a class="text-link" href="/blog/">Tüm yazılar %(arrow)s</a></p>
  </div>
</section>
''' % {'call': btn_call(), 'wa': btn_wa(), 'open': OPEN_STATUS, 'hero_img': img(hero_img, 'Psikolog Rojin Nazik, RN Psikoloji Çayyolu', eager=True),
       'trust': TRUST, 'office': office_card(), 'o1': img(office1, 'RN Psikoloji Çayyolu seans odası'), 'o2': img(office2, 'RN Psikoloji Çayyolu bekleme alanı'),
       'h_exp': section_head('Uzmanlarımız', 'Size uygun uzmanla görüşün', 'Çocuk, ergen, yetişkin ve çift görüşmelerinde deneyimli psikologlarımız.'),
       'experts': expert_cards(), 'h_svc': section_head('Hizmetler', 'Hangi konuda destek almak istersiniz?'), 'services': service_cards(),
       'wa_help': wa('Merhaba, hangi hizmetin bana uygun olduğunu öğrenmek istiyorum.'),
       'press': press_html, 'books': books_html, 'arrow': ICON['arrow'],
       'h_rev': section_head('Danışan yorumları', 'Danışanlarımız ne diyor?'), 'reviews': reviews_html,
       'h_steps': section_head('Görüşme süreci', 'İlk adım nasıl işler?'),
       'h_area': section_head('Bölgeler', 'Çayyolu ve çevresinde psikolog', 'Yaşamkent ofisimize yakın semtlerden danışanlarımız için hazırladığımız rehberler.'), 'areas': areas_html,
       'h_faq': section_head('Randevu öncesi', 'Sık sorulan sorular'), 'faq': faq_html(),
       'guide_open': guide_open, 'guide_more': guide_more,
       'h_blog': section_head('Blog', 'Son yazılar'), 'latest': latest} + footer_html()

TRUST = '''<section class="trust-strip" aria-label="Neden RN Psikoloji"><ul>
<li><b>15+ yıl</b>danışmanlık deneyimi</li>
<li><b>3 kitap</b>Psikolog Rojin Nazik</li>
<li><b>CNN Türk · Beyaz TV</b>TV programları ve röportajlar</li>
<li><b>Pzt – Cmt</b>09:00 – 20:00 · ücretsiz otopark</li>
</ul></section>'''

# ---------------------------------------------------------------- kardeş sitelere konu bağlantıları
RN = 'https://www.psikologrojinnazik.com'
EL = 'https://psikologeliferdogan.com'
SISTER = {
 '/cayyolu-cocuk-psikologu/': [(RN + '/ayrilma-kaygisi/', 'Çocuklarda ayrılma kaygısı'), (RN + '/sosyal-kaygi/', 'Sosyal kaygı'), (EL + '/hizmetler/oyun-terapisi', 'Oyun terapisi – Psikolog Elif Erdoğan'), (RN + '/ankara-cocuk-psikologu/', 'Ankara çocuk psikoloğu')],
 '/cayyolu-cift-terapisi/': [(RN + '/cift-iliski-terapisi/', 'Ankara çift terapisi – Psikolog Rojin Nazik'), (EL + '/blog/cift-terapisine-ne-zaman-basvurulmali', 'Çift terapisine ne zaman başvurulmalı?')],
 '/cayyolu-aile-terapisi/': [(RN + '/ankara-aile-terapisti/', 'Ankara aile terapisti'), (RN + '/internet-bagimliligi/', 'Ekran ve internet bağımlılığı')],
 '/ankara-psikolog-cayyolu-kizilay-umitkoy-yasamkent-incek-ve-cevresinde-guvenilir-psikolojik-destek/': [(RN + '/', 'Ankara psikolog – Psikolog Rojin Nazik'), (RN + '/kizilay-psikolog/', 'Kızılay psikolog')],
 '/cayyolu-psikolojik-danismanlik-merkezi/': [(RN + '/', 'Psikolog Rojin Nazik'), (EL + '/', 'Psikolog Elif Erdoğan')],
 '/cayyolu-psikolog-fiyatlari/': [(RN + '/ankara-psikolog-fiyatlari/', 'Ankara psikolog fiyatları 2026')],
 '/cocuklarda-kaygi-ebeveyn-rehberi/': [(RN + '/ayrilma-kaygisi/', 'Ayrılma kaygısı'), (RN + '/sosyal-kaygi/', 'Sosyal kaygı')],
 '/yurt-disi-online-ebeveyn-danismanligi/': [(RN + '/yurt-disi-online-turk-psikolog/', 'Yurt dışında Türk psikolog – Türkçe online terapi'), (EL + '/blog/yurt-disinda-online-cift-terapisi', 'Yurt dışında online çift terapisi – Psikolog Elif Erdoğan')],
 '/online-terapi/': [(RN + '/yurt-disi-online-turk-psikolog/', 'Yurt dışından Türkçe online terapi'), (RN + '/online-terapi/', 'Online terapi – Psikolog Rojin Nazik')],
 '/cocuklarda-uyku-sorunlari/': [(RN + '/ayrilma-kaygisi/', 'Ayrılma kaygısı'), (RN + '/okul-reddi/', 'Okul reddi'), (RN + '/uyku-bozukluklari/', 'Uyku bozuklukları')],
 '/cocuklarda-yas-ve-kayip/': [(RN + '/yas-terapisi/', 'Yas terapisi – Psikolog Rojin Nazik')],
 '/evlilikte-iletisim-sorunlari/': [(EL + '/blog/iliskilerde-iletisim-problemleri', 'İlişkilerde iletişim problemleri – Psikolog Elif Erdoğan'), (RN + '/cift-iliski-terapisi/', 'Ankara çift terapisi')],
 '/yalnizlik-hissi-ve-sosyal-geri-cekilme/': [(RN + '/sosyal-kaygi/', 'Sosyal kaygı'), (RN + '/depresyon-nedir/', 'Depresyon')],
 '/is-stresi-ve-tukenmislik/': [(RN + '/is-yerinde-tukenmislik-sendromu/', 'İş yerinde tükenmişlik sendromu'), (RN + '/ofke-kontrolu/', 'Öfke kontrolü')],
 '/travma-sonrasi-stres-belirtileri/': [(RN + '/travma-sonrasi-stres-bozuklugu/', 'Travma sonrası stres bozukluğu'), (RN + '/yas-terapisi/', 'Yas terapisi')],
 '/ilk-terapi-seansi-rehberi/': [(RN + '/ankara-psikolog-tavsiyesi/', 'Ankara psikolog tavsiyesi'), (RN + '/psikolog-tani-koyabilir-mi/', 'Psikolog tanı koyabilir mi?')],
 '/kaygi-sorunlari/': [(RN + '/anksiyete-bozukluklari/', 'Anksiyete bozuklukları'), (RN + '/panik-atak/', 'Panik atak'), (EL + '/blog/kaygi-mi-kaygi-bozuklugu-mu', 'Kaygı mı, kaygı bozukluğu mu?')],
 '/cocuk-ergen-danismanligi/': [(RN + '/sinav-kaygisi/', 'Sınav kaygısı'), (EL + '/hizmetler/ergen-psikoterapisi', 'Ergen psikoterapisi – Psikolog Elif Erdoğan')],
 '/umitkoy-psikolog/': [(RN + '/', 'Ankara psikolog – Psikolog Rojin Nazik')],
 '/yasamkent-psikolog/': [(RN + '/', 'Ankara psikolog – Psikolog Rojin Nazik'), (EL + '/', 'Psikolog Elif Erdoğan')],
 '/beysukent-psikolog/': [(RN + '/sinav-kaygisi/', 'Sınav kaygısı'), (RN + '/sosyal-kaygi/', 'Sosyal kaygı')],
 '/incek-psikolog/': [(RN + '/ayrilma-kaygisi/', 'Çocuklarda ayrılma kaygısı')],
}
RETITLE = {
 '/ankara-psikolog-cayyolu-kizilay-umitkoy-yasamkent-incek-ve-cevresinde-guvenilir-psikolojik-destek/': {
   'title': "Batı Ankara'da Psikolojik Destek: Çayyolu, Ümitköy, Yaşamkent ve İncek",
   'seo_title': "Batı Ankara'da Psikolojik Destek | Çayyolu, Ümitköy, Yaşamkent, İncek",
   'seo_desc': "Çayyolu, Ümitköy, Yaşamkent, Konutkent ve İncek'te yaşayanlar için RN Psikoloji Yaşamkent ofisinde yüz yüze psikolojik danışmanlık. Randevu: 0552 418 79 73."},
}
def sister_html(path):
    items = SISTER.get(path)
    if not items: return ''
    return '<aside class="route-box"><h3>İlgili kaynaklar</h3><ul>%s</ul></aside>' % ''.join(
        '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, esc(t)) for u, t in items)

# ---------------------------------------------------------------- anahtar kelime sayfaları
def landing_page(cfg):
    rec = {'type': 'page', 'path': cfg['path'], 'title': cfg['h1'], 'date': '2026-09-30', 'modified': '2026-09-30'}
    body = cfg['body'] % {'cta': inline_cta('Merhaba, %s sayfanızdan ulaşıyorum, randevu bilgisi almak istiyorum.' % cfg['h1'])}
    ex = EXTRA.get(cfg['path'])
    faqs = cfg['faqs'] + (ex['faqs'] if ex else [])
    if ex:
        rec['modified'] = '2026-10-01'
        body += ex['html']
    body += sister_html(cfg['path']) + '<h2>Sık sorulan sorular</h2>' + faq_html(faqs)
    near = [(a, p) for a, p in AREAS if p != cfg['path']]
    after = '''<section class="section section-alt"><div class="wrap">%s%s</div></section>
<section class="section"><div class="wrap office-grid">%s<div class="office-photos">%s%s</div></div></section>
%s
<section class="section section-alt"><div class="wrap">%s<div class="area-chips">%s%s</div></div></section>''' % (
        section_head('Uzmanlarımız', 'Kiminle görüşmek istersiniz?'), expert_cards(),
        office_card(), img(opt('wp-content/uploads/2024/05/seans-odasi-1.jpg', 900, 'seans-odasi'), 'RN Psikoloji seans odası'),
        img(opt('wp-content/uploads/2024/05/prev01.webp', 900, 'bekleme-alani'), 'RN Psikoloji bekleme alanı'),
        ('<section class="section"><div class="wrap">%s%s</div></section>' % (section_head('Danışan yorumları', 'Danışanlarımız ne diyor?'), reviews_html(3))) if REVIEWS else '',
        section_head('Yakın bölgeler', 'Çevre semtlerden danışanlarımız'),
        ''.join('<a class="area-chip" href="%s">%s %s psikolog</a>' % (p, ICON['pin'], esc(a)) for a, p in near),
        ''.join('<a class="area-chip" href="%s">%s Çayyolu %s</a>' % (p, ICON['arrow'], esc(t)) for p, t in FOCUS if p != cfg['path']))
    return article_page(rec, body, [('Ana Sayfa', '/'), (cfg['h1'], None)], kicker='RN Psikoloji · Yaşamkent ofisi',
                        lead=cfg['lead'], extra_after=after, extra_ld=[faq_ld(faqs), service_ld(cfg)], desc=cfg['desc'], title_tag=cfg['title'])

def service_ld(cfg):
    area = cfg['kw'].replace(' psikolog', '').replace(' Psikolog', '')
    return {'@type': 'Service', 'name': cfg['h1'], 'serviceType': 'Psikolojik danışmanlık', 'url': SITE + cfg['path'],
            'provider': {'@id': SITE + '/#isletme'},
            'areaServed': {'@type': 'Place', 'name': '%s, Ankara' % area} if 'psikolog' in cfg['kw'].lower() and len(cfg['kw'].split()) == 2 else {'@type': 'City', 'name': 'Ankara'}}

# ---------------------------------------------------------------- diğer özel sayfalar
def experts_page(rec):
    body = '<p class="page-lead">RN Psikoloji Çayyolu şubesinde çocuk, ergen, yetişkin ve çift görüşmeleri yürüten uzmanlarımız.</p>' + expert_cards()
    bc, bld = breadcrumb([('Ana Sayfa', '/'), ('Uzmanlarımız', None)])
    return head('Uzmanlarımız | %s' % BRAND, 'RN Psikoloji Çayyolu uzmanları: Psikolog Rojin Nazik, Psikolog Elif Erdoğan ve Klinik Psikolog Hazal Akşahin.', rec['path'], ld(business_ld(), bld)) + nav_html(rec['path']) + '''
<section class="page-hero"><div class="wrap">%s<h1>Uzmanlarımız</h1><div class="btn-row hero-btns">%s%s</div>%s</div></section>
<section class="section section-tight"><div class="wrap">%s</div></section>''' % (bc, btn_call(), btn_wa(), OPEN_STATUS, body) + footer_html()

def contact_page(rec):
    bc, bld = breadcrumb([('Ana Sayfa', '/'), ('İletişim', None)])
    o1 = opt('wp-content/uploads/2024/05/seans-odasi-1.jpg', 900, 'seans-odasi')
    return head('İletişim ve Randevu | %s' % BRAND, "RN Psikoloji Çayyolu iletişim: Yaşamkent ofisi, Pazartesi – Cumartesi 09:00 – 20:00. Telefon ve WhatsApp: 0552 418 79 73. Yol tarifi ve randevu.", rec['path'], ld(business_ld(), bld, faq_ld())) + nav_html(rec['path']) + '''
<section class="page-hero"><div class="wrap">%(bc)s<p class="eyebrow">İletişim ve randevu</p><h1>Bize ulaşın</h1><p class="page-lead">Randevu ve bilgi için arayın ya da WhatsApp'tan yazın. Pazartesi – Cumartesi 09:00 – 20:00.</p>
<div class="btn-row hero-btns">%(call)s%(wa)s</div>%(open)s
<p class="contact-phone"><a href="tel:%(raw)s">%(phone)s</a> · <a href="mailto:%(email)s">%(email)s</a></p></div></section>
<section class="section section-tight"><div class="wrap office-grid">%(office)s<div class="office-photos single">%(o1)s</div></div></section>
<section class="section section-alt"><div class="wrap">%(h_exp)s%(experts)s</div></section>
<section class="section"><div class="wrap narrow">%(h_faq)s%(faq)s</div></section>''' % {
        'bc': bc, 'call': btn_call(), 'wa': btn_wa(), 'open': OPEN_STATUS, 'raw': PHONE_RAW, 'phone': PHONE, 'email': EMAIL,
        'office': office_card(), 'o1': img(o1, 'RN Psikoloji Çayyolu seans odası'),
        'h_exp': section_head('Uzmanlarımız', 'Kiminle görüşmek istersiniz?'), 'experts': expert_cards(),
        'h_faq': section_head('Randevu öncesi', 'Sık sorulan sorular'), 'faq': faq_html()} + footer_html()

def press_page(rec):
    items = [('wp-content/uploads/2024/05/cnn-1.png', 'CNN Türk – İşin Uzmanı'), ('wp-content/uploads/2024/05/cnn-1.webp', 'CNN Türk'),
             ('wp-content/uploads/2024/05/cnn-2.webp', 'CNN Türk'), ('wp-content/uploads/2024/05/beyaz-tv.webp', 'Beyaz TV'),
             ('wp-content/uploads/2024/05/milliyet-1.png', 'Milliyet'), ('wp-content/uploads/2024/05/sabah-1.png', 'Sabah'),
             ('wp-content/uploads/2024/05/posta-1.png', 'Posta'), ('wp-content/uploads/2024/05/haberler.com_.png', 'Haberler.com'),
             ('wp-content/uploads/2024/05/acunn-1.png', 'Acunn'), ('wp-content/uploads/2024/05/slider-odul-1.jpg', 'Yılın En İyi Psikoloğu ödülü')]
    items += [('assets/img/basin/%s' % f, 'Gazete haberi') for f in sorted(os.listdir(os.path.join(ROOT, 'assets/img/basin')))]
    hazal = [('wp-content/uploads/2024/12/08.09.2023-Milliyet-Psi.Hazal-Aksahin-scaled-1.jpg', 'Milliyet'),
             ('wp-content/uploads/2024/12/19.11.2023-Cumhuriyet-Psi.Hazal-Aksahin-scaled-1.jpg', 'Cumhuriyet'),
             ('wp-content/uploads/2024/12/15.10.2023-Haber-Psi.Hazal-Aksahin-scaled-1.jpg', 'Haber'),
             ('wp-content/uploads/2024/12/01.10.2023-Bolge-Psi.Hazal-Aksahin-1.jpg', 'Bölge'),
             ('wp-content/uploads/2024/12/01.09.2023-Yesilpinar-Psi.Hazal-Aksahin-1-scaled-1.jpg', 'Yeşilpınar')]
    g1 = ''.join('<figure class="press-item">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 720), 'Psikolog Rojin Nazik – ' + n), esc(n)) for p, n in items)
    g2 = ''.join('<figure class="press-item">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 720), 'Klinik Psikolog Hazal Akşahin – ' + n), esc(n)) for p, n in hazal)
    body = '<h2>Psikolog Rojin Nazik</h2><p>Psikolog Rojin Nazik, CNN Türk, Beyaz TV ve ulusal gazetelerde psikoloji üzerine röportajlar veriyor; bilimsel bilgiyi toplumla buluşturmayı amaçlıyor.</p><div class="press-grid page">%s</div><h2>Klinik Psikolog Hazal Akşahin</h2><div class="press-grid page">%s</div><p>Daha fazla yayın için: <a href="https://www.psikologrojinnazik.com/basinda-biz/" target="_blank" rel="noopener">psikologrojinnazik.com/basinda-biz</a></p>' % (g1, g2)
    return article_page(dict(rec, title='Basında Biz'), body, [('Ana Sayfa', '/'), ('Basında Biz', None)], kicker='Basında RN Psikoloji',
                        lead='Psikolog Rojin Nazik ve ekibimizin televizyon ve gazete yayınları.',
                        desc='Basında RN Psikoloji: Psikolog Rojin Nazik ve Klinik Psikolog Hazal Akşahin\'in TV programları ve gazete röportajları.', title_tag='Basında Biz | %s' % BRAND)

def books_page(rec):
    books = [('wp-content/uploads/2024/05/bir-hayatla-evlenmek.webp', 'Bir Hayatla Evlenmek'), ('wp-content/uploads/2024/05/bir-odanin-otesi-500x500-1.webp', 'Bir Odanın Ötesi'),
             ('wp-content/uploads/2024/05/dengeyi-yakalamak.webp', 'Dengeyi Yakalamak')]
    soon = [('wp-content/uploads/2024/12/COK-YAKINDA.png', 'Çok yakında'), ('wp-content/uploads/2024/12/hazal.png', 'Çok yakında')]
    g = ''.join('<figure class="book big">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 520), n + ' – Psikolog Rojin Nazik'), esc(n)) for p, n in books)
    s = ''.join('<figure class="book big">%s<figcaption>%s</figcaption></figure>' % (img(opt(p, 520), n), esc(n)) for p, n in soon)
    body = '<h2>Psikolog Rojin Nazik\'in kitapları</h2><div class="books-grid">%s</div><h2>Yeni kitaplar</h2><div class="books-grid">%s</div><p>Kitaplar hakkında daha fazla bilgi: <a href="https://www.psikologrojinnazik.com/kitaplarim/" target="_blank" rel="noopener">psikologrojinnazik.com/kitaplarim</a></p>' % (g, s)
    return article_page(dict(rec, title='Kitaplarımız'), body, [('Ana Sayfa', '/'), ('Kitaplarımız', None)], kicker='Yayınlar',
                        desc='Psikolog Rojin Nazik\'in kitapları: Bir Hayatla Evlenmek, Bir Odanın Ötesi ve Dengeyi Yakalamak.', title_tag='Kitaplarımız | %s' % BRAND)

def gallery_page(rec):
    pics = ['wp-content/uploads/2024/05/seans-odasi-1.jpg', 'wp-content/uploads/2024/05/prev01.webp', 'wp-content/uploads/2024/05/meet-05.webp',
            'wp-content/uploads/2024/05/meet-06.webp', 'wp-content/uploads/2024/05/meet-07.webp', 'wp-content/uploads/2024/05/meet-08.webp',
            'wp-content/uploads/2024/05/meet-03.webp', 'assets/img/ofis-salon.webp', 'assets/img/ofis-koltuk.webp']
    g = ''.join('<figure class="gal">%s</figure>' % img(opt(p, 900), 'RN Psikoloji Çayyolu ofis') for p in pics)
    return article_page(dict(rec, title='Galeri'), '<div class="gallery">%s</div>' % g, [('Ana Sayfa', '/'), ('Galeri', None)], kicker='Ofisimiz',
                        lead='Yaşamkent ofisimizden görüntüler.', desc='RN Psikoloji Çayyolu Yaşamkent ofisinden görüntüler: seans odaları ve bekleme alanı.', title_tag='Galeri | %s' % BRAND)

def blog_index(posts, path, title='Blog'):
    bc, bld = breadcrumb([('Ana Sayfa', '/'), (title, None)])
    cards = ''.join(blog_card(p) for p in posts)
    return head('%s | %s' % (title, BRAND), 'RN Psikoloji Çayyolu blog: Çayyolu ve Ankara\'da psikolojik destek, terapi yöntemleri, ilişkiler ve çocuk gelişimi üzerine yazılar.', path, ld(business_ld(), bld)) + nav_html('/blog/') + '''
<section class="page-hero"><div class="wrap">%s<h1>%s</h1><p class="page-lead">Psikolojik destek, terapi yöntemleri, ilişkiler ve çocuk gelişimi üzerine yazılar.</p></div></section>
<section class="section section-tight"><div class="wrap"><div class="blog-grid">%s</div></div></section>''' % (bc, esc(title), cards) + footer_html()

# ---------------------------------------------------------------- ana akış
def main():
    recs = json.load(open(os.path.join(SRC, 'icerik.json'), encoding='utf-8'))
    # Başka kaynaklardan çevrilmiş eski yazılar yayından kaldırıldı; yerlerine özgün makaleler geldi
    removed = {m['eski'] for m in MAKALELER if m.get('eski')}
    recs = [r for r in recs if r['path'] not in removed]
    for m in MAKALELER:
        recs.append({'type': 'post', 'path': m['path'], 'slug': m['path'].strip('/'), 'title': m['title'], 'date': m.get('date', '2026-09-30'),
                     'modified': m.get('date', '2026-09-30'), 'html': m['html'], 'excerpt': '', 'seo_title': m['seo_title'], 'seo_desc': m['desc'],
                     'thumb': '/' + m['thumb'], 'categories': ['Blog'], 'faqs': m.get('faqs', [])})
    # 'Ankara psikolog' ana kelimesi Rojin Nazik ana sayfasına bırakıldı (yamyamlığı önlemek için)
    moved = {'/ankara-psikolog/': RN + '/',
             '/ankara-psikolog-tavsiyesi-2025-cayyolu-ve-yakin-bolgelerde-guvenilir-terapi-hizmeti/': RN + '/ankara-psikolog-tavsiyesi/',
             # 'Çayyolu psikolog' tek sayfada toplanır: yıllardır sıralanan ana sayfa (2026-10-05)
             '/cayyolu-psikolog/': '/'}
    recs = [r for r in recs if r['path'] not in moved]
    for r in recs:
        h = r.get('html') or ''
        for a, b in moved.items():
            h = h.replace('href="%s"' % a, 'href="%s"' % b).replace('href="%s%s"' % (SITE, a), 'href="%s"' % b)
        r['html'] = h
        if r['path'] in RETITLE:
            r.update(RETITLE[r['path']]); r['modified'] = '2026-10-01'
    posts = sorted([r for r in recs if r['type'] == 'post'], key=lambda r: r['date'], reverse=True)
    rojin = next(r for r in recs if r['path'] == '/psikolog-rojin-nazik/')
    special = {'/': None, '/uzmanlarimiz/': experts_page, '/iletisim/': contact_page, '/basinda-biz/': press_page,
               '/kitaplarimiz/': books_page, '/galeri/': gallery_page}
    pages = []
    for r in recs:
        p = r['path']
        if p == '/':
            write('/', home_page(recs, posts)); pages.append(('/', r.get('modified'))); continue
        if p in special:
            write(p, special[p](r)); pages.append((p, r.get('modified'))); continue
        body = clean_html(r['html'])
        expert = next((e for e in EXPERTS if e['path'] == p), None)
        boost = BOOST.get(p)
        if boost:
            body = boost['intro'] % {'cta': inline_cta()} + body + '<h2>Sık sorulan sorular</h2>' + faq_html(boost['faqs'])
            r = dict(r, title=boost['h1'])
        else:
            body = with_mid_cta(body, expert)
        crumbs = [('Ana Sayfa', '/')]
        if expert:
            crumbs.append(('Uzmanlarımız', '/uzmanlarimiz/'))
            hero = None
        elif r['type'] == 'post':
            crumbs.append(('Blog', '/blog/'))
            th = r.get('thumb')
            hero = opt(th, 1100) if th and os.path.exists(os.path.join(ROOT, th.lstrip('/'))) else None
        else:
            hero = None
        crumbs.append((r['title'], None))
        after = ''
        if expert:
            after = related_block('Diğer uzmanlarımız', expert_cards(exclude=p))
        elif r['type'] == 'post':
            others = [x for x in posts if x['path'] != p][:3]
            after = related_block('Diğer yazılar', '<div class="blog-grid">%s</div>' % ''.join(blog_card(x) for x in others))
        else:
            after = related_block('Hizmetlerimiz', service_cards())
        kicker = expert['role'] if expert else ('Blog' if r['type'] == 'post' else '')
        extra_ld = None
        body += sister_html(p)
        if r.get('faqs'):
            body += '<h2>Sık sorulan sorular</h2>' + faq_html(r['faqs'])
            extra_ld = [faq_ld(r['faqs'])]
        if boost:
            after = related_block('Çevre semtler', '<div class="area-chips">%s</div>' % ''.join('<a class="area-chip" href="%s">%s %s psikolog</a>' % (q, ICON['pin'], esc(a)) for a, q in AREAS if q != p)) + after
            write(p, article_page(r, body, crumbs, kicker='RN Psikoloji · Yaşamkent ofisi', lead=boost['lead'], extra_after=after,
                                  extra_ld=[faq_ld(boost['faqs'])], desc=boost['desc'], title_tag=boost['title']))
        else:
            write(p, article_page(r, body, crumbs, kicker=kicker, expert=expert, hero_img=hero, extra_after=after, extra_ld=extra_ld))
        pages.append((p, r.get('modified')))
    # anahtar kelime sayfaları
    for cfg in LANDINGS:
        write(cfg['path'], landing_page(cfg)); pages.append((cfg['path'], '2026-10-01' if cfg['path'] in EXTRA else '2026-09-30'))
    # Elif Erdoğan – yeni sayfa
    elif_rec = {'type': 'page', 'path': '/psikolog-elif-erdogan/', 'title': 'Psikolog Elif Erdoğan', 'date': '2026-09-30', 'modified': '2026-09-30', 'html': ELIF_BODY}
    ex = EXPERTS[1]
    write(elif_rec['path'], article_page(elif_rec, ELIF_BODY.replace('<h2>Psikolog Elif Erdoğan</h2>', '<figure class="article-hero-img">%s</figure>' % img(opt(ex['img'], 720, 'psikolog-elif-erdogan'), ex['name'])),
                                         [('Ana Sayfa', '/'), ('Uzmanlarımız', '/uzmanlarimiz/'), ('Psikolog Elif Erdoğan', None)], kicker='Psikolog', expert=ex,
                                         extra_after=related_block('Diğer uzmanlarımız', expert_cards(exclude=elif_rec['path'])),
                                         desc='Psikolog Elif Erdoğan – RN Psikoloji Çayyolu: yetişkin, ergen ve çift görüşmeleri, oyun terapisi ve psikolojik test. Yaşamkent ofisi, randevu: 0552 418 79 73.',
                                         title_tag='Psikolog Elif Erdoğan | RN Psikoloji Çayyolu'))
    pages.append((elif_rec['path'], '2026-09-30'))
    # blog listeleri
    write('/blog/', blog_index(posts, '/blog/')); pages.append(('/blog/', None))
    write('/category/blog/', blog_index(posts, '/category/blog/', 'Blog Yazıları')); pages.append(('/category/blog/', None))
    # 404
    open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8').write(
        head('Sayfa bulunamadı | %s' % BRAND, 'Aradığınız sayfa bulunamadı.', '/404.html', noindex=True) + nav_html('') +
        '<section class="page-hero"><div class="wrap"><h1>Sayfa bulunamadı</h1><p class="page-lead">Aradığınız sayfa taşınmış olabilir. Ana sayfaya dönebilir ya da bize doğrudan ulaşabilirsiniz.</p><div class="btn-row hero-btns">%s%s</div><p><a class="text-link" href="/">Ana sayfa %s</a></p></div></section>' % (btn_call(), btn_wa(), ICON['arrow']) + footer_html())
    # sitemap + robots
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p, mod in pages:
        sm.append('<url><loc>%s%s</loc>%s</url>' % (SITE, p, ('<lastmod>%s</lastmod>' % mod) if mod else ''))
    sm.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))
    open(os.path.join(ROOT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /_kaynak/\n\nSitemap: %s/sitemap.xml\n' % SITE)
    # sosyal paylaşım görseli
    opt('wp-content/uploads/2024/05/seans-odasi-1.jpg', 1200, 'og')
    print('sayfa:', len(pages))

if __name__ == '__main__':
    main()
