"""Locate argument codes of the Sussman-Alpoge outline YM4_sketch_500.tex.

Usage: python3 -I locate_codes.py <path to YM4_sketch_500.tex> [code ...]

Prints, for each code, every line on which the code occurs as a whole token
(not inside a longer number such as 2.80 or 12.8), with the enclosing
section title.  Read-only; no numerics.  Used for the sa-map item.
"""
import re
import sys

DEFAULT = ["1a.3.2", "1a.3.5", "2.8", "2.10", "2.12", "2.13", "4.11",
           "7.5", "7.6", "7a.1.8", "9.1", "9.3", "9.7", "9.10", "9.11",
           "1.2", "1.6"]


def main():
    path = sys.argv[1]
    codes = sys.argv[2:] or DEFAULT
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().split("\n")
    sec = [""] * len(lines)
    cur = ""
    for i, ln in enumerate(lines):
        m = re.match(r"\\(sub)*section\*?\{(.*)", ln)
        if m and m.group(1) is None:
            cur = m.group(2)[:70]
        sec[i] = cur
    for c in codes:
        pat = re.compile(r"(?<![0-9A-Za-z.])" + re.escape(c) + r"(?![0-9])(?!\.[0-9])")
        hits = [i for i, ln in enumerate(lines) if pat.search(ln)]
        print(f"== {c}: {len(hits)} lines")
        for i in hits:
            print(f"  {i+1}: [{sec[i]}] {lines[i].strip()[:200]}")


if __name__ == "__main__":
    main()
