#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract text from the 55 MTH PDFs (keyed on NN prefix) into _pdftext/NN.txt.
Source PDFs live in user Downloads (not committed)."""
import os, re, sys
from pypdf import PdfReader

SRC = "C:/Users/allen/Downloads/Magic Tree House 神奇树屋01-55（MOBI+PDF+MP3）/Magic Tree House 神奇树屋01-55（MOBI+PDF+MP3）"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_pdftext")
os.makedirs(OUT, exist_ok=True)

def find_pdf(num):
    prefix = f"{num:02d} "
    for name in sorted(os.listdir(SRC)):
        if name.startswith(prefix):
            d = os.path.join(SRC, name)
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    if f.lower().endswith(".pdf"):
                        return os.path.join(d, f)
    return None

def main():
    only = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else list(range(1, 56))
    for num in only:
        pdf = find_pdf(num)
        if not pdf:
            print(f"{num:02d} NO_PDF"); continue
        try:
            r = PdfReader(pdf)
            parts = []
            for p in r.pages:
                try:
                    parts.append(p.extract_text() or "")
                except Exception:
                    parts.append("")
            txt = "\n".join(parts)
            txt = re.sub(r"\n{3,}", "\n\n", txt)
            out = os.path.join(OUT, f"{num:02d}.txt")
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(txt)
            print(f"{num:02d} OK pages={len(r.pages)} chars={len(txt)}")
        except Exception as e:
            print(f"{num:02d} FAIL {e}")

if __name__ == "__main__":
    main()
