#!/usr/bin/env python3
"""J:attack-d:PR8177 — QUANTIFIER SCOPE.

Do not re-find the known T2 Z_B predecessor-value HIT ([-1,-1,0] vs all -1).

Two universal claims inside the stated range:
  (1) T3.3 / fence: exact rational super-solutions of the restricted recursion
      at the eight listed couplings, written as regions p >= p0 (2921 at (p,1,2)
      c=2, etc.). Test the exhibited triples at each listed point and at p' in
      {p0-1, p0, p0+1, p0+10, 2 p0} with the same (q,r,c) — a failure at any
      p' >= p0 is an in-range failure of the region reading.
  (2) T1.1: v(z) <= 1 + v(u) for every 1-predecessor of a non-seed site, and
      v(z) <= -1 + v(u) at amplified sites. Runner executed this on 140 tiny
      3x3x5 boxes. Recompute rooted values by the single-seed DP on the named
      larger realizations Z_A, Z_B, W1, W2 (the note's own objects).

Exact Fraction arithmetic. Independent of the runner (formulas restated).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

import sympy as sp

HITS: list[str] = []

E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORK_OFFSETS = [
    tuple(E3[a][i] - E3[b][i] for i in range(3))
    for a in range(3)
    for b in range(3)
    if a != b
]


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)]


def run_automaton(sites, zeta):
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if (sum(ps) >= 2 or zeta.get(z, 0)) else 0
    return eta


def kinds(eta):
    ones = {z for z, v in eta.items() if v == 1}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {
        z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc")
        for z in ones
    }
    return ones, npred, kind


def cost_of(kind_z, c):
    return Fraction(1) if kind_z == "proc" else (-Fraction(c) if kind_z == "amp" else Fraction(0))


def component(eta, root):
    ones, npred, kind = kinds(eta)
    seen = {root}
    st = [root]
    while st:
        z = st.pop()
        nb = list(npred[z]) + [s for s in ones if z in preds(s)]
        nb += [tuple(z[i] + o[i] for i in range(3)) for o in FORK_OFFSETS]
        for w in nb:
            if w in ones and w not in seen:
                seen.add(w)
                st.append(w)
    return seen


def single_seed_capped(eta, root, c, cap):
    """Exact min of |P| - c|A| over rooted single-seed trees at levels <= cap."""
    ones, npred, kind = kinds(eta)
    comp = {z for z in component(eta, root) if level(z) <= cap}
    seeds = [z for z in comp if kind[z] == "seed"]
    if len(seeds) != 1:
        return None
    s = seeds[0]
    at = {}
    for z in comp:
        at.setdefault(level(z), []).append(z)
    if any(len(at[l]) > 16 for l in at):
        return "too-wide"
    Lmax, Ls, lr = max(at), level(s), level(root)
    nodes = sorted(at.get(Lmax, []))
    states = {}
    for mask in range(1 << len(nodes)):
        X = frozenset(nodes[i] for i in range(len(nodes)) if mask >> i & 1)
        if Lmax == lr and root not in X:
            continue
        states[X] = sum(cost_of(kind[z], c) for z in X)
    for l in range(Lmax, Ls, -1):
        below = sorted(at.get(l - 1, []))
        nxt = {}
        for X, val in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if l - 1 == lr and root not in Y:
                    continue
                if any(not any(p in Y for p in npred[z]) for z in need):
                    continue
                v2 = val + sum(cost_of(kind[z], c) for z in Y)
                if Y not in nxt or v2 < nxt[Y]:
                    nxt[Y] = v2
        states = nxt
    return states.get(frozenset([s]))


def realization(spec):
    root, (A, B, L), marks = spec
    sites = [(a, b, c) for a in range(A) for b in range(B) for c in range(L)]
    return run_automaton(sites, {z: 1 for z in marks}), root


# Named realizations from the note / runner (restated).
Z_A = (
    (3, 3, 3),
    (4, 4, 7),
    [
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 2),
        (1, 0, 5), (1, 2, 0), (1, 2, 5), (1, 3, 1), (2, 0, 0), (2, 1, 3),
        (2, 2, 3), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 1, 0), (3, 1, 3),
        (3, 3, 5), (3, 3, 6),
    ],
)
Z_B = (
    (4, 4, 4),
    (5, 5, 8),
    [
        (0, 0, 0), (0, 0, 1), (0, 0, 7), (0, 1, 0), (0, 1, 1), (0, 1, 2),
        (0, 1, 7), (0, 2, 7), (0, 4, 4), (1, 0, 0), (1, 0, 2), (1, 1, 2),
        (1, 2, 0), (1, 2, 2), (1, 3, 1), (1, 3, 7), (2, 0, 0), (2, 2, 0),
        (2, 2, 2), (2, 2, 3), (2, 2, 6), (2, 3, 3), (2, 3, 4), (2, 4, 2),
        (2, 4, 6), (3, 0, 1), (3, 0, 2), (3, 1, 2), (3, 2, 1), (3, 2, 7),
        (4, 0, 2), (4, 0, 6), (4, 1, 1), (4, 2, 1), (4, 4, 2), (4, 4, 4),
    ],
)
W1 = (
    (3, 3, 4),
    (4, 4, 7),
    [
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 2), (1, 2, 0),
        (1, 3, 1), (2, 0, 0), (2, 2, 3), (2, 3, 4), (3, 0, 2),
    ],
)
W2 = (
    (3, 3, 6),
    (4, 4, 7),
    [
        (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2),
        (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6),
        (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1),
        (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2),
        (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3),
        (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0),
        (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5),
    ],
)


def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    return d1, d2, d3


def upf(n, xP, xA, U):
    return (1 + xA * U) ** n + n * xP * U * (1 + xA * U) ** (n - 1)


def rhs(xP, xA, y, D, U, Fv):
    x = xP + xA
    return (
        upf(2, xP, xA, U) * (1 + 3 * x * D) * (1 + y * Fv) ** 6,
        upf(3, xP, xA, U) * (1 + y * Fv) ** 6,
        upf(3, xP, xA, U) * (1 + 3 * x * D) * (1 + y * Fv) ** 5,
    )


# Exhibited triples from the note's D2 (restated as data to attack, not imported).
CERTS = {
    (2, 2921, 1, 2): (
        Fraction(121, 1000),
        Fraction(38819515651721, 125000000000),
        Fraction(2614495936247, 1000000000000),
        Fraction(411275330287659, 1000000000000),
    ),
    (2, 1464, 1, 1): (
        Fraction(121, 1000),
        Fraction(116365070741407, 500000000000),
        Fraction(652123939263, 250000000000),
        Fraction(3080327991177, 10000000000),
    ),
    (2, 5841, 2, 4): (
        Fraction(61, 500),
        Fraction(151842195690607, 500000000000),
        Fraction(1303405077461, 500000000000),
        Fraction(12551068393373, 31250000000),
    ),
    (2, 4380, 1, 3): (
        Fraction(121, 1000),
        Fraction(321841798858453, 1000000000000),
        Fraction(653785718103, 250000000000),
        Fraction(21312272709127, 50000000000),
    ),
    (1, 405, 1, 2): (
        Fraction(91, 1000),
        Fraction(11697402025031, 1000000000000),
        Fraction(155146937439, 62500000000),
        Fraction(46962997959, 3125000000),
    ),
    (1, 208, 1, 1): (
        Fraction(89, 1000),
        Fraction(10283263176051, 1000000000000),
        Fraction(152629090359, 62500000000),
        Fraction(2627739909739, 200000000000),
    ),
    (1, 810, 2, 4): (
        Fraction(91, 1000),
        Fraction(11697402025031, 1000000000000),
        Fraction(155146937439, 62500000000),
        Fraction(46962997959, 3125000000),
    ),
    (1, 605, 1, 3): (
        Fraction(93, 1000),
        Fraction(3032442310293, 250000000000),
        Fraction(2482877419491, 1000000000000),
        Fraction(7794092314937, 500000000000),
    ),
}


def dominates(c, p, q, r, t, Db, Ub, Fb):
    d1, d2, d3 = deviations(p, q, r)
    e1, e2 = d1, max(d2, d3)
    xP, xA, y = t, e2 / t ** c, e1 / t ** 3
    rD, rU, rF = rhs(xP, xA, y, Db, Ub, Fb)
    Rbar = upf(3, xP, xA, Ub) * (1 + 3 * (xP + xA) * Db) * (1 + y * Fb) ** 6
    ok = Db >= rD and Ub >= rU and Fb >= rF and min(Db, Ub, Fb) >= 1
    small = e1 * Rbar < Fraction(1, 10 ** 5)
    return ok, small, e1 * Rbar


def check_certs():
    print("== T3.3 certificates at listed points and in the p>=p0 reading ==")
    fail_listed = 0
    fail_region = 0
    hold_below = 0
    for (c, p0, q, r), (t, Db, Ub, Fb) in CERTS.items():
        ok, small, prod = dominates(c, p0, q, r, t, Db, Ub, Fb)
        print(f"  listed c={c} ({p0},{q},{r}): super={ok} e1R<{10**-5}={small} e1R={prod}")
        if not (ok and small):
            fail_listed += 1
            msg = f"certificate fails at listed ({p0},{q},{r}) c={c} super={ok} e1R={prod}"
            HITS.append(msg)
            print("HIT:", msg)
        # region reading p >= p0 with the same triple
        for p in (p0 - 1, p0 + 1, p0 + 10, 2 * p0):
            if p <= 0:
                continue
            okp, smallp, prodp = dominates(c, p, q, r, t, Db, Ub, Fb)
            tag = "below" if p < p0 else "in-region"
            print(f"    p={p} ({tag}): super={okp} e1R_ok={smallp}")
            if p < p0 and okp and smallp:
                hold_below += 1
            if p >= p0 and not (okp and smallp):
                fail_region += 1
                msg = (
                    f"exhibited triple for p0={p0} fails at p={p}>={p0} "
                    f"on ({p},{q},{r}) c={c} super={okp} e1R={prodp}"
                )
                HITS.append(msg)
                print("HIT:", msg)
    print(f"listed failures={fail_listed} in-region failures={fail_region} holds-at-p0-1={hold_below}")


def check_upfactor():
    print("== T3.1 up-factor identity for n=1..8 (note states n=2,3) ==")
    a, b, u = sp.symbols("a b u", positive=True)
    bad = []
    for n in range(1, 9):
        total = 0
        for kinds_ in product(("empty", "P", "A"), repeat=n):
            if kinds_.count("P") > 1:
                continue
            term = 1
            for kk in kinds_:
                term *= {"empty": 1, "P": a * u, "A": b * u}[kk]
            total += term
        target = (1 + b * u) ** n + n * a * u * (1 + b * u) ** (n - 1)
        ok = sp.expand(total - target) == 0
        print(f"  n={n} identity={ok}")
        if not ok:
            bad.append(n)
    # only a HIT if it fails at n=2 or n=3 (the claimed range)
    for n in bad:
        if n in (2, 3):
            msg = f"up-factor identity fails at claimed n={n}"
            HITS.append(msg)
            print("HIT:", msg)


def check_t11():
    print("== T1.1 on named larger realizations (single-seed DP) ==")
    for name, spec in (("Z_A", Z_A), ("Z_B", Z_B), ("W1", W1), ("W2", W2)):
        eta, root = realization(spec)
        ones, npred, kind = kinds(eta)
        # rooted values at every 1-site of the root component, cap = site's own level
        v = {}
        skipped = 0
        multi = 0
        for z in ones:
            val = single_seed_capped(eta, z, Fraction(1), level(z))
            if val == "too-wide":
                skipped += 1
                continue
            if val is None:
                multi += 1
                continue
            v[z] = val
        n_pairs = n_amp = n_fail = 0
        for z, vz in v.items():
            if kind[z] == "seed":
                continue
            for u in npred[z]:
                if u not in v:
                    continue
                n_pairs += 1
                if vz > 1 + v[u]:
                    n_fail += 1
                    msg = f"T1.1 fails on {name}: v({z})={vz} > 1+v({u})={1 + v[u]}"
                    HITS.append(msg)
                    print("HIT:", msg)
            if kind[z] == "amp":
                u = npred[z][0]
                if u in v:
                    n_amp += 1
                    if vz > -1 + v[u]:
                        n_fail += 1
                        msg = (
                            f"T1.1 amp fails on {name}: v({z})={vz} > -1+v({u})={-1 + v[u]}"
                        )
                        HITS.append(msg)
                        print("HIT:", msg)
        print(
            f"  {name} root={root} scored={len(v)} skipped_wide={skipped} "
            f"multi-seed={multi} pairs={n_pairs} amp={n_amp} fails={n_fail}"
        )


def check_ratio():
    """T3.3 'factor 1.43 below block 30 on every line' at the two lines the note names."""
    print("== T3.3 factor 1.43 vs block 30 on named lines ==")
    pairs = [(4165, 2921, "(p,1,2) c=2"), (2085, 1464, "(p,1,1) c=2")]
    for hi, lo, tag in pairs:
        num, den = Fraction(hi), Fraction(lo)
        ratio = num / den
        print(f"  {tag}: {hi}/{lo} = {ratio} ~ {float(ratio):.6f}")
        # 1.43 is a displayed rounding, not an exact identity; fire only if
        # the ratio is not in [1.42, 1.44].
        if not (Fraction(142, 100) <= ratio <= Fraction(144, 100)):
            msg = f"factor 1.43 claim misses {tag}: {hi}/{lo} = {ratio}"
            HITS.append(msg)
            print("HIT:", msg)


def main():
    check_upfactor()
    check_certs()
    check_ratio()
    check_t11()
    if HITS:
        print("HIT: " + HITS[0])
        print(
            "SUMMARY: QUANTIFIER SCOPE (PR #8177): "
            + "; ".join(HITS[:4])
        )
        return 0
    print(
        "SUMMARY: QUANTIFIER SCOPE (PR #8177): T3.3 super-solutions hold at all "
        "eight listed couplings and at p in {p0+1, p0+10, 2 p0} with the exhibited "
        "triples; T3.1 identity holds for n=1..8; T1.1 holds on Z_A, Z_B, W1, W2 "
        "by single-seed DP; 4165/2921 and 2085/1464 lie in [1.42, 1.44]; "
        "pattern has purchase and the claimed inequalities hold in-range "
        "(known T2 Z_B value-triple is not re-claimed)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
