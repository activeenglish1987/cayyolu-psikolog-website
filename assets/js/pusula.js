/* ============================================================
   Randevu Pusulası — "60 saniyede size özel yol haritası"
   ------------------------------------------------------------
   Ziyaretçi 3–4 dokunuşla kim için / hangi konuda / nerede sorularını
   seçer; Psikolog Rojin Nazik'in kartı, o konudaki gerçek notu ve
   Claude'un yazdığı kişiye özel "ilk görüşme yol haritası" açılır.
   Tek hedef: telefonla aramak.

   - İsim, telefon, serbest metin ALINMAZ; hiçbir şey kaydedilmez.
   - Yapay zekâ yanıt vermezse hazır metinle aynen çalışır.
   - Güvende hissetmiyorum seçeneği yapay zekâya gitmez: 112 ekranı.
   - Aramalar ads-conversion.js tarafından data-cta-area="pusula"
     olarak sayılır (Google Ads "Tıkla ve ara" dönüşümü).

   Ayar (isteğe bağlı, bu dosyadan ÖNCE):
     window.PUSULA_CFG = { site: 'rojin' | 'cayyolu', api: '...', foto: '...' }
   Sayfada herhangi bir öğeye data-pusula eklemek onu açar.
   Rojin ve Çayyolu sitelerinde aynı dosya kullanılır.
   ============================================================ */
(function () {
  'use strict';
  var w = window, d = document;
  if (w.__pusula) return;
  w.__pusula = true;

  var CFG = w.PUSULA_CFG || {};
  var SITE = CFG.site === 'cayyolu' ? 'cayyolu' : 'rojin';
  var API = CFG.api || 'https://www.psikologunubul.com.tr/api/pusula';
  var RN = SITE === 'rojin' ? '' : 'https://psikologrojinnazik.com';
  var FOTO = CFG.foto || (RN || '') + '/images/brand/rojin-nazik-portrait-800.webp';
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
    kendim: [['kaygi', 'Kaygı ve stres'], ['panik', 'Panik atak'], ['mutsuzluk', 'Mutsuzluk, isteksizlik'], ['iliski', 'İlişki sorunları'], ['ayrilik', 'Boşanma / ayrılık'], ['yas', 'Yas ve kayıp'], ['ofke', 'Öfke'], ['ozguven', 'Özgüven'], ['dusunce', 'Aşırı düşünme'], ['diger', 'Adını tam koyamıyorum']],
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
    kendim: { kaygi: 'kaygi1', panik: 'panik', mutsuzluk: 'degisim', iliski: 'cift3', ayrilik: 'bosanma1', yas: 'gitmeli', ofke: 'degisim', ozguven: 'terapi', dusunce: 'kaygi2', diger: 'ilk' },
    cocugum: { davranis: 'cocuk1', okul: 'cocuk2', korku: 'cocuk3', uyku: 'cocuk2', bosanma: 'bosanma2', ayrilma: 'cocuk3', diger: 'cocuk1' },
    ergen: { iletisim: 'ergen1', sinav: 'ergen2', icekapanma: 'ergen2', ofke: 'ergen1', ekran: 'ergen1', ozguven: 'ergen2', diger: 'ergen1' },
    cift: { iletisim: 'cift1', tartisma: 'cift3', guven: 'cift2', uzaklasma: 'uzak', evlilikoncesi: 'cift2', bosanma: 'bosanma1', diger: 'cift1' }
  };
  var NEDEN = {
    kendim: 'Yetişkinlerle bireysel görüşmelerde bilişsel davranışçı yaklaşım ve şema terapi eğitimiyle çalışır.',
    cocugum: 'Çocuk danışmanlığında ebeveynle birlikte çalışır; ilk görüşme genellikle sizinle yapılır.',
    ergen: 'Ergenlerle önce güvenli, yargılanmadan konuşulabilen bir ilişki kurmayı önemser; aileyi de sürece katar.',
    cift: 'Psikolog ve aile danışmanı olarak çift ve evlilik görüşmeleri yapar.'
  };

  /* ---------- Yapay zekâ yanıt vermezse: hazır yol haritaları ---------- */
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
      return { acik: day >= 1 && day <= 6 && m >= 540 && m < 1200, pazartesi: (day === 6 && m >= 1200) || day === 0 };
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
    + '.pu-toast{' + TEMA + 'position:fixed;left:12px;right:12px;bottom:calc(150px + env(safe-area-inset-bottom));z-index:9997;display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:18px;background:#fff;box-shadow:0 18px 44px -14px rgba(0,0,0,.35);border:1px solid var(--pu-line);transform:translateY(30px);opacity:0;transition:all .45s cubic-bezier(.2,.9,.25,1);font-family:inherit;color:var(--pu-ink)}'
    + '.pu-toast.on{transform:none;opacity:1}'
    + '@media(min-width:861px){.pu-toast{left:auto;right:24px;bottom:110px;max-width:380px}}'
    + '.pu-toast img{width:46px;height:46px;border-radius:50%;object-fit:cover;flex:none}'
    + '.pu-toast button.go{flex:1;text-align:left;border:0;background:none;font:inherit;cursor:pointer;color:inherit;padding:0}'
    + '.pu-toast b{display:block;font-size:14.5px;color:var(--pu-a2)}.pu-toast span{display:block;font-size:12.5px;color:var(--pu-mut)}'
    + '.pu-toast button.x{border:0;background:none;font-size:20px;color:var(--pu-mut);cursor:pointer;padding:4px 6px}'
    + 'html.pu-lock,html.pu-lock body{overflow:hidden!important}'
    + '@media(prefers-reduced-motion:reduce){.pu-root *,.pu-launch,.pu-toast{animation:none!important;transition:none!important}}';

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
    olay('pusula_analiz');

    // 1) Analiz ekranı
    goster('<div class="pu-orbw"><div class="pu-orb"><img src="' + esc(FOTO) + '" alt=""></div></div>'
      + '<h2 class="pu-h" style="text-align:center">Yol haritanız hazırlanıyor</h2>'
      + '<ul class="pu-lines"><li><i>✓</i>Seçimleriniz eşleştiriliyor</li><li><i>✓</i>Rojin Nazik\'in notları taranıyor</li><li><i>✓</i>İlk görüşme planınız yazılıyor</li></ul>', 92, false);
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
      fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ kim: s.kim, konu: s.konu, yas: s.yas, yer: s.yer }), signal: ctrl && ctrl.signal })
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
      var not = NOT[(s.yer === 'online' && s.konu === 'diger') ? 'online' : NOT_ESLE[s.kim][s.konu]] || NOT.ilk;
      var ozet = [kimEtiket, yasEtiket, konuEtiket, yerEtiket].filter(Boolean).join(' · ');
      // goster() açık isteği iptal eder; akış sürerken sonuç kartına geçiyoruz, istek yaşamalı
      var tut = istek; istek = null;
      goster('<div class="pu-ey">Yol haritanız hazır</div>'
        + '<p class="pu-p" style="margin:6px 0 14px">' + esc(ozet) + '</p>'
        + '<div class="pu-exp"><div class="pu-ph"><img src="' + esc(FOTO) + '" alt="Psikolog Rojin Nazik"></div><div><small>Sizin için önerilen uzman</small><b>Psikolog Rojin Nazik</b><span>Psikolog ve Aile Danışmanı · RN Psikoloji kurucusu</span></div></div>'
        + '<div class="pu-tags"><em>15+ yıllık mesleki deneyim</em><em>Şema terapi eğitimi</em><em>3 kitap yazarı</em><em>AB Psikologlar Derneği Genel Başkanı</em></div>'
        + '<p class="pu-why">' + esc(NEDEN[s.kim]) + '</p>'
        + '<figure class="pu-q"><p>' + esc(not[2]) + '</p><small><span>Psikolog Rojin Nazik · ' + esc(not[1]) + '</span><a href="' + RN + not[0] + '" target="_blank" rel="noopener">Notun tamamı →</a></small></figure>'
        + '<section class="pu-ai" aria-live="polite"><div class="pu-ai-h"><i></i><span>Size özel ilk görüşme yol haritası</span></div><div class="pu-ai-b"></div></section>'
        + '<div class="pu-facts">'
        + '<div class="pu-fact"><span>📍</span><span>' + esc(SUBE[s.yer]) + '</span></div>'
        + '<div class="pu-fact pu-selda">' + seldaAvatar() + '<span><b>Telefonu ' + SELDA + ' açar.</b> Size en yakın uygun saati ve ücret bilgisini hemen söyler. Ne anlatacağınızı düşünmenize gerek yok; bu yol haritasını okumanız yeterli.</span></div>'
        + '</div>'
        + '<p class="pu-note">Bu yol haritası genel bilgilendirmedir; tanı ya da tedavi önerisi değildir. Acil bir durumda 112\'yi arayın.</p>', 100, true);
      istek = tut;
      cta();
      olay('pusula_sonuc', { pusula_kaynak_metin: yedek ? 'hazir' : 'yapay_zeka' });
      yaz();
    }

    // Akan metni harf harf yaz (yapay zekâ akarken de, önbellekten gelince de aynı his)
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
    // 1) Giriş bölümündeki arama düğmelerinin altına
    var hero = d.querySelector(CFG.heroSecici || '.hero-actions, .hero .cta-row, .hero-ctas');
    if (hero && !d.querySelector('.pu-launch')) {
      var k = el('<div class="pu-launch-w" style="' + TEMA + '">' + launcherHtml() + '</div>');
      hero.parentNode.insertBefore(k, hero.nextSibling);
    }
    // 2) Sayfa sonunda, alt bilgiden önce bant
    var ft = d.querySelector('footer, .site-footer');
    if (ft && !d.querySelector('.pu-band')) {
      var bant = el('<section class="pu-band" aria-label="Size özel yol haritası"><div class="pu-band-in"><img src="' + esc(FOTO) + '" alt="" loading="lazy"><div class="pu-band-t"><b>Nereden başlayacağınızı bilmiyor musunuz?</b><span>3 dokunuşta size özel ilk görüşme yol haritanızı görün. İsim ya da telefon istemiyoruz.</span></div><button type="button" data-pusula="bant">Yol haritamı göster →</button></div></section>');
      ft.parentNode.insertBefore(bant, ft);
    }
    // 3) Sayfanın ortasına gelince bir kez, nazik bir hatırlatma
    var gosterildi = false;
    try { gosterildi = sessionStorage.getItem('pu_toast') === '1'; } catch (e) {}
    if (!gosterildi) {
      var izle = function () {
        var h = d.documentElement.scrollHeight - innerHeight;
        if (h > 600 && (scrollY || pageYOffset) / h > 0.45) { w.removeEventListener('scroll', izle); tost(); }
      };
      w.addEventListener('scroll', izle, { passive: true });
    }
  }

  function tost() {
    try { sessionStorage.setItem('pu_toast', '1'); } catch (e) {}
    if (root && root.parentNode) return;
    var t = el('<div class="pu-toast" role="note"><img src="' + esc(FOTO) + '" alt=""><button type="button" class="go" data-pusula="toast"><b>Size özel yol haritanız 60 saniyede</b><span>Uzmanınızı ve ilk görüşmenizi görün →</span></button><button type="button" class="x" aria-label="Kapat">×</button></div>');
    d.body.appendChild(t);
    requestAnimationFrame(function () { requestAnimationFrame(function () { t.classList.add('on'); }); });
    var kaldir = function () { t.classList.remove('on'); setTimeout(function () { if (t.parentNode) t.parentNode.removeChild(t); }, 400); };
    t.querySelector('.x').onclick = kaldir;
    t.querySelector('.go').addEventListener('click', kaldir);
    setTimeout(kaldir, 14000);
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
    rs.textContent = 'html.rn-reklam .rn-ig-float,html.rn-reklam .rn-ig,html.rn-reklam .instagram-ribbon,html.rn-reklam jdiv{display:none!important}';
    (d.head || d.documentElement).appendChild(rs);
  }

  w.Pusula = { ac: ac };
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { yerlestir(); hashKontrol(); });
  else { yerlestir(); hashKontrol(); }
})();
