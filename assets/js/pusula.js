/* ============================================================
   Randevu Pusulası — "60 saniyede size özel yol haritası"
   ------------------------------------------------------------
   Ziyaretçi 3–4 dokunuşla kim için / hangi konuda / nerede sorularını
   seçer; Psikolog Rojin Nazik'in kartı, o konudaki gerçek notu ve
   kişiye özel "ilk görüşme yol haritası" açılır.
   Tek hedef: telefonla aramak.

   - İsim, telefon, serbest metin ALINMAZ; hiçbir şey kaydedilmez.
   - Sunucu yanıt vermezse hazır metinle aynen çalışır.
   - Güvende hissetmiyorum seçeneği sunucuya gitmez: 112 ekranı.
   - Aramalar ads-conversion.js tarafından data-cta-area="pusula"
     olarak sayılır (Google Ads "Tıkla ve ara" dönüşümü).

   Ayar (isteğe bağlı, bu dosyadan ÖNCE):
     window.PUSULA_CFG = { site: 'rojin' | 'cayyolu', api: '...', foto: '...' }
   Sayfada herhangi bir öğeye data-pusula eklemek onu açar.
   Rojin, Çayyolu ve Elif Erdoğan sitelerinde aynı dosya kullanılır.
   ============================================================ */
(function () {
  'use strict';
  var w = window, d = document;
  if (w.__pusula) return;
  w.__pusula = true;

  var CFG = w.PUSULA_CFG || {};
  var SITE = CFG.site === 'cayyolu' || CFG.site === 'elif' ? CFG.site : 'rojin';
  var API = CFG.api || 'https://www.psikologunubul.com.tr/api/pusula';
  var RN = SITE === 'rojin' ? '' : 'https://psikologrojinnazik.com';
  var EE = SITE === 'elif' ? '' : 'https://psikologeliferdogan.com';
  // Sitenin ana uzmanı (giriş düğmesi, bant, hatırlatma fotoğrafı)
  var FOTO = CFG.foto || (SITE === 'elif' ? '/assets/elif/team-elif-erdogan.webp' : RN + '/images/brand/rojin-nazik-portrait-800.webp');
  var ELIF_FOTO = CFG.elifFoto || (SITE === 'elif' ? FOTO : SITE === 'cayyolu' ? '/assets/img/team-elif-erdogan.webp' : '/images/brand/elif-erdogan-720.webp');
  var TEL = 'tel:+905524187973', TEL_TXT = '0552 418 79 73', WA = '905524187973';
  // Telefonu açan gerçek kişi. Fotoğraf gelene kadar baş harf gösterilir: PUSULA_CFG.seldaFoto
  var SELDA = 'Selda Hanım', SELDA_FOTO = CFG.seldaFoto || '';
  var REDUCED = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Seçenekler (anahtarlar sunucudaki listeyle birebir aynı) ---------- */
  var KIM = [
    { k: 'kendim', i: '🙋', t: 'Kendim için', s: 'Yetişkin bireysel görüşme' },
    { k: 'cocugum', i: '🧒', t: 'Çocuğum için', s: '3–11 yaş' },
    { k: 'ergen', i: '🎧', t: 'Ergen çocuğum için', s: '12–18 yaş' },
    { k: 'cift', i: '💞', t: 'Eşim / partnerim ve ben', s: 'Çift ve ilişki görüşmesi' }
  ];
  var KONU = {
    kendim: [['kaygi', 'Kaygı ve stres'], ['panik', 'Panik atak'], ['mutsuzluk', 'Mutsuzluk, isteksizlik'], ['iliski', 'İlişki sorunları'], ['ayrilik', 'Boşanma / ayrılık'], ['yas', 'Yas ve kayıp'], ['ofke', 'Öfke'], ['ozguven', 'Özgüven'], ['dusunce', 'Aşırı düşünme'], ['test', 'Psikolojik test / MMPI'], ['diger', 'Adını tam koyamıyorum']],
    cocugum: [['davranis', 'Öfke ve davranış'], ['okul', 'Okul ve ders'], ['korku', 'Kaygı ve korkular'], ['uyku', 'Uyku sorunları'], ['bosanma', 'Boşanma sürecinde çocuğum'], ['ayrilma', 'Ayrılma kaygısı, okula başlama'], ['diger', 'Adını tam koyamıyorum']],
    ergen: [['iletisim', 'Bizimle konuşmuyor'], ['sinav', 'Sınav kaygısı'], ['icekapanma', 'İçe kapanma'], ['ofke', 'Öfke'], ['ekran', 'Telefon / ekran'], ['ozguven', 'Özgüven'], ['diger', 'Adını tam koyamıyorum']],
    cift: [['iletisim', 'İletişim kuramıyoruz'], ['tartisma', 'Sık tartışıyoruz'], ['guven', 'Güven sorunu'], ['uzaklasma', 'Birbirimizden uzaklaştık'], ['evlilikoncesi', 'Evlilik öncesi'], ['bosanma', 'Boşanma kararı'], ['diger', 'Adını tam koyamıyoruz']]
  };
  var YAS = [['3-6', '3–6 yaş'], ['7-11', '7–11 yaş'], ['12+', '12 yaş ve üstü']];
  var YER = [
    { k: 'yasamkent', i: '📍', t: 'Yaşamkent / Çayyolu', s: 'Konutkent · Pazartesi–Cumartesi' },
    { k: 'kizilay', i: '🏙️', t: 'Kızılay', s: 'Bakanlıklar · Pazartesi günleri' },
    { k: 'online', i: '💻', t: 'Online', s: 'Ankara dışından ya da evden' },
    { k: 'farketmez', i: '✨', t: 'Fark etmez', s: 'Bana uygun olanı önerin' }
  ];
  var SUBE = {
    yasamkent: 'Yaşamkent / Çayyolu şubesi: Konutkent, Dumlupınar Blv. No:399 Kat:28 D:121 · ücretsiz otopark',
    kizilay: 'Kızılay şubesi: Atatürk Blv. No:127 Kat:8, Bakanlıklar · Pazartesi günleri',
    online: 'Online görüşme: Türkiye ve yurt dışından, görüntülü',
    farketmez: 'Yaşamkent / Çayyolu (Pazartesi–Cumartesi), Kızılay (Pazartesi) veya online'
  };

  /* ---------- Psikolog Rojin Nazik'in sitede yayımlanmış kendi notları ---------- */
  var NOT = {
    cocuk1: ['/ankara-cocuk-psikologu/', 'Anne-babaların en sık kaçırdığı nokta', 'Ben davranışın ne zaman başladığına, hangi durumlarda arttığına ve çocuğun o dönemde hayatında neler yaşadığına bakmayı önemli buluyorum. Çünkü bazı çocuklar ifade etmekte zorlandıkları duyguları davranışları üzerinden gösterebiliyor.'],
    cocuk2: ['/ankara-cocuk-psikologu/', 'Ebeveynlere ilk önerim', 'Ebeveynlerden ilk istediğim şeylerden biri, çocuğun davranışını hemen değiştirmeye çalışmadan önce onu biraz daha dikkatli gözlemlemeleri oluyor. Özellikle bir davranışın öncesinde ve sonrasında neler yaşandığı çok önemli ipuçları verebiliyor.'],
    cocuk3: ['/cocuk-ergen-danismanligi/', 'İyi niyetle yapılıp çocuğu kapatabilen davranış', 'Çocuk bir sorun anlattığında hemen nasihat vermek, çözüm bulmak veya olayın neden yanlış olduğunu açıklamak yerine önce onun ne hissettiğini anlamaya çalışmak iletişimi değiştirebiliyor. Bazen çocukların ilk ihtiyacı çözüm değil, gerçekten duyulduklarını hissetmek oluyor.'],
    ergen1: ['/ankara-ergen-psikologu/', 'Ergenlerle çalışırken', 'Aile ‘bizimle konuşmuyor’ derken ergen ‘konuştuğumda hemen eleştiriliyorum veya bana çözüm söyleniyor’ diyebiliyor. Bu nedenle ergenlerle çalışırken önce güvenli ve yargılanmadan konuşabilecekleri bir ilişki kurulmasını önemli görüyorum.'],
    ergen2: ['/ankara-ergen-psikologu/', 'Ergenlerin söylemekte zorlandığı şey', 'Ergen görüşmelerinde zaman zaman ‘beni hemen düzeltmeye çalışmadan önce bir dinleseler’ duygusuyla karşılaşıyorum. Ergen önce anlaşılmak, sonra çözüm konuşmak isteyebiliyor.'],
    kaygi1: ['/anksiyete-bozukluklari/', 'Kaygıda en sık gördüğüm yanlış inanç', 'Kaygı yaşayan danışanlarda sık gördüğüm düşüncelerden biri, ‘Bu duyguyu hiç yaşamamalıyım’ beklentisi. Bazen sorun yalnızca kaygının kendisi değil, kişinin kaygı yaşamaktan korkması haline geliyor.'],
    kaygi2: ['/anksiyete-bozukluklari/', 'Kaygı seanslarında en faydalı bulduğum yaklaşım', 'Hangi düşüncenin hangi duyguyu tetiklediğini, ardından hangi kaçınma veya güvence arama davranışının geldiğini birlikte anlamak önemli olabiliyor. Aynı ‘kaygı’ tanımı altında bile her kişinin yaşadığı süreç farklı olabiliyor.'],
    panik: ['/panik-atak/', 'Panik atakta en sık korkulan şey', 'Panik yaşayan kişilerde bedensel belirtilerin kendisinden çok, bu belirtilere verilen anlamın kişiyi zorladığını sık görüyorum. Bu nedenle görüşmelerde kişinin yalnızca ne hissettiğine değil, hissettiği şeyi nasıl yorumladığına da bakıyorum.'],
    degisim: ['/bireysel-danismanlik/', 'İyi ilerleyen bir süreçte ilk fark ettiğim değişiklik', 'Bazen ilk önemli değişiklik, kişinin eskiden otomatik biçimde verdiği tepkiyi fark edip ‘Ben yine aynı şeyi yapıyorum’ diyebilmesi oluyor. Kişinin kendi döngüsünü fark etmeye başlamasını önemli bir adım olarak görüyorum.'],
    terapi: ['/psikotereapi-nedir/', 'Terapi hakkında en yanlış beklenti', 'Ben terapiyi kişinin hayatı hakkında onun yerine karar verilen bir alan olarak görmüyorum. Daha çok kişinin yaşadığı durumu, tekrar eden örüntülerini ve seçeneklerini daha net görebileceği bir çalışma alanı olarak değerlendiriyorum.'],
    ilk: ['/ankara-psikolog-randevusu-nasil-alinir/', 'İlk kez gelenler en çok neden çekiniyor?', 'İlk görüşmeye gelen kişilerde en sık gördüğüm kaygılardan biri, ‘Ne anlatacağım, nereden başlayacağım?’ düşüncesi. İlk görüşme ilerledikçe bunun bir sınav olmadığını ve her şeyi bir anda anlatmak zorunda olmadıklarını fark ettiklerinde daha rahatlayabildiklerini görüyorum.'],
    gitmeli: ['/ankara-psikolog-randevusu-nasil-alinir/', '‘Psikoloğa gitmeli miyim?’ diye soranlara', 'Psikoloğa başvurmak için kişinin hayatının tamamen kontrolden çıkmasını beklemesi gerektiğini düşünmüyorum. Aynı düşünce, duygu veya ilişki döngüsünün tekrar ettiğini fark ediyor ve bunun içinden çıkmakta zorlanıyorsa bunu konuşmak için yeterli bir neden olabilir.'],
    bosanma1: ['/bosanma-sonrasi-danismanlik/', 'Boşanma sürecinde en zor dönem', 'Boşanma sürecinde kişinin yalnızca eşinden değil, birlikte kurduğu gelecek düşüncesinden de ayrıldığını görüyorum. Alışılmış düzenin değişmesi ve yeni bir yaşam kurma dönemi bazı kişiler için karar aşamasından bile daha zorlayıcı olabiliyor.'],
    bosanma2: ['/bosanma-sonrasi-danismanlik/', 'Çocuklu çiftlere en önemli önerim', 'Çocuğun anne-baba arasındaki çatışmanın içine çekilmesi, mesaj taşıması veya taraf tutmak zorunda hissetmesi onu zorlayabiliyor. Çocuğun yetişkinler arasındaki sorunlardan mümkün olduğunca korunmasını önemli buluyorum.'],
    cift1: ['/cift-iliski-terapisi/', 'Çiftlerde en sık gördüğüm sorun', 'Çiftlerin çoğu ‘iletişim kuramıyoruz’ diyerek geliyor. Görüşmeler ilerledikçe çoğu zaman sorunun yalnızca iletişim olmadığını; uzun süredir konuşulmamış kırgınlıkların, anlaşılmama hissinin ve tekrar eden ilişki döngülerinin biriktiğini görüyorum.'],
    cift2: ['/cift-iliski-terapisi/', 'İlk seansta fark ettirdiğim şey', 'İlk çift görüşmelerinde tarafların yalnızca ne söylediklerine değil, birbirlerinin söylediklerini nasıl yorumladıklarına da bakıyorum. Çiftin kendi iletişim döngüsünü dışarıdan görebilmeye başlaması önemli ilk farkındalıklardan biri olabiliyor.'],
    cift3: ['/cift-iliski-terapisi/', 'Çift görüşmelerinde en sık duyduğum cümle', 'Tartışmanın içindeki öfkenin altında bazen ‘beni önemse’, ‘yanımda olduğunu hissettir’ veya ‘beni anlamaya çalış’ gibi çok daha temel bir ihtiyaç bulunabiliyor.'],
    uzak: ['/evlilik-ve-aile-danismanligi/', 'Sevgi varken çiftler neden uzaklaşıyor?', 'Çiftlerin birbirinden uzaklaşması her zaman sevginin tamamen bitmesiyle başlamıyor. Bazen iki taraf da hâlâ ilişkiyi önemsiyor fakat uzun süre duyulmadığını veya anlaşılmadığını düşündüğü için geri çekiliyor.'],
    online: ['/online-terapi/', 'Online terapi yüz yüzeden nasıl farklı?', 'Bazı danışanların kendi ortamlarından katıldıklarında daha rahat konuşabildiklerini, bazılarının ise yüz yüze görüşmede kendisini daha iyi hissettiğini gözlemliyorum. Online görüşmenin uygunluğunu kişinin ihtiyacı ve koşulları üzerinden değerlendiriyorum.']
  };
  var NOT_ESLE = {
    kendim: { kaygi: 'kaygi1', panik: 'panik', mutsuzluk: 'degisim', iliski: 'cift3', ayrilik: 'bosanma1', yas: 'gitmeli', ofke: 'degisim', ozguven: 'terapi', dusunce: 'kaygi2', test: 'terapi', diger: 'ilk' },
    cocugum: { davranis: 'cocuk1', okul: 'cocuk2', korku: 'cocuk3', uyku: 'cocuk2', bosanma: 'bosanma2', ayrilma: 'cocuk3', diger: 'cocuk1' },
    ergen: { iletisim: 'ergen1', sinav: 'ergen2', icekapanma: 'ergen2', ofke: 'ergen1', ekran: 'ergen1', ozguven: 'ergen2', diger: 'ergen1' },
    cift: { iletisim: 'cift1', tartisma: 'cift3', guven: 'cift2', uzaklasma: 'uzak', evlilikoncesi: 'cift2', bosanma: 'bosanma1', diger: 'cift1' }
  };
  /* ---------- Psikolog Elif Erdoğan'ın sitesinde yayımlanmış kendi notları ---------- */
  var ENOT = {
    oyun1: ['/hizmetler/oyun-terapisi', 'Oyunu nasıl değerlendiriyorum?', 'Çocuk bazen söyleyemediği veya adını koyamadığı bir duyguyu oyununda, seçimlerinde veya tekrar eden temalarında gösterebiliyor. Bu nedenle oyunu yalnızca çocuğun eğlendiği bir bölüm olarak değil, onu anlamanın yollarından biri olarak değerlendiriyorum.'],
    oyun2: ['/hizmetler/oyun-terapisi', 'Ailelerin en sık yanlış anladığı konu', 'Oyun terapisiyle ilgili ailelerin en sık yanlış anlayabildiği konulardan biri, çocuğun görüşme sırasında yalnızca oyun oynadığının düşünülmesi. Oysa oyun, çocukların duygularını ve yaşadıklarını ifade edebildiği doğal yollardan biridir.'],
    oyun3: ['/hizmetler/oyun-terapisi', 'Süreç yalnızca çocukla değil', 'Çocuğun yaşadığı güçlükleri anlamak için aile ilişkilerini ve günlük yaşam koşullarını da değerlendirmek gerekebiliyor. Bu nedenle ebeveynlerle iş birliğine ve gerekli durumlarda ebeveyn görüşmelerine önem veriyorum.'],
    ergen1: ['/hizmetler/ergen-psikoterapisi', 'Ergenlerle ilk görüşmede', 'Ergenlerle yaptığım ilk görüşmelerde en çok önem verdiğim konu, kendilerini yargılanmadan ifade edebilecekleri bir ortam oluşturmak. Bu nedenle hemen sorunlara odaklanmak yerine önce birbirimizi tanımaya ve güven ilişkisi kurmaya özen gösteriyorum.'],
    ergen2: ['/hizmetler/ergen-psikoterapisi', 'Davranışın öncesine bakmak', 'İçe kapanma, öfke veya derslerden uzaklaşmanın kendisine odaklanmak yerine bunun hangi dönemlerde arttığına ve öncesinde neler olduğuna bakmak daha fazla bilgi verebiliyor. Bu nedenle ergeni yalnızca ‘değişmesi gereken kişi’ olarak değerlendirmemeye dikkat ediyorum.'],
    ergen3: ['/hizmetler/ergen-psikoterapisi', 'Gizlilik ve güven', 'Görüşmenin başında gizliliğin sınırlarını, güvenlik ve yasal sorumluluklarla ilgili istisnaları yaşlarına uygun şekilde açıklamayı önemsiyorum. Gencin kendisini güvende hissedebilmesi, görüşme sürecinin önemli parçalarından biri.'],
    cift: ['/hizmetler/cift-iliski-danismanligi', 'Çiftlerde sık gördüğüm döngü', 'Bir tarafın kendisini anlatmak için daha fazla üzerine gitmesi, diğer tarafın ise gerilimi azaltmak için daha fazla geri çekilmesi. İki taraf da çoğu zaman ilişkiyi korumaya çalışırken birbirlerinde tam ters etkiyi oluşturabiliyor.'],
    mmpi1: ['/blog/mmpi-testi-nedir', 'MMPI hakkında en yanlış beklenti', 'MMPI konusunda en sık karşılaştığım yanlış beklentilerden biri testin kişiye tek başına kesin bir tanı koyacağı düşüncesi. Test benim için kişiyi bir etikete yerleştiren değil, değerlendirmeyi destekleyen araçlardan biridir.'],
    mmpi2: ['/blog/mmpi-testi-nedir', 'Doğru cevap kaygısı', 'Bu testte amaç başarılı olmak ya da doğru cevapları bulmak değil, kişinin kendisini mümkün olduğunca doğru yansıtabilmesi. Bu nedenle uygulama öncesinde testin amacı ve nasıl yanıtlanması gerektiği hakkında bilgilendirme yapmayı önemsiyorum.']
  };
  var ENOT_ESLE = {
    kendim: { test: 'mmpi1', iliski: 'cift', diger: 'mmpi2' },
    cocugum: { davranis: 'oyun1', okul: 'oyun3', korku: 'oyun1', uyku: 'oyun3', bosanma: 'oyun3', ayrilma: 'oyun2', diger: 'oyun2' },
    ergen: { iletisim: 'ergen1', sinav: 'ergen2', icekapanma: 'ergen2', ofke: 'ergen2', ekran: 'ergen1', ozguven: 'ergen1', diger: 'ergen3' },
    cift: { iletisim: 'cift', tartisma: 'cift', guven: 'cift', uzaklasma: 'cift', evlilikoncesi: 'cift', bosanma: 'cift', diger: 'cift' }
  };
  var ENEDEN = {
    kendim: 'Yetişkinlerle bilişsel ve davranışçı yaklaşımla çalışır; MMPI dahil psikolojik test ve değerlendirme uygular.',
    cocugum: 'Çocuklarla oyun terapisi ve gelişimsel değerlendirme araçlarıyla çalışır; ebeveynlerle iş birliğine önem verir.',
    ergen: 'Ergenlerle önce yargılanmadan konuşulabilen, güvenli bir ilişki kurmayı önemser.',
    cift: 'Çiftlerle tekrar eden ilişki döngülerini görünür kılmaya odaklanarak çalışır.'
  };

  // Hangi uzman önerilir? Elif sitesi: yalnız Elif Erdoğan.
  // Rojin ve Çayyolu: ağırlık Rojin Nazik'te; küçük çocuk (oyun terapisi), ergen sınav kaygısı ve
  // psikolojik test (MMPI) Elif Erdoğan'a.
  function uzmanSec(x) {
    if (SITE === 'elif') return 'elif';
    if (x.konu === 'test') return 'elif';
    if (x.kim === 'cocugum' && x.yas === '3-6') return 'elif';
    if (x.kim === 'ergen' && x.konu === 'sinav') return 'elif';
    return 'rojin';
  }
  function uzmanProfil(u, x) {
    if (u === 'elif') {
      var en = ENOT[ENOT_ESLE[x.kim][x.konu]];
      return { ad: 'Psikolog Elif Erdoğan', kisa: 'Elif Hanım', unvan: 'Psikolog · RN Psikoloji', foto: ELIF_FOTO, notlar: 'Elif Erdoğan\'ın notları taranıyor',
        etiket: ['Bilişsel davranışçı terapi (DATEM)', 'Oyun terapisi', 'MMPI ve psikolojik test', 'Yetişkin · ergen · çift'],
        neden: ENEDEN[x.kim], not: en, notTaban: EE };
    }
    var rn = NOT[(x.yer === 'online' && x.konu === 'diger') ? 'online' : NOT_ESLE[x.kim][x.konu]] || NOT.ilk;
    return { ad: 'Psikolog Rojin Nazik', kisa: 'Rojin Hanım', unvan: 'Psikolog ve Aile Danışmanı · RN Psikoloji kurucusu', foto: SITE === 'rojin' ? FOTO : RN + '/images/brand/rojin-nazik-portrait-800.webp',
      etiket: ['15+ yıllık mesleki deneyim', 'Şema terapi eğitimi', '3 kitap yazarı', 'AB Psikologlar Derneği Genel Başkanı'],
      neden: NEDEN[x.kim], not: rn, notTaban: RN, notlar: 'Rojin Nazik\'in notları taranıyor' };
  }

  var NEDEN = {
    kendim: 'Yetişkinlerle bireysel görüşmelerde bilişsel davranışçı yaklaşım ve şema terapi eğitimiyle çalışır.',
    cocugum: 'Çocuk danışmanlığında ebeveynle birlikte çalışır; ilk görüşme genellikle sizinle yapılır.',
    ergen: 'Ergenlerle önce güvenli, yargılanmadan konuşulabilen bir ilişki kurmayı önemser; aileyi de sürece katar.',
    cift: 'Psikolog ve aile danışmanı olarak çift ve evlilik görüşmeleri yapar.'
  };

  /* ---------- Sunucu yanıt vermezse: hazır yol haritaları ---------- */
  var YEDEK = {
    kendim: '## Sizi anlıyoruz\nYaşadığınız şeyi bir uzmanla konuşmayı düşünmeniz önemli bir adım. Pek çok kişi benzer duygularla başvuruyor ve ilk görüşmede her şeyi bir anda anlatmak zorunda değil.\n## İlk görüşmede neler olur\n- Ne yaşadığınızı, ne zamandır sürdüğünü ve gününüzü nasıl etkilediğini konuşursunuz.\n- Sizi zorlayan durumların hangi anlarda arttığına birlikte bakılır.\n- Görüşmenin sonunda nasıl bir çalışma planıyla ilerlenebileceği konuşulur.\n## Görüşmeden önce küçük hazırlık\n- Son haftalarda sizi en çok zorlayan iki üç anı kısaca not edin.\n- Terapiden ne beklediğinizi tek cümleyle yazmayı deneyin.\n- Aklınıza gelen soruları telefonunuza kaydedin; görüşmede sormak rahatlatır.\n## Telefonda sorabilecekleriniz\n- Bana en yakın uygun saat hangisi?\n- İlk görüşme yüz yüze mi online mı daha uygun olur?',
    cocugum: '## Sizi anlıyoruz\nÇocuğunuzdaki değişikliği fark edip destek aramanız ona verebileceğiniz en değerli şeylerden biri. Pek çok aile benzer sorularla başvuruyor.\n## İlk görüşmede neler olur\n- İlk görüşme genellikle sizinle, ebeveynlerle yapılır.\n- Davranışın ne zaman başladığı ve hangi durumlarda arttığı konuşulur.\n- Çocuğunuzla görüşmelerin nasıl ilerleyeceği birlikte planlanır.\n## Görüşmeden önce küçük hazırlık\n- Davranışın öncesinde ve sonrasında neler olduğunu birkaç gün not edin.\n- Çocuğunuza, duygularını konuşabileceği ve oyun oynayabileceği biriyle tanışacağını sade bir dille anlatabilirsiniz.\n- Okuldan ya da bakımını üstlenen kişilerden gelen gözlemleri yanınızda getirin.\n## Telefonda sorabilecekleriniz\n- İlk görüşmeye çocuğumla mı gelmeliyim, yalnız mı?\n- Bize en yakın uygun saat hangisi?',
    ergen: '## Sizi anlıyoruz\nErgenlik dönemi hem gençler hem aileler için zorlayıcı olabiliyor. Destek aramanız ilişkinizi güçlendirmek için atılmış önemli bir adım.\n## İlk görüşmede neler olur\n- Önce sizin gözlemleriniz dinlenir, ardından gencin kendi anlatımına yer açılır.\n- Gencin yargılanmadan konuşabileceği güvenli bir ilişki kurulmasına önem verilir.\n- Ailenin sürece nasıl katılacağı birlikte konuşulur.\n## Görüşmeden önce küçük hazırlık\n- Gencinize görüşmeyi bir ceza değil, kendisi için ayrılmış bir alan olarak anlatın.\n- Sizi en çok endişelendiren iki üç durumu not edin.\n- Gencinizin görüşmeye dair sorularını dinleyin ve bunları telefonda iletin.\n## Telefonda sorabilecekleriniz\n- İlk görüşmeye gencimle birlikte mi gelmeliyiz?\n- Okul saatleri dışında uygun bir saat var mı?',
    cift: '## Sizi anlıyoruz\nİlişkinizle ilgili destek aramanız, onu önemsediğinizi gösteriyor. Pek çok çift benzer döngülerle başvuruyor ve bunu konuşmak çoğu zaman ilk rahatlamayı getiriyor.\n## İlk görüşmede neler olur\n- İkinizin de ilişkiyi nasıl yaşadığı ayrı ayrı dinlenir.\n- Tartışmalarınızda tekrar eden döngüye birlikte bakılır.\n- Nasıl bir çalışma planıyla ilerleneceği konuşulur.\n## Görüşmeden önce küçük hazırlık\n- Görüşmeye ikinizin birlikte gelmesi en sık tercih edilen başlangıçtır; gerekirse bireysel görüşmeler de planlanır.\n- Son dönemde sizi en çok yoran bir tartışmayı kısaca not edin.\n- İlişkinizde neyin değişmesini istediğinizi tek cümleyle yazın.\n## Telefonda sorabilecekleriniz\n- İkimizin de uygun olduğu bir akşam ya da Cumartesi saati var mı?\n- İlk görüşmeye birimiz önce gelebilir mi?'
  };

  /* ---------- Ölçüm ---------- */
  function olay(ad, ek) {
    w.dataLayer = w.dataLayer || [];
    var p = { event: ad, pusula_site: SITE };
    if (ek) for (var k in ek) p[k] = ek[k];
    w.dataLayer.push(p);
  }

  /* ---------- Mesai durumu (Pzt–Cmt 09:00–20:00, İstanbul) ---------- */
  function mesai() {
    try {
      var p = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Istanbul', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var g = function (t) { for (var i = 0; i < p.length; i++) if (p[i].type === t) return p[i].value; return ''; };
      var day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(g('weekday'));
      var m = (parseInt(g('hour'), 10) % 24) * 60 + parseInt(g('minute'), 10);
      return { acik: day >= 1 && day <= 6 && m >= 540 && m < 1200, pazartesi: (day === 6 && m >= 1200) || day === 0, sabahOnce: m < 540 };
    } catch (e) { return { acik: true }; }
  }

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function seldaAvatar() {
    return SELDA_FOTO ? '<img class="pu-av" src="' + esc(SELDA_FOTO) + '" alt="' + SELDA + '">' : '<span class="pu-av" aria-hidden="true">S</span>';
  }
  function titret() { try { if (navigator.vibrate) navigator.vibrate(8); } catch (e) {} }

  /* ---------- Görünüm ---------- */
  var TEMA = SITE === 'cayyolu'
    ? '--pu-a:#14264A;--pu-a2:#2C4A86;--pu-hl:#E9A23B;--pu-bg:#F2F6FB;--pu-ink:#18223A;--pu-mut:#566179;--pu-line:#DCE4F0;'
    : SITE === 'elif'
    ? '--pu-a:#0e9e79;--pu-a2:#062b20;--pu-hl:#34D399;--pu-bg:#F3FBF7;--pu-ink:#062b20;--pu-mut:#4b635a;--pu-line:#D5EDE3;'
    : '--pu-a:#6B3A8C;--pu-a2:#3d1e54;--pu-hl:#C9A06B;--pu-bg:#FBF8F2;--pu-ink:#2A1F2D;--pu-mut:#766b78;--pu-line:#E8DFD0;';
  var CSS = ''
    + '.pu-root{' + TEMA + '--pu-call:#16A34A;position:fixed;inset:0;z-index:2147483000;display:flex;align-items:flex-end;justify-content:center;font-family:inherit;color:var(--pu-ink)}'
    + '.pu-root *{box-sizing:border-box}'
    + '.pu-veil{position:absolute;inset:0;background:rgba(18,12,24,.55);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);opacity:0;transition:opacity .3s}'
    + '.pu-root.on .pu-veil{opacity:1}'
    + '.pu-sheet{position:relative;width:100%;max-width:560px;height:94vh;height:94dvh;background:var(--pu-bg);border-radius:26px 26px 0 0;box-shadow:0 -20px 60px rgba(0,0,0,.25);display:flex;flex-direction:column;overflow:hidden;transform:translateY(40px);opacity:0;transition:transform .45s cubic-bezier(.2,.9,.25,1),opacity .3s}'
    + '@media(min-width:700px){.pu-root{align-items:center}.pu-sheet{height:min(860px,92vh);border-radius:26px}}'
    + '.pu-root.on .pu-sheet{transform:none;opacity:1}'
    + '.pu-aura{position:absolute;inset:-30% -30% auto;height:360px;background:radial-gradient(closest-side,color-mix(in srgb,var(--pu-a) 30%,transparent),transparent),radial-gradient(closest-side at 80% 40%,color-mix(in srgb,var(--pu-hl) 35%,transparent),transparent);filter:blur(30px);opacity:.55;pointer-events:none;animation:pu-drift 14s ease-in-out infinite alternate}'
    + '@keyframes pu-drift{to{transform:translate(8%,6%) rotate(8deg)}}'
    + '.pu-top{position:relative;display:flex;align-items:center;gap:10px;padding:14px 16px 8px}'
    + '.pu-back,.pu-x{width:40px;height:40px;border-radius:50%;border:1px solid var(--pu-line);background:#fff;color:var(--pu-ink);font-size:20px;line-height:1;cursor:pointer;display:grid;place-items:center;flex:none}'
    + '.pu-back[hidden]{visibility:hidden;display:grid}'
    + '.pu-prog{flex:1;height:6px;border-radius:9px;background:var(--pu-line);overflow:hidden}'
    + '.pu-prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--pu-a),var(--pu-hl));border-radius:9px;transition:width .5s cubic-bezier(.2,.9,.25,1)}'
    + '.pu-body{position:relative;flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:6px 18px 24px}'
    + '.pu-step{animation:pu-in .45s cubic-bezier(.2,.9,.25,1) both}'
    + '@keyframes pu-in{from{opacity:0;transform:translateY(14px)}}'
    + '.pu-ey{font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--pu-a)}'
    + '.pu-h{font-size:clamp(23px,6vw,29px);line-height:1.18;margin:8px 0 6px;font-weight:700;color:var(--pu-a2)}'
    + '.pu-p{margin:0 0 16px;color:var(--pu-mut);font-size:15px;line-height:1.55}'
    + '.pu-cards{display:grid;gap:10px}'
    + '.pu-card{display:flex;align-items:center;gap:14px;width:100%;text-align:left;padding:15px 16px;border-radius:18px;border:1.5px solid var(--pu-line);background:#fff;cursor:pointer;font:inherit;color:inherit;transition:transform .15s,border-color .2s,box-shadow .2s}'
    + '.pu-card:hover,.pu-card:focus-visible{border-color:var(--pu-a);box-shadow:0 8px 24px -14px var(--pu-a);outline:none}'
    + '.pu-card:active{transform:scale(.985)}'
    + '.pu-card .pu-i{font-size:26px;width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:var(--pu-bg);flex:none}'
    + '.pu-card b{display:block;font-size:16.5px}.pu-card small{display:block;color:var(--pu-mut);font-size:13px;margin-top:2px}'
    + '.pu-chips{display:flex;flex-wrap:wrap;gap:9px}'
    + '.pu-chip{padding:12px 16px;border-radius:999px;border:1.5px solid var(--pu-line);background:#fff;font:inherit;font-size:15px;font-weight:600;color:inherit;cursor:pointer;transition:transform .15s,border-color .2s,background .2s}'
    + '.pu-chip:hover,.pu-chip:focus-visible{border-color:var(--pu-a);outline:none}'
    + '.pu-chip:active{transform:scale(.96)}'
    + '.pu-sos{margin-top:18px;width:100%;padding:12px 14px;border-radius:14px;border:1.5px dashed #D9534F;background:#FFF6F5;color:#A12622;font:inherit;font-size:14px;font-weight:700;cursor:pointer;text-align:left}'
    + '.pu-safe{margin-top:16px;font-size:12.5px;color:var(--pu-mut);display:flex;gap:8px;align-items:flex-start;line-height:1.45}'
    + '.pu-orbw{display:grid;place-items:center;padding:34px 0 10px}'
    + '.pu-orb{position:relative;width:150px;height:150px;border-radius:50%;display:grid;place-items:center}'
    + '.pu-orb:before,.pu-orb:after{content:"";position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,var(--pu-a),var(--pu-hl),var(--pu-a2),var(--pu-a));animation:pu-spin 2.4s linear infinite;filter:blur(1px)}'
    + '.pu-orb:after{inset:-14px;filter:blur(22px);opacity:.55;animation-duration:3.6s}'
    + '.pu-orb img{position:relative;z-index:1;width:128px;height:128px;border-radius:50%;object-fit:cover;border:4px solid var(--pu-bg)}'
    + '@keyframes pu-spin{to{transform:rotate(360deg)}}'
    + '.pu-lines{list-style:none;margin:22px auto 0;padding:0;max-width:330px;display:grid;gap:10px}'
    + '.pu-lines li{display:flex;gap:10px;align-items:center;font-size:15px;color:var(--pu-mut);opacity:.35;transition:opacity .4s,color .4s}'
    + '.pu-lines li.on{opacity:1;color:var(--pu-ink)}'
    + '.pu-lines li i{width:20px;height:20px;border-radius:50%;border:2px solid var(--pu-line);flex:none;display:grid;place-items:center;font-style:normal;font-size:12px;color:#fff;transition:all .3s}'
    + '.pu-lines li.ok i{background:var(--pu-a);border-color:var(--pu-a)}'
    + '.pu-exp{display:flex;gap:14px;align-items:center;padding:14px;border-radius:20px;background:#fff;border:1px solid var(--pu-line);box-shadow:0 18px 40px -26px var(--pu-a2);animation:pu-in .5s .05s both}'
    + '.pu-ph{position:relative;width:78px;height:78px;flex:none;border-radius:50%;padding:3px;background:conic-gradient(var(--pu-a),var(--pu-hl),var(--pu-a))}'
    + '.pu-ph img{width:100%;height:100%;border-radius:50%;object-fit:cover;border:3px solid #fff;display:block}'
    + '.pu-ph:after{content:"";position:absolute;right:2px;bottom:4px;width:16px;height:16px;border-radius:50%;background:var(--pu-call);border:3px solid #fff}'
    + '.pu-exp small{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--pu-a)}'
    + '.pu-exp b{display:block;font-size:19px;color:var(--pu-a2);margin-top:2px}'
    + '.pu-exp span{display:block;font-size:13px;color:var(--pu-mut)}'
    + '.pu-tags{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 0}'
    + '.pu-tags em{font-style:normal;font-size:12px;font-weight:700;padding:6px 10px;border-radius:999px;background:#fff;border:1px solid var(--pu-line);color:var(--pu-a2)}'
    + '.pu-why{margin:12px 2px 0;font-size:14.5px;line-height:1.55}'
    + '.pu-q{margin:16px 0 0;padding:16px 16px 14px;border-radius:18px;background:linear-gradient(135deg,#fff,var(--pu-bg));border:1px solid var(--pu-line);position:relative;animation:pu-in .5s .15s both}'
    + '.pu-q:before{content:"“";position:absolute;top:-6px;left:12px;font:700 56px/1 Georgia,serif;color:var(--pu-hl);opacity:.6}'
    + '.pu-q p{margin:0;font-style:italic;font-size:15px;line-height:1.65;padding-top:10px}'
    + '.pu-q small{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:10px;font-size:12.5px;color:var(--pu-mut)}'
    + '.pu-q a{color:var(--pu-a);font-weight:700;text-decoration:none}'
    + '.pu-ai{margin-top:18px;padding:16px;border-radius:18px;background:#fff;border:1px solid var(--pu-line);min-height:120px}'
    + '.pu-ai-h{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--pu-a)}'
    + '.pu-ai-h i{width:8px;height:8px;border-radius:50%;background:var(--pu-hl);animation:pu-pulse 1.2s ease-in-out infinite}'
    + '.pu-ai.done .pu-ai-h i{animation:none;background:var(--pu-call)}'
    + '@keyframes pu-pulse{50%{opacity:.25;transform:scale(.7)}}'
    + '.pu-ai h4{margin:18px 0 8px;font-size:17px;line-height:1.3;font-weight:700;color:var(--pu-a2)}'
    + '.pu-ai p{margin:0;font-size:15px;line-height:1.6}'
    + '.pu-ai ul{margin:0;padding:0 0 0 2px;list-style:none;display:grid;gap:7px}'
    + '.pu-ai li{position:relative;padding-left:20px;font-size:15px;line-height:1.55}'
    + '.pu-ai li:before{content:"";position:absolute;left:3px;top:.62em;width:7px;height:7px;border-radius:50%;background:var(--pu-hl)}'
    + '.pu-bekle{color:var(--pu-mut)!important;margin:12px 0 10px!important}'
    + '.pu-sk{display:block;height:12px;border-radius:8px;margin:9px 0;background:linear-gradient(90deg,var(--pu-line),#fff,var(--pu-line));background-size:200% 100%;animation:pu-sk 1.4s linear infinite}'
    + '@keyframes pu-sk{to{background-position:-200% 0}}'
    + '.pu-cur{display:inline-block;width:2px;height:1.05em;background:var(--pu-a);vertical-align:-2px;margin-left:2px;animation:pu-blink .9s step-end infinite}'
    + '@keyframes pu-blink{50%{opacity:0}}'
    + '.pu-facts{margin-top:14px;display:grid;gap:8px}'
    + '.pu-fact{display:flex;gap:10px;align-items:flex-start;padding:12px 14px;border-radius:14px;background:#fff;border:1px solid var(--pu-line);font-size:14px;line-height:1.45}'
    + '.pu-fact b{color:var(--pu-a2)}'
    + '.pu-selda{align-items:center;background:linear-gradient(135deg,#fff,var(--pu-bg))}'
    + '.pu-av{width:44px;height:44px;border-radius:50%;flex:none;object-fit:cover;display:grid;place-items:center;font-weight:800;font-size:18px;color:#fff;background:linear-gradient(135deg,var(--pu-a),var(--pu-hl));box-shadow:0 0 0 3px #fff,0 0 0 5px var(--pu-call)}'
    + '.pu-note{margin:14px 2px 0;font-size:12px;color:var(--pu-mut);line-height:1.5}'
    + '.pu-foot{position:relative;padding:12px 16px calc(12px + env(safe-area-inset-bottom));background:rgba(255,255,255,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid var(--pu-line)}'
    + '.pu-foot[hidden]{display:none}'
    + '.pu-call{position:relative;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;padding:17px 18px;border-radius:16px;background:var(--pu-call);color:#fff!important;font-size:18px;font-weight:800;text-decoration:none;box-shadow:0 14px 30px -12px rgba(22,163,74,.75);overflow:hidden}'
    + '.pu-call:before{content:"";position:absolute;inset:0;border-radius:16px;box-shadow:0 0 0 0 rgba(22,163,74,.55);animation:pu-ring 2s ease-out infinite}'
    + '.pu-call:after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg);animation:pu-shine 3.2s ease-in-out infinite}'
    + '@keyframes pu-ring{70%{box-shadow:0 0 0 14px rgba(22,163,74,0)}100%{box-shadow:0 0 0 0 rgba(22,163,74,0)}}'
    + '@keyframes pu-shine{60%,100%{left:130%}}'
    + '.pu-call small{display:block;font-size:12.5px;font-weight:600;opacity:.92}'
    + '.pu-root a.pu-sub[href],.pu-sub{display:block;text-align:center;margin-top:9px;padding:0!important;background:none!important;box-shadow:none!important;border:0!important;font-size:13.5px;font-weight:600;color:var(--pu-mut)!important;text-decoration:underline;text-underline-offset:3px}'
    + '.pu-112{border:0;cursor:pointer;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;padding:18px;border-radius:16px;background:#C62828;color:#fff!important;font-size:20px;font-weight:800;text-decoration:none;margin:18px 0 10px}'
    + '.pu-launch{display:inline-flex;align-items:center;gap:10px;margin-top:12px;padding:12px 18px 12px 12px;border-radius:999px;border:0;cursor:pointer;font:inherit;font-weight:700;font-size:15px;color:#fff;background:linear-gradient(120deg,var(--pu-a2),var(--pu-a) 55%,var(--pu-hl));background-size:200% 100%;box-shadow:0 12px 26px -12px var(--pu-a2);animation:pu-grad 6s ease-in-out infinite alternate;text-align:left}'
    + '.pu-launch .pu-spark{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.22);display:grid;place-items:center;font-size:16px;flex:none}'
    + '.pu-launch small{display:block;font-weight:500;font-size:12px;opacity:.9}'
    + '@keyframes pu-grad{to{background-position:100% 0}}'
    + '.pu-band{' + TEMA + 'margin:28px auto;max-width:1100px;padding:0 16px}'
    + '.pu-band-in{position:relative;overflow:hidden;display:flex;flex-wrap:wrap;align-items:center;gap:16px 22px;padding:22px;border-radius:24px;background:linear-gradient(135deg,var(--pu-a2),var(--pu-a));color:#fff}'
    + '.pu-band-in:after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:radial-gradient(closest-side,var(--pu-hl),transparent);opacity:.45}'
    + '.pu-band img{width:64px;height:64px;border-radius:50%;object-fit:cover;border:3px solid rgba(255,255,255,.7);flex:none}'
    + '.pu-band-t{flex:1;min-width:200px;position:relative;z-index:1}'
    + '.pu-band-t b{display:block;font-size:19px;line-height:1.3}.pu-band-t span{display:block;opacity:.88;font-size:14px;margin-top:4px}'
    + '.pu-band button{position:relative;z-index:1;padding:14px 20px;border-radius:999px;border:0;background:#fff;color:var(--pu-a2);font:inherit;font-weight:800;font-size:15px;cursor:pointer}'
    + 'html.pu-lock,html.pu-lock body{overflow:hidden!important}'
    + '@media(prefers-reduced-motion:reduce){.pu-root *,.pu-launch,.pu-sb *{animation:none!important;transition:none!important}}';

  var stil = false;
  function stilEkle() {
    if (stil) return; stil = true;
    var s = d.createElement('style'); s.textContent = CSS; d.head.appendChild(s);
  }

  /* ---------- Durum ---------- */
  var root, body, prog, back, foot, secim = {}, adimlar = [], gecmisEkli = false, istek = null;

  function el(html) { var t = d.createElement('div'); t.innerHTML = html.trim(); var c = t.firstChild; t.removeChild(c); return c; }

  function kur() {
    stilEkle();
    root = el('<div class="pu-root" role="dialog" aria-modal="true" aria-label="Size özel yol haritası" data-cta-area="pusula">'
      + '<div class="pu-veil"></div><div class="pu-sheet"><div class="pu-aura"></div>'
      + '<div class="pu-top"><button class="pu-back" type="button" aria-label="Geri" hidden>‹</button><div class="pu-prog"><i></i></div><button class="pu-x" type="button" aria-label="Kapat">×</button></div>'
      + '<div class="pu-body"></div><div class="pu-foot" hidden></div></div></div>');
    body = root.querySelector('.pu-body');
    prog = root.querySelector('.pu-prog i');
    back = root.querySelector('.pu-back');
    foot = root.querySelector('.pu-foot');
    root.querySelector('.pu-x').onclick = kapat;
    root.querySelector('.pu-veil').onclick = kapat;
    back.onclick = geri;
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root && root.parentNode) kapat(); });
  }

  function ac(kaynak) {
    if (!root) kur();
    if (root.parentNode) return;
    secim = {}; adimlar = [];
    d.body.appendChild(root);
    d.documentElement.classList.add('pu-lock');
    requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('on'); }); });
    try { history.pushState({ pusula: 1 }, ''); gecmisEkli = true; } catch (e) { gecmisEkli = false; }
    olay('pusula_acildi', { pusula_kaynak: kaynak || 'diger' });
    adimKim();
  }

  function kapat(gecmistenGeldi) {
    if (!root || !root.parentNode) return;
    if (istek) { try { istek.abort(); } catch (e) {} istek = null; }
    root.classList.remove('on');
    d.documentElement.classList.remove('pu-lock');
    setTimeout(function () { if (root.parentNode) root.parentNode.removeChild(root); }, 320);
    if (gecmisEkli && gecmistenGeldi !== true) { gecmisEkli = false; try { history.back(); } catch (e) {} }
    gecmisEkli = false;
  }
  w.addEventListener('popstate', function () { if (root && root.parentNode) { gecmisEkli = false; kapat(true); } });

  function goster(html, oran, geriVar) {
    if (istek) { try { istek.abort(); } catch (e) {} istek = null; }
    body.innerHTML = '<div class="pu-step">' + html + '</div>';
    body.scrollTop = 0;
    prog.style.width = oran + '%';
    back.hidden = !geriVar;
    foot.hidden = true; foot.innerHTML = '';
  }
  function ileri(fn) { adimlar.push(fn); fn(); }
  function geri() { adimlar.pop(); var f = adimlar[adimlar.length - 1]; if (f) f(); }

  var GUVEN = '<div class="pu-safe"><span>🔒</span><span>İsim ya da telefon istemiyoruz. Seçimleriniz kaydedilmez.</span></div>';

  function adimKim() {
    adimlar = [adimKim];
    goster('<div class="pu-ey">Size özel yol haritası · 60 sn</div>'
      + '<h2 class="pu-h">Kim için destek arıyorsunuz?</h2>'
      + '<p class="pu-p">Birkaç dokunuşla size uygun uzmanı ve ilk görüşmede sizi neyin beklediğini görün.</p>'
      + '<div class="pu-cards">' + KIM.map(function (x) { return '<button type="button" class="pu-card" data-v="' + x.k + '"><span class="pu-i">' + x.i + '</span><span><b>' + x.t + '</b><small>' + x.s + '</small></span></button>'; }).join('') + '</div>' + GUVEN, 12, false);
    sec('.pu-card', function (v) { secim = { kim: v }; ileri(v === 'cocugum' ? adimYas : adimKonu); });
  }

  function adimYas() {
    goster('<div class="pu-ey">Adım 2</div><h2 class="pu-h">Çocuğunuz kaç yaşında?</h2><p class="pu-p">Yaşa göre görüşmenin nasıl ilerleyeceği değişir.</p>'
      + '<div class="pu-chips">' + YAS.map(function (x) { return '<button type="button" class="pu-chip" data-v="' + x[0] + '">' + x[1] + '</button>'; }).join('') + '</div>', 30, true);
    sec('.pu-chip', function (v) {
      if (v === '12+') { secim = { kim: 'ergen' }; } else { secim.yas = v; }
      ileri(adimKonu);
    });
  }

  function adimKonu() {
    var kim = secim.kim;
    var soru = { kendim: 'Sizi en çok ne zorluyor?', cocugum: 'Çocuğunuzda sizi en çok ne düşündürüyor?', ergen: 'Gencinizde sizi en çok ne düşündürüyor?', cift: 'İlişkinizde sizi en çok ne zorluyor?' }[kim];
    var sos = kim === 'kendim' || kim === 'cift' ? 'Şu an kendimi güvende hissetmiyorum' : 'Çocuğumun şu anki güvenliğinden endişeliyim';
    goster('<div class="pu-ey">Adım ' + (kim === 'cocugum' ? 3 : 2) + '</div><h2 class="pu-h">' + soru + '</h2><p class="pu-p">En yakın olanı seçin. Tanı koymuyoruz; yalnızca ilk görüşmeyi size göre anlatıyoruz.</p>'
      + '<div class="pu-chips">' + KONU[kim].map(function (x) { return '<button type="button" class="pu-chip" data-v="' + x[0] + '">' + x[1] + '</button>'; }).join('') + '</div>'
      + '<button type="button" class="pu-sos" data-sos>⚠️ ' + sos + '</button>', kim === 'cocugum' ? 52 : 42, true);
    sec('.pu-chip', function (v) { secim.konu = v; ileri(adimYer); });
    body.querySelector('[data-sos]').onclick = function () { titret(); ileri(adimKriz); };
  }

  function adimYer() {
    goster('<div class="pu-ey">Son adım</div><h2 class="pu-h">Görüşmeyi nerede yapmak istersiniz?</h2><p class="pu-p">İki şubemizde yüz yüze ya da online görüşebilirsiniz.</p>'
      + '<div class="pu-cards">' + YER.map(function (x) { return '<button type="button" class="pu-card" data-v="' + x.k + '"><span class="pu-i">' + x.i + '</span><span><b>' + x.t + '</b><small>' + x.s + '</small></span></button>'; }).join('') + '</div>', 75, true);
    sec('.pu-card', function (v) { secim.yer = v; ileri(adimSonuc); });
  }

  function adimKriz() {
    olay('pusula_kriz');
    goster('<div class="pu-ey" style="color:#C62828">Önce güvenliğiniz</div><h2 class="pu-h">Şu an güvende değilseniz lütfen hemen 112\'yi arayın.</h2>'
      + '<p class="pu-p">Kendinize ya da bir başkasına zarar verme düşüncesi, acil bir sağlık durumudur. 112 Acil Çağrı Merkezi 7/24 ücretsiz ulaşılabilir; en yakın acil servise de başvurabilirsiniz.</p>'
      + '<button type="button" class="pu-112" data-112>📞 112\'yi Ara</button>'
      + '<p class="pu-p">Yanınızda güvendiğiniz birinin olmasını isteyin. Acil durum geçtiğinde ya da durum acil değilse bizi arayabilirsiniz; ekibimiz size yol gösterir.</p>'
      + '<a class="pu-sub" style="font-size:15px" href="' + TEL + '">Acil değil: RN Psikoloji\'yi ara · ' + TEL_TXT + '</a>', 100, true);
    // Bağlantı değil düğme: 112 araması reklam dönüşümü olarak sayılmasın (ads-conversion.js tel: bağlantılarını sayar)
    body.querySelector('[data-112]').onclick = function () { location.href = 'tel:112'; };
  }

  function sec(sel, fn) {
    var b = body.querySelectorAll(sel);
    for (var i = 0; i < b.length; i++) b[i].onclick = function () { titret(); fn(this.getAttribute('data-v')); };
  }

  /* ---------- Sonuç ---------- */
  function adimSonuc() {
    var s = secim;
    var yasEtiket = s.yas ? (s.yas === '3-6' ? '3–6 yaş' : '7–11 yaş') : '';
    var konuEtiket = (KONU[s.kim].filter(function (x) { return x[0] === s.konu; })[0] || [])[1] || '';
    var kimEtiket = KIM.filter(function (x) { return x.k === s.kim; })[0].t;
    var yerEtiket = YER.filter(function (x) { return x.k === s.yer; })[0].t;
    var uz = uzmanSec(s), U = uzmanProfil(uz, s);
    olay('pusula_analiz', { pusula_uzman: uz });

    // 1) Analiz ekranı
    goster('<div class="pu-orbw"><div class="pu-orb"><img src="' + esc(U.foto) + '" alt=""></div></div>'
      + '<h2 class="pu-h" style="text-align:center">Yol haritanız hazırlanıyor</h2>'
      + '<ul class="pu-lines"><li><i>✓</i>Seçimleriniz eşleştiriliyor</li><li><i>✓</i>' + esc(U.notlar) + '</li><li><i>✓</i>İlk görüşme planınız yazılıyor</li></ul>', 92, false);
    var li = body.querySelectorAll('.pu-lines li'), n = 0;
    var tik = setInterval(function () {
      if (n > 0) li[n - 1].classList.add('ok');
      if (n < li.length) li[n].classList.add('on');
      n++; if (n > li.length) clearInterval(tik);
    }, REDUCED ? 150 : 650);

    var metin = '', bitti = false, yedek = false, kuyruk = '', yazilan = '';
    var basla = Date.now();
    var ctrl = w.AbortController ? new AbortController() : null;

    function yedegeGec() { if (!yedek) { yedek = true; metin = YEDEK[s.kim]; bitti = true; } }

    try {
      fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ kim: s.kim, konu: s.konu, yas: s.yas, yer: s.yer, uzman: uz }), signal: ctrl && ctrl.signal })
        .then(function (r) {
          if (!r.ok) throw new Error('durum ' + r.status);
          if (!r.body || !r.body.getReader || !w.TextDecoder) return r.text().then(function (t) { metin = t; bitti = true; });
          var rd = r.body.getReader(), dec = new TextDecoder();
          function oku() {
            return rd.read().then(function (x) {
              if (x.done) { bitti = true; return; }
              metin += dec.decode(x.value, { stream: true });
              return oku();
            });
          }
          return oku();
        })
        .then(function () { if (metin.indexOf('§YEDEK') >= 0 || (metin.match(/^## /gm) || []).length < 4) yedegeGec(); })
        .catch(function (e) { if (!(e && e.name === 'AbortError')) yedegeGec(); });
    } catch (e) { yedegeGec(); }
    // 20 sn içinde hiç metin gelmezse beklemeden hazır metne geç
    var zaman = setTimeout(function () { if (!metin) { if (ctrl) ctrl.abort(); yedegeGec(); } }, 20000);
    istek = { abort: function () { clearInterval(tik); clearTimeout(zaman); if (ctrl) ctrl.abort(); } };

    // 2) Sonuç kartı (analiz animasyonu en az ~2 sn görünür)
    var bekle = REDUCED ? 300 : 2200;
    var hazirMi = setInterval(function () {
      if (Date.now() - basla < bekle) return;
      clearInterval(hazirMi); clearInterval(tik);
      sonucCiz();
    }, 120);
    var eski = istek.abort;
    istek.abort = function () { clearInterval(hazirMi); eski(); };

    function sonucCiz() {
      var not = U.not;
      var ozet = [kimEtiket, yasEtiket, konuEtiket, yerEtiket].filter(Boolean).join(' · ');
      // goster() açık isteği iptal eder; akış sürerken sonuç kartına geçiyoruz, istek yaşamalı
      var tut = istek; istek = null;
      goster('<div class="pu-ey">Yol haritanız hazır</div>'
        + '<p class="pu-p" style="margin:6px 0 14px">' + esc(ozet) + '</p>'
        + '<div class="pu-exp"><div class="pu-ph"><img src="' + esc(U.foto) + '" alt="' + esc(U.ad) + '"></div><div><small>Sizin için önerilen uzman</small><b>' + esc(U.ad) + '</b><span>' + esc(U.unvan) + '</span></div></div>'
        + '<div class="pu-tags">' + U.etiket.map(function (t) { return '<em>' + esc(t) + '</em>'; }).join('') + '</div>'
        + '<p class="pu-why">' + esc(U.neden) + '</p>'
        + (not ? '<figure class="pu-q"><p>' + esc(not[2]) + '</p><small><span>' + esc(U.ad) + ' · ' + esc(not[1]) + '</span><a href="' + U.notTaban + not[0] + '" target="_blank" rel="noopener">Notun tamamı →</a></small></figure>' : '')
        + '<section class="pu-ai" aria-live="polite"><div class="pu-ai-h"><i></i><span>Size özel ilk görüşme yol haritası</span></div><div class="pu-ai-b"></div></section>'
        + '<div class="pu-facts">'
        + '<div class="pu-fact"><span>📍</span><span>' + esc(SUBE[s.yer]) + '</span></div>'
        + '<div class="pu-fact pu-selda">' + seldaAvatar() + '<span><b>Telefonu ' + SELDA + ' açar.</b> Size en yakın uygun saati ve ücret bilgisini hemen söyler. Ne anlatacağınızı düşünmenize gerek yok; bu yol haritasını okumanız yeterli.</span></div>'
        + '</div>'
        + '<p class="pu-note">Bu yol haritası genel bilgilendirmedir; tanı ya da tedavi önerisi değildir. Acil bir durumda 112\'yi arayın.</p>', 100, true);
      istek = tut;
      cta();
      olay('pusula_sonuc', { pusula_uzman: uz, pusula_kaynak_metin: yedek ? 'hazir' : 'kisiye_ozel' });
      yaz();
    }

    // Akan metni harf harf yaz (sunucudan akarken de, önbellekten gelince de aynı his)
    function yaz() {
      var kutu = body.querySelector('.pu-ai'), hedef = body.querySelector('.pu-ai-b');
      if (!hedef) return;
      var hiz = REDUCED ? 9999 : 3;
      var son = '';
      function adim() {
        if (!hedef.isConnected) return;
        var kaynak = metin.replace(/\n?§YEDEK[\s\S]*$/, '');
        if (yedek && yazilan && kaynak.indexOf(yazilan) !== 0) yazilan = '';
        if (yazilan.length < kaynak.length) yazilan = kaynak.slice(0, yazilan.length + hiz);
        var cizim = yazilan ? ciz(yazilan) + (bitti && yazilan.length >= kaynak.length ? '' : '<span class="pu-cur"></span>')
          : '<p class="pu-bekle">Seçimlerinize göre hazırlanıyor<span class="pu-cur"></span></p><i class="pu-sk"></i><i class="pu-sk"></i><i class="pu-sk" style="width:62%"></i>';
        if (cizim !== son) { hedef.innerHTML = cizim; son = cizim; }
        if (bitti && yazilan.length >= kaynak.length) { kutu.classList.add('done'); return; }
        requestAnimationFrame(adim);
      }
      adim();
    }
  }

  function ciz(t) {
    var out = '', liste = false;
    t.split('\n').forEach(function (sat) {
      var x = sat.trim();
      if (!x) return;
      if (/^##\s*/.test(x)) { if (liste) { out += '</ul>'; liste = false; } out += '<h4>' + esc(x.replace(/^##\s*/, '')) + '</h4>'; }
      else if (/^[-•*]\s*/.test(x)) { if (!liste) { out += '<ul>'; liste = true; } out += '<li>' + esc(x.replace(/^[-•*]\s*/, '')) + '</li>'; }
      else { if (liste) { out += '</ul>'; liste = false; } out += '<p>' + esc(x.replace(/\*\*/g, '')) + '</p>'; }
    });
    if (liste) out += '</ul>';
    return out;
  }

  function cta() {
    var m = mesai();
    var waMsg = 'Merhaba, sitenizdeki yol haritasını inceledim. ' + (m.acik ? 'Randevu almak istiyorum.' : (m.pazartesi ? 'Pazartesi sabahı' : 'Sabah') + ' aranmak istiyorum.');
    var waHref = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(waMsg);
    foot.innerHTML = m.acik
      ? '<a class="pu-call" href="' + TEL + '"><span>📞</span><span>' + SELDA + '\'ı Arayın<small>' + TEL_TXT + ' · uygun saati ve ücreti hemen söylesin</small></span></a>'
        + '<a class="pu-sub" href="' + waHref + '" target="_blank" rel="noopener">Yazmayı tercih ederim (WhatsApp)</a>'
      : '<a class="pu-call" href="' + waHref + '" target="_blank" rel="noopener"><span>🌙</span><span>' + (m.pazartesi ? 'Pazartesi' : 'Sabah') + ' ' + SELDA + ' ilk sizi arasın<small>Mesai dışındayız · WhatsApp\'tan bir mesaj yeterli</small></span></a>'
        + '<a class="pu-sub" href="' + TEL + '">Yine de ara · ' + TEL_TXT + '</a>';
    foot.hidden = false;
  }

  /* ---------- Sayfadaki giriş noktaları ---------- */
  function launcherHtml() {
    return '<button type="button" class="pu-launch" data-pusula="hero"><span class="pu-spark">✨</span><span>60 saniyede size özel yol haritası<small>Uzmanınız ve ilk görüşmeniz, sizin seçimlerinize göre</small></span></button>';
  }

  function yerlestir() {
    stilEkle();
    yerlestirOgeler();
    // Tek sayfalı sitede (Elif) içerik sonradan çizilir ve sayfa değişince yeniden çizilir: eksilen öğeyi geri koy
    if (w.MutationObserver) {
      var bekleyen = false;
      new MutationObserver(function () {
        if (bekleyen) return; bekleyen = true;
        setTimeout(function () { bekleyen = false; yerlestirOgeler(); }, 400);
      }).observe(d.body, { childList: true, subtree: true });
    }
  }

  function yerlestirOgeler() {
    // 1) Giriş bölümündeki arama düğmelerinin altına
    var hero = d.querySelector(CFG.heroSecici || '.hero-actions, .hero .cta-row, .hero-ctas');
    if (hero && !d.querySelector('.pu-launch')) {
      var k = el('<div class="pu-launch-w" style="' + TEMA + '">' + launcherHtml() + '</div>');
      hero.parentNode.insertBefore(k, hero.nextSibling);
    }
    // 2) Sayfa sonunda, alt bilgiden önce bant
    var ft = d.querySelector('footer, .site-footer');
    if (ft && !d.querySelector('.pu-band') && !(root && root.contains(ft))) {
      var bant = el('<section class="pu-band" aria-label="Size özel yol haritası"><div class="pu-band-in"><img src="' + esc(FOTO) + '" alt="" loading="lazy"><div class="pu-band-t"><b>Nereden başlayacağınızı bilmiyor musunuz?</b><span>3 dokunuşta size özel ilk görüşme yol haritanızı görün. İsim ya da telefon istemiyoruz.</span></div><button type="button" data-pusula="bant">Yol haritamı göster →</button></div></section>');
      ft.parentNode.insertBefore(bant, ft);
    }
    // 3) Sağ altta "Soru sorun" kutusu (eski canlı sohbetin yerine) ve sayfaya göre akıllı davet
    if (w.__puSoru) return;
    w.__puSoru = true;
    soruKur();
  }

  /* ---------- Soru sorun kutusu ----------
     Sık sorulan sorulara anında yanıt; her yanıtın sonunda arama düğmesi; isteyen numarasını bırakır,
     talep psikologunubul paneline düşer (mesai içinde "şimdi", dışında "sabah 09:00"). Canlı kişi gibi
     davranmaz: yanıtlar RN Psikoloji'nin hazır bilgileridir, telefonu Selda Hanım açar. */
  var TALEP_API = CFG.talepApi || 'https://www.psikologunubul.com.tr/api/talep';
  var AYDINLATMA = 'https://www.psikologunubul.com.tr/kvkk-aydinlatma';
  var EKIP = SITE === 'elif' ? 'Psikolog Elif Erdoğan' : 'Psikolog Rojin Nazik ve Psikolog Elif Erdoğan';
  var SORULAR = [
    ['ucret', 'Ücret ne kadar?', 'Seans ücretini Selda Hanım telefonda net olarak söylüyor. Aynı aramada ilk görüşmenin nasıl ilerleyeceğini ve size uygun saati de öğrenirsiniz.'],
    ['randevu', 'En yakın randevu ne zaman?', 'Boş saatler gün içinde değiştiği için en doğru bilgiyi Selda Hanım verir. Aradığınızda size uygun iki saat önerir.'],
    ['adres', 'Adres ve ulaşım', 'Yaşamkent / Çayyolu: Konutkent, Dumlupınar Blv. No:399 Kat:28 D:121 (ücretsiz otopark, Pazartesi–Cumartesi). Kızılay: Atatürk Blv. No:127 Kat:8, Bakanlıklar (Pazartesi günleri).'],
    ['online', 'Online görüşme var mı?', 'Evet. Ankara dışından ya da yurt dışından görüntülü görüşme yapılabiliyor. Bağlantı bilgisi randevu sonrası iletiliyor.'],
    ['ilk', 'İlk görüşmede ne olur?', 'İlk görüşme bir tanışma ve değerlendirme görüşmesidir: ne yaşadığınız, ne zamandır sürdüğü ve gününüzü nasıl etkilediği konuşulur, çalışma planı birlikte oluşturulur. Her şeyi bir anda anlatmanız gerekmez.'],
    ['cocuk', 'Çocuğum / ergenim için', 'Çocuklarda ilk görüşme genellikle ebeveynle yapılır; ardından çocuğun yaşına uygun görüşmeler planlanır. Küçük çocuklarla oyun terapisi, ergenlerle güvenli ve yargısız bir görüşme ortamı önceliklidir.'],
    ['gizlilik', 'Görüşmeler gizli mi?', 'Evet. Görüşmelerde konuşulanlar gizlidir; yalnız yasal zorunluluk ve can güvenliği gibi istisnalar vardır, bunlar ilk görüşmede açıkça anlatılır.'],
    ['ekip', 'Kimlerle görüşebilirim?', 'Ekibimizde ' + EKIP + ' var. Hangi uzmanın size daha uygun olduğunu Selda Hanım ihtiyacınıza göre birlikte belirler.'],
    ['saat', 'Çalışma saatleri', 'Pazartesi–Cumartesi 09:00–20:00. Mesai dışında numaranızı bırakırsanız Selda Hanım sabah ilk iş sizi arar.']
  ];
  var KONU_DAVET = [
    [/cocuk|pedagog|okul|oyun-terapisi|bosanmayi-cocuga|kardes/, 'Çocuğunuz için 60 saniyede bir yol haritası çıkaralım mı?'],
    [/ergen|sinav|genc/, 'Genciniz için 60 saniyede bir yol haritası çıkaralım mı?'],
    [/cift|evlilik|iliski|aldatil|bosanma/, 'İlişkiniz için 60 saniyede bir yol haritası çıkaralım mı?'],
    [/kaygi|anksiyete|panik|fobi|takinti|okb|stres/, 'Kaygınız için nereden başlayacağınızı 60 saniyede görelim mi?'],
    [/fiyat|ucret/, 'Ücret ve uygun saat için Selda Hanım\'ı arayabilirsiniz, ya da önce 60 saniyelik yol haritanıza bakın.'],
    [/test|mmpi/, 'Psikolojik test için 60 saniyede yol haritanızı görelim mi?']
  ];

  function soruKur() {
    var m = mesai();
    var css = ''
      + '.pu-sb{' + TEMA + '--pu-call:#16A34A;position:fixed;right:14px;bottom:calc(88px + env(safe-area-inset-bottom));z-index:9996;font-family:inherit;color:var(--pu-ink)}'
      + '@media(min-width:861px){.pu-sb{right:24px;bottom:24px}}'
      + '.pu-sb-btn{position:relative;display:flex;align-items:center;gap:8px;height:56px;padding:0 6px 0 6px;border-radius:999px;border:0;cursor:pointer;background:var(--pu-a2);color:#fff;box-shadow:0 14px 30px -10px rgba(0,0,0,.45);font:inherit;font-weight:700;font-size:14px}'
      + '.pu-sb-btn .pu-av{width:44px;height:44px;font-size:17px;box-shadow:0 0 0 2px #fff}'
      + '.pu-sb-btn span.t{display:none;padding-right:12px}'
      + '@media(min-width:861px){.pu-sb-btn span.t{display:inline}}'
      + '.pu-sb-btn i{position:absolute;left:38px;top:6px;width:12px;height:12px;border-radius:50%;background:' + (m.acik ? '#22C55E' : '#F59E0B') + ';border:2px solid var(--pu-a2)}'
      + '.pu-sb-tz{position:absolute;right:0;bottom:66px;width:min(300px,calc(100vw - 28px));padding:12px 34px 12px 14px;border-radius:16px 16px 4px 16px;background:#fff;border:1px solid var(--pu-line);box-shadow:0 18px 40px -16px rgba(0,0,0,.4);font-size:14px;line-height:1.45;cursor:pointer;opacity:0;transform:translateY(10px);transition:all .35s cubic-bezier(.2,.9,.25,1)}'
      + '.pu-sb-tz.on{opacity:1;transform:none}'
      + '.pu-sb-tz b{display:block;color:var(--pu-a2);margin-bottom:2px}'
      + '.pu-sb-tz button{position:absolute;right:6px;top:6px;border:0;background:none;font-size:18px;color:var(--pu-mut);cursor:pointer;padding:2px 6px}'
      + '.pu-sb-p{position:absolute;right:0;bottom:66px;width:min(370px,calc(100vw - 28px));max-height:min(600px,calc(100vh - 170px));display:flex;flex-direction:column;border-radius:20px;background:var(--pu-bg);border:1px solid var(--pu-line);box-shadow:0 24px 60px -18px rgba(0,0,0,.45);overflow:hidden}'
      + '.pu-sb-h{display:flex;align-items:center;gap:10px;padding:12px 12px 12px 14px;background:linear-gradient(135deg,var(--pu-a2),var(--pu-a));color:#fff}'
      + '.pu-sb-h b{display:block;font-size:15px}.pu-sb-h small{display:block;font-size:12px;opacity:.9}'
      + '.pu-sb-h .pu-av{width:40px;height:40px;font-size:16px;box-shadow:0 0 0 2px #fff}'
      + '.pu-sb-h .x{margin-left:auto;width:34px;height:34px;border-radius:50%;border:0;background:rgba(255,255,255,.18);color:#fff;font-size:20px;cursor:pointer}'
      + '.pu-sb-b{flex:1;overflow-y:auto;padding:14px 12px;display:flex;flex-direction:column;gap:8px}'
      + '.pu-sb-m{max-width:88%;padding:10px 12px;border-radius:14px 14px 14px 4px;background:#fff;border:1px solid var(--pu-line);font-size:14.5px;line-height:1.5;animation:pu-in .3s both}'
      + '.pu-sb-m.ben{align-self:flex-end;border-radius:14px 14px 4px 14px;background:var(--pu-a);color:#fff;border-color:var(--pu-a)}'
      + '.pu-sb-m.yaz{color:var(--pu-mut);font-size:13px}'
      + '.pu-sb-c{display:flex;flex-wrap:wrap;gap:6px;padding:4px 0}'
      + '.pu-sb-c button{padding:8px 11px;border-radius:999px;border:1.5px solid var(--pu-line);background:#fff;font:inherit;font-size:13.5px;font-weight:600;color:var(--pu-ink);cursor:pointer}'
      + '.pu-sb-c button.vurgu{border-color:var(--pu-a);color:var(--pu-a2)}'
      + '.pu-sb-f{padding:10px 12px calc(10px + env(safe-area-inset-bottom));background:#fff;border-top:1px solid var(--pu-line);display:grid;gap:7px}'
      + '.pu-sb-f a.ara{display:flex;justify-content:center;align-items:center;gap:8px;padding:13px;border-radius:12px;background:var(--pu-call);color:#fff!important;font-weight:800;font-size:15.5px;text-decoration:none}'
      + '.pu-sb-f button.geri{border:0;background:none;color:var(--pu-mut);font:inherit;font-size:13.5px;font-weight:600;text-decoration:underline;cursor:pointer;padding:2px}'
      + '.pu-sb-form{display:grid;gap:7px}.pu-sb-form input{padding:12px;border-radius:12px;border:1.5px solid var(--pu-line);font:600 16px inherit}'
      + '.pu-sb-form button{padding:12px;border-radius:12px;border:0;background:var(--pu-a2);color:#fff;font:inherit;font-weight:800;cursor:pointer}'
      + '.pu-sb-form small{font-size:11.5px;color:var(--pu-mut)}.pu-sb-form small a{color:var(--pu-mut)}'
      + '.pu-sb-form .err{color:#B42318;font-size:13px}'
      + '.pu-sb{transition:opacity .25s,transform .25s}.pu-sb.gizli{opacity:0;transform:translateY(12px);pointer-events:none}'
      + 'html.pu-lock .pu-sb{display:none}';
    var st = d.createElement('style'); st.textContent = css; d.head.appendChild(st);

    var kutu = el('<div class="pu-sb" data-cta-area="soru_kutusu"><button type="button" class="pu-sb-btn" aria-label="Soru sorun">' + seldaAvatar() + '<i></i><span class="t">Soru sorun</span></button></div>');
    d.body.appendChild(kutu);
    var panel = null, davet = null, etkilesti = false;
    // Telefonda balon, giriş bölümündeki arama düğmelerinin üstüne binmesin: ilk ekran geçilince görünür
    function balonKonum() {
      var gizle = innerWidth < 861 && (scrollY || pageYOffset || 0) < 520 && !panel && !davet;
      kutu.classList.toggle('gizli', gizle);
      // Alttaki sabit arama çubuğu (her sitede farklı yükseklik) varsa balon onun üstünde durur
      var h = altCubuk(); kutu.style.bottom = h ? (h + 12) + 'px' : '';
    }
    function altCubuk() {
      var m = 0, L = d.querySelectorAll('.rn-sticky-bar,.sticky-bar,.mobile-cta-bar,.mobile-leadbar,.bar');
      for (var i = 0; i < L.length; i++) {
        var cs = getComputedStyle(L[i]); if (cs.position !== 'fixed' || cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
        var r = L[i].getBoundingClientRect(); if (r.height < 20 || r.bottom < innerHeight - 40) continue;
        m = Math.max(m, innerHeight - r.top);
      }
      return m;
    }
    setTimeout(balonKonum, 800); setTimeout(balonKonum, 2500);
    balonKonum();
    var bkBekle = false;
    w.addEventListener('scroll', function () { if (bkBekle) return; bkBekle = true; requestAnimationFrame(function () { bkBekle = false; balonKonum(); }); }, { passive: true });
    w.addEventListener('resize', balonKonum);

    function kapatDavet() { if (davet) { var x = davet; davet = null; x.classList.remove('on'); setTimeout(function () { if (x.parentNode) x.parentNode.removeChild(x); balonKonum(); }, 350); } }

    function panelAc(kaynak) {
      kapatDavet(); etkilesti = true;
      if (panel) { panel.parentNode.removeChild(panel); panel = null; balonKonum(); return; }
      olay('soru_kutusu_acildi', { pusula_kaynak: kaynak || 'balon' });
      var mm = mesai();
      panel = el('<div class="pu-sb-p" role="dialog" aria-label="Soru sorun"><div class="pu-sb-h">' + seldaAvatar() + '<div><b>RN Psikoloji</b><small>' + (mm.acik ? '🟢 Şu an açığız · Telefonu Selda Hanım açar' : '🌙 Mesai dışı · Sabah 09:00\'da arıyoruz') + '</small></div><button type="button" class="x" aria-label="Kapat">×</button></div><div class="pu-sb-b"></div><div class="pu-sb-f"></div></div>');
      kutu.appendChild(panel);
      panel.querySelector('.x').onclick = function () { panelAc(); };
      var govde = panel.querySelector('.pu-sb-b'), alt = panel.querySelector('.pu-sb-f');
      function mesaj(t, sinif) { var b = d.createElement('div'); b.className = 'pu-sb-m' + (sinif ? ' ' + sinif : ''); b.textContent = t; govde.appendChild(b); govde.scrollTop = govde.scrollHeight; return b; }
      function secenekler(kaydirma) {
        var c = d.createElement('div'); c.className = 'pu-sb-c';
        var testVar = !/^\/(randevu|kaygi-testi|depresyon-testi)\//.test(location.pathname);
        c.innerHTML = '<button type="button" class="vurgu" data-yh>✨ Bana özel yol haritası (60 sn)</button>'
          + (testVar ? '<button type="button" data-test="/kaygi-testi/">🧭 Kaygı testi</button><button type="button" data-test="/depresyon-testi/">🧭 Depresyon testi</button>' : '') + SORULAR.map(function (q) { return '<button type="button" data-q="' + q[0] + '">' + esc(q[1]) + '</button>'; }).join('');
        govde.appendChild(c); if (kaydirma !== false) govde.scrollTop = govde.scrollHeight;
        c.querySelector('[data-yh]').onclick = function () { panelAc(); ac('soru_kutusu'); };
        var ts = c.querySelectorAll('[data-test]');
        for (var t = 0; t < ts.length; t++) ts[t].onclick = function () { olay('soru_test', { test: this.getAttribute('data-test') }); location.href = this.getAttribute('data-test'); };
        var bs = c.querySelectorAll('[data-q]');
        for (var i = 0; i < bs.length; i++) bs[i].onclick = function () {
          var id = this.getAttribute('data-q'), q = SORULAR.filter(function (x) { return x[0] === id; })[0];
          titret(); if (c.parentNode) c.parentNode.removeChild(c);
          mesaj(q[1], 'ben');
          var y = mesaj('yazıyor…', 'yaz');
          olay('soru_secildi', { soru: id });
          setTimeout(function () {
            if (y.parentNode) y.parentNode.removeChild(y);
            var cevap = mesaj(q[2]); secenekler(false);
            govde.scrollTop = Math.max(0, cevap.offsetTop - govde.offsetTop - 70); // soru ve cevap görünsün
          }, REDUCED ? 0 : 650);
        };
      }
      mesaj('Merhaba 👋 Merak ettiğiniz soruyu seçin, hemen yanıtlayalım. İsterseniz numaranızı bırakın, Selda Hanım sizi arasın.');
      secenekler();
      altCiz();
      function altCiz() {
        var m2 = mesai();
        alt.innerHTML = (m2.acik ? '<a class="ara" href="' + TEL + '">📞 Selda Hanım\'ı Arayın</a>' : '')
          + '<button type="button" class="geri">' + (m2.acik ? 'Numaramı bırakayım, beni arasınlar' : '📞 Sabah 09:00\'da beni arayın') + '</button>'
          + (m2.acik ? '' : '<a class="ara" style="background:none;color:var(--pu-mut)!important;font-weight:600;font-size:13px;text-decoration:underline;padding:0" href="' + TEL + '">Yine de ara · ' + TEL_TXT + '</a>');
        alt.querySelector('.geri').onclick = function () { formCiz(m2); };
      }
      function formCiz(m2) {
        var saat = m2.acik ? null : (m2.pazartesi ? 'Pazartesi 09:00' : (m2.sabahOnce ? 'Bugün 09:00' : 'Yarın 09:00'));
        alt.innerHTML = '<form class="pu-sb-form" novalidate><input type="tel" inputmode="tel" autocomplete="tel" placeholder="05xx xxx xx xx" aria-label="Cep telefonunuz" maxlength="20"><div class="err" aria-live="polite"></div><button type="submit">' + (m2.acik ? '📞 Beni arayın' : '📞 Sabah beni arayın') + '</button><small>Numaranızı yalnızca sizi aramak için kullanırız. <a href="' + AYDINLATMA + '" target="_blank" rel="noopener">Aydınlatma metni</a></small></form>';
        var f = alt.querySelector('form'), inp = f.querySelector('input'), err = f.querySelector('.err'), btn = f.querySelector('button');
        try { inp.focus(); } catch (e) {}
        f.onsubmit = function (e) {
          e.preventDefault();
          var dg = inp.value.replace(/\D/g, '').replace(/^90/, '').replace(/^0/, '');
          if (!/^5\d{9}$/.test(dg)) { err.textContent = 'Lütfen 05 ile başlayan cep numaranızı yazın.'; return; }
          btn.disabled = true; err.textContent = '';
          var a = {}; try { a = JSON.parse(localStorage.getItem('ads_attribution') || '{}') || {}; } catch (x) {}
          var at = { site: SITE, landing: (a.landing_page || location.pathname).slice(0, 120) };
          ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content'].forEach(function (k) { if (a[k]) at[k] = a[k]; });
          var body = { phone: '0' + dg, when: m2.acik ? 'simdi' : 'saat', landing: (location.hostname + location.pathname).slice(0, 120), attribution: at };
          if (saat) body.at = saat;
          fetch(TALEP_API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) })
            .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
            .then(function (x) {
              if (!x.ok || !x.j || !x.j.ok) throw new Error((x.j && x.j.error) || 'hata');
              olay('callback_request', { cta_area: 'soru_kutusu' });
              mesaj(m2.acik ? '✅ Talebiniz alındı. Selda Hanım birkaç dakika içinde sizi arayacak.' : '✅ Talebiniz alındı. Selda Hanım sabah 09:00\'dan itibaren sizi arayacak.');
              alt.innerHTML = m2.acik ? '<a class="ara" href="' + TEL + '">📞 Beklemeden arayın</a>' : '';
            })
            .catch(function (ex) { btn.disabled = false; err.textContent = (ex && ex.message && ex.message !== 'hata' && ex.message.indexOf('etch') < 0 ? ex.message : 'Şu an gönderilemedi, lütfen arayın: ' + TEL_TXT); });
        };
      }
    }
    kutu.querySelector('.pu-sb-btn').onclick = function () { panelAc('balon'); };

    // Ziyaretçi aradı, yazdı ya da Pusula'yı açtıysa davet gösterilmez
    d.addEventListener('click', function (e) { var t = e.target && e.target.closest && e.target.closest('a[href^="tel:"],a[href*="wa.me"],[data-pusula]'); if (t) etkilesti = true; }, true);

    /* Akıllı davet: ilk 12 sn hiçbir şey çıkmaz; sonra önce hangisi olursa:
       sayfanın %40'ını (uzun sayfada ~2,5 ekran boyunu) okumak, 35 sn kalmak (reklamdan gelende 20 sn), masaüstünde sayfadan çıkmaya
       yönelmek ya da telefonda okuduktan sonra hızla yukarı kaydırmak. Ziyaret başına bir kez,
       sayfanın konusuna göre metin; tıklayınca doğrudan Pusula açılır. */
    var gosterildi = false;
    try { gosterildi = sessionStorage.getItem('pu_davet') === '1'; } catch (e) {}
    if (gosterildi) return;
    var hazir = false, okudu = false, enDerin = 0, sonY = scrollY || 0;
    var reklam = reklamdan();
    var yol = location.pathname.toLowerCase();
    var metin = 'Nereden başlayacağınızı 60 saniyede birlikte bulalım mı?';
    for (var k = 0; k < KONU_DAVET.length; k++) if (KONU_DAVET[k][0].test(yol)) { metin = KONU_DAVET[k][1]; break; }
    function dene(neden) {
      if (gosterildi || etkilesti || !hazir || panel || (root && root.parentNode)) return;
      gosterildi = true;
      try { sessionStorage.setItem('pu_davet', '1'); } catch (e) {}
      olay('davet_gosterildi', { neden: neden });
      davet = el('<div class="pu-sb-tz" role="note"><b>' + (mesai().acik ? 'Şu an açığız 👋' : 'Merhaba 👋') + '</b>' + esc(metin) + '<button type="button" aria-label="Kapat">×</button></div>');
      kutu.appendChild(davet); kutu.classList.remove('gizli');
      requestAnimationFrame(function () { requestAnimationFrame(function () { if (davet) davet.classList.add('on'); }); });
      davet.onclick = function (e) { if (e.target.tagName === 'BUTTON') { kapatDavet(); return; } kapatDavet(); ac('davet'); };
      setTimeout(kapatDavet, 18000);
    }
    setTimeout(function () { hazir = true; if (okudu) dene('okuma'); }, 12000);
    setTimeout(function () { dene('sure'); }, reklam ? 20000 : 35000);
    w.addEventListener('scroll', function () {
      var h = d.documentElement.scrollHeight - innerHeight, y = scrollY || pageYOffset || 0;
      if (h > 0) enDerin = Math.max(enDerin, y / h);
      if (enDerin >= 0.4 || y >= innerHeight * 2.5) { okudu = true; dene('okuma'); }
      if (okudu && sonY - y > 600) dene('yukari'); // telefonda okuduktan sonra hızla yukarı: çıkmaya yakın
      sonY = y;
    }, { passive: true });
    d.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY <= 0) dene('cikis'); });
  }

  d.addEventListener('click', function (e) {
    var t = e.target && e.target.closest && e.target.closest('[data-pusula]');
    if (!t) return;
    e.preventDefault();
    ac(t.getAttribute('data-pusula') || 'baglanti');
  });
  // Bağlantıyla doğrudan açılış: sayfa.html#yol-haritasi
  function hashKontrol() { if (location.hash === '#yol-haritasi') ac('baglanti'); }

  /* ---------- Reklamdan gelen ziyaretçi: mesai saatinde tek hedef arama ----------
     Google Ads tıklaması (gclid/gbraid/wbraid; ads-conversion.js 90 gün saklar) + mesai açık:
     sohbet balonu yüklenmez (sayfadaki Jivo yükleyicisi window.__jivoKapali'ya bakar),
     Instagram rozetleri gizlenir. Mesai dışında sohbet açık kalır (talep kaçmasın). */
  function reklamdan() {
    if (/[?&](gclid|gbraid|wbraid)=/.test(location.search)) return true;
    try { var a = JSON.parse(localStorage.getItem('ads_attribution') || 'null'); return !!(a && a.exp > Date.now() && (a.gclid || a.gbraid || a.wbraid)); } catch (e) { return false; }
  }
  if (reklamdan() && mesai().acik) {
    w.__jivoKapali = true;
    d.documentElement.classList.add('rn-reklam');
    var rs = d.createElement('style');
    rs.textContent = 'html.rn-reklam .rn-ig-float,html.rn-reklam .rn-ig,html.rn-reklam .instagram-ribbon,html.rn-reklam .el-ig-float,html.rn-reklam .el-ig,html.rn-reklam jdiv{display:none!important}';
    (d.head || d.documentElement).appendChild(rs);
  }

  w.Pusula = { ac: ac };
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { yerlestir(); hashKontrol(); });
  else { yerlestir(); hashKontrol(); }
})();
