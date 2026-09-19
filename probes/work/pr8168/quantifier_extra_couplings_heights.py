#!/usr/bin/env python3
"""J:attack-d:PR8168 — pattern (d) QUANTIFIER SCOPE.

T0's noise map and T7's thresholds are proved for every positive (p, q, r)
and every integer p ≥ p0 on four lines; B3/B4 executed the 216-triple max
only at (3,1,2), (10,1,2), (30,1,2) and (5,2,4), E2 only at the four p0.
T5's super-solution is proved for every height h; E1 compared the generating
function only through five edges. T6 is for every ε ≤ ε0 = 7/10^6.

Look inside those ranges at extra couplings, extra p, extra values a, extra
heights, extra ε. HIT if an inequality the note asserts for every such
parameter fails at a value in range.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

HITS: list[str] = []

MENU = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORKS = tuple(
    tuple(E3[i][k] - E3[j][k] for k in range(3))
    for i in range(3)
    for j in range(3)
    if i != j
)
EPS0 = F(7, 10**6)
RBAR_CAP = F(391, 100)
P0 = {(1, 2): 285718, (1, 1): 142861, (2, 4): 571436, (1, 3): 428576}


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def phi(v, w, p, q, r):
    if v == w:
        return p
    if tuple(-c for c in v) == w:
        return q
    return r


def K(a, triple, p, q, r):
    num = 1
    for w in triple:
        num *= phi(a, w, p, q, r)
    den = 0
    for v in MENU:
        t = 1
        for w in triple:
            t *= phi(v, w, p, q, r)
        den += t
    return F(num, den)


def deviations(p, q, r):
    d1 = 1 - F(p**3, p**3 + q**3 + 4 * r**3)
    d2 = 1 - F(p**2 * q, p * q * (p + q) + 4 * r**3)
    d3 = 1 - F(p**2 * r, r * (p**2 + q**2) + r**2 * (p + q) + 2 * r**3)
    return d1, d2, d3


def eps_closed(p, q, r):
    return max(deviations(p, q, r))


def eps_triples(a, p, q, r):
    worst = F(0)
    n = 0
    for triple in product(MENU, repeat=3):
        if sum(1 for w in triple if w == a) < 2:
            continue
        n += 1
        worst = max(worst, 1 - K(a, triple, p, q, r))
    return worst, n


def M(k, z):
    return F(z[k]) - F(sum(z), 3)


def add(u, v):
    return (u[0] + v[0], u[1] + v[1], u[2] + v[2])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def least_p(q, r, cap=10**9):
    lo, hi = 1, cap
    while lo < hi:
        mid = (lo + hi) // 2
        if eps_closed(mid, q, r) <= EPS0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def rhs(D, U, Fv, t, s):
    Dn = (1 + t * U) ** 2 * (1 + 3 * t * D) * (1 + s * Fv) ** 6
    Un = (1 + t * U) ** 3 * (1 + s * Fv) ** 6
    Fn = (1 + t * U) ** 3 * (1 + 3 * t * D) * (1 + s * Fv) ** 5
    Rn = (1 + t * U) ** 3 * (1 + 3 * t * D) * (1 + s * Fv) ** 6
    return Dn, Un, Fn, Rn


def gf_R(A, FM):
    """Truncated [t^a s^f] of R, same recursion as the note, beyond the executed 5-edge cutoff."""

    def pmul(P, Q):
        R = {}
        for (a1, f1), c1 in P.items():
            for (a2, f2), c2 in Q.items():
                if a1 + a2 <= A and f1 + f2 <= FM:
                    R[(a1 + a2, f1 + f2)] = R.get((a1 + a2, f1 + f2), 0) + c1 * c2
        return R

    def ppow(P, n):
        R = {(0, 0): 1}
        for _ in range(n):
            R = pmul(R, P)
        return R

    def one_plus(P, c, da, df):
        R = {(0, 0): 1}
        for (a, f), v in P.items():
            if a + da <= A and f + df <= FM:
                R[(a + da, f + df)] = R.get((a + da, f + df), 0) + c * v
        return R

    D = U = Fv = {(0, 0): 1}
    for _ in range(A + FM + 1):
        xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fv, 1, 0, 1)
        D = pmul(pmul(ppow(xU, 2), xD3), ppow(yF, 6))
        U = pmul(ppow(xU, 3), ppow(yF, 6))
        Fv = pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 5))
    xU, xD3, yF = one_plus(U, 1, 1, 0), one_plus(D, 3, 1, 0), one_plus(Fv, 1, 0, 1)
    return pmul(pmul(ppow(xU, 3), xD3), ppow(yF, 6))


def main() -> int:
    # --- T0 / T7: extra couplings, extra a, extra p ---
    extra_pqr = [
        (3, 1, 2),
        (10, 1, 2),
        (30, 1, 2),
        (5, 2, 4),
        (285718, 1, 2),
        (285717, 1, 2),
        (142861, 1, 1),
        (571436, 2, 4),
        (428576, 1, 3),
        (400000, 1, 2),
        (10**6, 1, 2),
        (2, 1, 2),
        (1, 1, 1),
        (7, 3, 5),
        (F(5, 2), F(1, 3), F(7, 4)),
        (F(11, 2), F(2, 7), F(9, 5)),
        (100, 1, 10),
        (50, 50, 1),
        (8, 1, 1),
        (9, 2, 1),
    ]
    n_qual = None
    for p, q, r in extra_pqr:
        formula = eps_closed(p, q, r)
        for a in MENU:
            worst, n = eps_triples(a, p, q, r)
            if n_qual is None:
                n_qual = n
            if n != 16:
                hit(f"triples with ≥2 copies of {a} number {n}, not 16")
                break
            if worst != formula:
                hit(
                    f"ε triples {worst} != closed {formula} at (p,q,r)=({p},{q},{r}) a={a}"
                )
                break
            if worst > formula:
                hit(f"triple max exceeds closed forms at ({p},{q},{r}) a={a}")
                break
        else:
            print(f"OK T0: max over 16 triples = max(d1,d2,d3)={formula} at ({p},{q},{r}) for all 6 values a")
            continue
        break
    else:
        print(f"OK T0: {len(extra_pqr)} couplings × 6 values a; qualifying triples per a = {n_qual}")

    for (q, r), p0 in P0.items():
        e_at = eps_closed(p0, q, r)
        e_below = eps_closed(p0 - 1, q, r)
        print(f"T7(b) (p,{q},{r}): p0={p0} ε(p0)={e_at} ε(p0-1)={e_below} ε0={EPS0}")
        if not (e_at <= EPS0 < e_below):
            hit(f"threshold fails at (p,{q},{r}): ε({p0})={e_at} ε({p0-1})={e_below} vs ε0={EPS0}")
        if least_p(q, r) != p0:
            hit(f"least p at ({q},{r}) is {least_p(q, r)} not {p0}")
        for p in (p0, p0 + 1, p0 + 17, p0 * 2, 10**6 if 10**6 >= p0 else p0 + 10**5):
            e = eps_closed(p, q, r)
            if e > EPS0:
                hit(f"ε({p},{q},{r})={e} > ε0 inside the claimed p≥{p0} range")
            if p > p0 and e >= eps_closed(p - 1, q, r):
                hit(f"ε not strictly decreasing at p={p} on ({q},{r})")

    extra_lines = ((1, 4), (2, 2), (3, 1), (5, 5), (1, 10), (4, 1), (2, 3))
    for q, r in extra_lines:
        p0 = least_p(q, r)
        e_at = eps_closed(p0, q, r)
        e_below = eps_closed(p0 - 1, q, r)
        print(f"extra line (p,{q},{r}): least p={p0} ε(p0)≤ε0={e_at <= EPS0} ε(p0-1)>ε0={e_below > EPS0}")
        if not (e_at <= EPS0 < e_below):
            hit(f"least-p cut fails on extra line ({q},{r}) at p0={p0}")
        if p0 >= 2 and eps_closed(p0, q, r) >= eps_closed(p0 - 1, q, r):
            hit(f"ε not decreasing across extra-line threshold ({q},{r})")
        # T0 triples at the extra-line threshold (one a suffices; covariance checked above)
        worst, _ = eps_triples(MENU[0], p0, q, r)
        if worst != e_at:
            hit(f"triple max {worst} != closed {e_at} at extra-line p0=({p0},{q},{r})")

    # --- T6: every ε ≤ ε0 ---
    t = F(91, 1000)
    s = F(1000, 107653)
    Db = F(3290957526219, 10**12)
    Ub = F(514547476033, 25 * 10**10)
    Fb = F(943741493637, 25 * 10**10)
    rD = (1 + t * Ub) ** 2 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6
    rU = (1 + t * Ub) ** 3 * (1 + s * Fb) ** 6
    rF = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 5
    Rbar = (1 + t * Ub) ** 3 * (1 + 3 * t * Db) * (1 + s * Fb) ** 6
    print(f"T5 cert: D≥RHS {Db >= rD} U≥RHS {Ub >= rU} F≥RHS {Fb >= rF} Rbar={Rbar} < 391/100 {Rbar < RBAR_CAP}")
    if not (Db >= rD and Ub >= rU and Fb >= rF and min(Db, Ub, Fb) >= 1):
        hit("super-solution inequalities fail at the stated bars")
    if Rbar >= RBAR_CAP:
        hit(f"Rbar={Rbar} not < 391/100")
    if t**3 * s != EPS0:
        hit(f"t^3 s = {t**3 * s} != ε0")
    if RBAR_CAP * EPS0 != F(2737, 10**8):
        hit("(391/100)ε0 != 2737/10^8")
    if F(2737, 10**8) >= F(3, 10**5):
        hit("2737/10^8 not < 3/10^5")

    eps_grid = [F(0), F(1, 10**12), F(1, 10**8), F(1, 10**7), EPS0 / 2, EPS0 * F(99, 100), EPS0]
    for eps in eps_grid:
        if eps * Rbar >= RBAR_CAP * eps and eps > 0:
            hit(f"ε Rbar not < (391/100)ε at ε={eps}")
        if RBAR_CAP * eps > F(3, 10**5):
            hit(f"(391/100)ε={RBAR_CAP * eps} > 3/10^5 at ε={eps} ≤ ε0")
        if eps > 0 and eps / (t**3) > s:
            hit(f"ε/t^3={eps / t**3} > s at ε={eps} ≤ ε0")
        print(f"OK T6: ε={eps}  ε·Rbar={eps * Rbar}  (391/100)ε={RBAR_CAP * eps}  ≤3/10^5 {RBAR_CAP * eps <= F(3, 10**5)}")

    # --- T5: extra heights / extra interior points of the super-solution box ---
    t = F(91, 1000)
    s = F(1000, 107653)
    interiors = [
        (F(1), F(1), F(1)),
        (F(2), F(2), F(2)),
        ((1 + Db) / 2, (1 + Ub) / 2, (1 + Fb) / 2),
        (Db, Ub, Fb),
        (F(3), F(2), F(3)),
    ]
    D = U = Fv = F(1)
    for h in range(1, 4):
        D, U, Fv, Rn = rhs(D, U, Fv, t, s)
        print(f"T5 height {h}: D≤Dbar {D <= Db} U≤Ubar {U <= Ub} F≤Fbar {Fv <= Fb} R_h<391/100 {Rn < RBAR_CAP}")
        if D > Db or U > Ub or Fv > Fb or Rn >= RBAR_CAP:
            hit(f"recursion exceeds super-solution at height {h}")
            break
    for (D0, U0, F0) in interiors:
        Dn, Un, Fn, Rn = rhs(D0, U0, F0, t, s)
        inside = 1 <= D0 <= Db and 1 <= U0 <= Ub and 1 <= F0 <= Fb
        print(f"T5 map at ({D0},{U0},{F0}) inside_box={inside}: D'≤Dbar {Dn <= Db} U'≤Ubar {Un <= Ub} F'≤Fbar {Fn <= Fb}")
        if inside and (Dn > Db or Un > Ub or Fn > Fb or Rn >= RBAR_CAP):
            hit(f"super-solution box not forward-invariant at ({D0},{U0},{F0})")

    coeff = gf_R(8, 8)
    partial = sum((c * t**a * s**f for (a, f), c in coeff.items()), F(0))
    nmono = len(coeff)
    ntrees = sum(coeff.values())
    print(f"T5 truncated R through a,f ≤ 8: {nmono} monomials, {ntrees} typed trees, partial={partial} ≤ Rbar {partial <= Rbar}")
    if partial > Rbar:
        hit(f"partial sum through 8 edges {partial} > Rbar {Rbar}")

    # --- T2: extra sites and extra fork locations ---
    sites = ((0, 0, 0), (2, -1, 3), (-4, 7, 1), (5, 5, -9), (1, 0, 0))
    for x in sites:
        for k in range(3):
            if sum(M(j, x) for j in range(3)) != 0:
                hit(f"Σ M_k != 0 at {x}")
            for j in range(3):
                inc = M(k, sub(x, E3[j])) - M(k, x)
                want = F(1, 3) - (1 if j == k else 0)
                if inc != want:
                    hit(f"increment {inc} != {want} at x={x} k={k} j={j}")
    print(f"OK T2(a): increments 1/3-δ_jk at {len(sites)} sites")

    for x in sites:
        for off in FORKS:
            w2 = add(x, off)
            size = sum(max(M(k, x), M(k, w2)) for k in range(3))
            if size != 1:
                hit(f"fork Size={size} != 1 at {x} off={off}")
            for poles in product((x, w2), repeat=3):
                span = sum(M(k, poles[k]) for k in range(3))
                if span > 1:
                    hit(f"fork Span={span} > 1 at {x} off={off}")
    print(f"OK T2(b): Size=1 and Span≤1 on {len(sites)}×{len(FORKS)} fork pairs")

    if HITS:
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - T0's 16-triple max "
        "equals max(d1,d2,d3) at extra couplings including the four T7 "
        "thresholds and fractional weights, for every value a; T7(b) p≥p0 "
        "holds on extra integers and extra (q,r) lines stay monotone through "
        "their least p; T5's recursion stays under the super-solution through "
        "height 3, at extra interior points of the bar-box, and in the "
        "truncated series through 8 edges; T6's (391/100)ε ≤ 3/10^5 and "
        "ε/t^3 ≤ s hold on a grid of ε ≤ 7/10^6; T2 increments and fork "
        "Size=1 hold at extra sites"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
