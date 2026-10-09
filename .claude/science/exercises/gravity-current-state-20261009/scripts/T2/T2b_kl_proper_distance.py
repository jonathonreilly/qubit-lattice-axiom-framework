#!/usr/bin/env python3
"""T2b: family B = PROPER-DISTANCE kernels (R2 Route 3 construction with reflection-positive profiles).

Action: S = 1/4 sum_{x != y} J(|A(x-y)|) (phi_x - phi_y)^2 + m^2/2 sum phi^2,  A = G^{1/2} = diag(1, g^{1/2}),
so every displacement n in Z^4 (all axes and diagonals alike) is weighted by ONE fixed function of its 4D proper length.
  D_G(q) = m^2 + N sum_{n != 0} J(|A n|) (1 - cos q.n).
Profile: Kallen-Lehmann superposition J(x) = sum_i w_i Delta_{M_i}(x), w_i >= 0, Delta_M the 4D Euclidean propagator.
RP (EXACT, for every spatial metric g): at fixed spatial momentum k, Poisson in the 3 spatial directions gives
  sum_{n vec} J(n0, n vec) e^{i k.n vec} = sum_i w_i sum_{l} exp(-E_il |n0|)/(2 E_il),  E_il^2 = M_i^2 + |k+2 pi l|_g^2,
a positive mixture of lambda^|n0| with 0 < lambda < 1; so D(z0) = a - int dnu/(t - z0), nu >= 0, t > 1 (Lemma N class).
At g = 1 the weights depend only on |n|, so the kernel is hypercubic (indeed it treats every axis identically).
Evaluation: Ewald split of the Schwinger integral at t_c; short part summed in position space (|n_mu| <= 6),
long part summed in momentum space over images l (Poisson, det A = 1).  eps-derivatives analytic.
Width: sigma_N^2 = -4 c4/c2 of the time-axis kernel at zero spatial momentum (Lemma N's definition).
Prediction (m = 0, single mass M): kappa ~ (M^2/2) d^2/deps^2 [sum_{n != 0} J(|An|)]  (lattice-sum 'Epstein' term).
"""
import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.special import k1 as besselk1
from t2_core import CHANNELS, midgrid, fit_power

TC = 0.25          # Ewald split (Schwinger time)
RPOS = 6           # position-space box half-width for the short part
YL, WL = laggauss(80)


def Js_derivs(u, M2, jmax=2):
    """d^j/du^j J_s(u), J_s(u) = int_0^TC (4 pi t)^-2 exp(-u/4t - M2 t) dt, for u > 0 (array)."""
    u = np.asarray(u, float)[..., None]
    wc = 1.0 / TC
    w = wc + 4 * YL / u
    base = (4 / u) * np.exp(-u * wc / 4) / (16 * np.pi ** 2)
    g = np.exp(-M2 / w)
    out = []
    for j in range(jmax + 1):
        out.append((base * ((-w / 4) ** j * g * WL)).sum(-1))
    return out


def f_derivs(v, M2):
    s = v + M2
    f = np.exp(-s * TC) / s
    a = TC + 1 / s
    return f, -f * a, f * (a * a + 1 / s ** 2)


def image_list(thresh=40.0):
    out = []
    rng4 = range(-2, 3)
    for l in np.array(np.meshgrid(rng4, rng4, rng4, rng4, indexing="ij")).reshape(4, -1).T:
        mn = sum((np.pi * (2 * abs(x) - 1)) ** 2 for x in l if x != 0)
        if mn * TC <= thresh:
            out.append(l)
    return np.array(out)


IMAGES = image_list()


class KL:
    """D, D', D'' on the midpoint grid at g = 1 for profile sum_i w_i Delta_{M_i}."""

    def __init__(self, masses, weights, L):
        self.M2 = np.asarray(masses, float) ** 2
        self.w = np.asarray(weights, float)
        self.L = L
        R = RPOS
        rr = np.arange(-R, R + 1)
        n = np.array(np.meshgrid(rr, rr, rr, rr, indexing="ij")).reshape(4, -1).T
        n = n[np.any(n != 0, axis=1)]
        u = (n ** 2).sum(1).astype(float)
        J0 = np.zeros(len(n)); J1 = np.zeros(len(n)); J2 = np.zeros(len(n))
        for M2, wi in zip(self.M2, self.w):
            a, b, c = Js_derivs(u, M2)
            J0 += wi * a; J1 += wi * b; J2 += wi * c
        self.n, self.u, self.J = n, u, (J0, J1, J2)
        # Precompute per-n0 spatial Fourier transforms on the midpoint grid, for D and the channel derivatives.
        k = midgrid(L)
        phase = np.pi / L - np.pi
        self.k = k
        self.tabs = {}
        weights_list = {"D": J0}
        for ch, X in CHANNELS.items():
            ns = n[:, 1:].astype(float)
            an = np.einsum("ni,ij,nj->n", ns, X, ns)
            bn = np.einsum("ni,ij,nj->n", ns, X @ X, ns)
            weights_list["d1" + ch] = J1 * an
            weights_list["d2" + ch] = J2 * an ** 2 + J1 * bn
        for key, wts in weights_list.items():
            tab = {}
            for n0 in range(-R, R + 1):
                sel = n[:, 0] == n0
                arr = np.zeros((L, L, L), complex)
                nn = n[sel, 1:]
                ph = np.exp(1j * phase * nn.sum(1))
                np.add.at(arr, (nn[:, 0] % L, nn[:, 1] % L, nn[:, 2] % L), wts[sel] * ph)
                tab[n0] = np.fft.ifftn(arr) * L ** 3
            # total weight (q-independent part) = sum_n w_n
            self.tabs[key] = (tab, wts.sum())
        K1, K2, K3 = np.meshgrid(k, k, k, indexing="ij")
        self.K = (K1, K2, K3)
        # q = 0 image sums (constants of D, D', D'')
        self.c0 = self._image_terms(np.zeros(4), const=True)

    def _image_terms(self, q0_or_vec, const=False):
        """returns dict of image sums sum_l f(v), and per channel sum_l [f' (-c)], sum_l [f'' c^2 + f' d]."""
        res = {"D": 0.0}
        for ch in CHANNELS:
            res["d1" + ch] = 0.0; res["d2" + ch] = 0.0
        for l in IMAGES:
            if const:
                kv = [np.array(2 * np.pi * l[mu], float) for mu in range(4)]
            else:
                kv = [q0_or_vec + 2 * np.pi * l[0]] + [self.K[i] + 2 * np.pi * l[i + 1] for i in range(3)]
            v = kv[0] ** 2 + kv[1] ** 2 + kv[2] ** 2 + kv[3] ** 2
            ks = kv[1:]
            cd = {}
            for ch, X in CHANNELS.items():
                c = sum(X[i, j] * ks[i] * ks[j] for i in range(3) for j in range(3) if X[i, j] != 0)
                X2 = X @ X
                d = sum(X2[i, j] * ks[i] * ks[j] for i in range(3) for j in range(3) if X2[i, j] != 0)
                cd[ch] = (c, d)
            for M2, wi in zip(self.M2, self.w):
                if const and np.all(l == 0):
                    f = np.exp(-M2 * TC) / M2
                    res["D"] = res["D"] + wi * f
                    continue
                f, f1, f2 = f_derivs(v, M2)
                res["D"] = res["D"] + wi * f
                for ch in CHANNELS:
                    c, d = cd[ch]
                    res["d1" + ch] = res["d1" + ch] + wi * (-f1 * c)
                    res["d2" + ch] = res["d2" + ch] + wi * (f2 * c * c + f1 * d)
        return res

    def slice(self, q0):
        """D, and per channel (D', D'') on the spatial grid at time momentum q0 (N = 1)."""
        img = self._image_terms(q0)
        out = {}
        for key, (tab, tot) in self.tabs.items():
            pos = tot - sum((np.exp(1j * q0 * n0) * tab[n0]).real for n0 in tab)
            out[key] = pos + (self.c0[key] - img[key])
        return out

    def J_tot_dd(self):
        """d^2/deps^2 sum_{n!=0} J(|An|) per channel (position part + nonzero images at q = 0)."""
        return {ch: self.tabs["d2" + ch][1] + self.c0["d2" + ch] for ch in CHANNELS}


def kappa_KL(model, m2=0.0):
    acc = {ch: 0.0 for ch in CHANNELS}
    Dmin = np.inf
    for q0 in midgrid(model.L):
        s = model.slice(q0)
        D = m2 + s["D"]
        Dmin = min(Dmin, D.min())
        for ch in CHANNELS:
            acc[ch] += np.sum(s["d2" + ch] / D - (s["d1" + ch] / D) ** 2)
    return {ch: 0.5 * acc[ch] / model.L ** 4 for ch in CHANNELS}, Dmin


def sigmaN2_KL(masses, weights, lmax=6):
    num = 0.0; den = 0.0
    r = np.arange(-lmax, lmax + 1)
    l = np.array(np.meshgrid(r, r, r, indexing="ij")).reshape(3, -1).T
    for M, w in zip(masses, weights):
        E = np.sqrt(M ** 2 + 4 * np.pi ** 2 * (l ** 2).sum(1))
        x = np.exp(-E)
        Li2 = x * (1 + x) / (1 - x) ** 3
        Li4 = x * (1 + 11 * x + 11 * x ** 2 + x ** 3) / (1 - x) ** 5
        num += w * (Li4 / (2 * E)).sum(); den += w * (Li2 / (2 * E)).sum()
    return num / (3 * den)


def brute_D(M, q, R=40):
    """Direct position sum of sum_{n!=0} Delta_M(|n|)(1 - cos q.n) at g = 1 (validation)."""
    r = np.arange(-R, R + 1)
    acc = 0.0
    for n0 in r:
        n1, n2, n3 = np.meshgrid(r, r, r, indexing="ij")
        rr = np.sqrt(n0 ** 2 + n1 ** 2 + n2 ** 2 + n3 ** 2)
        with np.errstate(divide="ignore", invalid="ignore"):
            J = M * besselk1(M * rr) / (4 * np.pi ** 2 * rr)
        J[rr == 0] = 0.0
        acc += np.sum(J * (1 - np.cos(q[0] * n0 + q[1] * n1 + q[2] * n2 + q[3] * n3)))
    return acc


if __name__ == "__main__":
    print(f"== T2b: Kallen-Lehmann proper-distance kernels; Ewald t_c = {TC}, |n_mu| <= {RPOS}, {len(IMAGES)} images; m = 0 ==")
    # (0) validate Ewald D(q) against a brute-force position sum
    m = KL([1.0], [1.0], 8)
    for q in (np.array([0.3, 0.1, -0.2, 0.4]), np.array([np.pi, 0.5, 1.0, -2.0])):
        # evaluate Ewald at an arbitrary q: reuse internals on a 1-point spatial 'grid'
        m.K = tuple(np.array([[[q[i + 1]]]]) for i in range(3))
        img = m._image_terms(q[0])
        n = m.n
        pos = (m.J[0] * (1 - np.cos(n @ q))).sum()
        D_ew = pos + (m.c0["D"] - img["D"]).item()
        D_bf = brute_D(1.0, q)
        print(f" validate M=1, q={np.round(q,3)}: Ewald {D_ew:.12e}  brute {D_bf:.12e}  rel diff {abs(D_ew-D_bf)/D_bf:.1e}")

    print("\n-- single mass M: kappa vs width (L = 32/48) --")
    print("   M     sigma_N   L    kappa_E        kappa_T        pred_E (M^2/2)J''   pred_T        min D")
    rows = []
    for M in (2.0, 1.0, 0.7, 0.5, 0.35, 0.25, 0.18):
        sN = np.sqrt(sigmaN2_KL([M], [1.0]))
        for L in (32, 48):
            mod = KL([M], [1.0], L)
            kap, Dmin = kappa_KL(mod)
            Jdd = mod.J_tot_dd()
            print(f" {M:5.2f}  {sN:7.3f}  {L:3d}  {kap['E_g']:+.4e}  {kap['T_2g']:+.4e}   {M*M/2*Jdd['E_g']:+.4e}  {M*M/2*Jdd['T_2g']:+.4e}  {Dmin:.2e}")
        rows.append((sN, kap["E_g"], kap["T_2g"], Jdd["E_g"], Jdd["T_2g"]))
    rows = np.array(rows)
    sel = rows[:, 0] >= 4
    for j, name in ((1, "E_g"), (2, "T_2g")):
        p, c = fit_power(rows[sel, 0], rows[sel, j])
        print(f" fit sigma_N >= 4, {name}: |kappa| ~ {c:.4f} sigma_N^-{p:.3f}")
    print(" J_tot'' (lattice-sum curvature) by M, E/T:", [(round(r[0], 2), f"{r[3]:+.4f}", f"{r[4]:+.4f}") for r in rows])

    print("\n-- two-mass profiles at fixed sigma_N (search), L = 32 --")
    rng = np.random.default_rng(7)
    for M0 in (0.5, 0.25):
        target = sigmaN2_KL([M0], [1.0])
        mod = KL([M0], [1.0], 32); k1, _ = kappa_KL(mod); one = max(abs(k1['E_g']), abs(k1['T_2g']))
        best = np.inf
        for _ in range(12):
            Ma = M0 * 10 ** rng.uniform(-0.6, 0.0); Mb = M0 * 10 ** rng.uniform(0.0, 0.8)
            # weights normalized to unit IR coefficient ~ w/M^4; choose mixing so sigma_N matches target
            from scipy.optimize import brentq
            def g(t):
                wa, wb = t * Ma ** 4, (1 - t) * Mb ** 4
                return sigmaN2_KL([Ma, Mb], [wa, wb]) - target
            try:
                t = brentq(g, 1e-6, 1 - 1e-6)
            except ValueError:
                continue
            mod = KL([Ma, Mb], [t * Ma ** 4, (1 - t) * Mb ** 4], 32)
            kk, _ = kappa_KL(mod)
            best = min(best, max(abs(kk['E_g']), abs(kk['T_2g'])))
        print(f" sigma_N = {np.sqrt(target):.2f}: single mass max|kappa| = {one:.4e}; best two-mass = {best:.4e}; ratio {best/one:.3f}")
