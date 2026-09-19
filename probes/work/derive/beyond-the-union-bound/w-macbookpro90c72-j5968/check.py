#!/usr/bin/env python3
"""Exact checks for J:derive:beyond-the-union-bound:a4 (worker w-macbookpro90c72-j5968).

Finite claims are integers or fractions. Floating output is display only.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from typing import Dict, Iterable, List, Sequence, Tuple

# ---------------------------------------------------------------------------
# Closed forms on the line (p, 1, 2), as in block 30 T0/T1.
# ---------------------------------------------------------------------------

def d1(p: int) -> Fraction:
    return Fraction(33, p**3 + 33)


def d2(p: int) -> Fraction:
    return Fraction(p + 32, p * (p + 1) + 32)


def d3(p: int) -> Fraction:
    return Fraction(2 * p + 11, p * p + 2 * p + 11)


def eps2(p: int) -> Fraction:
    return max(d2(p), d3(p))


# ---------------------------------------------------------------------------
# Diamond-free occupancy of three up-slots (masks 0..7, bit d = direction d).
# ---------------------------------------------------------------------------

def _popcount(m: int) -> int:
    return bin(m).count("1")


def _has(mask: int, d: int) -> int:
    return (mask >> d) & 1


def _pair_diamond(ci: int, cj: int, i: int, j: int) -> bool:
    return bool(_has(ci, j) and _has(cj, i))


def allowed_triple(s: int, t: int, r: int) -> bool:
    if _pair_diamond(s, t, 0, 1):
        return False
    if _pair_diamond(s, r, 0, 2):
        return False
    if _pair_diamond(t, r, 1, 2):
        return False
    return True


def triple_monomials() -> Dict[Tuple[int, int, int, int], int]:
    counts: Counter = Counter()
    n_ok = 0
    for s, t, r in product(range(8), repeat=3):
        if allowed_triple(s, t, r):
            n_ok += 1
            c = [0, 0, 0, 0]
            c[_popcount(s)] += 1
            c[_popcount(t)] += 1
            c[_popcount(r)] += 1
            counts[tuple(c)] += 1
    if n_ok != 216:
        raise AssertionError(f"allowed triples {n_ok} != 216")
    return dict(counts)


def phi_triple(
    counts: Dict[Tuple[int, int, int, int], int], a0: Fraction, a1: Fraction, a2: Fraction, a3: Fraction
) -> Fraction:
    vec = (a0, a1, a2, a3)
    total = Fraction(0)
    for mon, coeff in counts.items():
        term = Fraction(coeff)
        for i, e in enumerate(mon):
            term *= vec[i] ** e
        total += term
    return total


def df_rhs(
    a1: Fraction, a2: Fraction, a3: Fraction, x: Fraction, counts: Dict[Tuple[int, int, int, int], int]
) -> Tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    a0 = Fraction(1)
    U = a0 + 3 * a1 + 3 * a2 + a3
    P = a1 + 2 * a2 + a3
    rhs1 = x * U
    rhs2 = x**2 * (U**2 - P**2)
    rhs3 = x**3 * phi_triple(counts, a0, a1, a2, a3)
    return U, P, rhs1, rhs2, rhs3


# ---------------------------------------------------------------------------
# Small 3-ary plane trees, lattice embeddings, diamonds, animals.
# ---------------------------------------------------------------------------

E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
Tree = Tuple[object, object, object]


def trees_by_size(max_n: int) -> Dict[int, List[Tree]]:
    memo: Dict[int, List[Tree]] = {1: [(None, None, None)]}

    def of(n: int) -> List[Tree]:
        if n in memo:
            return memo[n]
        out: List[Tree] = []
        for n0 in range(n):
            for n1 in range(n - n0):
                n2 = n - 1 - n0 - n1
                C0 = [None] if n0 == 0 else of(n0)
                C1 = [None] if n1 == 0 else of(n1)
                C2 = [None] if n2 == 0 else of(n2)
                for c0 in C0:
                    for c1 in C1:
                        for c2 in C2:
                            out.append((c0, c1, c2))
        memo[n] = out
        return out

    for n in range(1, max_n + 1):
        of(n)
    return memo


def positions(tree: Tree, origin: Tuple[int, int, int] = (0, 0, 0)) -> List[Tuple[int, int, int]]:
    pos = [origin]
    for d, ch in enumerate(tree):
        if ch is not None:
            child_orig = (origin[0] + E3[d][0], origin[1] + E3[d][1], origin[2] + E3[d][2])
            pos.extend(positions(ch, child_orig))  # type: ignore[arg-type]
    return pos


def has_diamond(tree: Tree) -> bool:
    ch = tree
    for i, j in ((0, 1), (0, 2), (1, 2)):
        ci, cj = ch[i], ch[j]
        if ci is not None and cj is not None:
            if ci[j] is not None and cj[i] is not None:
                return True
    for c in ch:
        if c is not None and has_diamond(c):  # type: ignore[arg-type]
            return True
    return False


# ---------------------------------------------------------------------------
# Two-level automaton on the depth-1 / depth-2 backward cone.
# ---------------------------------------------------------------------------

def P_depth1(e1: Fraction, e2: Fraction) -> Fraction:
    return (
        (1 - e1) ** 3 * e1
        + 3 * e1 * (1 - e1) ** 2 * e2
        + 3 * e1**2 * (1 - e1)
        + e1**3
    )


def P_depth2(e1: Fraction, e2: Fraction) -> Fraction:
    # Bottom bits: b11, b22, b33, b12, b13, b23.
    mid_pred_ix = ((0, 3, 4), (3, 1, 5), (4, 5, 2))
    one = Fraction(1)
    P = Fraction(0)
    for bits in product((0, 1), repeat=6):
        prb = one
        for b in bits:
            prb *= e1 if b else (one - e1)
        mps = []
        for pred_ix in mid_pred_ix:
            n = bits[pred_ix[0]] + bits[pred_ix[1]] + bits[pred_ix[2]]
            if n >= 2:
                mps.append(one)
            elif n == 1:
                mps.append(e2)
            else:
                mps.append(e1)
        for mb in product((0, 1), repeat=3):
            prm = one
            for i, b in enumerate(mb):
                prm *= mps[i] if b else (one - mps[i])
            nroot = mb[0] + mb[1] + mb[2]
            if nroot >= 2:
                pr = one
            elif nroot == 1:
                pr = e2
            else:
                pr = e1
            P += prb * prm * pr
    return P


# Directed animals in the depth-2 past cone, weight ε1^{n0} ε2^{n1}.
SITES_D2 = [
    (0, 0, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
    (-2, 0, 0),
    (0, -2, 0),
    (0, 0, -2),
    (-1, -1, 0),
    (-1, 0, -1),
    (0, -1, -1),
]
ROOT = (0, 0, 0)


def _preds(v: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    return [(v[0] - 1, v[1], v[2]), (v[0], v[1] - 1, v[2]), (v[0], v[1], v[2] - 1)]


def _toward_root(v: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    out = []
    if v[0] < 0:
        out.append((v[0] + 1, v[1], v[2]))
    if v[1] < 0:
        out.append((v[0], v[1] + 1, v[2]))
    if v[2] < 0:
        out.append((v[0], v[1], v[2] + 1))
    return out


def is_directed_animal(S: set) -> bool:
    if ROOT not in S:
        return False
    for v in S:
        if v == ROOT:
            continue
        if not any(s in S for s in _toward_root(v)):
            return False
    return True


def animal_weight(S: set, e1: Fraction, e2: Fraction) -> Fraction:
    n0 = n1 = 0
    for v in S:
        npred = sum(1 for p in _preds(v) if p in S)
        if npred == 0:
            n0 += 1
        elif npred == 1:
            n1 += 1
    return (e1**n0) * (e2**n1)


def animal_sum_depth2(e1: Fraction, e2: Fraction) -> Tuple[Fraction, int]:
    others = SITES_D2[1:]
    tot = Fraction(0)
    nA = 0
    for bits in product((0, 1), repeat=9):
        S = {ROOT}
        for i, b in enumerate(bits):
            if b:
                S.add(others[i])
        if is_directed_animal(S):
            nA += 1
            tot += animal_weight(S, e1, e2)
    return tot, nA


def phi_product(A: Fraction, e1: Fraction, e2: Fraction) -> Fraction:
    return e1 + 3 * e2 * A + 3 * A * A + A**3


def main() -> None:
    failures: List[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        status = "PASS" if cond else "FAIL"
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {status}{extra}")
        if not cond:
            failures.append(name)

    # ----- E0: block 30 ceiling arithmetic (restated, exact) -----
    v = Fraction(3, 2)
    check("E0a", (v - 1) / v**3 == Fraction(4, 27), f"(v-1)/v^3={(v-1)/v**3}")
    t_star = Fraction(8, 81)
    g = t_star**2 * (Fraction(4, 27) - t_star)
    check("E0b", g == Fraction(256, 531441), f"t^2(4/27-t)={g}")
    t1 = Fraction(2, 27)
    check("E0c", t1 * (Fraction(4, 27) - t1) == Fraction(4, 729))
    check("E0d", d3(4150) > Fraction(256, 531441) > d3(4165), f"d3(4150)={d3(4150)} d3(4165)={d3(4165)}")
    check("E0e", d3(367) > Fraction(4, 729) > d3(368))
    check("E0f", d3(4003) >= Fraction(1, 2000) > d3(4004), f"d3(4003)={d3(4003)} d3(4004)={d3(4004)}")

    # ----- E1: diamond-free triple count and super-solution at x=3/20 -----
    counts = triple_monomials()
    n_pair_ok = sum(
        1
        for s, t in product(range(8), repeat=2)
        if not (_has(s, 1) and _has(t, 0))
    )
    check("E1a", n_pair_ok == 48, f"allowed pairs {n_pair_ok}")
    x = Fraction(3, 20)
    a1 = Fraction(12, 25)
    a2 = Fraction(1, 5)
    a3 = Fraction(2, 25)
    U, P, rhs1, rhs2, rhs3 = df_rhs(a1, a2, a3, x, counts)
    check("E1b", U == Fraction(78, 25), f"U={U}")
    check("E1c", a1 >= rhs1, f"a1={a1} rhs1={rhs1} margin={a1-rhs1}")
    check("E1d", a2 >= rhs2, f"a2={a2} rhs2={rhs2} margin={a2-rhs2}")
    check("E1e", a3 >= rhs3, f"a3={a3} rhs3={rhs3} margin={a3-rhs3}")
    check("E1f", x > Fraction(4, 27), f"x={x} 4/27={Fraction(4,27)}")

    # ----- E2: D and R at y=0 from this U -----
    u = 1 + x * U
    check("E2a", u == Fraction(367, 250), f"1+xU={u}")
    three_x_u2 = 3 * x * u * u
    check("E2b", three_x_u2 < 1, f"3x(1+xU)^2={three_x_u2}")
    Dbar = Fraction(72)
    rhs_D = (u**2) * (1 + 3 * x * Dbar)
    check("E2c", Dbar >= rhs_D, f"Dbar={Dbar} rhs={rhs_D} margin={Dbar-rhs_D}")
    Rbar = (u**3) * (1 + 3 * x * Dbar)
    check(
        "E2d",
        Rbar == Fraction(8254954121, 78125000) and Rbar < 106,
        f"Rbar={Rbar} = {float(Rbar):.6f}",
    )

    # ----- E3: t-trick ceiling 1/2000 and p=4004 -----
    t = Fraction(1, 10)
    ceil_new = t**2 * (x - t)
    check("E3a", ceil_new == Fraction(1, 2000), f"t^2(3/20-t)={ceil_new}")
    check("E3b", eps2(4003) >= Fraction(1, 2000) > eps2(4004), f"eps2(4003)={eps2(4003)} eps2(4004)={eps2(4004)}")
    x_at = t + eps2(4004) / (t**2)
    check("E3c", x_at < x, f"t+eps2/t^2={x_at} vs {x}")
    e1_4004 = d1(4004)
    y_at = e1_4004 / (t**3)
    bound = e1_4004 * Rbar
    check("E3d", bound < Fraction(1, 2), f"e1 Rbar={bound} = {float(bound):.6e} y={float(y_at):.6e}")
    check("E3e", bound < Fraction(1, 10**6), f"e1 Rbar vs 1e-6: {float(bound):.6e}")

    # ----- E4: small-n plane / DF / injective / animals (integers) -----
    memo = trees_by_size(7)
    expected_plane = {1: 1, 2: 3, 3: 12, 4: 55, 5: 273, 6: 1428, 7: 7752}
    expected_df = {1: 1, 2: 3, 3: 12, 4: 55, 5: 270, 6: 1386, 7: 7344}
    expected_inj = {1: 1, 2: 3, 3: 12, 4: 55, 5: 270, 6: 1386, 7: 7329}
    expected_an = {1: 1, 2: 3, 3: 12, 4: 52, 5: 237, 6: 1113, 7: 5339}
    for n in range(1, 8):
        ts = memo[n]
        n_plane = len(ts)
        n_df = 0
        n_inj = 0
        sets = set()
        for tr in ts:
            df = not has_diamond(tr)
            if df:
                n_df += 1
            pos = positions(tr)
            inj = len(pos) == len(set(pos))
            if inj:
                n_inj += 1
                sets.add(frozenset(pos))
            if inj and not df:
                failures.append(f"E4-inj-not-df-n{n}")
        n_an = len(sets)
        print(
            f"COUNT n={n} plane={n_plane} df={n_df} inj={n_inj} animals={n_an}"
        )
        check(f"E4plane{n}", n_plane == expected_plane[n])
        check(f"E4df{n}", n_df == expected_df[n])
        check(f"E4inj{n}", n_inj == expected_inj[n])
        check(f"E4an{n}", n_an == expected_an[n])
        check(f"E4chain{n}", n_an <= n_inj <= n_df <= n_plane)

    # First n at which DF < plane, inj < DF, animals < inj.
    check("E4first_df", expected_df[5] < expected_plane[5] and expected_df[4] == expected_plane[4])
    check("E4first_inj", expected_inj[7] < expected_df[7] and expected_inj[6] == expected_df[6])
    check("E4first_an", expected_an[4] < expected_inj[4] and expected_an[3] == expected_inj[3])

    # ----- E5: naive set-product hole (exact) -----
    # S = {0, -e1, -e2, -e1-e2}: root processed, two amps, one shared seed.
    # w(S) = ε1 ε2^2.  Sub-animals at the two predecessors each have weight ε1 ε2;
    # product = ε1^2 ε2^2.  For ε1 < 1 this is strictly smaller than w(S).
    p_hole = 14
    e1h, e2h = d1(p_hole), eps2(p_hole)
    wS = e1h * e2h * e2h
    prod = (e1h * e2h) * (e1h * e2h)
    check("E5a", wS > prod, f"w(S)={wS} product={prod}")
    check("E5b", wS == Fraction(1587, 3696187), f"w(S)={wS}")
    check("E5c", prod == Fraction(4761, 933119209), f"product={prod}")
    # The 3-type product map at p=14 does have a super-solution, so existence of a
    # fixed point is not the obstruction — the inequality w(S) ≤ product is.
    Abar14 = Fraction(19, 500)
    check("E5d", Abar14 >= phi_product(Abar14, e1h, e2h), f"margin={Abar14 - phi_product(Abar14, e1h, e2h)}")

    # ----- E6: cone domination (true P and animal sum vs certificates) -----
    for p, Abar in ((14, Fraction(19, 500)), (20, Fraction(7, 1000)), (50, Fraction(1, 1000))):
        e1, e2 = d1(p), eps2(p)
        Pd1 = P_depth1(e1, e2)
        Pd2 = P_depth2(e1, e2)
        Asum, nA = animal_sum_depth2(e1, e2)
        check(f"E6nA{p}", nA == 185, f"n_animals={nA}")
        check(f"E6mono{p}", Pd1 <= Pd2 <= Asum, f"P_d1={float(Pd1):.6e} P_d2={float(Pd2):.6e} Asum={float(Asum):.6e}")
        check(f"E6Asum{p}", Asum <= Abar, f"Asum={Asum} Abar={Abar}")
        check(f"E6P{p}", Pd2 <= Abar)
        print(
            f"CONE p={p} e1={float(e1):.6e} e2={float(e2):.6e} "
            f"P_d1={float(Pd1):.6e} P_d2={float(Pd2):.6e} animal_sum={float(Asum):.6e} Abar={float(Abar):.6e}"
        )

    # DF tree bound at p=4004 vs block 30's 4165.
    print(f"DF U={U} Rbar={Rbar} e1(4004)*Rbar={bound}")
    print(f"NEW_CEILING 1/2000 p_first={4004} OLD_CEILING 256/531441 p_first={4165}")

    if failures:
        print("FAILED:", "; ".join(failures))
        print(
            "SUMMARY: ROUTE FAILS AT check "
            + failures[0]
            + " (exact arithmetic of the attempted certificate or enumeration disagreed)"
        )
        return 1

    print(
        "HIT: diamond-free U-system has rational super-solution "
        "(a1,a2,a3)=(12/25, 1/5, 2/25) at x=3/20 > 4/27 with U=78/25, "
        "Dbar=72, Rbar=8254954121/78125000; t-trick ceiling ε2 < 1/2000, "
        "first integer p on (p,1,2) with max(d2,d3)<1/2000 is p=4004 "
        "(block 30: p=4165 at 256/531441). Naive set-product A=ε1+3ε2 A+3A^2+A^3 "
        "is not a valid animal bound: on S={0,-e1,-e2,-e1-e2} one has "
        "w(S)=ε1 ε2^2 > (ε1 ε2)^2 = w(S1)w(S2) (exact at p=14: 1587/3696187 > 4761/933119209)."
    )
    print(
        "SUMMARY: PARTIAL diamond-free lift of explanation trees is finite at "
        "x=3/20>4/27 with exact super-solution (12/25,1/5,2/25), D=72, "
        "ceiling ε2<1/2000 and p=4004 on (p,1,2); the naive 3-type set-product "
        "recursion fails at the overlapping-cone step (w(S)>w(S1)w(S2) on the diamond)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
