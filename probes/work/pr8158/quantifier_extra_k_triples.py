#!/usr/bin/env python3
"""J:attack-d:PR8158 — QUANTIFIER SCOPE.

Do not re-find the known Q4(a) triangle-not-a-Z^3-window HIT.

Q2 is for every one-attachment component / every positive rule (executed:
pendant paths of length 2,3). Q3(c) is φ^{k+2} for every k (executed k<=3).
Q3(b) φ² constant iff p=q=r for every positive triple. Q5: R1=R2 whenever
every component of E is pendant, for every non-constant rule (Q4(c) only
at (2,1,2)). Sphere: sinh(z)/z increasing for every z>0 (series n<=10).

Look inside those quantifiers: extra k, extra pendant shapes (including
two-bond attachment), extra (p,q,r), extra series n. HIT if an identity
or inequality fails at a value in the stated range.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import factorial

import sympy as sp

MENU = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def phi_of(v, w, p, q, r):
    if v == w:
        return p
    if v == (-w[0], -w[1], -w[2]):
        return q
    return r


def phi_matrix(p, q, r):
    return sp.Matrix(6, 6, lambda i, j: phi_of(MENU[i], MENU[j], p, q, r))


def sector_basis():
    odd = [
        sp.Matrix([1 if k == 2 * i else (-1 if k == 2 * i + 1 else 0) for k in range(6)])
        for i in range(3)
    ]
    even = [
        sp.Matrix([1, 1, -1, -1, 0, 0]),
        sp.Matrix([1, 1, 0, 0, -1, -1]),
    ]
    return odd, even


def check_path_powers() -> None:
    print("== Q3(c) path φ^{k+2} eigenvalues beyond executed k<=3 ==")
    p, q, r = sp.symbols("p q r", positive=True)
    Phi = phi_matrix(p, q, r)
    odd, even = sector_basis()
    for k in (0, 4, 5, 6, 7, 8):
        Pk = sp.expand(Phi ** (k + 2))
        ok_odd = all(
            sp.simplify(Pk * f - (p - q) ** (k + 2) * f) == sp.zeros(6, 1) for f in odd
        )
        ok_even = all(
            sp.simplify(Pk * g - (p + q - 2 * r) ** (k + 2) * g) == sp.zeros(6, 1)
            for g in even
        )
        print(f"  k={k}: odd (p-q)^{k+2}={ok_odd} even (p+q-2r)^{k+2}={ok_even}")
        if not (ok_odd and ok_even):
            hit(
                f"Q3(c) path of k={k} internal bonds: Phi^{k+2} is not "
                f"(p-q)^{k+2} / (p+q-2r)^{k+2} on the odd/even sectors "
                f"(executed only k<=3; claimed for every k)"
            )
    # constancy iff p=q=r on extra integer triples, via entry differences of Phi^{k+2}
    triples = [
        (3, 1, 2),
        (5, 2, 4),
        (2, 1, 2),
        (2, 2, 1),
        (4, 4, 1),
        (1, 1, 1),
        (7, 3, 5),
        (6, 1, 1),
    ]
    print("== Q3(c) Phi^{k+2} constant iff p=q=r, extra triples ==")
    for k in (0, 4, 6):
        for tr in triples:
            Pnum = phi_matrix(*tr) ** (k + 2)
            entries = {sp.Integer(Pnum[i, j]) for i in range(6) for j in range(6)}
            const = len(entries) == 1
            expect = tr[0] == tr[1] == tr[2]
            print(f"  k={k} {tr}: constant={const} expect={expect}")
            if const != expect:
                hit(
                    f"Q3(c) at {tr} k={k}: Phi^{k+2} constant={const} "
                    f"but p=q=r is {expect}"
                )


def check_phi2_grid() -> None:
    print("== Q3(b) φ² differences vanish iff p=q=r on 1..4^3 ==")
    p, q, r = sp.symbols("p q r", positive=True)
    Phi2 = phi_matrix(p, q, r) ** 2
    d_same = sp.factor(sp.expand(Phi2[0, 0] - Phi2[0, 2]))
    d_anti = sp.factor(sp.expand(Phi2[0, 1] - Phi2[0, 2]))
    n_bad = 0
    n = 0
    for a, b, c in product(range(1, 5), repeat=3):
        n += 1
        ds = d_same.subs({p: a, q: b, r: c})
        da = d_anti.subs({p: a, q: b, r: c})
        vanish = sp.Integer(ds) == 0 and sp.Integer(da) == 0
        expect = a == b == c
        if vanish != expect:
            n_bad += 1
            hit(f"Q3(b) at {(a, b, c)}: diffs vanish={vanish} but p=q=r is {expect}")
            if n_bad >= 3:
                break
    print(f"  scanned {n} positive triples; mismatches={n_bad}")


def pendant_factor_sym(length: int, vb, p, q, r):
    total = 0
    for u in product(range(6), repeat=length):
        w = phi_of(vb, MENU[u[0]], p, q, r)
        for i in range(length - 1):
            w = w * phi_of(MENU[u[i]], MENU[u[i + 1]], p, q, r)
        total = total + w
    return sp.expand(total)


def check_pendants() -> None:
    print("== Q2 pendant paths extra lengths 1,4,5 ==")
    p, q, r = sp.symbols("p q r", positive=True)
    for length in (1, 4, 5):
        vals = [pendant_factor_sym(length, vb, p, q, r) for vb in MENU]
        same = all(sp.simplify(vals[0] - v) == 0 for v in vals[1:])
        print(f"  length={length}: constant in v_b: {same}")
        if not same:
            hit(
                f"Q2 pendant path of {length} unrecorded sites: F depends on v_b "
                f"(claimed for every one-attachment component; executed only 2,3)"
            )


def check_two_bond_attachment() -> None:
    """Pendant blob with two bonds from one recorded site: origin plus
    (1,0,0),(0,1,0),(1,1,0). ∂C = {origin}, |E|=3. Q2: F independent of v_b.
    Not a path; not Q4(a)."""
    print("== Q2 two-bond pendant (L with corner) at extra triples ==")
    E = ((1, 0, 0), (0, 1, 0), (1, 1, 0))
    bonds_int = [((1, 0, 0), (1, 1, 0)), ((0, 1, 0), (1, 1, 0))]
    attach = ((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (0, 1, 0))
    triples = [(3, 1, 2), (5, 2, 4), (2, 1, 2), (2, 2, 1), (1, 1, 1), (4, 4, 1)]
    for tr in triples:
        p, q, r = tr
        Fs = []
        for vb in MENU:
            tot = 0
            for u in product(MENU, repeat=3):
                rec = dict(zip(E, u))
                rec[(0, 0, 0)] = vb
                w = 1
                for a, b in bonds_int:
                    w *= phi_of(rec[a], rec[b], p, q, r)
                for a, b in attach:
                    w *= phi_of(rec[a], rec[b], p, q, r)
                tot += w
            Fs.append(tot)
        ok = len(set(Fs)) == 1
        print(f"  {tr}: F values {Fs[:2]}... unique={len(set(Fs))} constant={ok}")
        if not ok:
            hit(
                f"Q2 two-bond attachment at {tr}: F depends on v_b "
                f"(values {sorted(set(Fs))[:4]}); claimed for any number of bonds"
            )


def check_forest_tv() -> None:
    """Q4(c)/Q2: plaquette plus two pendant components, TV(R1,R2)=0.
    Executed only at (2,1,2). Extra triples, not Q4(a)."""
    print("== Q2/Q4(c) two-pendant forest TV=0 at extra triples ==")
    # W plaquette; E: (2,0,0)-(3,0,0) off (1,0,0); (0,2,0) off (0,1,0)
    W = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
    E1 = ((2, 0, 0), (3, 0, 0))
    E2 = ((0, 2, 0),)
    sites = W + E1 + E2
    bonds = [
        ((0, 0, 0), (1, 0, 0)),
        ((1, 0, 0), (1, 1, 0)),
        ((1, 1, 0), (0, 1, 0)),
        ((0, 1, 0), (0, 0, 0)),
        ((1, 0, 0), (2, 0, 0)),
        ((2, 0, 0), (3, 0, 0)),
        ((0, 1, 0), (0, 2, 0)),
    ]
    idx = {s: i for i, s in enumerate(sites)}
    nW = 4
    triples = [(2, 1, 2), (3, 1, 2), (5, 2, 4), (1, 1, 1)]
    for tr in triples:
        p, q, r = tr
        # R1 on W: 6^4
        w1 = {}
        z1 = 0
        for u in product(range(6), repeat=nW):
            rec = {W[i]: MENU[u[i]] for i in range(nW)}
            wt = 1
            for a, b in bonds[:4]:
                wt *= phi_of(rec[a], rec[b], p, q, r)
            w1[u] = wt
            z1 += wt
        # R2: sum E, 6^7
        w2 = {u: 0 for u in w1}
        z2 = 0
        for u in product(range(6), repeat=len(sites)):
            rec = {sites[i]: MENU[u[i]] for i in range(len(sites))}
            wt = 1
            for a, b in bonds:
                wt *= phi_of(rec[a], rec[b], p, q, r)
            key = u[:nW]
            w2[key] += wt
            z2 += wt
        tv = F(0)
        for key in w1:
            tv += abs(F(w1[key], z1) - F(w2[key], z2))
        tv /= 2
        print(f"  {tr}: TV(R1,R2)={tv}")
        if tv != 0:
            hit(
                f"Q2/Q4(c) forest at {tr}: TV(R1,R2)={tv} != 0 "
                f"(claimed R1=R2 for every pendant exterior; executed TV=0 only at (2,1,2))"
            )


def check_sphere_series() -> None:
    print("== Q3(e) series coefficients beyond n<=10; antipodal w=0 ==")
    z = sp.symbols("z", positive=True)
    series = sp.series(z * sp.cosh(z) - sp.sinh(z), z, 0, 44).removeO()
    for n in range(11, 21):
        coeff = series.coeff(z, 2 * n + 1)
        want = 2 * n / sp.factorial(2 * n + 1)
        ok = sp.simplify(coeff - want) == 0 and coeff > 0
        if n <= 12:
            print(f"  n={n}: coeff={coeff} want={want} ok={ok}")
        if not ok:
            hit(
                f"Q3(e) series n={n}: coeff {coeff} != 2n/(2n+1)! or not >0 "
                f"(claimed for every n>=1; executed n<=10)"
            )
    # antipodes: written 4π sinh(β|w|)/(β|w|) with |w|=0
    b = sp.symbols("beta", positive=True)
    t = sp.symbols("t")
    integral_w0 = 2 * sp.pi * sp.integrate(sp.Integer(1), (t, -1, 1))
    print(f"  antipodal integral 2π ∫_{-1}^1 1 dt = {integral_w0} (should be 4π)")
    if sp.simplify(integral_w0 - 4 * sp.pi) != 0:
        hit(f"antipodal sphere integral {integral_w0} != 4π")
    # the written closed form is undefined at w=0; the continuous extension is 4π
    # (limit sinh(x)/x → 1). Not scored as a HIT: removable, and the proof
    # restricts to w≠0. Record the limit.
    lim = sp.limit(4 * sp.pi * sp.sinh(b * z) / (b * z), z, 0)
    print(f"  lim_{{w→0}} 4π sinh(βw)/(βw) = {lim}")
    if sp.simplify(lim - 4 * sp.pi) != 0:
        hit(f"sphere factor limit at w=0 is {lim} != 4π")


def main() -> int:
    check_path_powers()
    check_phi2_grid()
    check_pendants()
    check_two_bond_attachment()
    check_forest_tv()
    check_sphere_series()
    if HITS:
        print("SUMMARY: QUANTIFIER SCOPE (PR #8158): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: QUANTIFIER SCOPE (PR #8158): Q3(c) φ^{k+2} odd/even eigenvalues "
        "and constancy iff p=q=r hold for k=0,4..8 and extra triples including "
        "(2,2,1) and (1,1,1); Q3(b) differences vanish iff p=q=r on 1..4^3; "
        "Q2 pendant F is independent of v_b at lengths 1,4,5 and on a two-bond "
        "blob; forest TV(R1,R2)=0 at extra triples; sphere series coeffs n=11..20 "
        "stay 2n/(2n+1)! > 0; not the Q4(a) triangle HIT; pattern has purchase "
        "and does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
