# -*- coding: utf-8 -*-
# Psikolog Rojin Nazik'in merkez adına kontrol edip onayladığı soru-cevaplar (Uzman İçerik Kontrol ve Onay Formu, 2026-10-14).
# build.py her sorunun cevabının altına "Uzman kontrolü" satırını ekler ve soruyu sayfanın SSS bölümünün başına koyar.
# Metinler onaylı haliyle korunur; değişiklik yeniden uzman onayı ister.
UZMAN_SSS_TARIHI = '2026-10-14'
UZMAN_SATIRI = '<p class="faq-uzman">Uzman kontrolü: <a href="/psikolog-rojin-nazik/">Psikolog Rojin Nazik</a> (kurucu) · Ekim 2026</p>'

UZMAN_SSS = {
 '/kaygi-sorunlari/': [
  ("Çayyolu'nda kaygı için yapılan ilk görüşmede neler değerlendirilir?", "Belirtilerin şiddeti kadar, kaygının günlük hayatı nasıl etkilediğine ve bedensel belirtileri sürekli kontrol etmek gibi kaygıyı sürdüren alışkanlıklara bakılır. Gerekirse tıbbi değerlendirme önerilir. Görüşme Yaşamkent ofisinde ya da online yapılabilir.")],
 '/cayyolu-psikolog-depresyon-panik-atak-sosyal-fobi-sinav-kaygisi-ve-travma-terapisi/': [
  ("Hayatım düzenli görünüyor ama hiçbir şeyden keyif almıyorum; destek almalı mıyım?", "Sorumlulukları yerine getirmeye devam etmek, kişinin duygusal olarak iyi olduğu anlamına gelmez. Keyif kaybı, yorgunluk ve hiçbir şeye yetişememe hissi birkaç haftadır sürüyorsa bir uzmanla konuşmak iyi bir başlangıçtır.")],
 '/cayyolu-cift-terapisi/': [
  ("Çift terapisinde tartışmalar nasıl ele alınır?", "Tartışmanın konusundan çok nasıl sürdüğüne bakılır: bir taraf kendini anlatmaya çalışırken diğeri eleştirildiğini hissedebilir. Bu döngü fark edildikçe küçük meselelerin büyük kırgınlıklara dönüşmesinin önüne geçilebilir.")],
 '/cift-iliski-terapisi/': [
  ("Aldatılma sonrası çift görüşmelerinde ilk olarak ne konuşulur?", "Önce güvenin sarsılmasıyla ortaya çıkan öfke, belirsizlik ve üzüntü anlaşılmaya çalışılır; yaşananın iki taraf için ne ifade ettiği ele alınır. İlişkinin geleceğiyle ilgili karar bu zeminden sonra konuşulur.")],
 '/bosanma-sonrasi-danismanlik/': [
  ("Boşanma kararını verdik ama hâlâ çok zorlanıyorum; bu normal mi?", "Evet. Duygusal ayrılık, kararla aynı hızda ilerlemeyebilir; bazıları için en zor dönem karardan önce, bazıları için ayrı yaşam başladıktan sonradır. Çocuklu ailelerde ebeveynin kendi duygularını çocuğun ihtiyaçlarından ayırabilmesi önemlidir.")],
 '/cocuk-ergen-danismanligi/': [
  ("Ergen çocuğumla iletişim için biz de görüşmelere katılır mıyız?", "Gerektiğinde evet. Yalnız ergenin davranışlarına değil, aile içindeki iletişimin nasıl kurulduğuna da bakılır; bu yüzden ebeveyn görüşmeleri planlanabilir. Gencin görüşmelerinin gizliliğinin nasıl korunacağı baştan konuşulur.")],
 '/cayyolu-cocuk-psikologu/': [
  ("Çocuğumun öfkesine sınır koymak ile duygusunu anlamak çelişir mi?", "Hayır, birbirini tamamlar. Öfkenin hangi durumlarda çıktığı, ne kadar sürdüğü ve yetişkinlerin nasıl tepki verdiği önemli bilgi verir. Çocuğun duygusunu tanımasına yardım ederken davranışına tutarlı sınır koymak birlikte yürütülür.")],
 '/cayyolu-bireysel-terapi-hizmetleri-ozguven-ofke-travma-bosanma-ve-yas-sureclerinde-uzman-destegi/': [
  ("Yakınımı kaybettim, çevrem “güçlü ol” diyor; ne zaman destek almalıyım?", "İyi niyetli bu tavsiyeler bazen duyguları paylaşmayı zorlaştırır; yasın kişiye özgü bir hızı vardır. Duygularınızı kimseyle paylaşamıyorsanız ya da günlük hayatınız uzun süre ciddi biçimde etkileniyorsa destek almak iyi gelir; acil bir durumda 112'yi arayın.")],
 '/bireysel-danismanlik/': [
  ("Girişken biriyim ama başkalarının onayını kaybetmekten korkuyorum; bu özgüven sorunu mu?", "Olabilir. Özgüven güçlükleri her zaman çekingenlik olarak görünmez; girişken görünen biri de onay kaybetmekten yoğun biçimde korkabilir. Bu yüzden özgüven yalnızca sosyal ortamlarda rahat konuşabilmek üzerinden değerlendirilmez.")],
 '/online-terapi/': [
  ("Yaşamkent ofisine gelemediğim haftalarda online görüşebilir miyim?", "Uygun durumlarda evet. Bunun için sessiz ve özel bir ortam ile iyi bir internet bağlantısı gerekir; online görüşmenin size uygun olup olmadığı önceden birlikte değerlendirilir. Ofise geldiğiniz haftalarda ücretsiz otopark vardır.")],
}
UZMAN_SORULARI = {q for v in UZMAN_SSS.values() for q, _ in v}
