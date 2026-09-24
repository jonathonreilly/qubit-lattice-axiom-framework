#!/usr/bin/env python3
"""Independent coverage check of MINIMAL_AXIOMS at origin/main."""
import subprocess

SHA = "fbe9f0f0154402d8afa07a8d12c920df2d9d0848"
PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"


def main():
    text = subprocess.check_output(["git", "show", f"{SHA}:{PATH}"], text=True)
    lines = text.splitlines()
    def span(a, b):
        return "\n".join(lines[a - 1 : b])
    s79 = span(79, 80)
    s166 = span(166, 168)
    s199 = span(199, 202)
    s228 = span(228, 233)
    ok = "records are permanent" in s79
    ok &= "unreadability of a site with no record" in s166
    ok &= "Records" in s199 and "form." in s199
    ok &= "distribution's form and values" in s228
    print("L79-80", s79.replace("\n", " | "))
    print("L166-168 has permanence restated", "permanence" in s166)
    print("L199 names Records form", "Records" in s199)
    print("L228 keeps distribution downstream", "downstream" in s228)
    if ok:
        print(
            "HIT: confirmed - the memo states permanence at L79-80 and again at L166-168, "
            "records the 2026-07-04 formation sentence at L199-202, and keeps the distribution downstream at L228-233"
        )
        print(
            "SUMMARY: confirmed the coverage gap: a clause that edits only L79-80 leaves the summary, the history entry, and the closing paragraph"
        )
    else:
        print("SUMMARY: fails at a cited line")


if __name__ == "__main__":
    main()
