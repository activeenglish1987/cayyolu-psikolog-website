# -*- coding: utf-8 -*-
"""Premium yeni yıl (25 Kas 2026, kullanıcı onayı): efektsiz. İnce koyu üst şerit + altın harf aralıklı 'MUTLU YILLAR ✦ 2027'
+ altın çerçeveli kadife davet kartı (gerçek çam/ışık fotoğrafı). 11 Ocak 2027'den sonra tarayıcıda gizlenir."""
SON = 'Date.UTC(2027,0,10,21)'

def css(zemin, zemin2, altin, yazi, foto, sabit=False, cizgi=None):
    cizgi = cizgi or altin
    return ('<style>'
     '.yy-bar{position:%s;top:0;left:0;right:0;z-index:70;display:flex;align-items:center;justify-content:center;gap:22px;min-height:42px;padding:6px 44px;'
     'background:%s;border-bottom:1px solid %s;font-family:"Playfair Display",Georgia,"Times New Roman",serif;color:%s;box-sizing:border-box}'
     '.yy-bar .t{font-size:12.5px;letter-spacing:.42em;text-transform:uppercase;white-space:nowrap}.yy-bar .t i{font-style:normal;color:%s;margin:0 .55em}'
     '.yy-bar a{font-size:13px;letter-spacing:.05em;color:%s;text-decoration:none;border-bottom:1px solid %s;padding-bottom:1px;white-space:nowrap}'
     '.yy-bar button{position:absolute;right:10px;top:50%%;transform:translateY(-50%%);width:28px;height:28px;border:0;background:transparent;color:%s;font-size:18px;cursor:pointer;opacity:.75;padding:0}'
     '.yy-pk{display:flex;align-items:stretch;max-width:540px;margin:24px 0 8px;background:linear-gradient(135deg,%s,%s);border:1px solid %s;border-radius:4px;overflow:hidden;'
     'box-shadow:0 24px 50px -28px rgba(0,0,0,.85);text-align:left}'
     '.yy-pk .f{flex:none;width:128px;background:%s center/cover no-repeat;position:relative}html.yy-hazir .yy-pk .f{background-image:url(%s)}'
     '.yy-pk .f:after{content:"";position:absolute;inset:0;box-shadow:inset -18px 0 22px -8px %s}'
     '.yy-pk .m{padding:16px 20px 16px 18px}.yy-pk .k{font-family:"Playfair Display",Georgia,serif;font-size:11px;letter-spacing:.38em;text-transform:uppercase;color:%s}'
     '.yy-pk .h{display:block;margin:6px 0 4px;font-family:"Playfair Display",Georgia,serif;font-weight:500;font-size:22px;line-height:1.25;color:%s}'
     '.yy-pk p{margin:0 0 12px;font-size:14px;line-height:1.55;color:%s;opacity:.8}'
     '.yy-pk a{display:inline-block;padding:8px 18px;border:1px solid %s;color:%s;text-decoration:none;font-size:13px;letter-spacing:.12em;text-transform:uppercase;border-radius:2px;transition:background .2s,color .2s}'
     '.yy-pk a:hover{background:%s;color:%s}'
     '@media(max-width:640px){.yy-bar{gap:12px;padding:6px 36px 6px 12px}.yy-bar .t{font-size:10.5px;letter-spacing:.28em}.yy-bar a{font-size:12px}'
     '.yy-pk .f{width:92px}.yy-pk .h{font-size:19px}.yy-pk p{font-size:13.5px}.yy-pk .m{padding:14px 16px}}'
     '</style><script>if(Date.now()<%s)addEventListener("load",function(){setTimeout(function(){document.documentElement.classList.add("yy-hazir")},200)})</script>') % (
     'fixed' if sabit else 'relative', zemin, cizgi, yazi, altin, yazi, altin, yazi,
     zemin2, zemin, cizgi, zemin2, foto, zemin, altin, yazi, yazi, altin, yazi, altin, zemin, SON)

def bar(baslik, link_metin, wa):
    return ('<div class="yy-bar" role="region" aria-label="Yeni yıl"><span class="t">%s</span>'
            '<a href="https://wa.me/905524187973?text=%s" target="_blank" rel="noopener">%s</a>'
            '<button type="button" aria-label="Kapat" onclick="this.parentNode.remove();document.documentElement.classList.remove(\'yy-acik\');try{sessionStorage.setItem(\'yy\',\'1\')}catch(e){}">×</button></div>'
            '<script>(function(){var b=document.currentScript.previousElementSibling,k=Date.now()>%s;try{k=k||!!sessionStorage.getItem("yy")}catch(e){}if(k)b.remove()})()</script>') % (baslik, wa, link_metin, SON)

def kart(ust, baslik, metin, btn, wa):
    return ('<div class="yy-pk"><div class="f" aria-hidden="true"></div><div class="m"><div class="k">%s</div><span class="h">%s</span><p>%s</p>'
            '<a href="https://wa.me/905524187973?text=%s" target="_blank" rel="noopener">%s</a></div></div>'
            '<script>(function(){if(Date.now()>%s){var k=document.currentScript.previousElementSibling;k&&k.remove()}})()</script>') % (ust, baslik, metin, wa, btn, SON)
