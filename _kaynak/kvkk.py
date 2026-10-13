# -*- coding: utf-8 -*-
"""KVKK aydınlatma metni ve gizlilik özeti: Rojin Nazik, RN Psikoloji Çayyolu ve Elif Erdoğan sitelerinde ortak.

Veri sorumlusu üç sitede de aynıdır (psikologunubul.com.tr ile aynı işletmeci; bkz. psikologunubul src/lib/site.ts operator).
Metin sitelerin GERÇEKTE yaptığına göre yazıldı (13 Ekim 2026):
  - Telefon ve WhatsApp ile iletişim; mesai dışı "sizi arayalım" ve "Soru sorun" kutusu telefon numarasını
    psikologunubul paneline (aynı işletmecinin sistemi) gönderir.
  - "Yol haritası" aracı yalnız kimlik içermeyen seçimleri gönderir, kayıt tutmaz.
  - Google Ads ölçümü (gtag/GTM, çerezler, reklam tıklama kimliği cihazda 90 gün), YouTube videosu yalnız oynatılınca yüklenir.
Bu dosya değişince: Rojin'de  python3 _araclar/kvkk.py ; Çayyolu'da build.py kopyayı (_kaynak/kvkk.py) kullanır.
Hukuki metin: yayından sonra avukat görüşüne sunulmalıdır.
"""
import html, os, re, sys

VS = {
    'unvan': 'Net Aktif Eğitim Hizmetleri Turizm Organizasyon İnşaat Sanayi ve Ticaret Ltd. Şti.',
    'adres': 'Meşrutiyet Mah. Atatürk Bulvarı No:127/8, Çankaya / Ankara',
    'vkn': '6310652210', 'vd': 'Mithatpaşa Vergi Dairesi',
    'tel': '0552 418 79 73',
}
GUNCELLEME = '13 Ekim 2026'
esc = lambda s: html.escape(s, quote=True)


def kvkk_govde(site_adi, alan, eposta=None):
    """<article> içine konacak HTML (h2'ler ve paragraflar)."""
    e = ('ya da <a href="mailto:%s">%s</a> adresine e-posta ile ' % (eposta, eposta)) if eposta else ''
    return '''<p>Bu metin, 6698 sayılı Kişisel Verilerin Korunması Kanunu'nun (KVKK) 10. maddesi uyarınca, %(site)s (%(alan)s) internet sitesini ziyaret eden ve bizimle telefon, WhatsApp ya da site üzerinden iletişime geçen kişileri bilgilendirmek amacıyla hazırlanmıştır. Son güncelleme: %(tarih)s.</p>
<h2>Veri sorumlusu</h2>
<p>%(unvan)s<br>Adres: %(adres)s<br>Vergi no: %(vkn)s (%(vd)s) · Telefon: <a href="tel:+905524187973">%(tel)s</a></p>
<h2>Hangi kişisel verileri işliyoruz?</h2>
<ul>
<li><strong>İletişim bilgileri:</strong> bizi aradığınızda ya da WhatsApp'tan yazdığınızda telefon numaranız, paylaşırsanız adınız ve mesajınız; mesai dışında "sizi arayalım" ya da "Soru sorun" kutusuna yazdığınız telefon numarası ve aranmak istediğiniz zaman.</li>
<li><strong>Randevu bilgileri:</strong> görüşme tercihiniz (kimin için, hangi şube ya da online, uygun gün ve saat) ve randevu sürecine ilişkin notlar.</li>
<li><strong>Sağlık verisi niteliğinde olabilecek bilgiler:</strong> görüşme talebiniz sırasında kendi isteğinizle paylaştığınız, destek almak istediğiniz konuya ilişkin bilgiler. Bu bilgiler KVKK'nın 6. maddesi kapsamında özel nitelikli kişisel veri sayılabilir; yalnızca randevu sürecinde ve gizlilik ilkesiyle işlenir, reklam ya da ölçüm hizmetlerine hiçbir zaman gönderilmez.</li>
<li><strong>Ziyaret ve kaynak bilgileri:</strong> siteye hangi sayfadan, hangi reklam ya da kampanya üzerinden geldiğiniz (reklam tıklama kimliği ve kampanya parametreleri), tıkladığınız arama ve WhatsApp düğmeleri, tarayıcı ve cihaz bilgileri ile IP adresi.</li>
</ul>
<p>Sitedeki "yol haritası" aracında yaptığınız seçimler (kimin için, konu, yaş aralığı, görüşme yeri) ad, telefon ya da başka bir kimlik bilgisi içermez ve kaydedilmez.</p>
<h2>Hangi amaçlarla işliyoruz?</h2>
<ul>
<li>Talebinize dönüş yapmak, size uygun psikoloğu, şubeyi ve görüşme saatini belirlemek ve randevu sürecini yürütmek,</li>
<li>Görüşmelere ilişkin hizmetin sunulması ve kayıtların mevzuata uygun tutulması,</li>
<li>Sitenin güvenliğini sağlamak, mükerrer ve kötüye kullanım amaçlı talepleri önlemek,</li>
<li>Reklamlarımızın sonucunu ölçmek (ör. bir reklamdan sonra arama düğmesine tıklanıp tıklanmadığı) ve sitenin işleyişini iyileştirmek,</li>
<li>Hukuki yükümlülüklerimizi yerine getirmek ve yetkili kurumların taleplerini karşılamak.</li>
</ul>
<h2>Hukuki sebepler ve toplama yöntemi</h2>
<p>Kişisel verileriniz; telefon, WhatsApp, site üzerindeki formlar ve çerezler aracılığıyla, kısmen otomatik yollarla toplanır. İletişim ve randevu bilgileri, bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması (KVKK m.5/2-c), hukuki yükümlülüğümüzü yerine getirmemiz (m.5/2-ç) ve temel hak ve özgürlüklerinize zarar vermemek kaydıyla meşru menfaatimiz (m.5/2-f) hukuki sebeplerine dayanılarak işlenir. Sağlık verisi niteliğindeki bilgiler, KVKK m.6'da sayılan şartlar çerçevesinde, gerektiğinde açık rızanıza dayanılarak işlenir. Ölçüm ve reklam amaçlı çerezler ile ziyaret bilgileri, ilgili mevzuatın öngördüğü hukuki sebeplere dayanılarak işlenir.</p>
<h2>Kimlere aktarıyoruz?</h2>
<ul>
<li><strong>Ekibimiz:</strong> talebiniz yalnızca randevu sürecinde görev alan danışan asistanı ve ilgili psikolog tarafından görülür. Mesai dışı talepler, aynı veri sorumlusuna ait randevu yönetim sistemine (psikologunubul.com.tr) kaydedilir.</li>
<li><strong>Hizmet sağlayıcılar:</strong> sitenin barındırma hizmeti; reklam ölçümü için Google (Google Ads); WhatsApp'tan yazmayı seçerseniz Meta Platforms (WhatsApp); sitedeki bir videoyu oynatırsanız YouTube (Google). Bu sağlayıcıların bir kısmının sunucuları yurt dışında bulunduğundan, bu hizmetlerin kullanımı KVKK'nın 9. maddesi kapsamında yurt dışına aktarım niteliği taşıyabilir.</li>
<li><strong>Yetkili kurumlar:</strong> yalnızca hukuki zorunluluk hâlinde ve talep edilen ölçüde.</li>
</ul>
<p>Kişisel verileriniz satılmaz ve pazarlama amacıyla üçüncü kişilerle paylaşılmaz.</p>
<h2>Ne kadar süre saklıyoruz?</h2>
<p>Randevuya dönüşmeyen talepler en geç 6 ay içinde silinir veya anonim hâle getirilir. Reklam kaynağı bilgisi (tıklama kimliği ve kampanya parametreleri) yalnızca kendi cihazınızın tarayıcı belleğinde, en fazla 90 gün tutulur. Diğer kayıtlar, ilgili mevzuatta öngörülen süreler boyunca saklanır ve bu sürelerin sonunda silinir, yok edilir veya anonim hâle getirilir.</p>
<h2>Çerezler</h2>
<p>Sitede, temel işleyiş için gerekli olanların yanında Google Ads ölçüm çerezleri kullanılır. Videolar, siz oynat düğmesine basana kadar yüklenmez. Tarayıcınızın ayarlarından çerezleri silebilir veya engelleyebilirsiniz; bu durumda sitenin bazı özellikleri beklendiği gibi çalışmayabilir.</p>
<h2>Haklarınız</h2>
<p>KVKK'nın 11. maddesi uyarınca; kişisel verilerinizin işlenip işlenmediğini öğrenme, işlenmişse buna ilişkin bilgi talep etme, işlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme, yurt içinde veya yurt dışında aktarıldığı üçüncü kişileri bilme, eksik veya yanlış işlenmişse düzeltilmesini, silinmesini veya yok edilmesini isteme, bu işlemlerin aktarıldığı üçüncü kişilere bildirilmesini isteme, münhasıran otomatik sistemlerle analiz edilmesi sonucunda aleyhinize bir sonuç çıkmasına itiraz etme ve kanuna aykırı işleme nedeniyle zarara uğramanız hâlinde zararın giderilmesini talep etme haklarına sahipsiniz.</p>
<p>Başvurularınızı, Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ'e uygun olarak, yukarıdaki adrese yazılı olarak %(e)siletebilirsiniz. Başvurunuz en geç 30 gün içinde ücretsiz olarak sonuçlandırılır.</p>''' % dict(VS, site=esc(site_adi), alan=esc(alan), tarih=GUNCELLEME, e=e)


def gizlilik_govde(kvkk_yolu):
    return '''<ul>
<li>Sizden yalnızca dönüş yapabilmemiz için gereken bilgiyi isteriz; çoğu zaman bu yalnızca telefon numaranızdır.</li>
<li>Görüşmelerde konuşulanlar gizlidir; yasal zorunluluk ve can güvenliği gibi istisnalar ilk görüşmede açıkça anlatılır.</li>
<li>Destek almak istediğiniz konu gibi sağlıkla ilgili bilgiler hiçbir zaman reklam ya da ölçüm hizmetlerine gönderilmez; reklam ölçümüne yalnızca "arama düğmesine tıklandı" gibi içeriksiz olaylar gider.</li>
<li>"Yol haritası" aracındaki seçimleriniz kimlik bilgisi içermez ve kaydedilmez.</li>
<li>Kişisel verileriniz satılmaz ve pazarlama amacıyla üçüncü kişilerle paylaşılmaz.</li>
</ul>
<p>Ayrıntılar ve haklarınız için: <a href="%s">KVKK aydınlatma metni</a>.</p>''' % kvkk_yolu


# ---------------------------------------------------------------- Rojin sitesi: mevcut sayfaların içeriğini yenile
def rojin_yaz(kok):
    for yol, baslik, lead, govde in [
        ('kvkk', 'KVKK Aydınlatma Metni', 'Kişisel verilerinizin hangi amaçlarla ve nasıl işlendiğine ilişkin bilgilendirme.', kvkk_govde('Psikolog Rojin Nazik', 'psikologrojinnazik.com')),
        ('gizlilik', 'Gizlilik Politikası', 'Gizliliğinize nasıl yaklaştığımızın kısa özeti.', gizlilik_govde('/kvkk/')),
    ]:
        p = os.path.join(kok, yol, 'index.html'); h = open(p, encoding='utf-8').read()
        yeni = re.sub(r'(<p class="lead">).*?(</p>)', lambda m: m.group(1) + esc(lead) + m.group(2), h, count=1, flags=re.S)
        yeni = re.sub(r'(<article class="article container-prose">).*?(</article>)', lambda m: m.group(1) + govde + m.group(2), yeni, count=1, flags=re.S)
        assert yeni != h or govde in h, p
        open(p, 'w', encoding='utf-8').write(yeni)
        print('yazıldı', p)


if __name__ == '__main__':
    rojin_yaz(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
