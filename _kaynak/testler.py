# -*- coding: utf-8 -*-
"""Kendini değerlendirme testleri: /kaygi-testi/ (GAD-7) ve /depresyon-testi/ (PHQ-9).

- Puanlama ziyaretçinin tarayıcısında yapılır; cevaplar hiçbir yere gönderilmez, kaydedilmez.
- Sonuç tanı değildir; her sonuçta uzmanla görüşme daveti ve Selda Hanım'ı arama düğmesi var.
- PHQ-9'un 9. sorusuna (kendine zarar verme düşüncesi) 0 dışında cevap verilirse, puandan bağımsız
  olarak sonucun en üstünde 112 / acil destek kutusu gösterilir.
- Sayfa iskeleti (üst menü, alt bilgi, stiller) sitenin mevcut bir sayfasından alınır, böylece
  site tasarımıyla birebir aynı görünür.
- Rojin'de dizine açık (--yayinla) ve site haritasında; kelimenin sahibi Rojin.
- Çayyolu (_kaynak/build.py) ve Elif (--elif <klasör>) kopyaları kendi renkleriyle çalışır,
  asıl adresleri (canonical) Rojin'deki sayfadır: siteler aynı kelimede yarışmaz.

Çalıştır: python3 _araclar/testler.py --yayinla
"""
import html, json, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.psikologrojinnazik.com'
SABLON = 'ankara-psikolog-randevusu-nasil-alinir/index.html'
esc = lambda x: html.escape(x or '', quote=True)
YAYINLA = '--yayinla' in sys.argv

SECENEK = ['Hiç', 'Birkaç gün', 'Günlerin yarısından fazlası', 'Neredeyse her gün']

TESTLER = [
    {
        'yol': '/kaygi-testi/', 'ad': 'Kaygı Testi', 'olcek': 'GAD-7',
        'title': 'Kaygı Testi (GAD-7): 2 Dakikada Kaygı Düzeyinizi Görün | Psikolog Rojin Nazik',
        'desc': 'Uluslararası kullanılan GAD-7 ölçeğine dayanan 7 soruluk kısa kaygı testi. Cevaplarınız kaydedilmez; sonuç tanı değildir. Ankara’da psikolojik destek için Psikolog Rojin Nazik.',
        'h1': 'Kaygı Testi (GAD-7)',
        'lead': 'Son iki haftada kaygıyla ilgili belirtileri ne sıklıkta yaşadığınızı 7 kısa soruyla görün. Cevaplarınız hiçbir yere gönderilmez ve kaydedilmez; sonuç bir tanı değildir.',
        'soru_basi': 'Son 2 hafta içinde aşağıdaki sorunlar sizi ne sıklıkla rahatsız etti?',
        'sorular': [
            'Sinirli, kaygılı ya da gergin hissetmek',
            'Endişelenmeyi durduramamak ya da kontrol edememek',
            'Farklı şeyler hakkında çok fazla endişelenmek',
            'Rahatlamakta zorlanmak',
            'Yerinde duramayacak kadar huzursuz olmak',
            'Kolayca sinirlenmek ya da huysuzlaşmak',
            'Kötü bir şey olacakmış gibi korkmak',
        ],
        'bantlar': [(0, 4, 'düşük', 'Belirtileriniz şu an düşük düzeyde görünüyor.'),
                    (5, 9, 'hafif', 'Hafif düzeyde kaygı belirtileri yaşıyor olabilirsiniz.'),
                    (10, 14, 'orta', 'Orta düzeyde kaygı belirtileri yaşıyor olabilirsiniz.'),
                    (15, 21, 'yüksek', 'Yüksek düzeyde kaygı belirtileri yaşıyor olabilirsiniz.')],
        'kaynak': 'GAD-7: Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing generalized anxiety disorder. Archives of Internal Medicine, 2006.',
        'not': ('Kaygıda en sık gördüğüm yanlış inanç', 'Kaygı yaşayan danışanlarda sık gördüğüm düşüncelerden biri, ‘Bu duyguyu hiç yaşamamalıyım’ beklentisi. Bazen sorun yalnızca kaygının kendisi değil, kişinin kaygı yaşamaktan korkması haline geliyor.'),
        'ilgili': [('/anksiyete-bozukluklari/', 'Kaygı (anksiyete) bozuklukları'), ('/panik-atak/', 'Panik atak'), ('/sosyal-kaygi/', 'Sosyal kaygı'), ('/asiri-dusunme/', 'Aşırı düşünme')],
        'bilgi': [
            ('Bu test neyi ölçer?', 'GAD-7, dünyada birinci basamak sağlık hizmetlerinde ve araştırmalarda yaygın olarak kullanılan, son iki haftadaki kaygı belirtilerinin sıklığını soran 7 soruluk kısa bir tarama ölçeğidir. Bir tanı aracı değildir; belirtilerin yoğunluğu hakkında genel bir fikir verir.'),
            ('Sonucum yüksek çıktı, ne yapmalıyım?', 'Yüksek bir puan, yaşadıklarınızı bir uzmanla konuşmanın faydalı olabileceğini gösterir. İlk görüşmede ne yaşadığınız, ne zamandır sürdüğü ve günlük hayatınızı nasıl etkilediği konuşulur; çalışma planı birlikte oluşturulur.'),
            ('Sonucum düşük çıktı; yine de görüşebilir miyim?', 'Elbette. Test yalnızca son iki haftaya bakar ve her zorluğu yakalamaz. Sizi zorlayan bir durum varsa konuşmak için yüksek bir puan gerekmez.'),
            ('Psikolog tanı koyar ya da ilaç yazar mı?', 'Hayır. Psikologlar tanı koymaz ve ilaç yazmaz. İlaç değerlendirmesi gerekebilecek durumlarda psikiyatri uzmanına yönlendirme yapılır.'),
        ],
    },
    {
        'yol': '/depresyon-testi/', 'ad': 'Depresyon Testi', 'olcek': 'PHQ-9',
        'title': 'Depresyon Testi (PHQ-9): 9 Soruda Ruh Halinizi Değerlendirin | Psikolog Rojin Nazik',
        'desc': 'Uluslararası kullanılan PHQ-9 ölçeğine dayanan 9 soruluk kısa depresyon testi. Cevaplarınız kaydedilmez; sonuç tanı değildir. Ankara’da psikolojik destek için Psikolog Rojin Nazik.',
        'h1': 'Depresyon Testi (PHQ-9)',
        'lead': 'Son iki haftada ruh halinizle ilgili belirtileri ne sıklıkta yaşadığınızı 9 kısa soruyla görün. Cevaplarınız hiçbir yere gönderilmez ve kaydedilmez; sonuç bir tanı değildir.',
        'soru_basi': 'Son 2 hafta içinde aşağıdaki sorunlar sizi ne sıklıkla rahatsız etti?',
        'sorular': [
            'Bir şeyler yapmaya karşı ilgi ya da istek duymamak',
            'Kendini çökkün, mutsuz ya da umutsuz hissetmek',
            'Uykuya dalmakta ya da uykuyu sürdürmekte zorlanmak veya çok fazla uyumak',
            'Yorgun ya da enerjisiz hissetmek',
            'İştahsızlık ya da aşırı yemek',
            'Kendini kötü hissetmek; başarısız olduğunu ya da kendini veya aileni hayal kırıklığına uğrattığını düşünmek',
            'Gazete okumak ya da televizyon izlemek gibi şeylere odaklanmakta zorlanmak',
            'Başkalarının fark edebileceği kadar yavaş hareket etmek ya da konuşmak; ya da tam tersi, her zamankinden çok daha huzursuz ve kıpır kıpır olmak',
            'Ölmüş olmanın daha iyi olacağını düşünmek ya da kendine bir şekilde zarar verme düşünceleri',
        ],
        'kriz_soru': 8,  # 0'dan sayılır: 9. soru
        'bantlar': [(0, 4, 'düşük', 'Belirtileriniz şu an düşük düzeyde görünüyor.'),
                    (5, 9, 'hafif', 'Hafif düzeyde depresif belirtiler yaşıyor olabilirsiniz.'),
                    (10, 14, 'orta', 'Orta düzeyde depresif belirtiler yaşıyor olabilirsiniz.'),
                    (15, 19, 'orta-yüksek', 'Orta-yüksek düzeyde depresif belirtiler yaşıyor olabilirsiniz.'),
                    (20, 27, 'yüksek', 'Yüksek düzeyde depresif belirtiler yaşıyor olabilirsiniz.')],
        'kaynak': 'PHQ-9: Kroenke K, Spitzer RL, Williams JBW. The PHQ-9: validity of a brief depression severity measure. Journal of General Internal Medicine, 2001.',
        'not': ('İyi ilerleyen bir süreçte ilk fark ettiğim değişiklik', 'Değişim her zaman kişinin ‘artık hiç üzülmüyorum’ demesiyle başlamıyor. Bazen ilk önemli değişiklik, kişinin eskiden otomatik biçimde verdiği tepkiyi fark edip ‘Ben yine aynı şeyi yapıyorum’ diyebilmesi oluyor.'),
        'ilgili': [('/depresyon-nedir/', 'Depresyon nedir?'), ('/yas-terapisi/', 'Yas ve kayıp'), ('/bireysel-danismanlik/', 'Bireysel danışmanlık'), ('/psikolog-ve-psikiyatri-farki/', 'Psikolog ve psikiyatrist farkı')],
        'bilgi': [
            ('Bu test neyi ölçer?', 'PHQ-9, dünyada birinci basamak sağlık hizmetlerinde ve araştırmalarda yaygın olarak kullanılan, son iki haftadaki depresif belirtilerin sıklığını soran 9 soruluk kısa bir tarama ölçeğidir. Bir tanı aracı değildir; belirtilerin yoğunluğu hakkında genel bir fikir verir.'),
            ('Sonucum yüksek çıktı, ne yapmalıyım?', 'Yüksek bir puan, yaşadıklarınızı bir uzmanla konuşmanın faydalı olabileceğini gösterir. İlaç değerlendirmesi gerekebilecek durumlarda psikiyatri uzmanına yönlendirme yapılır; psikolojik destek bu süreçle birlikte yürütülebilir.'),
            ('Kendime zarar verme düşüncelerim var.', 'Bu düşünceler acil destek gerektirebilir. Lütfen hemen 112’yi arayın ya da en yakın acil servise başvurun; yanınızda güvendiğiniz birinin olmasını isteyin.'),
            ('Psikolog tanı koyar ya da ilaç yazar mı?', 'Hayır. Psikologlar tanı koymaz ve ilaç yazmaz. İlaç değerlendirmesi gerekebilecek durumlarda psikiyatri uzmanına yönlendirme yapılır.'),
        ],
    },
]


def form_html(T):
    satirlar = []
    for i, q in enumerate(T['sorular']):
        secs = ''.join('<label><input type="radio" name="s%d" value="%d" required><span>%s</span></label>' % (i, v, esc(t)) for v, t in enumerate(SECENEK))
        satirlar.append('<fieldset class="ts-q"><legend><b>%d.</b> %s</legend><div class="ts-o">%s</div></fieldset>' % (i + 1, esc(q), secs))
    return '<form class="ts-form" id="ts-form" novalidate><p class="ts-basi">%s</p>%s<div class="ts-err" aria-live="polite"></div><button type="submit" class="btn btn-primary ts-btn">Sonucumu göster</button><p class="ts-gizli">🔒 Cevaplarınız yalnızca bu cihazda değerlendirilir; hiçbir yere gönderilmez ve kaydedilmez.</p></form><div id="ts-sonuc" class="ts-sonuc" hidden></div>' % (esc(T['soru_basi']), ''.join(satirlar))


TS_CSS = '''<style>
.ts-form{margin:8px 0 18px}.ts-basi{font-weight:700;margin:0 0 12px}
.ts-q{border:1px solid #E8DFD0;border-radius:16px;padding:14px 16px;margin:0 0 12px;background:#fff}
.ts-q legend{padding:0 4px;font-weight:600;line-height:1.5}
.ts-o{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin-top:10px}
@media(min-width:760px){.ts-o{grid-template-columns:repeat(4,1fr)}}
.ts-o label{display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:12px;border:1.5px solid #E8DFD0;cursor:pointer;font-size:14.5px;line-height:1.3;background:#FBF8F2}
.ts-o input{accent-color:#6B3A8C;width:18px;height:18px;flex:none}
.ts-o label:has(input:checked){border-color:#6B3A8C;background:#F4EEF8}
.ts-btn{width:100%;max-width:420px;justify-content:center}
.ts-err{color:#B42318;font-weight:600;min-height:1px;margin:4px 0 10px}
.ts-gizli{font-size:13px;color:#6b5f73;margin-top:10px}
.ts-sonuc{border-radius:20px;padding:22px;background:#F4EEF8;border:1px solid #E2D6EC;margin:10px 0 24px}
.ts-sonuc h2{margin-top:0}.ts-puan{font-size:42px;font-weight:800;color:#3d1e54;line-height:1}
.ts-bar{height:10px;border-radius:9px;background:#E8DFD0;overflow:hidden;margin:12px 0}.ts-bar i{display:block;height:100%;background:linear-gradient(90deg,#16A34A,#E5A50A,#C62828)}
.ts-kriz{border-radius:16px;padding:16px;background:#FFF1F0;border:2px solid #C62828;margin:0 0 16px;color:#7A1C17}
.ts-kriz b{display:block;font-size:18px;margin-bottom:6px}
.ts-ara{display:flex;align-items:center;justify-content:center;gap:8px;max-width:420px;padding:16px;border-radius:14px;background:#16A34A;color:#fff!important;font-weight:800;font-size:17px;text-decoration:none;margin:14px 0 8px}
.ts-not{font-size:13px;color:#6b5f73}
</style>'''


def betik(T):
    veri = {'bantlar': [[a, b, c, d] for a, b, c, d in T['bantlar']], 'n': len(T['sorular']), 'kriz': T.get('kriz_soru', -1), 'olcek': T['olcek'], 'ad': T['ad']}
    return '''<script>(function(){var V=%s;var f=document.getElementById('ts-form'),out=document.getElementById('ts-sonuc');
f.addEventListener('submit',function(e){e.preventDefault();var t=0,kriz=false,eksik=0;
for(var i=0;i<V.n;i++){var c=f.querySelector('input[name="s'+i+'"]:checked');if(!c){eksik++;continue}var v=+c.value;t+=v;if(i===V.kriz&&v>0)kriz=true}
if(eksik){f.querySelector('.ts-err').textContent='Lütfen tüm soruları cevaplayın ('+eksik+' soru kaldı).';var ilk=f.querySelector('fieldset:not(:has(input:checked))');if(ilk)ilk.scrollIntoView({behavior:'smooth',block:'center'});return}
f.querySelector('.ts-err').textContent='';var max=V.n*3,b=V.bantlar[0];for(var j=0;j<V.bantlar.length;j++)if(t>=V.bantlar[j][0]&&t<=V.bantlar[j][1])b=V.bantlar[j];
var dusuk=b[2]==='düşük';var h='';
if(kriz)h+='<div class="ts-kriz" role="alert"><b>Kendinize zarar verme düşünceleri acil destek gerektirebilir.</b>Lütfen hemen <a href="#" data-112>112\\'yi arayın</a> ya da en yakın acil servise başvurun. Yanınızda güvendiğiniz birinin olmasını isteyin.</div>';
h+='<h2>'+V.ad+' sonucunuz</h2><div class="ts-puan">'+t+' <small style="font-size:18px;color:#6b5f73">/ '+max+'</small></div><div class="ts-bar"><i style="width:'+Math.round(t/max*100)+'%%"></i></div>';
h+='<p><b>'+b[3]+'</b> Bu sonuç bir tanı değildir; son iki haftadaki belirtilerinizin yoğunluğu hakkında genel bir fikir verir.</p>';
h+='<p>'+(dusuk?'Sizi zorlayan bir durum varsa bunu konuşmak için yüksek bir puan gerekmez.':'Bu belirtiler günlük hayatınızı etkiliyorsa bir uzmanla konuşmak faydalı olabilir. İlk görüşmede ne yaşadığınız ve sizi nasıl etkilediği konuşulur, çalışma planı birlikte oluşturulur.')+'</p>';
h+='<a class="ts-ara" href="tel:+905524187973" data-cta-area="test_sonuc">📞 Selda Hanım\\'ı Arayın · 0552 418 79 73</a><p class="ts-not">Telefonu Selda Hanım açar; uygun saati ve ücret bilgisini söyler. Pazartesi–Cumartesi 09:00–20:00.</p>';
out.innerHTML=h;out.hidden=false;var k=out.querySelector('[data-112]');if(k)k.onclick=function(ev){ev.preventDefault();location.href='tel:112'};
out.scrollIntoView({behavior:'smooth',block:'start'});
(window.dataLayer=window.dataLayer||[]).push({event:'test_tamamlandi',test:V.olcek,test_duzey:b[2]});});
})();</script>''' % json.dumps(veri, ensure_ascii=False)


def ld(T):
    faq = {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in T['bilgi']]}
    page = {'@type': 'WebPage', '@id': SITE + T['yol'] + '#webpage', 'url': SITE + T['yol'], 'name': T['h1'], 'description': T['desc'], 'inLanguage': 'tr-TR',
            'author': {'@type': 'Person', 'name': 'Rojin Nazik', 'url': SITE + '/rojin-nazik-biyografi/'}}
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Ana sayfa', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': T['h1'], 'item': SITE + T['yol']}]}
    return '<script type="application/ld+json">%s</script>' % json.dumps({'@context': 'https://schema.org', '@graph': [page, faq, crumbs]}, ensure_ascii=False)


def main_html(T):
    bilgi = ''.join('<h2>%s</h2><p>%s</p>' % (esc(q), esc(a)) for q, a in T['bilgi'])
    ilgili = ' · '.join('<a href="%s">%s</a>' % (y, esc(t)) for y, t in T['ilgili'] if os.path.exists(os.path.join(KOK, y.strip('/'), 'index.html')))
    diger = [x for x in TESTLER if x['yol'] != T['yol']]
    diger_html = ''.join(' · <a href="%s">%s</a>' % (x['yol'], esc(x['ad'])) for x in diger)
    return ('<main><section class="page-hero"><div class="container-wide"><div class="breadcrumb"><a href="/">Ana sayfa</a> / %(h1)s</div>'
            '<div class="badge">Psikolog Rojin Nazik · Ankara</div><h1 style="margin-top:18px">%(h1)s</h1><p class="lead">%(lead)s</p>'
            '<div class="hero-actions"><a class="btn btn-primary btn-call" href="#ts-form">Teste başla ↓</a><a class="btn btn-wa-soft" href="tel:+905524187973">📞 0552 418 79 73</a></div></div></section>'
            '<section class="section-padding-sm"><div class="container-wide article-wrap"><article class="article">'
            '<p class="rn-byline" style="font-size:14px;color:#6b5f73;margin:0 0 18px">Hazırlayan: <a href="/rojin-nazik-biyografi/">Psikolog Rojin Nazik</a> · Ölçek: %(olcek)s</p>'
            '%(form)s'
            '<aside class="rn-note" style="margin:26px 0;padding:18px 20px;border-radius:16px;background:#FBF8F2;border-left:4px solid #6B3A8C"><p style="margin:0 0 8px;font-weight:700;color:#3d1e54">Psikolog Rojin Nazik\'in notu · %(notb)s</p><blockquote style="margin:0;font-style:italic;line-height:1.7">“%(not)s”</blockquote></aside>'
            '%(bilgi)s<p class="ts-not" style="margin-top:22px">İlgili sayfalar: %(ilgili)s%(diger)s</p>'
            '<p class="ts-not">Kaynak: %(kaynak)s Ölçek serbestçe kullanılabilir; buradaki Türkçe ifadeler bilgilendirme amaçlıdır. Bu test tanı koymaz. Acil bir durumda 112\'yi arayın.</p>'
            '</article></div></section></main>') % {
        'h1': esc(T['h1']), 'lead': esc(T['lead']), 'olcek': esc(T['olcek']), 'form': form_html(T), 'not': esc(T['not'][1]), 'notb': esc(T['not'][0]),
        'bilgi': bilgi, 'ilgili': ilgili, 'diger': diger_html, 'kaynak': esc(T['kaynak'])}


def sayfa(sablon, T):
    s = sablon
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(T['title']), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % esc(T['desc']), s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s%s">' % (SITE, T['yol']), s, count=1)
    robots = 'index, follow, max-image-preview:large' if YAYINLA else 'noindex, follow'
    s = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="%s">' % robots, s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % esc(T['title']), s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % esc(T['desc']), s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s%s">' % (SITE, T['yol']), s, count=1)
    s = re.sub(r'<script type="application/ld\+json"[^>]*>.*?</script>', '', s, flags=re.S)
    s = s.replace('</head>', ld(T) + TS_CSS + '</head>', 1)
    a, b = s.find('<main'), s.find('</main>') + len('</main>')
    s = s[:a] + main_html(T) + betik(T) + s[b:]
    return s


def site_haritasi(ekle):
    p = os.path.join(KOK, 'sitemap.xml')
    sm = open(p, encoding='utf-8').read()
    for T in TESTLER:
        loc = SITE + T['yol']
        if ekle and loc not in sm:
            sm = sm.replace('</urlset>', '<url><loc>%s</loc><lastmod>2026-10-10</lastmod></url>\n</urlset>' % loc)
    open(p, 'w', encoding='utf-8').write(sm)


# ---------------------------------------------------------------- Çayyolu ve Elif: bağımsız sayfa
# Aynı test üç sitede dizine girerse siteler "kaygı testi" kelimesinde birbiriyle yarışır.
# Bu yüzden Çayyolu ve Elif'teki kopyaların asıl adresi (canonical) Rojin'deki sayfadır.
TEMALAR = {
    'cayyolu': {'marka': 'RN Psikoloji Çayyolu', 'ana': '/', 'a': '#14264A', 'a2': '#14264A', 'acik': '#EEF3FA', 'cizgi': '#DCE4F0', 'zemin': '#F2F6FB', 'mut': '#566179',
                'logo': '<span style="display:inline-flex;align-items:center;gap:10px;font-weight:700;color:#14264A"><span style="width:38px;height:38px;border-radius:10px;background:#14264A;color:#fff;display:grid;place-items:center;font-size:15px">RN</span><span style="line-height:1.15">RN Psikoloji<small style="display:block;font-weight:500;font-size:12px;color:#566179">Çayyolu Şubesi</small></span></span>',
                'betikler': "<script src=\"/assets/js/ads-conversion.js?v=5\" defer></script><script src=\"/assets/js/after-hours.js?v=2\" data-pos=\"bottom\" defer></script><script>window.PUSULA_CFG={site:'cayyolu',foto:'/assets/img/opt/psikolog-rojin-nazik-720.webp'};</script><script src=\"/assets/js/pusula.js?v=6\" defer></script>",
                'ikon': '<link rel="icon" href="/favicon.svg" type="image/svg+xml">', 'not_sahibi': 'Psikolog Rojin Nazik'},
    'elif': {'marka': 'Psikolog Elif Erdoğan', 'ana': '/', 'a': '#0e9e79', 'a2': '#062b20', 'acik': '#E7F8F1', 'cizgi': '#D5EDE3', 'zemin': '#F3FBF7', 'mut': '#4b635a',
             'logo': '<img src="/assets/elif-logo.webp" alt="Psikolog Elif Erdoğan" height="34" style="height:34px;width:auto">',
             'betikler': "<script>window.ADS_CONV_CFG={spa:false};</script><script src=\"/ads-conversion.js?v=5\" defer></script><script src=\"/after-hours.js?v=3\" data-pos=\"bottom\" defer></script><script>window.PUSULA_CFG={site:'elif'};</script><script src=\"/pusula.js?v=6\" defer></script>",
             'ikon': '<link rel="icon" href="/favicon.ico">', 'not_sahibi': None},
}
GTM_HEAD = """<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KMR7XRJQ');</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11469933181"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','AW-11469933181',{url_passthrough:true});</script>"""


def bagimsiz(T, ad):
    M = TEMALAR[ad]
    css = TS_CSS.replace('#6B3A8C', M['a']).replace('#3d1e54', M['a2']).replace('#F4EEF8', M['acik']).replace('#E2D6EC', M['cizgi']).replace('#E8DFD0', M['cizgi']).replace('#FBF8F2', M['zemin']).replace('#6b5f73', M['mut'])
    bilgi = ''.join('<h2>%s</h2><p>%s</p>' % (esc(q), esc(a)) for q, a in T['bilgi'])
    diger = ' · '.join('<a href="%s">%s</a>' % (x['yol'], esc(x['ad'])) for x in TESTLER if x['yol'] != T['yol'])
    notu = ('<aside style="margin:24px 0;padding:16px 18px;border-radius:16px;background:%s;border-left:4px solid %s"><p style="margin:0 0 6px;font-weight:700">Psikolog Rojin Nazik\'in notu · %s</p><blockquote style="margin:0;font-style:italic;line-height:1.7">“%s”</blockquote></aside>' % (M['zemin'], M['a'], esc(T['not'][0]), esc(T['not'][1]))) if M['not_sahibi'] else ''
    return ("""<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
%(gtm)s
<title>%(title)s</title><meta name="description" content="%(desc)s"><meta name="robots" content="index, follow">
<link rel="canonical" href="%(canon)s">%(ikon)s
<style>*{box-sizing:border-box}body{margin:0;background:#fff;color:#1d1d22;font:16px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
.w{max-width:860px;margin:0 auto;padding:0 18px}.top{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 0;border-bottom:1px solid %(cizgi)s}
.top a.t{padding:9px 14px;border-radius:999px;border:1px solid %(cizgi)s;color:#1d1d22;font-weight:700;font-size:14px;text-decoration:none}
h1{font-size:clamp(28px,6vw,40px);line-height:1.15;margin:22px 0 10px;color:%(a2)s}h2{font-size:21px;color:%(a2)s;margin:26px 0 8px}
.lead{color:%(mut)s;font-size:17px}.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 20px;border-radius:14px;border:0;background:%(a)s;color:#fff;font:inherit;font-weight:800;cursor:pointer;text-decoration:none}
.dip{padding:24px 0 40px;font-size:13px;color:%(mut)s;border-top:1px solid %(cizgi)s;margin-top:30px}a{color:%(a)s}</style>%(css)s
%(betikler)s
</head><body><header class="w top"><a href="%(ana)s" style="text-decoration:none">%(logo)s</a><a class="t" href="tel:+905524187973" data-cta-area="test_header">📞 0552 418 79 73</a></header>
<main class="w"><h1>%(h1)s</h1><p class="lead">%(lead)s</p>%(form)s%(notu)s%(bilgi)s
<p class="ts-not" style="margin-top:20px">Diğer test: %(diger)s</p>
<p class="ts-not">Kaynak: %(kaynak)s Ölçek serbestçe kullanılabilir; buradaki Türkçe ifadeler bilgilendirme amaçlıdır. Bu test tanı koymaz. Acil bir durumda 112'yi arayın.</p></main>
<footer class="w dip"><a href="%(ana)s">%(marka)s</a> · Telefonu Selda Hanım açar · Pazartesi–Cumartesi 09:00–20:00</footer>%(betik)s</body></html>
""") % {'gtm': GTM_HEAD, 'title': esc(T['title'].replace('Psikolog Rojin Nazik', M['marka'])), 'desc': esc(T['desc']), 'canon': SITE + T['yol'], 'ikon': M['ikon'],
         'cizgi': M['cizgi'], 'a': M['a'], 'a2': M['a2'], 'mut': M['mut'], 'css': css, 'betikler': M['betikler'], 'ana': M['ana'], 'logo': M['logo'],
         'h1': esc(T['h1']), 'lead': esc(T['lead']), 'form': form_html(T), 'notu': notu, 'bilgi': bilgi, 'diger': diger, 'kaynak': esc(T['kaynak']),
         'marka': esc(M['marka']), 'betik': betik(T)}


def bagimsiz_yaz(kok, ad):
    yollar = []
    for T in TESTLER:
        d = os.path.join(kok, T['yol'].strip('/'))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(bagimsiz(T, ad))
        yollar.append(T['yol'])
    return yollar


if __name__ == '__main__':
    if '--elif' in sys.argv:
        print('Elif:', bagimsiz_yaz(sys.argv[sys.argv.index('--elif') + 1], 'elif')); sys.exit()
    sablon = open(os.path.join(KOK, SABLON), encoding='utf-8').read()
    for T in TESTLER:
        d = os.path.join(KOK, T['yol'].strip('/'))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(sayfa(sablon, T))
        print('yazıldı', T['yol'], '(yayında, dizine açık)' if YAYINLA else '(onay bekliyor: noindex)')
    site_haritasi(YAYINLA)
