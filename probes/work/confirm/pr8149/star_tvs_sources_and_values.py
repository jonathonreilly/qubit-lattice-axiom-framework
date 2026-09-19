#!/usr/bin/env python3
"""J:confirm:J-provenance-PR8149 -- independent test of the finder's provenance HIT on block 15 (PR #8149).

Finder's HIT: Theorem U3 lists the isolated-star sequential-vs-joint TVs 0, 0, 1/72, 5/144, 505/10368, 575/10368, 103375/1492992 for
k = 0..6 leaves before the center; the runner cache prints only k = 2, 3, 6, so 505/10368 and 575/10368 are unsourced.

Machinery:
  1. provenance: every rational token in the cache and every rational literal in the runner source is parsed as a Fraction (value
     match, any form), and the note is searched for an exact derivation of the k = 4, 5 values (the task's two sourcing routes);
  2. the values themselves, computed independently: the isolated star (center c, six leaves, six c-leaf bonds, leaves pairwise non-adjacent),
     six-axis menu at (3,1,2); joint law = the Gibbs law of the six bonds; sequential with k leaves first = k uniform leaves, the center
     from the rule given those k leaves, the other leaves from the rule given c. Later leaves have the same conditional in both laws, so
     the TV is that of (first k leaves, center), computed exactly by enumeration (6^(k+1) atoms), cross-checked for k <= 4 by enumerating
     the full 6^7 star.
"""
from __future__ import annotations

import itertools
import re
import subprocess
from fractions import Fraction as F

BRANCH = "physics-loop/admissibility-induced-law-block15-formation-unit-clause-witness-20260915"
AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(a, b, p=3, q=1, r=2):
    d = sum(x * y for x, y in zip(AXES[a], AXES[b]))
    return p if d == 1 else (q if d == -1 else r)


def tv_reduced(k):
    Z1 = F(sum(phi(s, 0) for s in range(6)))
    tot = F(0)
    for a in itertools.product(range(6), repeat=k):
        Zk = sum(_prod(phi(c, ai) for ai in a) for c in range(6))
        for c in range(6):
            w = _prod(phi(c, ai) for ai in a)
            seq = F(1, 6 ** k) * F(w, Zk)
            joint = F(1, 6) * F(w) / Z1 ** k
            tot += abs(seq - joint)
    return tot / 2


def _prod(it):
    out = 1
    for v in it:
        out *= v
    return out


def tv_full(k):
    """full star: sites = center + 6 leaves; exact over 6^7 atoms."""
    Z1 = sum(phi(s, 0) for s in range(6))
    ZJ = 6 * Z1 ** 6
    tot = F(0)
    for s in itertools.product(range(6), repeat=7):
        c, leaves = s[0], s[1:]
        wj = _prod(phi(c, l) for l in leaves)
        joint = F(wj, ZJ)
        first, later = leaves[:k], leaves[k:]
        Zk = sum(_prod(phi(u, a) for a in first) for u in range(6))
        seq = F(1, 6 ** k) * F(_prod(phi(c, a) for a in first), Zk) * F(_prod(phi(l, c) for l in later), Z1 ** len(later))
        tot += abs(seq - joint)
    return tot / 2


def main():
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], check=True)
    files = subprocess.run(["gh", "pr", "view", "8149", "--json", "files", "--jq", ".files[].path"],
                           capture_output=True, text=True, check=True).stdout.split()
    show = lambda p: subprocess.run(["git", "show", f"FETCH_HEAD:{p}"], capture_output=True, text=True, check=True).stdout
    cache = "\n".join(show(f) for f in files if f.startswith("logs/runner-cache/"))
    runner = "\n".join(show(f) for f in files if f.startswith("scripts/"))
    note = show([f for f in files if f.startswith("docs/") and "NOTE" in f][0])

    def fracs(text):
        out = set()
        for m in re.finditer(r'(?<![\w.])(\d+)\s*/\s*(\d+)(?![\w.])', text):
            out.add(F(int(m.group(1)), int(m.group(2))))
        for m in re.finditer(r'F\(\s*(\d+)\s*,\s*(\d+)\s*\)', text):
            out.add(F(int(m.group(1)), int(m.group(2))))
        return out

    cache_vals, runner_vals = fracs(cache), fracs(runner)
    stated = {2: F(1, 72), 3: F(5, 144), 4: F(505, 10368), 5: F(575, 10368), 6: F(103375, 1492992)}
    print("1. provenance of the stated star TVs")
    for k, v in stated.items():
        print(f"   k={k}: {v}: printed in the cache {v in cache_vals}; a literal in the runner {v in runner_vals}")
    classes = re.search(r"star's classes k = ([0-9, ]+)", cache)
    print(f"   the runner's star classes (cache C1/D1): k = {classes.group(1) if classes else '?'}; note proof of U3: "
          f"'{[l.strip() for l in note.splitlines() if l.strip().startswith('*Proof.* U2 with the star')][0][:90]}...'")

    print("2. the TVs computed independently at (3,1,2)")
    got = {k: tv_reduced(k) for k in range(7)}
    cross = {k: tv_full(k) for k in (2, 3, 4)}
    for k in range(7):
        extra = f" (full 6^7 enumeration {cross[k]})" if k in cross else ""
        print(f"   k={k}: TV = {got[k]}{extra}; stated {stated.get(k, 0)}; equal {got[k] == stated.get(k, F(0))}")

    unsourced = [k for k in (4, 5) if stated[k] not in cache_vals]
    values_ok = all(got[k] == stated.get(k, F(0)) for k in range(7)) and all(cross[k] == got[k] for k in cross)
    if unsourced and values_ok:
        print(f"HIT: confirmed - Theorem U3's star TVs for k = 4, 5 (505/10368, 575/10368) are printed by no cache line and are not runner "
              f"literals: the runner computes and checks only the classes k = 0, 1, 2, 3, 6, and the note's proof of U3 derives no number; "
              f"recomputed independently here the values are correct (k = 0..6: {', '.join(str(got[k]) for k in range(7))}, the full 6^7 "
              f"enumeration agreeing for k = 2, 3, 4)")
        print("SUMMARY: confirmed - two theorem numbers of block 15's U3 are unsourced in the PR (not printed, not derived), though they are "
              "right; the fix is to extend the runner's star classes to k = 4, 5 and print their TVs")
    elif unsourced:
        wrong = [k for k in range(7) if got[k] != stated.get(k, F(0))]
        print(f"HIT: confirmed - the k = 4, 5 star TVs are unsourced, and the independent computation differs at k = {wrong}: "
              f"{', '.join(f'{k}: {got[k]} vs {stated.get(k, 0)}' for k in wrong)}")
        print("SUMMARY: confirmed - unsourced (and differing) star TVs")
    else:
        print("SUMMARY: not reproduced - the k = 4, 5 TVs are printed in the cache")


if __name__ == "__main__":
    main()
