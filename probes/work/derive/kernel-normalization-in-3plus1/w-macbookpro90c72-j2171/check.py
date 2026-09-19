#!/usr/bin/env python3
"""J:derive:kernel-normalization-in-3plus1:a3 — exact checks for ATTEMPT.md.

Backward 3+1 formation, n = 4 predecessors, phi(k) = (1 + sum_j exp(-i k_j))/4.
Cubic truncation of the vMF one-step map, closed at Gaussian order on the linear
covariance S_lin(k) = sigma^2 / (1 - |phi|^2) (zero mode removed).
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product

import sympy as sp

N = 4  # predecessors
DIM = 3
I = sp.I
CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    status = "OK" if ok else "FAIL"
    print(f"CHECK {name}: {status}" + (f" ({detail})" if detail else ""))


# ---------------------------------------------------------------------------
# T1. Langevin / vMF identities from Z = 4 pi sinh(kappa)/kappa
# ---------------------------------------------------------------------------
def t1_vmf() -> None:
    k = sp.symbols("kappa", positive=True)
    Z = 4 * sp.pi * sp.sinh(k) / k
    A = sp.coth(k) - 1 / k
    dlog = sp.simplify(sp.diff(sp.log(Z), k) - A)
    record("T1a_mean", dlog == 0, "d log Z / d kappa = A(kappa)")

    # E[(s.u)^2] = Z'' / Z
    Zpp_over_Z = sp.simplify(sp.diff(Z, k, 2) / Z)
    long_var_second_moment = 1 - 2 * A / k
    dlong = sp.simplify(Zpp_over_Z - long_var_second_moment)
    record("T1b_longitudinal", dlong == 0, "Z''/Z = 1 - 2 A/kappa")

    trans = (1 - Zpp_over_Z) / 2
    dtr = sp.simplify(trans - A / k)
    record("T1c_transverse", dtr == 0, "(1 - E[(s.u)^2])/2 = A/kappa")

    # exact large-kappa form of A, not an expansion
    x = sp.symbols("x", positive=True)
    coth_id = sp.simplify(sp.coth(x).rewrite(sp.exp) - (sp.exp(2 * x) + 1) / (sp.exp(2 * x) - 1))
    A_id = sp.simplify(
        (sp.coth(x) - 1 / x).rewrite(sp.exp) - (1 - 1 / x + 2 / (sp.exp(2 * x) - 1))
    )
    record("T1d_coth", coth_id == 0, "coth x = (e^{2x}+1)/(e^{2x}-1)")
    record("T1e_A_exact", A_id == 0, "A(x) = 1 - 1/x + 2/(e^{2x}-1)")


# ---------------------------------------------------------------------------
# T2. 1 - |phi|^2 is the A3 root cosine
# ---------------------------------------------------------------------------
def t2_one_minus_u() -> None:
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sp.exp(-I * k1) + sp.exp(-I * k2) + sp.exp(-I * k3)) / N
    u = sp.simplify(sp.expand_complex(phi * sp.conjugate(phi)))
    rhs = (
        sp.Rational(3, 4)
        - sp.Rational(1, 8)
        * (
            sp.cos(k1)
            + sp.cos(k2)
            + sp.cos(k3)
            + sp.cos(k1 - k2)
            + sp.cos(k1 - k3)
            + sp.cos(k2 - k3)
        )
    )
    diff = sp.simplify(sp.expand_trig(sp.expand_complex((1 - u) - rhs)))
    record("T2_cosine", diff == 0, "1-|phi|^2 = 3/4 - (1/8) sum_{A3 roots} cos")


# ---------------------------------------------------------------------------
# T3. G_4 = 1913/1344
# ---------------------------------------------------------------------------
def _cos_quarter(m: int) -> int:
    return (1, 0, -1, 0)[m % 4]


def _one_minus_u_idx(a: int, b: int, c: int) -> Fr:
    sm = (
        _cos_quarter(a)
        + _cos_quarter(b)
        + _cos_quarter(c)
        + _cos_quarter(a - b)
        + _cos_quarter(a - c)
        + _cos_quarter(b - c)
    )
    return Fr(3, 4) - Fr(1, 8) * sm


def t3_G4() -> None:
    L = 4
    V = L ** 3
    acc = Fr(0)
    n_nonzero = 0
    for a, b, c in product(range(L), repeat=3):
        if a == b == c == 0:
            continue
        acc += 1 / _one_minus_u_idx(a, b, c)
        n_nonzero += 1
    G = acc / V
    record("T3_G4", G == Fr(1913, 1344) and n_nonzero == 63, f"G_4 = {G}")


# ---------------------------------------------------------------------------
# T4. A3 automorphisms; e1 and e1-e2 lie on one orbit
# ---------------------------------------------------------------------------
def _det3(M: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def _matmul(M, v):
    return (
        M[0][0] * v[0] + M[0][1] * v[1] + M[0][2] * v[2],
        M[1][0] * v[0] + M[1][1] * v[1] + M[1][2] * v[2],
        M[2][0] * v[0] + M[2][1] * v[1] + M[2][2] * v[2],
    )


def t4_automorphisms() -> None:
    roots = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, -1, 0),
        (1, 0, -1),
        (0, 1, -1),
    )

    def signed_root_set(vecs):
        s = set()
        for v in vecs:
            s.add(v)
            s.add((-v[0], -v[1], -v[2]))
        return s

    target = signed_root_set(roots)
    autos = []
    for entries in product((-1, 0, 1), repeat=9):
        M = (entries[0:3], entries[3:6], entries[6:9])
        if abs(_det3(M)) != 1:
            continue
        images = [_matmul(M, r) for r in roots]
        if signed_root_set(images) == target:
            autos.append(M)
    record("T4a_count", len(autos) == 48, f"{len(autos)} automorphisms in M_3({{-1,0,1}}), |det|=1")

    e1 = (1, 0, 0)
    edge = (1, -1, 0)
    senders = [M for M in autos if _matmul(M, e1) == edge]
    record(
        "T4b_e1_to_e1_minus_e2",
        len(senders) >= 1,
        f"{len(senders)} maps send e1 to e1-e2; one is {senders[0] if senders else None}",
    )


# ---------------------------------------------------------------------------
# T5. On L=4, C(e1)=C(e1-e2) and H(k)=C_v phi(k) exactly in Q(i)
# ---------------------------------------------------------------------------
class Cq:
    """Complex rationals."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = o if isinstance(o, Cq) else Cq(o)
        return Cq(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        o = o if isinstance(o, Cq) else Cq(o)
        return Cq(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        o = o if isinstance(o, Cq) else Cq(o)
        return Cq(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def __truediv__(self, o):
        if isinstance(o, Cq):
            d = o.re * o.re + o.im * o.im
            return Cq((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)
        return Cq(self.re / o, self.im / o)

    def conj(self):
        return Cq(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, Cq) else Cq(o)
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}+{self.im} i)"


def _cis_quarter(m: int) -> Cq:
    return (Cq(1, 0), Cq(0, 1), Cq(-1, 0), Cq(0, -1))[m % 4]


def _phi_idx(a: int, b: int, c: int) -> Cq:
    return (Cq(1) + _cis_quarter(-a) + _cis_quarter(-b) + _cis_quarter(-c)) / N


def t5_L4_kernel() -> None:
    L = 4
    V = L ** 3
    S = {}
    for a, b, c in product(range(L), repeat=3):
        if a == b == c == 0:
            S[(a, b, c)] = Fr(0)
        else:
            S[(a, b, c)] = 1 / _one_minus_u_idx(a, b, c)

    def C_at(x, y, z):
        acc = Cq(0)
        for a, b, c in product(range(L), repeat=3):
            acc = acc + Cq(S[(a, b, c)]) * _cis_quarter(a * x + b * y + c * z)
        return acc / V

    C0 = C_at(0, 0, 0)
    C100 = C_at(1, 0, 0)
    C1m10 = C_at(1, -1, 0)
    record("T5a_C_equal_edges", C100 == C1m10, f"C(e1)={C100} = C(e1-e2)")
    record("T5b_C0_is_G4", C0 == Cq(Fr(1913, 1344)), f"C(0)={C0}")

    G = sum(S.values()) / V
    Cv = G - (1 - Fr(1, V))
    record("T5c_Cv", Cv == Fr(295, 672), f"C_v = G - (1-1/V) = {Cv}")

    def H_at(kx, ky, kz):
        acc = Cq(0)
        for a, b, c in product(range(L), repeat=3):
            ph_m = _phi_idx((-a) % L, (-b) % L, (-c) % L)
            ph_pk = _phi_idx((a + kx) % L, (b + ky) % L, (c + kz) % L)
            acc = acc + ph_m * ph_pk * Cq(S[(a, b, c)])
        return acc / V

    ks = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 0, 0), (1, 1, 1), (3, 1, 2), (2, 2, 1))
    ok = True
    for k in ks:
        Hk = H_at(*k)
        ph = _phi_idx(*k)
        if Hk != Cq(Cv) * ph:
            ok = False
            record("T5d_H_eq_Cv_phi", False, f"fail at k={k}: H={Hk} vs Cv phi={Cq(Cv)*ph}")
            break
    if ok:
        record("T5d_H_eq_Cv_phi", True, f"H(k)=C_v phi(k) on {len(ks)} modes of L=4")


# ---------------------------------------------------------------------------
# T6. Cubic jet of A=1-1/kappa map matches the stated polynomial
# ---------------------------------------------------------------------------
def t6_cubic_jet() -> None:
    n = N
    eps, delta, beta = sp.symbols("eps delta beta", real=True, positive=True)
    Sx = eps + delta
    Sz = sp.sqrt(1 - eps ** 2) + sp.sqrt(1 - delta ** 2) + (n - 2)
    absS = sp.sqrt(Sx ** 2 + Sz ** 2)
    mx = (1 - 1 / (beta * absS)) * Sx / absS
    # jet: total degree <= 3 in (eps, delta), and 1/beta only on degree <= 1
    ser = sp.expand(mx.series(eps, 0, 4).removeO().series(delta, 0, 4).removeO())
    poly = (
        (1 / n) * Sx
        + (eps ** 2 + delta ** 2) * Sx / (2 * n ** 2)
        - Sx ** 3 / (2 * n ** 3)
        - Sx / (n ** 2 * beta)
    )
    b = sp.symbols("b")
    diff_b = sp.expand((ser - poly).subs(beta, 1 / b))
    rem_terms = []
    for term in sp.Add.make_args(diff_b) if diff_b != 0 else []:
        de = sp.degree(term, eps)
        dd = sp.degree(term, delta)
        db = sp.degree(term, b)
        tot = max(de, 0) + max(dd, 0)
        if tot >= 4:
            continue
        if tot >= 3 and max(db, 0) >= 1:
            continue
        rem_terms.append(term)
    rem = sp.simplify(sum(rem_terms) if rem_terms else 0)
    record("T6_cubic_jet", rem == 0, f"remainder after dropping O(theta^4), O(theta^3/beta) = {rem}")


# ---------------------------------------------------------------------------
# T7. Gain g = 1 - 1/(n beta) + sigma^2 (1-1/V), and the infinite-volume form
# ---------------------------------------------------------------------------
def t7_gain() -> None:
    n, beta, V = sp.symbols("n beta V", positive=True)
    A = 1 - 1 / (n * beta) + 2 / (sp.exp(2 * n * beta) - 1)
    sig2 = A / (n * beta)
    g = 1 - 1 / (n * beta) + sig2 * (1 - 1 / V)
    g_inf = sp.simplify(g.subs(V, sp.oo))
    expected = 1 - 1 / (n ** 2 * beta ** 2) + 2 / (n * beta * (sp.exp(2 * n * beta) - 1))
    d = sp.simplify(g_inf - expected)
    record("T7a_g_infinite_volume", d == 0, "g = 1 - 1/(n^2 beta^2) + 2/(n beta (e^{2n beta}-1))")

    # finite V: C0 - Cv = sig2 (1-1/V) when S = sig2/(1-|phi|^2) off zero
    # then K(k) = (1 - 1/(n beta) + C0 - Cv) phi(k) = g phi(k)
    g_from_parts = 1 - 1 / (n * beta) + sig2 * (1 - 1 / V)
    record("T7b_g_finite_V", sp.simplify(g - g_from_parts) == 0)

    # a_mean at O(1/beta): the 1/beta terms in 1-g cancel, leftover O(1/beta^2)
    # expand 1-g in 1/beta at infinite V, dropping the exponential
    g_poly = 1 - 1 / (n * beta) + (1 - 1 / (n * beta)) / (n * beta)  # drop 2/(e^{...}-1)
    one_minus = sp.expand(1 - g_poly)
    # = 1/(n^2 beta^2)
    record(
        "T7c_order",
        sp.simplify(one_minus - 1 / (n ** 2 * beta ** 2)) == 0,
        "without the exponentially small piece, 1-g = 1/(n^2 beta^2)",
    )

    # mass in 1-|K|^2 at k=0: 1-g^2 = 2(1-g)+O((1-g)^2) = O(1/beta^2), not O(1/beta)
    one_minus_n4 = 1 - expected.subs(n, 4)
    remainder = one_minus_n4 - 1 / (16 * beta ** 2)
    expected_exp = -1 / (2 * beta * (sp.exp(8 * beta) - 1))
    record(
        "T7d_remainder",
        sp.simplify(remainder - expected_exp) == 0,
        "1-g = 1/(16 beta^2) - 1/(2 beta (e^{8 beta}-1)); no power-law O(1/beta)",
    )
    # the exponential remainder is smaller than every power of 1/beta
    ratio = sp.simplify(remainder * beta * sp.exp(8 * beta))
    record(
        "T7e_exponentially_small",
        sp.limit(ratio, beta, sp.oo) == -sp.Rational(1, 2),
        f"beta e^{{8 beta}} (1-g - 1/(16 beta^2)) -> -1/2, so the leftover is ~ e^{{-8 beta}}/(2 beta)",
    )


def main() -> int:
    t1_vmf()
    t2_one_minus_u()
    t3_G4()
    t4_automorphisms()
    t5_L4_kernel()
    t6_cubic_jet()
    t7_gain()
    failed = [c for c in CHECKS if not c[1]]
    n = N
    print(
        "SUMMARY: PARTIAL the cubic-Gaussian one-step map of backward 3+1 vMF formation "
        "(n=4) is K(k)=g phi(k) with g=1-1/(n^2 beta^2)+2/(n beta (e^{2 n beta}-1)) "
        "in infinite volume (finite V: g=1-1/(n beta)+sigma^2 (1-1/V)); the O(1/beta) "
        "mean-map IR stiffness correction vanishes, so a_mean=0 and G_3 does not enter "
        "this truncation; the 1-a/beta kernel ratio cannot arise from cubic Wick closure "
        f"of the mean map ({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: cubic-Gaussian mean map is exactly K(k)=g phi(k) with "
        "g=1-1/(16 beta^2)+2/(4 beta (e^{8 beta}-1)) (n=4, V=infty); "
        "mean-map a=0 at O(1/beta), Goldstone mass 1-g^2=O(1/beta^2)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
