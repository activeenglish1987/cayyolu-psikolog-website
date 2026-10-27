"""Sayfa güçlendirme: uzman onaylı ek bölümler mevcut sayfanın metninin sonuna eklenir (yeni adres açılmaz).
Biçim: EKLER = {'/adres/': {'tarih': 'YYYY-AA-GG', 'html': '<h2>…</h2><p>…</p>', 'sss': [('soru', 'cevap'), …]}}
'sss' isteğe bağlıdır; sorular sayfanın SSS listesine ve FAQPage verisine eklenir.
Hem semt/hizmet (landing.py) hem içerik (icerik.json, makaleler.py) sayfalarında çalışır; sayfanın
güncelleme tarihi 'tarih' olur."""
EKLER = {'/alacaatli-psikolog/': {'html': "<h2>Alacaatlı'da çocukların okul ve arkadaşlık uyumu</h2>\n"
                                  '<p>Okul çağındaki çocuklar için yeni bir okul, sınıf değişikliği ya da arkadaş grubundaki değişimler zorlayıcı olabilir. Okula gitmek istememe, sabahları karın '
                                  'ağrısı gibi bedensel yakınmalar, arkadaş edinmekte zorlanma ya da evde öfke patlamaları bu zorlanmanın işaretleri olabilir. Çocukla ilgili görüşmelerde önce '
                                  'ebeveynlerle bir ön görüşme yapılır, gerekirse okulla iş birliği de planlanır. Çocuğun duygularını anlamak, davranışı değiştirmeye çalışmaktan önce gelir.</p>\n'
                                  "<h2>Alacaatlı'da yaşayan aileler için</h2>\n"
                                  "<p>Alacaatlı'da yaşayan danışanlarımızın önemli bir kısmı aile yaşamıyla ilgili konularla başvuruyor. Evin düzenini sürdürmeye çalışan bir ebeveynin kendi "
                                  'ihtiyaçlarını uzun süre ertelemesi, eşlerin çocuk yetiştirme konusunda farklı düşünmesi, yeni bir eve ve çevreye uyum sağlamak bu konuların başında geliyor. Bu '
                                  'zorluklar konuşulmadığında zamanla yorgunluğa, kırgınlığa ve yalnızlık duygusuna dönüşebiliyor.</p>\n'
                                  '<h2>Ebeveynler aynı dili konuşamadığında</h2>\n'
                                  '<p>Anne ve babanın her konuda aynı düşünmemesi çok doğaldır. Sorun, farklılıkların konuşulamaması ve çocuğun bu iki farklı yaklaşım arasında kalmasıyla başlar. '
                                  'Ebeveyn görüşmelerinde amaç kimin haklı olduğunu bulmak değil, iki ebeveynin de kabul edebileceği ortak bir zemin oluşturmaktır. Bu çalışma, çocuğun evde daha '
                                  'tutarlı bir ortamda büyümesine katkı sağlar.</p>\n'
                                  '<ul>\n'
                                  '<li>Ev kuralları ve sınırlar konusunda ortak bir dil geliştirmek</li>\n'
                                  '<li>Çocuğun önünde tartışmamak ve anlaşmazlıkları baş başa konuşmak</li>\n'
                                  '<li>Her ebeveynin güçlü yanlarını fark etmek ve paylaşmak</li>\n'
                                  '</ul>\n'
                                  '<h2>Kendinize ayıracak zamanı planlamak</h2>\n'
                                  '<p>Aile sorumlulukları yoğunken kendinize bir saat ayırmak bile zor görünebilir. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında yapılır; çocukların okulda '
                                  'olduğu saatler ya da cumartesi randevuları sık tercih ediliyor. Ofisimizde ücretsiz otopark bulunur. Gelmenin zor olduğu haftalarda görüşmeyi online '
                                  'yapabilirsiniz.</p>\n'
                                  '<h2>Aile görüşmesi mi, bireysel görüşme mi?</h2>\n'
                                  '<p>Hangi görüşme biçiminin size uygun olduğuna ilk görüşmede birlikte karar verilir. Bazen bir ebeveynin kendi duygularını konuşabileceği bireysel görüşmeler, '
                                  'bazen eşlerin birlikte katıldığı görüşmeler, bazen de çocuğun da dahil olduğu aile görüşmeleri daha uygundur. Süreç ihtiyaçlarınıza göre zaman içinde '
                                  'değişebilir.</p>',
                          'sss': [('Eşimle çocuk yetiştirme konusunda anlaşamıyoruz, birlikte gelebilir miyiz?',
                                   'Evet. Ebeveyn olarak birlikte yapılan görüşmelerde ortak bir yaklaşım geliştirmek üzerine çalışılır.'),
                                  ('Çocuklar okuldayken gündüz randevu alabilir miyim?', 'Evet. Görüşmeler hafta içi gündüz saatlerinde de planlanabilir.'),
                                  ('Önce bireysel mi, aile görüşmesi mi başlamalıyım?', 'Bunu ilk görüşmede birlikte değerlendiririz; başvuru nedeninize göre size uygun görüşme biçimi önerilir.')],
                          'tarih': '2026-10-27'},
 '/beysukent-psikolog/': {'html': "<h2>Beysukent'te yalnızlık ve sosyal çevre</h2>\n"
                                  '<p>Yeni bir şehirde ya da yeni bir ortamda kendine ait bir çevre kurmak zaman alır. Bazı gençler kalabalık bir kampüste bile yalnız hissettiklerini, arkadaşlık '
                                  'ilişkilerinde kabul görmekte zorlandıklarını söylüyor. Bu duygu çoğu zaman utançla birlikte yaşandığı için kimseye anlatılmıyor. Görüşmelerde sosyal ilişkilerde '
                                  'sizi neyin zorladığını, kendinizi nasıl ifade ettiğinizi ve küçük adımlarla nasıl bağ kurabileceğinizi birlikte konuşuruz. Yalnızlık hissi bir eksiklik değil, '
                                  'bağlantı ihtiyacının işaretidir.</p>\n'
                                  "<h2>Beysukent'te yaşayan gençler ve aileleri</h2>\n"
                                  "<p>Beysukent'te üniversite öğrencileri, genç yetişkinler ve aileler bir arada yaşıyor. Genç danışanlarımız çoğu zaman akademik baskı, gelecek belirsizliği, "
                                  'yalnızlık ve ilişkilerde zorlanma gibi konularla başvuruyor. Aileler ise çocuklarının ergenlik dönemi, okul başarısı ve ev içindeki iletişim konusunda destek '
                                  'arıyor.</p>\n'
                                  '<h2>Ders programı ile görüşmeleri dengelemek</h2>\n'
                                  '<p>Öğrenciler için en büyük zorluklardan biri, değişken ders ve sınav programı içinde görüşmeleri düzenli sürdürmek. Bu yüzden görüşme saatini dönem başında '
                                  'birlikte planlamak, sınav haftalarında ise esnek davranmak işe yarar. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında yapılır; cumartesi saatleri '
                                  'öğrenciler için çoğu zaman uygun bir seçenektir.</p>\n'
                                  '<ul>\n'
                                  '<li><b>Dönem başında planlayın:</b> Ders programınızı bildiğinizde sabit bir görüşme saati seçmek kolaylaşır.</li>\n'
                                  '<li><b>Sınav dönemlerini önceden konuşun:</b> Yoğun haftalarda randevuyu birlikte yeniden düzenleyebiliriz.</li>\n'
                                  '<li><b>Tatillerde online devam edin:</b> Şehir dışında olduğunuz dönemlerde görüşmeler online sürebilir.</li>\n'
                                  '</ul>\n'
                                  '<h2>İlk kez kendi başına başvuran genç yetişkinler</h2>\n'
                                  '<p>Pek çok genç yetişkin, psikolojik destek almaya ilk kez kendi kararıyla başvuruyor. Bu adım bazen ailenin bilgisi olmadan atılıyor ve "Ailem öğrenir mi?" sorusu '
                                  'akla geliyor. Reşit danışanlarla yapılan görüşmeler gizlidir; ne paylaşacağınıza siz karar verirsiniz. Ailenizle ilgili konuları konuşmak, onların görüşmelere '
                                  'katılacağı anlamına gelmez.</p>\n'
                                  '<h2>Ergen çocuğu olan aileler için</h2>\n'
                                  '<p>Ergenlik, çocuğun kendine ait bir alan istediği ve aileden uzaklaşıyormuş gibi göründüğü bir dönemdir. Ebeveynler bu dönemde çoğu zaman nasıl yaklaşacaklarını '
                                  'bilemediklerini söylüyor. Ergen görüşmelerinde önce ebeveynle bir ön görüşme yapılır; ardından gençle görüşmeler planlanır ve gencin mahremiyeti ile ailenin '
                                  'bilgilendirilmesi arasındaki denge en baştan konuşulur.</p>',
                          'sss': [('Öğrenciyim, sınav haftalarında görüşmelere ara verebilir miyim?',
                                   'Evet. Yoğun dönemlerde randevuları birlikte yeniden planlayabilir ya da görüşmeyi online yapabilirsiniz.'),
                                  ('Ailemin bilgisi olmadan görüşmeye başlayabilir miyim?', 'Reşitseniz evet. Görüşmeleriniz gizlidir ve ailenizle neyi paylaşacağınıza siz karar verirsiniz.'),
                                  ('Ergen çocuğumla ilgili görüşmelerde neler bana aktarılır?',
                                   'Gencin mahremiyetine saygı gösterilir; ailenin bilmesi gereken genel bilgiler ve güvenlikle ilgili durumlar en baştan konuşulan çerçevede paylaşılır.')],
                          'tarih': '2026-10-27'},
 '/bilkent-psikolog/': {'html': "<h2>Bilkent'te mezuniyet ve gelecek kararları</h2>\n"
                                '<p>Son sınıfa yaklaşırken kariyer seçimi, yüksek lisans, yurt dışı ya da iş başvuruları gibi kararlar ağırlaşabilir. Herkesin bir planı varmış gibi görünürken kendi '
                                'yolunuzu belirleyememek kaygıyı artırabilir. Ailenin beklentileri ile kendi istekleriniz arasında kalmak da bu dönemin sık konuşulan konularındandır. Görüşmelerde '
                                'seçeneklerinizi, değerlerinizi ve karar vermenizi zorlaştıran duyguları birlikte ele alırız; doğru kararı sizin yerinize vermek değil, kendi kararınızı daha net '
                                'görebilmenize yardım etmek amaçlanır.</p>\n'
                                "<h2>Bilkent'te okuyan öğrenciler için destek</h2>\n"
                                "<p>Bilkent'te okuyan öğrenciler, yoğun bir akademik ortamda hem derslerle hem de sosyal hayatla aynı anda başa çıkmaya çalışıyor. Başka bir şehirden gelen öğrenciler "
                                'için aileden uzak olmak, yeni bir çevreye uyum sağlamak ve yalnızlık da bu yüke ekleniyor. Danışanlarımızla en sık konuştuğumuz konular arasında sınav kaygısı, '
                                'mükemmeliyetçilik, motivasyon kaybı, ilişkiler ve gelecek belirsizliği var.</p>\n'
                                '<h2>Kampüs desteği ve dışarıdan bir psikolog</h2>\n'
                                '<p>Üniversitelerin öğrencilere sunduğu psikolojik danışmanlık hizmetleri değerli bir kaynaktır ve kullanmanızı öneririz. Bazı öğrenciler ise kampüs dışında, daha '
                                'uzun soluklu ya da daha esnek saatlerde bir destek arıyor. Aynı konu için iki ayrı destek sürecini aynı anda yürütmek çoğu zaman karışıklık yaratır; bu yüzden '
                                'kampüste bir süreciniz varsa bunu ilk görüşmede paylaşmanız iyi olur.</p>\n'
                                '<h2>Yüksek beklentiler ve kendinize yüklediğiniz baskı</h2>\n'
                                '<p>Başarılı öğrenciler arasında "yeterince iyi olamama" duygusu sanıldığından yaygındır. Not ortalaması, burslar, staj ve iş başvuruları sürekli bir karşılaştırma '
                                'ortamı yaratabilir. Bu baskı bazen ertelemeye, uykusuzluğa ya da hiçbir şeyden keyif alamamaya dönüşebilir. Görüşmelerde bu beklentilerin nereden geldiğini anlamak '
                                've kendinize daha gerçekçi hedefler koymak üzerine çalışılır.</p>\n'
                                '<h2>Görüşmeleri akademik takvime göre planlamak</h2>\n'
                                '<p>Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında yapılabilir; ders programınıza göre sabit bir saat seçmek süreci kolaylaştırır. Sınav dönemlerinde ve '
                                'tatillerde görüşmeler online sürdürülebilir. İlk görüşmede derslerinizi, sınav takviminizi ve sizi en çok zorlayan durumları paylaşmanız planlamayı '
                                'kolaylaştırır.</p>',
                        'sss': [('Kampüsteki psikolojik danışmanlık hizmetine gidiyorum, sizinle de görüşebilir miyim?',
                                 'Aynı konu için iki ayrı süreci aynı anda yürütmek çoğu zaman önerilmez. Kampüsteki süreciniz bittiyse ya da farklı bir ihtiyaç varsa durumunuzu ilk görüşmede '
                                 'birlikte değerlendiririz.'),
                                ('Sınav döneminde kaygım çok artıyor, ne zaman başvurmalıyım?',
                                 'Sınav dönemi gelmeden başlamak daha rahat çalışma imkânı verir; ancak kaygı yoğunlaştığında da başvurabilirsiniz.'),
                                ('Akşam saatlerinde görüşme yapılabiliyor mu?', "Evet. Görüşmeler 20:00'ye kadar planlanabilir; ders programınıza uygun saati birlikte seçeriz.")],
                        'tarih': '2026-10-27'},
 '/bireysel-danismanlik/': {'html': '<h2>İlk randevudan önce bilmeniz gerekenler</h2>\n'
                                    '<p>Bireysel görüşmeye başlamak için hazır bir sorun tanımı getirmeniz gerekmez. Randevu alırken yalnızca kısaca neden destek almak istediğinizi paylaşmanız '
                                    "yeterlidir; bu bilgi, başvuru konunuza uygun uzmanla eşleşmenizi kolaylaştırır. Görüşmeler Konutkent'teki ofisimizde, Dumlupınar Bulvarı No:399 adresinde yüz "
                                    'yüze ya da online olarak yapılabilir. Binada ücretsiz otopark bulunduğu için iş çıkışı arabayla gelenler park yeri aramak zorunda kalmaz.</p>\n'
                                    '<ul>\n'
                                    '<li><b>Yanınızda getirebilecekleriniz:</b> Daha önce aldığınız psikolojik ya da psikiyatrik destek varsa bunun kısa bir özeti, kullandığınız ilaçların adları '
                                    '(yalnızca bilgi amaçlı) ve aklınızdaki sorular.</li>\n'
                                    '<li><b>Not almak isteyenler için:</b> Son haftalarda sizi en çok zorlayan üç durumu kısaca yazmak, ilk görüşmede neyi anlatacağınızı düşünme yükünü '
                                    'hafifletir.</li>\n'
                                    '<li><b>Zamanlama:</b> Görüşmeye birkaç dakika erken gelmek, nefeslenip hazır hissederek başlamanıza yardım eder.</li>\n'
                                    '</ul>\n'
                                    '<h2>Görüşme sıklığı ve düzen</h2>\n'
                                    '<p>Bireysel görüşmeler çoğunlukla haftada bir yapılır; süreç ilerledikçe aralık iki haftaya açılabilir. Burada önemli olan, görüşmelerin düzenli olmasıdır. Aynı '
                                    'gün ve saatte devam eden görüşmeler, hem sizin için bir rutin oluşturur hem de bir görüşmede konuşulanın bir sonrakine taşınmasını kolaylaştırır. Görüşmeler '
                                    'pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabildiği için çalışan danışanlarımız çoğu zaman akşam ya da cumartesi saatlerini tercih ediyor.</p>\n'
                                    '<p>Bir dönem şehir dışında olacaksanız ya da gelmeniz zorlaşırsa, aynı uzmanla online görüşmeye geçebilirsiniz. Yüz yüze ve online görüşmeler arasında geçiş '
                                    'yapmak süreci bozmaz; önemli olan sürekliliğin korunmasıdır.</p>\n'
                                    '<h2>Süreç boyunca birlikte değerlendirme</h2>\n'
                                    '<p>Belirli aralıklarla, görüşmelerin size nasıl geldiğini birlikte konuşuruz: Başlangıçta belirlediğiniz hedeflere ne kadar yaklaştınız, hangi konular öne çıktı, '
                                    'neyin değişmesini istiyorsunuz? Bu değerlendirmeler, sürecin sizin ihtiyacınıza göre yeniden şekillenmesini sağlar. Bir görüşmede rahatsız olduğunuz ya da '
                                    'anlaşılmadığınızı hissettiğiniz bir an olursa bunu söylemeniz de sürecin bir parçasıdır; bu tür geri bildirimler çalışmayı derinleştirir.</p>\n'
                                    '<p>Görüşmeleri sonlandırma kararı da birlikte verilir. Genellikle bir anda bitirmek yerine aralıklar seyreltilerek kapanış yapılır; böylece öğrendiklerinizi '
                                    'günlük hayatta denemek için zaman kalır.</p>\n'
                                    '<h2>Size uygun uzmanla eşleşme</h2>\n'
                                    '<p>Ofisimizde farklı yaş grupları ve konularda deneyimli psikologlar görüşme yürütür. Randevu sırasında paylaştığınız kısa bilgi, başvuru konunuza ve tercihinize '
                                    'göre sizi uygun uzmanla eşleştirmemize yardım eder. Örneğin yetişkin bireysel görüşmeler ve ilişki konuları ile gençlik dönemine özgü konular farklı uzmanlarla '
                                    'planlanabilir. İlk görüşmelerden sonra uzmanla çalışmanın size iyi gelmediğini düşünürseniz bunu açıkça söyleyebilirsiniz; başka bir uzmanla devam etmek de bir '
                                    'seçenektir. Terapötik ilişkide kendinizi rahat hissetmeniz, sürecin verimli ilerlemesi için önemlidir.</p>\n'
                                    '<p>Bireysel danışmanlığın kapsamı, hangi konularda çalışıldığı ve terapist seçerken dikkat edilecekler için ayrıntılı bir rehber: <a '
                                    'href="https://www.psikologrojinnazik.com/bireysel-danismanlik/">Bireysel danışmanlık nedir, süreç nasıl ilerler?</a></p>',
                            'sss': [('İlk görüşmeden sonra devam etmek zorunda mıyım?',
                                     'Hayır. İlk görüşme bir tanışma ve değerlendirme görüşmesidir; sonrasında devam edip etmeme kararını siz verirsiniz.'),
                                    ('Görüşmelerde konuştuklarım kimseyle paylaşılır mı?',
                                     'Görüşmelerde konuşulanlar meslek etiği gereği gizli tutulur. Gizliliğin sınırları, örneğin can güvenliği riski gibi durumlar, ilk görüşmede açıkça konuşulur.'),
                                    ('Yüz yüze başlayıp online devam edebilir miyim?',
                                     'Evet. Aynı uzmanla yüz yüze ve online görüşmeler arasında geçiş yapabilirsiniz; sürecin düzenli devam etmesi daha önemlidir.')],
                            'tarih': '2026-10-27'},
 '/bosanma-sonrasi-danismanlik/': {'html': '<h2>Boşanma sürecinin hangi aşamasında başvurulabilir?</h2>\n'
                                           '<p>Boşanma sonrası danışmanlık için boşanmanın resmen tamamlanmasını beklemeniz gerekmez. Başvuranların bir kısmı karar aşamasında, bir kısmı dava '
                                           'sürerken, bir kısmı ise boşanmadan aylar ya da yıllar sonra gelir. Her aşamanın kendine özgü zorlukları vardır: Karar aşamasında belirsizlik ve suçluluk, '
                                           'süreç sırasında yorgunluk ve öfke, sonrasında ise yalnızlık ve yeni bir düzen kurmanın ağırlığı öne çıkabilir.</p>\n'
                                           "<p>Görüşmeler Konutkent'teki ofisimizde yüz yüze ya da online yapılabilir. Çocukların bakımı nedeniyle programı yoğun olan ebeveynler için akşam ve "
                                           'cumartesi saatleri ya da online görüşme süreci sürdürmeyi kolaylaştırır.</p>\n'
                                           '<h2>Psikolojik destek ve hukuki süreç</h2>\n'
                                           '<p>Boşanma sürecinde psikolojik destek ile hukuki süreç birbirinden ayrıdır. Görüşmelerde velayet, mal paylaşımı gibi hukuki konularda yönlendirme '
                                           'yapılmaz; bu konular için avukatınızla çalışmanız gerekir. Görüşmelerin odağı, bu sürecin sizde yarattığı duygular, kararlarınızı daha sakin bir zihinle '
                                           'verebilmeniz ve çocuklarınız varsa onlarla iletişiminizdir.</p>\n'
                                           '<p>Görüşmelerde konuşulanlar meslek etiği gereği gizlidir. Danışmanlık sürecinin bir dava sürecinde nasıl ele alınabileceğine ilişkin sorularınızı ilk '
                                           'görüşmede açıkça sorabilirsiniz.</p>\n'
                                           '<h2>Çocuklar için ayrı destek</h2>\n'
                                           '<p>Boşanma, çocuklar için de büyük bir değişimdir. Ebeveynlerin kendi süreçleri için destek alması, çocuklarına daha sakin bir ortam sunmalarına yardım '
                                           'eder. Bunun yanında, çocukta uzun süren uyku sorunları, okulda belirgin düşüş, içe kapanma ya da öfke patlamaları gibi değişiklikler görülürse, çocuğun '
                                           'ayrıca bir çocuk ve ergen görüşmesine başlaması değerlendirilebilir. Bu görüşmeler farklı bir uzmanla yürütülür; böylece ebeveynin ve çocuğun süreçleri '
                                           'birbirine karışmaz.</p>\n'
                                           '<h2>Boşanma sonrası sık yaşanan duygular</h2>\n'
                                           '<p>Boşanmayı kendisi isteyen kişi de, istemeden boşanan kişi de bu süreçte birbirine karışan duygular yaşayabilir. Rahatlama ile hüzün, öfke ile özlem, '
                                           'özgürlük hissi ile yalnızlık aynı gün içinde birbirini izleyebilir. Ortak arkadaş çevresinin değişmesi, bayram ve özel günlerin yeni bir düzende '
                                           'geçirilmesi, çocuklarla geçirilen zamanın paylaşılması gibi pratik değişiklikler de duygusal yükü artırabilir. Bu duyguların olağan olduğunu bilmek ve '
                                           'onları yargılamadan konuşabileceğiniz bir alan bulmak, yeni düzene uyumu kolaylaştırır.</p>\n'
                                           '<p>Ebeveynlerin çocuğa nasıl anlatacağına dair sorular sık gelir; bu konuda ilk adımlar için <a '
                                           'href="https://www.psikologrojinnazik.com/bosanmayi-cocuga-anlatmak/">boşanmayı çocuğa anlatmak</a> rehberine göz atabilirsiniz.</p>\n'
                                           '<p>Boşanma sonrası danışmanlıkta ele alınan konular için ayrıntılı rehber: <a '
                                           'href="https://www.psikologrojinnazik.com/bosanma-sonrasi-danismanlik/">Boşanma sonrası danışmanlık ve süreç</a></p>',
                                   'sss': [('Boşanma davası sürerken görüşmelere başlayabilir miyim?',
                                            'Evet. Görüşmeler sürecin her aşamasında başlayabilir; hukuki konularda ise avukatınızla çalışmanız gerekir.'),
                                           ('Eski eşimle birlikte görüşmeye gelebilir miyiz?',
                                            'Çocuklarla ilgili ortak kararlar için ebeveynlerin birlikte katıldığı görüşmeler planlanabilir; bu, ilk görüşmede durumunuza göre değerlendirilir.'),
                                           ('Çocuğum için de destek alabilir miyim?', 'Evet. Çocuğunuz için ayrı bir uzmanla çocuk ve ergen görüşmeleri planlanabilir.')],
                                   'tarih': '2026-10-27'},
 '/cayyolu-aile-terapisi/': {'html': '<h2>Aile görüşmesinde bir oturum nasıl geçer?</h2>\n'
                                     '<p>Aile görüşmelerinde amaç, bir kişiyi "sorunlu" ilan etmek değil, aile içindeki ilişkileri ve iletişim biçimlerini birlikte anlamaktır. Görüşmede her aile '
                                     'üyesinin söz almasına özen gösterilir; özellikle çocukların ve gençlerin kendilerini ifade edebilmesi için kurallar baştan konuşulur: Kimse sözü kesilmeden '
                                     'dinlenir, kimse alay edilmez, herkes kendi deneyimini anlatır.</p>\n'
                                     '<p>Oturumlarda aile içinde tekrar eden durumlar somut örnekler üzerinden ele alınır: Akşam yemeğinde başlayan tartışmalar, ödev saatleri, ekran kuralları ya da '
                                     'kardeşler arası çatışmalar gibi. Bu örnekler üzerinden ailenin kendine özgü döngüleri görünür hâle gelir ve değişim için küçük adımlar belirlenir.</p>\n'
                                     '<h2>Hangi durumlarda aile görüşmesi düşünülebilir?</h2>\n'
                                     '<ul>\n'
                                     '<li><b>Sürekli gerginlik:</b> Evde sık sık tartışma çıkıyor ve kimse kendini anlaşılmış hissetmiyorsa.</li>\n'
                                     '<li><b>Yaşam değişiklikleri:</b> Taşınma, yeni bir kardeşin doğumu, boşanma ya da yeniden evlilik gibi dönemlerde.</li>\n'
                                     '<li><b>Kayıp ve yas:</b> Aile bir yakınını kaybettiğinde ve herkes yasını farklı yaşadığında.</li>\n'
                                     '<li><b>Ergenlik dönemi:</b> Genç ile ebeveynler arasında iletişim kopma noktasına geldiğinde.</li>\n'
                                     '<li><b>Ebeveynler arasında farklı tutumlar:</b> Anne ile babanın çocuk yetiştirme konusunda anlaşamadığı durumlarda.</li>\n'
                                     '</ul>\n'
                                     '<h2>Aile görüşmesine nasıl hazırlanabilirsiniz?</h2>\n'
                                     '<p>Görüşmeden önce aile olarak neden destek almak istediğinizi kısaca konuşmanız faydalı olur. Çocuklara ve gençlere, görüşmenin kimseyi suçlamak için değil, '
                                     'evde herkesin daha iyi hissetmesi için yapıldığını açıklayabilirsiniz. Görüşmeye gelmek istemeyen bir aile üyesi varsa onu zorlamak yerine, görüşmeye '
                                     'katılanlarla başlamak da bir seçenektir; değişim çoğu zaman ailenin tamamına yansır.</p>\n'
                                     '<h2>Gizlilik ve bireysel görüşmeler</h2>\n'
                                     '<p>Aile çalışması sırasında gerekirse aile üyeleriyle bireysel görüşmeler de planlanabilir. Bu görüşmelerde paylaşılanların aile görüşmelerine nasıl taşınacağı '
                                     'baştan konuşulur. Görüşmeler meslek etiği çerçevesinde gizli tutulur; ancak bir aile üyesinin güvenliğini tehdit eden bir durum varsa bu bilgi ilgili kişilerle '
                                     "paylaşılır. Görüşmeler Konutkent'teki ofisimizde yüz yüze ya da uygun durumlarda online yapılabilir.</p>\n"
                                     '<h2>Aile içinde küçük değişimlerle başlamak</h2>\n'
                                     '<p>Aile görüşmelerinde büyük değişiklikler hedeflemek yerine, günlük hayatta uygulanabilir küçük adımlarla başlamak çoğu zaman daha işe yarar. Haftada bir '
                                     'ekranların kapalı olduğu bir aile yemeği, sabah hazırlığında tekrar eden tartışmalar için birlikte belirlenen bir düzen ya da her çocukla kısa bir baş başa '
                                     'zaman gibi adımlar, ailedeki havayı fark edilir biçimde değiştirebilir. Bu adımların evde nasıl gittiği bir sonraki görüşmede konuşulur; işe yaramayan noktalar '
                                     'birlikte yeniden düzenlenir. Böylece değişim, ailenin kendi ritmine uygun biçimde yerleşir.</p>',
                             'sss': [('Aile görüşmeleri ne kadar sürer?',
                                      'Aile görüşmelerinin sayısı ve sıklığı ailenin ihtiyacına göre birlikte belirlenir. Düzenli aralıklarla süreç değerlendirilir ve plan buna göre güncellenir.'),
                                     ('Büyükanne ya da büyükbaba da görüşmeye katılabilir mi?',
                                      'Evet. Aile içinde önemli bir rol üstlenen büyükler, ihtiyaç olduğunda görüşmelere davet edilebilir. Kimlerin katılacağı ilk görüşmede birlikte planlanır.'),
                                     ('Çocuğumuz küçükse aile görüşmesine katılabilir mi?',
                                      'Küçük çocuklar da yaşlarına uygun biçimde, oyun ve çizim gibi etkinliklerle aile görüşmelerine katılabilir. Bazı konular ise yalnızca ebeveynlerle konuşulur.')],
                             'tarih': '2026-10-27'},
 '/cayyolu-cift-terapisi/': {'html': '<h2>İlk çift görüşmesinde neler olur?</h2>\n'
                                     '<p>İlk görüşme, ilişkinizin bugün nerede durduğunu birlikte anlamak için yapılır. Her iki partnerin de bakış açısını anlatabileceği bir alan açılır; kimin haklı '
                                     'olduğundan çok, ilişkide tekrar eden döngünün nasıl işlediği konuşulur. Bu görüşmede ilişkinin kısa öyküsü, şu anki zorluklar ve sizi görüşmeye getiren son '
                                     'gelişme ele alınır.</p>\n'
                                     '<p>Görüşmenin sonunda nasıl bir çalışma planı izleneceği, görüşmelerin sıklığı ve gerekirse bireysel görüşmelerin yapılıp yapılmayacağı birlikte belirlenir. İlk '
                                     'görüşmeden sonra her iki partnerin de sürece devam etmek isteyip istemediğine kendi başına karar vermesine alan tanınır.</p>\n'
                                     '<h2>Görüşmeler arasında ne yapabilirsiniz?</h2>\n'
                                     '<p>Çift görüşmelerinde konuşulanların gündelik hayata taşınması, sürecin en önemli parçalarından biridir. Bu nedenle görüşmeler arasında küçük ve uygulanabilir '
                                     'adımlar önerilebilir:</p>\n'
                                     '<ul>\n'
                                     '<li><b>Haftalık kısa bir konuşma zamanı:</b> Sorunların değil, haftanın nasıl geçtiğinin konuşulduğu, dikkatin dağılmadığı bir zaman ayırmak.</li>\n'
                                     '<li><b>Mola işareti:</b> Tartışma kontrolden çıkmaya başladığında iki tarafın da kullanabileceği, önceden kararlaştırılmış bir ara verme yolu.</li>\n'
                                     '<li><b>Ben dili:</b> "Sen hep…" yerine "Ben … olduğunda kırılıyorum" diye başlayan cümleler kurmayı denemek.</li>\n'
                                     '</ul>\n'
                                     '<p>Bu adımlar her zaman ilk denemede işe yaramaz; zorlandığınız noktalar bir sonraki görüşmede birlikte ele alınır.</p>\n'
                                     '<h2>Çift görüşmesi için ne zaman başvurmalı?</h2>\n'
                                     '<p>Birçok çift, sorunlar iyice yerleştikten sonra destek arar. Oysa daha erken başvurmak, birikmiş kırgınlıkların derinleşmesini önleyebilir. Şu durumlarda bir '
                                     'uzmanla görüşmeyi düşünebilirsiniz:</p>\n'
                                     '<ul>\n'
                                     '<li>Aynı konular üzerine tekrar tekrar tartışıyor ve bir yere varamıyorsanız</li>\n'
                                     '<li>Konuşmak yerine susmayı ya da birbirinizden kaçınmayı tercih eder hâle geldiyseniz</li>\n'
                                     '<li>Güveni sarsan bir olay yaşadıysanız</li>\n'
                                     '<li>Çocuk sahibi olmak, taşınmak ya da iş değişikliği gibi büyük bir geçiş döneminden geçiyorsanız</li>\n'
                                     '</ul>\n'
                                     '<h2>Gizlilik ve güvenli bir alan</h2>\n'
                                     '<p>Çift görüşmelerinde konuşulanlar meslek etiği çerçevesinde gizli tutulur. Bireysel görüşme yapılması gerektiğinde, bu görüşmelerde paylaşılanların ortak '
                                     'görüşmelere nasıl yansıyacağı baştan konuşulur; böylece iki partner de neyin paylaşılacağını bilir. İlişkide fiziksel şiddet ya da güvenliği tehdit eden bir '
                                     'durum varsa öncelik her zaman güvenliktir; acil durumlarda 112 aranmalıdır.</p>\n'
                                     '<h2>Partnerlerden biri tereddüt ediyorsa</h2>\n'
                                     '<p>Çift görüşmelerine başvuran birçok çiftte partnerlerden biri daha istekli, diğeri daha temkinlidir. Bu durum oldukça olağandır. Tereddüt eden partnerin '
                                     'kaygıları çoğu zaman suçlanmak, yargılanmak ya da özel konuların konuşulmak zorunda kalınması üzerinedir. İlk görüşmede bu kaygılar açıkça konuşulabilir; hangi '
                                     'konuların, ne zaman ve hangi hızda ele alınacağına birlikte karar verilir. Tek bir tanışma görüşmesiyle başlamak ve sonra devam edip etmemeye birlikte karar '
                                     'vermek, tereddüt eden partner için ilk adımı kolaylaştırır.</p><p>Evlilikte tekrar eden tartışmalar üzerine: <a href="/evlilikte-iletisim-sorunlari/">Evlilikte '
                                     'iletişim sorunları</a>.</p>',
                             'sss': [('Çift görüşmesi online yapılabilir mi?',
                                      'Evet. Partnerlerden biri farklı bir şehirdeyse ya da yoğun çalışma saatleri nedeniyle ofise gelmek zorsa görüşmeler online da yapılabilir. Her iki partnerin de '
                                      'rahat konuşabileceği sessiz bir ortam önemlidir.'),
                                     ('Çift terapisinde ayrılma kararı da konuşulur mu?',
                                      'Evet. Çift görüşmelerinin amacı her durumda ilişkiyi sürdürmek değildir; bazen çiftler ayrılık kararını daha sakin ve saygılı biçimde vermek için de destek '
                                      'alır.'),
                                     ('Görüşmelere çocuğumuzu da getirmeli miyiz?',
                                      'Çift görüşmeleri genellikle yalnızca partnerlerle yapılır. Çocuklarla ilgili bir konu ele alınacaksa ebeveyn görüşmesi ya da aile görüşmesi ayrıca '
                                      'planlanabilir.')],
                             'tarih': '2026-10-27'},
 '/cayyolu-cocuk-psikologu/': {'html': '<h2>İlk görüşmeye çocuğunuzu nasıl hazırlayabilirsiniz?</h2>\n'
                                       '<p>Çocuklar yeni bir ortama gitmeden önce ne olacağını bilmek ister. Görüşmeden bir iki gün önce, sakin bir anda, kısa ve dürüst bir açıklama yapmanız '
                                       'yeterlidir. "Duyguları anlamaya yardım eden biriyle tanışacağız; birlikte oyun oynayıp konuşacaksınız" gibi bir cümle çoğu çocuk için anlaşılırdır.</p>\n'
                                       '<ul>\n'
                                       '<li><b>Ceza gibi sunmayın:</b> "Yaramazlık yaptığın için gidiyoruz" demek, çocuğun görüşmeye kaygıyla gelmesine yol açar.</li>\n'
                                       '<li><b>Söz vermeyin, sözünüzü tutun:</b> Görüşmede ne olacağını bilmediğiniz konularda tahmin yürütmek yerine "Gidince birlikte göreceğiz" '
                                       'diyebilirsiniz.</li>\n'
                                       '<li><b>Sorularını ciddiye alın:</b> Çocuğunuz merak ettiklerini sorarsa kısa ve sakin yanıtlar verin.</li>\n'
                                       '</ul>\n'
                                       '<h2>Çocukla görüşmelerde ebeveynin rolü</h2>\n'
                                       '<p>Çocukla yapılan çalışmanın etkili olması, büyük ölçüde evde neler olduğuna bağlıdır. Bu nedenle süreç yalnızca çocukla yapılan görüşmelerden oluşmaz; '
                                       'belirli aralıklarla ebeveynlerle de görüşülür. Bu görüşmelerde çocuğun gelişimi hakkındaki gözlemler paylaşılır, evde uygulanabilecek küçük ve somut adımlar '
                                       'birlikte belirlenir.</p>\n'
                                       '<p>Anne ve babanın aynı görüşmeye katılabilmesi çoğu zaman sürece katkı sağlar. Ebeveynlerin ayrı yaşadığı durumlarda da her iki ebeveynin süreçten haberdar '
                                       'olması ve mümkünse sürece dahil olması önemlidir. Çocuğun kendine ait bir alanı olduğunu hissetmesi için görüşmelerde konuşulanların ayrıntısı paylaşılmaz; '
                                       'ancak çocuğun güvenliğini ilgilendiren bir durum olduğunda ebeveynler mutlaka bilgilendirilir.</p>\n'
                                       '<h2>Okul ve öğretmenle iş birliği</h2>\n'
                                       '<p>Bazı zorluklar en çok okulda görünür: derse katılmamak, arkadaş ilişkilerinde sorunlar, öğretmenin dikkat çektiği davranışlar. Böyle durumlarda öğretmenin '
                                       'gözlemleri değerli bir bilgi kaynağıdır. Ebeveynlerin onayıyla, okulla paylaşılabilecek genel öneriler üzerine konuşulabilir. Okul rehberlik servisiyle uyumlu '
                                       'bir yaklaşım, çocuğun evde ve okulda benzer bir tutumla karşılaşmasını sağlar.</p>\n'
                                       '<h2>Görüşmeler ne sıklıkta ve nasıl planlanır?</h2>\n'
                                       '<p>Çocuk görüşmeleri genellikle haftada bir yapılır ve düzenli bir gün ile saatte sürdürülmesi önerilir; bu öngörülebilirlik çocuğun kendini güvende '
                                       'hissetmesine yardım eder. Okul saatleri göz önünde bulundurularak hafta içi akşamüstü ya da cumartesi saatleri planlanabilir. Ofisimiz Dumlupınar Bulvarı '
                                       'No:399, Konutkent adresindedir ve ücretsiz otopark vardır; bu da okul çıkışı gelen aileler için ulaşımı kolaylaştırır. Sürecin ne kadar süreceği, çocuğun '
                                       'ihtiyaçlarına ve ilerleyişe göre ebeveynlerle birlikte değerlendirilir.</p>\n'
                                       '<h2>Çocuğunuzun ihtiyaçlarını gözlemlerken nelere dikkat edebilirsiniz?</h2>\n'
                                       '<p>Görüşmeye başlamadan önce ya da süreç boyunca kısa notlar tutmak, hem sizin hem de uzmanın çocuğunuzu daha iyi anlamasına yardım eder. Zorlanılan '
                                       'durumların hangi saatlerde, hangi ortamlarda ve kimlerle birlikteyken ortaya çıktığını yazmanız yeterlidir. Örneğin öfke nöbetleri daha çok yorgunken mi, okul '
                                       'çıkışında mı, yoksa ekran süresi bittiğinde mi görülüyor? Uyku, iştah ve oyun düzenindeki değişiklikleri de not edebilirsiniz. Bu gözlemler, görüşmelerde '
                                       'somut örnekler üzerinden çalışmayı kolaylaştırır ve küçük ilerlemelerin fark edilmesini sağlar.</p>',
                               'sss': [('Çocuğum görüşmede hiç konuşmazsa ne olur?',
                                        'İlk görüşmelerde çocukların sessiz kalması çok olağandır. Oyun, çizim ve etkinlikler çocuğun kendini konuşmadan da ifade etmesine alan açar; güven zamanla '
                                        'oluşur.'),
                                       ('Görüşmeye kardeşini de getirebilir miyim?',
                                        'Görüşme odasına yalnızca görüşmeye gelen çocuk ve gerektiğinde ebeveyn alınır. Kardeşin bekleme alanında bir yetişkinle kalması gerekir; mümkünse görüşme '
                                        'saatini buna göre planlamanızı öneririz.'),
                                       ('Okul tatilinde görüşmelere ara vermeli miyiz?',
                                        'Tatiller planlanabilir; ancak uzun aralar sürecin ritmini bozabilir. Tatil dönemini önceden konuşarak görüşme sıklığını birlikte ayarlayabiliriz.')],
                               'tarih': '2026-10-27'},
 '/cayyolu-psikolog-fiyatlari/': {'html': '<h2>Seans süresi ve görüşme sıklığı nasıl planlanır?</h2>\n'
                                          '<p>Bir görüşmenin toplam maliyetini belirleyen şey yalnızca tek bir seansın ücreti değildir; görüşmelerin ne sıklıkla ve ne kadar süreyle yapılacağı da '
                                          'önemlidir. Bireysel görüşmeler genellikle haftada bir ya da iki haftada bir planlanır. Süreç ilerledikçe ve ihtiyaçlar değiştikçe görüşme aralıkları '
                                          'birlikte gözden geçirilir.</p>\n'
                                          '<p>Başlangıçta kaç görüşme yapılacağını net olarak söylemek çoğu zaman mümkün değildir; çünkü bu, başvuru nedeninize, hedeflerinize ve sürecin nasıl '
                                          'ilerlediğine bağlıdır. Ancak ilk görüşmelerden sonra nasıl bir yol izleneceği ve görüşmelerin ne sıklıkla sürdürüleceği sizinle açıkça konuşulur. Böylece '
                                          'bütçenizi önceden planlayabilirsiniz.</p>\n'
                                          '<h2>Ücrete neler dahildir?</h2>\n'
                                          '<ul>\n'
                                          '<li><b>Görüşmenin kendisi:</b> Uzmanla yapılan görüşme süresinin tamamı.</li>\n'
                                          '<li><b>Ebeveyn görüşmeleri:</b> Çocuk ve ergen çalışmalarında ebeveynlerle yapılan bilgilendirme görüşmelerinin nasıl ücretlendirileceği baştan '
                                          'açıklanır.</li>\n'
                                          '<li><b>Psikolojik testler:</b> Bir test ya da değerlendirme gerekirse, kapsamı ve ücreti uygulanmadan önce ayrıca paylaşılır.</li>\n'
                                          "<li><b>Ofis olanakları:</b> Konutkent'teki ofisimizde ücretsiz otopark vardır; ulaşım için ek bir otopark masrafınız olmaz.</li>\n"
                                          '</ul>\n'
                                          '<h2>Ücret sorarken hangi bilgileri paylaşmalısınız?</h2>\n'
                                          '<p>Size doğru bilgi verebilmemiz için ücret sorarken birkaç bilgiyi paylaşmanız yeterlidir:</p>\n'
                                          '<ul>\n'
                                          '<li>Görüşmenin kimin için olduğu (kendiniz, çiftiniz, çocuğunuz ya da aileniz)</li>\n'
                                          '<li>Yüz yüze mi, online mı görüşmek istediğiniz</li>\n'
                                          '<li>Tercih ettiğiniz bir uzman varsa adı</li>\n'
                                          '<li>Size uygun gün ve saat aralıkları</li>\n'
                                          '</ul>\n'
                                          "<p>Bu bilgilerle size uygun uzmanı, saati ve güncel ücreti aynı konuşmada öğrenebilirsiniz. Telefonu açamadığımız saatlerde WhatsApp'tan mesaj "
                                          'bırakabilirsiniz; size dönüş yapılır.</p>\n'
                                          '<h2>Ücret karşılaştırırken dikkat edilmesi gerekenler</h2>\n'
                                          '<p>Psikolojik destek alırken yalnızca ücreti karşılaştırmak yanıltıcı olabilir. Görüşmeyi yürüten kişinin psikoloji eğitimi almış bir uzman olup '
                                          'olmadığını, hangi alanlarda deneyim sahibi olduğunu ve etik ilkelere bağlı çalışıp çalışmadığını sorgulamanızı öneririz. Çok düşük ücretli ya da sonucu '
                                          'önceden vaat eden hizmetlere karşı dikkatli olun. Görüşme süresi, iptal koşulları ve ödeme biçimi gibi konuları randevu almadan önce açıkça sormaktan '
                                          'çekinmeyin.</p>\n'
                                          '<h2>Bütçenize uygun bir plan yapmak</h2>\n'
                                          '<p>Psikolojik destek, çoğu zaman tek bir görüşmeyle sınırlı kalmayan bir süreçtir. Bu nedenle bütçenizi düşünerek bir plan yapmak isterseniz bunu ilk '
                                          'görüşmede açıkça konuşabilirsiniz. Görüşme sıklığı, sürecin farklı aşamalarında ihtiyaca göre değişebilir; örneğin başlangıçta daha sık, ilerleyen dönemde '
                                          'daha seyrek görüşmeler planlanabilir. Ücret konusunu konuşmak sürecin doğal bir parçasıdır; bu konudaki sorularınızı rahatlıkla sorabilirsiniz.</p>',
                                  'sss': [('Görüşme ücretini görüşmeden önce mi, sonra mı ödüyorum?',
                                           'Ödeme biçimi ve zamanı randevu oluşturulurken size açıkça bildirilir. Aklınıza takılan her konuyu bu aşamada sorabilirsiniz.'),
                                          ('Randevumu iptal edersem ücret alınır mı?',
                                           'İptal ve randevu değişikliği koşulları randevu oluşturulurken paylaşılır. Gelemeyeceğiniz durumlarda mümkün olduğunca erken haber vermeniz önemlidir.')],
                                  'tarih': '2026-10-27'},
 '/cayyolu-psikolojik-danismanlik-merkezi/': {'html': '<h2>Başvurudan ilk görüşmeye adım adım süreç</h2>\n'
                                                      '<ul>\n'
                                                      "<li><b>1. İlk temas:</b> Telefonla ya da WhatsApp'tan bize ulaşırsınız. Kısaca hangi konuda destek almak istediğinizi ve kimin için "
                                                      'başvurduğunuzu paylaşmanız yeterlidir; ayrıntıya girmeniz gerekmez.</li>\n'
                                                      '<li><b>2. Uygun uzman ve saat:</b> Başvuru nedeninize ve görüşme türüne göre size uygun uzman ve saat birlikte belirlenir. Ücret ve iptal '
                                                      'koşulları bu aşamada açıkça paylaşılır.</li>\n'
                                                      '<li><b>3. İlk görüşme:</b> Sizi neyin getirdiği, ne zamandır sürdüğü ve beklentileriniz konuşulur. Görüşmenin sonunda nasıl bir yol izleneceği '
                                                      'birlikte planlanır.</li>\n'
                                                      '<li><b>4. Düzenli görüşmeler:</b> Görüşmeler genellikle haftalık ya da iki haftalık aralıklarla sürdürülür ve süreç belirli aralıklarla '
                                                      'birlikte değerlendirilir.</li>\n'
                                                      '</ul>\n'
                                                      '<h2>Gizlilik ve etik ilkeler</h2>\n'
                                                      '<p>Merkezimizde yapılan tüm görüşmeler meslek etiği çerçevesinde gizli tutulur. Görüşmelerde paylaştıklarınız, sizin izniniz olmadan kimseyle '
                                                      'paylaşılmaz. Yalnızca sizin ya da bir başkasının hayatını tehdit eden durumlar gibi yasal ve etik olarak zorunlu hâllerde bu ilkenin sınırları '
                                                      'vardır; bu sınırlar ilk görüşmede açıkça konuşulur. Çocuk ve ergenlerle yapılan çalışmalarda ebeveynlerle neyin, nasıl paylaşılacağı da baştan '
                                                      'netleştirilir.</p>\n'
                                                      '<h2>Yüz yüze ve online görüşme bir arada</h2>\n'
                                                      '<p>Görüşmeler Dumlupınar Bulvarı No:399, Konutkent adresindeki ofisimizde yüz yüze yapılır; binada ücretsiz otopark vardır. Pazartesi – '
                                                      'Cumartesi 09:00 – 20:00 arasında randevu verilir. Seyahat, hastalık ya da yoğun dönemler nedeniyle ofise gelemediğiniz haftalarda aynı uzmanla '
                                                      'online görüşmeye geçebilirsiniz. Böylece görüşmelerin sürekliliği bozulmaz.</p>\n'
                                                      '<h2>Bir uzmana başvurmanın zamanı geldiğini gösteren işaretler</h2>\n'
                                                      '<p>Psikolojik destek almak için sorunun çok büyümesini beklemek gerekmez. Şu durumlardan biri sizin için tanıdıksa bir uzmanla görüşmek iyi '
                                                      'gelebilir:</p>\n'
                                                      '<ul>\n'
                                                      '<li>Uzun süredir kendinizi yorgun, gergin ya da isteksiz hissediyorsanız</li>\n'
                                                      '<li>Uyku, iştah ya da odaklanma düzeniniz belirgin biçimde değiştiyse</li>\n'
                                                      '<li>İlişkilerinizde ya da ailenizde aynı sorunlar tekrar ediyorsa</li>\n'
                                                      '<li>Çocuğunuzun davranışlarında sizi düşündüren bir değişiklik fark ettiyseniz</li>\n'
                                                      '<li>Bir kayıp, ayrılık ya da büyük bir değişimin ardından toparlanmakta zorlanıyorsanız</li>\n'
                                                      '</ul>\n'
                                                      "<p>Kendinize ya da bir başkasına zarar verme düşünceleri varsa beklemeden 112'yi arayın.</p>\n"
                                                      '<h2>Size uygun görüşme türünü nasıl seçersiniz?</h2>\n'
                                                      '<p>Başvuru sırasında hangi görüşme türünün size uygun olduğunu bilmeniz gerekmez. Kendi duygularınız, ilişkileriniz ya da yaşam '
                                                      'değişiklikleriyle ilgili bir konuda destek arıyorsanız bireysel görüşme; partnerinizle yaşadığınız sorunlar için çift görüşmesi; çocuğunuzun '
                                                      'davranışları ya da duyguları sizi düşündürüyorsa çocuk ve ebeveyn görüşmeleri; evde herkesin etkilendiği bir durum varsa aile görüşmesi uygun '
                                                      'olabilir. Kararsız kaldığınızda bunu randevu sırasında söylemeniz yeterlidir; başvuru nedeninize göre en uygun başlangıç birlikte '
                                                      'belirlenir.</p>',
                                              'sss': [('İlk görüşmeden önce bir form doldurmam gerekiyor mu?',
                                                       'Hayır. Randevu sırasında yalnızca iletişim bilgileriniz ve kısaca başvuru nedeniniz alınır; gerisi ilk görüşmede konuşulur.'),
                                                      ('Görüşmelerim sırasında uzman değiştirmek mümkün mü?',
                                                       'Evet. Görüşmelerin işe yaraması için uzmanla aranızda güven olması önemlidir. Kendinizi rahat hissetmezseniz bunu açıkça söyleyebilir, başka '
                                                       'bir uzmanla devam etmeyi konuşabilirsiniz.'),
                                                      ('Bekleme alanında başka danışanlarla karşılaşır mıyım?',
                                                       'Randevular, danışanların birbirleriyle karşılaşmasını en aza indirecek biçimde planlanır. Mahremiyetiniz konusunda bir isteğiniz varsa randevu '
                                                       'alırken belirtebilirsiniz.')],
                                              'tarih': '2026-10-27'},
 '/cift-iliski-terapisi/': {'html': '<h2>Çift olarak randevu almak: pratik adımlar</h2>\n'
                                    '<p>Çift görüşmesi için randevuyu iki taraftan biri alabilir. Randevu sırasında kısaca neden başvurduğunuzu ve iki tarafın da gelmeye istekli olup olmadığını '
                                    'paylaşmanız, görüşmenin planlanmasını kolaylaştırır. Çiftlerin ortak boş zamanı bulmak çoğu zaman zor olduğu için akşam ve cumartesi saatleri sık tercih '
                                    'ediliyor; görüşmeler pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabilir.</p>\n'
                                    '<ul>\n'
                                    "<li><b>Ayrı yerlerden gelmek:</b> İş çıkışı farklı yerlerden gelecekseniz, ofisimizin Konutkent'te Dumlupınar Bulvarı üzerinde olması ve binadaki ücretsiz "
                                    'otopark işinizi kolaylaştırır.</li>\n'
                                    '<li><b>Biri şehir dışındaysa:</b> Çok zorunlu durumlarda görüşmeler online yapılabilir. Ancak çift görüşmelerinde iki tarafın aynı ortamda olması genellikle '
                                    'tercih edilir; bu konu birlikte değerlendirilir.</li>\n'
                                    '</ul>\n'
                                    '<h2>Görüşme öncesinde ve sonrasında evde</h2>\n'
                                    '<p>Çiftler bazen görüşmeye gelirken yolda tartışmaya başladıklarını ya da görüşme sonrası eve dönünce konuşmaya devam edip yeniden gerildiklerini anlatır. Bu çok '
                                    'sık görülen bir durumdur. Görüşmede açılan konuları evde hemen "bitirmeye" çalışmak yerine, bir sonraki görüşmeye taşımak çoğu zaman daha sağlıklıdır. '
                                    'Görüşmelerde, ev için küçük ve uygulanabilir adımlar birlikte belirlenir; örneğin haftada bir kez telefonsuz kısa bir sohbet zamanı ya da tartışma büyüdüğünde '
                                    'ara vermenin ortak bir işareti.</p>\n'
                                    '<h2>Bireysel görüşmelerin yeri</h2>\n'
                                    '<p>Çift çalışması sürerken zaman zaman taraflarla ayrı ayrı görüşmek gerekebilir. Bu görüşmeler, her birinin kendi duygusunu daha rahat ifade etmesine yardım '
                                    'eder. Burada önemli bir ilke vardır: Çift çalışmasında psikolog taraflardan birinin sırrını saklayan kişi konumuna geçmez; bireysel görüşmelerde konuşulanların '
                                    'çift sürecine nasıl yansıyacağı baştan açıkça konuşulur.</p>\n'
                                    '<p>Taraflardan biri bir süre sonra kendi konularına daha derinlemesine bakmak isterse, bireysel görüşmelerin ayrı bir uzmanla yürütülmesi önerilebilir. Böylece '
                                    'çift sürecinin tarafsızlığı korunur.</p>\n'
                                    '<h2>Hangi çiftler başvuruyor?</h2>\n'
                                    '<p>Çift görüşmelerine yalnızca evlilikte kriz yaşayan çiftler başvurmaz. Uzun süredir birlikte olup birbirinden uzaklaştığını hisseden çiftler, ilk çocuktan '
                                    'sonra ilişkisi değişen eşler, aile büyükleriyle sınır konusunda zorlanan çiftler, güven sarsıntısı yaşayanlar ya da ayrılık kararını sakin bir zeminde konuşmak '
                                    'isteyenler de başvurur. Bazı çiftler ise ortada büyük bir sorun yokken, tekrar eden küçük tartışmaların büyümemesi için gelir. Görüşmelerin amacı her zaman '
                                    'ilişkiyi sürdürmek değildir; amaç, iki tarafın da ne istediğini netleştirip kararlarını daha sağlıklı biçimde verebilmesidir.</p>\n'
                                    '<p>Çift terapisinin nasıl ilerlediği, hangi durumlarda başvurulduğu ve sık sorulan sorular için ayrıntılı rehber: <a '
                                    'href="https://www.psikologrojinnazik.com/cift-iliski-terapisi/">Çift ve ilişki terapisi hakkında bilmeniz gerekenler</a></p>',
                            'sss': [('Randevuyu ikimizden biri alabilir mi?', 'Evet. Randevuyu taraflardan biri alabilir; görüşmeye iki tarafın da katılması planlanır.'),
                                    ('Görüşme sırasında tartışırsak ne olur?',
                                     'Görüşmelerde gerginlik yaşanması olağandır. Psikolog konuşmanın güvenli kalmasına yardım eder ve tartışmanın altındaki ihtiyaçları anlamaya odaklanır.'),
                                    ('Çift görüşmeleri ne sıklıkla yapılır?',
                                     'Genellikle haftada bir ya da iki haftada bir yapılır; sıklık çiftin ihtiyacına ve programına göre birlikte belirlenir.')],
                            'tarih': '2026-10-27'},
 '/cocuk-ergen-danismanligi/': {'html': '<h2>Çocuğunuz için randevu: ilk adım ebeveyn görüşmesi</h2>\n'
                                        '<p>Çocuk ve ergen görüşmelerinde süreç genellikle ebeveynlerle yapılan bir ön görüşmeyle başlar. Bu görüşmede çocuğunuzun gelişim öyküsü, sizi kaygılandıran '
                                        'durumun ne zamandır sürdüğü, evde ve okulda nasıl göründüğü konuşulur. Ön görüşmeye mümkünse iki ebeveynin birlikte katılması önerilir; bu mümkün değilse '
                                        'diğer ebeveynle ayrıca görüşme planlanabilir. Ardından çocuğunuzla tanışma görüşmeleri yapılır.</p>\n'
                                        '<ul>\n'
                                        '<li><b>Okul saatleriyle çakışmaması için:</b> Görüşmeler pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabildiğinden, okul sonrası ve cumartesi '
                                        'saatleri ailelerin sık tercih ettiği zamanlardır.</li>\n'
                                        "<li><b>Ulaşım:</b> Ofisimiz Konutkent'te, Dumlupınar Bulvarı No:399 adresindedir; binada ücretsiz otopark vardır.</li>\n"
                                        '</ul>\n'
                                        '<h2>Ofise ilk gelişte çocuğun rahat etmesi</h2>\n'
                                        '<p>Küçük çocuklar için yeni bir yere gelmek ve tanımadığı bir yetişkinle konuşmak heyecan verici ya da ürkütücü olabilir. Görüşmeye birkaç dakika erken '
                                        'gelmek, çocuğun ortama alışmasına zaman tanır. İlk görüşmelerde bir süre ebeveynin de odada bulunması gerekebilir; çocuk hazır hissettiğinde ebeveyn bekleme '
                                        'alanına geçer. Ergenlerde ise görüşmenin büyük kısmı gencin kendisiyle yapılır ve gencin özel alanına saygı sürecin temelidir.</p>\n'
                                        '<p>Çocuğa neden gideceğini anlatırken "cezalandırılma" çağrışımı yapan ifadelerden kaçınmak, onun görüşmelere daha rahat başlamasına yardım eder.</p>\n'
                                        '<h2>Süreç boyunca ebeveynlerle iletişim</h2>\n'
                                        '<p>Çocukla yapılan görüşmelerin yanında, belirli aralıklarla ebeveyn görüşmeleri de yapılır. Bu görüşmelerde çocuğun genel gidişatı paylaşılır ve evde neyin '
                                        'işe yarayabileceği birlikte konuşulur. Çocuğun ya da gencin görüşmede anlattığı her ayrıntı ebeveynle paylaşılmaz; ancak güvenliğini ilgilendiren bir durum '
                                        'varsa aile mutlaka bilgilendirilir. Bu denge ilk görüşmede hem aileye hem çocuğa açıkça anlatılır.</p>\n'
                                        '<p>Okulla iş birliği gerektiğinde, bunun hangi bilgilerle ve nasıl yapılacağı önce aileyle konuşulur; aile onayı olmadan okulla bilgi paylaşılmaz.</p>\n'
                                        '<h2>Hangi durumlarda başvuruluyor?</h2>\n'
                                        '<p>Ailelerin bizi aradığı durumlar çok çeşitlidir: Okula başlama ya da okul değişikliğinde uyum güçlüğü, kardeş doğumu sonrası değişen davranışlar, öfke '
                                        'nöbetleri, uyku ve ayrılma sorunları, sınav dönemlerinde yoğun kaygı, ekran kullanımı üzerine çatışmalar ya da ergenin aileyle iletişimi kesmesi. Bazen tek '
                                        'bir belirgin sorun yoktur; ebeveyn yalnızca çocuğundaki bir değişikliğin nedenini anlamak ister. Emin olamadığınız durumlarda bir ebeveyn görüşmesi, '
                                        'çocuğunuzun görüşmelere ihtiyacı olup olmadığını değerlendirmek için iyi bir başlangıçtır.</p>\n'
                                        '<p>Çocuk ve ergen danışmanlığının hangi durumlarda gerektiği ve kullanılan yöntemler için ayrıntılı rehber: <a '
                                        'href="https://www.psikologrojinnazik.com/cocuk-ergen-danismanligi/">Çocuk ve ergen danışmanlığı rehberi</a></p><p>Ailede bir kayıp yaşandıysa: <a '
                                        'href="/cocuklarda-yas-ve-kayip/">Çocuklarda yas ve kayıp: ebeveynler için rehber</a>.</p>',
                                'sss': [('İlk görüşmeye çocuğumu da getirmeli miyim?',
                                         'Genellikle ilk görüşme yalnızca ebeveynlerle yapılır; çocukla tanışma görüşmeleri bundan sonra planlanır. Ergenlerde bu sıra durumun özelliğine göre '
                                         'değişebilir.'),
                                        ('Görüşme sırasında ben nerede beklerim?',
                                         'Çocuk hazır hissettiğinde ebeveyn bekleme alanında bekler. İlk görüşmelerde çocuğun rahat etmesi için bir süre odada kalmanız istenebilir.'),
                                        ('Ergen çocuğum gelmek istemiyorsa ne yapabilirim?',
                                         'Önce ebeveyn olarak siz görüşmeye başlayabilirsiniz. Gencin görüşmeye nasıl davet edileceği bu görüşmelerde birlikte planlanır.')],
                                'tarih': '2026-10-27'},
 '/cocuklarda-kaygi-ebeveyn-rehberi/': {'html': '<h2>Yaşa göre kaygı nasıl görünür?</h2>\n'
                                                '<ul>\n'
                                                '<li><b>Okul öncesi dönem:</b> Anne babadan ayrılırken ağlama, yabancılardan çekinme, karanlık ya da hayvan korkuları sık görülür.</li>\n'
                                                '<li><b>İlkokul dönemi:</b> Okulda başarısız olma, arkadaşlar tarafından dışlanma, ailesine bir şey olacağı ya da hastalanma endişeleri öne çıkabilir. '
                                                'Karın ağrısı ve baş ağrısı gibi bedensel yakınmalar kaygının dili olabilir.</li>\n'
                                                '<li><b>Ergenlik:</b> Sosyal kabul, görünüş, sınavlar ve gelecekle ilgili kaygılar artar. Ergen kaygısını öfke ya da geri çekilmeyle '
                                                'gösterebilir.</li>\n'
                                                '</ul>\n'
                                                '<h2>Güven vermek ile kaygıyı beslemek arasındaki ince çizgi</h2>\n'
                                                '<p>Kaygılı bir çocuğu rahatlatmak istemek çok doğaldır. Ancak çocuk aynı soruyu sürekli sorduğunda ve her seferinde uzun güvencelerle '
                                                'karşılaştığında, kaygı geçici olarak azalır ama kısa sürede geri gelir. Zamanla çocuk rahatlamak için ebeveynin güvencesine daha çok ihtiyaç duyar. '
                                                'Bunun yerine çocuğun duygusunu kabul eden kısa bir yanıt verip onu kendi baş etme yollarını denemeye teşvik etmek daha yararlıdır: "Endişelendiğini '
                                                'görüyorum. Geçen sefer ne yapmıştın, hatırlıyor musun?"</p>\n'
                                                '<h2>Kendi kaygınızın çocuğa yansıması</h2>\n'
                                                '<p>Çocuklar, ebeveynlerinin belirsiz durumlara nasıl tepki verdiğini yakından izler. Sık sık "dikkat et, düşersin" ya da "ya bir şey olursa" diyen '
                                                'bir ebeveyn, farkında olmadan dünyayı tehlikeli bir yer olarak tanımlayabilir. Kendi kaygılarınızı fark etmek ve çocuğunuzun yanında sakin bir model '
                                                'olmaya çalışmak, onun kaygısını yönetmesine de yardım eder. Kendi kaygınız sizi zorluyorsa bu konuda destek almak, çocuğunuza da dolaylı olarak iyi '
                                                'gelir.</p>\n'
                                                '<h2>Görüşmelerde neler yapılır?</h2>\n'
                                                '<p>İlk görüşme genellikle ebeveynlerle yapılır; kaygının ne zaman başladığı, hangi durumlarda arttığı ve ailenin nasıl tepki verdiği konuşulur. '
                                                'Ardından çocukla yaşına uygun oyun, çizim ya da sohbetle tanışma görüşmeleri yapılır. Çocuğa kaygısını tanımayı ve küçük adımlarla korktuğu '
                                                'durumlarla yüzleşmeyi öğreten çalışmalar planlanır; ebeveynlere de evde tutarlı biçimde uygulayabilecekleri öneriler verilir.</p>\n'
                                                '<h2>Okulla iş birliği</h2>\n'
                                                '<p>Kaygı çoğu zaman okulda da kendini gösterir: Sabah okula gitmek istememek, sınıfta söz almaktan kaçınmak, teneffüste yalnız kalmak ya da sık sık '
                                                'revire gitmek gibi. Öğretmenle ve okul rehberlik servisiyle iletişim kurmak, çocuğunuzun okulda nasıl göründüğünü anlamanıza ve evde yaptığınız '
                                                'çalışmaların okulda da desteklenmesine yardım eder.</p>\n'
                                                '<p>Okulla birlikte küçük ve ulaşılabilir hedefler belirlemek işe yarayabilir: Örneğin sınıfta haftada bir kez söz almak ya da teneffüste bir '
                                                'arkadaşla oyuna katılmak. Kaygılı çocuğu tamamen korumak yerine, desteklenerek zorlandığı durumlarla yüzleşmesine fırsat tanımak kaygıyla baş etme '
                                                'becerisini güçlendirir.</p><p>Ailede bir kayıp yaşandıysa: <a href="/cocuklarda-yas-ve-kayip/">Çocuklarda yas ve kayıp: ebeveynler için '
                                                'rehber</a>.</p>',
                                        'sss': [('Çocuğum her akşam aynı endişeyi soruyor, ne cevap vermeliyim?',
                                                 'Duygusunu kabul eden kısa ve sakin bir yanıt verin, ardından ona kendi baş etme yollarını hatırlatın. Her seferinde uzun açıklamalar yapmak, '
                                                 'kaygının döngüsünü güçlendirebilir.'),
                                                ('Kaygılı çocuğu okul gezisine göndermeli miyim?',
                                                 'Mümkünse göndermeniz önerilir. Önceden ne olacağını konuşmak, küçük bir plan yapmak ve çocuğu desteklemek, kaygıyla baş edebildiğini deneyimlemesine '
                                                 'yardım eder.')],
                                        'tarih': '2026-10-27'},
 '/cocuklarda-uyku-sorunlari/': {'html': '<h2>Yaşa göre uyku: neler beklenir?</h2>\n'
                                         '<p>Çocukların uyku ihtiyacı ve uyku alışkanlıkları yaşla birlikte değişir. Bu değişimi bilmek, neyin olağan neyin destek gerektiren bir durum olduğunu ayırt '
                                         'etmeyi kolaylaştırır.</p>\n'
                                         '<ul>\n'
                                         '<li><b>Okul öncesi dönem:</b> Gece uyanmaları, karanlık korkusu ve ebeveynin yanında uyuma isteği bu yaşlarda sık görülür. Hayal gücünün geliştiği bu '
                                         'dönemde canavar ya da hırsız korkuları da uykuya geçişi zorlaştırabilir.</li>\n'
                                         '<li><b>İlkokul dönemi:</b> Okul, arkadaş ilişkileri ve ödevle ilgili kaygılar yatma saatinde daha çok konuşulur. Çocuk gün içinde bastırdığı endişeleri '
                                         'yatakta dile getirebilir.</li>\n'
                                         '<li><b>Ergenlik:</b> Biyolojik saat doğal olarak geç saatlere kayar. Erken kalkma zorunluluğu, ekran kullanımı ve sınav temposu birleştiğinde kronik '
                                         'uykusuzluk oluşabilir.</li>\n'
                                         '</ul>\n'
                                         '<h2>Yatma saatindeki pazarlıklarla baş etmek</h2>\n'
                                         '<p>"Bir su daha", "bir masal daha" ya da "biraz daha kalsana" istekleri birçok evde her akşam tekrar eder. Bu istekler çoğu zaman ayrılmanın zorluğunu ya da '
                                         'günün sonunda ebeveynle daha fazla zaman geçirme ihtiyacını gösterir.</p>\n'
                                         '<ul>\n'
                                         '<li>Yatma rutinini önceden birlikte belirleyin ve sırasını resimli bir listeyle görünür kılın.</li>\n'
                                         '<li>Rutinin sonunda kısa ve öngörülebilir bir veda cümlesi kullanın; her akşam aynı olması güven verir.</li>\n'
                                         '<li>Gün içinde çocuğunuzla baş başa kısa bir zaman ayırmak, akşam bu ihtiyacın yatma saatine taşınmasını azaltabilir.</li>\n'
                                         '<li>Sınırı koruduğunuzda sakin ve kararlı kalın; öfkeli bir tartışma uykuya geçişi daha da zorlaştırır.</li>\n'
                                         '</ul>\n'
                                         '<h2>Uyku sorunu ailenin tamamını etkilediğinde</h2>\n'
                                         '<p>Uzun süren uyku sorunları yalnızca çocuğu değil, ebeveynlerin uykusunu, sabrını ve eşler arasındaki ilişkiyi de etkiler. Yorgun bir ebeveynin tutarlı '
                                         'kalması zorlaşır; bu da sorunun sürmesine katkıda bulunabilir. Ebeveynlerin dönüşümlü olarak sorumluluk alması ve kendi dinlenmelerine de alan açması bu '
                                         'nedenle önemlidir.</p>\n'
                                         '<h2>Uyku sorunuyla başvurduğunuzda görüşmeler nasıl ilerler?</h2>\n'
                                         '<p>İlk görüşmede çocuğunuzun uyku düzeni, akşam rutini, gün içindeki yaşantısı ve son dönemde ailede yaşanan değişiklikler konuşulur. Birkaç hafta boyunca '
                                         'tutulan basit bir uyku günlüğü örüntüleri görmeyi kolaylaştırır. Ardından aileye uygun, küçük ve uygulanabilir adımlar planlanır; çocuğun yaşına göre oyun '
                                         'ya da çizim yoluyla duyguları anlamaya yönelik görüşmeler de yapılabilir. Horlama, nefes durması ya da sık bedensel yakınmalar varsa önce bir çocuk '
                                         'doktoruna başvurmanız önerilir.</p>\n'
                                         '<h2>Gündüz düzeninin geceye etkisi</h2>\n'
                                         '<p>Gece uykusu, gün içinde olanlardan bağımsız değildir. Gün boyunca yeterince hareket etmeyen, dışarıda vakit geçirmeyen ya da öğleden sonra geç saatte '
                                         'uzun uyuyan çocuk akşam uykuya dalmakta zorlanabilir. Akşam yemeğinin çok geç ya da çok ağır olması, yatmadan hemen önce heyecanlı oyunlar ve kafeinli '
                                         'içecekler de uykuya geçişi geciktirir. Hafta sonları kalkış saatinin hafta içine göre çok kaymaması, pazartesi sabahlarının daha kolay geçmesini '
                                         'sağlar.</p>\n'
                                         '<p>Okul döneminin başlangıcı, tatil dönüşleri ve saat değişiklikleri gibi geçiş zamanlarında uyku düzeni bozulabilir. Bu dönemlerde yatma saatini birkaç gün '
                                         'içinde azar azar öne almak, ani değişikliklere göre çocuğun uyum sağlamasını kolaylaştırır.</p>',
                                 'sss': [('Çocuğum gece sık sık bizim yatağımıza geliyor, ne yapmalıyım?',
                                          'Önce bunun yeni başlayan bir durum mu, yoksa uzun süredir mi devam ettiğine bakın. Çocuğunuzu sakin bir şekilde kendi yatağına geri götürmek ve bunu '
                                          'tutarlı biçimde tekrarlamak çoğu zaman işe yarar; ailede yakın zamanda bir değişiklik olduysa bunu da konuşmak gerekir.'),
                                         ('Ergen çocuğum gece geç saate kadar uyumuyor, normal mi?',
                                          'Ergenlikte biyolojik saatin geç saatlere kayması olağandır. Yine de okul performansı, ruh hâli ya da günlük işlevler etkileniyorsa ekran kullanımı ve akşam '
                                          'düzeni birlikte gözden geçirilmeli, gerekirse destek alınmalıdır.'),
                                         ('Uyku günlüğünde neleri not etmeliyim?',
                                          'Yatma ve uykuya dalma saatini, gece uyanmaları, sabah kalkış saatini, gündüz uykularını ve o gün yaşanan dikkat çekici olayları kısaca not etmeniz '
                                          'yeterlidir.')],
                                 'tarih': '2026-10-27'},
 '/cocuklarda-yas-ve-kayip/': {'html': '<h2>Yaşa göre çocukların ölümü anlaması</h2>\n'
                                       '<p>Çocukların ölümü nasıl anladığı yaşlarına göre değişir. Bunu bilmek, sorularına uygun yanıtlar vermenize yardımcı olur.</p>\n'
                                       '<ul>\n'
                                       '<li><b>Okul öncesi dönem:</b> Ölümün kalıcı olduğunu kavramak zordur. "Dedem ne zaman geri gelecek?" sorusu birçok kez sorulabilir. Sabırla ve aynı sade '
                                       'cümlelerle yanıt vermek önemlidir.</li>\n'
                                       '<li><b>İlkokul dönemi:</b> Ölümün kalıcı olduğu anlaşılmaya başlar; çocuk ayrıntılar hakkında sorular sorabilir ve kendisinin ya da anne babasının ölümünden '
                                       'korkabilir.</li>\n'
                                       '<li><b>Ergenlik:</b> Kaybı yetişkine yakın biçimde anlar ama duygularını aileyle değil, arkadaşlarıyla paylaşmayı tercih edebilir. Öfke, geri çekilme ya da '
                                       'her şey yolundaymış gibi davranma görülebilir.</li>\n'
                                       '</ul>\n'
                                       '<h2>Evcil hayvan kaybı ve diğer kayıplar</h2>\n'
                                       '<p>Çocuklar için kayıp yalnızca bir yakının ölümü değildir. Bir evcil hayvanın ölümü, taşınma, okul değiştirme, yakın bir arkadaşın uzağa gitmesi ya da '
                                       'ebeveynlerin ayrılığı da yas tepkilerine yol açabilir. Evcil hayvan kaybı çoğu zaman çocuğun ölümle ilk karşılaşmasıdır; bu kaybı küçümsemeden konuşmak, '
                                       'ileride yaşanacak kayıplarla baş etmeyi de kolaylaştırır.</p>\n'
                                       '<h2>Okul ve öğretmenle iş birliği</h2>\n'
                                       '<p>Yas, çocuğun okuldaki dikkatini, arkadaş ilişkilerini ve ders başarısını geçici olarak etkileyebilir. Öğretmeni bilgilendirmek, çocuğun okulda zorlandığı '
                                       'anlarda anlayışla karşılanmasını sağlar. Çocuğunuzla birlikte, sınıfta ne kadarının bilinmesini istediğine karar verebilirsiniz. Özel günler, anneler ya da '
                                       'babalar günü gibi etkinlikler öncesinde öğretmenle konuşmak da zor anların önceden düşünülmesine yardım eder.</p>\n'
                                       '<h2>Ebeveyn de yas tutarken</h2>\n'
                                       '<p>Çocuğunuzun yasına eşlik ederken siz de aynı kaybın yasını tutuyor olabilirsiniz. Çocuğun yanında hiç ağlamamaya çalışmak gerekmez; duygularınızı sade bir '
                                       'dille paylaşmak, çocuğa üzülmenin doğal olduğunu gösterir. Ancak kendi yasınız sizi çok zorluyorsa yakınlarınızdan ya da bir uzmandan destek almak, çocuğunuza '
                                       'eşlik edebilmeniz için de önemlidir. Çocukla yapılan görüşmelerde yaşa göre oyun, çizim ve hikâyeler kullanılır; ebeveynlerle ayrıca görüşülerek evde nasıl '
                                       'destek olunabileceği birlikte planlanır.</p>\n'
                                       '<h2>Yasın ilk haftalarında ev düzeni</h2>\n'
                                       '<p>Kayıptan sonra evdeki düzen çoğu zaman altüst olur: Misafirler gelir, ritüeller yapılır, yetişkinler yorgun ve üzgündür. Çocuklar için bu belirsizlik '
                                       'dönemi ayrıca zorlayıcıdır. Yatma saati, okul ve yemek düzeni gibi gündelik rutinleri olabildiğince korumak, çocuğa hayatın devam ettiği ve güvende olduğu '
                                       'duygusunu verir.</p>\n'
                                       '<p>Çocuğa kaybedilen kişiyle ilgili bir anı kutusu hazırlamak, fotoğraflara birlikte bakmak, bir resim çizmek ya da mektup yazmak duygularını ifade etmesine '
                                       'yardım edebilir. Çocuğun oyunlarında ölümü ya da cenazeyi canlandırması da yası anlamlandırmanın bir yolu olabilir; bu oyunlar genellikle endişe verici '
                                       'değildir.</p>',
                               'sss': [('Çocuğum kaybı hiç sormuyor, bu iyi bir işaret mi?',
                                        'Her zaman değil. Bazı çocuklar ailenin üzülmesini istemediği için sormaz. Ara ara konuyu nazikçe açmak ve sorularına açık olduğunuzu göstermek, duygularını '
                                        'paylaşmasını kolaylaştırır.'),
                                       ('Evcil hayvanımız öldü, yeni bir hayvan almalı mıyız?',
                                        'Hemen yeni bir hayvan almak, kaybın yasını yaşamayı zorlaştırabilir. Önce çocuğun üzüntüsünü konuşmasına zaman tanımak, kararı daha sonra birlikte vermek '
                                        'genellikle daha uygundur.'),
                                       ('Öğretmene kaybı anlatmalı mıyım?',
                                        'Evet, kısaca bilgi vermeniz önerilir. Böylece öğretmen çocuktaki dikkat dağınıklığı ya da duygusal değişiklikleri anlayışla karşılayabilir.')],
                               'tarih': '2026-10-27'},
 '/eryaman-psikolog/': {'html': "<h2>Eryaman'dan bireysel görüşmeler</h2>\n"
                                '<p>Kaygı, stres, uyku sorunları, kendine güvensizlik ya da yaşamda bir dönüm noktasında hissedilen belirsizlik, bireysel görüşmelerde sık konuşulan konulardır. '
                                'Düzenli görüşmeler, neyin sizi zorladığını anlamanıza ve günlük hayatta işe yarayacak yeni yollar denemenize alan açar. Bireysel görüşmeler yüz yüze ya da online '
                                'yapılabilir; ilk görüşmede size uygun düzeni birlikte belirleriz.</p>\n'
                                '<p>Görüşmelere başlamak için yaşadığınız zorluğun "yeterince büyük" olmasını beklemeniz gerekmez.</p>\n'
                                "<h2>Eryaman'dan düzenli görüşme planlamak</h2>\n"
                                "<p>Eryaman'dan gelen danışanlarımız için en önemli konu, görüşmeleri günlük düzene uygun ve sürdürülebilir biçimde planlamak. Terapide düzenlilik önemli olduğu için "
                                'ilk görüşmede size en uygun gün ve saati birlikte belirliyoruz. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında yapılır ve ofisimizde ücretsiz otopark '
                                'bulunur.</p>\n'
                                '<ul>\n'
                                '<li><b>Yüz yüze ve online görüşmeyi birleştirin:</b> Bazı haftalar yüz yüze, bazı haftalar online görüşmek mümkündür.</li>\n'
                                '<li><b>Cumartesi saatlerini değerlendirin:</b> Hafta içi yoğun çalışanlar için cumartesi randevuları uygun olabilir.</li>\n'
                                '<li><b>Ön görüşmeyi online yapın:</b> Özellikle ebeveyn ön görüşmeleri online planlanabilir.</li>\n'
                                '</ul>\n'
                                "<h2>Eryaman'da yaşayan ailelerin sık sorduğu konular</h2>\n"
                                "<p>Eryaman'dan başvuran aileler çoğu zaman ergenlik dönemindeki iletişim sorunları, okul motivasyonu, ekran kullanımı ve kardeş ilişkileri hakkında destek arıyor. "
                                'Çiftler ise günlük sorumluluklar arasında birbirine zaman ayıramamaktan ve ilişkinin yalnızca yapılacak işler etrafında dönmesinden söz ediyor. Bu konular, küçük '
                                'adımlarla ve düzenli görüşmelerle ele alınabilir.</p>\n'
                                '<h2>Ergenle konuşmak zorlaştığında</h2>\n'
                                '<p>Ergenlik döneminde gencin kendi odasına çekilmesi, az konuşması ya da aileyle tartışması sık görülür. Bu davranışlar her zaman bir sorun işareti değildir; ancak '
                                'uzun süren içe kapanma, okuldan uzaklaşma ya da belirgin duygu değişiklikleri destek almayı gerektirebilir. Ergen görüşmelerinde önce ebeveynle bir ön görüşme '
                                'yapılır, ardından gençle ayrı görüşmeler planlanır.</p>\n'
                                '<h2>Çiftler için ortak zaman</h2>\n'
                                '<p>Aynı evde yaşamak, birlikte vakit geçirmekle aynı şey değildir. Çift görüşmelerinde iletişimi yeniden kurmak, ihtiyaçları suçlamadan ifade etmek ve ilişkiye küçük '
                                'ama düzenli zaman ayırmak üzerine çalışılır. Çift görüşmeleri genellikle yüz yüze yapılır; ihtiyaca göre online görüşme de planlanabilir.</p>',
                        'sss': [("Eryaman'dan haftalık görüşmeye gelmek zor olursa ne yapabilirim?",
                                 'Görüşmelerin bir kısmını online yapabilir ya da sıklığı ihtiyacınıza göre birlikte düzenleyebiliriz.'),
                                ('Ergen çocuğum gelmek istemiyor, önce ben gelebilir miyim?', 'Evet. Ebeveynle yapılan ön görüşme, gence nasıl yaklaşılacağını planlamak için iyi bir başlangıçtır.'),
                                ('Çift görüşmeleri online yapılabilir mi?', 'Genellikle yüz yüze tercih edilir; ancak gerektiğinde çift görüşmeleri online da planlanabilir.')],
                        'tarih': '2026-10-27'},
 '/evlilik-oncesi-danismanlik/': {'html': '<h2>Evlilik öncesi görüşmelere ne zaman başlamalı?</h2>\n'
                                          '<p>Evlilik öncesi görüşmeler için ideal zaman, düğün telaşının en yoğun olduğu son haftalar değil, karar verilmiş ama hazırlıkların henüz başladığı '
                                          'dönemdir. Bu dönemde çiftler hem birbirlerinin beklentilerini konuşmaya daha açık olur hem de konuşulanları günlük hayatta denemek için zaman bulur. '
                                          'Nişanlılık süreci kısa olan çiftler için de birkaç görüşme, önemli konuları masaya yatırmak için değerli bir fırsattır.</p>\n'
                                          "<p>Görüşmeler Konutkent'teki ofisimizde, iki tarafın birlikte katılımıyla yapılır. Çalışan çiftlerin ortak zamanı sınırlı olduğu için akşam ve cumartesi "
                                          'saatleri sık tercih edilir; görüşmeler pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabilir. Taraflardan biri farklı bir şehirdeyse görüşmeler '
                                          'online da yapılabilir.</p>\n'
                                          '<h2>Görüşmelere hazırlanırken konuşabileceğiniz sorular</h2>\n'
                                          '<p>Görüşmeler için bir hazırlık zorunlu değildir; yine de çiftlerin kendi aralarında düşünmeye başlayabileceği bazı sorular süreci verimli kılar:</p>\n'
                                          '<ul>\n'
                                          '<li>Evlilikten en çok ne bekliyorum, en çok neyden endişe ediyorum?</li>\n'
                                          '<li>Kendi ailemde tartışmalar nasıl çözülürdü ve ben bundan neyi sürdürmek, neyi değiştirmek isterim?</li>\n'
                                          '<li>Ev işleri, para ve aileyle geçirilecek zaman konusunda kafamdaki tablo ne?</li>\n'
                                          '<li>Kırıldığımda ne yaparım: susar mıyım, uzaklaşır mıyım, hemen konuşmak mı isterim?</li>\n'
                                          '</ul>\n'
                                          '<p>Bu soruların doğru ya da yanlış cevabı yoktur. Amaç, farklılıkları erken fark edip onları konuşulabilir hâle getirmektir.</p>\n'
                                          '<h2>Görüşmeler sırasında ve sonrasında</h2>\n'
                                          '<p>Evlilik öncesi görüşmeler bir "uygunluk sınavı" değildir; kimse not almaz, kimse haklı ya da haksız ilan edilmez. Görüşmelerde zaman zaman çiftlerin hiç '
                                          'konuşmadığı bir konunun açıldığını görürüz; bu bir sorun işareti değil, tam da bu görüşmelerin amacıdır. Görüşmeler sona erdikten sonra evliliğin ilk '
                                          'yılında bir ya da birkaç izleme görüşmesi yapmak da isteyen çiftler için bir seçenektir.</p>\n'
                                          '<h2>Farklı durumlardaki çiftler için</h2>\n'
                                          '<p>Evlilik öncesi görüşmelere başvuran çiftlerin durumu birbirinden farklıdır. Uzun süredir birlikte olup evlilik kararı alan çiftler, kısa bir '
                                          'tanışıklığın ardından evlenmeye karar verenler, ikinci evliliğini yapacak ve çocuklu bir aile kuracak olanlar, farklı şehir ya da kültürlerden gelen '
                                          'çiftler ve evlilikten sonra başka bir şehre ya da ülkeye taşınacak olanlar bunlardan bazılarıdır. Her durumda konuşulması gereken başlıklar farklılaşır; '
                                          'görüşmeler çiftin kendi gündemine göre şekillenir.</p>\n'
                                          '<p>Evlilik öncesi danışmanlıkta ele alınan konular ve sürecin ayrıntıları için rehber: <a '
                                          'href="https://www.psikologrojinnazik.com/evlilik-oncesi-danismanlik/">Evlilik öncesi danışmanlık hakkında bilmeniz gerekenler</a></p>',
                                  'sss': [('Evlilik öncesi danışmanlık kaç görüşme sürer?', 'Görüşme sayısı çiftin ihtiyacına göre değişir ve ilk görüşmede birlikte planlanır.'),
                                          ('Aramızda ciddi bir sorun yok, yine de gelmemiz anlamlı mı?',
                                           'Evet. Bu görüşmeler sorun çözmekten çok, beklentileri ve iletişim biçimlerini evlilik başlamadan konuşmak için yapılır.'),
                                          ('Partnerim başka bir şehirde yaşıyor, nasıl görüşebiliriz?',
                                           'Görüşmeler online da yapılabilir; mümkün olduğunda bazı görüşmelerin yüz yüze yapılması da planlanabilir.')],
                                  'tarih': '2026-10-27'},
 '/evlilikte-iletisim-sorunlari/': {'html': '<h2>Tartışmalar neden hep aynı yere çıkar?</h2>\n'
                                            '<p>Birçok çift farklı konularda tartıştıklarını düşünür; oysa yakından bakıldığında tartışmaların çoğu aynı döngüyü izler. Biri eleştirir ya da ısrar '
                                            'eder, diğeri savunmaya geçer ya da susup uzaklaşır. Israr eden taraf duyulmadığını hissettikçe sesini yükseltir, uzaklaşan taraf baskı hissettikçe daha '
                                            'da geri çekilir. Bu döngüyü fark etmek, "kim haklı?" sorusundan "bu döngüden nasıl çıkarız?" sorusuna geçmenin ilk adımıdır.</p>\n'
                                            '<h2>Gündelik hayatta iletişimi yıpratan küçük alışkanlıklar</h2>\n'
                                            '<ul>\n'
                                            '<li><b>Konuşurken telefona bakmak:</b> Karşı tarafa önemsenmediği mesajını verir.</li>\n'
                                            '<li><b>"Sen hep…", "Sen hiç…" cümleleri:</b> Tek bir davranışı kişiliğe genelleştirir ve savunmayı artırır.</li>\n'
                                            '<li><b>Konuyu geçmişe taşımak:</b> Bugünkü sorun yerine eski kırgınlıkların hesabı yapılır.</li>\n'
                                            '<li><b>Yalnızca sorun olduğunda konuşmak:</b> İletişim zamanla yalnızca görev ve şikâyetten ibaret hâle gelir.</li>\n'
                                            '<li><b>Mesajla tartışmak:</b> Ses tonu ve yüz ifadesi olmadan yanlış anlaşılma kolaylaşır.</li>\n'
                                            '</ul>\n'
                                            '<h2>Zor bir konuyu açmadan önce</h2>\n'
                                            '<p>Önemli konular yorgunken, aç karnına, çocukların yanında ya da kapıdan çıkarken açıldığında tartışmaya dönüşme olasılığı artar. Eşinize "Seninle bir '
                                            'konuyu konuşmak istiyorum, ne zaman uygun olur?" diye sormak, konuşmaya hazırlıklı başlamanızı sağlar. Konuşmaya bir eleştiriyle değil, kendi duygunuz ve '
                                            'ihtiyacınızla başlamak, karşı tarafın dinleme olasılığını artırır. Tartışma kontrolden çıkıyorsa bir mola vermek ve belirli bir süre sonra konuşmaya geri '
                                            'dönmek üzere anlaşmak işe yarayabilir.</p>\n'
                                            '<h2>Çift görüşmeleri nasıl ilerler?</h2>\n'
                                            '<p>İlk görüşmede ilişkinin geçmişi, sorunların ne zaman başladığı ve iki tarafın beklentileri dinlenir. Gerekirse eşlerle ayrı ayrı da görüşülür. Sonraki '
                                            'görüşmelerde tartışma döngüleri birlikte incelenir; seans aralarında denenecek küçük iletişim adımları belirlenir. Amaç bir tarafı haklı çıkarmak değil, '
                                            'iki kişinin birbirini daha iyi anlayabileceği bir dil bulmaktır. İlişkide fiziksel ya da yoğun psikolojik şiddet varsa önce güvenliğin sağlanması '
                                            "gerekir; acil durumlarda 112'yi arayın.</p>\n"
                                            '<h2>Onarım girişimlerini fark etmek</h2>\n'
                                            '<p>Her çift tartışır; ilişkiyi koruyan şey tartışmanın hiç olmaması değil, tartışmadan sonra yeniden yakınlaşabilmektir. Bir şaka yapmak, "haklısın, '
                                            'burada abarttım" demek, bir çay koymak ya da elini tutmak gibi küçük hareketler onarım girişimleridir. Bu girişimler fark edilip karşılık bulduğunda '
                                            'kırgınlık birikmez.</p>\n'
                                            '<p>Uzun süredir zorlanan çiftlerde bu girişimler çoğu zaman görülmez ya da reddedilir. Eşinizin barışmak için yaptığı küçük adımları fark etmeye çalışmak '
                                            've onlara karşılık vermek, ilişkideki havayı zamanla değiştirebilir. Günlük hayatta birbirinize küçük ilgiler göstermek ve olumlu şeyleri de dile '
                                            'getirmek, zor konuşmaların daha güvenli bir zeminde yapılmasını sağlar.</p>',
                                    'sss': [('Her tartışmada eşim susup odadan çıkıyor, ne yapmalıyım?',
                                             'Geri çekilme çoğu zaman yoğun duygudan korunma yoludur. Sakin bir zamanda bunu konuşup tartışma sırasında mola vermek ve belirli bir süre sonra geri '
                                             'dönmek üzere anlaşmak, iki taraf için de daha güvenli bir yol olabilir.'),
                                            ('Çocuklarımızın önünde tartışmak onlara zarar verir mi?',
                                             'Sakin biçimde yürütülen ve çözümle biten fikir ayrılıkları çocuklar için öğretici bile olabilir. Ancak bağırma, aşağılama ve çözümsüz kalan sık '
                                             'tartışmalar çocukları olumsuz etkiler; bu konuşmaları çocukların olmadığı bir zamana bırakmak daha uygundur.'),
                                            ('Çift görüşmeleri ne sıklıkla yapılır?',
                                             'Görüşme sıklığı çiftin ihtiyacına göre belirlenir; başlangıçta genellikle düzenli aralıklarla planlanır ve ilerleyen süreçte aralar açılabilir.')],
                                    'tarih': '2026-10-27'},
 '/ilk-terapi-seansi-rehberi/': {'html': '<h2>İlk seanstan önceki gece: kaygı normaldir</h2>\n'
                                         '<p>İlk görüşmeden önce gergin hissetmek, ne anlatacağınızı düşünüp durmak ya da randevuyu iptal etmeyi aklınızdan geçirmek çok yaygındır. Bu kaygı, yeni ve '
                                         'kişisel bir adım attığınızı gösterir. Görüşmeye "doğru" bir şekilde hazırlanmanız gerekmez; gergin olduğunuzu söylemek de görüşmenin doğal bir başlangıcı '
                                         'olabilir.</p>\n'
                                         '<h2>İlk seansta sorabileceğiniz sorular</h2>\n'
                                         '<p>İlk görüşme yalnızca psikoloğun sizi tanıdığı bir görüşme değildir; sizin de psikoloğunuzu ve çalışma biçimini tanımanız için bir fırsattır. Şu soruları '
                                         'sormakta özgürsünüz:</p>\n'
                                         '<ul>\n'
                                         '<li>Benim yaşadıklarıma benzer konularda nasıl çalışıyorsunuz?</li>\n'
                                         '<li>Görüşmeler hangi sıklıkta ve ne kadar süre planlanır?</li>\n'
                                         '<li>Seans aralarında yapmam gereken çalışmalar olacak mı?</li>\n'
                                         '<li>Gizlilik hangi durumlarda sınırlanabilir?</li>\n'
                                         '<li>İlerlemeyi birlikte nasıl değerlendireceğiz?</li>\n'
                                         '</ul>\n'
                                         '<h2>İlk seanstan sonra neler hissedebilirsiniz?</h2>\n'
                                         '<p>İlk görüşmenin ardından bazı kişiler hafiflemiş hisseder, bazıları ise yorgun ya da duygusal olarak hassas hissedebilir. Uzun süredir konuşulmayan '
                                         'konuların dile getirilmesi bu tepkileri doğurabilir. Görüşmeden sonra kendinize biraz zaman ayırmak, hemen yoğun bir işe geçmemek iyi gelebilir. Aklınıza '
                                         'takılan düşünceleri not alıp bir sonraki görüşmeye taşıyabilirsiniz.</p>\n'
                                         '<h2>Psikoloğunuzla uyum sağlayamadığınızı hissederseniz</h2>\n'
                                         '<p>Terapötik ilişkide kendinizi rahat hissetmeniz önemlidir. İlk birkaç görüşmeden sonra anlaşılmadığınızı ya da rahat edemediğinizi düşünüyorsanız bunu '
                                         'psikoloğunuzla açıkça konuşabilirsiniz. Bu konuşma çoğu zaman süreci güçlendirir; gerekirse farklı bir yaklaşım ya da farklı bir uzman birlikte '
                                         'değerlendirilebilir. Bunu dile getirmek kaba ya da saygısız bir davranış değildir.</p>\n'
                                         '<h2>Terapiden ne beklememelisiniz?</h2>\n'
                                         '<p>Terapiyle ilgili bazı beklentiler sürecin yanlış anlaşılmasına yol açabilir. Psikolog size ne yapmanız gerektiğini söyleyen biri değildir; birlikte '
                                         'düşünür, farklı bakış açıları sunar ve kararlarınızı kendiniz vermenize yardım eder. Değişim genellikle tek bir görüşmede değil, zaman içinde ve küçük '
                                         'adımlarla gerçekleşir.</p>\n'
                                         '<p>Bazı görüşmelerden sonra kendinizi daha iyi, bazılarından sonra ise daha düşünceli ya da duygusal hissedebilirsiniz. Bu dalgalanma sürecin olağan bir '
                                         'parçasıdır. Görüşmelerden neler beklediğinizi ve süreçte nasıl hissettiğinizi psikoloğunuzla düzenli olarak konuşmak, çalışmanın size uygun ilerlemesini '
                                         'sağlar.</p>',
                                 'sss': [('İlk seansta ağlarsam ne olur?',
                                          'Ağlamak görüşmelerde çok sık yaşanan, tamamen doğal bir tepkidir. Kendinizi tutmak zorunda değilsiniz; bu duyguların güvenli bir ortamda ifade edilmesi '
                                          'görüşmenin bir parçasıdır.'),
                                         ('İlk seanstan sonra devam edip etmeyeceğime nasıl karar veririm?',
                                          'Kendinizi ne kadar rahat hissettiğinize, anlaşıldığınızı düşünüp düşünmediğinize ve önerilen yol haritasının size uygun gelip gelmediğine bakabilirsiniz. '
                                          'Bu kararı vermek için birkaç görüşmeye ihtiyaç duymanız da olağandır.')],
                                 'tarih': '2026-10-27'},
 '/incek-psikolog/': {'html': "<h2>İncek'te taşınma sonrası uyum</h2>\n"
                              "<p>İncek'e yeni taşınan aileler için ilk aylar hem heyecan hem de yorgunluk getirebilir. Çocuklar için yeni okul, yeni arkadaşlar ve değişen ev düzeni; yetişkinler "
                              'için ise uzayan yollar, yeni komşuluk ilişkileri ve değişen günlük rutinler uyum gerektirir. Bu süreçte çocuklarda geçici uyku sorunları, huzursuzluk ya da içe kapanma '
                              'görülebilir. Çoğu zaman bu tepkiler zamanla azalır; uzun sürdüğünde ise aileyle birlikte değerlendirmek faydalı olur.</p>\n'
                              "<h2>İncek'te çocuklu aileler için destek</h2>\n"
                              "<p>İncek'te yaşayan ailelerin önemli bir kısmı küçük ve okul çağındaki çocuklarla birlikte yaşıyor. Bu dönemde ebeveynlerin en sık sorduğu sorular; çocuğun okula ve "
                              'yeni çevreye uyumu, uyku ve yeme düzeni, öfke nöbetleri, kardeş kıskançlığı ve ekran kullanımı etrafında şekilleniyor. Çocuğun davranışlarındaki değişim, çoğu zaman '
                              'yaşamındaki bir değişimin dışa yansıması olabilir.</p>\n'
                              '<p>Çocukla çalışırken aile her zaman sürecin bir parçasıdır. Ebeveynlerle yapılan görüşmeler, evde neyin işe yaradığını ve neyin zorlandığını birlikte anlamaya yardım '
                              'eder.</p>\n'
                              '<h2>Uzak hissettiğinizde düzenli görüşmeyi sürdürmek</h2>\n'
                              "<p>İncek'ten gelen aileler için görüşme günlerini okul ve kurs programlarıyla uyumlu planlamak önemli. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında "
                              'yapılabildiği için hafta içi okul dönüşü ya da cumartesi saatleri sık tercih ediliyor. Ofisimizde ücretsiz otopark bulunur.</p>\n'
                              '<ul>\n'
                              '<li><b>Çocuk görüşmeleri:</b> Çocuğun yüz yüze gelmesi genellikle daha uygundur; oyun ve etkinlik temelli çalışmalar ofiste yapılır.</li>\n'
                              '<li><b>Ebeveyn görüşmeleri:</b> Ebeveynlerle yapılan bazı görüşmeler, gelmenin zor olduğu haftalarda online planlanabilir.</li>\n'
                              '</ul>\n'
                              '<h2>Çocuğunuzu ilk görüşmeye hazırlamak</h2>\n'
                              '<p>Çocuğa psikoloğa gideceğini anlatırken sakin ve dürüst olmak önemlidir. "Duyguları anlamaya yardım eden biriyle tanışacağız, oyun oynayıp konuşacağız" gibi basit '
                              'bir açıklama çoğu çocuk için yeterlidir. Görüşmeyi ceza ya da tehdit gibi sunmaktan kaçınmak, çocuğun sürece güvenle başlamasını kolaylaştırır.</p>\n'
                              '<h2>Ebeveynlerin kendi ihtiyaçları</h2>\n'
                              '<p>Çocukla ilgili bir zorluk yaşanırken ebeveynler de yorulabilir, kendini suçlayabilir ya da eşiyle farklı düşünebilir. Bu duyguları konuşmak, çocuğa yaklaşımı da '
                              'olumlu etkiler. Ebeveynler kendileri için de bireysel ya da çift görüşmesi alabilir.</p>',
                      'sss': [('Çocuğum görüşmeye gelmek istemezse ne yapmalıyım?',
                               'Önce ebeveyn olarak siz gelebilirsiniz. Çocuğun çekincelerini nasıl ele alacağınızı birlikte konuşur, ilk görüşmeyi ona uygun biçimde planlarız.'),
                              ("İncek'ten gelen aileler için ebeveyn görüşmeleri online olabilir mi?",
                               'Evet. Ebeveynlerle yapılan bazı görüşmeler online planlanabilir; çocukla yapılan görüşmelerin ise genellikle yüz yüze olması tercih edilir.'),
                              ('Kardeşler birlikte görüşmeye gelebilir mi?',
                               'İhtiyaca göre değişir. İlk görüşmede ailenin durumu değerlendirilir ve görüşmelerin kimlerle yapılacağı birlikte belirlenir.')],
                      'tarih': '2026-10-27'},
 '/is-stresi-ve-tukenmislik/': {'html': '<h2>İşten sonra kapanmayan zihin</h2>\n'
                                        '<p>Mesai bittiği hâlde e-postaları kontrol etmek, akşam yemeğinde yarınki toplantıyı düşünmek ya da gece uyanıp yapılacakları sıralamak, iş stresinin günlük '
                                        'hayata ne kadar sızdığını gösterir. Zihnin işten ayrılamaması, dinlenme zamanını da dinlendirici olmaktan çıkarır.</p>\n'
                                        '<ul>\n'
                                        '<li><b>Bir kapanış ritüeli belirleyin:</b> Günün sonunda ertesi günün listesini yazıp bilgisayarı kapatmak, zihne "bugün bitti" mesajı verir.</li>\n'
                                        '<li><b>Bildirimleri sınırlayın:</b> Mümkünse akşam saatlerinde iş uygulamalarının bildirimlerini kapatın.</li>\n'
                                        '<li><b>Geçiş zamanı yaratın:</b> Eve dönüş yolunu kısa bir yürüyüş ya da müzikle bir ara alan olarak kullanabilirsiniz.</li>\n'
                                        '</ul>\n'
                                        '<h2>Evden çalışanlarda tükenmişlik</h2>\n'
                                        '<p>Evden ya da karma düzende çalışmak esneklik sağlasa da işle ev arasındaki sınırları bulanıklaştırabilir. Mutfak masasının hem ofis hem yemek alanı olması, '
                                        'mesai saatlerinin uzaması ve iş arkadaşlarıyla yüz yüze temasın azalması yalnızlık ve yorgunluğu artırabilir. Ayrı bir çalışma köşesi belirlemek, sabah ve '
                                        'akşam için sabit başlangıç ve bitiş saatleri koymak ve gün içinde kısa aralar vermek bu yükü hafifletebilir.</p>\n'
                                        '<h2>İş yerinde sınır koymak</h2>\n'
                                        '<p>Tükenmişlik çoğu zaman yalnızca iş yükünden değil, sürekli "evet" demekten de beslenir. Her talebi kabul etmek kısa vadede sorunsuz görünse de zamanla '
                                        'öfke, yorgunluk ve değersizlik duygusuna dönüşebilir. Önceliklerinizi yöneticinizle netleştirmek, bir işi kabul etmeden önce zaman istemek ve gerçekçi teslim '
                                        'tarihleri önermek sınır koymanın pratik yollarıdır. Sınır koymakta zorlanıyorsanız bunun arkasındaki düşünceleri, örneğin "hayır dersem değersiz görülürüm" '
                                        'inancını görüşmelerde ele almak mümkündür.</p>\n'
                                        '<h2>Ailenizin fark edebileceği işaretler</h2>\n'
                                        '<p>Tükenmişlik bazen kişinin kendisinden önce yakınları tarafından fark edilir. Sürekli gergin olmak, eskiden keyif alınan şeylere ilgisizlik, küçük '
                                        'konularda öfkelenmek, hafta sonlarını yalnızca uyuyarak geçirmek ya da aileyle vakit geçirirken aklın hep işte olması dikkat edilmesi gereken işaretlerdir. '
                                        'Bu değişiklikleri suçlamadan, merak ederek konuşmak destek almanın ilk adımı olabilir.</p>\n'
                                        '<h2>Dinlenmeyi yeniden öğrenmek</h2>\n'
                                        '<p>Uzun süre yoğun tempoda çalışan kişiler için dinlenmek bile bir görev gibi gelebilir. Boş zamanda telefonda gezinmek ya da diziden diziye geçmek kısa '
                                        'süreli bir uyuşma sağlar ama gerçek bir dinlenme hissi vermeyebilir. Dinlendirici etkinlikler kişiden kişiye değişir: Doğada yürümek, bir arkadaşla sohbet '
                                        'etmek, el işiyle uğraşmak ya da müzik dinlemek gibi.</p>\n'
                                        '<p>Hafta içinde kısa da olsa iş dışı bir etkinliğe düzenli zaman ayırmak, hafta sonunu yalnızca yorgunluğu atmakla geçirmekten daha koruyucudur. Uyku '
                                        'düzenini korumak, düzenli yemek yemek ve gün içinde hareket etmek de stres karşısındaki dayanıklılığı destekler.</p>',
                                'sss': [('Tatile çıkmak tükenmişliği geçirir mi?',
                                         'Tatil kısa süreli bir rahatlama sağlayabilir; ancak tükenmişliğe yol açan iş düzeni değişmezse yorgunluk genellikle kısa sürede geri döner. Kalıcı '
                                         'değişiklik için gündelik alışkanlıkları ve sınırları da gözden geçirmek gerekir.'),
                                        ('İşimi değiştirmeden tükenmişlikle baş edebilir miyim?',
                                         'Birçok kişi iş düzeninde, sınırlarında ve dinlenme alışkanlıklarında yaptığı değişikliklerle rahatlayabilir. Görüşmelerde hangi değişikliklerin sizin '
                                         'durumunuzda mümkün olduğu birlikte değerlendirilir.')],
                                'tarih': '2026-10-27'},
 '/kaygi-sorunlari/': {'html': '<h2>Kaygı için başvurduğunuzda ilk görüşmeler</h2>\n'
                               '<p>Kaygı nedeniyle başvuran kişiler çoğu zaman ilk görüşmeye gelirken bile gergin hissettiklerini anlatır: "Ne soracaklar, doğru anlatabilecek miyim?" İlk görüşmede '
                               'sizden düzenli bir anlatım beklenmez. Kaygının hangi durumlarda arttığı, bedeninizde nasıl hissedildiği, uykunuzu, işinizi ve ilişkilerinizi nasıl etkilediği birlikte '
                               'konuşulur. Daha önce bir hekimle görüştüyseniz ve bedensel nedenler değerlendirildiyse bunu paylaşmanız da yardımcı olur.</p>\n'
                               "<p>Görüşmeler Konutkent'teki ofisimizde yüz yüze ya da online yapılabilir. Kalabalık ya da yeni ortamlarda zorlananlar için online başlamak bir seçenek olabilir; "
                               'ancak kaçınmanın kaygıyı beslediği durumlarda zamanla yüz yüze görüşmeye geçmek de çalışmanın parçası hâline gelebilir.</p>\n'
                               '<h2>Görüşmeler arasında neler yapılır?</h2>\n'
                               '<p>Kaygı üzerine yapılan çalışmalarda görüşme odasında konuşulanlar kadar, görüşmeler arasında yapılanlar da önemlidir. Bu çalışmalar kişiye göre belirlenir ve küçük '
                               'adımlarla ilerler:</p>\n'
                               '<ul>\n'
                               '<li><b>Gözlem:</b> Kaygının arttığı anları, o an aklınızdan geçenleri ve ne yaptığınızı kısaca not etmek.</li>\n'
                               '<li><b>Nefes ve beden:</b> Görüşmede öğrenilen sakinleşme yöntemlerini, kaygı yokken de düzenli olarak denemek.</li>\n'
                               '<li><b>Küçük yüzleşmeler:</b> Kaçındığınız bir duruma, sizin onayınız ve belirlediğiniz hızda, adım adım yaklaşmak.</li>\n'
                               '</ul>\n'
                               '<p>Bu adımlar zorlayıcı gelirse bunu görüşmede söylemeniz yeterlidir; plan sizin hızınıza göre yeniden düzenlenir.</p>\n'
                               '<h2>Kaygıyla birlikte yaşayan aile üyeleri</h2>\n'
                               '<p>Kaygı yaşayan kişinin yakınları da çoğu zaman nasıl yardım edeceğini bilemez. Sürekli güvence vermek ya da kişinin yerine işleri halletmek kısa vadede rahatlatsa '
                               'da kaygıyı sürdürebilir. Gerektiğinde, danışanın onayıyla, bir yakının da katıldığı bir görüşme planlanarak evde nasıl destek olunabileceği konuşulabilir.</p>\n'
                               '<h2>Kaygı günlük hayatta nasıl görünür?</h2>\n'
                               '<p>Kaygı her zaman yoğun bir korku olarak yaşanmaz. Çoğu zaman "ya olursa" diye başlayan bitmeyen düşünceler, sabaha karşı uyanıp bir türlü uyuyamamak, mesajlara '
                               'hemen cevap gelmediğinde huzursuzlanmak, toplantı öncesi midede düğüm, sürekli kontrol etme ihtiyacı ya da bazı yerlerden ve durumlardan sessizce kaçınmak şeklinde '
                               'görünür. Bu belirtiler zamanla kişinin yaşam alanını daraltabilir. Kaygının sizi ne kadar kısıtladığını fark etmek, destek almanın zamanının gelip gelmediğini '
                               'anlamanın önemli bir işaretidir.</p>\n'
                               '<p>Kendi kaygı düzeyinizi gözden geçirmek isterseniz kısa bir ön değerlendirme aracı olan <a href="/kaygi-testi/">kaygı testini</a> kullanabilirsiniz; sonuç tanı '
                               'değildir.</p>\n'
                               '<p>Kaygı ve anksiyete bozukluklarının belirtileri, nedenleri ve kullanılan yaklaşımlar için ayrıntılı rehber: <a '
                               'href="https://www.psikologrojinnazik.com/anksiyete-bozukluklari/">Anksiyete bozuklukları nedir?</a></p>',
                       'sss': [('Kaygım yüzünden dışarı çıkmakta zorlanıyorum; online başlayabilir miyim?',
                                'Evet. Online başlamak bir seçenektir; süreç ilerledikçe yüz yüze görüşmeye geçmek de birlikte planlanabilir.'),
                               ('Kaygı için görüşmeler ne sıklıkla yapılır?', 'Genellikle başlangıçta haftada bir yapılır; ilerleme oldukça aralık açılabilir.'),
                               ('Ailem de görüşmeye katılabilir mi?', 'Sizin onayınızla, yakınlarınızın evde nasıl destek olabileceğini konuşmak için ortak bir görüşme planlanabilir.')],
                       'tarih': '2026-10-27'},
 '/kaygili-kacingan-ve-fobik-kisilikler/': {'html': '<h2>Kaygılı ve kaçıngan örüntüler günlük hayatta nasıl görünür?</h2>\n'
                                                    '<p>Kaygılı ve kaçıngan örüntüler çoğu zaman "dikkatli", "çekingen" ya da "utangaç" olmak gibi masum görünen özelliklerin arkasına gizlenir. Bazı '
                                                    'örnekler:</p>\n'
                                                    '<ul>\n'
                                                    '<li>Yeni bir ortama girmeden önce günlerce olası senaryoları düşünmek.</li>\n'
                                                    '<li>Eleştirilme korkusuyla toplantılarda fikrini söylememek.</li>\n'
                                                    '<li>Başarısız olma ihtimali olan fırsatlardan, istense bile uzak durmak.</li>\n'
                                                    '<li>Telefon açmak, randevu almak gibi küçük adımları sürekli ertelemek.</li>\n'
                                                    '</ul>\n'
                                                    '<p>Kaçınmak kısa vadede rahatlatır; ancak zamanla yaşam alanını daraltır ve kişinin kendine güvenini daha da azaltır.</p>\n'
                                                    '<h2>İlişkilerde ve iş hayatında</h2>\n'
                                                    '<p>Kaygılı ve kaçıngan örüntüler ilişkilerde, yakınlık isteğiyle reddedilme korkusu arasında sıkışmak şeklinde yaşanabilir. Kişi bağ kurmak ister '
                                                    'ama yanlış anlaşılmaktan ya da yetersiz görülmekten korktuğu için geri çekilir. İş hayatında ise yetenekli olduğu hâlde kendini geri planda '
                                                    'tutmak, terfi ya da yeni sorumluluk fırsatlarını ertelemek sık görülür. Bu tablo, çevredekiler tarafından ilgisizlik olarak yanlış '
                                                    'okunabilir.</p>\n'
                                                    '<h2>Sık karşılaşılan yanılgılar</h2>\n'
                                                    '<ul>\n'
                                                    '<li><b>"Biraz cesaretle geçer."</b> Kaçınma çoğu zaman irade eksikliği değil, yıllar içinde öğrenilmiş bir korunma biçimidir.</li>\n'
                                                    '<li><b>"Utangaçlık bir kişilik özelliğidir, üzerinde çalışılmaz."</b> Kendinizi kısıtlanmış hissediyorsanız bu kalıplar üzerinde çalışmak '
                                                    'mümkündür.</li>\n'
                                                    '<li><b>"Zorlarsam korkum geçer."</b> Kendini zorla maruz bırakmak bazen kaygıyı artırabilir; değişim genellikle küçük, güvenli ve kademeli '
                                                    'adımlarla gelir.</li>\n'
                                                    '</ul>\n'
                                                    '<h2>Kaygıyla birlikte yaşarken günlük hayatta neler yapılabilir?</h2>\n'
                                                    '<p>Kaygılı ve kaçıngan örüntülerle baş ederken küçük ama düzenli adımlar büyük farklar yaratabilir:</p>\n'
                                                    '<ul>\n'
                                                    '<li><b>Kaçındığınız durumları sıralayın:</b> En az zorlayandan en çok zorlayana doğru bir liste yapmak, nereden başlayacağınızı görmenizi '
                                                    'sağlar.</li>\n'
                                                    '<li><b>Küçük deneyler yapın:</b> Toplantıda tek bir cümle söylemek ya da ertelediğiniz bir aramayı yapmak gibi küçük adımlar, korkunun gerçekte '
                                                    'ne kadar büyük olduğunu sınamanıza yardım eder.</li>\n'
                                                    '<li><b>Kendinizle konuşma biçiminize dikkat edin:</b> "Yine beceremeyeceğim" yerine "Deneyip göreceğim" demek, adım atmayı '
                                                    'kolaylaştırabilir.</li>\n'
                                                    '<li><b>Bedensel rahatlama yollarını keşfedin:</b> Yavaş nefes, kısa yürüyüşler ve düzenli uyku, kaygının şiddetini azaltmaya yardımcı '
                                                    'olabilir.</li>\n'
                                                    '</ul>\n'
                                                    '<h2>Görüşmelerde nasıl çalışılır?</h2>\n'
                                                    '<p>Bu örüntüler üzerine yapılan çalışmalarda önce kaygının nerede ve nasıl ortaya çıktığı birlikte anlaşılır. Terapist ile güvenli bir ilişki '
                                                    'kurmak, sürecin en önemli parçalarından biridir; çünkü kaygılı kişiler için yargılanmadan dinlenmek başlı başına yeni bir deneyimdir. Ardından, '
                                                    'kişinin kendi hızına uygun küçük adımlarla kaçınılan durumlara yaklaşması desteklenir. Süreç genellikle uzun soluklu ve iş birliğine '
                                                    'dayalıdır.</p>',
                                            'sss': [('Utangaçlık ile kaçıngan örüntüler arasındaki fark nedir?',
                                                     'Utangaçlık birçok kişide görülen ve hayatı belirgin biçimde kısıtlamayan bir özelliktir. Kaçınma, kişinin istediği ilişki, iş ya da fırsatlardan '
                                                     'sürekli uzak durmasına yol açıyorsa bir uzmanla konuşmak faydalı olabilir.'),
                                                    ('Kaygılı biri için ilk görüşmeye gelmek zor olabilir mi?',
                                                     'Evet, bu çok anlaşılır bir durumdur. İsterseniz ilk adımı yazılı mesajla atabilir, ilk görüşmede yaşadığınız tedirginliği de konuşabilirsiniz; '
                                                     'bu da sürecin bir parçasıdır.'),
                                                    ('Online görüşme kaçınmayı artırır mı?',
                                                     'Online görüşme, başlangıçta ilk adımı kolaylaştırabilir. Sürecin ilerleyen aşamalarında hangi görüşme biçiminin size daha uygun olduğu birlikte '
                                                     'değerlendirilir.')],
                                            'tarih': '2026-10-27'},
 '/kisilik-kavrami/': {'html': '<h2>Kişilik günlük hayatta nasıl görünür?</h2>\n'
                               '<p>Kişilik soyut bir kavram gibi görünse de her gün verdiğimiz küçük tepkilerde kendini gösterir. Eleştiri aldığınızda hemen savunmaya mı geçiyorsunuz, yoksa günlerce '
                               'kendinizi mi suçluyorsunuz? Bir plan bozulduğunda kolayca uyum sağlayabiliyor musunuz, yoksa bu sizi uzun süre huzursuz mu ediyor? Yakınlaşmak mı sizi rahatlatıyor, '
                               'yoksa bir mesafe korumak mı? Bu soruların cevapları, kişiliğinizin hangi yönlerinin öne çıktığına dair ipuçları verir.</p>\n'
                               '<p>Bu özelliklerin hiçbiri tek başına "iyi" ya da "kötü" değildir. Titiz olmak işte başarı getirirken ilişkide kontrolcü bir tutuma dönüşebilir; uyumlu olmak '
                               'sevilmeyi kolaylaştırırken kendi ihtiyaçlarınızı ertelemenize yol açabilir. Önemli olan, bir özelliğin farklı durumlarda ne kadar esnek kullanılabildiğidir.</p>\n'
                               '<h2>Kişilik ve ilişkiler</h2>\n'
                               '<p>Kişiliğimiz en çok yakın ilişkilerde belirginleşir. Benzer tartışmaların farklı partnerlerle tekrar etmesi, iş yerinde hep aynı tür insanlarla zorlanmak ya da '
                               'arkadaşlıklarda sürekli "veren taraf" olmak, çoğu zaman şans değil, tekrar eden bir örüntünün işaretidir. Bu örüntüyü fark etmek, kendinizi suçlamak için değil, '
                               'nelerin değişebileceğini görmek için önemlidir.</p>\n'
                               '<h2>Kişilik hakkında yaygın yanılgılar</h2>\n'
                               '<ul>\n'
                               '<li><b>"Ben böyleyim, değişmem."</b> Kişilik görece istikrarlıdır ama değişmez değildir; yaşam deneyimleri, ilişkiler ve terapi süreci zamanla belirgin farklar '
                               'yaratabilir.</li>\n'
                               '<li><b>"Kişilik özellikleri bir etikettir."</b> Kişilik, bir insanı tek kelimeyle tanımlamaya yaramaz; aynı kişi farklı ortamlarda çok farklı yönlerini '
                               'gösterebilir.</li>\n'
                               '<li><b>"Kişilik konuşmak için ciddi bir sorun yaşamak gerekir."</b> Kendini daha iyi tanımak isteyen herkes, kişilik örüntüleri üzerine düşünmekten fayda '
                               'görebilir.</li>\n'
                               '</ul>\n'
                               '<h2>Kendinizi gözlemlemek için birkaç soru</h2>\n'
                               '<p>Kişiliğinizi daha iyi tanımak için kendinize zaman zaman şu soruları sorabilirsiniz. Cevapların doğrusu ya da yanlışı yoktur; amaç yalnızca fark etmektir.</p>\n'
                               '<ul>\n'
                               '<li>Hangi durumlarda kendimi en rahat, hangilerinde en tedirgin hissediyorum?</li>\n'
                               '<li>Zorlandığımda ilk tepkim ne oluyor: geri çekilmek mi, kontrolü ele almak mı, başkasından destek istemek mi?</li>\n'
                               '<li>İlişkilerimde en çok neye ihtiyaç duyuyorum ve bunu dile getirebiliyor muyum?</li>\n'
                               '<li>Hayatımın farklı dönemlerinde tekrar eden bir tema var mı?</li>\n'
                               '</ul>\n'
                               '<p>Bu soruları bir deftere yazmak ya da güvendiğiniz biriyle konuşmak, kendinize daha şefkatli ve meraklı bir gözle bakmanızı kolaylaştırabilir.</p>\n'
                               '<h2>Terapide kişilik üzerine nasıl çalışılır?</h2>\n'
                               '<p>Kişilik üzerine yapılan çalışmalar genellikle uzun soluklu ve iş birliğine dayalıdır. Görüşmelerde yalnızca bugünkü şikâyet değil, bu şikâyetin hayatınızın farklı '
                               'alanlarında nasıl tekrar ettiği de ele alınır. Terapist ile kurduğunuz ilişki de bu sürecin bir parçasıdır; çünkü başka ilişkilerde yaşadığınız duygular çoğu zaman bu '
                               'ilişkide de canlanır ve güvenli bir ortamda konuşulabilir hâle gelir. Hedef, kim olduğunuzu değiştirmek değil; sizi zorlayan kalıpları daha esnek hâle '
                               'getirmektir.</p>',
                       'sss': [('Kişilik ile mizaç arasındaki fark nedir?',
                                'Mizaç, büyük ölçüde doğuştan gelen tepki verme eğilimlerini anlatır. Kişilik ise bu temelin üzerine yaşam deneyimleri, ilişkiler ve kültürle şekillenen daha geniş '
                                'bir yapıdır.'),
                               ('Kendi kişilik örüntülerimi nasıl fark edebilirim?',
                                'Hayatınızın farklı dönemlerinde ve farklı ilişkilerinde tekrar eden duygu ve tepkilere bakmak iyi bir başlangıçtır. Güvendiğiniz kişilerin gözlemleri ve bir uzmanla '
                                'yapılan görüşmeler de bu farkındalığı derinleştirebilir.'),
                               ('Kişilik üzerine çalışmak ne kadar sürer?',
                                'Bu, kişiye ve ele alınan konulara göre değişir. Kişilik örüntüleri yıllar içinde oluştuğu için bu çalışmalar genellikle kısa süreli yaklaşımlara göre daha uzun '
                                'soluklu olur.')],
                       'tarih': '2026-10-27'},
 '/kisilik-orgutlenmesi-duzeyi-bozuklugun-siddeti/': {'html': '<h2>Bir yelpaze olarak kişilik</h2>\n'
                                                              '<p>Kişilik örgütlenmesi düzeylerini, insanları kutulara ayıran kategoriler gibi değil, bir yelpaze gibi düşünmek daha doğrudur. Herkes '
                                                              'zor dönemlerde bu yelpazenin farklı noktalarında hissedebilir; yoğun stres, kayıp ya da tükenmişlik, en esnek insanı bile daha katı '
                                                              'tepkilere itebilir. Önemli olan, kişinin genel olarak hangi esneklikle işlediği ve zorlandığında kendini ne kadar '
                                                              'toparlayabildiğidir.</p>\n'
                                                              '<h2>Bu kavramlar ne işe yarar?</h2>\n'
                                                              '<p>Kişilik örgütlenmesi kavramı, bir uzmanın size etiket koyması için değil, sizinle nasıl çalışmanın daha uygun olacağını anlaması '
                                                              'için kullanılır. Örneğin bazı kişiler için görüşmelerde iç çatışmaları keşfetmek ön plandayken, bazıları için önce duyguları '
                                                              'düzenlemeye ve günlük hayatta güvenli bir zemin kurmaya odaklanmak daha uygundur. Bu ayrım, görüşmelerin hızını, sıklığını ve yöntemini '
                                                              'belirlemeye yardımcı olur.</p>\n'
                                                              '<h2>Günlük hayatta hangi alanlara bakılır?</h2>\n'
                                                              '<ul>\n'
                                                              '<li><b>Kimlik duygusu:</b> Kendinizi farklı ortamlarda tutarlı bir kişi olarak hissedebiliyor musunuz?</li>\n'
                                                              '<li><b>İlişkiler:</b> Yakın ilişkiler görece dengeli mi, yoksa sık sık ani kopuşlar ve yoğun çatışmalar mı yaşanıyor?</li>\n'
                                                              '<li><b>Duygu düzenleme:</b> Yoğun duygular bir süre sonra yatışabiliyor mu?</li>\n'
                                                              '<li><b>Gerçeklik değerlendirmesi:</b> Stres altında olayları değerlendirme biçiminiz ne kadar korunuyor?</li>\n'
                                                              '</ul>\n'
                                                              '<p>Bu alanlar, kendinizi yargılamak için bir kontrol listesi değildir; yalnızca uzmanların kişiliği bütüncül olarak anlamak için '
                                                              'baktığı başlıklardır.</p>\n'
                                                              '<h2>Yakınlarınız için bilmeniz gerekenler</h2>\n'
                                                              '<p>Kişilik örüntüleri yalnızca kişinin kendisini değil, çevresindekileri de etkiler. Bir yakınınızın tepkilerini anlamakta '
                                                              'zorlanıyorsanız, davranışın arkasında çoğu zaman bir korku ya da ihtiyaç olduğunu hatırlamak işinizi kolaylaştırabilir. Bu, her '
                                                              'davranışı kabul etmeniz gerektiği anlamına gelmez; kendi sınırlarınızı korumak da en az onu anlamak kadar önemlidir. Yakınlarının '
                                                              'durumu nedeniyle yıpranan kişilerin de kendileri için destek alması faydalı olabilir.</p>\n'
                                                              '<p>Bir yakınınıza destek almasını önermek istiyorsanız, bunu suçlamadan ve onun yaşadığı zorluğa duyduğunuz ilgiyi vurgulayarak yapmak '
                                                              'daha kolay kabul edilmesini sağlar.</p>\n'
                                                              '<h2>Destek almak için doğru zaman</h2>\n'
                                                              '<p>İlişkilerinizde sık tekrar eden kırılmalar, kendinizle ilgili yoğun ve değişken duygular ya da uzun süredir devam eden bir boşluk '
                                                              'hissi yaşıyorsanız bir uzmanla konuşmak iyi gelebilir. Kişilik üzerine yapılan çalışmalar genellikle uzun soluklu ve iş birliğine '
                                                              "dayalıdır. Kendinize zarar verme düşünceleri varsa beklemeden <b>112</b>'yi arayın.</p>",
                                                      'sss': [('Bu sayfayı okuyarak kendi örgütlenme düzeyimi belirleyebilir miyim?',
                                                               'Hayır. Bu kavramlar ancak bir uzmanın kapsamlı görüşmeleriyle ve bütüncül biçimde değerlendirilebilir. Sayfadaki bilgiler yalnızca '
                                                               'genel bir fikir vermek içindir.'),
                                                              ('Kişilik örgütlenmesi zamanla değişebilir mi?',
                                                               'Evet. Kişilik görece istikrarlı olsa da destekleyici ilişkiler, yaşam deneyimleri ve uzun soluklu terapi çalışmaları zamanla daha '
                                                               'esnek bir işleyişe katkı sağlayabilir.')],
                                                      'tarih': '2026-10-27'},
 '/kisilik-oruntuleri-ve-dinamik-yaklasim/': {'html': '<h2>Tekrar eden örüntülere günlük hayattan örnekler</h2>\n'
                                                      '<p>Kişilik örüntüleri çoğu zaman kendimizi "yine aynı şey oldu" derken bulduğumuz anlarda fark edilir. Bazı örnekler:</p>\n'
                                                      '<ul>\n'
                                                      '<li>Bir ilişkide yakınlık arttıkça uzaklaşma ihtiyacı duymak, uzaklaştıkça da yalnız kalma korkusu yaşamak.</li>\n'
                                                      '<li>İş yerinde hayır diyememek, sonra biriken yük nedeniyle öfkelenip kendinizi suçlamak.</li>\n'
                                                      '<li>Küçük bir eleştiriyi tüm değerinizin sorgulanması gibi yaşamak.</li>\n'
                                                      '<li>Her şeyin kontrol altında olmadığında yoğun bir huzursuzluk hissetmek.</li>\n'
                                                      '</ul>\n'
                                                      '<p>Bu kalıplar bir zamanlar, özellikle çocuklukta, kişiyi korumak için oluşmuş olabilir. Ancak bugünkü yaşamda aynı işlevi görmediklerinde '
                                                      'yorucu hâle gelirler.</p>\n'
                                                      '<h2>Dinamik yaklaşım bu örüntülere nasıl bakar?</h2>\n'
                                                      '<p>Dinamik yaklaşımda amaç, davranışı yalnızca durdurmak değil, onun arkasındaki ihtiyacı ve duyguyu anlamaktır. Örneğin sürekli başkalarını '
                                                      'memnun etmeye çalışan biri için görüşmelerde, bu davranışın hangi korkuyu yatıştırdığı ve ilk nerede öğrenildiği birlikte araştırılır. Anlamak, '
                                                      'değişimi kolaylaştırır; çünkü kişi artık neden öyle davrandığını bildiği için yeni seçenekler deneyebilir.</p>\n'
                                                      '<h2>Terapi sürecinde neler olur?</h2>\n'
                                                      '<p>Bu tür çalışmalar genellikle haftalık ve düzenli görüşmelerle, uzun soluklu bir süreç olarak ilerler. Görüşmelerde aklınıza gelenleri '
                                                      'olabildiğince serbestçe konuşmanız, rüyalarınız, anılarınız ve terapistle aranızdaki ilişkide hissettikleriniz de sürecin malzemesidir. '
                                                      'İlerleme her zaman düz bir çizgi izlemez; bazı dönemlerde eski duyguların yeniden canlanması, sürecin doğal bir parçasıdır. Görüşmelerin yönü '
                                                      've hedefleri belirli aralıklarla birlikte gözden geçirilir.</p>\n'
                                                      '<h2>Örüntüleri fark etmek için küçük adımlar</h2>\n'
                                                      '<p>Değişim çoğu zaman fark etmekle başlar. Günlük hayatta şu adımlar yardımcı olabilir:</p>\n'
                                                      '<ul>\n'
                                                      '<li><b>Tetikleyiciyi not edin:</b> Sizi en çok sarsan durumları ve o anda ne hissettiğinizi kısaca yazın.</li>\n'
                                                      '<li><b>Bedeninizi dinleyin:</b> Göğüste sıkışma, yüzde ısınma gibi bedensel işaretler, duygunun yükseldiğini erken haber verir.</li>\n'
                                                      '<li><b>Tepkiyi biraz erteleyin:</b> Hemen cevap vermek yerine birkaç dakika beklemek, otomatik tepkinin yerine bir seçim yapmanızı '
                                                      'kolaylaştırır.</li>\n'
                                                      '<li><b>Kendinize karşı yumuşak olun:</b> Bir örüntüyü fark ettiğinizde kendinizi suçlamak yerine, onun bir zamanlar neden gerekli olduğunu '
                                                      'düşünmeye çalışın.</li>\n'
                                                      '</ul>\n'
                                                      '<h2>Ne zaman destek almayı düşünmelisiniz?</h2>\n'
                                                      '<p>Aynı tür zorlukların farklı ilişkilerde ve dönemlerde tekrar ettiğini fark ediyorsanız, duygularınız sık sık kontrolünüz dışında '
                                                      'yükseliyorsa ya da "kendimi tanıyamıyorum" hissi uzun süredir sürüyorsa bir uzmanla görüşmek faydalı olabilir. Kendinize ya da bir başkasına '
                                                      "zarar verme düşünceleriniz varsa beklemeden <b>112</b>'yi arayın.</p>",
                                              'sss': [('Geçmişi konuşmak gerçekten bugünü değiştirir mi?',
                                                       'Geçmişi konuşmanın amacı geçmişte kalmak değil, bugünkü tepkilerin nereden geldiğini anlamaktır. Bu anlayış, benzer durumlarda farklı seçimler '
                                                       'yapabilmenin zeminini hazırlar.'),
                                                      ('Dinamik terapi ile diğer yaklaşımlar arasındaki fark nedir?',
                                                       'Dinamik yaklaşım, belirtilerin arkasındaki duygu, ihtiyaç ve ilişki örüntülerine odaklanır. Bazı yaklaşımlar ise daha yapılandırılmış ve '
                                                       'belirli becerilere yönelik çalışır; hangi yaklaşımın uygun olduğu ilk görüşmelerde birlikte değerlendirilir.')],
                                              'tarih': '2026-10-27'},
 '/konutkent-psikolog/': {'html': "<h2>Konutkent'te yaşam değişiklikleri ve yas</h2>\n"
                                  '<p>Taşınma, iş değişikliği, emeklilik, çocukların evden ayrılması ya da bir yakının kaybı gibi büyük değişimler, en güçlü hissettiğimiz anlarda bile bizi '
                                  'sarsabilir. Bu dönemlerde yaşanan hüzün, kaygı ya da boşluk hissi çoğu zaman doğal tepkilerdir. Yine de bu duygular uzun sürdüğünde ya da günlük hayatı '
                                  'zorlaştırdığında, onları konuşabileceğiniz bir alan bulmak iyi gelebilir. Görüşmelerde yaşadığınız değişimin sizin için anlamını ve yeni duruma nasıl uyum '
                                  'sağlayabileceğinizi birlikte ele alırız.</p>\n'
                                  '<p>Yas sürecinde herkesin hızı farklıdır; görüşmelerde sizden belirli bir sürede "toparlanmanız" beklenmez.</p>\n'
                                  "<h2>Konutkent'te yaşayanlar için yakın bir destek alanı</h2>\n"
                                  "<p>Ofisimiz Konutkent'te, Dumlupınar Bulvarı No:399 adresinde bulunuyor. Konutkent'te yaşayan danışanlarımız için bu yakınlık, terapiyi günlük hayatın bir parçası "
                                  'hâline getirmeyi kolaylaştırıyor. Uzun yol ya da park yeri derdi olmadan, haftanın bir saatini kendinize ayırmak çoğu zaman sanıldığından daha kolay oluyor.</p>\n'
                                  "<p>Konutkent'ten başvuranlar arasında hem yetişkinler hem çiftler hem de çocuklu aileler var. Kaygı, stres, ilişkide iletişim sorunları, yas ve yaşam "
                                  'değişiklikleri sık konuşulan konular arasında.</p>\n'
                                  '<h2>Terapiye ilk kez başlayacaklar için</h2>\n'
                                  '<p>İlk kez bir psikologla görüşecek kişiler çoğu zaman ne anlatacağını bilememekten, yanlış anlaşılmaktan ya da yargılanmaktan çekiniyor. Bu çekinceler çok doğal. '
                                  'İlk görüşmede sizden hazırlıklı bir anlatım beklenmez; sorular yol gösterir ve konuşmak istemediğiniz bir konuyu anlatmak zorunda kalmazsınız.</p>\n'
                                  '<ul>\n'
                                  '<li><b>Kısa notlar alın:</b> Sizi en çok zorlayan anları ya da sorularınızı yazmak işe yarayabilir.</li>\n'
                                  '<li><b>Beklentinizi paylaşın:</b> Görüşmelerden ne umduğunuzu söylemek, süreci birlikte planlamayı kolaylaştırır.</li>\n'
                                  '<li><b>Sorularınızı sorun:</b> Görüşmelerin nasıl ilerleyeceğini, gizliliği ya da sıklığı sormaktan çekinmeyin.</li>\n'
                                  '</ul>\n'
                                  '<h2>Yürüme mesafesindeyken mahremiyet</h2>\n'
                                  '<p>Yaşadığınız yere çok yakın bir ofiste görüşmek, bazı kişilerde komşularla karşılaşma kaygısı yaratabilir. Görüşmeleriniz meslek etiği gereği gizli tutulur ve '
                                  'randevular bekleme süresi kısa olacak şekilde planlanır. Bu konudaki tercihlerinizi randevu alırken paylaşabilirsiniz; isterseniz bazı görüşmeleri online da '
                                  'yapabilirsiniz.</p>\n'
                                  '<h2>Görüşmeler arasında neler yapabilirsiniz?</h2>\n'
                                  '<p>Terapi yalnızca görüşme saatinde ilerlemez. Görüşmede fark ettiklerinizi hafta içinde gözlemlemek, küçük değişiklikleri denemek ve bir sonraki görüşmede bunları '
                                  'konuşmak süreci derinleştirir. Bu çalışmalar size dayatılmaz; hızınıza ve ihtiyacınıza göre birlikte belirlenir.</p>',
                          'sss': [('İlk görüşmede her şeyi anlatmak zorunda mıyım?',
                                   'Hayır. Ne kadarını, ne zaman paylaşacağınıza siz karar verirsiniz; güven duygusu görüşmeler ilerledikçe gelişir.'),
                                  ("Konutkent'ten online görüşmeyi de seçebilir miyim?", 'Evet. Yakında olsanız da dilediğiniz görüşmeleri online yapabilirsiniz.'),
                                  ('Görüşmeler kaç dakika sürer?', 'Bireysel görüşmeler yaklaşık 50 dakika sürer; çift ve aile görüşmelerinin süresi randevu alırken netleştirilir.')],
                          'tarih': '2026-10-27'},
 '/online-terapi/': {'html': '<h2>Online görüşme adım adım nasıl ilerler?</h2>\n'
                             '<ul>\n'
                             "<li><b>Randevu:</b> Telefonla ya da WhatsApp'tan ulaşarak online görüşmek istediğinizi belirtirsiniz. Size uygun uzman, gün ve saat birlikte belirlenir.</li>\n"
                             '<li><b>Bağlantı:</b> Görüşme saatinden önce size güvenli bir görüntülü görüşme bağlantısı iletilir. Ek bir program kurmanız çoğu zaman gerekmez.</li>\n'
                             '<li><b>Görüşme:</b> Görüşme, yüz yüze görüşmelerde olduğu gibi, belirlenen sürede ve aynı etik ilkelerle yapılır.</li>\n'
                             '<li><b>Süreklilik:</b> Görüşmeler genellikle haftalık ya da iki haftalık düzenle sürdürülür; gerektiğinde yüz yüze görüşmelerle birleştirilebilir.</li>\n'
                             '</ul>\n'
                             '<h2>Online görüşmeye nasıl hazırlanmalısınız?</h2>\n'
                             '<p>Online görüşmenin verimli olması için birkaç küçük hazırlık yeterlidir:</p>\n'
                             '<ul>\n'
                             '<li><b>Mahremiyet:</b> Kimsenin sizi duymayacağı, kapısı kapalı bir oda seçin. Evde başkaları varsa kulaklık kullanmak rahat konuşmanızı kolaylaştırır.</li>\n'
                             '<li><b>Bağlantı:</b> Görüşmeden birkaç dakika önce internet bağlantınızı, kameranızı ve mikrofonunuzu kontrol edin.</li>\n'
                             '<li><b>Bölünmeler:</b> Telefon bildirimlerini kapatın; görüşme sırasında başka işlerle ilgilenmemeye çalışın.</li>\n'
                             '<li><b>Geçiş zamanı:</b> Görüşmeden hemen önce ve sonra birkaç dakikalık boş zaman bırakmak, duygularınızı toparlamanıza yardım eder.</li>\n'
                             '</ul>\n'
                             '<h2>Online mı, yüz yüze mi?</h2>\n'
                             '<p>Her iki görüşme biçiminin de kendine göre avantajları vardır. Online görüşme; ulaşım süresini ortadan kaldırır, yoğun çalışma saatlerine uyum sağlar ve şehir dışında '
                             'olduğunuz dönemlerde görüşmelerin aksamamasını sağlar. Yüz yüze görüşme ise bazı kişilerin kendini daha rahat ifade etmesine yardımcı olur; küçük çocuklarla yapılan '
                             'oyun temelli çalışmalarda ve bazı çift ya da aile görüşmelerinde çoğu zaman tercih edilir.</p>\n'
                             "<p>Hangi biçimin size uygun olduğu ilk görüşmede birlikte değerlendirilebilir. Konutkent'teki ofisimizde yüz yüze başlayıp gerektiğinde online devam etmek ya da tam "
                             'tersi de mümkündür.</p>\n'
                             '<h2>Online görüşmenin uygun olmadığı durumlar</h2>\n'
                             '<p>Online görüşme birçok kişi için iyi bir seçenek olsa da her durum için uygun değildir. Kendinize ya da bir başkasına zarar verme düşüncelerinin yoğun olduğu, acil '
                             "müdahale gerektiren durumlarda online görüşme yeterli değildir; böyle bir durumda hemen 112'yi arayın. Ayrıca evde kendinizi güvende hissetmiyor ya da rahat "
                             'konuşabileceğiniz bir ortam bulamıyorsanız yüz yüze görüşme daha uygun olabilir.</p>\n'
                             '<h2>Online görüşmede gizlilik nasıl korunur?</h2>\n'
                             '<p>Online görüşmeler, yüz yüze görüşmelerle aynı meslek etiği ve gizlilik ilkeleriyle yürütülür. Görüşmeler kaydedilmez ve görüşme bağlantısı yalnızca size iletilir. '
                             'Gizliliğin sizin tarafınızda da korunması için ortak kullanılan bilgisayarlar yerine kendi cihazınızı kullanmanızı, görüşmeden sonra tarayıcı sekmesini kapatmanızı ve '
                             'güvenli bir internet bağlantısı tercih etmenizi öneririz. Kafe gibi kalabalık ortamlardan görüşmeye katılmak, rahat konuşmanızı zorlaştırabilir.</p><p>Yurt dışında '
                             'çocuk büyüten aileler için: <a href="/yurt-disi-online-ebeveyn-danismanligi/">Türkçe online ebeveyn danışmanlığı</a>.</p>',
                     'sss': [('Online görüşmeler kaydediliyor mu?',
                              'Hayır. Görüşmeler kaydedilmez ve yüz yüze görüşmelerle aynı gizlilik ilkelerine tabidir. Sizin de görüşmeyi kaydetmemenizi rica ederiz.'),
                             ('Bağlantı koparsa ne olur?',
                              'Bağlantı koparsa aynı bağlantı üzerinden yeniden bağlanmayı deneriz; sorun sürerse telefonla devam etmek ya da kalan süreyi birlikte planlamak mümkündür.'),
                             ('Çift görüşmesini online yapabilir miyiz?',
                              'Evet. Partnerlerin aynı ekrandan katılması ya da farklı yerlerden bağlanması mümkündür. Uygun yöntem ilk görüşmede birlikte belirlenir.')],
                     'tarih': '2026-10-27'},
 '/randevu-sik-sorulan-sorular/': {'html': '<h2>Randevu süreci adım adım</h2>\n'
                                           '<ul>\n'
                                           "<li><b>1. Bize ulaşın:</b> Telefonla arayabilir ya da WhatsApp'tan kısa bir mesaj bırakabilirsiniz. Destek almak istediğiniz konuyu birkaç cümleyle "
                                           'paylaşmanız yeterlidir.</li>\n'
                                           '<li><b>2. Uzman ve saat:</b> Başvuru nedeninize ve tercihlerinize göre size uygun olabilecek uzman ve görüşme saatleri hakkında bilgi verilir.</li>\n'
                                           '<li><b>3. Yüz yüze ya da online:</b> Görüşmeyi ofisimizde yüz yüze ya da online olarak yapabilirsiniz.</li>\n'
                                           '<li><b>4. İlk görüşme:</b> İlk görüşme bir tanışma ve değerlendirme görüşmesidir; ihtiyaçlarınız birlikte ele alınır ve sonrasında nasıl bir yol '
                                           'izleneceği konuşulur.</li>\n'
                                           '</ul>\n'
                                           '<h2>Ofisimize ulaşım</h2>\n'
                                           "<p>Ofisimiz Konutkent'te, Dumlupınar Bulvarı No:399 adresindedir. Binada ücretsiz otopark bulunur. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 saatleri "
                                           'arasında randevu ile yapılır. İlk görüşmenize birkaç dakika erken gelmeniz, görüşmeye daha sakin başlamanıza yardımcı olur.</p>\n'
                                           '<h2>Online görüşme tercih ediyorsanız</h2>\n'
                                           '<p>Ofise gelmeniz zor olduğunda, şehir dışında olduğunuzda ya da kendi ortamınızda görüşmeyi tercih ettiğinizde online görüşme bir seçenektir. Online '
                                           'görüşme için sessiz ve kimsenin sizi duymayacağı bir oda seçmeniz, internet bağlantınızı önceden kontrol etmeniz ve mümkünse kulaklık kullanmanız '
                                           'önerilir.</p>\n'
                                           '<h2>Çocuğunuz ya da ergeniniz için randevu alırken</h2>\n'
                                           '<p>Çocuk ve ergenlerle yapılan çalışmalarda genellikle önce ebeveynlerle bir ön görüşme planlanır. Bu görüşmede çocuğunuzun gelişimi, sizi kaygılandıran '
                                           'konular ve ailedeki son değişiklikler konuşulur. Ardından çocuğunuzla görüşmeler planlanır. Çocuğunuza psikoloğa gideceğini nasıl anlatacağınız konusunda '
                                           'da bilgi alabilirsiniz.</p>\n'
                                           '<h2>Çift ya da aile görüşmesi için randevu</h2>\n'
                                           '<p>Çift görüşmelerinde genellikle iki tarafın birlikte katıldığı bir ilk görüşme planlanır; ilerleyen süreçte gerekirse bireysel görüşmeler de '
                                           'yapılabilir. Eşinizin henüz görüşmeye gelmeye hazır olmadığı durumlarda tek başınıza başlamak da mümkündür. Aile görüşmelerinde hangi aile üyelerinin '
                                           'katılacağı başvuru nedeninize göre birlikte belirlenir.</p>\n'
                                           '<p>Randevu sırasında başvuru nedeninizi kısaca paylaşmanız, sizin için uygun görüşme türünü ve uzmanı belirlemeyi kolaylaştırır. Ayrıntıları paylaşmak '
                                           'istemiyorsanız bunları ilk görüşmede doğrudan psikoloğunuzla konuşabilirsiniz.</p>',
                                   'sss': [('Online ve yüz yüze görüşme arasında geçiş yapabilir miyim?',
                                            'Evet. Görüşmelere yüz yüze başlayıp gerektiğinde online devam edebilir ya da tersini tercih edebilirsiniz; bu konuyu uzmanınızla birlikte '
                                            'planlayabilirsiniz.'),
                                           ('Ofisinizde otopark var mı?', "Evet. Konutkent'te Dumlupınar Bulvarı No:399 adresindeki binamızda ücretsiz otopark bulunur."),
                                           ('Çocuğum için randevu alırken ilk görüşmeye kim gelmeli?',
                                            'Çocuk ve ergen çalışmalarında genellikle önce ebeveynlerle bir ön görüşme yapılır; ardından çocukla görüşmeler planlanır.')],
                                   'tarih': '2026-10-27'},
 '/travma-sonrasi-stres-belirtileri/': {'html': '<h2>Yakınınız zor bir olay yaşadıysa</h2>\n'
                                                '<p>Travmatik bir olay yaşayan birine destek olmak isteyip ne söyleyeceğinizi bilemeyebilirsiniz. Bu dönemde en önemli şey, yanında olduğunuzu '
                                                'hissettirmek ve onu konuşmaya zorlamamaktır.</p>\n'
                                                '<ul>\n'
                                                '<li><b>Dinleyin, sorgulamayın:</b> Anlatmak isterse ayrıntı sormadan, yargılamadan dinleyin.</li>\n'
                                                '<li><b>Pratik destek sunun:</b> Yemek, alışveriş ya da çocuklara bakmak gibi gündelik işlerde yardım etmek çoğu zaman sözlerden daha '
                                                'rahatlatıcıdır.</li>\n'
                                                '<li><b>"Artık unut" demekten kaçının:</b> İyi niyetli olsa da kişinin yaşadıklarını küçümsenmiş hissetmesine yol açabilir.</li>\n'
                                                '<li><b>Kendi sınırlarınızı da gözetin:</b> Destek olurken siz de yorulabilirsiniz; kendinize de alan açın.</li>\n'
                                                '</ul>\n'
                                                '<h2>Tetikleyiciler: geçmiş neden birden şimdiye taşınır?</h2>\n'
                                                '<p>Bir koku, ses, mekân ya da yıl dönümü, travmatik olayı hatırlatarak yoğun duyguları yeniden canlandırabilir. Örneğin bir trafik kazası geçiren '
                                                'kişi fren sesinde irkilebilir ya da olayın yaşandığı yola yaklaşırken kalbi hızla çarpabilir. Tetikleyicileri fark etmek, bu tepkilerin "şu anda bir '
                                                'tehlike var" anlamına gelmediğini hatırlamayı kolaylaştırır. Ayaklarınızı yere basarak, çevrenizdeki beş nesneyi sayarak ya da yavaş nefes alarak '
                                                'kendinizi şimdiki ana döndürmek bu anlarda işe yarayabilir.</p>\n'
                                                '<h2>Kaçınmanın tuzağı</h2>\n'
                                                '<p>Olayı hatırlatan yerlerden, kişilerden ya da konuşmalardan uzak durmak ilk başta rahatlatıcı gelir. Ancak kaçınılan alan zamanla genişlerse hayat '
                                                'daralır: Araba kullanmamak, belirli bir semte gitmemek, haber izleyememek gibi. Kaçınma uzun sürdüğünde destek almak, adım adım ve güvenli bir '
                                                'şekilde günlük hayata dönmeye yardımcı olur.</p>\n'
                                                '<h2>Görüşmelerde neler yapılır?</h2>\n'
                                                '<p>Görüşmelerde önce güven ve denge sağlanır; kişi olayı anlatmaya zorlanmaz. Bedensel tepkileri tanımak, sakinleşme becerileri kazanmak ve günlük '
                                                'düzeni yeniden kurmak ilk adımlardır. Kişi hazır hissettiğinde yaşadıkları kendi hızında ele alınır. Kendinize ya da başkasına zarar verme '
                                                "düşünceleri varsa ya da acil bir tehlike söz konusuysa hemen 112'yi arayın.</p>\n"
                                                '<h2>Toplu kayıp ve afet dönemlerinde</h2>\n'
                                                '<p>Deprem, sel ya da büyük kazalar gibi toplumu derinden etkileyen olaylardan sonra yalnızca doğrudan etkilenenler değil, haberleri sürekli '
                                                'izleyenler de stres tepkileri yaşayabilir. Uyku sorunları, huzursuzluk, sürekli haberleri kontrol etme isteği ve suçluluk duygusu bu dönemlerde sık '
                                                'görülür.</p>\n'
                                                '<p>Haber takibini günün belirli saatleriyle sınırlamak, özellikle çocukların yanında sarsıcı görüntülerin izlenmesinden kaçınmak ve mümkünse yardım '
                                                'çalışmalarına küçük de olsa katkı sunmak çaresizlik hissini azaltabilir. Gündelik rutinleri korumak ve sevdiklerinizle konuşmak da bu dönemlerde en '
                                                'önemli destek kaynaklarındandır.</p>',
                                        'sss': [('Olayı anlatmak istemiyorum, yine de görüşmeye gelebilir miyim?',
                                                 'Evet. Görüşmelerde olayı anlatmanız için zorlanmazsınız; önce güven ve denge üzerine çalışılır. Ne zaman ve ne kadar anlatacağınıza siz karar '
                                                 'verirsiniz.'),
                                                ('Olaydan aylar sonra tepkilerin başlaması mümkün mü?',
                                                 'Evet. Bazı kişilerde belirtiler olaydan bir süre sonra, örneğin yıl dönümünde ya da benzer bir durumla karşılaşınca ortaya çıkabilir. Bu durumda da '
                                                 'destek almak faydalıdır.'),
                                                ('Yakınıma travma yaşadıktan sonra nasıl destek olabilirim?',
                                                 'Yanında olduğunuzu hissettirmek, yargılamadan dinlemek ve gündelik işlerde pratik yardım sunmak çoğu zaman en değerli destektir. Belirtiler uzun '
                                                 'sürüyorsa profesyonel destek almaya nazikçe teşvik edebilirsiniz.')],
                                        'tarih': '2026-10-27'},
 '/umitkoy-psikolog/': {'html': "<h2>Ümitköy'de iş stresi ve tükenmişlik</h2>\n"
                                '<p>Uzun çalışma saatleri, sürekli ulaşılabilir olma beklentisi ve yoğun sorumluluklar, zamanla tükenmişlik hissine dönüşebilir. Sabahları işe gitmekte zorlanmak, '
                                'eskiden keyif aldığınız şeylerden uzaklaşmak, sık sık hastalanmak ya da ailenize karşı sabırsızlaşmak bu sürecin işaretleri arasında olabilir. Görüşmelerde iş '
                                'yükünüzü, sınır koyma biçiminizi ve dinlenmenin önündeki engelleri birlikte ele alırız. Amaç işinizi bırakmak değil, kendinizi kaybetmeden çalışabileceğiniz bir '
                                'denge kurmaktır.</p>\n'
                                "<h2>Ümitköy'de yoğun tempoda kendinize zaman ayırmak</h2>\n"
                                "<p>Ümitköy'de yaşayan pek çok kişi gününün büyük kısmını işte, yolda ya da çocukların okul ve kurs programları arasında geçiriyor. Bu tempoda kendi duygularına "
                                'ayıracak zaman kalmadığını söyleyenler çok. Sürekli yorgun hissetmek, küçük şeylere hemen sinirlenmek, uykuya geçememek ya da hafta sonu bile dinlenememek, çoğu '
                                'zaman bu birikimin işaretleri olabilir.</p>\n'
                                '<p>Psikolojik destek almak için her şeyin yolunda gitmemesini beklemeniz gerekmez. Haftada bir saatlik bir görüşme, neyin sizi bu kadar yorduğunu fark etmek ve '
                                'önceliklerinizi yeniden düzenlemek için bir alan açabilir.</p>\n'
                                '<h2>Görüşmeleri haftanıza nasıl yerleştirebilirsiniz?</h2>\n'
                                "<p>Terapide süreklilik önemlidir; bu yüzden en baştan gerçekçi bir gün ve saat seçmek işinizi kolaylaştırır. Ümitköy'den gelen danışanlarımızın bir kısmı iş çıkışı "
                                'saatlerini, bir kısmı ise cumartesi randevularını tercih ediyor. Görüşmeler Pazartesi – Cumartesi 09:00 – 20:00 arasında planlanabilir.</p>\n'
                                '<ul>\n'
                                '<li><b>Sabit bir saat seçin:</b> Her hafta aynı gün ve saatte gelmek, görüşmeyi alışkanlık hâline getirir.</li>\n'
                                '<li><b>Yoğun dönemleri önceden konuşun:</b> Seyahat ya da yoğun iş haftaları için randevuyu birlikte yeniden planlayabiliriz.</li>\n'
                                '<li><b>Gerektiğinde online devam edin:</b> Gelmenin zor olduğu haftalarda görüşmeyi online yapmak süreci kesintiye uğratmaz.</li>\n'
                                '</ul>\n'
                                "<h2>Ümitköy'den gelen aileler ve gençler için</h2>\n"
                                "<p>Ümitköy'de çocuklu aileler ve üniversite çağındaki gençler bir arada yaşıyor. Ebeveynler çoğu zaman çocuklarının okul uyumu, ekran kullanımı ya da ergenlikteki "
                                'iletişim sorunları için başvuruyor; gençler ise sınav dönemi, gelecek kaygısı ya da aileden bağımsızlaşma konularını konuşmak istiyor. Bu farklı ihtiyaçlar için '
                                'görüşmeler ayrı ayrı planlanır; ebeveynle ve gençle yapılan görüşmelerin sınırları en baştan netleştirilir.</p>\n'
                                '<h2>İlk görüşmeye gelmeden önce</h2>\n'
                                '<p>İlk görüşmeye hazırlıklı gelmek zorunda değilsiniz. Yine de aklınızdaki soruları, sizi en çok zorlayan durumları ya da ne zamandır böyle hissettiğinizi kısaca not '
                                'etmek, ilk görüşmede kendinizi anlatmayı kolaylaştırabilir. Ofisimizde ücretsiz otopark olduğu için park yeri aramanız gerekmez; birkaç dakika erken gelmek görüşmeye '
                                'daha sakin başlamanızı sağlar.</p>',
                        'sss': [("Ümitköy'den gelen danışanlar genellikle hangi saatleri tercih ediyor?",
                                 'Çalışanlar çoğunlukla akşam saatlerini ve cumartesi randevularını tercih ediyor. Size uygun saat, ilk iletişimde birlikte belirlenir.'),
                                ('Bazı haftalar yüz yüze, bazı haftalar online görüşebilir miyim?',
                                 'Evet. Gelmenin zor olduğu haftalarda görüşmeyi online yapabilir, sonra yüz yüze devam edebilirsiniz.'),
                                ('Hem kendim hem çocuğum için destek almak istiyorum, nasıl ilerleriz?',
                                 'İhtiyaçlarınız ilk görüşmede konuşulur; sizin ve çocuğunuzun görüşmeleri ayrı planlanır ve gerektiğinde farklı uzmanlarla yürütülür.')],
                        'tarih': '2026-10-27'},
 '/yalnizlik-hissi-ve-sosyal-geri-cekilme/': {'html': '<h2>Kalabalık içinde yalnızlık</h2>\n'
                                                      '<p>Yalnızlık her zaman tek başına olmakla ilgili değildir. Bir evlilik içinde, kalabalık bir ailede ya da iş yerinde de insan kendini yalnız '
                                                      'hissedebilir. Bu duygu çoğu zaman görülmediğini, anlaşılmadığını ya da gerçekte nasıl hissettiğini paylaşacak kimsesi olmadığını düşünmekten '
                                                      'kaynaklanır. Bu nedenle çevrede çok insan olması, yalnızlık hissinin geçeceği anlamına gelmez.</p>\n'
                                                      '<h2>Hayatın farklı dönemlerinde yalnızlık</h2>\n'
                                                      '<ul>\n'
                                                      '<li><b>Üniversite ve ilk iş yılları:</b> Yeni bir şehre ya da ortama taşınmak, eski arkadaşlıklardan uzaklaşmak yalnızlığı artırabilir.</li>\n'
                                                      '<li><b>Yeni ebeveynlik:</b> Bebekle evde geçen uzun saatler ve değişen arkadaşlık ilişkileri, mutlu bir dönemde bile yalnız '
                                                      'hissettirebilir.</li>\n'
                                                      '<li><b>Ayrılık ve boşanma:</b> Ortak arkadaş çevresinin dağılması ve gündelik paylaşımların kaybı yalnızlığı derinleştirebilir.</li>\n'
                                                      '<li><b>Emeklilik:</b> İş yerindeki gündelik temasların sona ermesi ve günün yapısının değişmesi yalnızlık hissine yol açabilir.</li>\n'
                                                      '</ul>\n'
                                                      '<h2>Sosyal medya ve yalnızlık</h2>\n'
                                                      '<p>Sosyal medya bağlantıda kalmayı kolaylaştırsa da başkalarının paylaştığı seçilmiş anlar, kendi hayatınızı eksik görmenize neden olabilir. '
                                                      'Sürekli kaydırarak geçirilen zaman, gerçek temasın yerini almaya başladığında yalnızlık artabilir. Sosyal medyayı tamamen bırakmak gerekmez; '
                                                      'ancak pasif izlemek yerine bir arkadaşa mesaj atmak, bir buluşma ayarlamak gibi etkileşimli kullanımı tercih etmek daha iyi gelebilir.</p>\n'
                                                      '<h2>Bir yakınınız giderek içine kapanıyorsa</h2>\n'
                                                      '<p>Arkadaşlarından uzaklaşan, davetleri sürekli geri çeviren ya da evden çıkmak istemeyen bir yakınınız varsa onu suçlamadan merak ettiğinizi '
                                                      'göstermek önemlidir. "Seni özledim, bir kahve içelim mi?" gibi küçük ve baskı içermeyen davetler kapıyı açık tutar. Geri çekilmeye umutsuzluk, '
                                                      'uyku ve iştah değişiklikleri ya da yaşamın anlamsız olduğuna dair sözler eşlik ediyorsa bir uzmandan destek almasını teşvik edin; kendine zarar '
                                                      "verme riski varsa hemen 112'yi arayın.</p>\n"
                                                      '<h2>Yalnızlıkla ilgili düşünce tuzakları</h2>\n'
                                                      '<p>Uzun süre yalnız hisseden kişilerde bazı düşünceler, yeniden bağ kurmayı zorlaştırabilir: "Kimse benimle vakit geçirmek istemez", '
                                                      '"Aradığımda rahatsız ederim", "Herkesin zaten bir arkadaş çevresi var" gibi. Bu düşünceler kişiyi davetleri geri çevirmeye ve ilk adımı '
                                                      'atmaktan kaçınmaya yöneltir; bu da yalnızlığı pekiştirir.</p>\n'
                                                      '<p>Bu düşünceleri fark etmek ve küçük denemelerle sınamak işe yarayabilir: Uzun süredir konuşmadığınız birine kısa bir mesaj atmak, bir '
                                                      'etkinliğe yalnızca yarım saatliğine katılmak gibi. Her deneme beklediğiniz gibi sonuçlanmayabilir; ama zamanla bu adımlar yeni bağların '
                                                      'kurulmasına zemin hazırlar.</p>',
                                              'sss': [('Evliyim ama kendimi çok yalnız hissediyorum, bu normal mi?',
                                                       'Evet, ilişki içinde de yalnızlık hissedilebilir. Bu duygu çoğu zaman duygusal yakınlığın azaldığına işaret eder; bunu eşinizle ya da bir '
                                                       'uzmanla konuşmak ilk adım olabilir.'),
                                                      ('Yeni bir şehre taşındım, arkadaş edinmekte zorlanıyorum. Ne yapabilirim?',
                                                       'Düzenli olarak aynı insanlarla karşılaşabileceğiniz bir kurs, spor grubu ya da gönüllü çalışma gibi ortamlar arkadaşlık kurmayı kolaylaştırır. '
                                                       'Yakınlık zamanla gelişir; ilk haftalarda yalnız hissetmek olağandır.')],
                                              'tarih': '2026-10-27'},
 '/yasamkent-psikolog/': {'html': "<h2>Yaşamkent'te yetişkinler için bireysel görüşmeler</h2>\n"
                                  '<p>Aile içindeki rolleriniz ne kadar yoğun olursa olsun, kendi ihtiyaçlarınız da önemlidir. Bireysel görüşmelerde kaygı, stres, değersizlik hissi, karar vermede '
                                  'zorlanma ya da hayatın bir döneminde yaşanan belirsizlikler konuşulabilir. Kendinizi anlatırken neyin sizi zorladığını fark etmek, çoğu zaman değişimin ilk '
                                  'adımıdır. Görüşmelerin sıklığı ve süresi ihtiyacınıza göre birlikte belirlenir; düzenli görüşmeler süreci daha verimli kılar.</p>\n'
                                  '<p>Bireysel görüşmelerde konuşulanlar size aittir; aile ya da çift görüşmesine geçmek isterseniz bu karar da birlikte verilir.</p>\n'
                                  "<h2>Yaşamkent'te yaşayanların sık konuştuğu konular</h2>\n"
                                  '<p>Yaşamkent, aile yaşamının ağırlıkta olduğu bir semt. Danışanlarımızın önemli bir kısmı evlilikte biriken kırgınlıklar, çocuk yetiştirirken eşler arasındaki '
                                  'farklı yaklaşımlar, iş ve ev sorumlulukları arasında sıkışmışlık hissi gibi konularla başvuruyor. Bu konular çoğu zaman tek bir büyük sorundan değil, uzun süre '
                                  'konuşulmadan biriken küçük gerginliklerden oluşuyor.</p>\n'
                                  '<ul>\n'
                                  '<li><b>Çiftler:</b> iletişimin azalması, tekrar eden tartışmalar, ebeveynlik rolleri yüzünden ilişkinin geri planda kalması</li>\n'
                                  '<li><b>Ebeveynler:</b> çocuğun okul uyumu, öfke nöbetleri, ergenlikte iletişim</li>\n'
                                  '<li><b>Yetişkinler:</b> iş stresi, kaygı, kendine zaman ayıramama</li>\n'
                                  '</ul>\n'
                                  '<h2>Eve yakın bir ofisin terapiye katkısı</h2>\n'
                                  "<p>Terapide değişim genellikle düzenli görüşmelerle oluşur. Ofise ulaşmanın kolay olması, yoğun bir haftada bile randevuyu ertelememenize yardım eder. Yaşamkent'te "
                                  'yaşayan danışanlarımız için görüşme saatini günlük düzene yerleştirmek daha kolaydır; çocuğu okuldan almadan önce ya da iş dönüşü bir saat ayırmak mümkün olabilir. '
                                  'Binada ücretsiz otopark bulunur.</p>\n'
                                  '<h2>Mahremiyet konusunda merak edilenler</h2>\n'
                                  '<p>Yaşadığınız semte yakın bir yerde görüşme yapmak, bazı kişilerde "tanıdık birine rastlar mıyım" endişesi yaratabilir. Görüşmeleriniz meslek etiği gereği '
                                  'gizlidir; randevular, bekleme süresi kısa tutulacak şekilde planlanır. Bu konuda bir endişeniz varsa randevu alırken paylaşabilir, size uygun saati birlikte '
                                  'seçebiliriz. Dilerseniz görüşmelerin bir kısmını online da yapabilirsiniz.</p>\n'
                                  '<h2>Çift ve aile görüşmesine gelmeden önce</h2>\n'
                                  '<p>Çift ya da aile olarak başvuruyorsanız, görüşmeye kimlerin katılacağını önceden konuşmanız işinizi kolaylaştırır. İlk görüşmede her tarafın kendi bakış açısını '
                                  'anlatabileceği bir alan açılır; kimse haklı ya da haksız ilan edilmez. Çocukla ilgili başvurularda ise genellikle önce ebeveynlerle bir ön görüşme yapılır, '
                                  'ardından çocuğun ihtiyacına göre süreç planlanır.</p>',
                          'sss': [('Eşimle birlikte gelmek istiyoruz ama eşim çekiniyor, ne yapabiliriz?',
                                   'İlk görüşmeye tek başınıza gelmeniz de mümkündür. Eşinizin çekincelerini nasıl konuşabileceğinizi birlikte değerlendirebiliriz.'),
                                  ('Yaşamkent ofisinde görüşmeler ne sıklıkla yapılır?', 'Genellikle haftada bir görüşmeyle başlanır; süreç ilerledikçe sıklık ihtiyacınıza göre birlikte belirlenir.'),
                                  ('Görüşmeye gelirken yanımda bir şey getirmem gerekir mi?',
                                   'Gerekmez. Çocuğunuz için başvuruyorsanız okuldan gelen notlar ya da gözlemleriniz ilk görüşmede faydalı olabilir.')],
                          'tarih': '2026-10-27'},
 '/yetiskinler-icin/': {'html': '<h2>Yetişkinler hangi konularla başvuruyor?</h2>\n'
                                '<p>Yetişkin danışanlarımızın başvuru nedenleri çok çeşitlidir. Kimi uzun süredir geçmeyen bir yorgunluk ve isteksizlikle, kimi bir ayrılık ya da kayıp sonrasında, '
                                'kimi de iş hayatındaki baskı ya da ilişkilerinde tekrar eden sorunlarla gelir. Bazen ortada belirgin bir sorun yoktur; kişi yalnızca kendini daha iyi anlamak, bir '
                                'karar öncesinde düşüncelerini netleştirmek ister. Bunların hepsi görüşmeler için geçerli nedenlerdir.</p>\n'
                                '<ul>\n'
                                '<li>Kaygı, stres ve sürekli tetikte olma hâli</li>\n'
                                '<li>İsteksizlik, keyif alamama ve duygu durumunda düşüklük</li>\n'
                                '<li>İlişki, evlilik ve aile içi sorunlar</li>\n'
                                '<li>İş stresi, tükenmişlik ve kariyer kararları</li>\n'
                                '<li>Yas, ayrılık ve yaşam geçişleri</li>\n'
                                '<li>Özgüven, sınır koyma ve kendini ifade etme</li>\n'
                                '</ul>\n'
                                '<h2>Çalışan yetişkinler için görüşme planlaması</h2>\n'
                                '<p>Yoğun çalışan yetişkinler için en büyük engel çoğu zaman zaman bulmaktır. Görüşmeler pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabilir; akşam ve '
                                "cumartesi saatleri bu nedenle en çok talep gören saatlerdir. Ofisimiz Konutkent'te, Dumlupınar Bulvarı No:399 adresinde yer alır ve binada ücretsiz otopark vardır. "
                                'İş seyahati ya da yoğun dönemlerde aynı uzmanla online görüşmeye geçmek de mümkündür.</p>\n'
                                '<p>Düzenli görüşmeler için her hafta aynı gün ve saati ayırmak, görüşmeleri günlük programın doğal bir parçası hâline getirir ve sürekliliği kolaylaştırır.</p>\n'
                                '<h2>Psikolog mu, psikiyatrist mi?</h2>\n'
                                '<p>Yetişkinlerin sık sorduğu sorulardan biri, kime başvurmaları gerektiğidir. Psikologlar görüşmeler yoluyla psikolojik destek verir ve ilaç yazmaz. Belirtilerin çok '
                                'yoğun olduğu, günlük işlevselliğin belirgin biçimde bozulduğu durumlarda bir psikiyatriste de başvurmanız önerilebilir; bu durumda görüşmeler psikiyatrik destekle '
                                "birlikte sürdürülebilir. Kendinize ya da başkasına zarar verme düşünceleriniz varsa beklemeden 112'yi arayın.</p>\n"
                                '<h2>İlk görüşmeye nasıl hazırlanılır?</h2>\n'
                                '<p>İlk görüşme için özel bir hazırlık gerekmez. Yine de bazı kişiler, aklına gelenleri kısaca not ederek gelmeyi rahatlatıcı bulur: Sizi en çok zorlayan durumlar, '
                                'bunların ne zamandır sürdüğü, daha önce destek alıp almadığınız ve görüşmelerden beklentileriniz. İlk görüşmede her şeyi anlatmak zorunda değilsiniz; anlatmak '
                                'istemediğiniz konuları daha sonraya bırakabilirsiniz. Görüşmenin sonunda nasıl bir yol izlenebileceği, görüşme sıklığı ve sürenin nasıl belirleneceği birlikte '
                                'konuşulur.</p>\n'
                                '<p>Yetişkinlerde psikolojik desteğin kapsamı ve süreç hakkında ayrıntılı rehber: <a href="https://www.psikologrojinnazik.com/ankara-yetiskin-psikologu/">Yetişkin '
                                'psikoloğu kimlere destek verir?</a></p>',
                        'sss': [('Belirgin bir sorunum yok, yine de görüşme alabilir miyim?',
                                 'Evet. Kendinizi daha iyi tanımak ya da bir karar sürecinde düşüncelerinizi netleştirmek de görüşme için geçerli bir nedendir.'),
                                ('İş çıkışı görüşmeye gelebilir miyim?',
                                 'Evet. Görüşmeler pazartesiden cumartesiye 09:00 – 20:00 arasında planlanabilir; akşam saatleri için erken randevu almanızı öneririz.'),
                                ('Psikiyatriste de gitmem gerekir mi?',
                                 'Her durumda gerekmez. Belirtiler çok yoğunsa ya da günlük hayatınızı belirgin biçimde etkiliyorsa psikiyatrik değerlendirme de önerilebilir.')],
                        'tarih': '2026-10-27'},
 '/yurt-disi-online-ebeveyn-danismanligi/': {'html': '<h2>Görüşmeye kimler katılabilir?</h2>\n'
                                                     '<p>Online ebeveyn danışmanlığında görüşmeler çoğunlukla anne ve babayla yapılır. Ebeveynlerin aynı ekrandan birlikte katılması en sık tercih '
                                                     'edilen yöntemdir; ancak farklı şehirlerde ya da farklı ülkelerde yaşayan ebeveynler ayrı yerlerden de bağlanabilir. Çocuğun ya da gencin '
                                                     'görüşmelere katılıp katılmayacağı, yaşına ve konuya göre birlikte değerlendirilir. Bazı aileler için yalnızca ebeveyn görüşmeleri yeterli '
                                                     'olurken, ergenlerle ayrıca görüşmek de mümkündür.</p>\n'
                                                     '<h2>İki dilli çocuklarla evde neler yapabilirsiniz?</h2>\n'
                                                     '<ul>\n'
                                                     "<li><b>Türkçeyi bir zorunluluk değil, bir bağ hâline getirin:</b> Masal okumak, şarkı söylemek, Türkiye'deki akrabalarla görüntülü konuşmalar "
                                                     'Türkçeyi duygusal bir deneyimle ilişkilendirir.</li>\n'
                                                     '<li><b>Dil karışıklığını düzeltmek yerine yansıtın:</b> Çocuğunuz iki dili karıştırarak konuşuyorsa onu düzeltmek yerine, aynı cümleyi doğal bir '
                                                     'şekilde Türkçe tekrar edebilirsiniz.</li>\n'
                                                     '<li><b>Okul dilini küçümsemeyin:</b> Çocuğun yaşadığı ülkenin dili de kimliğinin bir parçasıdır. Her iki dile de değer verildiğini hissetmesi, '
                                                     'aidiyet duygusunu güçlendirir.</li>\n'
                                                     '<li><b>Kendi duygularınızı fark edin:</b> Çocuğunuz Türkçe konuşmak istemediğinde hissettiğiniz kırgınlık ya da kaygı anlaşılır bir duygudur; '
                                                     'bunu konuşabileceğiniz bir alan bulmak, çocuğunuza daha sakin yaklaşmanızı kolaylaştırır.</li>\n'
                                                     '</ul>\n'
                                                     '<h2>Saat farkı ve randevu planlaması</h2>\n'
                                                     '<p>Görüşme saatleri, Türkiye saati ile bulunduğunuz ülkenin saati birlikte yazılarak planlanır. Yaz saati uygulamasına geçişlerde saat farkı '
                                                     'değişebileceği için, bu dönemlerde randevu saatleri ayrıca teyit edilir. Çalışan ebeveynler için akşam saatleri ya da cumartesi günleri tercih '
                                                     'edilebilir; çocukların okul ve uyku saatleri de planlamada dikkate alınır.</p>\n'
                                                     '<h2>Nasıl başvurulur ve ödeme nasıl yapılır?</h2>\n'
                                                     "<p>Yurt dışından telefonla aramak ücretli ya da zor olabileceği için başvurularda WhatsApp'ı öneriyoruz. Mesajınızda bulunduğunuz ülkeyi, "
                                                     'çocuğunuzun yaşını ve kısaca hangi konuda destek almak istediğinizi yazmanız yeterlidir. Size uygun gün ve saatler, görüşme süreci ve ödeme '
                                                     'bilgileri WhatsApp üzerinden iletilir. Görüşmeler Türkçe yapılır; kültürel bağlamı baştan açıklamak zorunda kalmadan konuşabilirsiniz.</p>\n'
                                                     '<h2>Ebeveynlerin kendi yükü de konuşulur</h2>\n'
                                                     '<p>Yurt dışında çocuk büyütmek, ebeveynler için çoğu zaman görünmeyen bir yük taşır. Büyükanne ve büyükbabanın desteğinden uzak olmak, yeni bir '
                                                     'dilde okul ve resmi işlerle uğraşmak, bazen de eşlerden birinin yalnız kalması yorgunluğu artırır. Online ebeveyn danışmanlığında yalnızca '
                                                     'çocuğun ihtiyaçları değil, ebeveynlerin kendi duyguları ve yorgunluğu da ele alınır. Ebeveynin kendini daha dengede hissetmesi, çocukla kurulan '
                                                     'ilişkiye de doğrudan yansır.</p>',
                                             'sss': [('Görüşmeye yalnızca bir ebeveyn katılabilir mi?',
                                                      'Evet. Ebeveynlerden biri katılabileceği gibi iki ebeveyn birlikte de katılabilir. Mümkünse her iki ebeveynin de sürece dahil olması önerilir.'),
                                                     ('Ödemeyi nasıl yapacağım?', 'Ödeme bilgileri, randevu planlanırken WhatsApp üzerinden size iletilir.'),
                                                     ('Ergen çocuğumla da görüşme yapılabilir mi?',
                                                      'Evet. Ergenin yaşı ve isteğine göre kendisiyle de online görüşmeler planlanabilir; öncesinde ebeveynlerle ön görüşme yapılır.')],
                                             'tarih': '2026-10-27'}}

# Meta açıklama düzeltmeleri (27 Ekim SEO denetimi): 100–165 karakter, telefon numarası yok.
# Kaynaktaki açıklamanın yerine geçer (semt, hizmet ve içerik sayfaları).
ACIKLAMA = {
    '/cayyolu-psikolog-fiyatlari/': "Çayyolu, Yaşamkent ve Konutkent'te psikolog seans ücretleri: bireysel, çift, aile, çocuk ve ergen görüşmelerinde ücreti belirleyen etkenler.",
    '/cayyolu-psikolojik-danismanlik-merkezi/': "RN Psikoloji Çayyolu: bireysel, çift, aile, çocuk ve ergen psikolojik danışmanlık merkezi. Konutkent ofisi, ücretsiz otopark, online görüşme.",
    '/cocuklarda-uyku-sorunlari/': "Çocuk yalnız uyuyamıyor, gece sık uyanıyor ya da kâbus görüyorsa ne yapmalı? Uyku düzeni, ekran ve kaygıyla ilişkisi üzerine ebeveyn rehberi.",
    '/ilk-terapi-seansi-rehberi/': "Psikoloğa ilk kez gidecekler için rehber: ilk seansta neler konuşulur, nasıl hazırlanılır, gizlilik nasıl korunur? Merak edilenler yanıtlarıyla.",
    '/randevu-sik-sorulan-sorular/': "RN Psikoloji Çayyolu'nda randevu ve ilk görüşme: ilk görüşmede neler yapılır, hangi uzmanla görüşmeli, nasıl randevu alınır? En sık sorular.",
    '/yalnizlik-hissi-ve-sosyal-geri-cekilme/': "Kalabalıklar içinde yalnız hissetmek ve insanlardan uzaklaşmak: nedenleri, yalnızlıkla baş etme yolları ve psikolojik desteğin ne zaman gerektiği.",
    '/yasamkent-psikolog/': "Yaşamkent'te yüz yüze psikolojik danışmanlık: yetişkin, çift, aile, çocuk ve ergen görüşmeleri. Ücretsiz otopark, Pazartesi–Cumartesi randevu.",
    '/yurt-disi-online-ebeveyn-danismanligi/': "Yurt dışında çocuk büyüten Türk ailelere Türkçe online ebeveyn danışmanlığı: iki dil, iki kültür, okul uyumu ve ergenlik dönemi.",
    '/basinda-biz/': "Basında RN Psikoloji: kurucu psikoloğumuz Rojin Nazik'in katıldığı TV programları, gazete röportajları ve uzman görüşleri bir arada.",
    '/galeri/': "RN Psikoloji Çayyolu ofisinden görüntüler: seans odaları ve bekleme alanından kareler. İlk görüşmenizden önce ofisimize göz atabilirsiniz.",
    '/gizlilik/': "RN Psikoloji Çayyolu gizlilik yaklaşımı: hangi bilgileri neden istediğimiz, bu bilgileri nasıl koruduğumuz ve haklarınız hakkında bilgilendirme.",
    '/kitaplarimiz/': "Kurucu psikoloğumuz Rojin Nazik'in kitapları: Bir Hayatla Evlenmek, Bir Odanın Ötesi ve Dengeyi Yakalamak. Kitaplar hakkında kısa bilgiler.",
    '/uzmanlarimiz/': "RN Psikoloji Çayyolu uzmanları: Psikolog Rojin Nazik ve Psikolog Elif Erdoğan. Uzmanlarımızın çalışma alanları ve görüşme yaptıkları konular.",
}
