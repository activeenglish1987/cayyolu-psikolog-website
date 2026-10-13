# -*- coding: utf-8 -*-
"""Google Ads'e özel sade açılış sayfaları (Rojin Nazik ve Çayyolu sitelerinde ortak şablon).

- Arama motorlarına kapalı (noindex), site haritasında ve menüde yok: SEO'ya dokunmaz,
  yalnız reklamdan gelen ziyaretçi görür. Reklamların "Nihai URL"si bu sayfalardır.
- Tek hedef telefonla aramak: menü yok, dışarı giden bağlantı yok; başlık aranan kelimeyle aynı.
- Ücret yazılmaz (avukat görüşü); telefonu Selda Hanım açar.
- Dönüşümler sitenin kendi ads-conversion.js'i ile sayılır; Pusula ve mesai dışı formu da çalışır.

Rojin sitesinde: python3 _araclar/reklam.py   (sayfaları randevu/ altına yazar)
Çayyolu sitesinde: build.py içinden çağrılır (_kaynak/reklam.py).
"""
import html, os, sys

esc = lambda x: html.escape(x or '', quote=True)
TEL = '+905524187973'
TEL_TXT = '0552 418 79 73'
WA = '905524187973'

ROJIN = {
    'ad': 'rojin', 'marka': 'Psikolog Rojin Nazik', 'site': 'https://www.psikologrojinnazik.com',
    'logo': '<img src="/images/brand/logo-rojin-nazik.png" alt="Psikolog Rojin Nazik" height="38" style="height:38px;width:auto">',
    'foto': '/images/brand/rojin-nazik-portrait-800.webp',
    'renk': {'a': '#6B3A8C', 'a2': '#3d1e54', 'hl': '#C9A06B', 'bg': '#FBF8F2', 'ink': '#2A1F2D', 'mut': '#6b5f73', 'line': '#E8DFD0'},
    'baslik_font': "Georgia,'Times New Roman',serif",
}
CAYYOLU = {
    'ad': 'cayyolu', 'marka': 'RN Psikoloji Çayyolu', 'site': 'https://www.cayyolupsikolog.com.tr',
    'logo': '<span style="display:inline-flex;align-items:center;gap:10px;font-weight:700;color:#14264A"><span style="width:38px;height:38px;border-radius:10px;background:#14264A;color:#fff;display:grid;place-items:center;font-size:15px">RN</span><span style="line-height:1.15">RN Psikoloji<small style="display:block;font-weight:500;font-size:12px;color:#566179">Çayyolu Şubesi</small></span></span>',
    'foto': '/assets/img/opt/psikolog-rojin-nazik-720.webp',
    'renk': {'a': '#14264A', 'a2': '#14264A', 'hl': '#E9A23B', 'bg': '#F2F6FB', 'ink': '#18223A', 'mut': '#566179', 'line': '#DCE4F0'},
    'baslik_font': "system-ui,-apple-system,'Segoe UI',sans-serif",
}

# Telefonun açıldığı saatler (Google Ads reklam ve arama öğesi zaman planı da aynı). Pazar kapalı.
SAAT_TXT = 'Hafta içi 10:00–19:00 · Cumartesi 10:00–18:00'
ROJIN_ETIKET = ['15+ yıllık mesleki deneyim', 'Şema terapi eğitimi', 'AB Psikologlar Derneği Genel Başkanı', '3 kitap yazarı']
SUBELER = [
    ('Yaşamkent / Çayyolu', 'Konutkent, Dumlupınar Blv. No:399 Kat:28 D:121, Çankaya', 'Pazartesi–Cumartesi · ücretsiz otopark'),
    ('Kızılay', 'Atatürk Blv. No:127 Kat:8, Bakanlıklar', 'Pazartesi günleri'),
    ('Online', 'Türkiye ve yurt dışından görüntülü görüşme', 'Pazartesi–Cumartesi'),
]
ADIMLAR = [
    ('Arayın', 'Telefonu Selda Hanım açar. İhtiyacınızı kısaca dinler; her şeyi anlatmanız gerekmez.'),
    ('Size uygun saat', 'Gün, saat ve şubeyi birlikte belirlersiniz; ücret bilgisini de aynı aramada öğrenirsiniz.'),
    ('İlk görüşme', 'Tanışma ve değerlendirme görüşmesi: ne yaşadığınız konuşulur, çalışma planı birlikte oluşturulur.'),
]
ORTAK_SSS = [
    ('Ücret ne kadar?', 'Seans ücretini Selda Hanım telefonda net olarak söyler; aynı aramada size uygun saati de öğrenirsiniz.'),
    ('Görüşmeler gizli mi?', 'Evet. Görüşmelerde konuşulanlar gizlidir; yasal zorunluluk ve can güvenliği gibi istisnalar ilk görüşmede açıkça anlatılır.'),
    ('Online görüşme yapılıyor mu?', 'Evet. Ankara dışından ya da yurt dışından görüntülü görüşme yapılabilir.'),
    ('Psikolog ilaç yazar mı?', 'Hayır. Psikologlar tanı koymaz ve ilaç yazmaz; gerekli durumlarda psikiyatri uzmanına yönlendirme yapılır.'),
]

# "Ekranda ve basında" bölümü: logolar gerçek gazete sayfalarından kırpıldı (_araclar/basin.py, assets/basin/).
# Çayyolu sitesine de aynı dosyalar kopyalanır. Video tıklanınca sayfada oynar; dışarı bağlantı yok.
VIDEOLAR = {
    'fw1zD6zr62k': ('CNN Türk · İşin Uzmanı', 'Panik atak nedir, belirtileri nelerdir?'),
    'QaMYPc-FUw4': ('CNN Türk · İşin Uzmanı', 'Bilişsel davranışçı terapi teknikleri'),
    'ZEPbGUV6MSE': ('Beyaz TV · Duyduk Duymadık', 'Programın konuk uzmanı'),
    '6eg7skd0824': ('Video', 'Sınav stresi ve psikolojik dayanıklılık'),
}
LOGOLAR = [('CNN TÜRK', 'cnnturk', 146, 120), ('Beyaz TV', 'beyaztv', 204, 70), ('Milliyet', 'milliyet', 480, 87),
           ('Akşam', 'aksam', 480, 103), ('Takvim', 'takvim', 460, 120), ('Vatan', 'vatan', 480, 102)]

KUPUR = {  # anahtar: (gazete, tarih, başlık) - basin.py KUPURLER'den
    'milliyet-2022-11': ('Milliyet', '13 Kasım 2022', 'Ergenlik dönemindeki çocukların psikolojilerine dikkat!'),
    'aksam-cumartesi-2022-06': ('Akşam Cumartesi', '25 Haziran 2022', 'Stresin olumsuz etkileri nelerdir?'),
    'takvim-2022-07': ('Takvim', '31 Temmuz 2022', 'Uyku bozukluğuna dikkat!'),
    'vatan-2023-01': ('Vatan', '29 Ocak 2023', 'Aşırı düşünmek neden olur?'),
    'izgazete-2022-11': ('İzgazete', '6 Kasım 2022', 'Ergen psikolojisinde terapilerin önemi'),
    'haber-2023-10': ('Haber', '1 Ekim 2023', 'Çocuklar da ve ergenler de psikolojiye dikkat edilmeli!'),
    'star-stres': ('Kıbrıs Star', '2022', 'Stresle nasıl başa çıkarız?'),
    'zafer-2022-06': ('Zafer', '12 Haziran 2022', 'Depresyona yol açan faktörler nelerdir?'),
    'yesil-2023-10': ('Yeşil', '1 Ekim 2023', 'Aşırı düşünmek neden olur?'),
}
GAZETE_SIRA = ['milliyet-2022-11', 'aksam-cumartesi-2022-06', 'vatan-2023-01', 'takvim-2022-07', 'izgazete-2022-11', 'star-stres', 'zafer-2022-06', 'yesil-2023-10']
KITAPLAR = [('bir-hayatla-evlenmek', 'Bir Hayatla Evlenmek'), ('bir-odanin-otesi', 'Bir Odanın Ötesi'), ('dengeyi-yakalamak', 'Dengeyi Yakalamak')]

# Her reklam grubu için bir sayfa: başlık aranan kelimeyle aynı olmalı (mesaj uyumu)
SAYFALAR = {
    'rojin': [
        {'yol': '/randevu/ankara-psikolog/', 'video': 'QaMYPc-FUw4', 'h1': 'Ankara Psikolog', 'h1b': 'Rojin Nazik',
         'alt': "Yaşamkent ve Kızılay'da yüz yüze, dilerseniz online psikolojik danışmanlık. Kendinizi rahatça anlatabileceğiniz, acele edilmeyen bir ortam.",
         'konular': ['Kaygı, stres ve panik atak', 'Depresif duygular ve isteksizlik', 'İlişki, evlilik ve aile sorunları', 'Yas, boşanma ve zor yaşam dönemleri', 'Öfke, özgüven ve tekrar eden düşünceler', 'Çocuk ve ergen danışmanlığı'],
         'not': ('‘Psikoloğa gitmeli miyim?’ diye soranlara', 'Psikoloğa başvurmak için kişinin hayatının tamamen kontrolden çıkmasını beklemesi gerektiğini düşünmüyorum. Aynı düşünce, duygu veya ilişki döngüsünün tekrar ettiğini fark ediyor ve bunun içinden çıkmakta zorlanıyorsa bunu konuşmak için yeterli bir neden olabilir.')},
        {'yol': '/randevu/cocuk-psikologu/', 'video': '6eg7skd0824', 'gazete': ['milliyet-2022-11', 'izgazete-2022-11', 'haber-2023-10'], 'h1': 'Ankara Çocuk ve Ergen', 'h1b': 'Psikoloğu',
         'alt': 'Okul, kaygı, öfke ve uyum sorunlarında çocuk ve ergen görüşmeleri; küçük yaşta oyun terapisi ve ebeveyn danışmanlığı. Yaşamkent, Kızılay ve online.',
         'konular': ['Öfke nöbetleri ve davranış sorunları', 'Okul, ders ve sınav kaygısı', 'Korkular, ayrılma kaygısı ve uyku sorunları', 'Boşanma sürecinde çocuk', 'Ergenlikte iletişim, içe kapanma, ekran kullanımı', 'Küçük yaşta oyun terapisi (Psikolog Elif Erdoğan)'],
         'ekip': 'Küçük yaştaki çocuklarla oyun terapisi ve psikolojik test için ekibimizde Psikolog Elif Erdoğan da çalışıyor; size uygun uzmanı Selda Hanım birlikte belirler.',
         'not': ('Anne-babaların en sık kaçırdığı nokta', 'Ben davranışın ne zaman başladığına, hangi durumlarda arttığına ve çocuğun o dönemde hayatında neler yaşadığına bakmayı önemli buluyorum. Çünkü bazı çocuklar ifade etmekte zorlandıkları duyguları davranışları üzerinden gösterebiliyor.'),
         'sss': [('İlk görüşmeye çocuğumla mı gelmeliyim?', 'Çocuklarda ilk görüşme genellikle ebeveynle yapılır; ardından çocuğun yaşına uygun görüşmeler planlanır. Telefonda Selda Hanım size durumunuza göre yol gösterir.')]},
        {'yol': '/randevu/cift-terapisi/', 'video': 'ZEPbGUV6MSE', 'h1': 'Ankara Çift ve', 'h1b': 'Evlilik Terapisi',
         'alt': 'İletişim sorunları, sık tartışma, güven ve uzaklaşma için çift ve evlilik görüşmeleri. Yaşamkent ve Kızılay’da yüz yüze ya da online.',
         'konular': ['İletişim kuramama, sık tartışma', 'Güven sorunu ve aldatılma sonrası süreç', 'Birbirinden uzaklaşma', 'Evlilik öncesi danışmanlık', 'Boşanma kararı ve sonrası', 'Ebeveynlik ve aile içi çatışma'],
         'not': ('Çift görüşmelerinde en sık duyduğum cümle', '‘Ben defalarca söyledim ama beni anlamadı’ cümlesini çift görüşmelerinde oldukça sık duyuyorum. Tartışmanın içindeki öfkenin altında bazen ‘beni önemse’, ‘yanımda olduğunu hissettir’ veya ‘beni anlamaya çalış’ gibi çok daha temel bir ihtiyaç bulunabiliyor.'),
         'sss': [('İkimizin birlikte gelmesi mi gerekiyor?', 'Çift görüşmelerine genellikle birlikte başlanır; gerekirse bireysel görüşmeler de planlanır. İlk adımı biriniz atabilir.')]},
        {'yol': '/randevu/kaygi-panik-atak/', 'video': 'fw1zD6zr62k', 'gazete': ['aksam-cumartesi-2022-06', 'vatan-2023-01', 'star-stres'], 'h1': 'Kaygı ve Panik Atak', 'h1b': 'Psikolojik Destek · Ankara',
         'alt': 'Kaygı, panik atak, sosyal kaygı ve takılan düşünceler için bilişsel davranışçı yaklaşımla psikolojik destek. Yaşamkent, Kızılay ve online.',
         'konular': ['Panik atak ve beklenti kaygısı', 'Yaygın kaygı ve sürekli endişe', 'Sosyal kaygı', 'Sınav ve performans kaygısı', 'Takılan düşünceler, aşırı düşünme', 'Bedensel belirtilerle gelen kaygı'],
         'not': ('Panik atakta en sık korkulan şey', 'Panik yaşayan kişilerde bedensel belirtilerin kendisinden çok, bu belirtilere verilen anlamın kişiyi zorladığını sık görüyorum. Bu nedenle görüşmelerde kişinin yalnızca ne hissettiğine değil, hissettiği şeyi nasıl yorumladığına da bakıyorum.')},
    ],
    'cayyolu': [
        {'yol': '/randevu/cayyolu-psikolog/', 'video': 'QaMYPc-FUw4', 'h1': 'Çayyolu ve Yaşamkent', 'h1b': 'Psikolog',
         'alt': "RN Psikoloji'nin Yaşamkent ofisinde yüz yüze psikolojik danışmanlık: Çayyolu, Ümitköy, Konutkent, İncek ve Beysukent'e yakın, ücretsiz otopark.",
         'konular': ['Kaygı, stres ve panik atak', 'İlişki, evlilik ve aile sorunları', 'Çocuk ve ergen danışmanlığı', 'Yas, boşanma ve zor yaşam dönemleri', 'Depresif duygular ve isteksizlik', 'Online görüşme seçeneği'],
         'ekip': 'Kurucu Psikolog Rojin Nazik ve Psikolog Elif Erdoğan bu ofiste görüşme yapıyor; size uygun uzmanı Selda Hanım birlikte belirler.',
         'not': ('İlk kez gelenler en çok neden çekiniyor?', 'İlk görüşmeye gelen kişilerde en sık gördüğüm kaygılardan biri, ‘Ne anlatacağım, nereden başlayacağım?’ düşüncesi. İlk görüşme ilerledikçe bunun bir sınav olmadığını ve her şeyi bir anda anlatmak zorunda olmadıklarını fark ettiklerinde daha rahatlayabildiklerini görüyorum.')},
        {'yol': '/randevu/cocuk-psikologu/', 'video': '6eg7skd0824', 'h1': 'Çayyolu Çocuk ve Ergen', 'h1b': 'Psikoloğu',
         'alt': 'Yaşamkent ofisinde çocuk ve ergen görüşmeleri, küçük yaşta oyun terapisi ve ebeveyn danışmanlığı. Çayyolu, Ümitköy ve Konutkent’e yakın.',
         'konular': ['Öfke ve davranış sorunları', 'Okul, ders ve sınav kaygısı', 'Korkular, ayrılma kaygısı, uyku', 'Boşanma sürecinde çocuk', 'Ergenlikte iletişim ve içe kapanma', 'Oyun terapisi ve psikolojik test (Psikolog Elif Erdoğan)'],
         'ekip': 'Küçük yaştaki çocuklarla oyun terapisi ve psikolojik test için Psikolog Elif Erdoğan da bu ofiste çalışıyor; size uygun uzmanı Selda Hanım birlikte belirler.',
         'not': ('Ebeveynlere ilk önerim', 'Ebeveynlerden ilk istediğim şeylerden biri, çocuğun davranışını hemen değiştirmeye çalışmadan önce onu biraz daha dikkatli gözlemlemeleri oluyor. Özellikle bir davranışın öncesinde ve sonrasında neler yaşandığı çok önemli ipuçları verebiliyor.'),
         'sss': [('İlk görüşmeye çocuğumla mı gelmeliyim?', 'Çocuklarda ilk görüşme genellikle ebeveynle yapılır; ardından çocuğun yaşına uygun görüşmeler planlanır.')]},
        {'yol': '/randevu/cift-terapisi/', 'video': 'ZEPbGUV6MSE', 'h1': 'Çayyolu Çift ve', 'h1b': 'Evlilik Terapisi',
         'alt': 'Yaşamkent ofisinde çift ve evlilik görüşmeleri: iletişim, güven, sık tartışma ve uzaklaşma. Çayyolu, Ümitköy ve Konutkent’e yakın, ücretsiz otopark.',
         'konular': ['İletişim kuramama, sık tartışma', 'Güven sorunu', 'Birbirinden uzaklaşma', 'Evlilik öncesi danışmanlık', 'Boşanma kararı ve sonrası', 'Ebeveynlik ve aile içi çatışma'],
         'not': ('Çiftlerde en sık gördüğüm sorun', 'Çiftlerin çoğu ‘iletişim kuramıyoruz’ diyerek geliyor. Görüşmeler ilerledikçe çoğu zaman sorunun yalnızca iletişim olmadığını; uzun süredir konuşulmamış kırgınlıkların, anlaşılmama hissinin ve tekrar eden ilişki döngülerinin biriktiğini görüyorum.'),
         'sss': [('İkimizin birlikte gelmesi mi gerekiyor?', 'Çift görüşmelerine genellikle birlikte başlanır; gerekirse bireysel görüşmeler de planlanır.')]},
    ],
}


def css(S):
    r = S['renk']
    return ('''<style>
:root{--a:%(a)s;--a2:%(a2)s;--hl:%(hl)s;--bg:%(bg)s;--ink:%(ink)s;--mut:%(mut)s;--line:%(line)s;--call:#16A34A}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;padding-bottom:calc(84px + env(safe-area-inset-bottom))}
a{color:var(--a)}
.w{max-width:980px;margin:0 auto;padding:0 18px}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0}
.top a.t{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;border-radius:999px;background:#fff;border:1px solid var(--line);color:var(--ink);font-weight:700;font-size:14px;text-decoration:none}
.hi{display:grid;gap:22px;padding:8px 18px 26px}
@media(min-width:860px){.hi{grid-template-columns:1.15fr .85fr;align-items:center;padding:30px 18px 46px}}
main.w{padding-top:18px}
.ey{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--a)}
h1{font-family:%(f)s;font-weight:600;font-size:clamp(32px,8vw,52px);line-height:1.08;margin:8px 0 12px;color:var(--a2);letter-spacing:-.01em}
h1 em{font-style:italic;color:var(--a)}
.alt{color:var(--mut);font-size:17px;margin:0 0 18px}
.acik{display:flex;align-items:center;gap:8px;font-size:14.5px;font-weight:600;color:#166534;margin:0 0 12px}
.acik i{width:9px;height:9px;border-radius:50%%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.18)}
.hero-actions{display:grid;gap:10px;max-width:440px}
.ara{display:flex;align-items:center;justify-content:center;gap:10px;padding:17px 18px;border-radius:16px;background:var(--call);color:#fff!important;font-weight:800;font-size:18px;text-decoration:none;box-shadow:0 14px 30px -12px rgba(22,163,74,.7)}
.ara small{display:block;font-size:12.5px;font-weight:600;opacity:.92}
.wa{display:block;text-align:center;font-size:14.5px;font-weight:600;color:var(--mut)!important;text-decoration:underline;text-underline-offset:3px;padding:4px}
.puan{margin-top:14px;font-size:14px;color:var(--mut)}.puan b{color:var(--ink)}.puan span{color:#E5A50A;letter-spacing:1px}
.foto{position:relative;max-width:420px;width:100%%;justify-self:center}
.foto img{width:100%%;height:auto;max-height:440px;object-fit:cover;object-position:50%% 20%%;border-radius:24px;display:block;box-shadow:0 24px 50px -28px rgba(0,0,0,.45)}
@media(max-width:859px){.foto{order:-1;max-width:none}.foto img{max-height:210px}}
.kart{background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px;margin:0 0 16px}
h2{font-family:%(f)s;font-weight:600;font-size:24px;line-height:1.25;margin:0 0 12px;color:var(--a2)}
.etiket{display:flex;flex-wrap:wrap;gap:8px;margin:0}
.etiket span{padding:7px 12px;border-radius:999px;background:var(--bg);border:1px solid var(--line);font-size:13.5px;font-weight:700;color:var(--a2)}
.konu{list-style:none;margin:0;padding:0;display:grid;gap:8px}
@media(min-width:700px){.konu{grid-template-columns:1fr 1fr}}
.konu li{padding:10px 12px 10px 34px;border-radius:12px;background:var(--bg);position:relative;font-weight:600;font-size:15px}
.konu li:before{content:"✓";position:absolute;left:12px;top:10px;color:var(--call);font-weight:800}
.adim{display:grid;gap:10px;counter-reset:a}
@media(min-width:760px){.adim{grid-template-columns:repeat(3,1fr)}}
.adim div{padding:14px;border-radius:14px;background:var(--bg)}
.adim b{display:flex;align-items:center;gap:8px;color:var(--a2)}
.adim b:before{counter-increment:a;content:counter(a);width:26px;height:26px;border-radius:50%%;display:grid;place-items:center;background:var(--a);color:#fff;font-size:13px}
.adim p{margin:6px 0 0;font-size:14.5px;color:var(--mut)}
blockquote{margin:0;padding:16px 18px;border-left:4px solid var(--hl);background:var(--bg);border-radius:0 14px 14px 0;font-style:italic;line-height:1.7}
.qk{margin-top:8px;font-size:13px;color:var(--mut)}
.sube{display:grid;gap:10px}@media(min-width:760px){.sube{grid-template-columns:repeat(3,1fr)}}
.sube div{padding:14px;border-radius:14px;background:var(--bg);font-size:14.5px}.sube b{display:block;color:var(--a2)}
details{border-bottom:1px solid var(--line);padding:12px 0}details:last-child{border:0}
summary{cursor:pointer;font-weight:700;list-style:none}summary::-webkit-details-marker{display:none}
summary:after{content:"+";float:right;color:var(--a)}details[open] summary:after{content:"–"}
details p{margin:8px 0 0;color:var(--mut)}
.son{text-align:center;background:linear-gradient(135deg,var(--a2),var(--a));color:#fff;border:0}
.son h2{color:#fff}.son p{opacity:.9;margin:0 0 14px}.son .ara{max-width:420px;margin:0 auto}
.gos .lg{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 14px;padding:0;list-style:none}
.gos .lg li{height:44px;padding:6px 10px;border:1px solid var(--line);border-radius:10px;background:#fff;display:flex;align-items:center}
.gos .lg img{max-height:30px;max-width:96px;width:auto;height:auto;display:block}.gos .lg .tv8{font:900 15px/1 Arial,sans-serif;color:#fff;background:#111;padding:5px 7px;border-radius:5px}
.gos .vd{all:unset;box-sizing:border-box;cursor:pointer;position:relative;display:block;width:100%%;aspect-ratio:16/9;border-radius:16px;overflow:hidden;background:#111}
.gos .vd img,.gos .vd iframe{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;border:0}
.gos .vd i{position:absolute;left:50%%;top:50%%;width:62px;height:62px;margin:-31px 0 0 -31px;border-radius:50%%;background:rgba(255,255,255,.94);box-shadow:0 8px 24px rgba(0,0,0,.35)}
.gos .vd i:after{content:"";position:absolute;left:25px;top:19px;border-left:18px solid var(--a);border-top:12px solid transparent;border-bottom:12px solid transparent}
.gos .vk{margin:8px 0 0;font-size:14px;color:var(--mut)}.gos .vk b{color:var(--a2)}
.gos .say{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px}.gos .say div{padding:10px;border-radius:12px;background:var(--bg);text-align:center;font-size:12.5px;color:var(--mut);font-weight:600}.gos .say b{display:block;font-size:20px;color:var(--a2)}
.gos .vr{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;margin:12px -4px 0;padding:2px 4px 8px;-webkit-overflow-scrolling:touch}
.gos .vr button,.gos .gz button{all:unset;box-sizing:border-box;cursor:pointer;flex:0 0 auto;scroll-snap-align:start;border-radius:12px;overflow:hidden;background:#fff;border:1px solid var(--line)}
.gos .vr button{width:210px}.gos .vr img{display:block;width:100%%;aspect-ratio:16/9;object-fit:cover}
.gos .vr span,.gos .gz span{display:block;padding:7px 9px;font-size:12.5px;line-height:1.35;color:var(--mut)}.gos .vr b,.gos .gz b{display:block;color:var(--a2);font-size:12.5px}
.gos h3{font-family:%(f)s;font-weight:600;font-size:18px;color:var(--a2);margin:16px 0 8px}
.gos .gz{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -4px;padding:2px 4px 8px}
.gos .gz button{width:132px}.gos .gz img{display:block;width:100%%;height:170px;object-fit:cover;object-position:top;background:#f3efe8}
.buyuk{position:fixed;inset:0;z-index:10000;background:rgba(10,6,14,.88);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:16px;cursor:zoom-out}
.buyuk img{max-width:100%%;max-height:86vh;border-radius:8px;background:#fff}.buyuk span{color:#fff;font-size:13px;opacity:.8}
.kt{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px;max-width:460px}.kt figure{margin:0;text-align:center}
.kt img{width:100%%;height:auto;aspect-ratio:1;object-fit:cover;border-radius:12px;display:block}.kt figcaption{font-size:12.5px;font-weight:700;color:var(--a2);margin-top:6px;line-height:1.3}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:10px}.pn div{padding:14px;border-radius:14px;background:var(--bg);text-align:center;font-weight:700;color:var(--a2)}
.pn b{display:block;font-family:%(f)s;font-size:34px;line-height:1.1}.pn span{display:block;color:#E5A50A;letter-spacing:2px}.pn small{display:block;font-weight:500;color:var(--mut);font-size:13px}
.gl{display:inline-block;margin-top:12px;font-weight:700;font-size:14.5px}
.ek{display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:520px}.ek div{text-align:center}.ek img{width:100%%;height:auto;aspect-ratio:4/5;object-fit:cover;object-position:50%% 20%%;border-radius:14px;display:block;margin-bottom:8px}
.ek b{display:block;color:var(--a2)}.ek small{color:var(--mut);font-size:13px}
.of{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}.of img{width:100%%;height:200px;object-fit:cover;border-radius:14px;display:block}
@media(min-width:760px){.of img{height:280px}}
.bar{transition:transform .25s,opacity .25s}
.dip{padding:18px 0 26px;font-size:12.5px;color:var(--mut);text-align:center}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:9990;display:flex;gap:8px;padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:rgba(255,255,255,.96);border-top:1px solid var(--line);backdrop-filter:blur(10px)}
.bar .ara{flex:1;padding:14px;font-size:16.5px;box-shadow:none}
.bar .w2{display:grid;place-items:center;width:54px;border-radius:14px;border:2px solid #25D366;color:#128C4A;text-decoration:none;font-size:22px}
@media(min-width:860px){.bar{display:none}body{padding-bottom:0}}
</style>''' % dict(r, f=S['baslik_font']))


def govde(S, P):
    """Sayfanın <body> içeriği (head hariç). Rojin sitesinde ana sayfadaki "şov" da burada:
    akan basın şeridi + izleyin düğmesi (vitrin.js), videolar, gazete sayfaları, kitaplar, puanlar, ekip ve ofis."""
    rojin = S['ad'] == 'rojin'
    etiketler = ''.join('<span>%s</span>' % esc(t) for t in ROJIN_ETIKET)
    konular = ''.join('<li>%s</li>' % esc(k) for k in P['konular'])
    adimlar = ''.join('<div><b>%s</b><p>%s</p></div>' % (esc(a), esc(b)) for a, b in ADIMLAR)
    subeler = ''.join('<div><b>%s</b>%s<br><small>%s</small></div>' % (esc(a), esc(b), esc(c)) for a, b, c in SUBELER)
    sss = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(c)) for q, c in (P.get('sss', []) + ORTAK_SSS))
    wa_msg = 'Merhaba, %s için randevu bilgisi almak istiyorum.' % (P['h1'] + ' ' + P['h1b']).replace(' · Ankara', '')
    wa = 'https://wa.me/%s?text=%s' % (WA, html.escape(__import__('urllib.parse').parse.quote(wa_msg)))
    vid = P.get('video', 'QaMYPc-FUw4'); vk = VIDEOLAR[vid]
    logolar = ''.join('<li><img src="/assets/basin/logo/%s.webp" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></li>' % (k, esc(a), w, h) for a, k, w, h in LOGOLAR[:2])
    logolar += '<li><span class="tv8">TV8 INT</span></li>'
    logolar += ''.join('<li><img src="/assets/basin/logo/%s.webp" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></li>' % (k, esc(a), w, h) for a, k, w, h in LOGOLAR[2:])
    # Diğer yayınlar: küçük kapaklar; dokununca büyük oynatıcıda açılır
    digerleri = ''.join('<button type="button" data-yt="%s" aria-label="%s – videoyu oynat"><img src="/assets/basin/video-%s.webp" alt="" width="320" height="180" loading="lazy" decoding="async"><span><b>%s</b>%s</span></button>' % (
        v, esc(VIDEOLAR[v][1]), v, esc(VIDEOLAR[v][0]), esc(VIDEOLAR[v][1])) for v in VIDEOLAR if v != vid)
    gazete = ''
    if rojin:
        sira = P.get('gazete', []) + [g for g in GAZETE_SIRA if g not in P.get('gazete', [])]
        gazete = '<h3>Gazete sayfalarında</h3><div class="gz">%s</div>' % ''.join(
            '<button type="button" data-g="%s" aria-label="%s, %s: %s – büyüt"><img src="/assets/lp/kupur/%s.webp" alt="" width="264" height="340" loading="lazy" decoding="async"><span><b>%s</b>%s</span></button>' % (
                g, esc(KUPUR[g][0]), esc(KUPUR[g][1]), esc(KUPUR[g][2]), g, esc(KUPUR[g][0]), esc(KUPUR[g][2])) for g in sira[:8])
    gosteri = ('<section class="kart gos"><h2>Ekranda ve basında</h2><ul class="lg">%s</ul>'
               '<button type="button" class="vd" data-yt="%s" aria-label="%s – videoyu oynat"><img src="/assets/basin/video-%s.webp" alt="%s programında Psikolog Rojin Nazik" width="640" height="360" loading="lazy" decoding="async"><i></i></button>'
               '<p class="vk"><b>%s</b> · %s</p><div class="vr">%s</div>%s'
               '<div class="say"><div><b>7</b>TV ve video yayını</div><div><b>19</b>gazete sayfası</div><div><b>3</b>kitap</div></div></section>') % (
        '' if rojin else logolar, vid, esc(vk[1]), vid, esc(vk[0]), esc(vk[0]), esc(vk[1]), digerleri, gazete)
    if rojin:  # logolar sayfanın üstündeki akan şeritte (vitrin.js); burada tekrar edilmez
        gosteri = gosteri.replace('<ul class="lg"></ul>', '')
    ekip = ('<p style="margin:12px 0 0;color:var(--mut);font-size:15px">%s</p>' % esc(P['ekip'])) if P.get('ekip') else ''
    kitaplar = puan_kart = ekip_kart = ofis = ''
    puan = '<span>★★★★★</span> <b>5.0</b> · Doktorsitesi\'nde 169 danışan değerlendirmesi'
    if rojin:
        puan = '<span>★★★★★</span> <b>5.0</b> Doktorsitesi (169) · <b>4.8</b> Google (120+)'
        kitaplar = '<div class="kt">%s</div>' % ''.join(
            '<figure><img src="/assets/lp/kitap-%s.webp" alt="%s – Psikolog Rojin Nazik" width="300" height="300" loading="lazy" decoding="async"><figcaption>%s</figcaption></figure>' % (k, esc(a), esc(a)) for k, a in KITAPLAR)
        puan_kart = ('<section class="kart"><h2>Danışanlar ne diyor?</h2><div class="pn">'
                     '<div><b>5.0</b><span>★★★★★</span>Doktorsitesi<small>169 değerlendirme</small></div>'
                     '<div><b>4.8</b><span>★★★★★</span>Google<small>120\'yi aşkın değerlendirme</small></div></div>'
                     '<a class="gl" href="https://g.page/psikologrojinnazik" target="_blank" rel="noopener">Google değerlendirmelerini okuyun →</a></section>')
        ekip_kart = ('<section class="kart"><h2>Ekibimiz</h2><div class="ek">'
                     '<div><img src="/assets/lp/rojin-nazik.webp" alt="Psikolog Rojin Nazik" width="360" height="450" loading="lazy" decoding="async"><b>Rojin Nazik</b><small>Psikolog · Kurucu</small></div>'
                     '<div><img src="/assets/lp/elif-erdogan.webp" alt="Psikolog Elif Erdoğan" width="360" height="450" loading="lazy" decoding="async"><b>Elif Erdoğan</b><small>Psikolog · Çocuk, ergen ve oyun terapisi</small></div>'
                     '</div><p style="margin:12px 0 0;color:var(--mut);font-size:15px">Size hangi psikoloğun uygun olduğunu Selda Hanım telefonda birlikte belirler.</p></section>')
        ofis = ('<div class="of"><img src="/assets/lp/ofis-salon.webp" alt="RN Psikoloji ofisinden bekleme alanı" width="600" height="800" loading="lazy" decoding="async">'
                '<img src="/assets/lp/ofis-koltuk.webp" alt="RN Psikoloji ofisinden görüşme alanı" width="600" height="800" loading="lazy" decoding="async"></div>')
    return '''<header class="w top">%(logo)s<a class="t" href="tel:%(tel)s" data-cta-area="lp_header">📞 %(teltxt)s</a></header>
<section class="hero"><div class="w hi">
<div>
<div class="ey">Psikolog Rojin Nazik · RN Psikoloji</div>
<h1>%(h1)s <em>%(h1b)s</em></h1>
<p class="alt">%(alt)s</p>
<div class="acik" data-open-status><i></i>Telefonu Selda Hanım açar · %(saat)s</div>
<div class="hero-actions" data-cta-area="lp_hero">
<a class="ara" href="tel:%(tel)s"><span>📞</span><span>Hemen Ara · %(teltxt)s<small>Uygun saati ve ücreti Selda Hanım hemen söylesin</small></span></a>
<a class="wa" href="%(wa)s" target="_blank" rel="noopener">WhatsApp'tan yazmayı tercih ederim</a>
</div>
<div class="puan">%(puan)s</div>
</div>
<div class="foto portrait-card"><img src="%(foto)s" alt="Psikolog Rojin Nazik" width="720" height="900" fetchpriority="high"></div>
</div></section>
<main class="w">
%(gosteri)s
<section class="kart"><h2>Psikolog Rojin Nazik</h2><div class="etiket">%(etiket)s</div>
<p style="margin:12px 0 0;color:var(--mut);font-size:15px">CNN Türk, Milliyet ve Sabah'ta uzman konuk; Psychology Times kurucusu.</p>%(ekip)s%(kitaplar)s</section>
%(puan_kart)s
<section class="kart"><h2>Hangi konularda destek alabilirsiniz?</h2><ul class="konu">%(konular)s</ul></section>
<section class="kart"><h2>Randevu 3 adımda</h2><div class="adim">%(adimlar)s</div></section>
%(ekip_kart)s
<section class="kart"><h2>Rojin Nazik'in notu</h2><blockquote>“%(not)s”</blockquote><div class="qk">Psikolog Rojin Nazik · %(notb)s</div></section>
<section class="kart"><h2>Görüşme yerleri</h2><div class="sube">%(subeler)s</div>%(ofis)s</section>
<section class="kart"><h2>Sık sorulanlar</h2>%(sss)s</section>
<section class="kart son"><h2>İlk adım tek bir telefon</h2><p>Selda Hanım size en yakın uygun saati söylesin.</p><a class="ara" href="tel:%(tel)s" data-cta-area="lp_son"><span>📞</span><span>Hemen Ara · %(teltxt)s</span></a></section>
</main>
<footer class="w dip">%(marka)s · Psikologlar tanı koymaz ve ilaç yazmaz. Acil bir durumda 112'yi arayın.</footer>
<script>(function(){try{var p=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Istanbul',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()),g=function(t){for(var i=0;i<p.length;i++)if(p[i].type===t)return p[i].value},d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(g('weekday')),m=(+g('hour')%%24)*60+(+g('minute'));var e=document.querySelector('.acik');if((d>=1&&d<=5&&m>=600&&m<1140)||(d===6&&m>=600&&m<1080))e.innerHTML='<i></i>Şu an açığız · Telefonu Selda Hanım açar';else{e.innerHTML='<i style="background:#F59E0B;box-shadow:0 0 0 4px rgba(245,158,11,.2)"></i>Şu an mesai dışındayız · %(saat)s';e.style.color='var(--mut)'}}catch(x){}})();</script>
<script>/* Aranan kelimeye göre başlık (mesaj uyumu). Google Ads > Hesap ayarları > "Nihai URL son eki": kw={keyword}
   Yalnız hazır tablodaki kalıplar kullanılır; aranan kelime sayfaya olduğu gibi yazılmaz. */
(function(){try{var q=new URLSearchParams(location.search),k=(q.get('kw')||q.get('utm_term')||q.get('keyword')||'').toLocaleLowerCase('tr-TR').replace(/[+_]/g,' ');if(!k)return;
var Y=[[/kızılay|kizilay/,'Kızılay'],[/çankaya|cankaya/,'Çankaya'],[/yaşamkent|yasamkent/,'Yaşamkent'],[/çayyolu|cayyolu/,'Çayyolu'],[/ümitköy|umitkoy/,'Ümitköy'],[/konutkent/,'Konutkent'],[/incek/,'İncek'],[/beysukent/,'Beysukent'],[/bilkent/,'Bilkent'],[/eryaman/,'Eryaman'],[/ankara/,'Ankara']];
var K=[[/ergen|genç|genc/,'Ergen Psikoloğu'],[/çocuk|cocuk|pedagog|oyun terap/,'Çocuk Psikoloğu'],[/çift|cift|evlilik|ilişki|iliski/,'Çift Terapisi'],[/aile/,'Aile Danışmanı'],[/panik/,'Panik Atak Desteği'],[/kaygı|kaygi|anksiyete/,'Kaygı İçin Psikolog'],[/depresyon/,'Depresyon İçin Psikolog'],[/takıntı|takinti|okb/,'Takıntı (OKB) İçin Psikolog'],[/travma/,'Travma İçin Psikolog'],[/boşanma|bosanma/,'Boşanma Danışmanlığı'],[/online|çevrimiçi|cevrimici|internet/,'Online Psikolog'],[/kadın psikolog|kadin psikolog/,'Kadın Psikolog'],[/psikoterapist|terapist/,'Psikoterapist'],[/psikolojik danışman|psikolojik danisman/,'Psikolojik Danışmanlık']];
var bul=function(L){for(var i=0;i<L.length;i++)if(L[i][0].test(k))return L[i][1];return ''};var y=bul(Y),c=bul(K);if(!y&&!c)return;
y=y||'%(kwyer)s';c=c||'Psikolog';var h=document.querySelector('h1');h.textContent=y+' ';var e=document.createElement('em');e.textContent=c;h.appendChild(e);
document.title=y+' '+c+' | %(marka)s';(window.dataLayer=window.dataLayer||[]).push({event:'lp_baslik_uyumu',lp_baslik:y+' '+c});}catch(x){}})();</script>
<script>(function(){var dl=function(o){(window.dataLayer=window.dataLayer||[]).push(o)},b=document.querySelector('.gos .vd');if(!b)return;
function oynat(id,ad){var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0&playsinline=1';f.title=ad;f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;b.innerHTML='';b.appendChild(f);dl({event:'lp_video_oynat',video:id});}
b.addEventListener('click',function(){if(!b.querySelector('iframe'))oynat(b.getAttribute('data-yt'),b.getAttribute('aria-label'));});
var r=document.querySelector('.gos .vr');if(r)r.addEventListener('click',function(e){var x=e.target.closest('button');if(!x)return;var t=x.querySelector('span');document.querySelector('.gos .vk').innerHTML=t.innerHTML.replace('</b>','</b> · ');oynat(x.getAttribute('data-yt'),x.getAttribute('aria-label'));b.scrollIntoView({behavior:'smooth',block:'center'});});
var z=document.querySelector('.gos .gz');if(z)z.addEventListener('click',function(e){var x=e.target.closest('button');if(!x)return;var d=document.createElement('div');d.className='buyuk';d.setAttribute('role','dialog');d.setAttribute('aria-label',x.getAttribute('aria-label'));d.innerHTML='<img src="/assets/basin/kupur/'+x.getAttribute('data-g')+'.webp" alt=""><span>Kapatmak için dokunun</span>';d.addEventListener('click',function(){d.remove()});document.body.appendChild(d);dl({event:'lp_gazete',gazete:x.getAttribute('data-g')});});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){var d=document.querySelector('.buyuk');if(d)d.remove();}});})();</script>
<div class="bar rn-sticky-bar" data-cta-area="lp_bar"><a class="ara" href="tel:%(tel)s">📞 Selda Hanım'ı Ara</a><a class="w2" href="%(wa)s" target="_blank" rel="noopener" aria-label="WhatsApp">💬</a></div>''' % {
        'logo': S['logo'], 'tel': TEL, 'teltxt': TEL_TXT, 'h1': esc(P['h1']), 'h1b': esc(P['h1b']), 'alt': esc(P['alt']),
        'wa': wa, 'foto': S['foto'], 'gosteri': gosteri, 'etiket': etiketler, 'ekip': ekip, 'konular': konular, 'adimlar': adimlar,
        'not': esc(P['not'][1]), 'notb': esc(P['not'][0]), 'subeler': subeler, 'sss': sss, 'marka': esc(S['marka']),
        'kwyer': 'Çayyolu' if S['ad'] == 'cayyolu' else 'Ankara', 'saat': SAAT_TXT, 'puan': puan, 'kitaplar': kitaplar,
        'puan_kart': puan_kart, 'ekip_kart': ekip_kart, 'ofis': ofis}


def baslik(P, S):
    return '%s %s | %s' % (P['h1'], P['h1b'], S['marka'])


def aciklama(P):
    return P['alt'][:155]


# ---------------------------------------------------------------- Rojin sitesi: bağımsız çalıştırma
ROJIN_HEAD = '''<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KMR7XRJQ');</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11469933181"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','AW-11469933181',{url_passthrough:true});</script>
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="#3d1e54">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" as="image" href="%(foto)s" fetchpriority="high">
%(css)s
<script src="/assets/js/ads-conversion.js?v=5" defer></script>
<script src="/assets/js/after-hours.js?v=6" data-pos="bottom" defer></script>
<script src="/assets/js/pusula.js?v=8" defer></script>
<script src="/assets/js/vitrin.js?v=4" defer></script>
</head><body>'''


def rojin_yaz(kok):
    S = ROJIN
    for P in SAYFALAR['rojin']:
        h = ROJIN_HEAD % {'title': esc(baslik(P, S)), 'desc': esc(aciklama(P)), 'foto': S['foto'], 'css': css(S)}
        dosya = os.path.join(kok, P['yol'].strip('/'), 'index.html')
        os.makedirs(os.path.dirname(dosya), exist_ok=True)
        open(dosya, 'w', encoding='utf-8').write(h + govde(S, P) + '\n</body></html>\n')
        print('yazıldı', P['yol'])


# ---------------------------------------------------------------- Çayyolu sitesi: build.py içinden
CAYYOLU_HEAD = ROJIN_HEAD.replace('<meta name="theme-color" content="#3d1e54">', '<meta name="theme-color" content="#14264A">').replace(
    '<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png">', '<link rel="icon" href="/favicon.svg" type="image/svg+xml">').replace(
    '<script src="/assets/js/pusula.js?v=8" defer></script>',
    "<script>window.PUSULA_CFG={site:'cayyolu',foto:'/assets/img/opt/psikolog-rojin-nazik-720.webp'};</script>\n<script src=\"/assets/js/pusula.js?v=8\" defer></script>").replace(
    '<script src="/assets/js/vitrin.js?v=4" defer></script>\n', '')  # vitrin.js yalnız Rojin sitesinde


def cayyolu_yaz(kok):
    S = CAYYOLU
    yollar = []
    for P in SAYFALAR['cayyolu']:
        h = CAYYOLU_HEAD % {'title': esc(baslik(P, S)), 'desc': esc(aciklama(P)), 'foto': S['foto'], 'css': css(S)}
        dosya = os.path.join(kok, P['yol'].strip('/'), 'index.html')
        os.makedirs(os.path.dirname(dosya), exist_ok=True)
        open(dosya, 'w', encoding='utf-8').write(h + govde(S, P) + '\n</body></html>\n')
        yollar.append(P['yol'])
    return yollar


if __name__ == '__main__':
    rojin_yaz(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
