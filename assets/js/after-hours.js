/* Mesai dışı yakalama: Pazartesi–Cumartesi 09:00–20:00 (İstanbul) dışında
   "Sabah ilk sizi arayalım" düğmesi gösterir; tıklanınca hazır WhatsApp mesajı açılır.
   Üç sitede ortak dosya. */
(function () {
  var WA = '905524187973';
  var POS = (document.currentScript && document.currentScript.getAttribute('data-pos')) || 'top';
  var day, mins;
  try {
    var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Istanbul', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    var get = function (t) { for (var i = 0; i < parts.length; i++) if (parts[i].type === t) return parts[i].value; return ''; };
    day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(get('weekday'));
    mins = (parseInt(get('hour'), 10) % 24) * 60 + parseInt(get('minute'), 10);
  } catch (e) { return; }
  var open = day >= 1 && day <= 6 && mins >= 540 && mins < 1200;
  if (open) return;

  // Ne zaman aranacağı: akşam/gece ise "yarın sabah", Cumartesi akşamı ve Pazar "Pazartesi sabahı"
  var when = 'sabah';
  if ((day === 6 && mins >= 1200) || day === 0) when = 'Pazartesi sabahı';
  else if (mins < 540) when = 'bu sabah';
  var msg = 'Merhaba, mesai dışında yazıyorum. ' + (when === 'Pazartesi sabahı' ? 'Pazartesi sabahı' : 'Sabah') + ' aranmak istiyorum. Konu: ';
  var href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);

  var css = '.ah-bar{position:relative;z-index:40;background:#14264A;color:#fff;font:600 14.5px/1.35 system-ui,-apple-system,"Segoe UI",sans-serif;padding:9px 44px 9px 14px;text-align:center}'
    + '.ah-bar a{color:#fff;text-decoration:none;display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center}'
    + '.ah-bar b{background:#17A34A;border-radius:999px;padding:5px 12px;white-space:nowrap}'
    + '.ah-bar button{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:none;border:0;color:#fff;font-size:20px;line-height:1;cursor:pointer;padding:6px;opacity:.75}'
    + '.ah-bar.ah-bottom{position:fixed;left:12px;right:84px;bottom:calc(86px + env(safe-area-inset-bottom));z-index:9998;border-radius:16px;box-shadow:0 10px 30px -10px rgba(0,0,0,.45);padding:10px 40px 10px 12px;font-size:13.5px}'
    + '@media(min-width:861px){.ah-bar.ah-bottom{left:24px;right:auto;bottom:24px;max-width:430px}}'
    + '.ah-inline{display:inline-flex;align-items:center;gap:8px;margin-top:10px;padding:10px 16px;border-radius:999px;background:#17A34A;color:#fff!important;font:700 15px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif;text-decoration:none}'
    + '.ah-inline:hover{filter:brightness(.95)}';

  function wa(label, cls, area) {
    var a = document.createElement('a');
    a.href = href; a.target = '_blank'; a.rel = 'noopener';
    if (cls) a.className = cls;
    a.setAttribute('data-cta-area', area);
    a.innerHTML = label;
    return a;
  }

  function init() {
    var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    var dismissed = false;
    try { dismissed = sessionStorage.getItem('ah_kapat') === '1'; } catch (e) {}
    if (!dismissed) {
      var bar = document.createElement('div'); bar.className = 'ah-bar' + (POS === 'bottom' ? ' ah-bottom' : ''); bar.setAttribute('role', 'note');
      bar.appendChild(wa('<span>🌙 Şu an mesai dışındayız.</span><b>' + (when === 'Pazartesi sabahı' ? 'Pazartesi' : 'Sabah') + ' ilk sizi arayalım →</b>', '', 'after_hours_bar'));
      var x = document.createElement('button'); x.type = 'button'; x.setAttribute('aria-label', 'Kapat'); x.innerHTML = '×';
      x.onclick = function () { bar.parentNode && bar.parentNode.removeChild(bar); try { sessionStorage.setItem('ah_kapat', '1'); } catch (e) {} };
      bar.appendChild(x);
      if (POS === 'bottom') document.body.appendChild(bar); else document.body.insertBefore(bar, document.body.firstChild);
    }
    // "Açık / kapalı" yazan alanların altına düğme
    var spots = document.querySelectorAll('[data-open-status]');
    for (var i = 0; i < spots.length; i++) {
      if (spots[i].nextElementSibling && spots[i].nextElementSibling.classList && spots[i].nextElementSibling.classList.contains('ah-inline')) continue;
      spots[i].parentNode.insertBefore(wa('💬 ' + (when === 'Pazartesi sabahı' ? 'Pazartesi' : 'Sabah') + ' ilk sizi arayalım', 'ah-inline', 'after_hours_inline'), spots[i].nextSibling);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
