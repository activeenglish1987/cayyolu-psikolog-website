# -*- coding: utf-8 -*-
"""Ofis fotoğraf galerisi (Çayyolu dili): masaüstünde dergi düzeni (büyük kapak + küçükler), telefonda kaydırmalı kartlar,
dokununca açık renkli tam ekran görüntüleyici. Görseller /assets/ofis/ altında 480/900/1400 webp; ekrana yaklaşınca yüklenir."""
import html
E = lambda s: html.escape(s, quote=True)
META = {"salon-manzara": {"w": 1500, "h": 2000, "lq": "data:image/webp;base64,UklGRqYAAABXRUJQVlA4IJoAAACQBQCdASoYACAAPu1mqU2ppiQiMBgMATAdiWUArj1DxCxgS7XsXeOALpK9aqC06/q8+iXAAAD43QsdHQL7RkLecmZkGB+sqxOBg2hCD0nKKkQTE+ENB7dYJ+cegDiS1WtRFfn/QAxi18tMnRpkEZNmcOYWN4uZFY8us2PYbRjimrHZdYPZzAqQ+sOZJwvA/ibQJWrqN1ldJAAA"}, "salon-karsi": {"w": 1040, "h": 1550, "lq": "data:image/webp;base64,UklGRsQAAABXRUJQVlA4ILgAAABwBgCdASoYACQAPuFepU2opSOiNVgMARAcCUAXZli3v5ITZjY9SmDerdPk7CRftB4HktuS1IK5JzAsFTAA+8yKsQvbRMtCljPevZkTkI1z37ihpNIH8FgB15CH2nfsr+pxaMMW1vT6WYExlrjAw4vTwuk7Ee7aAHWQ4jy8lfX3jEkZQ5aZmnJ/WMxgMqgQVtt16mF4B2XutOcKx+S1LdERWzq2evqT57orwyknm/5SgrIDlTnwAAAA"}, "bekleme-koridor": {"w": 1500, "h": 2000, "lq": "data:image/webp;base64,UklGRpoAAABXRUJQVlA4II4AAACQBQCdASoYACAAPt1epU2opaOiN/qoARAbiUATpnHYY7i+7n55jG3uB2NqM1sTVJJlVDxlIAD+sHFBIxAJ5LLKsiu7fLakfim+1ZsL9QWPz0ZofzVwdFdjkZihCs+ynV4JwVYVbXstVP8YRqmA6h9mZSLJ78HRN1kSNHXGzAA4fXi6yLyMZflZpnwuAAAA"}, "salon-giris": {"w": 980, "h": 1300, "lq": "data:image/webp;base64,UklGRqYAAABXRUJQVlA4IJoAAADQBQCdASoYACAAPu1orVCppaQiqAqpMB2JZQDLLGmgYl6n9IfPu8s/ZJt3JULtUJg3IDC/yQgAAP7IsahSX3oZ6yLX5k1W4Z5bVODg2BCZcq538r9r8OU5CrNETeVyQVkeyY/u92of3LCTtiUcpb+Phc8x7n/jm7USNncRv90ymE+O1LeJ9s/xI1sdbqG1+OBwXEXQ2ukUhAAA"}, "gorusme-yesil": {"w": 1500, "h": 2000, "lq": "data:image/webp;base64,UklGRqQAAABXRUJQVlA4IJgAAADwBQCdASoYACAAPuFep02opSOiMAwBEBwJZACdMzL6ALoI4zWss6KqD+1OqyOTGwd58Vdl20y2AAD3BGcMmJRgMZTWDWAXlQ08gPipdYBRBnAU8kk3VMYCu6dqXNcd9fLWO+RLOMhsrhiJNPwIi27y3hxxf4jnis7Unw2TJF3sZaQZ2EUAtEyokgLp0mAkjnK0iVne3IAAAA=="}, "gorusme-yesil-genis": {"w": 1230, "h": 1780, "lq": "data:image/webp;base64,UklGRq4AAABXRUJQVlA4IKIAAADwBQCdASoYACMAPu1oqk6ppiOiKqwBMB2JYgCdMwTGd/oHlRgXAGnJxvsceEZieciz6H16CvV5yADLDmmczncBkGhH0i5ey1MZKhuTWZGVx9U3nEqQAvZXGY3kk8uPvU0VeicMJfFr9V7xJVxVPg9sGZp2NSw4NLv/G9IsPgEoIMjBlHN4ZHTIysvE2zrd7S6MsXCHx7QofXXThhrzYyOsAAA="}, "gorusme-krem": {"w": 1500, "h": 2000, "lq": "data:image/webp;base64,UklGRpYAAABXRUJQVlA4IIoAAABwBQCdASoYACAAPt1apk2opSOiN/qoARAbiWIAqSPAgZgLfW8+49tHBgCnbQ2XgdO7LO8AAP7cV5mHG8EVZOSqH0UgS0rf8GOoXCMY0aTqXHjSNdTwtU88ukVVIN5m19xJXCxU+uyDZbjzewda6pFLIpj2RLOh8ODv1nAYBcUCgK/L0cb0pCAAAAA="}, "ikram-kosesi": {"w": 1130, "h": 1700, "lq": "data:image/webp;base64,UklGRq4AAABXRUJQVlA4IKIAAABwBgCdASoYACQAPu1gqU6ppSOiNVQIATAdiWUAzNA7ehAH4I52wnzpAYLO8QGlF+FofXPjUf2J8q30+YAA/n6ilVLZtXiVbJ3GEZO3Xv34vXqXZuDh4afONGIo6/V4704ZxB12s7YvaxXCdGEheaR8I2itxspRBbdqwylmxvCPaC7Oz6EgQpSBg0mLSs5F2j5PJXLC2W3GpsTCcuQFSCWAAAA="}, "detay-masa": {"w": 1500, "h": 1700, "lq": "data:image/webp;base64,UklGRpQAAABXRUJQVlA4IIgAAABwBQCdASoYABsAPuFeqU2opSQiMAwBEBwJaACdOUAAm3un3JhduWIp2Ylx116RwGFz6GBgAPzUB4mdoXD1l3dDJAef5kdI7oMmrMjKkhkkSpTUBzRx8TGX7EMv12xSPR+8HsXxO8RNAVYLnSvti73yrgzxNi0HZlHelcWwSdSOjacbsaW6cAAA"}}
FOTO = [('salon-manzara', 'Salon', 'Ankara manzarasına açılan geniş pencereler', 'RN Psikoloji ofisinde manzaralı salon'),
        ('bekleme-koridor', 'Bekleme alanı', 'Sakin, aydınlık bir karşılama', 'RN Psikoloji ofisinde bekleme alanı'),
        ('gorusme-yesil', 'Görüşme odası', 'Sıcak ışık, rahat oturma', 'RN Psikoloji ofisinde görüşme odası'),
        ('gorusme-krem', 'Görüşme odası', 'Yumuşak tonlar, sessiz bir ortam', 'RN Psikoloji ofisinde krem tonlarında görüşme odası'),
        ('salon-karsi', 'Salon', 'Tanışma ve bekleme alanı', 'RN Psikoloji ofisinde salon'),
        ('ikram-kosesi', 'İkram köşesi', 'Çay, kahve ve su', 'RN Psikoloji ofisinde ikram köşesi'),
        ('detay-masa', 'Ayrıntılar', 'Görüşme odasından bir köşe', 'Görüşme odasında masa üzerinde dergiler ve kuru çiçekler')]

CSS = """<style>
.cg{margin:6px 0 4px}
.cg-ust{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:4px 12px;margin-bottom:14px}
.cg-ust p{margin:0;color:#5b6577;font-size:14.5px;line-height:1.5}
.cg-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:170px;gap:12px}
.cg-k{position:relative;margin:0;border-radius:14px;overflow:hidden;background:#EEF2F8 var(--lq) center/cover;box-shadow:0 1px 0 #fff inset,0 14px 30px -20px rgba(20,38,74,.55)}
.cg-k:first-child{grid-column:span 2;grid-row:span 2}
.cg-k:nth-child(4){grid-row:span 2}
.cg-k button{all:unset;position:absolute;inset:0;cursor:zoom-in;display:block}
.cg-k button:focus-visible{outline:3px solid #E8A33D;outline-offset:-3px;border-radius:14px}
.cg-k img{width:100%;height:100%;object-fit:cover;display:block;opacity:0;transition:opacity .6s,transform .6s}
.cg-k img.cg-y{opacity:1}
.cg-k button:hover img.cg-y{transform:scale(1.04)}
.cg-k figcaption{position:absolute;left:10px;bottom:10px;right:10px;display:flex;align-items:center;gap:8px;pointer-events:none}
.cg-k figcaption b{display:grid;place-items:center;width:26px;height:26px;border-radius:7px;background:#E8A33D;color:#14264A;font-size:12.5px;flex:none}
.cg-k figcaption span{background:rgba(255,255,255,.94);color:#14264A;font-weight:700;font-size:13px;padding:5px 9px;border-radius:7px;box-shadow:0 6px 16px -10px rgba(20,38,74,.6);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cg-say{display:none}
@media(max-width:759px){
 .cg-grid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;gap:10px;margin:0 -16px;padding:2px 16px 6px;scroll-padding-inline:16px}
 .cg-grid::-webkit-scrollbar{display:none}
 .cg-k,.cg-k:first-child,.cg-k:nth-child(4){flex:0 0 84%;aspect-ratio:4/5;grid-column:auto;grid-row:auto;scroll-snap-align:center}
 .cg-say{display:flex;justify-content:center;gap:6px;margin-top:10px}
 .cg-say i{width:7px;height:7px;border-radius:50%;background:#C9D3E6;transition:all .25s}
 .cg-say i.on{width:20px;border-radius:4px;background:#14264A}
}
.cg-l{position:fixed;inset:0;z-index:99999;background:rgba(246,241,230,.97);display:flex;align-items:center;justify-content:center;padding:58px 12px 70px;opacity:0;pointer-events:none;transition:opacity .25s}
.cg-l.on{opacity:1;pointer-events:auto}
.cg-l figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:12px;max-width:min(1100px,100%)}
.cg-l img{max-width:100%;max-height:calc(100vh - 150px);max-height:calc(100dvh - 150px);object-fit:contain;border-radius:10px;box-shadow:0 30px 60px -30px rgba(20,38,74,.6);background:#fff;padding:6px}
.cg-l figcaption{color:#14264A;font-weight:700;font-size:15px;text-align:center}
.cg-l figcaption small{display:block;font-weight:500;color:#5b6577;margin-top:2px}
.cg-l button{all:unset;cursor:pointer;position:absolute;display:grid;place-items:center;width:46px;height:46px;border-radius:12px;background:#14264A;color:#fff;font-size:24px}
.cg-l button:focus-visible{outline:3px solid #E8A33D;outline-offset:2px}
.cg-l .cg-x{top:10px;right:10px}.cg-l .cg-o1{left:12px;top:50%;margin-top:-23px}.cg-l .cg-o2{right:12px;top:50%;margin-top:-23px}
.cg-n{position:absolute;top:22px;left:16px;font-weight:800;color:#14264A;font-size:13px;letter-spacing:.08em}
@media(max-width:700px){.cg-l .cg-o1,.cg-l .cg-o2{top:auto;bottom:12px;margin-top:0}.cg-l .cg-o1{left:calc(50% - 56px)}.cg-l .cg-o2{right:calc(50% - 56px)}}
html.cg-acik{overflow:hidden}html.cg-acik .bar,html.cg-acik .sticky-bar{visibility:hidden}
@media (prefers-reduced-motion:reduce){.cg-k img{transition:none}.cg-k button:hover img.cg-y{transform:none}}
</style>"""

JS = """<script>(function(){var d=document,w=window,R=d.querySelector('[data-cg]');if(!R)return;var K=[].slice.call(R.querySelectorAll('.cg-k')),n=K.length,G=R.querySelector('.cg-grid'),D=[].slice.call(R.querySelectorAll('.cg-say i')),L=null,li=0;
K.forEach(function(k){var im=k.querySelector('img');function y(){im.classList.add('cg-y')}if(im.complete&&im.naturalWidth)y();else im.addEventListener('load',y)});
function nok(){if(!D.length)return;var c=G.getBoundingClientRect(),m=c.left+c.width/2,b=0,bd=1e9;K.forEach(function(k,i){var r=k.getBoundingClientRect(),x=Math.abs(r.left+r.width/2-m);if(x<bd){bd=x;b=i}});D.forEach(function(e,i){e.classList.toggle('on',i===b)})}
var rq=0;G.addEventListener('scroll',function(){if(!rq){rq=1;w.requestAnimationFrame(function(){rq=0;nok()})}},{passive:true});nok();
function p2(x){return(x<9?'0':'')+(x+1)}
function gos(i){li=(i+n)%n;var k=K[li],im=k.querySelector('img'),b=L.querySelector('img');b.src=im.getAttribute('data-big');b.alt=im.alt;L.querySelector('figcaption').innerHTML='';var t=d.createElement('span');t.textContent=k.getAttribute('data-b');var s=d.createElement('small');s.textContent=k.getAttribute('data-k');L.querySelector('figcaption').appendChild(t);L.querySelector('figcaption').appendChild(s);L.querySelector('.cg-n').textContent=p2(li)+' / '+p2(n-1);var nx=new Image();nx.src=K[(li+1)%n].querySelector('img').getAttribute('data-big')}
function kap(){L.classList.remove('on');d.documentElement.classList.remove('cg-acik');var b=K[li].querySelector('button');if(b)b.focus({preventScroll:true})}
function ac(i){if(!L){L=d.createElement('div');L.className='cg-l';L.setAttribute('role','dialog');L.setAttribute('aria-modal','true');L.setAttribute('aria-label','Ofis fotoğrafları');L.innerHTML='<span class="cg-n"></span><button class="cg-x" type="button" aria-label="Kapat">×</button><button class="cg-o1" type="button" aria-label="Önceki">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="cg-o2" type="button" aria-label="Sonraki">›</button>';d.body.appendChild(L);
 L.querySelector('.cg-x').addEventListener('click',kap);L.querySelector('.cg-o1').addEventListener('click',function(){gos(li-1)});L.querySelector('.cg-o2').addEventListener('click',function(){gos(li+1)});L.addEventListener('click',function(e){if(e.target===L||e.target.tagName==='FIGURE')kap()});
 var sx=0,sy=0;L.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;sy=e.touches[0].clientY},{passive:true});L.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx,dy=e.changedTouches[0].clientY-sy;if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy))gos(li+(dx<0?1:-1));else if(dy>90)kap()},{passive:true});
 d.addEventListener('keydown',function(e){if(!L.classList.contains('on'))return;if(e.key==='Escape')kap();else if(e.key==='ArrowRight')gos(li+1);else if(e.key==='ArrowLeft')gos(li-1)});}
 gos(i);L.classList.add('on');d.documentElement.classList.add('cg-acik');L.querySelector('.cg-x').focus({preventScroll:true});(w.dataLayer=w.dataLayer||[]).push({event:'ofis_foto_ac',foto:i+1})}
K.forEach(function(k,i){k.querySelector('button').addEventListener('click',function(){ac(i)})});})();</script>"""


def galeri(baslik='Ofisimizden kareler', alt='Fotoğrafa dokunup büyütebilirsiniz.', h='h2'):
    ks = []
    for i, (ad, b, k, a) in enumerate(FOTO):
        m = META[ad]; p = '/assets/ofis/' + ad
        ks.append('<figure class="cg-k" style="--lq:url(%s)" data-b="%s" data-k="%s"><button type="button" aria-label="Büyüt: %s – %s">'
                  '<img src="%s-900.webp" srcset="%s-480.webp 480w, %s-900.webp 900w, %s-1400.webp 1400w" sizes="(max-width: 759px) 84vw, %s" '
                  'width="%d" height="%d" alt="%s" loading="lazy" decoding="async" data-big="%s-1400.webp"></button>'
                  '<figcaption><b>%d</b><span>%s</span></figcaption></figure>' % (
                      m['lq'], E(b), E(k), E(b), E(k), p, p, p, p, '50vw' if i == 0 else '25vw', m['w'], m['h'], E(a), p, i + 1, E(b)))
    return (CSS + '<div class="cg" data-cg><div class="cg-ust"><%s style="margin:0">%s</%s><p>%s</p></div><div class="cg-grid" role="group" aria-label="Ofis fotoğrafları">%s</div>'
            '<div class="cg-say" aria-hidden="true">%s</div></div>' % (h, E(baslik), h, E(alt), ''.join(ks), '<i></i>' * len(FOTO)) + JS)
