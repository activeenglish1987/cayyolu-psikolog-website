/* Mesai dışı yakalama: Pazartesi–Cumartesi 09:00–20:00 (İstanbul) dışında
   "Sabah Selda Hanım sizi arasın" düğmesi gösterir. Tıklanınca küçük bir pencere açılır:
   ziyaretçi cep numarasını bırakır, talep reklam kimliğiyle (gclid) birlikte psikologunubul
   panelindeki talepler listesine düşer ve sabah ilk iş aranır. WhatsApp ikinci seçenek olarak kalır.
   Rojin Nazik ve Çayyolu sitelerinde ortak dosya (Elif sitesinde eski sürüm). */
(function () {
  var WA = '905524187973';
  var API = 'https://www.psikologunubul.com.tr/api/talep';
  var AYDINLATMA = 'https://www.psikologunubul.com.tr/kvkk-aydinlatma';
  var SITE = /cayyolu/.test(location.hostname) ? 'cayyolu' : 'rojin';
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
  var kisa = when === 'Pazartesi sabahı' ? 'Pazartesi' : 'Sabah';
  // Panelde arama hatırlatması bu saate kurulur (psikologunubul lib/hours.ts callbackAtFrom)
  var saat = when === 'Pazartesi sabahı' ? 'Pazartesi 09:00' : when === 'bu sabah' ? 'Bugün 09:00' : 'Yarın 09:00';
  var msg = 'Merhaba, mesai dışında yazıyorum. ' + kisa + ' aranmak istiyorum. Konu: ';
  var waHref = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);

  var css = '.ah-bar{position:relative;z-index:40;background:#14264A;color:#fff;font:600 14.5px/1.35 system-ui,-apple-system,"Segoe UI",sans-serif;padding:9px 44px 9px 14px;text-align:center}'
    + '.ah-bar .ah-go{color:#fff;background:none;border:0;font:inherit;cursor:pointer;display:inline-flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center;padding:0}'
    + '.ah-bar b{background:#17A34A;border-radius:999px;padding:5px 12px;white-space:nowrap}'
    + '.ah-bar .ah-x{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:none;border:0;color:#fff;font-size:20px;line-height:1;cursor:pointer;padding:6px;opacity:.75}'
    + '.ah-bar.ah-bottom{position:fixed;left:12px;right:84px;bottom:calc(86px + env(safe-area-inset-bottom));z-index:9998;border-radius:16px;box-shadow:0 10px 30px -10px rgba(0,0,0,.45);padding:10px 40px 10px 12px;font-size:13.5px}'
    + '@media(min-width:861px){.ah-bar.ah-bottom{left:24px;right:auto;bottom:24px;max-width:430px}}'
    + '.ah-inline{display:inline-flex;align-items:center;gap:8px;margin-top:10px;padding:10px 16px;border-radius:999px;border:0;cursor:pointer;background:#17A34A;color:#fff!important;font:700 15px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif;text-decoration:none}'
    + '.ah-inline:hover{filter:brightness(.95)}'
    + '.ah-sheet{position:fixed;inset:0;z-index:2147483001;display:flex;align-items:flex-end;justify-content:center;background:rgba(18,12,24,.55);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:#18223A}'
    + '@media(min-width:700px){.ah-sheet{align-items:center}}'
    + '.ah-card{position:relative;width:100%;max-width:440px;background:#fff;border-radius:24px 24px 0 0;padding:22px 20px calc(20px + env(safe-area-inset-bottom));box-shadow:0 -16px 50px rgba(0,0,0,.25)}'
    + '@media(min-width:700px){.ah-card{border-radius:24px}}'
    + '.ah-card h3{margin:0 40px 6px 0;font-size:21px;line-height:1.25;color:#14264A}'
    + '.ah-card p{margin:0 0 14px;color:#566179}'
    + '.ah-card .ah-x{position:absolute;right:14px;top:14px;width:36px;height:36px;border-radius:50%;border:1px solid #DCE4F0;background:#fff;font-size:20px;cursor:pointer;color:#18223A}'
    + '.ah-who{display:flex;align-items:center;gap:12px;margin:0 0 14px;padding:10px 12px;border-radius:14px;background:#F2F6FB}'
    + '.ah-who i{width:40px;height:40px;border-radius:50%;flex:none;display:grid;place-items:center;font-style:normal;font-weight:800;color:#fff;background:linear-gradient(135deg,#6B3A8C,#C9A06B)}'
    + '.ah-card input{width:100%;box-sizing:border-box;padding:15px 16px;border-radius:14px;border:1.5px solid #DCE4F0;font:600 18px/1.2 inherit;letter-spacing:.02em;outline:none}'
    + '.ah-card input:focus{border-color:#17A34A}'
    + '.ah-send{width:100%;margin-top:10px;padding:16px;border-radius:14px;border:0;background:#17A34A;color:#fff;font:800 17px/1.2 inherit;cursor:pointer}'
    + '.ah-send[disabled]{opacity:.6}'
    + '.ah-small{font-size:12.5px;color:#566179;margin-top:10px}.ah-small a{color:#566179}'
    + '.ah-err{color:#B42318;font-size:14px;margin-top:8px;min-height:1px}'
    + '.ah-card a.ah-wa[href]{display:block;text-align:center;margin-top:12px;padding:0!important;border:0!important;box-shadow:none!important;font-size:14px;font-weight:600;color:#566179!important;background:none!important;text-decoration:underline}'
    + '.ah-ok{text-align:center;padding:10px 0 4px}.ah-ok b{display:block;font-size:20px;color:#14264A;margin:8px 0 6px}';

  function track(ev, extra) {
    window.dataLayer = window.dataLayer || [];
    var p = { event: ev, cta_area: 'after_hours', page_path: location.pathname, site: SITE };
    if (extra) for (var k in extra) p[k] = extra[k];
    window.dataLayer.push(p);
  }

  function attribution() {
    var a = {};
    try { a = JSON.parse(localStorage.getItem('ads_attribution') || '{}') || {}; } catch (e) {}
    var out = { site: SITE, landing: (a.landing_page || location.pathname).slice(0, 120) };
    ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content'].forEach(function (k) { if (a[k]) out[k] = a[k]; });
    return out;
  }

  function sheet(area) {
    track('callback_form_open', { cta_area: area });
    var s = document.createElement('div');
    s.className = 'ah-sheet';
    s.setAttribute('role', 'dialog');
    s.setAttribute('aria-modal', 'true');
    s.innerHTML = '<div class="ah-card"><button type="button" class="ah-x" aria-label="Kapat">×</button>'
      + '<h3>' + kisa + ' 09:00\'da sizi arayalım</h3>'
      + '<div class="ah-who"><i>S</i><span><b>Selda Hanım</b> ' + when + ' ilk iş sizi arar, size uygun saati ve ücret bilgisini söyler.</span></div>'
      + '<form novalidate><input name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="05xx xxx xx xx" aria-label="Cep telefonunuz" maxlength="20">'
      + '<input name="hp" type="text" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0" aria-hidden="true">'
      + '<div class="ah-err" aria-live="polite"></div>'
      + '<button class="ah-send" type="submit">📞 Beni ' + kisa.toLowerCase() + ' arayın</button>'
      + '<div class="ah-small">Telefon numaranızı yalnızca sizi aramak için kullanırız. <a href="' + AYDINLATMA + '" target="_blank" rel="noopener">Aydınlatma metni</a></div></form>'
      + '<a class="ah-wa" href="' + waHref + '" target="_blank" rel="noopener" data-cta-area="after_hours_sheet">WhatsApp\'tan yazmayı tercih ederim</a></div>';
    document.body.appendChild(s);
    var kapat = function () { if (s.parentNode) s.parentNode.removeChild(s); };
    s.querySelector('.ah-x').onclick = kapat;
    s.addEventListener('click', function (e) { if (e.target === s) kapat(); });
    var f = s.querySelector('form'), inp = f.querySelector('[name=phone]'), err = f.querySelector('.ah-err'), btn = f.querySelector('.ah-send');
    setTimeout(function () { try { inp.focus(); } catch (e) {} }, 60);
    f.onsubmit = function (e) {
      e.preventDefault();
      var digits = inp.value.replace(/\D/g, '').replace(/^90/, '').replace(/^0/, '');
      if (!/^5\d{9}$/.test(digits)) { err.textContent = 'Lütfen 05 ile başlayan cep numaranızı yazın.'; inp.focus(); return; }
      btn.disabled = true; err.textContent = '';
      fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ phone: '0' + digits, when: 'saat', at: saat, hp: f.querySelector('[name=hp]').value, landing: (location.hostname + location.pathname).slice(0, 120), attribution: attribution() }) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (x) {
          if (!x.ok || !x.j || !x.j.ok) throw new Error((x.j && x.j.error) || 'hata');
          track('callback_request', { cta_area: area });
          s.querySelector('.ah-card').innerHTML = '<button type="button" class="ah-x" aria-label="Kapat">×</button><div class="ah-ok"><div style="font-size:40px">✅</div><b>Talebiniz alındı</b><p>Selda Hanım ' + when + ' 09:00\'dan itibaren sizi arayacak. İyi dinlenmeler.</p></div>';
          s.querySelector('.ah-x').onclick = kapat;
        })
        .catch(function (ex) {
          btn.disabled = false;
          err.innerHTML = (ex && ex.message && ex.message !== 'hata' && ex.message.indexOf('Failed') < 0 ? ex.message : 'Şu an gönderilemedi.') + ' <a href="' + waHref + '" target="_blank" rel="noopener">WhatsApp\'tan yazın</a>.';
        });
    };
  }

  function btn(label, cls, area) {
    var b = document.createElement('button');
    b.type = 'button';
    if (cls) b.className = cls;
    b.setAttribute('data-cta-area', area);
    b.innerHTML = label;
    b.onclick = function () { sheet(area); };
    return b;
  }

  function init() {
    var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    var dismissed = false;
    try { dismissed = sessionStorage.getItem('ah_kapat') === '1'; } catch (e) {}
    if (!dismissed) {
      var bar = document.createElement('div'); bar.className = 'ah-bar' + (POS === 'bottom' ? ' ah-bottom' : ''); bar.setAttribute('role', 'note');
      bar.appendChild(btn('<span>🌙 Şu an mesai dışındayız.</span><b>' + kisa + ' Selda Hanım sizi arasın →</b>', 'ah-go', 'after_hours_bar'));
      var x = document.createElement('button'); x.type = 'button'; x.className = 'ah-x'; x.setAttribute('aria-label', 'Kapat'); x.innerHTML = '×';
      x.onclick = function () { bar.parentNode && bar.parentNode.removeChild(bar); try { sessionStorage.setItem('ah_kapat', '1'); } catch (e) {} };
      bar.appendChild(x);
      if (POS === 'bottom') document.body.appendChild(bar); else document.body.insertBefore(bar, document.body.firstChild);
    }
    // "Açık / kapalı" yazan alanların altına düğme
    var spots = document.querySelectorAll('[data-open-status]');
    for (var i = 0; i < spots.length; i++) {
      if (spots[i].nextElementSibling && spots[i].nextElementSibling.classList && spots[i].nextElementSibling.classList.contains('ah-inline')) continue;
      spots[i].parentNode.insertBefore(btn('📞 ' + kisa + ' Selda Hanım sizi arasın', 'ah-inline', 'after_hours_inline'), spots[i].nextSibling);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
