"""Sayfa güçlendirme: uzman onaylı ek bölümler mevcut sayfanın metninin sonuna eklenir (yeni adres açılmaz).
Biçim: EKLER = {'/adres/': {'tarih': 'YYYY-AA-GG', 'html': '<h2>…</h2><p>…</p>'}}
Hem semt/hizmet (landing.py) hem içerik (icerik.json, makaleler.py) sayfalarında çalışır; sayfanın
güncelleme tarihi 'tarih' olur."""
EKLER = {}
