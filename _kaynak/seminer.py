# -*- coding: utf-8 -*-
"""Okullar için veli ve öğretmen seminerleri sayfası (27 Ekim; kullanıcı teyidi: okul/veli semineri verilebiliyor).
build.py LANDINGS listesine ekler. Fiyat, okul adı ya da referans yazılmaz."""

SEMINER = {
 'path': '/okul-veli-seminerleri/',
 'kw': 'okul veli semineri',
 'h1': 'Okullar İçin Veli ve Öğretmen Seminerleri',
 'title': 'Okullar İçin Veli ve Öğretmen Seminerleri | RN Psikoloji Çayyolu',
 'desc': "Çayyolu, Ümitköy, İncek ve çevresindeki okullar için veli ve öğretmen seminerleri: sınav kaygısı, ekran kullanımı, ergenlikte iletişim, okula uyum.",
 'lead': "Okulunuzdaki velilere ve öğretmenlere; çocukların ve gençlerin duygusal gelişimi, sınav dönemleri ve aile içi iletişim üzerine psikolog seminerleri sunuyoruz.",
 'body': '''
<h2>Seminer konularımız</h2>
<p>Konular, okulunuzun yaş grubuna ve rehberlik servisinin gözlemlerine göre birlikte seçilir. Sık talep edilen başlıklar:</p>
<ul class="topic-grid">
<li><b>Sınav kaygısı:</b> LGS ve YKS dönemlerinde çocuğa baskı yapmadan destek olmak, sınav sabahı ve sonuçlar açıklandıktan sonra.</li>
<li><b>Ekran ve sosyal medya:</b> Yaşa göre ekran düzeni, aile ekran planı, çevrim içi oyunlar ve uyku.</li>
<li><b>Ergenlikte iletişim:</b> Odasından çıkmayan, konuşmayan genç; sınır koymak ile ilişkiyi korumak arasındaki denge.</li>
<li><b>Okula uyum ve okul reddi:</b> Okula başlama, okul değişikliği, sabah karın ağrıları ve okula gitmek istememe.</li>
<li><b>Duygularla baş etmek:</b> Öfke nöbetleri, kaygı, kardeş kıskançlığı; evde neler yapılabilir?</li>
<li><b>Akran ilişkileri:</b> Arkadaş edinmekte zorlanma, dışlanma ve akran zorbalığında ailenin ve okulun rolü.</li>
</ul>
<h2>Öğretmenler için</h2>
<p>Öğretmenlerle yapılan çalışmalarda sınıfta kaygılı, içine kapanık ya da öfkeli görünen öğrenciyi fark etmek, aileyle zor bir konuyu konuşmak ve öğretmenin kendi tükenmişliği gibi başlıklar ele alınır. Amaç, öğretmene bir psikolog gibi davranmasını yüklemek değil; ne zaman ve nasıl yönlendirme yapılacağını netleştirmektir.</p>
%(cta)s
<h2>Seminer nasıl planlanır?</h2>
<ul>
<li><b>Ön görüşme:</b> Okul yönetimi ya da rehberlik servisiyle konu, yaş grubu, katılımcı sayısı ve tarih konuşulur.</li>
<li><b>İçerik:</b> Seminer, okulunuzun ihtiyacına göre hazırlanır; velilerin önceden soru iletmesi için bir yol da planlanabilir.</li>
<li><b>Seminer günü:</b> Kısa bir sunum ardından soru-cevap bölümü yapılır. Velilerin kendi çocuklarına özel sorularını herkesin önünde sormak zorunda kalmaması için genel örnekler üzerinden ilerlenir.</li>
<li><b>Sonrası:</b> İhtiyaç duyan aileler için bilgilendirme notu ve başvuru yolları paylaşılır.</li>
</ul>
<h2>Okul yılı boyunca seminer takvimi</h2>
<p>Velilerin gündemi okul yılı boyunca değişir; seminer konusu da döneme göre seçildiğinde katılım ve fayda artar:</p>
<ul>
<li><b>Eylül–Ekim:</b> Okula başlama ve uyum, yeni okul, sabah ayrılıkları, ödev düzeni.</li>
<li><b>Kasım–Aralık:</b> Ekran ve sosyal medya, akran ilişkileri, ergenlikte iletişim.</li>
<li><b>Ocak–Mart:</b> Karne dönemi, motivasyon, sınav kaygısı ve deneme sınavlarına yaklaşım.</li>
<li><b>Nisan–Haziran:</b> LGS ve YKS öncesi aile tutumu, sonuçlar açıklandığında çocuğa nasıl destek olunur, yaz tatili düzeni.</li>
</ul>
<h2>Rehberlik servisiyle iş birliği</h2>
<p>Seminerler okulun rehberlik servisinin yerine geçmez; onu destekler. Rehber öğretmenlerin gözlemleri konu seçiminde yol gösterir. Bir öğrenci ya da aile için okul dışından psikolojik destek gerektiğinde, aile kendi kararıyla başvurabilir; okul ile paylaşılacak bilgiler yalnızca ailenin onayıyla ve gerektiği kadar olur.</p>
<h2>Çayyolu, Ümitköy, İncek ve Yaşamkent'teki okullar için</h2>
<p>Batı yakasındaki okulların velileri çoğu zaman benzer konularla gelir: yoğun sınav ve kurs temposu, servisle geçen uzun saatler, ekran süresi ve çalışan ebeveynlerin akşam saatlerine sıkışan aile zamanı. Seminer içeriği okulun bulunduğu çevreye ve velilerin gündemine göre uyarlanır. Çayyolu, Ümitköy, İncek, Yaşamkent, Konutkent ve Beysukent'teki okullar için seminerler okulun kendi salonunda yapılabilir; ofisimiz bu semtlere yakın olduğu için takvim esnek planlanabilir.</p>
<h2>Seminer sonrası veliler için destek yolu</h2>
<p>Bir seminer pek çok veliye kendi çocuğuyla ilgili yeni sorular düşündürür. Seminerin sonunda velilere, isterlerse kendi kararlarıyla başvurabilecekleri bir destek yolu tanıtılır: çocuk ve ergen görüşmeleri, ebeveyn danışmanlığı ve aile görüşmeleri. Bu başvurular tamamen gönüllüdür ve okul ile hiçbir bilgi paylaşılmaz. Çocuklarla ilgili görüşmelerin nasıl planlandığını <a href="/cayyolu-cocuk-psikologu/">Çayyolu çocuk psikoloğu</a> sayfamızda anlattık.</p>
<h2>Kimler sunar?</h2>
<p>Seminerler RN Psikoloji ekibinden psikologlar tarafından verilir. Kurucu psikoloğumuz <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> aile ve ebeveynlik konularında, <a href="/psikolog-elif-erdogan/">Psikolog Elif Erdoğan</a> çocuk ve ergenlerle çalışma konularında seminer verir. Tarih ve konu için WhatsApp'tan yazmanız ya da aramanız yeterli.</p>
''',
 'faqs': [
  ("Seminer okulda mı yapılıyor?", "Evet, seminer okulunuzda yapılır. Okulun tercihine göre online seminer de planlanabilir."),
  ("Seminerde velilerin özel bilgileri konuşulur mu?", "Hayır. Seminerler genel örnekler üzerinden ilerler; kimsenin kendi çocuğuyla ilgili özel bilgiyi herkesin önünde paylaşması beklenmez."),
  ("Hangi yaş gruplarına uygun seminer var?", "Okul öncesi, ilkokul, ortaokul ve lise velileri için ayrı içerikler hazırlanabilir; konu ve dil yaş grubuna göre uyarlanır."),
  ("Seminer sonrasında veliler bireysel destek alabilir mi?", "Evet. İsteyen veliler kendi kararlarıyla çocuk ve ergen görüşmesi, ebeveyn danışmanlığı ya da aile görüşmesi için başvurabilir; okul ile hiçbir bilgi paylaşılmaz."),
  ("Seminer için nasıl iletişime geçebiliriz?", "WhatsApp'tan ya da telefonla okulunuzun adını, yaş grubunu ve ilgilendiğiniz konuyu yazmanız yeterli; uygun tarih ve içerik birlikte planlanır."),
 ],
}
