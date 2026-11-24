# -*- coding: utf-8 -*-
"""KIŞ 2027 mevsim kapısı (dört sitede ortak, görünmeyen teknik katman).
Ayar: mevsim-ayar.json → {"mod": "otomatik|acik|kapali", "baslangic": ISO+03:00, "bitis": ISO+03:00}
<head> içine en başta eklenen küçük betik, tarih aralığındaysa <html class="k27"> verir (boyamadan önce: titreme yok).
Önbellekteki eski HTML de 11 Ocak 00:00 TR'de kendiliğinden kapanır (karar ziyaretçinin tarayıcısında, saat dilimi ofsetli).
Önizleme: ?kis27=1 / ?kis27=0 (yalnız o sekme için, sessionStorage). Mevsim öğeleri: .k27-y (yalnız temada), .k27-g (temada gizli)."""
import json, os


def oku(yol):
    a = json.load(open(yol, encoding='utf-8'))
    assert a['mod'] in ('otomatik', 'acik', 'kapali'), a['mod']
    for k in ('baslangic', 'bitis'):
        assert a[k].endswith('+03:00'), k
    return a


def kapi(a, onyukle=None):
    """onyukle: [(href, media[, imagesrcset, imagesizes])] — tema açıkken ilk ekran mevsim görselini erken indir (kapalıyken hiç istenmez)."""
    pre = ''
    if onyukle:
        pre = ('var P=%s;for(var i=0;i<P.length;i++){var l=d.createElement("link");l.rel="preload";l.as="image";l.href=P[i][0];l.media=P[i][1];if(P[i][2]){l.setAttribute("imagesrcset",P[i][2]);l.setAttribute("imagesizes",P[i][3]||"100vw")}l.setAttribute("fetchpriority","high");d.head.appendChild(l)}'
               % json.dumps([list(x) for x in onyukle]))
    js = ('(function(d){var A=%s,n=Date.now(),on=A.mod==="acik"||(A.mod==="otomatik"&&n>=Date.parse(A.baslangic)&&n<Date.parse(A.bitis));'
          'try{var q=/[?&]kis27=([01])/.exec(location.search);if(q){on=q[1]==="1";sessionStorage.setItem("kis27",q[1])}else{var s=sessionStorage.getItem("kis27");if(s)on=s==="1"}}catch(e){}'
          'if(on){d.documentElement.classList.add("k27");%s}})(document)') % (json.dumps({'mod': a['mod'], 'baslangic': a['baslangic'], 'bitis': a['bitis']}), pre)
    return ('<script id="kis27-kapi">%s</script><style id="kis27-temel">html:not(.k27) .k27-y{display:none!important}html.k27 .k27-g{display:none!important}</style>' % js)
