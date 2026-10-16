#!/usr/bin/env python3
"""Check publishable paths, UTF-8 text, and PDF text for Chinese characters.

Raster figures need visual review; available SVG/PDF sources are scanned.
Install pymupdf to include PDF text. Git-ignored build output is excluded.
"""
from pathlib import Path
import argparse
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HAN = re.compile('[\u2e80-\u2fdf\u3007\u3100-\u312f\u31a0-\u31bf\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f\U00030000-\U000323af]')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--text-only', action='store_true', help='Skip PDFs explicitly; check file paths and text files.')
    args = parser.parse_args()
    paths = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '--cached', '--others', '--exclude-standard', '-z']).decode().split('\0')
    failures, text_count, pdf_count, raster_count = [], 0, 0, 0
    for name in sorted(set(filter(None, paths))):
        p = ROOT / name
        if not p.is_file():
            continue
        if HAN.search(name):
            failures.append(f'{name}: Chinese character in path')
        if p.suffix.lower() == '.pdf':
            if args.text_only:
                continue
            try:
                import pymupdf
            except ImportError:
                sys.exit('PDF scanning requires pymupdf. Install it, or explicitly use --text-only.')
            with pymupdf.open(p) as doc:
                for page_number, page in enumerate(doc, 1):
                    if HAN.search(page.get_text()):
                        failures.append(f'{name}:page {page_number}: Chinese text')
            pdf_count += 1
            continue
        if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico'}:
            raster_count += 1
            continue
        raw = p.read_bytes()
        if b'\0' in raw:
            failures.append(f'{name}: unsupported binary file requires review')
            continue
        try:
            content = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            failures.append(f'{name}: non-UTF-8 file requires review')
            continue
        text_count += 1
        for line_number, line in enumerate(content.splitlines(), 1):
            if HAN.search(line):
                failures.append(f'{name}:{line_number}: Chinese text')
        if p.suffix == '.json':
            import json
            if HAN.search(str(json.loads(content))):
                failures.append(f'{name}: Chinese text in decoded JSON')
    if failures:
        print('\n'.join(failures))
        sys.exit(1)
    print(f'PASS: {text_count} text files and {pdf_count} PDFs contain no Chinese characters; all publishable paths checked.')
    print(f'{raster_count} raster images require visual review; check available SVG/PDF sources and directly review the promotional hero PNGs.')


if __name__ == '__main__':
    main()
