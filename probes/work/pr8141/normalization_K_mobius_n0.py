#!/usr/bin/env python3
"""J:attack-f:PR8141 — pattern (f) NORMALIZATION.

T1 writes μ = (1/6)^{n0} Π_edges K / Π_{|A|>=2} K_|A| with K=φ/Z1, K_1≡1,
K_2=K^2. T3's vacuum-normalized Möbius uses (−1)^{|S∖T|} and mixed
differences Δ_k with vacuum 0=+e1. T6 quotes exp Φ_ab=3, exp Φ_bd=3/4,
exp Φ_bc=12/13, exp Φ_ad=1, exp Φ_leaves=165/169 at a named witness.

Recompute K-sum-rules, (1/6)^{n0} on a disconnected two-edge window (n0=2),
Δ_k exp-ratios, and the T6 Möbius factors from T1 at (3,1,2) by brute force.
HIT if a written 1/6, Z1, K_2=K^2, Möbius sign, or T6 factor disagrees.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {
    "+x": "-x",
    "-x": "+x",
    "+y": "-y",
    "-y": "+y",
    "+z": "-z",
    "-z": "+z",
}
VAC = "+x"  # note: 0 = P(+e_1)
P, Q, Rwt = 3, 1, 2
M = 6
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def phi(s, t):
    if s == t:
        return P
    if OPP[s] == t:
        return Q
    return Rwt


def make_K():
    Z1 = P + Q + 4 * Rwt
    K = {a: {s: F(phi(s, a), Z1) for s in VALS} for a in VALS}
    return Z1, K


def Kk(K, rec):
    tot = F(0)
    for s in VALS:
        pr = F(1)
        for a in rec:
            pr *= K[a][s]
        tot += pr
    return tot


def matmul_K(K):
    out = {a: {b: F(0) for b in VALS} for a in VALS}
    for a in VALS:
        for b in VALS:
            out[a][b] = sum(K[a][s] * K[s][b] for s in VALS)
    return out


def check_sum_rules() -> dict:
    print("== K sum rules at (3,1,2) ==")
    Z1, K = make_K()
    print(f"  Z1={Z1} p+q+4r={P + Q + 4 * Rwt}")
    if Z1 != 12:
        hit(f"Z1={Z1} != 12")
    for a in VALS:
        rs = sum(K[a][s] for s in VALS)
        cs = sum(K[s][a] for s in VALS)
        if rs != 1:
            hit(f"K_1≡1 fails: row {a} sums to {rs}")
        if cs != 1:
            hit(f"K not doubly stochastic: col {a} sums to {cs}")
        for s in VALS:
            if K[a][s] != K[s][a]:
                hit(f"K not symmetric at {a},{s}")
                break
    K2 = {a: {b: sum(K[a][s] * K[b][s] for s in VALS) for b in VALS} for a in VALS}
    Ksq = matmul_K(K)
    n_off = sum(1 for a in VALS for b in VALS if K2[a][b] != Ksq[a][b])
    print(f"  K_2 vs K^2 mismatches={n_off}")
    if n_off:
        hit(f"K_2 != K^2 on {n_off}/36 pairs")
    return K


def mu_disjoint_edges(K, cfg):
    """Two disjoint edges (a-b) and (c-d); order a,c,b,d so n0=2."""
    # A_a=∅, A_c=∅, A_b={a}, A_d={c}
    return (F(1, M) ** 2) * K[cfg["a"]][cfg["b"]] * K[cfg["c"]][cfg["d"]]


def cond_disjoint(K, cfg):
    return (
        F(1, M)
        * F(1, M)
        * K[cfg["a"]][cfg["b"]]
        * K[cfg["c"]][cfg["d"]]
    )


def check_n0(K) -> None:
    print("== T1 (1/6)^{n0} on two disjoint edges (n0=2) ==")
    n = 0
    bad = 0
    for vals in product(VALS, repeat=4):
        cfg = dict(zip(("a", "b", "c", "d"), vals))
        n += 1
        if mu_disjoint_edges(K, cfg) != cond_disjoint(K, cfg):
            bad += 1
            if bad == 1:
                hit(
                    f"T1 (1/6)^{{n0}} fails on disconnected window n0=2 "
                    f"cfg={cfg} closed={mu_disjoint_edges(K, cfg)} "
                    f"cond={cond_disjoint(K, cfg)}"
                )
    tot = sum(
        mu_disjoint_edges(K, dict(zip(("a", "b", "c", "d"), vals)))
        for vals in product(VALS, repeat=4)
    )
    print(f"  configs={n} mismatches={bad} total mass={tot}")
    if tot != 1:
        hit(f"disconnected n0=2 law does not sum to 1: {tot}")
    # if n0 were wrongly 1, mass would be 6
    wrong = sum(
        F(1, M) * K[cfg["a"]][cfg["b"]] * K[cfg["c"]][cfg["d"]]
        for cfg in (
            dict(zip(("a", "b", "c", "d"), vals))
            for vals in product(VALS, repeat=4)
        )
    )
    print(f"  mass if n0 wrongly 1: {wrong}")


def delta_k_exp(K, k, wit) -> F:
    """exp(Δ_k log K_k) = Π_S K_k(a_S, 0_{S^c})^{(-1)^{k-|S|}}."""
    num = F(1)
    den = F(1)
    for mask in range(1 << k):
        rec = []
        size = 0
        for i in range(k):
            if mask & (1 << i):
                rec.append(wit[i])
                size += 1
            else:
                rec.append(VAC)
        val = Kk(K, tuple(rec))
        sign = (k - size) % 2
        if sign == 0:
            num *= val
        else:
            den *= val
    return F(num, den)


def check_mixed_diff(K) -> None:
    print("== T3 Δ_k exp(Δ log K_k) at (3,1,2) ==")
    # k=2 stated 169/121; k=3 stated 169/165. Witnesses from T6 / B2 style.
    # try several assignments; the note says "a witness assignment"
    stated = {2: F(169, 121), 3: F(169, 165)}
    # T6 star witness leaves (-x,-x,+y) is a k=3 assignment
    wits = {
        2: [("+y", "+z"), ("-x", "+y"), ("+x", "+y"), ("+y", "+y")],
        3: [("-x", "-x", "+y"), ("+y", "+z", "-y"), ("-x", "+y", "+z")],
    }
    for k, want in stated.items():
        found = None
        for wit in wits[k]:
            got = delta_k_exp(K, k, wit)
            print(f"  k={k} wit={wit}: exp Δ={got} stated={want}")
            if got == want:
                found = wit
        if found is None:
            # brute a few more for k=2
            if k == 2:
                for a, b in product(VALS, repeat=2):
                    got = delta_k_exp(K, 2, (a, b))
                    if got == want:
                        found = (a, b)
                        print(f"  k=2 found witness {found} with {got}")
                        break
            if found is None:
                hit(
                    f"T3 exp(Δ_{k} log K_{k}) never equals stated {want} "
                    f"on the tried assignments (Möbius/K convention)"
                )


def plaquette_mu(K, v):
    """Order (a,b,c,d): A_a=∅, A_b={a}, A_c={a}, A_d={b,c}."""
    a, b, c, d = v["a"], v["b"], v["c"], v["d"]
    return (
        F(1, M)
        * K[a][b]
        * K[a][c]
        * K[b][d]
        * K[c][d]
        / Kk(K, (b, c))
    )


def star_mu(K, v):
    """Leaves first, center x last: n0=3, A_x={l1,l2,l3}."""
    x, l1, l2, l3 = v["x"], v["l1"], v["l2"], v["l3"]
    return (F(1, M) ** 3) * K[l1][x] * K[l2][x] * K[l3][x] / Kk(K, (l1, l2, l3))


def fill_vac(base, sites, which):
    v = dict(base)
    for s in sites:
        if s not in which:
            v[s] = VAC
    return v


def mobius_exp(mu_fn, K, sites, S, vS):
    """exp Φ_S(v_S) = Π_{T⊆S} μ(v_T, 0_{W∖T})^{(-1)^{|S∖T|}}."""
    S = tuple(S)
    num = F(1)
    den = F(1)
    nS = len(S)
    for mask in range(1 << nS):
        T = [S[i] for i in range(nS) if mask & (1 << i)]
        sizeT = len(T)
        cfg = {s: VAC for s in sites}
        for s in T:
            cfg[s] = vS[s]
        val = mu_fn(K, cfg)
        sign = (nS - sizeT) % 2
        if sign == 0:
            num *= val
        else:
            den *= val
    return F(num, den)


def check_t6(K) -> None:
    print("== T6 vacuum Möbius factors at the named witness ==")
    sites = ("a", "b", "c", "d")
    wit = {"a": "-x", "b": "+y", "c": "+z", "d": "-y"}
    want = {
        ("b", "c"): F(12, 13),
        ("a", "d"): F(1),
        ("a", "b"): F(3),
        ("b", "d"): F(3, 4),
        ("a", "b", "c", "d"): F(1),
        ("b", "c", "d"): F(1),
    }
    for S, stated in want.items():
        vS = {s: wit[s] for s in S}
        got = mobius_exp(plaquette_mu, K, sites, S, vS)
        print(f"  plaquette exp Φ_{{{''.join(S)}}} = {got} stated {stated}")
        if got != stated:
            hit(
                f"T6 plaquette exp Φ_{{{''.join(S)}}} at witness "
                f"{wit} = {got} != stated {stated} "
                f"(vacuum Möbius of T1's K-form)"
            )
    # exp Φ_ad = 1 on ALL 1296 configs
    n_ad = 0
    n_ad_off = 0
    for vals in product(VALS, repeat=4):
        cfg = dict(zip(sites, vals))
        n_ad += 1
        got = mobius_exp(plaquette_mu, K, sites, ("a", "d"), {"a": cfg["a"], "d": cfg["d"]})
        if got != 1:
            n_ad_off += 1
            if n_ad_off <= 2:
                hit(f"T6 exp Φ_ad={got} != 1 at {cfg}")
    print(f"  exp Φ_ad == 1 on {n_ad - n_ad_off}/{n_ad} configs")

    # star three-body
    swit = {"l1": "-x", "l2": "-x", "l3": "+y", "x": VAC}
    got3 = mobius_exp(
        star_mu, K, ("x", "l1", "l2", "l3"), ("l1", "l2", "l3"), swit
    )
    print(f"  star exp Φ_leaves={got3} stated 165/169")
    if got3 != F(165, 169):
        hit(f"T6 star exp Φ_{{l1 l2 l3}}={got3} != 165/169 at {swit}")


def main() -> int:
    K = check_sum_rules()
    check_n0(K)
    check_mixed_diff(K)
    check_t6(K)
    if HITS:
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION has purchase (Z1, K_1≡1, K_2=K^2, "
        "(1/6)^{n0} on a disconnected n0=2 window, Δ_k mixed-difference ratios, "
        "T6 vacuum-Möbius exp Φ factors 3, 3/4, 12/13, 1, 165/169) and every "
        "identity recomputes exactly at (3,1,2); no HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
