# -*- coding: utf-8 -*-
"""WordPress dışa aktarımından (XML) yayınlanmış sayfa ve yazıları icerik.json'a çıkarır.
Kullanım: python3 _kaynak/extract.py /yol/wordpress.xml
XML dosyası depoya eklenmez (yorum ve e-posta verisi içerir)."""
import json, os, re, sys
import xml.etree.ElementTree as ET

NS = {'wp': 'http://wordpress.org/export/1.2/',
      'content': 'http://purl.org/rss/1.0/modules/content/',
      'excerpt': 'http://wordpress.org/export/1.2/excerpt/'}
SITE = 'https://www.cayyolupsikolog.com.tr'

def main(xml_path):
    items = ET.parse(xml_path).getroot().find('channel').findall('item')
    attachments = {}
    for it in items:
        if it.find('wp:post_type', NS).text == 'attachment':
            attachments[it.find('wp:post_id', NS).text] = it.find('wp:attachment_url', NS).text
    out = []
    for it in items:
        ptype = it.find('wp:post_type', NS).text
        if ptype not in ('page', 'post') or it.find('wp:status', NS).text != 'publish':
            continue
        meta = {pm.find('wp:meta_key', NS).text: (pm.find('wp:meta_value', NS).text or '')
                for pm in it.findall('wp:postmeta', NS)}
        link = it.find('link').text or ''
        path = link.replace(SITE, '') or '/'
        if not path.endswith('/'):
            path += '/'
        thumb = attachments.get(meta.get('_thumbnail_id', ''), '')
        cats = [c.text for c in it.findall('category') if c.get('domain') == 'category']
        out.append({
            'type': ptype,
            'path': path,
            'slug': it.find('wp:post_name', NS).text,
            'title': it.find('title').text or '',
            'date': (it.find('wp:post_date', NS).text or '')[:10],
            'modified': (it.find('wp:post_modified', NS).text or '')[:10],
            'html': it.find('content:encoded', NS).text or '',
            'excerpt': it.find('excerpt:encoded', NS).text or '',
            'seo_title': meta.get('_yoast_wpseo_title', ''),
            'seo_desc': meta.get('_yoast_wpseo_metadesc', ''),
            'thumb': thumb.replace(SITE, '') if thumb else '',
            'categories': cats,
        })
    out.sort(key=lambda x: (x['type'], x['path']))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icerik.json')
    json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'kayıt ->', dest)

if __name__ == '__main__':
    main(sys.argv[1])
