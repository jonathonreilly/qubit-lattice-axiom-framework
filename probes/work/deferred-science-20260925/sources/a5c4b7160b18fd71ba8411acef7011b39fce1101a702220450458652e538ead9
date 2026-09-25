#!/usr/bin/env python3
"""The pure transverse structure factor of the ring model on the 10^3 torus, and the four-size series at the smallest momentum.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss
law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided
continuous-time projector Monte Carlo of open PR 9148 with the forward-walking (lineage) estimator of open PR 9161, in the
zero-winding sector of open PR 9153. Supplied model, finite diagnostics, no physical reading.

Open PR 9161 measured the pure transverse structure factor S_T(k_min) = 0.692 +- 0.013, 0.557 +- 0.022, 0.575 +- 0.028 on
4^3, 6^3, 8^3 (a fall, then a level step) and left the power undecided; open PR 9166 (a supplied Gaussian comparator)
predicts for 10^3 at k_min = pi/5 the values 0.46 (a linear photon, fitted), 0.575 (a level) and 0.375 (a quadratic law),
and warns that the forward-walking lag may need to grow with the torus. This runner adds the 10^3 point with forward
lags out to tau_f = 6, the mode's ground-state correlation at k_min, the Feynman bound 2 u_0 s^2 / S_T, and the
four-size series: pairwise exponents, a linear-plus-constant fit S = S_0 + a k against a pure power S ~ k^nu.

Checks: (1) 10^3 pure-ring point: energy, S_T(k_min) resolved with a lag plateau, correlation chain; (2) the four-size
series and the two fits, reported with residuals; (3) the Feynman bound series. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 1800

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


class Ice:
    def __init__(self, L):
        self.L = L
        self.nv, self.nl = L ** 3, 3 * L ** 3
        self.verts = list(itertools.product(range(L), repeat=3))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        self.axis = np.zeros(self.nl, dtype=int)
        self.coord = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
        self.xc = np.array([self.verts[l // 3][0] for l in range(self.nl)])      # x-coordinate of the link's tail vertex
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        plaq = []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % L
                vb[b] = (vb[b] + 1) % L
                plaq.append([3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b])
        self.plaq = np.array(plaq)
        self.sign = np.tile([1, 1, -1, -1], (len(plaq), 1))
        self.np_ = len(plaq)
        pol = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                pol[l].append(p)
        self.pol = pol
        width = max(len({q for l in links for q in pol[l]}) for links in self.plaq)
        self.A = np.full((self.np_, width), self.np_, dtype=int)
        self.M = np.zeros((self.np_, width, 4))
        for p, links in enumerate(self.plaq):
            aff = sorted({q for l in links for q in pol[l]})
            self.A[p, :len(aff)] = aff
            for j, q in enumerate(aff):
                for k, l in enumerate(links):
                    for h in np.flatnonzero(self.plaq[q] == l):
                        self.M[p, j, k] += self.sign[q, h]

    def circ(self, sigma):
        c = np.zeros(self.np_ + 1)
        c[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        return c

    def deltas(self, sigma, C, P):
        Ca = C[self.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", self.M[P], sigma[self.plaq[P]])
        return Cn, (np.abs(Cn) == 4).sum(axis=1) - (np.abs(Ca) == 4).sum(axis=1)

    def winding_fast(self, sigma):
        return tuple(int(sigma[(self.axis == a) & (self.coord == 0)].sum()) for a in range(3))

    def sector_state(self, quanta=0):
        sigma = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            i = self.vid[v]
            sigma[3 * i] = (-1) ** v[1]
            sigma[3 * i + 1] = (-1) ** v[0]
            sigma[3 * i + 2] = (-1) ** v[0]
        for q in range(quanta):
            for x in range(self.L):
                sigma[3 * self.vid[(x, 1, q)]] *= -1
        return sigma

    def modes(self, ms):
        """Transverse field modes O_b(k e_a) = N^{-1/2} sum over b-links of e^{i k x_a} sigma, b != a, k = 2 pi m / L:
        for each m the six (axis, polarisation) modes."""
        PH = np.zeros((len(ms), 6, self.nl), dtype=complex)
        tail_coord = np.array([self.verts[l // 3] for l in range(self.nl)])       # (nl, 3)
        for j, m in enumerate(ms):
            q = 0
            for a in range(3):
                e = np.exp(1j * 2 * np.pi * m / self.L * tail_coord[:, a]) / np.sqrt(self.nv)
                for b in range(3):
                    if b != a:
                        PH[j, q] = e * (self.axis == b)
                        q += 1
        return PH


def loop_vmc(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    sigma = np.ones(ice.nl, dtype=int) if start is None else start.copy()
    C = ice.circ(sigma)
    W0 = ice.winding_fast(sigma)
    samples = []
    per_sweep = max(1, ice.nl // 20)
    for sw in range(therm + sweeps):
        for _ in range(per_sweep):
            v = r.integers(ice.nv)
            seen, path_l = {v: 0}, []
            while True:
                outs = [l for (l, s) in ice.inc[v] if sigma[l] * s == 1]
                l = outs[r.integers(3)]
                v = ice.head[l] if ice.tail[l] == v else ice.tail[l]
                path_l.append(l)
                if v in seen:
                    cyc = path_l[seen[v]:]
                    break
                seen[v] = len(path_l)
            aff = sorted({p for l in cyc for p in ice.pol[l]})
            before = int((np.abs(C[aff]) == 4).sum())
            sigma[cyc] *= -1
            C_new = (sigma[ice.plaq[aff]] * ice.sign[aff]).sum(axis=1)
            after = int((np.abs(C_new) == 4).sum())
            keep = r.random() < np.exp(2 * alpha * (after - before))
            if keep and fix_winding and ice.winding_fast(sigma) != W0:
                keep = False
            if keep:
                C[aff] = C_new
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            samples.append(sigma.copy())
    return samples


def gfmc_fw(ice, alpha, init, n_w, tau_total, dtau, r, E_ref, PH, lags, corr_idx, fw_idx, therm_blocks):
    """Continuous-time projector with lineage histories: forward-walking (pure) structure factors at the block lags
    `lags`, and ground-state imaginary-time correlations C(j dtau) at the forward lag `fw_idx`."""
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    n_hist = max(max(lags), fw_idx + max(corr_idx)) + 1
    assert therm_blocks >= n_hist
    nm = PH.shape[0]
    hist = np.zeros((n_w, n_hist, nm, 6), dtype=complex)
    E_blocks, S_blocks, C_blocks, hops = [], [], [], 0
    for b in range(n_blocks):
        w = np.ones(n_w)
        EL = np.zeros(n_w)
        for i in range(n_w):
            sigma, C = walkers[i], Cs[i]
            t = 0.0
            while True:
                P = np.flatnonzero(np.abs(C[:-1]) == 4)
                Cn, dN = ice.deltas(sigma, C, P)
                rates = G * np.exp(alpha * dN)
                lam = rates.sum()
                E_loc = -lam
                dt = r.exponential(1 / lam) if lam > 0 else np.inf
                if t + dt >= dtau:
                    w[i] *= np.exp(-(E_loc - E_ref) * (dtau - t))
                    EL[i] = E_loc
                    break
                w[i] *= np.exp(-(E_loc - E_ref) * dt)
                t += dt
                j = r.choice(len(P), p=rates / lam)
                p = P[j]
                sigma[ice.plaq[p]] *= -1
                C[ice.A[p]] = Cn[j]
                C[ice.np_] = 0.0
                hops += 1
            hist[i, b % n_hist] = PH @ sigma
        W = w.sum()
        E_blocks.append(float((w * EL).sum() / W))
        if b >= therm_blocks:
            wn = w / W
            S = np.zeros((len(lags), nm))
            for a, lag in enumerate(lags):
                o = hist[:, (b - lag) % n_hist]                                  # (n_w, nm, 2)
                S[a] = np.einsum("i,ijp->j", wn, np.abs(o) ** 2) / 6
            oa = hist[:, (b - fw_idx) % n_hist]
            Cc = np.zeros((len(corr_idx), nm))
            for a, j in enumerate(corr_idx):
                ob = hist[:, (b - fw_idx - j) % n_hist]
                Cc[a] = np.einsum("i,ijp->j", wn, (oa * ob.conj()).real) / 6
            S_blocks.append(S)
            C_blocks.append(Cc)
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        hist = hist[picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), np.array(S_blocks), np.array(C_blocks), hops


def stats(x, n_bins=10):
    x = np.asarray(x, dtype=float)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))




# ------------------------------------------------------------------------------------------------ main
rng = np.random.default_rng(5001)
DTAU = 0.05
TAUS = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0])
CORR_IDX = [int(round(t / DTAU)) for t in TAUS]
LAGS = [0, 20, 40, 80, 120]                                # forward-walking lags tau_f = 0, 1, 2, 4, 6
FW = 40
THERM = 170
L = 10
CERT = {4: (0.692, 0.013, -0.29263), 6: (0.557, 0.022, -0.28885), 8: (0.575, 0.028, -0.28800)}   # open PR 9161 (forward lag 2)
GAUSS = dict(linear=0.46, level=0.575, quadratic=0.375)    # open PR 9166's 10^3 predictions at k_min


def s2(k):
    return 2 - 2 * np.cos(k)


def window_rate(Cm, Ce, i, j):
    r = (np.log(Cm[i]) - np.log(Cm[j])) / (TAUS[j] - TAUS[i])
    e = np.sqrt((Ce[i] / Cm[i]) ** 2 + (Ce[j] / Cm[j]) ** 2) / (TAUS[j] - TAUS[i])
    return float(r), float(e)


# ---------------------------------------------------------------- 1. the 10^3 point
tL = time.time()
ice = Ice(L)
PH = ice.modes([1, 2])
init = loop_vmc(ice, ALPHA, sweeps=300, therm=80, r=rng, start=ice.sector_state(0), fix_winding=True)
Eb, Sb, Cb, hops = gfmc_fw(ice, ALPHA, init, n_w=100, tau_total=32.0, dtau=DTAU, r=rng, E_ref=-0.29 * ice.np_,
                           PH=PH, lags=LAGS, corr_idx=CORR_IDX, fw_idx=FW, therm_blocks=THERM)
Em, Ee = stats(Eb[THERM:])
e0, e0e = Em / ice.np_, Ee / ice.np_
S = [[stats(Sb[:, a, j]) for a in range(len(LAGS))] for j in range(2)]
Cm = np.array([stats(Cb[:, a, 0])[0] for a in range(len(TAUS))])
Ce = np.array([stats(Cb[:, a, 0])[1] for a in range(len(TAUS))])
S10, S10e = S[0][2]
plateau = max(abs(S[0][a][0] - S10) / np.sqrt(S[0][a][1] ** 2 + S10e ** 2) for a in (3, 4))
k1 = 2 * np.pi / L
u0 = -e0
om = 2 * u0 * s2(k1) / S10
ome = om * S10e / S10
early, ee = window_rate(Cm, Ce, 0, 3)
late, le = window_rate(Cm, Ce, 4, 6)
late2, le2 = window_rate(Cm, Ce, 6, 8)
check("10^3 pure-ring point: energy in the range of the smaller tori, S_T(k_min = pi/5) resolved (error <= 12 %) with a forward-walking "
      "plateau (lags 4 and 6 within 2.5 standard errors of lag 2), correlation chain (early rate <= bound, later rates <= earlier, within errors)",
      -0.292 < e0 < -0.284 and S10e / S10 <= 0.12 and plateau <= 2.5 and early <= om + 2 * np.sqrt(ee ** 2 + ome ** 2)
      and late <= early + 2.5 * np.sqrt(ee ** 2 + le ** 2) and late2 <= late + 2.5 * np.sqrt(le ** 2 + le2 ** 2),
      f"e0 {e0:.5f}+-{e0e:.5f} (8^3 at 120 walkers -0.28800, at 240 -0.28813); S_T(k_min) mixed {S[0][0][0]:.3f}, forward lags 1/2/4/6 "
      + "/".join(f"{S[0][a][0]:.3f}+-{S[0][a][1]:.3f}" for a in (1, 2, 3, 4))
      + f"; S_T(2 pi/5) lag 2 {S[1][2][0]:.3f}+-{S[1][2][1]:.3f}; omega_SMA {om:.3f}+-{ome:.3f}, omega L {om * L:.2f}, omega/k {om / k1:.3f}; "
      f"rates on [0,0.3] {early:.2f}+-{ee:.2f}, [0.5,1] {late:.2f}+-{le:.2f}, [1,2] {late2:.2f}+-{le2:.2f}; {hops} hops, {time.time() - tL:.0f} s")

# ---------------------------------------------------------------- 2. the four-size series
Ls = np.array([4, 6, 8, 10], dtype=float)
ks = 2 * np.pi / Ls
Sv = np.array([CERT[4][0], CERT[6][0], CERT[8][0], S10])
Se = np.array([CERT[4][1], CERT[6][1], CERT[8][1], S10e])
def pair_nu(i, j):
    r = np.log(Sv[i] / Sv[j]) / np.log(Ls[j] / Ls[i])
    e = np.sqrt((Se[i] / Sv[i]) ** 2 + (Se[j] / Sv[j]) ** 2) / np.log(Ls[j] / Ls[i])
    return r, e
# weighted fits: power law ln S = -nu ln L + c ; linear-plus-constant S = S0 + a k
cp, covp = np.polyfit(np.log(Ls), np.log(Sv), 1, w=Sv / Se, cov="unscaled")
nu, nue = -cp[0], float(np.sqrt(covp[0, 0]))
chi_pow = float((((np.exp(np.polyval(cp, np.log(Ls))) - Sv) / Se) ** 2).sum())
cl, covl = np.polyfit(ks, Sv, 1, w=1 / Se, cov="unscaled")
a_lin, S0 = cl[0], cl[1]
a_e, S0e = float(np.sqrt(covl[0, 0])), float(np.sqrt(covl[1, 1]))
chi_lin = float((((np.polyval(cl, ks) - Sv) / Se) ** 2).sum())
pred12 = dict(power=float(np.exp(np.polyval(cp, np.log(12.0)))), linconst=float(np.polyval(cl, 2 * np.pi / 12)))
dev = {name: (S10 - v) / S10e for name, v in GAUSS.items()}
check("the four-size series S_T(k_min) on 4^3-10^3: pairwise exponents, a weighted power-law fit and a linear-plus-constant fit with "
      "their chi^2 (2 degrees of freedom each), the 12^3 value each predicts, and the 10^3 point against open PR 9166's three readings "
      "(reported; no power asserted)", np.isfinite(nu) and np.isfinite(S0),
      f"S_T {', '.join(f'{v:.3f}+-{e:.3f}' for v, e in zip(Sv, Se))}; pairwise nu 4-6 {pair_nu(0, 1)[0]:.2f}+-{pair_nu(0, 1)[1]:.2f}, "
      f"6-8 {pair_nu(1, 2)[0]:.2f}+-{pair_nu(1, 2)[1]:.2f}, 8-10 {pair_nu(2, 3)[0]:.2f}+-{pair_nu(2, 3)[1]:.2f}, 4-10 {pair_nu(0, 3)[0]:.2f}+-{pair_nu(0, 3)[1]:.2f}; "
      f"power law nu = {nu:.2f}+-{nue:.2f} (chi^2 {chi_pow:.1f}); S = S0 + a k: S0 = {S0:.3f}+-{S0e:.3f}, a = {a_lin:.3f}+-{a_e:.3f} (chi^2 {chi_lin:.1f}); "
      f"12^3 predictions: power {pred12['power']:.3f}, linear-plus-constant {pred12['linconst']:.3f}; 10^3 point vs open PR 9166: "
      + ", ".join(f"{n} {v:.3f} ({dev[n]:+.1f} sigma)" for n, v in GAUSS.items()))

# ---------------------------------------------------------------- 3. the Feynman bound series
u0s = np.array([-CERT[4][2], -CERT[6][2], -CERT[8][2], u0])
oms = 2 * u0s * s2(ks) / Sv
omse = oms * Se / Sv
slope = np.polyfit(np.log(ks), np.log(oms), 1, w=oms / omse)[0]
check("the Feynman bound omega_SMA = 2 u0 s^2 / S_T at k_min on 4^3-10^3: omega L, omega/k and the fitted exponent of the bound in k (reported)",
      np.all(np.isfinite(oms)),
      "; ".join(f"{int(Lv)}^3: omega {o:.3f}+-{e:.3f}, omega L {o * Lv:.2f}, omega/k {o / k:.3f}" for Lv, o, e, k in zip(Ls, oms, omse, ks))
      + f"; exponent of omega in k over the four points {slope:.2f} (1 linear, 2 quadratic); late-rate x L at k_min on 10^3 {late * L:.1f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
