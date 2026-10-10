/* RN Psikoloji Çayyolu – menü ve açık/kapalı durumu */
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('ana-menu');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Menüyü kapat' : 'Menüyü aç');
      nav.classList.toggle('open', open);
      document.body.classList.toggle('menu-open', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.classList.contains('open')) btn.click();
    });
  }

  // Pazartesi – Cumartesi 09:00 – 20:00 (İstanbul saati)
  var els = document.querySelectorAll('[data-open-status]');
  if (!els.length) return;
  var day = 0, mins = 0;
  try {
    var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Istanbul', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    var get = function (t) { for (var i = 0; i < parts.length; i++) if (parts[i].type === t) return parts[i].value; return ''; };
    day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(get('weekday'));
    mins = (parseInt(get('hour'), 10) % 24) * 60 + parseInt(get('minute'), 10);
  } catch (e) { return; }
  var open = day >= 1 && day <= 6 && mins >= 540 && mins < 1200;
  var text = open ? 'Şu an açığız · Telefonu Selda Hanım açar.' : "Şu an mesai dışındayız. WhatsApp'tan mesaj bırakabilirsiniz, ilk mesaide dönüş yapılır.";
  for (var i = 0; i < els.length; i++) {
    els[i].innerHTML = '<span class="dot"></span><span></span>';
    els[i].lastChild.textContent = text;
    if (open) els[i].classList.add('is-open');
  }
})();

/* Jivo sohbet simgesi mobilde alttaki Ara/WhatsApp çubuğunun üstünde dursun */
(function () {
  var OFFSET = 76, handled = [];
  function mobile() { return window.innerWidth < 1024; }
  function candidate(el) {
    if (handled.indexOf(el) !== -1 || el.closest('.sticky-bar')) return false;
    var cs; try { cs = getComputedStyle(el); } catch (e) { return false; }
    if (cs.position !== 'fixed') return false;
    var r = el.getBoundingClientRect();
    if (r.width < 36 || r.width > 110 || r.height < 36 || r.height > 110) return false;
    return (window.innerWidth - r.right) < 60 && (window.innerHeight - r.bottom) < 60;
  }
  function apply(el) {
    handled.push(el);
    var set = function () { if (mobile()) el.style.setProperty('bottom', OFFSET + 'px', 'important'); else el.style.removeProperty('bottom'); };
    set(); window.addEventListener('resize', set);
  }
  function scan() { var all = document.querySelectorAll('body > *, jdiv, jdiv *'); for (var i = 0; i < all.length; i++) if (candidate(all[i])) apply(all[i]); }
  var n = 0, t = setInterval(function () { scan(); if (++n > 20) clearInterval(t); }, 1000);
})();
