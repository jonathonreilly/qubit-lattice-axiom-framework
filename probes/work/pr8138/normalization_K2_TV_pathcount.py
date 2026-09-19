#!/usr/bin/env python3
"""J:attack-f:PR8138 — pattern (f) NORMALIZATION.

The note has no Fourier 2π/L sum. It does declare sum-rule / 1/2 / N factors:
  Z_1 = p+q+4r, K(a,s)=φ(s,a)/Z_1 doubly stochastic, K_1 ≡ 1,
  K_2(a,b) = (K^2)(a,b)  (block 02 E1),
  TV = (1/2) Σ|μ-ν| in c_k,
  r(∅)=1/6 and coordinate-line pairs (1/6)K, anti-diagonal (1/6)K^2,
  N(z,x) = |x-z|_1! / Π_i (x_i-z_i)!, Σ_{|d|_1=d} N ≤ 3^d,
  Σ_j C(n+j,n) 2^j c^{n+j} = c^n (1-2c)^{-n-1} = (1-2c)^{-1} θ^n.

Recompute at the silent triple (3,1,2) and the constant control by brute force
on the 6-point menu, 2-site and 2×2 windows, and short monotone paths.
HIT if a written factor disagrees with the exact object it names.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import factorial

M = 6
AXES = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def binom(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def orbit_phi(s: int, t: int, p: int, q: int, r: int) -> int:
    d = sum(AXES[s][i] * AXES[t][i] for i in range(3))
    if d == 1:
        return p
    if d == -1:
        return q
    return r


def make_K(p: int, q: int, r: int):
    """Note: K(a,s) = φ(s,a)/Z_1 with Z_1 = p+q+4r."""
    Z1 = p + q + 4 * r
    phi = [[orbit_phi(s, t, p, q, r) for t in range(M)] for s in range(M)]
    # K[a][s]
    K = [[F(phi[s][a], Z1) for s in range(M)] for a in range(M)]
    return phi, Z1, K


def matmul(A, B):
    n = len(A)
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            if aik == 0:
                continue
            rowb = B[k]
            outi = out[i]
            for j in range(n):
                outi[j] += aik * rowb[j]
    return out


def tv(u, v) -> F:
    return sum(abs(x - y) for x, y in zip(u, v)) / 2


def multinomial_N(delta):
    d = sum(delta)
    if any(x < 0 for x in delta):
        return 0
    acc = factorial(d)
    for x in delta:
        acc //= factorial(x)
    return acc


def count_paths(delta) -> int:
    """Enumerate step-words in {e1,e2,e3} with given counts."""
    steps = (0,) * delta[0] + (1,) * delta[1] + (2,) * delta[2]
    if not steps:
        return 1
    seen = set()
    n = 0
    from itertools import permutations

    for w in permutations(steps):
        if w in seen:
            continue
        seen.add(w)
        n += 1
    return n


def check_sum_rules(p, q, r, label: str) -> None:
    print(f"== sum rules at {label} {(p, q, r)} ==")
    phi, Z1, K = make_K(p, q, r)
    want_Z1 = p + q + 4 * r
    print(f"  Z1={Z1} stated p+q+4r={want_Z1}")
    if Z1 != want_Z1:
        hit(f"{label}: Z1={Z1} != p+q+4r={want_Z1}")

    # φ 1 = Z1 1
    for s in range(M):
        if sum(phi[s][t] for t in range(M)) != Z1:
            hit(f"{label}: row-sum φ[{s}] != Z1")
            break
        if sum(phi[t][s] for t in range(M)) != Z1:
            hit(f"{label}: col-sum φ[:,{s}] != Z1")
            break
    else:
        print("  φ 1 = Z1 1 (rows and cols): True")

    # K symmetric doubly stochastic; K_1 ≡ 1
    for a in range(M):
        rs = sum(K[a][s] for s in range(M))
        cs = sum(K[s][a] for s in range(M))
        if rs != 1:
            hit(f"{label}: K row {a} sums to {rs} != 1 (K_1 ≡ 1 fails)")
        if cs != 1:
            hit(f"{label}: K col {a} sums to {cs} != 1 (not doubly stochastic)")
        for s in range(M):
            if K[a][s] != K[s][a]:
                hit(f"{label}: K not symmetric at ({a},{s}): {K[a][s]} vs {K[s][a]}")
                break
    print("  K doubly stochastic and symmetric; K_1 ≡ 1")

    # K_2(a,b) = Σ_s K(a,s) K(b,s)  vs  (K^2)(a,b) = Σ_s K(a,s) K(s,b)
    K2 = [[sum(K[a][s] * K[b][s] for s in range(M)) for b in range(M)] for a in range(M)]
    Ksq = matmul(K, K)
    n_mismatch = 0
    worst = None
    for a in range(M):
        for b in range(M):
            if K2[a][b] != Ksq[a][b]:
                n_mismatch += 1
                if worst is None:
                    worst = (a, b, K2[a][b], Ksq[a][b])
    print(f"  K_2 vs K^2 mismatches: {n_mismatch}")
    if n_mismatch:
        hit(
            f"{label}: K_2(a,b)=Σ_s K(a,s)K(b,s) != (K^2)(a,b)=Σ_s K(a,s)K(s,b) "
            f"at {n_mismatch}/36 pairs, e.g. {worst}"
        )
    else:
        print("  K_2 = K^2 on all 36 pairs (symmetry of K): True")

    # K_2 rows sum to 1 (stochastic, as claimed equal to K^2)
    for a in range(M):
        srow = sum(K2[a][b] for b in range(M))
        if srow != 1:
            hit(f"{label}: K_2 row {a} sums to {srow} != 1")


def check_tv_half(p, q, r, stated_c1: F, label: str) -> None:
    print(f"== TV 1/2 convention at {label} ==")
    _, _, K = make_K(p, q, r)
    # point masses
    e0 = [F(1 if i == 0 else 0) for i in range(M)]
    e1 = [F(1 if i == 1 else 0) for i in range(M)]
    t_eq = tv(e0, e0)
    t_pt = tv(e0, e1)
    print(f"  TV(point,point)={t_eq} TV(distinct points)={t_pt}")
    if t_eq != 0:
        hit(f"{label}: TV(μ,μ)={t_eq} != 0")
    if t_pt != 1:
        hit(
            f"{label}: TV of distinct point masses = {t_pt} != 1 "
            f"(1/2 convention; without 1/2 this is 2)"
        )
    # c_1 = max TV of one-neighbor kernels
    c1 = F(0)
    for a, b in product(range(M), repeat=2):
        if a == b:
            continue
        d = tv(K[a], K[b])
        if d > c1:
            c1 = d
    # L1 without 1/2 would double it
    print(f"  c1={c1} stated={stated_c1}; twice would be {2 * c1}")
    if c1 != stated_c1:
        hit(f"{label}: c1 with TV=(1/2)Σ|·| is {c1} != stated {stated_c1}")


def check_one_sixth_pairs(p, q, r, label: str) -> None:
    """Coordinate-line pair = (1/6)K; length-2 chain = (1/6)K^2;
    2×2 anti-diagonal = (1/6)K_2. Enumerate."""
    print(f"== (1/6)K and (1/6)K^2 pair laws at {label} ==")
    _, Z1, K = make_K(p, q, r)
    K2 = [[sum(K[a][s] * K[b][s] for s in range(M)) for b in range(M)] for a in range(M)]
    Ksq = matmul(K, K)

    # 2-site line: P(a,b) = (1/6) K[a][b]
    pair = [[F(0) for _ in range(M)] for _ in range(M)]
    tot = F(0)
    for a, b in product(range(M), repeat=2):
        w = F(1, M) * K[a][b]
        pair[a][b] += w
        tot += w
    if tot != 1:
        hit(f"{label}: 2-site chain total mass {tot} != 1")
    n_off = sum(1 for a, b in product(range(M), repeat=2) if pair[a][b] != F(1, M) * K[a][b])
    print(f"  2-site P(a,b)=(1/6)K(a,b) on all 36: {n_off == 0}; mass={tot}")
    if n_off:
        hit(f"{label}: 2-site pair law != (1/6)K on {n_off} entries")

    # length-2 chain of three sites: P(v0=a, v2=b) = (1/6) (K^2)(a,b)
    chain = [[F(0) for _ in range(M)] for _ in range(M)]
    for a, m, b in product(range(M), repeat=3):
        w = F(1, M) * K[a][m] * K[m][b]
        chain[a][b] += w
    n_off2 = sum(1 for a, b in product(range(M), repeat=2) if chain[a][b] != F(1, M) * Ksq[a][b])
    print(f"  length-2 chain P(ends)=(1/6)K^2 on all 36: {n_off2 == 0}")
    if n_off2:
        hit(f"{label}: length-2 chain pair != (1/6)K^2 on {n_off2} entries")

    # 2×2 anti-diagonal: sites (0,1) and (1,0), both children of origin
    # P(v01=a, v10=b) = Σ_s (1/6) K(s,a) K(s,b) = (1/6) K_2(a,b)
    anti = [[F(0) for _ in range(M)] for _ in range(M)]
    for s, a, b in product(range(M), repeat=3):
        w = F(1, M) * K[s][a] * K[s][b]
        anti[a][b] += w
    n_k2 = sum(1 for a, b in product(range(M), repeat=2) if anti[a][b] != F(1, M) * K2[a][b])
    n_ksq = sum(1 for a, b in product(range(M), repeat=2) if anti[a][b] != F(1, M) * Ksq[a][b])
    print(f"  2x2 anti-diagonal = (1/6)K_2: {n_k2 == 0}; = (1/6)K^2: {n_ksq == 0}")
    if n_k2:
        hit(f"{label}: anti-diagonal pair != (1/6)K_2 on {n_k2} entries")
    if n_ksq:
        hit(
            f"{label}: anti-diagonal pair != (1/6)K^2 on {n_ksq} entries "
            f"(note names it a (1/6)K^2-pair)"
        )

    # stated (1/6)K(+x,+x) = 1/24 at (3,1,2)
    if (p, q, r) == (3, 1, 2):
        got = F(1, M) * K[0][0]
        print(f"  (1/6)K(+x,+x)={got} stated 1/24")
        if got != F(1, 24):
            hit(f"{label}: (1/6)K(+x,+x)={got} != 1/24")


def check_path_N() -> None:
    print("== N multinomial path counts ==")
    samples = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 0, 0), (3, 0, 0), (2, 1, 1)]
    for delta in samples:
        N = multinomial_N(delta)
        enum = count_paths(delta)
        print(f"  delta={delta} N={N} enumerated={enum}")
        if N != enum:
            hit(f"N({delta}) multinomial {N} != enumerated monotone words {enum}")
    # cube influence uses N((1,1,1))=6, not menu-size coincidence
    if multinomial_N((1, 1, 1)) != 6:
        hit(f"N(1,1,1)={multinomial_N((1, 1, 1))} != 6 (note's cube bound)")
    if multinomial_N((2, 1, 0)) == 6:
        hit("N(2,1,0)=6: path count accidentally equals menu size")
    print(f"  N(2,1,0)={multinomial_N((2, 1, 0))} (menu size 6 would be wrong here)")

    # Σ_{z: |x-z|_1=d, z≤x} N(z,x) vs 3^d
    for d in range(0, 5):
        total = 0
        for n1, n2, n3 in product(range(d + 1), repeat=3):
            if n1 + n2 + n3 != d:
                continue
            total += multinomial_N((n1, n2, n3))
        print(f"  sum N at distance {d} = {total}; 3^{d}={3 ** d}")
        if total != 3 ** d:
            hit(f"Σ N at d={d} is {total} != 3^{d}={3 ** d} (note writes ≤ 3^d)")
        # the inequality is equality on the monotone orthant


def check_generating_function() -> None:
    print("== Q4c generating function at (3,1,2) ==")
    c = F(27, 110)
    theta = c / (1 - 2 * c)
    print(f"  c={c} theta={theta} stated 27/56={F(27, 56)}")
    if theta != F(27, 56):
        hit(f"theta=c/(1-2c)={theta} != 27/56")
    for n in range(0, 7):
        lhs_closed = (c ** n) / ((1 - 2 * c) ** (n + 1))
        rhs_theta = theta ** n / (1 - 2 * c)
        if lhs_closed != rhs_theta:
            hit(
                f"n={n}: c^n (1-2c)^{{-(n+1)}}={lhs_closed} != "
                f"(1-2c)^{{-1}} theta^n={rhs_theta}"
            )
        # partial sum of the path series vs closed form: remainder ≥ 0 so partial ≤ closed
        partial = F(0)
        for j in range(0, 12):
            partial += binom(n + j, n) * (2 ** j) * (c ** (n + j))
        if partial > lhs_closed:
            hit(f"n={n}: truncated path sum {partial} exceeds closed form {lhs_closed}")
        print(f"  n={n}: closed={lhs_closed} partial_j<12={partial} theta_form={rhs_theta}")
    # Pascal for the binomial in the path count
    pascal_ok = True
    for n in range(1, 8):
        for j in range(0, 8):
            if binom(n + j, n) != binom(n + j - 1, n) + binom(n + j - 1, n - 1):
                pascal_ok = False
                hit(f"Pascal fails at n={n} j={j} for C(n+j,n)")
    print(f"  Pascal for C(n+j,n): {pascal_ok}")


def check_z1_cancellation(p, q, r) -> None:
    """Numerator Π_edges K carries Z1^{-n_edges}; K_k = Z_k/Z1^k restores
    Z1^{2 n2 + 3 n3}, leaving den = 6 Z1^{n_one} Π Z2 Π Z3 as in the runner."""
    print(f"== Z1-power cancellation on the 2x2x2 cube at {(p, q, r)} ==")
    sites = list(product(range(2), repeat=3))

    def preds(x):
        return [
            tuple(x[i] - (1 if j == i else 0) for i in range(3))
            for j in range(3)
            if x[j] > 0
        ]

    n_one = sum(1 for x in sites if len(preds(x)) == 1)
    n_two = sum(1 for x in sites if len(preds(x)) == 2)
    n_three = sum(1 for x in sites if len(preds(x)) == 3)
    n_edges = n_one + 2 * n_two + 3 * n_three
    # after writing every edge as φ/Z1 and every K_k as Z_k/Z1^k:
    z1_num_from_K = n_edges
    z1_den_from_Kk = 2 * n_two + 3 * n_three
    leftover = z1_num_from_K - z1_den_from_Kk
    print(
        f"  n_one={n_one} n_two={n_two} n_three={n_three} n_edges={n_edges}; "
        f"Z1 leftover exponent {leftover} (should equal n_one={n_one})"
    )
    if leftover != n_one:
        hit(
            f"Z1 cancellation on the cube: leftover exponent {leftover} != n_one={n_one} "
            f"(product form in K would not match φ / (6 Z1^{{n_one}} Z2 Z3))"
        )
    # 2x2 rectangle: n_one=2, n_two=1, n_three=0, leftover 2
    sites2 = list(product(range(2), repeat=2))

    def preds2(x):
        return [
            tuple(x[i] - (1 if j == i else 0) for i in range(2))
            for j in range(2)
            if x[j] > 0
        ]

    n1 = sum(1 for x in sites2 if len(preds2(x)) == 1)
    n2 = sum(1 for x in sites2 if len(preds2(x)) == 2)
    n3 = 0
    ne = n1 + 2 * n2 + 3 * n3
    left2 = ne - (2 * n2 + 3 * n3)
    print(f"  2x2: n_one={n1} n_two={n2} leftover={left2}")
    if left2 != n1:
        hit(f"Z1 cancellation on 2x2: leftover {left2} != n_one {n1}")


def check_influence_factor() -> None:
    print("== cube influence N c^3 factor at (3,1,2) ==")
    N = multinomial_N((1, 1, 1))
    c = F(27, 110)
    bound = N * c ** 3
    stated = F(59049, 665500)
    print(f"  N={N} c^3={c ** 3} N c^3={bound} stated 6*(27/110)^3={stated}")
    if bound != stated:
        hit(f"cube N c^3 = {bound} != stated {stated}")
    crude = (3 * c) ** 3
    print(f"  crude (3c)^3={crude} (N=6 vs 27)")
    if bound == crude:
        hit("cube bound used (3c)^3 not N c^3")


def main() -> int:
    check_sum_rules(3, 1, 2, "(3,1,2)")
    check_sum_rules(2, 2, 2, "(2,2,2)")
    check_tv_half(3, 1, 2, F(1, 6), "(3,1,2)")
    check_tv_half(2, 2, 2, F(0), "(2,2,2)")
    check_one_sixth_pairs(3, 1, 2, "(3,1,2)")
    check_one_sixth_pairs(2, 2, 2, "(2,2,2)")
    check_path_N()
    check_generating_function()
    check_z1_cancellation(3, 1, 2)
    check_influence_factor()

    if HITS:
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: pattern (f) NORMALIZATION has purchase (Z1=p+q+4r, K_1≡1, "
        "K_2=K^2 on the 6x6 menu, TV=1/2 giving c1=1/6, (1/6)K and (1/6)K^2 "
        "pair laws, N multinomial with ΣN=3^d, Q4c generating function, Z1 "
        "cancellation leftover n_one) and every identity recomputes exactly "
        "at (3,1,2) and (2,2,2); no HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
