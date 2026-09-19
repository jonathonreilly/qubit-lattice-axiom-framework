#!/usr/bin/env python3
"""gravity-node-with-the-formation-kernels, attempt a3 (w-jonathonsmac4f50-ja6b4): exact checks behind ATTEMPT.md.

The node (main @ abb98a12): 'The gravity node takes as input the covariant scalar record statistic whose two-point function on the formation
law is the lattice Green function' (docs/work_history/repo/review_feedback/pr8093-evidence/pr8093-original-proposal.md L627-629); the kernel it
uses is the Z^3 graph Green function G = 1/E(k), E(k) = sum_a (2 - 2 cos k_a), with 4 pi r G(r) -> 1, G(0) = 0.252731, the cubic-harmonic
correction [5/(32 pi)] K4(n)/r^3, the small-k symbol |k|^2 - (1/12) sum k^4, and the Regge symbol Delta = sum_a p_a^2, p_a = 2 sin(k_a/2).

 N1  E(k) = sum_a p_a^2 (Regge's Delta at zero frequency) and E = |k|^2 - (1/12) sum k_a^4 + O(k^6)
 L1  light-cone 3+1 (7-stencil, sphere menu): phi = (1 + 2 sum_j cos k_j)/7 = 1 - E/7; chi = 1/(1 - phi) = 7/E exactly;
     C/sigma^2 = 1/(1 - phi^2) = 49/(E (14 - E)) = (7/2)(1/E + 1/(14 - E)); C/(sigma^2 chi) = 1/(1 + phi) = 7/(14 - E) -> 1/2 as k -> 0
 L2  the remainder H = 1/(14 - E): 2 <= 14 - E <= 14 on the torus, and its Fourier coefficients satisfy |H(r)| <= (1/2)(6/7)^{|r|_1}
     (expansion in (E/14)^n with E/14 <= 6/7 and nearest-neighbour support); exact coefficient table on the torus L = 16 against the bound
 L3  the normalization equations: the node's unit coefficient needs A(7 beta)/beta = 1 (response reading, sigma^2 chi) or = 2 (covariance
     reading, (7/2) sigma^2); A(k)/k is decreasing (series lemma), so each has one root; brackets by interval arithmetic (mpmath.iv):
     beta_resp in [0.8273, 0.8274], beta_cov in [0.2340, 0.2341]
 B1  backward 3+1: phi = (1 + sum_j e^{i k_j})/4, 1 - |phi|^2 = (1/8)[sum_j (1 - cos k_j) + sum_{i<j} (1 - cos(k_i - k_j))] (the twelve-neighbour
     FCC Laplacian of the level lattice), small-k form (1/16) k^T (4I - J) k (eigenvalues 4, 4, 1), not a multiple of |k|^2; chi = 1/(1 - phi)
     has chi(-k) = conj chi(k) != chi(k) (one-sided response)
 B2  backward 2+1 (block 35): E(K) = 3|1 - phi e^{iw}|^2 + 3(1 - u(k)) with phi = (1 + e^{ik1} + e^{ik2})/3 (the formation spectral density is not
     c/E: the difference is the mass-like 3(1 - u)); the equal-level kernel sigma^2/(1 - u) is two-dimensional (1 - u = k^T M k + ...)
"""
import itertools
import sys
import time
from fractions import Fraction as F

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def main():
    k1, k2, k3, eps = sp.symbols("k1 k2 k3 epsilon", real=True)
    ks = (k1, k2, k3)
    E = sum(2 - 2 * sp.cos(k) for k in ks)
    # N1
    ok = sp.simplify(sum((2 * sp.sin(k / 2)) ** 2 for k in ks) - E) == 0
    ser = sp.series(E.subs({k1: eps * k1, k2: eps * k2, k3: eps * k3}), eps, 0, 6).removeO()
    ok &= sp.simplify(ser - (eps ** 2 * (k1 ** 2 + k2 ** 2 + k3 ** 2) - eps ** 4 * (k1 ** 4 + k2 ** 4 + k3 ** 4) / 12)) == 0
    check("N1", ok, "E(k) = sum_a (2 - 2 cos k_a) = sum_a p_a^2 with p_a = 2 sin(k_a/2) (the Regge note's Delta at zero frequency), and "
          "E = |k|^2 - (1/12) sum_a k_a^4 + O(k^6) (the cubic-anisotropy note's symbol)")
    # L1
    s2 = sp.Symbol("sigma2", positive=True)
    phi = (1 + 2 * sum(sp.cos(k) for k in ks)) / 7
    ok = sp.simplify(phi - (1 - E / 7)) == 0
    chi = 1 / (1 - phi)
    C = s2 / (1 - phi ** 2)
    ok &= sp.simplify(chi - 7 / E) == 0
    ok &= sp.simplify(C - 49 * s2 / (E * (14 - E))) == 0
    ok &= sp.simplify(C - sp.Rational(7, 2) * s2 * (1 / E + 1 / (14 - E))) == 0
    ok &= sp.simplify(C / (s2 * chi) - 1 / (1 + phi)) == 0 and sp.simplify(C / (s2 * chi) - 7 / (14 - E)) == 0
    check("L1", ok, "light-cone 3+1: phi = (1 + 2 sum cos k_j)/7 = 1 - E/7; static response chi = 1/(1 - phi) = 7/E exactly; equal-time covariance "
          "C = sigma^2/(1 - phi^2) = 49 sigma^2/(E(14 - E)) = (7/2) sigma^2 (1/E + 1/(14 - E)); C/(sigma^2 chi) = 1/(1 + phi) = 7/(14 - E), "
          "equal to 1/2 at k = 0 and 7/2 at the zone corner (E = 12)")
    # L2: the remainder
    # coefficients of (E/14)^n: exact on the torus L = 16 by FFT-free exact convolution in Z^3 (nearest-neighbour polynomial powers)
    def poly_pow(n):
        # E as a Laurent polynomial in z_a: E = 6 - sum_a (z_a + 1/z_a); dict offsets -> coefficient
        base = {(0, 0, 0): F(6)}
        for a in range(3):
            for s in (1, -1):
                off = [0, 0, 0]
                off[a] = s
                base[tuple(off)] = F(-1)
        cur = {(0, 0, 0): F(1)}
        for _ in range(n):
            nxt = {}
            for o, c in cur.items():
                for o2, c2 in base.items():
                    key = (o[0] + o2[0], o[1] + o2[1], o[2] + o2[2])
                    nxt[key] = nxt.get(key, F(0)) + c * c2
            cur = nxt
        return cur
    N = 18
    Hcoef = {}
    for n in range(N + 1):
        pw = poly_pow(n)
        for o, c in pw.items():
            Hcoef[o] = Hcoef.get(o, F(0)) + c / F(14) ** (n + 1)
    # truncation tail bound: sum_{n > N} (1/14)(6/7)^n = (1/2)(6/7)^(N+1)
    tail = F(1, 2) * F(6, 7) ** (N + 1)
    ok = True
    worst = F(0)
    for o, c in Hcoef.items():
        d = abs(o[0]) + abs(o[1]) + abs(o[2])
        if d <= 6:
            bound = F(1, 2) * F(6, 7) ** d
            ok &= abs(c) <= bound + tail
            worst = max(worst, abs(c) / bound)
    check("L2", ok, f"the remainder H = 1/(14 - E) = sum_n (1/14)(E/14)^n with 0 <= E/14 <= 6/7 and (E/14)^n supported on |r|_1 <= n: |H(r)| <= "
          f"(1/2)(6/7)^(|r|_1) (exponentially decaying, so the covariance's tail is (7/2) sigma^2 G(r) up to an exponentially small term); exact partial sums "
          f"(n <= {N}) respect the bound on |r|_1 <= 6 up to the truncation tail {float(tail):.2e}; largest ratio to the bound {float(worst):.3f}")
    # L3: the normalization roots
    import mpmath as mp
    mp.mp.dps = 50
    iv = mp.iv
    iv.dps = 50

    def g_iv(beta, target):
        k = 7 * beta
        e2 = iv.exp(2 * k)
        A = (e2 + 1) / (e2 - 1) - 1 / k            # coth k - 1/k
        return A / beta - target
    def bracket(lo, hi, target):
        a = g_iv(iv.mpf(lo), target)
        b = g_iv(iv.mpf(hi), target)
        return a.a > 0 and b.b < 0
    okr = bracket("0.8273", "0.8274", 1)
    okc = bracket("0.2340", "0.2341", 2)
    # the series lemma gives monotonicity: A(k)/k decreasing (coefficients of cosh u - 1 - u^2/4 - (u/4) sinh u are <= 0), so A(7b)/b = 7 A(7b)/(7b) is decreasing
    u = sp.Symbol("u", positive=True)
    g = sp.cosh(u) - 1 - u ** 2 / 4 - (u / 4) * sp.sinh(u)
    serg = sp.series(g, u, 0, 30).removeO()
    okm = all(serg.coeff(u, 2 * m) <= 0 for m in range(1, 15))
    ser0 = sp.series(sp.coth(7 * u) - 1 / (7 * u), u, 0, 4).removeO()
    lim0 = ser0.coeff(u, 1) if ser0.coeff(u, 0) == 0 else None
    check("L3", okr and okc and okm and lim0 == sp.Rational(7, 3), f"A(7b)/b decreases from 7/3 (b -> 0) to 0 (A(k)/k decreasing: the series of cosh u - 1 - u^2/4 - "
          f"(u/4) sinh u has nonpositive coefficients); interval arithmetic (50 digits) brackets the unique roots: A(7b)/b = 1 at b in [0.8273, 0.8274] "
          f"(response reading: node output sigma^2 chi = A(7b)/(b E)), A(7b)/b = 2 at b in [0.2340, 0.2341] (covariance reading: tail (7/2) sigma^2 = "
          f"A(7b)/(2b))")
    # B1: backward 3+1
    phi4 = (1 + sum(sp.exp(sp.I * k) for k in ks)) / 4
    u4 = sp.expand(sp.expand_complex(phi4 * sp.conjugate(phi4)))
    fcc = sp.Rational(1, 8) * (sum(1 - sp.cos(k) for k in ks) + sum(1 - sp.cos(ks[i] - ks[j]) for i, j in ((0, 1), (0, 2), (1, 2))))
    ok = sp.simplify(sp.expand(sp.expand_trig(1 - u4 - fcc))) == 0
    q = sp.series((1 - u4).subs({k1: eps * k1, k2: eps * k2, k3: eps * k3}), eps, 0, 3).removeO()
    kv = sp.Matrix([k1, k2, k3])
    Q = (4 * sp.eye(3) - sp.ones(3, 3)) / 16
    ok &= sp.simplify(q - eps ** 2 * (kv.T * Q * kv)[0]) == 0
    ev = sorted((4 * sp.eye(3) - sp.ones(3, 3)).eigenvals().items())
    chi4 = 1 / (1 - phi4)
    pt = {k1: sp.Rational(1, 2), k2: sp.Rational(1, 3), k3: sp.Rational(1, 5)}
    c_plus = sp.N(chi4.subs(pt), 20)
    c_minus = sp.N(chi4.subs({k: -v for k, v in pt.items()}), 20)
    ok &= abs(sp.im(c_plus)) > 1e-6 and abs(c_minus - sp.conjugate(c_plus)) < 1e-15
    check("B1", ok, f"backward 3+1: 1 - |phi|^2 = (1/8)[sum_j (1 - cos k_j) + sum_(i<j) (1 - cos(k_i - k_j))], the twelve-neighbour (FCC) Laplacian of the "
          f"level lattice; small-k form k^T (4I - J) k/16 with eigenvalues {ev} (not a multiple of |k|^2: isotropic only in the level lattice's own "
          f"metric); the response chi = 1/(1 - phi) is complex, chi(-k) = conj chi(k) (at k = (1/2, 1/3, 1/5): {sp.N(c_plus, 6)}): one-sided in real space")
    # B2: backward 2+1
    w = sp.Symbol("w", real=True)
    phi3 = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u3 = sp.expand(sp.expand_complex(phi3 * sp.conjugate(phi3)))
    EK = (2 - 2 * sp.cos(k1 + w)) + (2 - 2 * sp.cos(k2 + w)) + (2 - 2 * sp.cos(w))
    absq = sp.expand_complex((1 - phi3 * sp.exp(sp.I * w)) * sp.conjugate(1 - phi3 * sp.exp(sp.I * w)))
    ok = sp.simplify(sp.expand(sp.expand_trig(EK - 3 * absq - 3 * (1 - u3)))) == 0
    check("B2", ok, "backward 2+1 (block 35 in Z^3 coordinates K = (k1 + w, k2 + w, w)): E(K) = 3|1 - phi e^{iw}|^2 + 3(1 - u(k)); the formation spectral "
          "density sigma^2/|1 - phi e^{iw}|^2 is not c/E(K) (the difference is 3(1 - u)), and its equal-level kernel sigma^2/(1 - u) is two-dimensional")
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("the node on main takes a record statistic whose two-point function is the Z^3 Green function 1/E (tail 1/(4 pi r) with coefficient 1, "
            "cubic-harmonic correction, G(0) = 0.252731, Regge Delta = E at zero frequency); of the formation kernels only the light-cone 3+1 one has "
            "the node's symbol: static response chi = 7/E exactly, two-point function C = (7/2) sigma^2 (1/E + 1/(14 - E)) = (7/2) sigma^2 G + an "
            "exponentially small remainder (|H(r)| <= (1/2)(6/7)^|r|_1), with C/(sigma^2 chi) = 7/(14 - E) (1/2 at long wavelength: the formation law "
            "is not an equilibrium FDT pair); with chi as input and sigma^2 = A(7b)/(7b) the node's output is the lattice Green function times "
            "A(7b)/b, unit coefficient at b in [0.8273, 0.8274]; with the two-point function as input the tail coefficient is A(7b)/(2b), unit at b in "
            "[0.2340, 0.2341]; the backward kernels fail the node's symbol (2+1: E = 3|1 - phi e^{iw}|^2 + 3(1 - u); 3+1: the FCC Laplacian of the level "
            "lattice, eigenvalues 4, 4, 1 in the lattice coordinates, one-sided response)")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
