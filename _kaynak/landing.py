# -*- coding: utf-8 -*-
"""Anahtar kelime sayfaları (semt ve hizmet odaklı).
Search Console'da zayıf kalan aramalar için yazılmış özgün içerikler.
build.py tarafından içe aktarılır."""

# Ortak sözlük alanları:
# path, kw (ana arama), h1, title, desc, lead, body (HTML), faqs [(soru, cevap)], near [(ad, yol)]

LANDINGS = [
{
 'path': '/umitkoy-psikolog/',
 'kw': 'Ümitköy psikolog',
 'h1': 'Ümitköy Psikolog',
 'title': 'Ümitköy Psikolog | RN Psikoloji – Yüz Yüze Danışmanlık, Randevu',
 'desc': "Ümitköy'e birkaç dakika mesafedeki ofisimizde yetişkin, çift, çocuk ve ergen görüşmeleri. Pazartesi – Cumartesi 09:00 – 20:00. Randevu: 0552 418 79 73.",
 'lead': "Ümitköy'de yaşıyor ya da çalışıyorsanız, Dumlupınar Bulvarı üzerindeki ofisimiz size çok yakın. Yetişkin, çift, çocuk ve ergen görüşmeleri için hafta içi ve cumartesi randevu verebiliyoruz.",
 'body': '''
<h2>Ümitköy'de psikolog arayanlar için kısa bilgi</h2>
<p>Ümitköy; üniversitelere, iş merkezlerine ve Eskişehir Yolu'na yakınlığıyla hem öğrencilerin hem de yoğun tempoda çalışan ailelerin tercih ettiği bir semt. Bu tempo; iş stresi, uykusuzluk, ilişkide iletişim sorunları ya da çocukların okul uyumu gibi konuları gündelik hayatın parçası hâline getirebiliyor. RN Psikoloji Çayyolu şubesi, Ümitköy'den gelen danışanlarımızın trafiğe takılmadan, uzun yol yapmadan ulaşabileceği bir konumda.</p>
<p>Görüşmeler randevu ile ve yüz yüze yapılır. İlk adımı atmak için telefonla aramanız ya da WhatsApp'tan kısa bir mesaj bırakmanız yeterli; başvuru nedeninize göre size uygun uzmanı ve saati birlikte belirleriz.</p>
<div class="route-box"><h3>Ümitköy'den ofisimize ulaşım</h3><ul>
<li>Ofisimiz Konutkent'te, <b>Dumlupınar Bulvarı No:399</b> adresinde, Ümitköy'ün hemen batısında yer alır.</li>
<li>Özel araçla Eskişehir Yolu üzerinden kısa bir sürüş mesafesindedir; binada <b>ücretsiz otopark</b> vardır.</li>
<li>Toplu taşımada Eskişehir Yolu güzergâhındaki metro ve otobüs hatlarını kullanabilirsiniz.</li>
</ul></div>
<h2>Ümitköy'den gelen danışanlarımızın en sık başvuru nedenleri</h2>
<ul class="topic-grid">
<li><b>Kaygı ve stres:</b> iş yükü, sınav dönemi, sürekli tetikte olma hâli</li>
<li><b>İlişki ve evlilik:</b> iletişim kopukluğu, güven, tekrar eden tartışmalar</li>
<li><b>Ergenlik dönemi:</b> okul motivasyonu, ekran kullanımı, aileyle çatışma</li>
<li><b>Çocuklarda uyum:</b> okula başlama, kardeş kıskançlığı, öfke nöbetleri</li>
<li><b>Yaşam geçişleri:</b> taşınma, iş değişikliği, ayrılık ve yas</li>
<li><b>Özgüven:</b> kendini ifade etme, sınır koyma, sosyal ortamlarda zorlanma</li>
</ul>
%(cta)s
<h2>Size uygun uzmanı nasıl belirliyoruz?</h2>
<p>Ofisimizde görüşme yürüten psikologlarımız farklı yaş gruplarında ve farklı konularda deneyim sahibidir. Yetişkin bireysel görüşmeler ve çift çalışmaları için kurucu psikoloğumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a>; ergen, çift görüşmeleri ve oyun terapisi için <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a>; çocuk ve ergen görüşmeleri için <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> ile randevu alabilirsiniz. Hangisinin size uygun olduğundan emin değilseniz, kısaca durumunuzu anlatmanız yeterli.</p>
<h2>İlk görüşmede neler olur?</h2>
<p>İlk görüşme bir tanışma ve değerlendirme görüşmesidir. Sizi buraya getiren konu, ne zamandır sürdüğü, günlük hayatınızı nasıl etkilediği ve görüşmelerden beklentileriniz konuşulur. Görüşmenin sonunda nasıl bir yol izleneceği, görüşmelerin sıklığı ve süreç hakkında net bir bilgi alırsınız. Her şey gizlilik ilkesi çerçevesinde yürütülür.</p>
<h2>Ümitköy psikolog ücretleri</h2>
<p>Görüşme ücretleri uzmana ve görüşme türüne (bireysel, çift, çocuk-ergen) göre değişir. Güncel ücret bilgisini WhatsApp'tan yazarak ya da arayarak hemen öğrenebilirsiniz; telefonda size uygun gün ve saati de birlikte planlarız.</p>
''',
 'faqs': [
  ("Ümitköy'e en yakın ofisiniz nerede?", "Ofisimiz Konutkent'te, Dumlupınar Bulvarı No:399 Kat:28 Daire:121 adresindedir. Ümitköy'e birkaç dakikalık sürüş mesafesindedir ve ücretsiz otopark vardır."),
  ("Ümitköy'den akşam saatlerinde görüşmeye gelebilir miyim?", "Evet. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında yapılır; iş çıkışı saatleri için erken aramanızı öneririz."),
  ("Ergen çocuğum için randevu alabilir miyim?", "Evet. Ergen görüşmelerinde önce ebeveynle kısa bir ön görüşme yapılır, ardından gencin kendisiyle görüşmeler planlanır."),
  ("Çift olarak birlikte gelebilir miyiz?", "Evet. Çift görüşmeleri iki tarafın birlikte katılımıyla yapılır; gerektiğinde bireysel görüşmeler de planlanabilir."),
  ("Randevu için ne yapmam gerekiyor?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz. Kısaca başvuru nedeninizi paylaşmanız yeterli."),
 ],
},
{
 'path': '/yasamkent-psikolog/',
 'kw': 'Yaşamkent psikolog',
 'h1': 'Yaşamkent Psikolog',
 'title': 'Yaşamkent Psikolog | RN Psikoloji Yaşamkent Ofisi – Randevu',
 'desc': "Yaşamkent ofisimizde yüz yüze psikolojik danışmanlık: yetişkin, çift, aile, çocuk ve ergen. Ücretsiz otopark. Pazartesi – Cumartesi 09:00 – 20:00. Tel: 0552 418 79 73.",
 'lead': "RN Psikoloji'nin Yaşamkent ofisi, Dumlupınar Bulvarı üzerinde, Yaşamkent ve Konutkent'in kesiştiği noktada. Yakınınızda, randevulu ve yüz yüze psikolojik danışmanlık.",
 'body': '''
<h2>Yaşamkent'te, yürüme ve kısa sürüş mesafesinde</h2>
<p>Yaşamkent'te psikolog ararken çoğu kişi için en önemli iki şey, güvenilir bir uzman ve düzenli gelebileceği bir konum. Görüşmelerin etkili olması için süreklilik önemli; bu yüzden eve ya da işe yakın bir ofis, sürecin aksamadan devam etmesini kolaylaştırır. Yaşamkent ofisimiz tam da bu ihtiyaç için burada.</p>
<p>Ofisimizde yetişkin bireysel görüşmeler, çift ve aile görüşmeleri ile çocuk ve ergen görüşmeleri yapılır. Sakin, aydınlık ve mahremiyete uygun seans odalarımızda, randevu saatinize göre sizi bekleme yaşatmadan karşılamaya özen gösteririz.</p>
<div class="route-box"><h3>Ofis bilgileri</h3><ul>
<li><b>Adres:</b> Konutkent, Dumlupınar Blv. No:399 Kat:28 Daire:121, Çankaya / Ankara</li>
<li><b>Görüşme günleri:</b> Pazartesi – Cumartesi, 09:00 – 20:00</li>
<li><b>Otopark:</b> Ücretsiz otopark mevcut</li>
<li>Yaşamkent'in tüm sitelerinden ve Konutkent'ten kısa sürede ulaşılır.</li>
</ul></div>
<h2>Yaşamkent ofisimizde hangi konularda destek alabilirsiniz?</h2>
<ul class="topic-grid">
<li><b>Bireysel danışmanlık:</b> kaygı, stres, özgüven, öfke yönetimi</li>
<li><b>Çift ve evlilik:</b> iletişim, güven, evlilik öncesi hazırlık</li>
<li><b>Aile görüşmeleri:</b> ebeveynlik, sınırlar, aile içi iletişim</li>
<li><b>Çocuk:</b> oyun terapisi, okul uyumu, duygu düzenleme</li>
<li><b>Ergen:</b> sınav kaygısı, akran ilişkileri, kimlik arayışı</li>
<li><b>Zor dönemler:</b> boşanma, kayıp ve yas, iş değişikliği</li>
</ul>
%(cta)s
<h2>Neden RN Psikoloji?</h2>
<p>RN Psikoloji, kurucusu <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a>'in uzun yıllara dayanan danışmanlık deneyimi üzerine kurulu. Rojin Nazik'in televizyon programlarına katılımları, gazete röportajları ve yayımlanmış kitapları, psikolojiyi herkesin anlayabileceği bir dille aktarma çabasının parçası. Ekibimizde <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> ve <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> de görüşme yürütüyor.</p>
<p>Her başvuruyu kendi koşulları içinde değerlendiriyor, hazır kalıplar yerine kişiye özel bir görüşme planı oluşturuyoruz. Bilimsel temelli yöntemleri esas alıyor, gizliliği ve etik ilkeleri sürecin merkezinde tutuyoruz.</p>
<h2>Randevu nasıl alınır?</h2>
<p>Telefonla aradığınızda ya da WhatsApp'tan yazdığınızda size birkaç kısa soru sorarız: görüşmeyi kimin için istediğiniz, genel olarak hangi konuda destek aradığınız ve hangi gün ve saatlerin size uyduğu. Buna göre uygun uzman ve randevu saati belirlenir. Mesai dışında yazdığınız mesajlara ilk mesai saatinde dönüş yapılır.</p>
''',
 'faqs': [
  ("Yaşamkent ofisiniz tam olarak nerede?", "Konutkent, Dumlupınar Bulvarı No:399 Kat:28 Daire:121, Çankaya / Ankara adresindeyiz. Yol tarifi için sayfadaki “Yol tarifi al” bağlantısını kullanabilirsiniz."),
  ("Yaşamkent'te hangi günler görüşme yapılıyor?", "Pazartesi – Cumartesi, 09:00 – 20:00 saatleri arasında randevu ile görüşme yapılır."),
  ("Otopark var mı?", "Evet, ücretsiz otopark mevcuttur."),
  ("Çocuğum için hangi uzmanla görüşmeliyim?", "Çocuk ve ergen görüşmeleri için Psikolog Elif Erdoğan ve Klinik Psikolog Hazal Akşahin ile randevu alabilirsiniz. Kısaca durumu paylaşırsanız size uygun uzmanı öneririz."),
  ("Ücret bilgisini nasıl öğrenebilirim?", "WhatsApp'tan yazarak ya da 0552 418 79 73 numarasını arayarak güncel ücret bilgisini öğrenebilirsiniz."),
 ],
},
{
 'path': '/konutkent-psikolog/',
 'kw': 'Konutkent psikolog',
 'h1': 'Konutkent Psikolog',
 'title': 'Konutkent Psikolog | RN Psikoloji – Dumlupınar Bulvarı, Randevu',
 'desc': "Konutkent'te, Dumlupınar Bulvarı üzerindeki ofisimizde yetişkin, çift, çocuk ve ergen görüşmeleri. Pazartesi – Cumartesi 09:00 – 20:00. Randevu: 0552 418 79 73.",
 'lead': "Ofisimiz Konutkent'in içinde, Dumlupınar Bulvarı No:399'da. Konutkent sitelerinden birkaç dakikada ulaşabileceğiniz, sakin ve mahremiyete önem veren bir ortamda görüşüyoruz.",
 'body': '''
<h2>Konutkent'te mahallenizdeki psikolog</h2>
<p>Konutkent, site yaşamının yoğun olduğu, ailelerin ve çalışan profesyonellerin bir arada yaşadığı bir bölge. Böyle bir çevrede psikolojik destek almak isteyen birçok kişi, hem yakın hem de gizliliğe özen gösterilen bir yer arıyor. RN Psikoloji Çayyolu şubesi Konutkent'in tam içinde; randevu saatleri, danışanların birbirleriyle karşılaşmayacağı şekilde planlanır.</p>
<p>Yakınlık, psikolojik danışmanlıkta küçümsenmeyecek bir avantajdır: yol ve trafik yükü azaldıkça görüşmelere düzenli devam etmek kolaylaşır. Konutkent'ten gelen danışanlarımızın çoğu iş çıkışı ya da cumartesi saatlerini tercih ediyor.</p>
<div class="route-box"><h3>Konutkent'ten ulaşım</h3><ul>
<li><b>Adres:</b> Dumlupınar Blv. No:399 Kat:28 Daire:121, Konutkent</li>
<li>Konutkent sitelerinden birkaç dakikalık yürüme veya sürüş mesafesi</li>
<li>Ücretsiz otopark</li>
</ul></div>
<h2>Konutkent'ten en sık başvurulan konular</h2>
<ul class="topic-grid">
<li><b>İş ve kariyer stresi:</b> tükenmişlik, performans kaygısı</li>
<li><b>Ebeveynlik:</b> sınır koyma, ekran süresi, uyku düzeni</li>
<li><b>Çift ilişkisi:</b> çocuk sonrası değişen ilişki dengesi</li>
<li><b>Ergenler:</b> okul başarısı, sınav dönemi, sosyal medya</li>
<li><b>Kaygı:</b> panik hissi, sürekli endişe, beden duyumlarına odaklanma</li>
<li><b>Kayıp ve yas:</b> bir yakının kaybı sonrası uyum</li>
</ul>
%(cta)s
<h2>Görüşmeler nasıl ilerler?</h2>
<p>İlk görüşmede sizi dinler, başvuru nedeninizi ve beklentilerinizi birlikte netleştiririz. Sonraki görüşmelerde belirlenen hedefler doğrultusunda, kişiye özel ve bilimsel temelli bir yol izlenir. Görüşmelerin sıklığı ve süreci ihtiyacınıza göre planlanır; her aşamada sorularınızı rahatça sorabilirsiniz.</p>
<h2>Uzmanlarımız</h2>
<p>Kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> yetişkin, çift ve aile görüşmeleri yürütür. <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> yetişkin, ergen ve çift görüşmeleri ile oyun terapisi alanında; <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> çocuk, ergen ve yetişkin görüşmelerinde çalışır.</p>
''',
 'faqs': [
  ("Konutkent'te ofisiniz hangi binada?", "Dumlupınar Bulvarı No:399, Kat:28, Daire:121 adresindeyiz. Yol tarifi bağlantısıyla doğrudan navigasyon başlatabilirsiniz."),
  ("Cumartesi günü görüşme yapılıyor mu?", "Evet, Cumartesi de dahil olmak üzere Pazartesi – Cumartesi 09:00 – 20:00 arasında randevu verilir."),
  ("Görüşmeler gizli mi?", "Evet. Görüşmelerde konuşulanlar etik ilkeler ve gizlilik çerçevesinde korunur."),
  ("Çocuk ve ergen görüşmesi yapıyor musunuz?", "Evet. Çocuklarla oyun terapisi yaklaşımıyla, ergenlerle yaşlarına uygun yöntemlerle çalışılır; ebeveyn görüşmeleri de sürecin parçasıdır."),
 ],
},
{
 'path': '/incek-psikolog/',
 'kw': 'İncek psikolog',
 'h1': 'İncek Psikolog',
 'title': 'İncek Psikolog | RN Psikoloji – Çocuk, Ergen, Aile ve Yetişkin',
 'desc': "İncek'e yakın ofisimizde çocuk, ergen, aile, çift ve yetişkin görüşmeleri. Ücretsiz otopark, Pazartesi – Cumartesi 09:00 – 20:00. Randevu: 0552 418 79 73.",
 'lead': "İncek'ten gelen danışanlarımız için Yaşamkent ofisimiz kısa bir sürüş mesafesinde. Özellikle çocuklu aileler, çiftler ve yetişkinler için randevulu, yüz yüze psikolojik danışmanlık.",
 'body': '''
<h2>İncek'te yaşayan aileler için psikolojik destek</h2>
<p>İncek, son yıllarda genç ailelerin ve çocuklu hanelerin yoğun olarak yerleştiği, doğayla iç içe ama şehir merkezine uzak bir yaşam alanı. Bu mesafe, gündelik ihtiyaçlar için olduğu gibi psikolojik destek için de yakın bir seçenek bulmayı önemli hâle getiriyor. Yaşamkent ofisimiz, İncek'ten merkeze inmeden ulaşabileceğiniz bir konumda.</p>
<p>Taşınma ve yeni bir çevreye uyum, okul değişikliği, iki ebeveynin de çalıştığı yoğun bir aile düzeni ya da çift ilişkisinde biriken yorgunluk; İncek'ten gelen danışanlarımızla en sık konuştuğumuz konular arasında.</p>
<div class="route-box"><h3>İncek'ten ofisimize</h3><ul>
<li>Ofisimiz Konutkent, Dumlupınar Bulvarı No:399'dadır.</li>
<li>İncek'ten Yaşamkent yönüne doğru kısa bir sürüşle ulaşılır; şehir merkezi trafiğine girmeniz gerekmez.</li>
<li>Ücretsiz otopark mevcuttur, randevunuza zamanında yetişmeniz kolaylaşır.</li>
</ul></div>
<h2>İncek'ten başvuran ailelerin en sık ihtiyaçları</h2>
<ul class="topic-grid">
<li><b>Okul öncesi ve ilkokul çağı:</b> uyum, ayrılık kaygısı, öfke</li>
<li><b>Ergenlik:</b> motivasyon, ekran bağımlılığı, sınav stresi</li>
<li><b>Ebeveyn danışmanlığı:</b> tutarlı sınırlar, ortak tutum</li>
<li><b>Çift ilişkisi:</b> iş ve ev yükünün paylaşımı, iletişim</li>
<li><b>Yetişkin:</b> kaygı, yalnızlık hissi, yaşam geçişleri</li>
<li><b>Aile görüşmeleri:</b> kardeş ilişkileri, aile içi çatışma</li>
</ul>
%(cta)s
<h2>Çocuğunuz için doğru uzman</h2>
<p>Çocuk ve ergen görüşmelerinde ilk adım genellikle ebeveynle yapılan bir ön görüşmedir. Çocuğunuzun gelişim öyküsü, okul ve evdeki durumu dinlenir; ardından çocuğunuzla yaşına uygun yöntemlerle, küçük yaş grubunda oyun terapisi yaklaşımıyla görüşmeler planlanır. Bu alanda <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> ve <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> ile çalışabilirsiniz. Yetişkin, çift ve aile görüşmeleri için kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> ile randevu alabilirsiniz.</p>
<h2>Randevu ve bilgi</h2>
<p>Hangi uzmanın size uygun olduğunu bilmiyorsanız sorun değil. Arayın ya da WhatsApp'tan kısaca yazın; ihtiyacınıza göre yönlendirme yapalım. Güncel ücret bilgisini de aynı şekilde öğrenebilirsiniz.</p>
''',
 'faqs': [
  ("İncek'ten ofisinize ne kadar sürede ulaşırım?", "Trafiğe bağlı olarak değişmekle birlikte, İncek'ten Konutkent'teki ofisimize kısa bir sürüşle ulaşılır. Ücretsiz otopark mevcuttur."),
  ("Çocuğum için ilk görüşmeye kim gelmeli?", "Genellikle ilk görüşme ebeveynlerle yapılır. Çocuğunuzla görüşmeler bu ön değerlendirmeden sonra planlanır."),
  ("Oyun terapisi yapıyor musunuz?", "Evet. Küçük yaştaki çocuklarla oyun terapisi yaklaşımıyla çalışılır."),
  ("Hafta sonu randevu var mı?", "Cumartesi günleri de 09:00 – 20:00 arasında randevu verilmektedir."),
 ],
},
{
 'path': '/beysukent-psikolog/',
 'kw': 'Beysukent psikolog',
 'h1': 'Beysukent Psikolog',
 'title': 'Beysukent Psikolog | RN Psikoloji – Yetişkin, Öğrenci, Çift',
 'desc': "Beysukent'e yakın ofisimizde yetişkin, üniversite öğrencisi, çift ve ergen görüşmeleri. Pazartesi – Cumartesi 09:00 – 20:00. Randevu: 0552 418 79 73.",
 'lead': "Beysukent'e yakın Yaşamkent ofisimizde; yetişkinler, üniversite öğrencileri, çiftler ve ergenler için randevulu, yüz yüze psikolojik danışmanlık.",
 'body': '''
<h2>Beysukent ve çevresinden gelen danışanlarımız</h2>
<p>Beysukent, üniversite yerleşkelerine yakınlığıyla öğrencilerin, akademisyenlerin ve ailelerin bir arada yaşadığı bir semt. Bu çeşitlilik, psikolojik destek ihtiyaçlarına da yansıyor: bir yanda sınav ve gelecek kaygısı yaşayan gençler, diğer yanda iş ve aile sorumluluklarını dengelemeye çalışan yetişkinler.</p>
<p>RN Psikoloji Çayyolu şubesi, Beysukent'e yakın konumuyla her iki gruba da ulaşılabilir bir seçenek sunuyor. Görüşmeler yüz yüze, randevu ile ve gizlilik ilkesine bağlı kalınarak yapılır.</p>
<div class="route-box"><h3>Beysukent'ten ulaşım</h3><ul>
<li>Ofisimiz Konutkent, Dumlupınar Bulvarı No:399 Kat:28'dedir.</li>
<li>Beysukent'ten Eskişehir Yolu bağlantısıyla kısa bir sürüş mesafesindedir.</li>
<li>Ücretsiz otopark mevcuttur.</li>
</ul></div>
<h2>Beysukent'ten en sık başvurulan konular</h2>
<ul class="topic-grid">
<li><b>Üniversite dönemi:</b> uyum, yalnızlık, akademik baskı</li>
<li><b>Gelecek kaygısı:</b> kariyer seçimi, karar vermede zorlanma</li>
<li><b>Sınav kaygısı:</b> lise ve üniversite sınav dönemleri</li>
<li><b>İlişkiler:</b> romantik ilişkiler, ayrılık, bağlanma</li>
<li><b>Yetişkin:</b> iş stresi, tükenmişlik, özgüven</li>
<li><b>Aile:</b> ebeveyn-genç iletişimi, evden ayrılma süreci</li>
</ul>
%(cta)s
<h2>Genç yetişkinlerle çalışırken</h2>
<p>Üniversite yılları; bağımsızlaşma, kimlik ve ilişkiler açısından yoğun bir dönem. Bu dönemde yaşanan zorlanmalar çoğu zaman “geçer” diye ertelenir. Oysa erken dönemde alınan destek; kaygıyla baş etme, ilişkilerde sağlıklı sınırlar kurma ve karar verme becerilerini güçlendirebilir. Görüşmelerde gencin kendi hedefleri merkeze alınır.</p>
<h2>Uzman seçimi ve randevu</h2>
<p>Yetişkin ve çift görüşmeleri için <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a>, ergen ve genç yetişkinlerle çalışmak için <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> ile görüşebilirsiniz. Randevu için arayabilir veya WhatsApp'tan yazabilirsiniz.</p>
''',
 'faqs': [
  ("Beysukent'e en yakın ofisiniz nerede?", "Konutkent, Dumlupınar Bulvarı No:399 Kat:28 Daire:121 adresindeki Yaşamkent ofisimiz Beysukent'e kısa bir sürüş mesafesindedir."),
  ("Üniversite öğrencileriyle görüşüyor musunuz?", "Evet. Uyum, kaygı, ilişkiler ve gelecek planlaması gibi konularda genç yetişkinlerle görüşmeler yapılır."),
  ("Sınav kaygısı için destek alabilir miyim?", "Evet. Lise ve üniversite öğrencilerinde sınav kaygısı sık başvuru nedenlerindendir; kaygıyı yönetmeye yönelik çalışılır."),
  ("Randevu almak için ne yapmalıyım?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ],
},
{
 'path': '/alacaatli-psikolog/',
 'kw': 'Alacaatlı psikolog',
 'h1': 'Alacaatlı Psikolog',
 'title': 'Alacaatlı Psikolog | RN Psikoloji – Yüz Yüze Danışmanlık',
 'desc': "Alacaatlı'ya yakın Yaşamkent ofisimizde yetişkin, çift, aile, çocuk ve ergen görüşmeleri. Ücretsiz otopark. Randevu: 0552 418 79 73.",
 'lead': "Alacaatlı'dan gelen danışanlarımız için Yaşamkent ofisimiz kısa bir mesafede. Yetişkin, çift, aile, çocuk ve ergen görüşmeleri; Pazartesi – Cumartesi.",
 'body': '''
<h2>Alacaatlı'dan kısa mesafede psikolog</h2>
<p>Alacaatlı, geniş bahçeli evleri ve yeni konut projeleriyle sakin bir yaşam arayan ailelerin tercih ettiği bir bölge. Sakin yaşamın içinde de iş yükü, çocukların okul dönemleri, çift ilişkisindeki gerginlikler ya da yaşam değişiklikleri zorlayıcı olabiliyor. Destek almak istediğinizde uzun yol gitmeden ulaşabileceğiniz bir ofis, sürece düzenli devam etmenizi kolaylaştırır.</p>
<p>RN Psikoloji'nin Yaşamkent ofisi, Alacaatlı'dan kısa bir sürüşle ulaşılabilen Konutkent'te. Görüşmeler randevu ile, yüz yüze ve gizlilik ilkesi çerçevesinde yapılır.</p>
<div class="route-box"><h3>Alacaatlı'dan ofisimize</h3><ul>
<li><b>Adres:</b> Dumlupınar Blv. No:399 Kat:28 Daire:121, Konutkent</li>
<li>Alacaatlı'dan Yaşamkent üzerinden kısa bir sürüş mesafesi</li>
<li>Ücretsiz otopark</li>
</ul></div>
<h2>Hangi konularda görüşüyoruz?</h2>
<ul class="topic-grid">
<li><b>Kaygı ve stres:</b> sürekli endişe, uyku sorunları</li>
<li><b>Evlilik ve çift:</b> iletişim, güven, ortak karar alma</li>
<li><b>Ebeveynlik:</b> çocukla iletişim, sınırlar, disiplin</li>
<li><b>Çocuk ve ergen:</b> okul uyumu, duygu düzenleme</li>
<li><b>Boşanma süreci:</b> çocuklara anlatma, yeni düzene uyum</li>
<li><b>Kişisel gelişim:</b> özgüven, kendini tanıma</li>
</ul>
%(cta)s
<h2>İlk adım</h2>
<p>Arayın ya da WhatsApp'tan kısa bir mesaj bırakın. Görüşmeyi kimin için istediğinizi ve genel olarak hangi konuda destek aradığınızı paylaşmanız yeterli. Size uygun uzmanı ve saati birlikte belirleriz. Kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> başta olmak üzere ekibimizin profillerini <a href="/uzmanlarimiz/">Uzmanlarımız</a> sayfasında inceleyebilirsiniz.</p>
''',
 'faqs': [
  ("Alacaatlı'ya en yakın ofisiniz hangisi?", "Konutkent, Dumlupınar Bulvarı No:399 adresindeki Yaşamkent ofisimizdir; kısa bir sürüş mesafesindedir."),
  ("Hangi gün ve saatlerde görüşüyorsunuz?", "Pazartesi – Cumartesi 09:00 – 20:00 arasında randevu ile görüşme yapılır."),
  ("Aile olarak birlikte görüşme yapabilir miyiz?", "Evet. Aile görüşmeleri ve ebeveyn danışmanlığı yapılmaktadır."),
  ("Ücret bilgisi nasıl alınır?", "WhatsApp'tan yazarak ya da arayarak güncel ücret bilgisini öğrenebilirsiniz."),
 ],
},
{
 'path': '/cayyolu-cocuk-psikologu/',
 'kw': 'Çayyolu çocuk psikoloğu',
 'h1': 'Çayyolu Çocuk ve Ergen Psikoloğu',
 'title': 'Çayyolu Çocuk Psikoloğu | Ergen Psikoloğu, Oyun Terapisi – RN Psikoloji',
 'desc': "Çayyolu'nda çocuk ve ergen psikoloğu: oyun terapisi, okul uyumu, sınav kaygısı, öfke ve ebeveyn danışmanlığı. Yaşamkent ofisi. Randevu: 0552 418 79 73.",
 'lead': "Çocuğunuzun ya da ergen yaştaki gencinizin duygusal ve davranışsal zorlanmalarında, yaşına uygun yöntemlerle çalışan psikologlarımızla yanınızdayız. Oyun terapisi, ergen görüşmeleri ve ebeveyn danışmanlığı.",
 'body': '''
<h2>Çocuğunuz için ne zaman destek almalısınız?</h2>
<p>Her çocuk gelişim sürecinde zorlanır; bu doğaldır. Ancak bir davranış haftalarca sürüyor, evde ya da okulda günlük hayatı belirgin biçimde etkiliyor ya da siz ebeveyn olarak ne yapacağınızı bilemediğinizi hissediyorsanız, bir uzmanla konuşmak iyi bir adımdır. Erken dönemde alınan destek, sorunların büyümesini önlemeye yardımcı olabilir.</p>
<ul class="topic-grid">
<li><b>Okula uyum:</b> okula gitmek istememe, ayrılık kaygısı</li>
<li><b>Öfke ve duygu düzenleme:</b> sık öfke nöbetleri, ağlama krizleri</li>
<li><b>Kardeş kıskançlığı:</b> yeni kardeş, rekabet, geri çekilme</li>
<li><b>Korkular:</b> karanlık, yalnız kalma, uyku sorunları</li>
<li><b>Dikkat ve odak:</b> ders çalışmada zorlanma, dağınıklık</li>
<li><b>Aile değişiklikleri:</b> taşınma, boşanma, kayıp</li>
</ul>
<h2>Ergenlik döneminde destek</h2>
<p>Ergenlik; kimlik arayışı, akran ilişkileri ve bağımsızlaşma isteğiyle yoğun bir dönem. Sınav baskısı, sosyal medya, ekran süresi ve aileyle yaşanan çatışmalar gençlerin en sık zorlandığı alanlar. Ergen görüşmelerinde gencin kendini güvende hissetmesi ve görüşmelerin gizliliği önemlidir; ebeveynlerle ise gencin mahremiyeti korunarak ayrıca görüşülür.</p>
<ul class="topic-grid">
<li><b>Sınav kaygısı:</b> LGS ve üniversite sınavı dönemleri</li>
<li><b>Özgüven:</b> beden algısı, sosyal çekingenlik</li>
<li><b>Akran ilişkileri:</b> dışlanma, zorbalık, yalnızlık</li>
<li><b>Aile iletişimi:</b> sık tartışmalar, içine kapanma</li>
</ul>
%(cta)s
<h2>Oyun terapisi nedir?</h2>
<p>Küçük çocuklar duygularını çoğu zaman kelimelerle anlatamaz; oyun onların doğal dilidir. Oyun terapisinde çocuk, güvenli bir ortamda oyun aracılığıyla yaşadıklarını ifade eder. Psikolog bu süreçte çocuğun duygularını anlamaya, baş etme becerilerini güçlendirmeye ve ebeveynlere evde nasıl destek olabileceklerini göstermeye odaklanır.</p>
<h2>Süreç nasıl işler?</h2>
<ol>
<li><b>Ebeveyn ön görüşmesi:</b> Çocuğunuzun gelişim öyküsü, evdeki ve okuldaki durumu dinlenir.</li>
<li><b>Çocukla tanışma:</b> Yaşına uygun yöntemlerle çocuğunuzla görüşmeler başlar.</li>
<li><b>Ebeveyn geri bildirimi:</b> Düzenli aralıklarla sizinle süreç paylaşılır, evde uygulanabilecek öneriler konuşulur.</li>
</ol>
<h2>Çocuk ve ergen görüşmesi yapan uzmanlarımız</h2>
<p><a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> çocuklarla oyun terapisi yaklaşımıyla, ergenlerle ise yapılandırılmış ve bilimsel temelli yöntemlerle çalışır. <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> çocuk ve ergen görüşmeleri yürütür. Ebeveyn ve aile görüşmeleri için kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> ile de randevu alabilirsiniz. Daha fazla bilgi için <a href="/cocuk-ergen-danismanligi/">Çocuk ve Ergen Danışmanlığı</a> sayfamıza göz atabilirsiniz.</p>
''',
 'faqs': [
  ("Çocuğumu ilk görüşmeye getirmeli miyim?", "Genellikle ilk görüşme yalnızca ebeveynlerle yapılır. Çocuğunuzla görüşmeler bu ön görüşmeden sonra planlanır."),
  ("Hangi yaştaki çocuklarla çalışıyorsunuz?", "Okul öncesi dönemden ergenlik sonuna kadar çocuk ve gençlerle yaşlarına uygun yöntemlerle çalışılır."),
  ("Ergen çocuğum görüşmeye gelmek istemiyor, ne yapmalıyım?", "Bu sık karşılaşılan bir durumdur. Öncelikle ebeveynlerle görüşerek gencin sürece nasıl dahil edilebileceği birlikte planlanır."),
  ("Görüşmelerde konuşulanlar bizimle paylaşılır mı?", "Çocuğun ve gencin güveni için görüşme içerikleri ayrıntılı olarak aktarılmaz; ancak ebeveynlere sürecin genel gidişatı ve evde yapılabilecekler hakkında düzenli bilgi verilir. Güvenliği ilgilendiren durumlar bunun dışındadır."),
  ("Randevu nasıl alınır?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ],
},
{
 'path': '/cayyolu-cift-terapisi/',
 'kw': 'Çayyolu çift terapisi',
 'h1': 'Çayyolu Çift Terapisi ve Evlilik Danışmanlığı',
 'title': 'Çayyolu Çift Terapisi | Evlilik ve İlişki Danışmanlığı – RN Psikoloji',
 'desc': "Çayyolu ve Yaşamkent'te çift terapisi, evlilik ve ilişki danışmanlığı: iletişim, güven, aldatılma sonrası süreç, evlilik öncesi hazırlık. Randevu: 0552 418 79 73.",
 'lead': "İlişkinizde iletişim koptuysa, aynı tartışmalar tekrar ediyorsa ya da güven sarsıldıysa, çift görüşmeleri iki tarafın da sesinin duyulduğu güvenli bir alan sunar.",
 'body': '''
<h2>Çift terapisi kimler için?</h2>
<p>Çift terapisi yalnızca “bitmek üzere olan” ilişkiler için değildir. Birbirini seven ama anlaşmakta zorlanan, çocuk sonrası değişen düzene uyum sağlamaya çalışan, evliliğe hazırlanan ya da zor bir dönemi birlikte atlatmak isteyen her çift için bir destek alanıdır. Sorunlar kronikleşmeden alınan destek, çiftin kendi çözüm yollarını bulmasını kolaylaştırır.</p>
<ul class="topic-grid">
<li><b>İletişim:</b> konuşamamak, sürekli tartışmak, geri çekilme</li>
<li><b>Güven:</b> aldatılma sonrası süreç, kıskançlık</li>
<li><b>Yakınlık:</b> duygusal ve fiziksel uzaklaşma</li>
<li><b>Ebeveynlik:</b> çocuk yetiştirmede farklı tutumlar</li>
<li><b>Aile sınırları:</b> geniş aileyle ilişkiler</li>
<li><b>Karar dönemleri:</b> evlilik, taşınma, ayrılık kararı</li>
</ul>
%(cta)s
<h2>Görüşmeler nasıl yürütülür?</h2>
<p>Çift görüşmelerine genellikle iki taraf birlikte katılır. İlk görüşmede ilişkinin öyküsü, yaşanan zorluklar ve her iki tarafın beklentileri dinlenir. Gerektiğinde her bir partnerle ayrı görüşmeler de planlanabilir. Psikolog hiçbir tarafın “haklı” ya da “haksız” olduğunu belirlemez; amaç çiftin birbirini daha iyi anlaması ve birlikte işleyen yeni yollar geliştirmesidir.</p>
<h2>Evlilik öncesi danışmanlık</h2>
<p>Evliliğe adım atmadan önce beklentileri, maddi ve ailevi konuları, çatışma çözme biçimlerini konuşmak; ilişkinin sağlam bir zemine oturmasına yardımcı olur. Ayrıntılı bilgi için <a href="/evlilik-oncesi-danismanlik/">Evlilik Öncesi Danışmanlık</a> sayfamızı inceleyebilirsiniz.</p>
<h2>Çift görüşmesi yapan uzmanlarımız</h2>
<p>Kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a>, çift ve aile ilişkileri üzerine uzun yıllara dayanan deneyimiyle çift görüşmeleri yürütür; “Bir Hayatla Evlenmek” kitabının da yazarıdır. <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> da çift ve ilişki danışmanlığı alanında görüşme yapmaktadır. Genel bilgi için <a href="/cift-iliski-terapisi/">Çift ve İlişki Terapisi</a> sayfamıza bakabilirsiniz.</p>
''',
 'faqs': [
  ("Partnerim gelmek istemezse ne yapabilirim?", "Bireysel olarak başlayabilirsiniz. İlişkinizde sizin tarafınızdan neler değişebileceği üzerine çalışmak da ilişkiye olumlu yansıyabilir; partneriniz daha sonra sürece katılabilir."),
  ("Çift görüşmeleri ne sıklıkla yapılır?", "Görüşme sıklığı çiftin ihtiyacına göre belirlenir; genellikle haftalık ya da iki haftada bir planlanır."),
  ("Aldatılma sonrası çift terapisi işe yarar mı?", "Birçok çift bu süreçte destek alarak güveni yeniden inşa etmeye çalışır. Sürecin nasıl ilerleyeceği iki tarafın da istekliliğine bağlıdır."),
  ("Görüşmede taraf tutulur mu?", "Hayır. Psikolog iki tarafa da eşit mesafede durur ve ilişkinin kendisine odaklanır."),
  ("Randevu için ne yapmalıyız?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ],
},
{
 'path': '/cayyolu-aile-terapisi/',
 'kw': 'Çayyolu aile terapisi',
 'h1': 'Çayyolu Aile Terapisi ve Ebeveyn Danışmanlığı',
 'title': 'Çayyolu Aile Terapisi | Ebeveyn Danışmanlığı – RN Psikoloji',
 'desc': "Çayyolu ve Yaşamkent'te aile terapisi ve ebeveyn danışmanlığı: aile içi iletişim, ergen-ebeveyn çatışması, boşanma sürecinde çocuklar. Randevu: 0552 418 79 73.",
 'lead': "Aile içindeki gerginlikler herkesi etkiler. Aile görüşmeleri, her bireyin sesinin duyulduğu, suçlamadan uzak bir ortamda birlikte çözüm aramaya odaklanır.",
 'body': '''
<h2>Aile terapisi neye odaklanır?</h2>
<p>Aile, birbirini sürekli etkileyen bireylerden oluşan bir bütündür. Bir çocuğun okul sorunu, ebeveynler arasındaki gerginlik ya da bir aile üyesinin yaşadığı kriz tüm aileyi etkileyebilir. Aile görüşmelerinde sorun tek bir kişide aranmaz; aile içi iletişim, roller ve sınırlar birlikte ele alınır.</p>
<ul class="topic-grid">
<li><b>İletişim:</b> sık tartışmalar, konuşamamak, küslükler</li>
<li><b>Ergen – ebeveyn çatışması:</b> kurallar, özerklik, güven</li>
<li><b>Ortak ebeveynlik:</b> anne ve babanın farklı tutumları</li>
<li><b>Boşanma süreci:</b> çocuklara anlatma, iki evli düzen</li>
<li><b>Yeni aile düzenleri:</b> üvey ebeveyn, birleşik aileler</li>
<li><b>Kayıp ve kriz:</b> hastalık, yas, ani değişiklikler</li>
</ul>
%(cta)s
<h2>Ebeveyn danışmanlığı</h2>
<p>Bazen çocukla doğrudan görüşmek yerine ebeveynlerle çalışmak daha etkilidir. Ebeveyn danışmanlığında çocuğunuzun davranışlarının arkasındaki ihtiyaçları anlamanız, tutarlı sınırlar koymanız ve evde uygulanabilir yöntemler geliştirmeniz hedeflenir. Özellikle okul öncesi ve ilkokul çağındaki çocukların ebeveynleri için bu yaklaşım sık tercih edilir.</p>
<h2>Görüşmeler nasıl planlanır?</h2>
<p>İlk görüşmede aileden kimlerin katılacağı, başvuru nedeni ve beklentiler konuşulur. Sonraki görüşmeler ihtiyaca göre tüm aileyle, yalnızca ebeveynlerle ya da aile üyeleriyle ayrı ayrı yapılabilir. Görüşme planı ve sıklığı sizinle birlikte belirlenir.</p>
<h2>Uzmanlarımız</h2>
<p>Aile ve ebeveyn görüşmeleri için kurucumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> ile randevu alabilirsiniz; çocuk ve ergen boyutu olan durumlarda <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> ve <a href="/psikolog-hazal-aksahin/">Klinik Psikolog Hazal Akşahin</a> de sürece dahil olabilir. Genel bilgi için <a href="/aile-terapisi/">Aile Terapisi</a> sayfamıza da bakabilirsiniz.</p>
''',
 'faqs': [
  ("Aile görüşmesine herkesin katılması şart mı?", "Hayır. Görüşmeler ihtiyaca göre tüm aileyle, yalnızca ebeveynlerle ya da bireysel olarak planlanabilir."),
  ("Boşanma sürecinde çocuklar için destek veriyor musunuz?", "Evet. Boşanmanın çocuklara nasıl anlatılacağı ve yeni düzene uyum sürecinde hem ebeveynlerle hem de çocuklarla görüşülür."),
  ("Ergen çocuğumuzla sürekli tartışıyoruz, aile görüşmesi uygun mu?", "Ergen – ebeveyn çatışmaları aile görüşmelerinin en sık konularındandır. Gençle ve ebeveynlerle ayrı ve ortak görüşmeler planlanabilir."),
  ("Randevu nasıl alınır?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ],
},
{
 'path': '/cayyolu-psikolojik-danismanlik-merkezi/',
 'kw': 'Çayyolu psikolojik danışmanlık merkezi',
 'h1': 'Çayyolu Psikolojik Danışmanlık Merkezi',
 'title': 'Çayyolu Psikolojik Danışmanlık Merkezi | RN Psikoloji Çayyolu',
 'desc': "RN Psikoloji Çayyolu: bireysel, çift, aile, çocuk ve ergen psikolojik danışmanlık merkezi. Yaşamkent ofisi, ücretsiz otopark, Pazartesi – Cumartesi. Tel: 0552 418 79 73.",
 'lead': "Bireysel, çift, aile, çocuk ve ergen görüşmelerinin bir arada yürütüldüğü, deneyimli psikologlardan oluşan ekibimizle Çayyolu bölgesinde hizmet veriyoruz.",
 'body': '''
<h2>Tek adreste farklı yaş ve ihtiyaçlar</h2>
<p>Bir aile içinde farklı bireylerin farklı ihtiyaçları olabilir: annenin yaşadığı kaygı, gencin sınav stresi, küçük çocuğun uyum sorunu, çiftin iletişim zorluğu. RN Psikoloji Çayyolu, bu ihtiyaçların farklı uzmanlarca ama aynı çatı altında, birbiriyle uyumlu biçimde ele alınabildiği bir psikolojik danışmanlık merkezidir.</p>
<ul class="topic-grid">
<li><b><a href="/bireysel-danismanlik/">Bireysel danışmanlık</a>:</b> kaygı, stres, özgüven</li>
<li><b><a href="/cayyolu-cift-terapisi/">Çift terapisi</a>:</b> iletişim, güven, yakınlık</li>
<li><b><a href="/cayyolu-aile-terapisi/">Aile terapisi</a>:</b> aile içi iletişim, ebeveynlik</li>
<li><b><a href="/cayyolu-cocuk-psikologu/">Çocuk ve ergen</a>:</b> oyun terapisi, okul, sınav</li>
<li><b><a href="/evlilik-oncesi-danismanlik/">Evlilik öncesi</a>:</b> beklentiler, hazırlık</li>
<li><b><a href="/bosanma-sonrasi-danismanlik/">Boşanma sonrası</a>:</b> uyum ve yeniden yapılanma</li>
</ul>
%(cta)s
<h2>Merkezimizin yaklaşımı</h2>
<p>Her danışanı kendi öyküsüyle ele alıyoruz. İlk görüşmede ihtiyacınızı ve beklentilerinizi dinliyor, ardından size uygun, bilimsel temelli bir görüşme planı oluşturuyoruz. Gizlilik ve etik ilkeler çalışmalarımızın temelini oluşturur. Klinik tanı ya da ilaç tedavisi gerektiren durumlarda psikiyatri uzmanına yönlendirme yapıyoruz.</p>
<h2>Kurucumuz: Psikolog Rojin Nazik</h2>
<p><a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a>, RN Psikoloji'nin kurucusudur. Televizyon programlarına katılımları, ulusal gazetelerdeki röportajları ve yayımlanmış üç kitabıyla psikolojiyi geniş kitlelere anlaşılır bir dille ulaştırmaya çalışmaktadır. Basın çalışmalarını <a href="/basinda-biz/">Basında Biz</a>, kitaplarını <a href="/kitaplarimiz/">Kitaplarımız</a> sayfasında inceleyebilirsiniz.</p>
<h2>Konum ve çalışma saatleri</h2>
<p>Merkezimiz Konutkent, Dumlupınar Bulvarı No:399 Kat:28 Daire:121 adresindedir; Çayyolu, Ümitköy, Yaşamkent, İncek, Alacaatlı ve Beysukent'e yakındır. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 saatleri arasında randevu ile yapılır. Ücretsiz otopark mevcuttur.</p>
''',
 'faqs': [
  ("Merkezinizde hangi hizmetler veriliyor?", "Bireysel danışmanlık, çift ve evlilik terapisi, aile terapisi, çocuk ve ergen danışmanlığı, evlilik öncesi ve boşanma sonrası danışmanlık hizmetleri verilmektedir."),
  ("Tanı veya ilaç tedavisi yapıyor musunuz?", "Hayır. Merkezimizde psikolojik danışmanlık ve destek hizmeti verilir; tanı veya ilaç tedavisi gerektiren durumlarda psikiyatri uzmanına yönlendirme yapılır."),
  ("Hangi uzmanla görüşeceğimi nasıl seçerim?", "Kısaca durumunuzu paylaşmanız yeterli; başvuru nedeninize ve yaş grubuna göre size uygun uzmanı öneririz."),
  ("Merkeziniz nerede?", "Konutkent, Dumlupınar Bulvarı No:399 Kat:28 Daire:121, Çankaya / Ankara adresindeyiz."),
 ],
},
]

# Mevcut sayfalara eklenecek güçlendirme blokları (adres değişmez)
BOOST = {
 '/ankara-psikolog/': {
  'h1': 'Ankara Psikolog',
  'title': 'Ankara Psikolog | RN Psikoloji – Çayyolu, Yaşamkent Ofisi, Randevu',
  'desc': "Ankara'da psikolog: RN Psikoloji Yaşamkent ofisinde yetişkin, çift, aile, çocuk ve ergen görüşmeleri. Pazartesi – Cumartesi 09:00 – 20:00. Randevu: 0552 418 79 73.",
  'lead': "Ankara'nın batı yakasında, Çayyolu – Yaşamkent bölgesindeki ofisimizde deneyimli psikologlarla yüz yüze görüşme. Randevu için arayın ya da WhatsApp'tan yazın.",
  'intro': '''<h2>Ankara'da psikolog seçerken dikkat edilmesi gerekenler</h2>
<p>Ankara'da psikolog ararken çok sayıda seçenekle karşılaşırsınız. Doğru seçimi yapmak için uzmanın eğitimi ve deneyim alanı, sizin yaş grubunuz ve konunuzla ne kadar çalıştığı, görüşmelere düzenli devam edebileceğiniz bir konumda olması ve kendinizi rahat hissedip hissetmediğiniz önemlidir. İlk görüşme, bu uyumu değerlendirmek için de bir fırsattır.</p>
<ul class="topic-grid">
<li><b>Eğitim:</b> psikoloji lisansı ve alanında aldığı eğitimler</li>
<li><b>Deneyim alanı:</b> çocuk, ergen, yetişkin, çift</li>
<li><b>Konum:</b> düzenli gelebileceğiniz bir ofis</li>
<li><b>İletişim:</b> sorularınıza açık ve net yanıt verilmesi</li>
</ul>
%(cta)s
''',
  'faqs': [
   ("Ankara'da hangi semtlere hizmet veriyorsunuz?", "Yaşamkent'teki ofisimiz Çayyolu, Ümitköy, Konutkent, İncek, Alacaatlı ve Beysukent'e yakındır. Ankara'nın her yerinden danışanlarımız randevu ile görüşmeye gelebilir."),
   ("Ankara'da psikolog randevusu nasıl alınır?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz; uygun uzman ve saat birlikte belirlenir."),
   ("Hangi yaş gruplarıyla çalışıyorsunuz?", "Çocuk, ergen, yetişkin, çift ve ailelerle görüşme yapılmaktadır."),
   ("Görüşme saatleri nelerdir?", "Pazartesi – Cumartesi 09:00 – 20:00 arasında randevu ile görüşme yapılır."),
  ],
 },
 '/cayyolu-psikolog/': {
  'h1': 'Çayyolu Psikolog',
  'title': 'Çayyolu Psikolog | RN Psikoloji Çayyolu – Randevu 0552 418 79 73',
  'desc': "Çayyolu psikolog: RN Psikoloji'nin Yaşamkent ofisinde yetişkin, çift, aile, çocuk ve ergen görüşmeleri. Ücretsiz otopark, Pazartesi – Cumartesi. Randevu: 0552 418 79 73.",
  'lead': "Çayyolu'na birkaç dakika mesafedeki ofisimizde, kurucu psikoloğumuz Rojin Nazik ve ekibiyle yüz yüze psikolojik danışmanlık.",
  'intro': '''<h2>Çayyolu'nda yakınınızda psikolojik destek</h2>
<p>Çayyolu ve çevresinde yaşayanlar için RN Psikoloji'nin Yaşamkent ofisi, trafiğe ve uzun yollara takılmadan ulaşılabilecek bir konumda. Yetişkin bireysel görüşmelerden çift ve aile çalışmalarına, çocuk ve ergen görüşmelerinden evlilik öncesi danışmanlığa kadar geniş bir alanda deneyimli psikologlarımızla çalışıyoruz.</p>
<ul class="topic-grid">
<li><b><a href="/cayyolu-cocuk-psikologu/">Çocuk ve ergen psikoloğu</a></b></li>
<li><b><a href="/cayyolu-cift-terapisi/">Çift terapisi</a></b></li>
<li><b><a href="/cayyolu-aile-terapisi/">Aile terapisi</a></b></li>
<li><b><a href="/bireysel-danismanlik/">Bireysel danışmanlık</a></b></li>
</ul>
%(cta)s
''',
  'faqs': [
   ("Çayyolu'na en yakın ofisiniz nerede?", "Konutkent, Dumlupınar Bulvarı No:399 Kat:28 Daire:121 adresindeki Yaşamkent ofisimiz Çayyolu'na birkaç dakika mesafededir."),
   ("Çayyolu'nda hafta sonu psikolog randevusu alabilir miyim?", "Cumartesi günleri de 09:00 – 20:00 arasında randevu verilmektedir."),
   ("Otopark var mı?", "Evet, ücretsiz otopark mevcuttur."),
   ("Randevu nasıl alınır?", "0552 418 79 73 numarasını arayabilir ya da WhatsApp'tan yazabilirsiniz."),
  ],
 },
}
