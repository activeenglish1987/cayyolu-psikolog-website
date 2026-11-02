"""Ortak 'Ekranda ve basında' şov bandı (Rojin, Çayyolu, Elif ana sayfaları).
Rakamlar Rojin /basinda-biz/ sayfasıyla aynı tutulur. Kendi içinde stil; JS yok."""
import html
E = lambda x: html.escape(x, quote=True)
TUM = 'https://www.psikologrojinnazik.com/basinda-biz/'
SAYAC = [('45', 'çevrimiçi haber'), ('19', 'gazete sayfası'), ('11', 'ulusal yayın'), ('7', 'TV ve video yayını'), ('3', 'kitap')]
LOGO = [('CNN TÜRK', 'cnnturk', 146, 120), ('Hürriyet', None, 0, 0), ('Milliyet', 'milliyet', 480, 87), ('Sabah', 'sabah', 292, 105),
        ('Cumhuriyet', None, 0, 0), ('Posta', 'posta', 307, 91), ('Akşam', 'aksam', 480, 103), ('Takvim', 'takvim', 460, 120),
        ('Vatan', 'vatan', 480, 102), ('Beyaz TV', 'beyaztv', 204, 70), ('TV8 INT', None, 0, 0)]
H = {
 'miras': ('Hürriyet', 'Şubat 2024', 'Çocuğuma miras bırakmalı mıyım?', 'https://www.hurriyet.com.tr/aile/bir-sorudan-fazlasi-cocuguma-miras-birakmali-miyim-42399121'),
 'aldatan': ('Hürriyet', 'Aralık 2023', 'Aldatan eş itiraf etmeli mi yoksa saklamalı mı?', 'https://www.hurriyet.com.tr/aile/bir-sorudan-fazlasi-aldatan-es-itiraf-etmeli-mi-yoksa-saklamali-mi-42372630'),
 'makyaj': ('Hürriyet', 'Ocak 2024', 'Partnerin makyaja, kıyafete karışması istismar mıdır?', 'https://www.hurriyet.com.tr/mahmure/yazarlar/selin-irmak-kacmaz/partnerin-makyaja-kiyafete-karismasi-istismar-midir-42396458'),
 'zit': ('Hürriyet', 'Ekim 2023', 'Zıt kutuplar birbirini çeker mi? Araştırma sonuçları ezber bozuyor', 'https://www.hurriyet.com.tr/aile/yazarlar/sedef-bati/yillardir-zit-kutuplar-birbirini-ceker-diye-biliyorduk-ama-arastirma-sonuclari-ezber-bozuyor-42343549'),
 'cocuk_aldatma': ('Hürriyet', 'Eylül 2023', 'Evlilikte aldatmalar çocukları nasıl etkiliyor?', 'https://www.hurriyet.com.tr/aile/yazarlar/sedef-bati/evlilikte-aldatmalar-cocuklari-nasil-etkiliyor-42333665'),
 'uyku': ('CNN Türk', 'Ekim 2023', 'Uyku şekliniz birçok hastalığa davetiye çıkarıyor', 'https://www.cnnturk.com/saglik/uyku-sekliniz-bircok-hastaliga-davetiye-cikariyor-2056022'),
 'stres': ('CNN Türk', 'Kasım 2022', 'Stresten nasıl kurtuluruz?', 'https://www.cnnturk.com/saglik/stresten-nasil-kurtuluruz-1853827'),
 'kaygi': ('CNN Türk', '', 'Kaygı bozukluğu nedir?', 'https://www.cnnturk.com/saglik/kaygi-bozuklugu-nedir'),
 'ergenlik': ('CNN Türk', '', 'Ergenlik dönemindeki çocukların psikolojisine dikkat', 'https://www.cnnturk.com/saglik/ergenlik-donemindeki-cocuklarin-psikolojilerine-dikkat'),
 'travma': ('Cumhuriyet', 'Kasım 2022', 'Travmalar sonrası stresten nasıl kurtuluruz?', 'https://www.cumhuriyet.com.tr/saglik/travmalar-sonrasi-stresten-nasil-kurtuluruz-2003010'),
 'cocuk_ergen': ('Cumhuriyet', 'Ekim 2022', 'Çocuklarda ve ergenlerde psikolojiye dikkat edilmeli', 'https://www.cumhuriyet.com.tr/saglik/cocuklarda-ve-ergenlerde-psikolojiye-dikkat-edilmeli-1994237'),
 'asiri': ('Sabah', 'Ocak 2023', 'Aşırı düşünmenin psikolojiye etkisi', 'https://www.sabah.com.tr/roza/ruh-sagligi/asiri-dusunmenin-psikolojiye-etkisi'),
 'sinav': ('Milliyet', '', 'Psikolog Rojin Nazik sınav stresini aşmanın yollarını anlattı', 'https://www.milliyet.com.tr/pembenar/psikolog-rojin-nazik-sinav-stresini-asmanin-yollarini-anlatti-6441751'),
 'sosyal': ('CNN Türk', 'Haziran 2022', 'Evli kişilerde sosyal medya kullanımı aile sorununa sebep oluyor', 'https://www.cnnturk.com/iyilik-saglik/iliskiler/evli-kisilerde-sosyal-medya-kullanimi-aile-sorununa-sebep-oluyor-1802509'),
}
SITE = {
 'rojin': dict(baslik='Ulusal basında <em>Psikolog Rojin Nazik</em>', kart=['miras', 'aldatan', 'makyaj', 'uyku', 'travma', 'asiri'], tum='/basinda-biz/',
               alt='Hürriyet’ten CNN Türk’e, ulusal gazetelerde ve televizyon programlarında uzman görüşleriyle.'),
 'cayyolu': dict(baslik='Kurucumuz <em>Psikolog Rojin Nazik</em> ekranda ve basında', kart=['cocuk_aldatma', 'miras', 'cocuk_ergen', 'ergenlik', 'sinav', 'aldatan'], tum=TUM,
               alt='RN Psikoloji’nin kurucusu Rojin Nazik; aile, çocuk ve ergen konularında ulusal gazetelerde ve televizyon programlarında uzman görüşleriyle yer alıyor.'),
 'elif': dict(baslik='Ekibimizin kurucusu <em>Psikolog Rojin Nazik</em> basında', kart=['makyaj', 'zit', 'asiri', 'kaygi', 'stres', 'sosyal'], tum=TUM,
               alt='Psikolog Elif Erdoğan, Rojin Nazik’in kurduğu RN Psikoloji ekibinde çalışıyor. Ekibimizin kurucusu ilişkiler, kaygı ve stres konularında ulusal basında uzman görüşleriyle yer alıyor.'),
}
CSS = ('<style>.bsov{background:linear-gradient(160deg,#1d1027 0%,#3d1e54 60%,#4a2766 100%);color:#fff;padding:64px 16px;font-family:inherit}'
 '.bsov *{box-sizing:border-box}.bsov-in{max-width:1180px;margin:0 auto}'
 '.bsov-k{font-size:12px;letter-spacing:.22em;font-weight:700;color:#D9BF83;text-align:center}'
 '.bsov h2{font-size:clamp(1.7rem,3.6vw,2.6rem);line-height:1.15;font-weight:600;text-align:center;margin:12px auto 10px;max-width:820px;color:#fff;letter-spacing:-.02em}'
 '.bsov h2 em{font-style:italic;color:#E9D3A3}'
 '.bsov-alt{text-align:center;max-width:720px;margin:0 auto;color:rgba(255,255,255,.78);font-size:16px;line-height:1.6}'
 '.bsov-unvan{display:block;width:max-content;max-width:100%;margin:18px auto 0;padding:8px 16px;border:1px solid rgba(217,191,131,.5);border-radius:999px;font-size:13.5px;color:#F3E6C6;text-align:center}'
 '.bsov-lg{list-style:none;margin:30px 0 0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:10px}'
 '.bsov-lg li{background:#fff;border-radius:12px;height:52px;padding:0 16px;display:flex;align-items:center;justify-content:center;min-width:96px}'
 '.bsov-lg img{max-height:30px;width:auto;height:auto;max-width:120px}'
 '.bsov-lg span{font:800 17px/1 Georgia,"Times New Roman",serif;color:#1d1027;letter-spacing:-.01em}'
 '.bsov-say{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:28px 0 0}'
 '.bsov-say div{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:16px 8px;text-align:center;font-size:13px;color:rgba(255,255,255,.8)}'
 '.bsov-say b{display:block;font-size:clamp(1.7rem,3.4vw,2.4rem);line-height:1.05;color:#E9D3A3;font-weight:700;margin-bottom:4px}'
 '.bsov-hb{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:28px 0 0}'
 '.bsov-hb a{display:flex;flex-direction:column;gap:8px;background:#fff;color:#1d1027;border-radius:18px;padding:18px 18px 16px;text-decoration:none;transition:transform .25s ease,box-shadow .25s ease}'
 '.bsov-hb a:hover{transform:translateY(-3px);box-shadow:0 18px 40px -18px rgba(0,0,0,.55)}'
 '.bsov-hb i{font-style:normal;font-size:11.5px;font-weight:700;letter-spacing:.06em;color:#6B3A8C;text-transform:uppercase}'
 '.bsov-hb i small{font-weight:500;color:#8a7d93;text-transform:none;letter-spacing:0;margin-left:6px}'
 '.bsov-hb b{font-size:16.5px;line-height:1.35;font-weight:600}'
 '.bsov-hb u{text-decoration:none;font-size:13px;color:#6B3A8C;margin-top:auto}'
 '.bsov-tum{display:block;width:max-content;max-width:100%;margin:26px auto 0;padding:13px 22px;border-radius:999px;background:#D9BF83;color:#1d1027!important;font-weight:700;text-decoration:none;text-align:center}'
 '@media(max-width:900px){.bsov-hb{grid-template-columns:1fr 1fr}.bsov-say{grid-template-columns:repeat(3,1fr)}}'
 '@media(max-width:560px){.bsov{padding:48px 16px}.bsov-hb{grid-template-columns:1fr}.bsov-say{grid-template-columns:repeat(2,1fr)}.bsov-say div:last-child{grid-column:span 2}.bsov-lg li{height:46px;padding:0 12px;min-width:0}.bsov-lg img{max-height:24px;max-width:96px}.bsov-hb a:nth-child(n+5){display:none}}'
 '</style>')
def bant(site, logo_yol='/assets/basin/logo/'):
    c = SITE[site]
    lg = ''.join(('<li><img src="%s%s.webp" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></li>' % (logo_yol, k, E(a), w, h)) if k else '<li><span>%s</span></li>' % E(a) for a, k, w, h in LOGO)
    say = ''.join('<div><b>%s</b>%s</div>' % (n, E(t)) for n, t in SAYAC)
    hb = ''.join('<a href="%s" target="_blank" rel="noopener"><i>%s%s</i><b>%s</b><u>Haberi oku ↗</u></a>' % (E(H[k][3]), E(H[k][0]), ('<small>%s</small>' % E(H[k][1])) if H[k][1] else '', E(H[k][2])) for k in c['kart'])
    return '<!-- BASIN-SOV:BAS -->' + CSS + ('<section class="bsov" id="ekranda-basinda" aria-label="Ekranda ve basında"><div class="bsov-in">'
            '<div class="bsov-k">EKRANDA VE BASINDA</div><h2>%s</h2><p class="bsov-alt">%s</p>'
            '<span class="bsov-unvan">Hürriyet’te: “Avrupa Birliği Psikologlar Derneği Genel Başkanı Psikolog Rojin Nazik”</span>'
            '<ul class="bsov-lg" aria-label="Yer aldığı yayınlar">%s</ul><div class="bsov-say">%s</div><div class="bsov-hb">%s</div>'
            '<a class="bsov-tum" href="%s">Tüm haberler, gazete sayfaları ve TV programları →</a></div></section><!-- BASIN-SOV:SON -->') % (c['baslik'], E(c['alt']), lg, say, hb, c['tum'])
import re
def yerlestir(s, site, capa, once=True):
    s = re.sub(r'<!-- BASIN-SOV:BAS -->.*?<!-- BASIN-SOV:SON -->', '', s, flags=re.S)
    assert s.count(capa) == 1, ('çapa', capa, s.count(capa))
    b = bant(site)
    return s.replace(capa, (b + capa) if once else (capa + b))
