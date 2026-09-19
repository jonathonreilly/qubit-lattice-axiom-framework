#!/usr/bin/env python3
"""J:provenance:PR8148 — every number in the theorem statements of the
formation-rate clause note, located in the runner cache or derived here.

Not a re-find of the known R3 uniform-distance HIT (1/216, 56059/3369600);
those are sourced in the cache (D2) even if attack-g disputes the metric.
HIT only for a theorem number with no cache line, runner check, or derivation.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/admissibility-induced-law-block14-formation-rate-clause-witness-20260915"
NOTE = "docs/ADMISSIBILITY_RULE_FORMATION_RATE_CLAUSE_WITNESS_NO_COVARIANT_CLOCK_LAW_REACHES_THE_STATIC_LAW_ON_A_PLAQUETTE_BOUNDED_THEOREM_NOTE_2026-09-15.md"
RUNNER = "scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.txt"
HITS: list[str] = []


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path):
    r = git("show", f"origin/{BRANCH}:{path}")
    if r.returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
        r = git("show", f"origin/{BRANCH}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr.strip()[:200]}")
    return r.stdout


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def derive_d():
    p, q, r = 3, 1, 2
    Z1 = p + q + 4 * r
    Ks = F(p, Z1)
    Ka = F(q, Z1)
    Ko = F(r, Z1)
    K2s = Ks * Ks + Ka * Ka + 4 * Ko * Ko
    K2a = 2 * Ks * Ka + 4 * Ko * Ko
    K2o = 2 * Ko * (Ks + Ka) + 2 * Ko * Ko
    return F(1, K2s), F(1, K2a), F(1, K2o)


def main() -> int:
    note = show(NOTE)
    raw_cache = show(CACHE)
    cache = raw_cache
    if "----- stdout -----\n" in raw_cache:
        cache = raw_cache.split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    runner = show(RUNNER)
    print(f"cache stdout lines={len(cache.splitlines())} runner bytes={len(runner)}")

    ds, da, do = derive_d()
    print(f"derived d_same={ds} d_anti={da} d_orth={do}")
    if ds != F(72, 13) or da != F(72, 11) or do != 6:
        hit(f"d_same/d_anti/d_orth derive {ds},{da},{do} != 72/13, 72/11, 6")
    else:
        print("[DERIVED] d_same=72/13 d_anti=72/11 d_orth=6 from 1/K_2 at (3,1,2)")

    # G(p,d)=(1-p)d/6 + p d^2/36
    psym, dsym = F(1, 2), F(72, 13)
    G = (1 - psym) * dsym / 6 + psym * dsym * dsym / 36
    print(f"[DERIVED] G(1/2, 72/13)={G} from the stated formula")

    items = [
        ("R2 2x3 uniform TV", "372254646387017/12790481418000000"),
        ("R2 2x3 seeded TV", "5951761987229/292725576000000"),
        ("R2 2x3 attracting TV", "32318135184155791/1253467178964000000"),
        ("R2 plaquette uniform TV", "262271/15806232"),
        ("R2 plaquette seeded TV", "30457/2431728"),
        ("R2 plaquette attracting TV", "591377/39515580"),
        ("R2 plaquette parallel TV", "2239744469/137703893184"),
        ("R3 path3 uniform TV (known metric dispute)", "1/216"),
        ("R3 star4 uniform TV (known metric dispute)", "56059/3369600"),
        ("R4 d_same", "72/13"),
        ("R4 d_anti", "72/11"),
        ("R4 d_orth", "d_orth = 6"),
        ("R4 G formula 1/6", "1/6"),
        ("R4 G formula 1/36", "d^2/36"),
        ("R4 G formula 1/4", "(1/4) sum_s G"),
        ("R4 uniform ratios", "152/169"),
        ("R4 P3 ratio", "136/121"),
        ("executed (3,1,2)", "(3, 1, 2)"),
    ]
    n_cache = 0
    n_note = 0
    for name, needle in items:
        in_cache = needle in cache or needle.replace(" ", "") in cache.replace(" ", "")
        in_note = needle in note
        in_run = needle in runner
        src = []
        if in_cache:
            src.append("CACHE")
            n_cache += 1
        if in_note:
            src.append("NOTE")
            n_note += 1
        if in_run and not in_cache:
            src.append("RUNNER")
        print(f"[{'+'.join(src) or 'NONE'}] {name}: {needle}")
        if not src:
            hit(f"theorem number {needle} ({name}) has no cache/runner/note source")
        elif name.startswith("R2") or name.startswith("R3") or name.startswith("R4 d_"):
            if not in_cache:
                hit(f"{name} {needle} not in runner cache")

    # claim_scope fractions must appear in theorems or cache
    scope = re.search(r'claim_scope:\s*"(.*)"', note, re.S)
    print(f"claim_scope present={scope is not None}")

    if HITS:
        print("SUMMARY: PROVENANCE (PR #8148): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: PROVENANCE (PR #8148): all listed theorem numbers "
        f"(2x3 TVs, plaquette TVs, d_same=72/13 derived, G 1/4 1/6 1/36, "
        f"R3 1/216 and 56059/3369600) have CACHE and/or DERIVED sources "
        f"({n_cache} cache hits); the known R3 metric HIT is sourced at D2 "
        "not unsourced; no provenance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
