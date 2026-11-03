# -*- coding: utf-8 -*-
"""Çayyolu /basinda-biz/ için "Basın Dosyası" sahnesi (gazete ön sayfası + yayın monitörü).
Rojin sitesindeki TV kurgusunun ÖZELLİKLERİ (canlı yayın gibi akan videolar, kanal listesi, manşet, sayaç,
kaydırma ipuçları, ara → WhatsApp) burada farklı bir görsel dille: gazete kâğıdı, lacivert mürekkep, ince ekran.
Kendi içinde CSS/JS; dış dosya yok. YouTube yalnızca ziyaretçinin ilk dokunuş/kaydırmasından sonra ve ekran yakındayken yüklenir."""
import html, json
E = lambda x: html.escape(x, quote=True)

# Türkçe bulunma eki: "CNN Türk'te", "Sabah'ta" ...
EK = {'CNN Türk': "CNN Türk'te", 'Milliyet': "Milliyet'te", 'Sabah': "Sabah'ta", 'Posta': "Posta'da", 'Cumhuriyet': "Cumhuriyet'te",
      'Haberler.com': "Haberler.com'da", 'Psychology Times': "Psychology Times'ta", 'Lezzet': "Lezzet'te"}
SAYAC = [(46, 'çevrimiçi haber'), (19, 'gazete sayfası'), (11, 'ulusal yayın'), (7, 'TV ve video yayını'), (3, 'kitap')]
LOGO = [('CNN TÜRK', 'cnnturk', 146, 120), ('Milliyet', 'milliyet', 480, 87), ('Sabah', 'sabah', 292, 105), ('Posta', 'posta', 307, 91),
        ('Akşam', 'aksam', 480, 103), ('Takvim', 'takvim', 460, 120), ('Vatan', 'vatan', 480, 102), ('Beyaz TV', 'beyaztv', 204, 70),
        ('Psychology Times', 'psychologytimes', 480, 81)]

CSS = '''<style>
.bd{--kg:#F6F1E6;--kg2:#EDE5D3;--mr:#14264A;--kr:#B3261E;font-family:var(--ff-b);color:var(--mr)}
.bd *{box-sizing:border-box}
.bd-on{background:var(--kg);border:1px solid #DDD2BC;border-radius:6px;padding:18px 16px 20px;margin:0 0 28px;box-shadow:0 1px 0 #fff inset,0 18px 40px -26px rgba(20,38,74,.45);position:relative;overflow:hidden}
.bd-on:before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.5;background:repeating-linear-gradient(0deg,rgba(20,38,74,.025) 0 1px,transparent 1px 3px)}
.bd-ust{display:flex;justify-content:space-between;gap:8px;font:700 11px/1.3 var(--ff-b);letter-spacing:.14em;text-transform:uppercase;color:#6a6252;border-bottom:1px solid var(--mr);padding-bottom:6px}
.bd-bas{font:900 clamp(2.1rem,9vw,3.6rem)/.95 Georgia,"Times New Roman",serif;letter-spacing:-.02em;text-align:center;margin:12px 0 6px;color:var(--mr)}
.bd-alt{display:flex;justify-content:center;flex-wrap:wrap;gap:4px 14px;border-top:3px double var(--mr);border-bottom:3px double var(--mr);padding:6px 0;font-size:12.5px;font-weight:700;letter-spacing:.04em;color:#3b3a36;text-align:center}
.bd-ms{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:10px;margin:14px 0 4px;min-height:58px}
.bd-ms b{background:var(--kr);color:#fff;font:800 11px/1 var(--ff-b);letter-spacing:.14em;padding:7px 8px;border-radius:2px;align-self:start;margin-top:4px}
.bd-ms a{font:700 clamp(1.15rem,4.6vw,1.6rem)/1.22 Georgia,serif;color:var(--mr);text-decoration:none;transition:opacity .45s,transform .45s;display:block}
.bd-ms a.bd-gz{opacity:0;transform:translateY(6px)}
.bd-ms a small{display:block;font:700 11.5px/1.4 var(--ff-b);letter-spacing:.08em;text-transform:uppercase;color:#7a6f5c;margin-top:4px}
.bd-iki{display:grid;grid-template-columns:1.35fr 1fr;gap:18px;margin-top:14px;border-top:1px solid #cdbfa3;padding-top:14px}
@media(max-width:760px){.bd-iki{grid-template-columns:1fr}}
.bd-mon{position:relative}
.bd-ekr{position:relative;aspect-ratio:16/9;background:#0b0f18;border:7px solid #11151c;border-bottom-width:9px;border-radius:10px;overflow:hidden;box-shadow:0 0 0 1px #2a3140,0 16px 30px -16px rgba(0,0,0,.6)}
.bd-ekr:after{content:"";position:absolute;inset:0;pointer-events:none;z-index:5;background:linear-gradient(115deg,rgba(255,255,255,.10) 0%,rgba(255,255,255,0) 38%)}
.bd-ayak{width:26%;height:10px;margin:0 auto;background:linear-gradient(#2a2f38,#11151c);border-radius:0 0 8px 8px}
.bd-k{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .5s;z-index:1}
.bd-k.on{opacity:1}
.bd-yt{position:absolute;inset:0;z-index:2;overflow:hidden;opacity:0;pointer-events:none!important;transition:opacity .5s}
.bd-yt iframe{position:absolute;left:50%;top:50%;width:150%;height:150%;transform:translate(-50%,-50%);border:0;pointer-events:none}
.bd-mon.canli .bd-yt{opacity:1}.bd-mon.canli.bekle .bd-yt{opacity:0;transition:none}
.bd-kar{position:absolute;inset:0;z-index:3;opacity:0;pointer-events:none;background:#1c2230 repeating-linear-gradient(90deg,rgba(255,255,255,.08) 0 2px,transparent 2px 5px);transition:opacity .15s}
.bd-mon.kar .bd-kar,.bd-mon.bekle .bd-kar{opacity:1;animation:bdkar .25s steps(3) infinite}
@keyframes bdkar{0%{background-position:0 0}50%{background-position:7px 2px}100%{background-position:-5px -3px}}
.bd-bug{position:absolute;z-index:6;left:10px;top:10px;display:flex;align-items:center;gap:6px;background:rgba(11,15,24,.72);color:#fff;font:800 10.5px/1 var(--ff-b);letter-spacing:.12em;padding:6px 8px;border-radius:3px}
.bd-bug i{width:7px;height:7px;border-radius:50%;background:#E5484D;animation:bdnb 1.4s ease-in-out infinite}
@keyframes bdnb{50%{opacity:.25}}
.bd-alt2{margin:8px 0 0;font-size:13.5px;line-height:1.35;color:var(--mr);min-height:38px}
.bd-alt2 b{display:block;font:800 10.5px/1.4 var(--ff-b);letter-spacing:.12em;color:var(--kr);text-transform:uppercase}
.bd-alt2 b:before{content:"Şimdi · "}
.bd-ses{position:absolute;z-index:7;right:10px;top:10px;min-height:36px;padding:0 12px;border-radius:999px;border:1px solid rgba(255,255,255,.5);background:rgba(179,38,30,.92);color:#fff;font:700 12.5px/1 var(--ff-b);cursor:pointer}
.bd-ses[hidden]{display:none}
.bd-akis h3{font:800 12px/1 var(--ff-b);letter-spacing:.16em;text-transform:uppercase;margin:2px 0 8px;color:var(--kr)}
.bd-akis ol{list-style:none;margin:0;padding:0;border-top:2px solid var(--mr)}
.bd-akis li{border-bottom:1px solid #d6caae}
.bd-akis button{all:unset;box-sizing:border-box;display:grid;grid-template-columns:34px 1fr;gap:8px;align-items:center;width:100%;min-height:48px;padding:8px 2px;cursor:pointer;font-size:14px;line-height:1.3;color:var(--mr)}
.bd-akis button span{font:800 13px/1 Georgia,serif;color:#7a6f5c;border:1px solid #bfb196;border-radius:3px;text-align:center;padding:6px 0}
.bd-akis button.on span{background:var(--kr);border-color:var(--kr);color:#fff}
.bd-akis button.on{font-weight:800}
.bd-akis button:focus-visible{outline:2px solid var(--kr);outline-offset:2px}
.bd-say{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin:16px 0 0;border-top:1px solid var(--mr);border-bottom:1px solid var(--mr)}
.bd-say div{padding:10px 4px;text-align:center;font-size:11.5px;line-height:1.25;color:#4b4638;border-left:1px solid #cdbfa3}
.bd-say div:first-child{border-left:0}
.bd-say b{display:block;font:900 clamp(1.5rem,6vw,2.1rem)/1 Georgia,serif;color:var(--mr);margin-bottom:3px}
@media(max-width:560px){.bd-say{grid-template-columns:repeat(6,1fr)}.bd-say div{grid-column:span 2}.bd-say div:nth-child(n+4){grid-column:span 3;border-top:1px solid #cdbfa3}.bd-say div:nth-child(4){border-left:0}}
@media(max-width:760px){.bd .bz-vs{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:12px;padding-bottom:8px}.bd .bz-v{flex:0 0 82%;scroll-snap-align:center}}
.bd-lg{overflow:hidden;margin:14px -16px 0;padding:10px 0;background:#fff;border-top:1px solid #DDD2BC;border-bottom:1px solid #DDD2BC;-webkit-mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.bd-lg ul{display:flex;gap:30px;width:max-content;list-style:none;margin:0;padding:0;animation:bdlg 32s linear infinite}
.bd-lg li{display:flex;align-items:center;height:34px}.bd-lg img{height:26px;width:auto;max-width:130px}
@keyframes bdlg{to{transform:translateX(-50%)}}
.bd-cta{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0 0;align-items:center}
.bd-cta p{flex-basis:100%;margin:0;font:700 15px/1.4 Georgia,serif}
.bd-ipu{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:13px;font-weight:700;color:#7a6f5c;margin:-4px 0 8px}
.bd-ipu i{font-style:normal;display:inline-block;animation:bdok 1.6s ease-in-out infinite}
@keyframes bdok{50%{transform:translateX(5px)}}
.bd .press-grid.page.bd-kay{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:16px;padding:10px 4px 18px;-webkit-overflow-scrolling:touch;scrollbar-width:thin}
.bd .bd-kay .press-item{flex:0 0 min(78%,300px);scroll-snap-align:center;background:#fff;padding:10px 10px 12px;margin:0;border-radius:2px;box-shadow:0 10px 24px -14px rgba(20,38,74,.5);position:relative;transform:rotate(-.8deg)}
.bd .bd-kay .press-item:nth-child(2n){transform:rotate(.9deg)}
.bd .bd-kay .press-item:before{content:"";position:absolute;left:50%;top:-8px;width:70px;height:18px;margin-left:-35px;background:rgba(233,162,59,.55);transform:rotate(-3deg)}
.bd .bd-kay .press-item img{width:100%;height:220px;object-fit:cover;object-position:top;display:block;cursor:zoom-in;filter:sepia(.12)}
.bd .bd-kay figcaption{font-size:13.5px;line-height:1.4;margin-top:8px}
.bd-orta{margin:22px 0;padding:18px 16px;border:2px solid var(--mr);background:var(--kg);border-radius:4px}
.bd-orta b{display:block;font:800 11px/1 var(--ff-b);letter-spacing:.16em;color:var(--kr);text-transform:uppercase;margin-bottom:8px}
.bd-orta p{margin:0 0 12px;font:700 clamp(1.05rem,4.2vw,1.3rem)/1.35 Georgia,serif}
.bd .bd-hab{list-style:none;padding:0;margin:0 0 18px;border-top:2px solid var(--mr)}
.bd .bd-hab li{border-bottom:1px solid var(--line,#DCE4F0);margin:0}
.bd .bd-hab a{display:block;padding:12px 0;min-height:44px;text-decoration:none;color:var(--mr);font:600 16px/1.35 Georgia,serif}
.bd .bd-hab a strong{display:block;font:800 11px/1.3 var(--ff-b);letter-spacing:.12em;text-transform:uppercase;color:var(--kr);margin-bottom:2px}
.bd-lb{position:fixed;inset:0;z-index:9999;background:rgba(11,15,24,.92);display:flex;align-items:center;justify-content:center;padding:16px}
.bd-lb img{max-width:100%;max-height:86vh;width:auto;height:auto;background:#fff;padding:6px}
.bd-lb button{position:absolute;right:12px;top:12px;width:44px;height:44px;border-radius:50%;border:0;background:#fff;color:var(--mr);font-size:22px;cursor:pointer}
@media(prefers-reduced-motion:reduce){.bd *{animation:none!important;transition:none!important}}
</style>'''

JS = r'''<script>(function(){var d=document,w=window,az=w.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
/* Manşet: yayınlardan başlıklar sırayla döner */
var ms=d.querySelector('.bd-ms a'),M=[];try{M=JSON.parse(ms.getAttribute('data-m'))}catch(e){}var mi=0;
if(ms&&M.length>1&&!az)setInterval(function(){if(d.hidden)return;ms.classList.add('bd-gz');setTimeout(function(){mi=(mi+1)%M.length;var x=M[mi];ms.href=x.u;ms.firstChild.textContent=x.t;ms.lastChild.textContent=x.o;ms.classList.remove('bd-gz')},450)},5200);
/* Sayaç: görünür olunca sayarak artar */
var sy=d.querySelector('.bd-say');if(sy&&'IntersectionObserver' in w&&!az){var bs=sy.querySelectorAll('b');bs.forEach(function(b){b.setAttribute('data-n',b.textContent);b.textContent='0'});
 var io=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;io.disconnect();var t0=performance.now();(function f(t){var p=Math.min(1,(t-t0)/1100);bs.forEach(function(b){b.textContent=Math.round(+b.getAttribute('data-n')*(1-Math.pow(1-p,3)))});if(p<1)requestAnimationFrame(f)})(t0)},{threshold:.4});io.observe(sy);}
/* Kupürler: kaydırma sayacı + büyütme */
d.querySelectorAll('.bd-kay').forEach(function(k){var ip=k.previousElementSibling,s=ip&&ip.querySelector('em'),n=k.children.length;
 if(s)k.addEventListener('scroll',function(){var c=Math.round(k.scrollLeft/(k.children[0].offsetWidth+16))+1;s.textContent=Math.min(n,c)+' / '+n;},{passive:true});
 k.addEventListener('click',function(e){var im=e.target.closest('img');if(!im)return;var lb=d.createElement('div');lb.className='bd-lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-label',im.alt);
  lb.innerHTML='<img alt=""><button type="button" aria-label="Kapat">×</button>';lb.firstChild.src=im.currentSrc||im.src;lb.firstChild.alt=im.alt;d.body.appendChild(lb);lb.querySelector('button').focus();
  var kapa=function(){lb.remove();d.removeEventListener('keydown',tus)},tus=function(e){if(e.key==='Escape')kapa()};lb.addEventListener('click',kapa);d.addEventListener('keydown',tus);});});
/* Yayın monitörü: kareler akar; ilk dokunuştan sonra gerçek videolar sessiz, 4,5 sn'de bir kanal değiştirir */
var mon=d.querySelector('.bd-mon');if(!mon)return;var L=[];try{L=JSON.parse(mon.getAttribute('data-kanal'))}catch(e){}if(!L.length)return;
var ekr=mon.querySelector('.bd-ekr'),kl=mon.querySelectorAll('.bd-k'),kn=mon.querySelector('.bd-alt2 b'),bs2=mon.querySelector('.bd-alt2 span'),ses=mon.querySelector('.bd-ses'),btn=d.querySelectorAll('[data-bd-no]');
var i=0,tm=null,gor=false,yakin=false,etk=false,pl=null,hazir=false,sesli=false,basla=0,oynadi=false,bekci=null,bekle=null,kuruldu=false,hata=0;
var bag=navigator.connection||{},zayif=bag.saveData||/(^|-)2g$/.test(bag.effectiveType||'');
function isaret(){btn.forEach(function(b){var on=+b.getAttribute('data-bd-no')===i;b.classList.toggle('on',on);b.setAttribute('aria-current',on?'true':'false')});kn.textContent=L[i].k;bs2.textContent=L[i].b;}
function kare(n){i=(n+L.length)%L.length;mon.classList.add('kar');setTimeout(function(){kl.forEach(function(m,j){m.classList.toggle('on',j===i)});isaret();},160);setTimeout(function(){mon.classList.remove('kar')},380);}
function akis(){if(!tm&&!pl&&!az&&L.length>1)tm=setInterval(function(){if(gor)kare(i+1)},4050);}
function birak(){try{pl&&pl.destroy()}catch(e){}pl=null;hazir=false;clearInterval(bekci);bekci=null;clearTimeout(bekle);mon.classList.remove('canli','bekle','kar');ses.hidden=true;mon.querySelector('.bd-yt').innerHTML='';kare(i);akis();}
function gec(n){if(!pl)return;basla=0;mon.classList.add('bekle');i=(n===undefined?i+1:n+L.length)%L.length;var x=L[i];clearTimeout(bekle);bekle=setTimeout(function(){if(mon.classList.contains('bekle'))birak()},12000);
 setTimeout(function(){try{pl.loadVideoById({videoId:x.y,startSeconds:x.t||45})}catch(e){}kl.forEach(function(m,j){m.classList.toggle('on',j===i)});isaret();},160);}
function kur(){if(kuruldu||zayif||az)return;kuruldu=true;if(tm){clearInterval(tm);tm=null}
 var s=d.createElement('script');s.src='https://www.youtube.com/iframe_api';s.async=true;d.head.appendChild(s);
 var eski=w.onYouTubeIframeAPIReady;w.onYouTubeIframeAPIReady=function(){if(eski)try{eski()}catch(e){}var k=d.createElement('div');mon.querySelector('.bd-yt').appendChild(k);mon.classList.add('bekle');
  pl=new YT.Player(k,{host:'https://www.youtube-nocookie.com',videoId:L[i].y,playerVars:{autoplay:1,mute:1,controls:0,cc_load_policy:0,cc_lang_pref:'xx',hl:'tr',playsinline:1,rel:0,modestbranding:1,disablekb:1,fs:0,iv_load_policy:3,start:L[i].t||45},
   events:{onReady:function(e){hazir=true;e.target.mute();if(gor||yakin)e.target.playVideo();bekle=setTimeout(function(){if(!oynadi)birak()},12000);
     bekci=setInterval(function(){if(!pl||!hazir||sesli||!basla||!gor)return;var st=-1;try{st=pl.getPlayerState()}catch(e){}if(st===1&&Date.now()-basla>=4500)gec();},400);},
    onStateChange:function(e){if(e.data===1){basla=Date.now();oynadi=true;hata=0;clearTimeout(bekle);try{pl.unloadModule('captions');pl.unloadModule('cc')}catch(x){}mon.classList.remove('bekle','kar');mon.classList.add('canli');ses.hidden=false;return;}
     /* duraklama/takılma/bitiş: YouTube'un kendi ekranı ve önerileri görünmez */mon.classList.add('bekle');if(e.data===0)gec();else if(e.data===2&&(gor||yakin)){try{pl.playVideo()}catch(x){}}},
    onError:function(){if(++hata>=2||!oynadi){birak();return;}gec();}}});};}
function dene(){if(etk&&(gor||yakin))kur();}
if('IntersectionObserver' in w){new IntersectionObserver(function(es){gor=es[0].isIntersecting;if(pl&&hazir){try{gor||yakin?pl.playVideo():(sesli||pl.pauseVideo())}catch(e){}}dene();},{threshold:.35}).observe(ekr);
 new IntersectionObserver(function(es){yakin=es[0].isIntersecting;dene();},{rootMargin:'0px 0px 900px 0px'}).observe(ekr);}
['scroll','touchstart','pointerdown','keydown','mousemove','wheel'].forEach(function(ev){w.addEventListener(ev,function(){if(!etk){etk=true;dene();}},{passive:true,once:true})});
akis();isaret();
ses.addEventListener('click',function(){if(!pl)return;if(sesli){sesli=false;try{pl.mute()}catch(e){}basla=Date.now();ses.textContent='🔊 Sesi aç';ses.setAttribute('aria-pressed','false');return;}
 sesli=true;try{pl.unMute();pl.setVolume(100);pl.playVideo()}catch(e){}ses.textContent='🔇 Sesi kapat';ses.setAttribute('aria-pressed','true');});
btn.forEach(function(b){b.addEventListener('click',function(){var n=+b.getAttribute('data-bd-no');if(!etk){etk=true;dene();}
 if(pl&&hazir){gec(n);}else{if(tm){clearInterval(tm);tm=null}kare(n);akis();}
 var r=ekr.getBoundingClientRect();if(r.top<0||r.bottom>innerHeight)ekr.scrollIntoView({behavior:az?'auto':'smooth',block:'center'});});});
})();</script>'''


def on_sayfa(vids, news, logo_yol='/assets/basin/logo/', btn_call='', btn_wa=''):
    """vids: [(id, kanal, başlık)], news: [(yayın, başlık, url)]"""
    M = [{'t': t, 'o': EK.get(o, o) + ' yayımlandı', 'u': u} for o, t, u in news]
    kanal = [{'y': v, 'k': k, 'b': t, 't': 45} for v, k, t in vids]
    kareler = ''.join('<img class="bd-k%s" src="/assets/basin/video-%s.webp" alt="" width="640" height="360" %s decoding="async">' % (
        ' on' if j == 0 else '', v, 'fetchpriority="low"' if j == 0 else 'loading="lazy"') for j, (v, k, t) in enumerate(vids))
    akis = ''.join('<li><button type="button" data-bd-no="%d"><span>%02d</span>%s · %s</button></li>' % (j, j + 1, E(k), E(t)) for j, (v, k, t) in enumerate(vids))
    say = ''.join('<div><b>%d</b>%s</div>' % (n, E(t)) for n, t in SAYAC)
    lg = ''.join('<li><img src="%s%s.webp" alt="%s" width="%d" height="%d" loading="lazy" decoding="async"></li>' % (logo_yol, k, E(a), w_, h) for a, k, w_, h in LOGO)
    lg2 = lg.replace('alt="', 'aria-hidden="true" alt="" data-a="')  # ikinci kopya yalnızca kesintisiz kayma için
    ilk = M[0]
    return CSS + ('<section class="bd-on" aria-label="Basın dosyası">'
        '<div class="bd-ust"><span>RN Psikoloji · Çayyolu</span><span>Basın dosyası</span></div>'
        '<p class="bd-bas">Ekranda ve Gazetelerde</p>'
        '<div class="bd-alt"><span>Kurucumuz Psikolog Rojin Nazik</span><span>13 yıl deneyim</span><span>3 kitap</span></div>'
        '<p class="bd-ms"><b>MANŞET</b><a href="%s" target="_blank" rel="noopener" data-m="%s">%s<small>%s</small></a></p>'
        '<div class="bd-iki"><div class="bd-mon" data-kanal="%s"><div class="bd-ekr">%s<div class="bd-yt"></div><div class="bd-kar"></div>'
        '<span class="bd-bug"><i></i>YAYINDA</span><button class="bd-ses" type="button" hidden aria-pressed="false">🔊 Sesi aç</button>'
        '</div><div class="bd-ayak"></div><p class="bd-alt2" aria-live="off"><b></b><span></span></p></div>'
        '<div class="bd-akis"><h3>Yayın listesi</h3><ol>%s</ol></div></div>'
        '<div class="bd-say" aria-label="Basın sayıları">%s</div>'
        '<div class="bd-lg"><ul aria-label="Yer aldığı yayınlar">%s%s</ul></div>'
        '<div class="bd-cta"><p>Bu yayınlarda konuşan kurucumuzun ekibiyle Yaşamkent ofisimizde görüşebilirsiniz.</p>%s%s</div>'
        '</section>') % (E(ilk['u']), E(json.dumps(M, ensure_ascii=False)), E(ilk['t']), E(ilk['o']), E(json.dumps(kanal, ensure_ascii=False)),
                         kareler, akis, say, lg, lg2, btn_call, btn_wa)


def ipucu(n):
    return '<p class="bd-ipu" aria-hidden="true"><span>Sağa kaydırın <i>→</i></span><em>1 / %d</em></p>' % n


def orta_cta(btn_call, btn_wa):
    return ('<aside class="bd-orta"><b>Randevu</b><p>Gazetelerde anlatılan konular sizin de gündeminizdeyse, ilk adımı telefonla atabilirsiniz.</p>'
            '<div class="btn-row">%s%s</div></aside>') % (btn_call, btn_wa)


JS_SON = JS
