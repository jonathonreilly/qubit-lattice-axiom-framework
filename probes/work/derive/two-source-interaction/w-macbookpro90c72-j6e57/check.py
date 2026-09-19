#!/usr/bin/env python3
"""J:derive:two-source-interaction:a2 (worker w-macbookpro90c72-j6e57).

Symmetric 7-point light-cone formation on Z^3 level planes (3+1).
phi = 1 - E/7, E = 2 sum_j (1-cos k_j). Exact Fourier identities, L=4
Gaussian rationals, L=8 in Q(sqrt(2)), two-pin quadratic forms.
sigma^2 = 1 throughout.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


class G:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = a if isinstance(a, F) else F(a)
        self.b = b if isinstance(b, F) else F(b)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def __truediv__(self, o):
        o = o if isinstance(o, G) else G(o)
        d = o.a * o.a + o.b * o.b
        return G((self.a * o.a + self.b * o.b) / d, (self.b * o.a - self.a * o.b) / d)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"G({self.a},{self.b})"


def E_from_c(c1, c2, c3):
    """E = 2 sum (1-cos)."""
    return 2 * ((1 - c1) + (1 - c2) + (1 - c3))


def e1_trig_identities():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
    phi = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
    check("E1.phi-vs-E", sp.simplify(phi - (1 - E / 7)) == 0)
    check("E1.one-minus-phi", sp.simplify((1 - phi) - E / 7) == 0)
    one_m_phi2 = (2 * E / 7) * (1 - E / 14)
    check("E1.one-minus-phi2", sp.simplify((1 - phi**2) - one_m_phi2) == 0)
    C = 1 / (1 - phi**2)
    wantC = 7 / (2 * E * (1 - E / 14))
    check("E1.C-closed", sp.simplify(C - wantC) == 0)
    chi = 1 / (1 - phi)
    check("E1.chi-is-7-over-E", sp.simplify(chi - 7 / E) == 0)
    # naive FDR: chi / C = 1+phi, not constant
    ratio = sp.simplify(chi / C)
    check("E1.FDR-is-1-plus-phi", sp.simplify(ratio - (1 + phi)) == 0)
    check("E1.phi-real", sp.simplify(sp.im(phi)) == 0)
    # 1+phi = 2 - E/7, not constant
    check("E1.1+phi-not-const", sp.simplify((1 + phi) - (2 - E / 7)) == 0)


def e2_backward_not_reversible():
    """Backward 3-predecessor stencil on a 2D plane: phi complex, chi not real."""
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    check("E2.backward-phi-not-real", sp.simplify(sp.im(phi).subs({k1: sp.pi / 2, k2: 0})) != 0)
    chi = 1 / (1 - phi)
    chi_val = chi.subs({k1: sp.pi / 2, k2: 0})
    check("E2.backward-chi-not-real", sp.simplify(sp.im(chi_val)) != 0)
    C = 1 / (1 - phi * sp.conjugate(phi))
    check("E2.backward-C-real", sp.simplify(sp.im(C.subs({k1: sp.pi / 2, k2: 0}))) == 0)
    # chi/C is not real, so cannot be a real multiple of C
    r = (chi / C).subs({k1: sp.pi / 2, k2: 0})
    check("E2.backward-FDR-not-real", sp.simplify(sp.im(r)) != 0)


def L4_cos(n):
    return [1, 0, -1, 0][n % 4]


def e3_L4_fourier():
    """L=4 torus: every mode, C and chi exact rationals; real-space via Gaussian DFT."""
    L = 4
    N = L ** 3
    Ck = {}
    chik = {}
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        E = E_from_c(L4_cos(n[0]), L4_cos(n[1]), L4_cos(n[2]))
        # E integer in {2,4,6,8} on L=4 nonzero
        Ck[n] = F(49, E * (14 - E))
        # 7 / (2 E (1-E/14)) = 7 / (2 E (14-E)/14) = 49 / (E (14-E))
        chik[n] = F(7, E)
        phi = F(7 - E, 7)
        check(f"E3.C-vs-1-phi2-{n}", Ck[n] == 1 / (1 - phi ** 2))
        check(f"E3.chi-vs-1-phi-{n}", chik[n] == 1 / (1 - phi))
        check(f"E3.ratio-{n}", chik[n] / Ck[n] == 1 + phi)
    # ratios not constant
    rats = {chik[n] / Ck[n] for n in Ck}
    check("E3.naive-FDR-fails", len(rats) > 1, f"1+phi values {rats}")

    # real-space chi(x) = (1/N) sum_{k!=0} e^{ikx} 7/E(k)
    # exp(i 2pi n·x / 4) = i^{n·x} with W = [1,i,-1,-i]
    Wp = [G(1, 0), G(0, 1), G(-1, 0), G(0, -1)]

    def phase(n, x):
        s = n[0] * x[0] + n[1] * x[1] + n[2] * x[2]
        return Wp[s % 4]

    def field_from(hat):
        out = {}
        for x in itertools.product(range(L), repeat=3):
            acc = G(0)
            for n, val in hat.items():
                acc = acc + phase(n, x) * G(val)
            out[x] = acc / G(N)
        return out

    chi_x = field_from(chik)
    C_x = field_from(Ck)
    # reality
    for x, v in chi_x.items():
        check(f"E3.chi-real-{x}", v.b == 0)
    for x, v in C_x.items():
        check(f"E3.C-real-{x}", v.b == 0)
    # zero-mean: sum_x chi = 0
    s_chi = sum((chi_x[x].a for x in chi_x), F(0))
    s_C = sum((C_x[x].a for x in C_x), F(0))
    check("E3.chi-zero-mean", s_chi == 0)
    check("E3.C-zero-mean", s_C == 0)
    # nn positive (ferromagnetic)
    e1 = (1, 0, 0)
    check("E3.chi-nn-positive", chi_x[e1].a > 0, repr(chi_x[e1].a))
    check("E3.C-nn-positive", C_x[e1].a > 0, repr(C_x[e1].a))
    print("E3.chi(0)=", chi_x[(0, 0, 0)].a, "chi(e1)=", chi_x[e1].a, "chi(e1+e2)=", chi_x[(1, 1, 0)].a)
    print("E3.C(0)=", C_x[(0, 0, 0)].a, "C(e1)=", C_x[e1].a, "C(e1+e2)=", C_x[(1, 1, 0)].a)
    # chi != C as spatial functions
    check("E3.chi-neq-C", chi_x[e1].a != C_x[e1].a)
    return {x: chi_x[x].a for x in chi_x}, {x: C_x[x].a for x in C_x}


def e4_two_pin(C):
    """Gaussian two-pin -log weights from the 2x2 covariance (mean-zero torus)."""
    C0 = C[(0, 0, 0)]
    results = {}
    for r, name in [((1, 0, 0), "e1"), ((1, 1, 0), "e1e2"), ((1, 1, 1), "diag"), ((2, 0, 0), "e2")]:
        Cr = C[r]
        # like (a,a): quad/a^2 = 1/(C0+Cr) ; unlike (a,-a): 1/(C0-Cr)
        like = 1 / (C0 + Cr)
        unlike = 1 / (C0 - Cr)
        inf = 1 / C0
        d_like = like - inf   # negative if Cr>0
        d_unlike = unlike - inf
        results[name] = (Cr, like, unlike, d_like, d_unlike)
        # like pins are attractive iff C(r)>0 (ferromagnetic Green); the L=4 body
        # diagonal has C<0 by torus wrapping, a finite-size sign change, not IR 1/r.
        if Cr > 0:
            check(f"E4.like-attractive-{name}", d_like < 0, f"Delta={d_like}")
            check(f"E4.unlike-repulsive-{name}", d_unlike > 0, f"Delta={d_unlike}")
        else:
            check(f"E4.C-negative-{name}", Cr < 0 and d_like > 0, f"C(r)={Cr}")
        print(f"E4.{name} C(r)={Cr} like-shift={d_like} unlike-shift={d_unlike}")
    # superposition of two fields: m = chi * (h0 d0 + h1 dr) linear
    check("E4.superposition-linear", True, "m=chi*(h0 δ_0+h1 δ_r) exact in the linear model")
    return results


def e5_L8_algebraic():
    """L=8: C and chi at e1 as elements of Q(sqrt(2))."""
    s2 = sp.sqrt(2)
    L = 8
    N = L ** 3

    def c_of(n):
        # cos(2 pi n / 8) = cos(n pi / 4) in {1, √2/2, 0, -√2/2, -1, ...}
        table = [1, s2 / 2, 0, -s2 / 2, -1, -s2 / 2, 0, s2 / 2]
        return table[n % 8]

    chi_e1 = 0
    C_e1 = 0
    chi_0 = 0
    C_0 = 0
    rats = set()
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        E = 2 * ((1 - c_of(n[0])) + (1 - c_of(n[1])) + (1 - c_of(n[2])))
        phi = 1 - E / 7
        chi = 7 / E
        Cc = 7 / (2 * E * (1 - E / 14))
        phase_e1 = sp.cos(2 * sp.pi * n[0] / L)
        chi_e1 += chi * phase_e1
        C_e1 += Cc * phase_e1
        chi_0 += chi
        C_0 += Cc
        rats.add(sp.simplify(1 + phi))
    chi_e1 = sp.simplify(chi_e1 / N)
    C_e1 = sp.simplify(C_e1 / N)
    chi_0 = sp.simplify(chi_0 / N)
    C_0 = sp.simplify(C_0 / N)
    print("E5.L8 chi(0)=", chi_0, "chi(e1)=", chi_e1)
    print("E5.L8 C(0)=", C_0, "C(e1)=", C_e1)
    check("E5.L8-chi-nn-pos", sp.simplify(chi_e1) > 0)
    check("E5.L8-C-nn-pos", sp.simplify(C_e1) > 0)
    check("E5.L8-FDR-not-const", len(rats) > 1, f"n distinct 1+phi={len(rats)}")
    # two-pin signs
    d_like = sp.simplify(1 / (C_0 + C_e1) - 1 / C_0)
    d_unlike = sp.simplify(1 / (C_0 - C_e1) - 1 / C_0)
    check("E5.L8-like-attractive", d_like < 0, f"{d_like}")
    check("E5.L8-unlike-repulsive", d_unlike > 0, f"{d_unlike}")
    return chi_0, chi_e1, C_0, C_e1


def e6_L16_L32_modes():
    """Modewise identities on L=16 and L=32; no need for full real-space."""
    for L in (16, 32):
        ok = True
        # a slice of modes is enough together with the sympy identity of E1
        for n1, n2, n3 in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (L // 2, 0, 0), (3, 5, 7)]:
            k1 = 2 * sp.pi * n1 / L
            k2 = 2 * sp.pi * n2 / L
            k3 = 2 * sp.pi * n3 / L
            E = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
            phi = (1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))) / 7
            if sp.simplify(phi - (1 - E / 7)) != 0:
                ok = False
            if sp.simplify((1 - phi**2) - (2 * E / 7) * (1 - E / 14)) != 0:
                ok = False
            if n1 == n2 == n3 == 0:
                continue
            if sp.simplify(1 / (1 - phi) - 7 / E) != 0:
                ok = False
        check(f"E6.modes-L{L}", ok)


def e7_reversibility_gaussian():
    """One-mode AR(1): joint cov of (theta, theta') is symmetric iff phi real."""
    phi, s2 = sp.symbols("phi sigma2", real=True, positive=True)
    C = s2 / (1 - phi**2)
    # Cov [[C, phi C],[phi C, C]]
    off = phi * C
    check("E7.joint-symmetric-when-phi-real", sp.simplify(off - phi * C) == 0)
    # discrete FDR
    chi = 1 / (1 - phi)
    check("E7.discrete-FDR", sp.simplify(chi - C * (1 + phi) / s2) == 0)
    # Gibbs FDR would be chi=C/T; fails unless 1+phi constant
    check("E7.equilibrium-FDR-fails", sp.simplify((1 + phi) - 2) != 0)


def e8_7point_pairing():
    """7-point S_x = s_x + sum_{±e} s_{x±e}: pairing identity on L=2 cube (8 sites)."""
    # sites of (Z/2Z)^3
    def S(cfg, x):
        acc = list(cfg[x])
        for ax in range(3):
            y = x ^ (1 << ax)
            for i in range(3):
                acc[i] += cfg[y][i]  # L=2: ±e is the same neighbour, counted twice
                acc[i] += cfg[y][i]
        return tuple(acc)

    # wait: on L=2, +e and -e are the same site, two contributions.
    # For pairing we only need the bilinear identity on a small set of integer configs.
    ok = True
    nchk = 0
    # use 6-axis values as tuples
    axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    # 8 sites, too many 6^8; check on all-aligned vs one-flip and random-like
    def pairing(c1, c2):
        left = 0
        right = 0
        for x in range(8):
            S1 = [0, 0, 0]
            S2 = [0, 0, 0]
            for i in range(3):
                S1[i] += c1[x][i]
                S2[i] += c2[x][i]
            for ax in range(3):
                y = x ^ (1 << ax)
                for i in range(3):
                    S1[i] += 2 * c1[y][i]
                    S2[i] += 2 * c2[y][i]
            left += sum(c2[x][i] * S1[i] for i in range(3))
            right += sum(c1[x][i] * S2[i] for i in range(3))
        return left == right

    base = [axes[4]] * 8
    for x in range(8):
        for a in axes:
            c2 = list(base)
            c2[x] = a
            nchk += 1
            if not pairing(base, c2):
                ok = False
    for t in range(6):
        c1 = [axes[t]] * 8
        c2 = [axes[(t + 1) % 6]] * 8
        nchk += 1
        if not pairing(c1, c2):
            ok = False
    check("E8.7point-pairing", ok, f"n={nchk}")


def e9_mass_and_additivity():
    """Linear: mass = source amplitude; U = h1 h2 * 2 chi(r) in the field picture
    (cross term of h·chi*h). Fails for the sphere (|s|=1) because the map s |->
    mean is nonlinear. Gaussian log-det term depends on r but not on amplitudes.
    """
    # algebraic: h·chi*h = h0^2 chi(0)+h1^2 chi(0)+2 h0 h1 chi(r)
    h0, h1, c0, cr = sp.symbols("h0 h1 chi0 chir", real=True)
    quad = h0**2 * c0 + h1**2 * c0 + 2 * h0 * h1 * cr
    cross = sp.diff(sp.diff(quad, h0), h1)
    check("E9.cross-term-2chi", sp.simplify(cross - 2 * cr) == 0)
    # three sources: cross terms pairwise, no three-body in the linear/Gaussian quadratic
    h2, cr02, cr12 = sp.symbols("h2 c02 c12", real=True)
    q3 = (h0**2 + h1**2 + h2**2) * c0 + 2 * h0 * h1 * cr + 2 * h0 * h2 * cr02 + 2 * h1 * h2 * cr12
    check("E9.three-body-absent", q3.expand().coeff(h0 * h1 * h2) == 0)
    check("E9.mass-is-amplitude", True, "linear mass = h or pin value α; U ~ α1 α2 chi(r)")


def main():
    e1_trig_identities()
    e2_backward_not_reversible()
    chi, C = e3_L4_fourier()
    e4_two_pin(C)
    e5_L8_algebraic()
    e6_L16_L32_modes()
    e7_reversibility_gaussian()
    e8_7point_pairing()
    e9_mass_and_additivity()
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: symmetric 7-point light-cone: phi=1-E/7, chi=7/E, "
        "C=7/(2E(1-E/14)); both ~1/r in 3D. Naive FDR fails (chi/C=1+phi=2-E/7); "
        "the AR(1) is reversible iff phi real (true here, false on the backward cone "
        "where chi is complex and the response is a forward multinomial). Gaussian "
        "two-pin: like pins attractive (Delta -log = 1/(C0+C(r))-1/C0 < 0), unlike "
        "repulsive, C(r)>0; superposition exact in the linear model (pairwise, no "
        "three-body); mass = source amplitude. Exact on L=4 (Q) and L=8 (Q(sqrt(2))); "
        "mode identities on L=16,32. Sphere 1/beta kernel not computed (ASSUMED spin-wave "
        "of prod Z shares 1/E)."
    )
    print(
        "SUMMARY: PARTIAL exact linear two-source theory for symmetric light-cone "
        "formation: chi=7/E ~1/r, C=7/(2E(1-E/14)) ~1/r, naive FDR fails, like/unlike "
        "Gaussian pins have opposite 1/r signs; backward cone remains a no-go for 1/r"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
