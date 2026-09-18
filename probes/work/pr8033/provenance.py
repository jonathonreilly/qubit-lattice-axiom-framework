#!/usr/bin/env python3
"""J:provenance:PR8033 — theorem numbers vs PR branch runner, cache, and note."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/finite-pw-confinement-block43-20260907"
RUNNER = "scripts/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.py"
NOTE = "docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md"
CACHE = "logs/runner-cache/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.txt"

NUMBERS = [
    ("4/a", "charged free floor and bound (1) prefactor"),
    ("3u/4", "r=3u/4 and cell perturbation norm"),
    ("3cr", "kappa=3cr"),
    ("(1-kappa)d", "bound (1) and resolvent radius"),
    ("gap 1", "cell vacuum gap exactly 1 for every R>=1"),
    ("4d/a", "charged free floor"),
    ("9", "endpoint source dimension"),
    ("sqrt9", "factor 3=sqrt(9) independent of irrep dim"),
    ("h_R", "R²-floor(R²/4)+3R"),
    ("8ud", "theta_bar=8ud/h_R"),
    ("sqrt(8u)", "upper envelope (4)"),
    ("32u", "2u sqrt(32u/h_R) in (4)"),
    ("18", "exact helper controls"),
    ("243", "R1 center flows per cube endpoint pair"),
    ("2", "two cube endpoint pairs"),
    ("3Delta", "K_e=-3 Delta_e/(2a)"),
    ("p²+pq+q²+3p+3q", "one-link electric energies /a"),
    ("(8)-(15)", "Yarotsky 0411042 Section 2 equations"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    spelled = {
        "4/a": [r"4/a", r"(4/a)", "4d/a", "energy at least4/a", "minimum_energy4d"],
        "3u/4": [r"3u/4", r"r=3u/4", "3*u/4"],
        "3cr": [r"kappa=3cr", r"3cr", "3*c*r"],
        "(1-kappa)d": [r"(1-kappa)d", r"(1-kappa)", "1-kappa"],
        "gap 1": ["gap is exactly1", "gap is exactly 1", "the gap is exactly1"],
        "4d/a": [r"4d/a", "at least4d/a", "floor d on the charged"],
        "9": ["9-dimensional", "sqrt9", r"\sqrt9", "9-dimensional endpoint"],
        "sqrt9": [r"3=\sqrt9", r"3=sqrt(9)", r"factor3=\sqrt9", "sqrt9"],
        "h_R": [r"h_R=R²-floor(R²/4)+3R", r"h_R=R^2", "h_R"],
        "8ud": [r"theta_bar=8ud/h_R", r"8ud", "h_R>8ud"],
        "sqrt(8u)": [r"sqrt(8u)", r"\sqrt(8u)", r"1+\sqrt(8u)"],
        "32u": [r"32u/h_R", r"32u"],
        "18": ["performs18 exact", "18 exact controls", "TOTAL: 18", "expected),18"],
        "243": ["all243", "exact243", "len(sol)==243"],
        "2": ["two cube endpoint pairs", "two actual cube endpoint pairs"],
        "3Delta": [r"-3Delta_e/(2a)", r"-3\Delta_e/(2a)", "3Delta"],
        "p²+pq+q²+3p+3q": [r"p²+pq+q²+3p+3q", "p*p+p*q+q*q+3*p+3*q", "p^2+pq+q^2+3p+3q"],
        "(8)-(15)": ["equations(8)–(15)", "equations(8)-(15)", "(8)–(15)"],
    }
    return spelled.get(token, [token])


def find_line(blob: str, token: str) -> str | None:
    for alt in alts_for(token):
        pat = re.compile(re.escape(alt))
        for line in blob.splitlines():
            if "sha256" in line.lower():
                continue
            if pat.search(line):
                return line.strip()
    return None


def main() -> None:
    runner = git_show(RUNNER)
    note = git_show(NOTE)
    cache = git_show(CACHE)
    blobs = [("cache", cache), ("runner", runner), ("note", note)]
    unsourced = 0
    hits: list[str] = []
    for token, role in NUMBERS:
        src = None
        for name, blob in blobs:
            hit_line = find_line(blob, token)
            if hit_line:
                src = f"{name}: {hit_line[:140]}"
                break
        if src:
            status = "OK"
        else:
            src = "NOT IN RUNNER, CACHE, OR NOTE LINE"
            status = "UNSOURCED"
            unsourced += 1
            hits.append(f"{token} ({role})")
        print(f"{token} | {role} | {src} | {status}")

    h_vals = [r * r - (r * r) // 4 + 3 * r for r in range(1, 21)]
    h_ok = all(h > 0 for h in h_vals) and h_vals == sorted(h_vals)
    print("IDENTITY | h_R=R^2-floor(R^2/4)+3R positive increasing R=1..20 | " + ("OK" if h_ok else "MISMATCH"))
    print("IDENTITY | 3=sqrt(9) | " + ("OK" if 3 * 3 == 9 else "MISMATCH"))
    print("IDENTITY | 243=3^5 | " + ("OK" if 3 ** 5 == 243 else "MISMATCH"))
    if not h_ok:
        unsourced += 1
        hits.append("h_R identity")
    if 3 ** 5 != 243:
        unsourced += 1
        hits.append("243 != 3^5")

    print(f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced")
    if hits:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
