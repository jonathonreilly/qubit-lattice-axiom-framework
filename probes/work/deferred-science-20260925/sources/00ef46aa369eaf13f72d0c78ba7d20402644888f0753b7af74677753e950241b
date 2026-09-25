#!/usr/bin/env python3
"""The Feynman (single-mode) photon bound and the pure transverse structure factor at the pure-ring point.

Setting (all supplied, none adopted): spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law
(cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0 (open PRs 9066, 9072), g = 1; the guided
continuous-time projector Monte Carlo of open PR 9148 started in the zero-winding sector of open PR 9153. Supplied
model, finite diagnostics, no physical reading.

The landed note UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS (2026-09-23) bounds the
photon of the uniform-ice (RK) state by the Feynman quotient 2 n_f s^2 / S_T(k), s^2 = 2 - 2 cos k, and finds it
quadratic because the transverse structure factor S_T(k) of uniform ice is constant at small k. Here the same quotient
is computed in the pure-ring ground state, where an exact sum rule gives the numerator 2 u_0 s^2 from the energy per
plaquette (u_0 = -E_0/N_p) and the denominator is the pure (forward-walking) structure factor of the transverse field
mode O_a(k) = N^{-1/2} sum_{a-links} e^{ikx} sigma, k = 2 pi m / L along one axis, averaged over the three axes and both
transverse polarisations. The lineage histories also give the ground-state imaginary-time correlation C(tau) of the
mode, whose effective rates bound the lowest excitation at that momentum from above and the quotient from below.

Checks: (1) exact 2^3 torus: component, sum rule, quotient against the exact lowest coupled level, exact C(tau);
(2) the projector's mixed and forward-walking estimators against those exact numbers; (3) uniform-ice reference on
4^3, 6^3, 8^3 reproducing the landed constant S_T and quadratic quotient; (4) pure-ring point: energies, the pure
S_T(k_min) by size with its forward-walking plateau and the fitted exponent; (5) the bound times L by size, the
dispersion on 8^3, and the correlation-rate chain. Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import eigsh, expm_multiply

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


def exact_L2(ice, canon):
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    codes = []
    n = 1 << ice.nl
    step = 1 << 18
    for start in range(0, n, step):
        ids = np.arange(start, min(n, start + step), dtype=np.int64)
        sig = (((ids[:, None] >> bits) & 1) * 2 - 1).astype(np.int64)
        ok = np.all(sig @ B.T == 0, axis=1)
        codes.append(ids[ok])
    codes = np.concatenate(codes)
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)

    def sig_of(code):
        return ((code >> bits) & 1) * 2 - 1

    def flippable(code):
        s = sig_of(code)
        return np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)

    def code_of(s):
        return int(((s + 1) // 2 * (1 << bits)).sum())

    c0 = code_of(canon)
    comp = {c0: 0}
    order = [c0]
    q = 0
    while q < len(order):
        c = order[q]
        q += 1
        for p in flippable(c):
            c2 = int(c ^ masks[p])
            if c2 not in comp:
                comp[c2] = len(order)
                order.append(c2)
    n_c = len(order)
    rows, cols = [], []
    for c in order:
        for p in flippable(c):
            rows.append(comp[int(c ^ masks[p])])
            cols.append(comp[c])
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n_c, n_c)).tocsr()
    return codes, order, H, sig_of




# ------------------------------------------------------------------------------------------------ main
rng = np.random.default_rng(4001)
DTAU = 0.05
TAUS = np.array([0.0, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0])
CORR_IDX = [int(round(t / DTAU)) for t in TAUS]
LAGS = [0, 20, 40, 80]                                     # forward-walking lags tau_f = 0, 1, 2, 4
FW = 40                                                    # forward lag (tau_f = 2) behind the correlation function
THERM = 160
REF = {4: -0.2926, 6: -0.2883, 8: -0.2871}                 # open PR 9148's projector energies per plaquette
LANDED_NF8, LANDED_OMEGA8 = 0.25934, 0.2027                # landed uniform-ice runner on 8^3: n_f and 2 n_f K_L s^2 at k = pi/4


def s2(k):
    return 2 - 2 * np.cos(k)


def window_rate(Cm, Ce, i, j):
    r = (np.log(Cm[i]) - np.log(Cm[j])) / (TAUS[j] - TAUS[i])
    e = np.sqrt((Ce[i] / Cm[i]) ** 2 + (Ce[j] / Cm[j]) ** 2) / (TAUS[j] - TAUS[i])
    return float(r), float(e)


# ---------------------------------------------------------------- 1. exact 2^3 torus
ice2 = Ice(2)
canon2 = ice2.sector_state(0)
codes, order, H2, sig_of = exact_L2(ice2, canon2)
n_c = H2.shape[0]
vals, vecs = eigsh(H2, k=12, which="SA")
srt = np.argsort(vals)
vals, vecs = vals[srt], vecs[:, srt]
E0x = float(vals[0])
psi0 = np.abs(vecs[:, 0])
PH2 = ice2.modes([1])
Sg = np.array([sig_of(c) for c in order])
O2 = np.einsum("mpl,cl->cmp", PH2, Sg)[:, 0, :]            # (n_c, 6): the six k = pi transverse modes
meanO = float(np.abs(np.einsum("c,cp->p", psi0 ** 2, O2)).max())
S_ex = float((psi0 ** 2 * (np.abs(O2) ** 2).sum(axis=1)).sum() / 6)
u0x = -E0x / ice2.np_
f_ex, ov, Cex = 0.0, np.zeros(len(vals)), np.zeros(len(TAUS))
Hs = H2 - E0x * identity(n_c)
for q in range(6):
    v = O2[:, q] * psi0
    f_ex += float((np.vdot(v, H2 @ v) - E0x * np.vdot(v, v)).real) / 6
    ov += np.abs(vecs.T @ v) ** 2 / 6
    for a, tau in enumerate(TAUS):
        Cex[a] += float(np.vdot(v, expm_multiply(-tau * Hs, v)).real) / 6
omega_ex = f_ex / S_ex
coupled = [n for n in range(1, len(vals)) if ov[n] > 1e-8]
gap_ex = float(vals[coupled[0]] - E0x)
rates_ex = np.array([window_rate(Cex, np.zeros_like(Cex), a, a + 1)[0] for a in range(len(TAUS) - 1)])
check("exact 2^3 torus: flip component of the canonical zero-winding state, the sum rule f = 2 u0 s^2, the quotient against the "
      "lowest coupled level, and the exact log-convex correlation function",
      len(codes) == 9600 and n_c == 864 and H2.nnz == 6912 and abs(E0x + 9.026721) < 1e-5 and abs(f_ex - 2 * u0x * s2(np.pi)) < 1e-9
      and meanO < 1e-12 and omega_ex >= gap_ex and np.all(np.diff(rates_ex) <= 1e-6),
      f"{len(codes)} ice states, component {n_c} states / {H2.nnz} flips, E0 {E0x:.6f}; f {f_ex:.6f} vs 2 u0 s^2 {2 * u0x * s2(np.pi):.6f}; "
      f"<O> {meanO:.0e}; S {S_ex:.6f}; omega_SMA {omega_ex:.4f} vs lowest coupled level {gap_ex:.4f} (ratio {omega_ex / gap_ex:.3f}; "
      f"uncoupled levels below it: {coupled[0] - 1}); exact rates {rates_ex[0]:.3f} on [0,0.1] -> {rates_ex[-1]:.3f} on [1.5,2]; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. projector estimators against the exact numbers
Eb, Sb, Cb, hops2 = gfmc_fw(ice2, ALPHA, [canon2], n_w=200, tau_total=40.0, dtau=DTAU, r=rng, E_ref=E0x, PH=PH2,
                            lags=LAGS, corr_idx=CORR_IDX, fw_idx=FW, therm_blocks=THERM)
Em, Ee = stats(Eb[THERM:])
S_lag = [stats(Sb[:, a, 0]) for a in range(len(LAGS))]
devS = [(m - S_ex) / e for m, e in S_lag]
Cm2 = np.array([stats(Cb[:, a, 0])[0] for a in range(len(TAUS))])
Ce2 = np.array([stats(Cb[:, a, 0])[1] for a in range(len(TAUS))])
devC = (Cm2[:7] - Cex[:7]) / Ce2[:7]                       # tau <= 1.0
check("projector estimators against the exact 2^3 numbers: mixed energy, forward-walking S at lags 1 and 2, C(tau <= 1) at forward lag 2",
      abs(Em - E0x) <= 3 * Ee and max(abs(devS[1]), abs(devS[2])) <= 3 and np.abs(devC).max() <= 3.5 and np.abs(devC).mean() <= 2,
      f"E mixed {Em:.4f}+-{Ee:.4f} (exact {E0x:.4f}); S mixed {S_lag[0][0]:.4f}+-{S_lag[0][1]:.4f} ({devS[0]:+.1f} sigma), "
      f"forward lags 1/2/4: {S_lag[1][0]:.4f}+-{S_lag[1][1]:.4f} ({devS[1]:+.1f}), {S_lag[2][0]:.4f}+-{S_lag[2][1]:.4f} ({devS[2]:+.1f}), "
      f"{S_lag[3][0]:.4f}+-{S_lag[3][1]:.4f} ({devS[3]:+.1f}) vs exact {S_ex:.4f}; C(tau<=1): max |dev| {np.abs(devC).max():.1f}, "
      f"mean {np.abs(devC).mean():.1f} sigma; {hops2} hops; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3. uniform-ice reference
rk = {}
for L in (4, 6, 8):
    ice = Ice(L)
    PH = ice.modes([1])
    samples = loop_vmc(ice, 0.0, sweeps={4: 2000, 6: 1000, 8: 600}[L], therm=100, r=rng)
    Ou = np.array([PH @ s for s in samples])[:, 0, :]
    Su = (np.abs(Ou) ** 2).mean(axis=1)
    nf = np.array([(np.abs(ice.circ(s)[:-1]) == 4).mean() for s in samples])
    (Sm, Se), (nfm, nfe) = stats(Su), stats(nf)
    rk[L] = dict(S=Sm, Se=Se, nf=nfm, nfe=nfe, omega=2 * nfm * s2(2 * np.pi / L) / Sm, n=len(samples))
Sr = [rk[L]["S"] for L in (4, 6, 8)]
check("uniform-ice reference: S_T(k_min) constant in L and the quotient quadratic, reproducing the landed uniform-ice runner on 8^3",
      abs(rk[8]["nf"] - LANDED_NF8) < 0.003 and max(Sr) / min(Sr) <= 1.25 and abs(rk[8]["omega"] - LANDED_OMEGA8) / LANDED_OMEGA8 <= 0.15
      and rk[8]["omega"] * 8 <= 0.8 * rk[4]["omega"] * 4,
      "; ".join(f"{L}^3: n_f {rk[L]['nf']:.4f}, S_T(k_min) {rk[L]['S']:.3f}+-{rk[L]['Se']:.3f}, omega_RK {rk[L]['omega']:.4f}, omega_RK L {rk[L]['omega'] * L:.2f}"
               for L in (4, 6, 8)) + f" (landed 8^3: n_f {LANDED_NF8}, omega {LANDED_OMEGA8}); {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. pure-ring point: energies and the pure S_T(k_min)
CFG = {4: dict(n_w=120, tau=40.0, sweeps=1500), 6: dict(n_w=120, tau=40.0, sweeps=800), 8: dict(n_w=120, tau=40.0, sweeps=400)}
MS = {4: [1, 2], 6: [1, 2, 3], 8: [1, 2, 3]}
res = {}
for L, cfg in CFG.items():
    tL = time.time()
    ice = Ice(L)
    PH = ice.modes(MS[L])
    init = loop_vmc(ice, ALPHA, sweeps=cfg["sweeps"], therm=max(60, cfg["sweeps"] // 5), r=rng, start=ice.sector_state(0), fix_winding=True)
    Eb, Sb, Cb, hops = gfmc_fw(ice, ALPHA, init, n_w=cfg["n_w"], tau_total=cfg["tau"], dtau=DTAU, r=rng, E_ref=-0.29 * ice.np_,
                               PH=PH, lags=LAGS, corr_idx=CORR_IDX, fw_idx=FW, therm_blocks=THERM)
    Em, Ee = stats(Eb[THERM:])
    res[L] = dict(e0=Em / ice.np_, e0e=Ee / ice.np_, hops=hops, time=time.time() - tL, n_init=len(init),
                  S=[[stats(Sb[:, a, j]) for a in range(len(LAGS))] for j in range(len(MS[L]))],
                  C=[(np.array([stats(Cb[:, a, j])[0] for a in range(len(TAUS))]), np.array([stats(Cb[:, a, j])[1] for a in range(len(TAUS))]))
                     for j in range(len(MS[L]))])
Ls = np.array([4, 6, 8], dtype=float)
Sp = np.array([res[L]["S"][0][2][0] for L in (4, 6, 8)])                 # pure S_T(k_min) at forward lag 2
Spe = np.array([res[L]["S"][0][2][1] for L in (4, 6, 8)])
S4l = np.array([res[L]["S"][0][3][0] for L in (4, 6, 8)])
S4le = np.array([res[L]["S"][0][3][1] for L in (4, 6, 8)])
plateau = np.abs(S4l - Sp) / np.sqrt(Spe ** 2 + S4le ** 2)
coef, cov = np.polyfit(np.log(Ls), np.log(Sp), 1, w=Sp / Spe, cov="unscaled")
nu, nue = -coef[0], float(np.sqrt(cov[0, 0]))
fall = (Sp[0] / Sp[2] - 1) / (Sp[0] / Sp[2] * np.sqrt((Spe[0] / Sp[0]) ** 2 + (Spe[2] / Sp[2]) ** 2))


def pair_nu(i, j):
    r = np.log(Sp[i] / Sp[j]) / np.log(Ls[j] / Ls[i])
    e = np.sqrt((Spe[i] / Sp[i]) ** 2 + (Spe[j] / Sp[j]) ** 2) / np.log(Ls[j] / Ls[i])
    return f"{r:.2f}+-{e:.2f}"


check("pure-ring point: energies reproduce open PR 9148; the pure S_T(k_min) is resolved on 4^3, 6^3, 8^3 with a forward-walking plateau "
      "and falls between 4^3 and 8^3 (threshold 2.5 standard errors); three-point and pairwise exponents S ~ L^-nu",
      all(abs(res[L]["e0"] - REF[L]) < 0.002 for L in REF) and np.all(Spe / Sp <= 0.12) and np.all(plateau <= 2.5) and fall >= 2.5,
      "; ".join(f"{L}^3: e0 {res[L]['e0']:.5f}+-{res[L]['e0e']:.5f} (ref {REF[L]}), S_T(k_min) mixed {res[L]['S'][0][0][0]:.3f}, "
               f"forward lags 1/2/4 {res[L]['S'][0][1][0]:.3f}/{res[L]['S'][0][2][0]:.3f}+-{res[L]['S'][0][2][1]:.3f}/{res[L]['S'][0][3][0]:.3f}+-{res[L]['S'][0][3][1]:.3f}, "
               f"{res[L]['hops']} hops, {res[L]['time']:.0f} s" for L in (4, 6, 8))
      + f"; uniform-ice S_T(k_min) {rk[4]['S']:.2f}/{rk[6]['S']:.2f}/{rk[8]['S']:.2f}; fall S(4)/S(8) - 1 = {Sp[0] / Sp[2] - 1:.2f} at {fall:.1f} sigma; "
        f"three-point nu = {nu:.2f}+-{nue:.2f}, pairwise 4-6 {pair_nu(0, 1)}, 6-8 {pair_nu(1, 2)} (1 for a linear photon, 0 for the uniform-ice constant)")

# ---------------------------------------------------------------- 5. the bound times L, the dispersion on 8^3, the correlation chain
rows, cond5 = [], True
omegaL = {}
for L in (4, 6, 8):
    k = 2 * np.pi / L
    u0 = -res[L]["e0"]
    S, Se = res[L]["S"][0][2]
    om = 2 * u0 * s2(k) / S
    ome = om * Se / S
    omegaL[L] = (om, ome)
    Cm, Ce = res[L]["C"][0]
    early, ee = window_rate(Cm, Ce, 0, 3)
    late, le = window_rate(Cm, Ce, 4, 6)
    cond5 &= early <= om + 2 * np.sqrt(ee ** 2 + ome ** 2) and late <= early + 2.5 * np.sqrt(ee ** 2 + le ** 2)
    rows.append(f"{L}^3 (k {k:.3f}): omega_SMA {om:.3f}+-{ome:.3f}, omega L {om * L:.2f}+-{ome * L:.2f}, omega/k {om / k:.3f} (uniform ice {rk[L]['omega'] / k:.3f}); "
                f"rates on [0,0.3] {early:.2f}+-{ee:.2f}, on [0.5,1] {late:.2f}+-{le:.2f}, late x L {late * L:.1f}")
disp = []
for j, m in enumerate(MS[8]):
    k = 2 * np.pi * m / 8
    S, Se = res[8]["S"][j][2]
    disp.append(2 * (-res[8]["e0"]) * s2(k) / S)
d2, d3 = disp[1] / disp[0], disp[2] / disp[0]
lat2, lat3 = np.sqrt(s2(np.pi / 2) / s2(np.pi / 4)), np.sqrt(s2(3 * np.pi / 4) / s2(np.pi / 4))
stable = abs(omegaL[8][0] * 8 - omegaL[4][0] * 4) / np.sqrt((omegaL[8][1] * 8) ** 2 + (omegaL[4][1] * 4) ** 2)
check("the Feynman bound: omega_SMA L by size next to the uniform-ice value (reported, not asserted), the dispersion of the bound on "
      "8^3, and the correlation-rate chain (early rate <= bound, late rate <= early rate, within errors)", bool(cond5),
      "; ".join(rows) + f"; omega L on 8^3 differs from 4^3 by {stable:.1f} sigma; 8^3 bound at k = pi/4, pi/2, 3pi/4: "
      f"{disp[0]:.3f}, {disp[1]:.3f}, {disp[2]:.3f}; ratios {d2:.2f}, {d3:.2f} (linear 2, 3; lattice 2 sin(k/2): {lat2:.2f}, {lat3:.2f}; quadratic 4, 9); "
      f"8^3 S_T at pi/2 {res[8]['S'][1][2][0]:.3f}+-{res[8]['S'][1][2][1]:.3f} vs 4^3 {res[4]['S'][0][2][0]:.3f}+-{res[4]['S'][0][2][1]:.3f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
