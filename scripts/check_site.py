#!/usr/bin/env python3
"""Dependency-free checks for the static Wareneinsatz site."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.go = []
        self.scripts = []
        self.external = []
        self._in_script = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
        if a.get('data-go'):
            self.go.append(a['data-go'])
        if a.get('href', '').startswith('#') and a['href'] != '#':
            self.links.append(a['href'][1:])
        for key in ('src', 'href'):
            if a.get(key, '').startswith(('http://', 'https://')):
                self.external.append(a[key])
        if tag == 'script' and not a.get('src'):
            self._in_script = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self._in_script = False

    def handle_data(self, data):
        if self._in_script:
            self.scripts.append(data)


def main():
    page = Path('index.html')
    if not page.is_file():
        sys.exit('FEHLER: index.html fehlt')
    source = page.read_text(encoding='utf-8')
    check = Inspector()
    check.feed(source)
    check.close()
    errors = []
    id_set = set(check.ids)
    duplicates = sorted({x for x in check.ids if check.ids.count(x) > 1})
    if duplicates:
        errors.append('Doppelte HTML-IDs: ' + ', '.join(duplicates))
    for target in check.links:
        if target not in id_set:
            errors.append(f'Link-Ziel fehlt: #{target}')
    for target in check.go:
        if f'p-{target}' not in id_set:
            errors.append(f'Navigationsziel fehlt: p-{target}')
    for target in ('p-start', 'p-belege', 'p-s1', 'p-s2', 'p-s3'):
        if target not in id_set:
            errors.append(f'Wichtiger Abschnitt fehlt: {target}')
    if not check.scripts:
        errors.append('Inline-JavaScript fehlt')
    if re.search(r'\b(amann|2bkwi1|bsz hechingen)\b', source, re.I):
        errors.append('Entfernte Schul-/Personenbezüge wiedergefunden')
    if check.external:
        print('HINWEIS: Externe Ressourcen vorhanden: ' + ', '.join(check.external))
    script_path = Path('/tmp/wareneinsatz-check.js')
    script_path.write_text('\n'.join(check.scripts), encoding='utf-8')
    if errors:
        for error in errors:
            print('FEHLER:', error)
        sys.exit(1)
    print(f'OK: HTML-IDs ({len(check.ids)}), Navigation ({len(check.go)}) und Struktur geprüft')
    print('JavaScript-Auszug:', script_path)

if __name__ == '__main__':
    main()
