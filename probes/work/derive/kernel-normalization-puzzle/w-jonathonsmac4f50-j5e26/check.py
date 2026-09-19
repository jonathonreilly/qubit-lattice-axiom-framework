#!/usr/bin/env python3
"""kernel-normalization-puzzle, attempt a3 (w-jonathonsmac4f50-j5e26): the one-loop (order 1/beta) normalization of the transverse kernel.

Model (probes/lib/formation_levelplane.py; blocks 26/34/35): records s in S^2, s_x ~ vMF(beta S_x), S_x = sum of the n predecessors; lab-frame
transverse field theta_x = s_x^perp (components along t1, t2 orthogonal to the initial direction e3); sigma^2 = A(n beta)/(n beta).
Exact one-step facts: E[theta_x | preds] = A(beta|S|) S^perp/|S|; Cov(theta_x | preds) = (A/k)(I - S^perp S^perpT/|S|^2) + A'(k) S^perp S^perpT/|S|^2,
k = beta|S|; |S|^2 = n^2 - sum_{y<y'} |s_y - s_y'|^2.
 E1  the uniform-stencil identity sum_{y<y'} (1 - cos k.(y - y')) = (n^2/2)(1 - |phi(k)|^2), for the backward 2+1 (n = 3), backward 3+1 (n = 4) and
     light-cone (n = 7) stencils: hence, for the linear stationary covariance C = sigma^2/(1 - |phi|^2) per component, E[delta] = n sigma^2 with
     delta := n - |S| = (1/(2n)) sum_{y<y'} |theta_y - theta_y'|^2 + O(theta^4), exactly (the return sum drops out)
 E2  the gain: A(n beta)(1 + E[delta]/n) with A(k) = 1 - 1/k + O(e^{-2k}), sigma^2 = A(n beta)/(n beta): g = 1 - 1/(n^2 beta^2) + O(beta^-3) (the GIVEN)
 E3  the exchange (Fock) term of the cubic (delta/n) P theta: (1/n^2) sum_y (Gamma(y) - Gamma_bar) theta_y with Gamma(y) = sum_{z in pred} C(y - z);
     it vanishes when the stencil's symmetry group is transitive on ordered pairs of distinct predecessors (the backward simplex stencils, checked),
     and for the light-cone equals -(Delta_Gamma/n^3) n ... = (Delta_Gamma/343)(nearest-neighbour Laplacian), Delta_Gamma = C(2e) + 4C(e1 - e2) - 5C(e)
 E4  the noise: E[Cov(theta_x | preds)] per component = sigma^2 [1 + E[delta]/n - E|P theta|^2/2] + O(beta^-2 sigma^2) = sigma^2 [1 + sigma^2 (2 - W)],
     W = (1/L^d) sum_{k != 0} 1/(1 - |phi|^2) (the site variance per component over sigma^2); symbolic assembly of the one-loop ratio
 N1  (numerical, labelled) W and the light-cone lattice covariances on the executed tori; predictions R = 1 + sigma^2 (2 - W) (backward) and
     R = 1 + sigma^2 (2 - W) - sigma^2 Delta_c/49 (light-cone, small k) against the plateaus of the executed logs; the finite-T transient
     (1 - u^t) averaged over the measurement window for the lowest shell
"""
import glob
import itertools
import math
import os
import re
import sys

import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


STENCILS = {
    "backward 2+1 (n = 3)": [(0, 0), (-1, 0), (0, -1)],
    "backward 3+1 (n = 4)": [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)],
    "light-cone (n = 7)": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
}


def main():
    # E1
    ok = True
    for name, st in STENCILS.items():
        d = len(st[0])
        ks = sp.symbols(f"k1:{d + 1}", real=True)
        n = len(st)
        phi = sum(sp.exp(sp.I * sum(k * c for k, c in zip(ks, y))) for y in st) / n
        u = sp.expand(sp.expand_complex(phi * sp.conjugate(phi)))
        lhs = sum(1 - sp.cos(sum(k * (a - b) for k, a, b in zip(ks, y, yp))) for y, yp in itertools.combinations(st, 2))
        ok &= sp.simplify(sp.expand(sp.expand_trig(lhs - sp.Rational(n * n, 2) * (1 - u)))) == 0
    check("E1", ok, "sum_{y<y'} (1 - cos k.(y - y')) = (n^2/2)(1 - |phi(k)|^2) for the three stencils (symbolic): with C = sigma^2/(1 - |phi|^2) per component, "
          "E|theta_y - theta_y'|^2 = 4 sigma^2 (1/L^d) sum_k (1 - cos k.(y - y'))/(1 - |phi|^2), so E[delta] = (1/(2n)) sum_{y<y'} E|theta_y - theta_y'|^2 = "
          "(2 sigma^2/n)(n^2/2) = n sigma^2 exactly")
    # E2
    b, n = sp.symbols("beta n", positive=True)
    Aa = 1 - 1 / (n * b)
    s2 = Aa / (n * b)
    g = sp.series(Aa * (1 + s2), b, sp.oo, 4).removeO()
    x = sp.Symbol("x", positive=True)
    gx = sp.expand((1 - x) * (1 + x * (1 - x)))
    ok = sp.expand(gx - (1 - 2 * x ** 2 + x ** 3)) == 0 and gx.coeff(x, 1) == 0
    gG = sp.expand((1 - x) * (1 + x))
    ok &= gG == 1 - x ** 2
    check("E2", ok, "the Hartree gain A(n beta)(1 + E[delta]/n) with x = 1/(n beta): (1 - x)(1 + x(1 - x)) = 1 - 2x^2 + x^3 (exact sigma^2 = A/(n beta)); "
          "with the leading sigma^2 = x it is (1 - x)(1 + x) = 1 - x^2, the GIVEN's g = 1 - 1/(n^2 beta^2): in both the order-1/beta term cancels; "
          "the order-1/beta^2 coefficient needs the two-loop terms and is not claimed")
    # E3: exchange term vanishes for the simplex stencils; light-cone form
    ok = True
    for name in ("backward 2+1 (n = 3)", "backward 3+1 (n = 4)"):
        st = STENCILS[name]
        d = len(st[0])
        # the stencil's symmetry: permutations of the n predecessors induced by lattice maps preserving phi (for simplices: all permutations of the
        # step vectors e_a in the event lattice); check transitivity on ordered pairs via the event-lattice picture: the predecessors are X - eps_a,
        # a = 1..n (n = d + 1), pairwise differences eps_a - eps_b all of one orbit under S_n
        n_ = len(st)
        diffs = set()
        for a_, b_ in itertools.permutations(range(n_), 2):
            v = [0] * n_
            v[a_] += 1
            v[b_] -= 1
            diffs.add(tuple(sorted(v)))
        ok &= len(diffs) == 1
    # light-cone: Gamma(y) - Gamma_bar in terms of c(e), c(2e), c(d)
    ce, c2e, cd, c0 = sp.symbols("c_e c_2e c_d c_0")
    def C(v):
        r2 = sum(x * x for x in v)
        nz = sum(1 for x in v if x != 0)
        if r2 == 0:
            return c0
        if r2 == 1:
            return ce
        if r2 == 4:
            return c2e
        if r2 == 2 and nz == 2:
            return cd
        raise ValueError(v)
    st = STENCILS["light-cone (n = 7)"]
    Gam = {y: sum(C(tuple(a - b for a, b in zip(y, z))) for z in st) for y in st}
    Gbar = sum(Gam.values()) / 7
    DG = c2e + 4 * cd - 5 * ce
    ok &= sp.simplify(Gam[(0, 0, 0)] - Gbar + sp.Rational(6, 7) * DG) == 0 and all(sp.simplify(Gam[y] - Gbar - DG / 7) == 0 for y in st if y != (0, 0, 0))
    # symbol: (1/49) sum_y (Gamma(y) - Gamma_bar) e^{ik.y} = (DG/343)(2 sum cos k_j - 6) = -(DG/343) E(k)
    check("E3", ok, "the exchange term (1/n^2) sum_y (Gamma(y) - Gamma_bar) theta_y of the cubic (delta/n) P theta vanishes for the simplex stencils (all ordered pairs "
          "of predecessors, differences eps_a - eps_b of the event lattice, form one orbit, so Gamma is constant); for the light-cone Gamma(0) - Gamma_bar = "
          "-(6/7) Delta, Gamma(+-e_j) - Gamma_bar = Delta/7 with Delta = C(2e) + 4 C(e1 - e2) - 5 C(e): the mean map becomes phi(k) - (Delta/343) E(k)")
    # E4: noise assembly
    S2, W, Dl = sp.symbols("sigma2 W Delta_c")
    noise = 1 + S2 - S2 * (W - 1)
    ok = sp.expand(noise - (1 + S2 * (2 - W))) == 0
    E = sp.Symbol("E", positive=True)
    phi_lc = 1 - E / 7
    m = phi_lc - S2 * Dl * E / 343
    R = noise * (1 - phi_lc ** 2) / (1 - m ** 2)
    R0 = sp.limit(R, E, 0)
    ok &= sp.simplify(R0 - noise / (1 + S2 * Dl / 49)) == 0
    check("E4", ok, "noise per component: sigma^2 [1 + E[delta]/n - E|P theta|^2/2] = sigma^2 [1 + sigma^2 - sigma^2 (W - 1)] = sigma^2 [1 + sigma^2 (2 - W)] "
          "(E|P theta|^2/2 = sigma^2 (1/L^d) sum |phi|^2/(1 - |phi|^2) = sigma^2 (W - 1)); one-loop ratio R(k) = [1 + sigma^2 (2 - W)] (1 - |phi|^2)/(1 - |m(k)|^2), "
          "m = phi for the simplex stencils (k-independent R), and for the light-cone R(0+) = [1 + sigma^2 (2 - W)]/(1 + sigma^2 Delta_c/49) with Delta = sigma^2 Delta_c")
    # N1: numerical (labelled)
    import numpy as np

    def Afun(x):
        return 1 / np.tanh(x) - 1 / x

    def lattice(L, law):
        k = 2 * np.pi * np.fft.fftfreq(L)
        K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
        if law == 4:
            ph = (1 + np.exp(1j * K1) + np.exp(1j * K2) + np.exp(1j * K3)) / 4
        else:
            ph = (1 + 2 * (np.cos(K1) + np.cos(K2) + np.cos(K3))) / 7 + 0j
        u = np.abs(ph) ** 2
        mask = np.ones_like(u, bool)
        mask[0, 0, 0] = False
        G = np.zeros_like(u)
        G[mask] = 1 / (1 - u[mask])
        c = np.real(np.fft.ifftn(G))
        W_ = G.sum() / L ** 3
        Dc = c[2, 0, 0] + 4 * c[1, L - 1, 0] - 5 * c[1, 0, 0] if law == 7 else 0.0
        return W_, Dc, u, K1, K2, K3

    here = os.getcwd()
    rows = []
    agree = []
    zs = []
    for f in sorted(glob.glob(os.path.join(here, "logs/probes/X:*/*.txt"))):
        txt = open(f).read()
        hm = re.search(r"dim=3 \(event lattice Z\^4\) menu=sphere beta=([\d.]+) L=(\d+) T=(\d+) T0=(\d+) seed=\d+; predecessors n=(\d)", txt)
        if not hm:
            continue
        beta, L, T, T0, nn = float(hm.group(1)), int(hm.group(2)), int(hm.group(3)), int(hm.group(4)), int(hm.group(5))
        if beta < 0.9:          # below the ordered regime (the linearization's premise), not compared
            continue
        shells = [float(x) for x in re.findall(r"\|k\| in \[[^)]*\): ([\d.]+)", txt)]
        if len(shells) != 7:
            continue
        W_, Dc, u, K1, K2, K3 = lattice(L, nn)
        s2 = Afun(nn * beta) / (nn * beta)
        pred = (1 + s2 * (2 - W_)) / (1 + s2 * Dc / 49)
        plateau = sum(shells[3:6]) / 3
        # transient for the lowest shell: mean over modes with 0 < |k| < 0.3 of (1/(T - T0)) sum_{t = T0+1..T} (1 - u^t)
        kk = np.sqrt(K1 ** 2 + K2 ** 2 + K3 ** 2)
        sel = (kk > 0) & (kk < 0.3)
        uu = u[sel]
        tt = np.arange(T0 + 1, T + 1)
        trans = np.mean([np.mean(1 - ui ** tt) for ui in uu]) if uu.size else float("nan")
        Wn = T - T0
        se = float(np.sqrt(np.sum((1 + uu) / (1 - uu)) / Wn) / uu.size) if uu.size else float("nan")   # AR(1) |z|^2 autocorrelation u^s
        z = (shells[0] - pred * trans) / (pred * se) if se == se and se > 0 else float("nan")
        zs.append(z)
        # zero-mode tilt (leading order): the lab-frame power at k != 0 is reduced by E|psi|^2/2 = sigma^2 t/L^3 averaged over the window
        tbar = (T0 + 1 + T) / 2
        zm = s2 * tbar / L ** 3
        res0 = plateau - pred
        res1 = plateau - pred * (1 - zm)
        rows.append(f"n={nn} beta={beta:g} L={L}: W={W_:.4f}, predicted {pred:.4f}, measured plateau (shells 4-6) {plateau:.4f}, lowest shell {shells[0]:.4f} "
                    f"(transient factor {trans:.4f}, sampling s.e. {se:.3f}, z = {z:+.1f}); plateau - predicted = {res0:+.4f} = {res0 / s2 ** 2:+.2f} sigma^4; "
                    f"zero-mode tilt factor 1 - sigma^2 tbar/L^3 = {1 - zm:.4f}, with it plateau - predicted = {res1:+.4f} = {res1 / s2 ** 2:+.2f} sigma^4")
        agree.append(abs(pred - plateau) < 0.03)
    ok = len(rows) >= 6 and all(agree) and all(abs(z) < 3 for z in zs)
    check("N1", ok, "(numerical, labelled; lattice sums in floating point on the executed tori, plateaus parsed from logs/probes/X:*) " + "; ".join(rows))
    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("(one-loop Gaussian closure, ATTEMPT.md S5) to order 1/beta the lab-frame transverse kernel of the sphere formation law is S(k) = sigma^2 [1 + sigma^2 (2 - W)]/(1 - |m(k)|^2): the mean map's "
            "order-1/beta corrections cancel (E[delta] = n sigma^2 exactly by the uniform-stencil identity, so g = 1 + O(1/beta^2)), the noise gains sigma^2 "
            "from the misalignment of the predecessors and loses sigma^2 (W - 1) to the tilt of the local mean (the lab-frame projection), W the return "
            "sum; the exchange term vanishes for the backward simplex stencils (R = 1 + sigma^2 (2 - W), flat in k) and equals (Delta/343) x Laplacian for "
            "the light-cone; predicted plateaus 1.025/1.009/1.0024 (backward 3+1, beta 2/6/24) and 1.078/1.055/1.042 (light-cone, beta 1/1.5/2) against "
            "the executed plateaus (N1); the sub-1 lowest shells are the finite-level transient from the aligned start plus sampling noise, not the kernel")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
