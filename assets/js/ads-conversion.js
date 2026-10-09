/* ============================================================
   Google Ads / GA4 dönüşüm katmanı
   ------------------------------------------------------------
   Google Tag Manager'a (dataLayer) şu olayları gönderir:
     phone_call_click     tel: bağlantısına tıklama
     whatsapp_click       wa.me / WhatsApp bağlantısına tıklama
     instagram_click      Instagram profil bağlantısına tıklama
     chat_started         Jivo sohbetinde ilk mesaj gönderildi
     chat_contact_shared  Jivo sohbetinde ziyaretçi iletişim bilgisi bıraktı
     virtual_page_view    tek sayfalı sitelerde sayfa değişimi

   Ayrıca reklam tıklama kimliklerini (gclid / gbraid / wbraid)
   ve UTM parametrelerini 90 gün saklar ve Jivo operatör
   ekranına iletir.

   Ayarlar (isteğe bağlı), bu dosyadan ÖNCE tanımlanır:
     window.ADS_CONV_CFG = { spa: true }
   ============================================================ */
(function () {
  'use strict';
  var w = window, d = document;
  if (w.__adsConvLoaded) return;
  w.__adsConvLoaded = true;
  w.dataLayer = w.dataLayer || [];
  var CFG = w.ADS_CONV_CFG || {};

  /* ---------- 1. Reklam tıklama kimliği ve UTM saklama ---------- */
  var STORE_KEY = 'ads_attribution';
  var TTL = 90 * 24 * 60 * 60 * 1000;
  var PARAMS = ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];

  function readAttr() {
    try {
      var v = JSON.parse(localStorage.getItem(STORE_KEY) || 'null');
      if (v && v.exp > Date.now()) return v;
    } catch (e) {}
    return null;
  }

  function captureAttr() {
    var got = {}, any = false;
    try {
      var q = new URLSearchParams(location.search);
      PARAMS.forEach(function (p) {
        var v = q.get(p);
        if (v) { got[p] = v.slice(0, 250); any = true; }
      });
    } catch (e) {}
    if (any) {
      got.landing_page = location.pathname;
      got.exp = Date.now() + TTL;
      try { localStorage.setItem(STORE_KEY, JSON.stringify(got)); } catch (e) {}
      return got;
    }
    return readAttr();
  }

  var attr = captureAttr();
  var fromAds = !!(attr && (attr.gclid || attr.gbraid || attr.wbraid));

  /* ---------- 2. Olay gönderimi (çift saymaya karşı korumalı) ---------- */
  var lastSent = {};
  function track(eventName, extra) {
    var now = Date.now();
    if (lastSent[eventName] && now - lastSent[eventName] < 1000) return;
    lastSent[eventName] = now;
    var payload = {
      event: eventName,
      page_path: location.pathname,
      page_title: d.title,
      traffic_type: fromAds ? 'google_ads' : 'other'
    };
    if (extra) for (var k in extra) if (Object.prototype.hasOwnProperty.call(extra, k)) payload[k] = extra[k];
    w.dataLayer.push(payload);
    sendAdsConversion(eventName);
  }

  /* ---------- 2b. Google Ads dönüşümü (gtag) ----------
     Etiketler Google Ads > Hedefler > Dönüşümler > [işlem] > Etiket kurulumu
     ekranındaki "Dönüşüm etiketi"dir. Etiket boşsa dönüşüm gönderilmez. */
  var ADS = {
    id: CFG.adsId || 'AW-11469933181',
    labels: CFG.adsLabels || { phone_call_click: 't-kJCIrB7pYdEP2Upd0q', whatsapp_click: 'zO3TCK2h-JYdEP2Upd0q' },
    values: { phone_call_click: 100, whatsapp_click: 60 }
  };
  var adsSent = {};
  function sendAdsConversion(eventName) {
    var label = ADS.labels[eventName];
    if (!label || typeof w.gtag !== 'function' || adsSent[eventName]) return;
    adsSent[eventName] = true;
    w.gtag('event', 'conversion', {
      send_to: ADS.id + '/' + label,
      value: ADS.values[eventName] || 1,
      currency: 'TRY',
      transport_type: 'beacon'
    });
  }
  w.adsTrack = track;

  function ctaArea(el) {
    var a = el.closest('[data-cta-area]');
    if (a) return a.getAttribute('data-cta-area');
    if (el.closest('.rn-sticky-bar, .mobile-cta-bar, .mobile-leadbar')) return 'sticky_bar';
    if (el.closest('.sticky-whatsapp')) return 'floating_button';
    if (el.closest('header, .header')) return 'header';
    if (el.closest('footer')) return 'footer';
    if (el.closest('.mobile-panel')) return 'mobile_menu';
    return 'content';
  }

  /* ---------- 3. Telefon ve WhatsApp tıklamaları ---------- */
  d.addEventListener('click', function (e) {
    var t = e.target;
    if (!t || !t.closest) return;
    var call = t.closest('a[href^="tel:"]');
    if (call) {
      track('phone_call_click', { cta_area: ctaArea(call), cta_href: call.getAttribute('href') });
      return;
    }
    var wa = t.closest('a[href*="wa.me/"], a[href*="api.whatsapp.com"], a[href*="whatsapp://"]');
    if (wa) {
      track('whatsapp_click', { cta_area: ctaArea(wa) });
    }
    var ig = t.closest('a[href*="instagram.com/"]');
    if (ig) {
      track('instagram_click', { cta_area: ctaArea(ig) });
    }
  }, true);

  /* ---------- 4. Jivo canlı sohbet ---------- */
  function chain(name, fn) {
    var prev = w[name];
    w[name] = function () {
      try { fn.apply(this, arguments); } catch (e) {}
      if (typeof prev === 'function') return prev.apply(this, arguments);
    };
  }
  var chatSent = false;
  chain('jivo_onMessageSent', function () {
    if (chatSent) return;
    chatSent = true;
    track('chat_started', { chat_provider: 'jivo' });
  });
  chain('jivo_onIntroduction', function () {
    track('chat_contact_shared', { chat_provider: 'jivo' });
  });
  chain('jivo_onLoadCallback', function () {
    var a = readAttr();
    if (!a || !w.jivo_api || typeof w.jivo_api.setCustomData !== 'function') return;
    var rows = [{ title: 'Kaynak', content: (a.gclid || a.gbraid || a.wbraid) ? 'Google Ads' : (a.utm_source || 'Diğer') }];
    if (a.utm_campaign) rows.push({ title: 'Kampanya', content: a.utm_campaign });
    if (a.utm_term) rows.push({ title: 'Anahtar kelime', content: a.utm_term });
    if (a.landing_page) rows.push({ title: 'Giriş sayfası', content: a.landing_page });
    try { w.jivo_api.setCustomData(rows); } catch (e) {}
  });

  /* ---------- 5. Tek sayfalı site: sayfa değişimlerini bildir ---------- */
  if (CFG.spa) {
    var lastPath = location.pathname;
    var onRoute = function () {
      setTimeout(function () {
        if (location.pathname === lastPath) return;
        lastPath = location.pathname;
        w.dataLayer.push({
          event: 'virtual_page_view',
          page_path: location.pathname,
          page_location: location.href,
          page_title: d.title
        });
      }, 150);
    };
    var origPush = history.pushState;
    history.pushState = function () {
      var r = origPush.apply(this, arguments);
      onRoute();
      return r;
    };
    w.addEventListener('popstate', onRoute);
  }
})();
