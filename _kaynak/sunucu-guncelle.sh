#!/bin/bash
# cPanel cron ile çalışır: GitHub'daki main dalında yeni sürüm varsa public_html'e kopyalar.
# Sunucuda ~/guncelle.sh olarak kaydedilir. Cron: */5 * * * * /bin/bash $HOME/guncelle.sh >/dev/null 2>&1
REPO="activeenglish1987/cayyolu-psikolog-website"
HEDEF="$HOME/public_html"
IS="$HOME/.site-guncelle"
mkdir -p "$IS"
exec 9>"$IS/kilit"; flock -n 9 || exit 0

SHA=$(git ls-remote "https://github.com/$REPO.git" refs/heads/main 2>/dev/null | cut -f1)
if [ -z "$SHA" ]; then
  SHA=$(curl -fsS "https://api.github.com/repos/$REPO/commits/main" 2>/dev/null | grep -m1 '"sha"' | cut -d'"' -f4)
fi
[ -z "$SHA" ] && exit 0
[ "$SHA" = "$(cat "$IS/son" 2>/dev/null)" ] && exit 0

rm -rf "$IS/yeni" && mkdir -p "$IS/yeni"
if ! curl -fsSL "https://codeload.github.com/$REPO/tar.gz/$SHA" | tar -xz -C "$IS/yeni" --strip-components=1; then
  echo "$(date '+%F %T') indirme hatası $SHA" >> "$IS/kayit.txt"; exit 1
fi
[ -f "$IS/yeni/index.html" ] || { echo "$(date '+%F %T') index.html yok, iptal" >> "$IS/kayit.txt"; exit 1; }
rm -rf "$IS/yeni/_kaynak" "$IS/yeni/.github" "$IS/yeni/.gitignore"
cp -a "$IS/yeni/." "$HEDEF/" && echo "$SHA" > "$IS/son" && echo "$(date '+%F %T') yayınlandı $SHA" >> "$IS/kayit.txt"
rm -rf "$IS/yeni"
