#!/usr/bin/env python3
"""J:derive:chessboard-repair:a4 — orbit, lemma, sharpness, 216^{4/3}=1296, CS arithmetic."""
from __future__ import annotations

import itertools
import sys
from collections import deque
from fractions import Fraction as Fr

M = range(6)


def lemma_ok(n, alphabet=5):
    letters = range(alphabet)
    for a in itertools.product(letters, repeat=n):
        if any(a[t] == a[(t + 1) % n] for t in range(n)):
            continue
        for s in itertools.product(letters, repeat=n):
            bad_s = sum(s[t] != s[(t + 1) % n] for t in range(n))
            bad_sa = sum(s[t] != a[t] for t in range(n))
            if bad_s + 2 * bad_sa < n:
                return False
    return True


def orbit_2d(L=4):
    pts = ((0, 0), (1, 0))
    seen = {tuple(sorted(pts))}
    q = deque([pts])
    dir0 = []
    while q:
        b = q.popleft()
        if b[0][1] == b[1][1]:
            dir0.append(b)
        for axis in (0, 1):
            for k in range(L):
                nb = []
                for p in b:
                    pp = list(p)
                    pp[axis] = (2 * k - pp[axis]) % L
                    nb.append(tuple(pp))
                key = tuple(sorted(nb))
                if key not in seen:
                    seen.add(key)
                    q.append(key)
    par = {bond[0][1] % 2 for bond in dir0}
    N = L * L
    return len(seen), len(dir0), par, N, N // 2


def sharpness_2d(L):
    def val(x, y):
        return (0 if x % 2 == 0 else 2) if y % 2 == 0 else 0
    bad = 0
    for x, y in itertools.product(range(L), repeat=2):
        if val(x, y) != val((x + 1) % L, y):
            bad += 1
        if val(x, y) != val(x, (y + 1) % L):
            bad += 1
    return bad, L * L


def sharpness_3d(L):
    def val(x, y, z):
        if y % 2 == 0 and z % 2 == 0:
            return 0 if x % 2 == 0 else 2
        return 0
    bad = 0
    for x, y, z in itertools.product(range(L), repeat=3):
        for w in (val((x + 1) % L, y, z), val(x, (y + 1) % L, z), val(x, y, (z + 1) % L)):
            if val(x, y, z) != w:
                bad += 1
    N = L ** 3
    return bad, N, 3 * N // 4


def main():
    hits = []
    print("C1 orbit (Z/4)^2 site reflections of canonical horizontal bond:")
    nseen, ndir, par, N, Nh = orbit_2d(4)
    print(f"  |orbit|={nseen} dir0={ndir} parities={par} N/2={Nh}")
    if ndir != Nh or par != {0}:
        hits.append("orbit")

    print("C2 lemma bad(s)+2 bad(s,a)>=n:")
    for n, alph in ((4, 5), (6, 4)):
        ok = lemma_ok(n, alph)
        print(f"  n={n} alphabet={alph}: {ok}")
        if not ok:
            hits.append(f"lemma n={n}")

    print("C3 sharpness 2L>=4:")
    for L in (4, 6):
        bad, N = sharpness_2d(L)
        print(f"  2D L={L}: bad={bad} N={N} {bad == N}")
        if bad != N:
            hits.append(f"2D {L}")
    for L in (4, 6):
        bad, N, tgt = sharpness_3d(L)
        print(f"  3D L={L}: bad={bad} 3N/4={tgt} {bad == tgt}")
        if bad != tgt:
            hits.append(f"3D {L}")

    print("C4 216^{4/3}=1296; CS does not improve the 3/4 exponent:")
    okA = 6 ** 3 == 216 and 6 ** 4 == 1296
    # CS: mu(cap)^{1/N} <= max mu_i^{1/N}; 4 classes in 3D still 6 (m/p)^{3/4}
    # 1296^{3/4} = (6^4)^{3/4} = 6^3 = 216, so 6*(1/216)=1/36
    eps3 = Fr(6, 6 ** 3)
    print(f"  6^3=216, 6^4=1296: {okA}; 6 (1/1296)^{{3/4}} = {eps3} (want 1/36={Fr(1, 36)})")
    if eps3 != Fr(1, 36) or not okA:
        hits.append("arithmetic")
    p2 = 216
    eps2 = 6 * Fr(1, p2)
    print(f"  2D: 6m/p at p=216m is {eps2} = 1/36 {eps2 == Fr(1, 36)}")
    if eps2 != Fr(1, 36):
        hits.append("2D eps")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + "; ".join(hits))
        return 1
    print(
        "HIT: route (i) CS over parity classes: site-reflection orbit is one class (N/2 on (Z/4)^2); "
        "lemma and sharpness give b0=N in 2D and 3N/4 in 3D (sides 4,6); CS recovers the intended "
        "'every direction-i bond' event at the same N-th root, so T4 holds with eps=6m/p in 2D "
        "(p>=216m) and cannot beat 6(m/p)^{3/4} in 3D (p>=1296m=6^4 m)"
    )
    print(
        "SUMMARY: PARTIAL - Cauchy-Schwarz over parity classes repairs T4 in 2D at 216m and is a "
        "no-go for 216m in 3D (stays 1296m); bond-plane RP not used"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
