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
  var text = open ? 'Şu an açığız, hemen arayabilirsiniz.' : "Şu an mesai dışındayız. WhatsApp'tan mesaj bırakabilirsiniz, ilk mesaide dönüş yapılır.";
  for (var i = 0; i < els.length; i++) {
    els[i].innerHTML = '<span class="dot"></span><span></span>';
    els[i].lastChild.textContent = text;
    if (open) els[i].classList.add('is-open');
  }
})();
