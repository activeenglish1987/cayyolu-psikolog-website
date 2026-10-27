#!/usr/bin/env python3
"""Yayın öncesi SEO kontrolü (üç sitede aynı dosya).

Kullanım:  python3 seo_kontrol.py <site-kökü> <rojin|cayyolu|elif>
Çıkış kodu 0 = temiz, 1 = HATA var (yayınlama). UYARI'lar yayını durdurmaz.

Kontroller (yalnız Google'a açık sayfalar):
- Her ana kelimenin tek sahibi var: başka sayfanın başlığı/H1'i o kelimeyi taşımaz (izinli istisnalar aşağıda).
- Sayfada tek H1 (Elif'te şablon {{ }} başlıkları sayılmaz).
- <title> var; başlık/H1/açıklamada "en iyi", "garanti", "mucize", "kesin çözüm" yok.
- Hazal Akşahin adı hiçbir sayfada geçmez.
- Asıl adres (canonical) sayfanın kendisi ya da (testlerde) Rojin sitesi.
- Site haritasındaki her adresin dosyası var ve hiçbiri noindex değil.
"""
import glob, html, os, re, sys

KOK, SITE = sys.argv[1], sys.argv[2]
ALAN = {'rojin': 'https://www.psikologrojinnazik.com', 'cayyolu': 'https://www.cayyolupsikolog.com.tr',
        'elif': 'https://psikologeliferdogan.com'}[SITE]
ROJIN = 'https://www.psikologrojinnazik.com'

# kelime -> (sahibi, başlığında geçmesine izin verilen diğer sayfalar)
SAHIP = {
    'rojin': {
        'ankara psikolog': ('/', ['/ankara-psikolog-fiyatlari/', '/ankara-psikolog-tavsiyesi/']),
        'ankara cocuk psikolog': ('/ankara-cocuk-psikologu/', []),
        'ankara ergen psikolog': ('/ankara-ergen-psikologu/', []),
        'ankara yetiskin psikolog': ('/ankara-yetiskin-psikologu/', []),
        'ankara aile terapi': ('/ankara-aile-terapisti/', []),
        'kizilay psikolog': ('/kizilay-psikolog/', []),
        'cankaya psikolog': ('/ankara-cankaya-psikolog/', []),
        'psikolog fiyat': ('/ankara-psikolog-fiyatlari/', []),
    },
    'cayyolu': {
        'cayyolu psikolog': ('/', ['/cayyolu-psikolog-fiyatlari/']),
        'yasamkent psikolog': ('/yasamkent-psikolog/', []),
        'umitkoy psikolog': ('/umitkoy-psikolog/', []),
        'konutkent psikolog': ('/konutkent-psikolog/', []),
        'cayyolu cocuk psikolog': ('/cayyolu-cocuk-psikologu/', []),
        'cayyolu cift terapi': ('/cayyolu-cift-terapisi/', []),
        'cayyolu aile terapi': ('/cayyolu-aile-terapisi/', []),
        'incek psikolog': ('/incek-psikolog/', []),
        'beysukent psikolog': ('/beysukent-psikolog/', []),
        'bilkent psikolog': ('/bilkent-psikolog/', []),
        'alacaatli psikolog': ('/alacaatli-psikolog/', []),
        'eryaman psikolog': ('/eryaman-psikolog/', []),
        'ankara psikolog': (None, []),  # Rojin'in kelimesi: Çayyolu'da hiçbir sayfa başlığında olmaz
    },
    'elif': {
        'ankara psikolog': (None, []),  # Rojin'in kelimesi
        'ankara ergen psikolog': (None, []),  # Rojin'in kelimeleri: Elif'te başlık/H1'de olmaz
        'ankara yetiskin psikolog': (None, []),
        'ankara cocuk psikolog': (None, []),
        'ankara aile terapi': (None, []),
        'kizilay psikolog': (None, []),
        'cayyolu psikolog': (None, []),  # Çayyolu sitesinin kelimesi
        'ankara oyun terapi': ('/hizmetler/oyun-terapisi/', []),
        'mmpi': ('/blog/mmpi-testi-nedir/', ['/hizmetler/psikolojik-test-degerlendirme/']),
    },
}[SITE]
YASAK = re.compile(r'\ben iyi\b|garanti|mucize|kesin çözüm|kesin sonuç', re.I)

def kucuk(t):
    t = html.unescape(t).replace('İ', 'i').replace('I', 'ı').lower()
    for a, b in zip('ığüşöç', 'igusoc'): t = t.replace(a, b)
    return re.sub(r"[’'`]", "'", re.sub(r'\s+', ' ', t))

def dosyalar():
    if SITE == 'elif':
        harita = {'home': '/', 'blog': '/blog/', 'hakkimizda': '/hakkimizda/', 'iletisim': '/iletisim/'}
        for f in glob.glob(os.path.join(KOK, '_ssr', '*.html')):
            ad = os.path.basename(f)[:-5]
            yol = harita.get(ad) or ('/' + ad.replace('--', '/') + '/')
            yield yol, f
        for f in glob.glob(os.path.join(KOK, '*', 'index.html')):
            yield '/' + os.path.relpath(os.path.dirname(f), KOK) + '/', f
        return
    for f in glob.glob(os.path.join(KOK, '**', 'index.html'), recursive=True):
        r = os.path.relpath(f, KOK)
        if r.startswith(('_', 'wp-content', 'node_modules', 'assets', '.')): continue
        yield ('/' if r == 'index.html' else '/' + os.path.dirname(r) + '/'), f

# İnce içerik / gelen bağlantı kontrolünden muaf: araç, yasal ve vitrin sayfaları (Rojin)
INCE_IZINLI = {'/', '/de/', '/kaygi-testi/', '/depresyon-testi/', '/galeri/', '/sertifikalar/', '/ekibimiz/', '/basinda-biz/',
               '/iletisim/', '/kitaplarim/', '/tv-programlarim/', '/hizmetlerimiz/', '/gizlilik/', '/cerez-politikasi/', '/kvkk/',
               '/cinsel-islev-bozukluklari/', '/pdr-taban-puanlari/', '/psikoloji-taban-puanlari/', '/turk-psikologlar-dernegi-akreditasyon/'} if SITE == 'rojin' else \
    {'/', '/kaygi-testi/', '/depresyon-testi/', '/galeri/', '/basinda-biz/', '/iletisim/', '/kitaplarimiz/', '/konferanslar/', '/uzmanlarimiz/',
     '/hakkimizda/', '/gizlilik/', '/kvkk/', '/onerilenler/', '/blog/', '/psikolog-rojin-nazik/', '/psikolog-elif-erdogan/'} if SITE == 'cayyolu' else \
    {'/', '/hakkimizda/', '/iletisim/', '/kaygi-testi/', '/depresyon-testi/', '/kvkk/', '/blog/'} if SITE == 'elif' else set()
hata, uyari, sayfa = [], [], {}
for yol, f in dosyalar():
    s = open(f, encoding='utf-8', errors='ignore').read()
    g = lambda r: (re.search(r, s, re.S | re.I) or [None, ''])[1] if re.search(r, s, re.S | re.I) else ''
    robots = g(r'<meta name="robots" content="([^"]+)"')
    if 'noindex' in robots.lower(): sayfa[yol] = None; continue
    title = html.unescape(g(r'<title>(.*?)</title>')).strip()
    # Elif: arama motoruna giden metin #seo-ssr bloğunda; arkasındaki uygulama şablonu sayfaya göre tek başlık çizer
    alan = s
    if SITE == 'elif' and 'id="seo-ssr"' in s:
        alan = s[s.index('id="seo-ssr"'):]; alan = alan[:alan.index('</main>')]
    h1ler = [re.sub(r'<[^>]+>', '', h).strip() for h in re.findall(r'<h1[^>]*>(.*?)</h1>', alan, re.S)]
    h1ler = [h for h in h1ler if '{{' not in h]
    desc = html.unescape(g(r'<meta name="description" content="([^"]*)"'))
    can = g(r'<link rel="canonical" href="([^"]+)"')
    sayfa[yol] = dict(title=title, h1=h1ler, can=can)
    if not title: hata.append('%s: <title> yok' % yol)
    if len(h1ler) != 1: hata.append('%s: %d adet H1 %s' % (yol, len(h1ler), h1ler[:3]))
    for ad, metin in (('başlık', title), ('H1', ' '.join(h1ler)), ('açıklama', desc)):
        m = YASAK.search(metin)
        if m: hata.append('%s: %s içinde yasak ifade "%s"' % (yol, ad, m.group(0)))
    if re.search(r'hazal|akşahin|aksahin', re.sub(r'<script.*?</script>', '', s, flags=re.S), re.I):
        hata.append('%s: Hazal Akşahin adı geçiyor' % yol)
    if can and can.rstrip('/') != (ALAN + yol).rstrip('/') and not can.startswith(ROJIN):
        hata.append('%s: canonical başka adresi gösteriyor: %s' % (yol, can))
    if len(title) > 70: uyari.append('%s: başlık %d karakter (Google keser)' % (yol, len(title)))
    # içerik derinliği, açıklama uzunluğu ve gelen bağlantı (27 Ekim denetiminden sonra eklendi)
    if desc and not 100 <= len(desc) <= 165: uyari.append('%s: açıklama %d karakter (100–165 olmalı)' % (yol, len(desc)))
    makale = re.search(r'<article.*?</article>', alan, re.S) or (re.search(r'.+', alan, re.S) if SITE == 'elif' and alan is not s else None)
    if makale and yol not in INCE_IZINLI:
        govde = re.sub(r'<nav class="rn-ilgili".*?</nav>|<aside.*?</aside>|<script.*?</script>|<style.*?</style>', '', makale.group(0), flags=re.S)
        kelime = len(re.sub(r'<[^>]+>', ' ', govde).split())
        if kelime < 600: uyari.append('%s: içerik ince (%d kelime; en az 600)' % (yol, kelime))
    sayfa[yol]['linkler'] = {l if l.endswith('/') or '.' in l.rsplit('/', 1)[-1] else l + '/' for l in re.findall(r'href="(?:' + re.escape(ALAN) + r')?(/[^"#?]*)"', s)}

for kel, (sahip, izinli) in SAHIP.items():
    rakip = [y for y, d in sayfa.items() if d and y != sahip and y not in izinli
             and (kel in kucuk(d['title']) or any(kel in kucuk(h) for h in d['h1']))]
    for y in rakip: hata.append('%s: "%s" kelimesi %s sayfasının; bu sayfanın başlığında/H1\'inde olmamalı' % (y, kel, sahip or 'Rojin sitesi'))
    if sahip and sayfa.get(sahip) and kel not in kucuk(sayfa[sahip]['title']):
        uyari.append('%s: sahibi olduğu "%s" kelimesi başlıkta yok' % (sahip, kel))

gelen = {}
for y, v in sayfa.items():
    for l in (v or {}).get('linkler', ()):
        if l != y: gelen[l] = gelen.get(l, 0) + 1
for y, v in sayfa.items():
    if v and y != '/' and y not in INCE_IZINLI and gelen.get(y, 0) < 2:
        uyari.append('%s: yalnızca %d sayfadan bağlantı alıyor (en az 2)' % (y, gelen.get(y, 0)))

sm = os.path.join(KOK, 'sitemap.xml')
if os.path.exists(sm):
    for loc in re.findall(r'<loc>([^<]+)</loc>', open(sm, encoding='utf-8').read()):
        yol = loc.replace(ALAN, '') or '/'
        if not yol.endswith('/') and '.' not in yol.rsplit('/', 1)[-1]: yol += '/'
        if yol.endswith('.html') or yol.endswith('.xml'): continue
        if yol not in sayfa: hata.append('site haritası: %s için sayfa yok' % yol)
        elif sayfa[yol] is None: hata.append('site haritası: %s noindex ama haritada' % yol)

for u in uyari: print('UYARI  ', u)
for h in hata: print('HATA   ', h)
print('%s: %d sayfa, %d hata, %d uyarı' % (SITE, len([v for v in sayfa.values() if v]), len(hata), len(uyari)))
sys.exit(1 if hata else 0)
