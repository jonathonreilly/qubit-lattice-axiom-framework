#!/usr/bin/env python3
"""Conserved winding and finite projector relaxation diagnostics.
Supplied model only. See the bound note for exact hypotheses, estimator biases and historical-input limits.
Numerical PASS thresholds are finite diagnostic checks, not phase or convergence certificates.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md']

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0


def check(label, ok, detail=""):
    # Labels describe finite diagnostics; limits in the source note govern interpretation.
    label = "finite diagnostic: " + label
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
        self.coord = np.zeros(self.nl, dtype=int)             # the link's own coordinate along its axis
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
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

    def sector_state(self, quanta):
        """A zero-winding ice state, sigma(v,x) = (-1)^{v_y}, sigma(v,y) = sigma(v,z) = (-1)^{v_x}, with `quanta` directed
        x-lines (rows of odd y at z = 0, 1, ...) reversed: each reversal adds two to W_x and keeps the ice rule."""
        sigma = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            i = self.vid[v]
            sigma[3 * i] = (-1) ** v[1]
            sigma[3 * i + 1] = (-1) ** v[0]
            sigma[3 * i + 2] = (-1) ** v[0]
        for q in range(quanta):
            y0, z0 = 1, q                                        # row of odd y: all its x-links point along -x
            for x in range(self.L):
                sigma[3 * self.vid[(x, y0, z0)]] *= -1
        return sigma

    def winding(self, sigma):
        """W_a = sum of arrows along axis a through the slab of coordinate 0; also the spread over slabs (0 for ice)."""
        W, spread = [], 0
        for a in range(3):
            slabs = [sigma[(self.axis == a) & (self.coord == x)].sum() for x in range(self.L)]
            W.append(int(slabs[0]))
            spread = max(spread, max(slabs) - min(slabs))
        return tuple(W), spread


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


def gfmc(ice, alpha, init, n_w, tau_total, dtau, r, E_ref):
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    E_blocks, hops = [], 0
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
        W = w.sum()
        E_blocks.append(float((w * EL).sum() / W))
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), hops


def stats(x, n_bins=10):
    x = np.asarray(x)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))


rng = np.random.default_rng(3009)
SIZES = {4: dict(n_w=120, tau=24.0, sweeps=1500, fluxes=(0, 2, 4), relax_w=150, reps=3, relax_tau=6.0),
         6: dict(n_w=150, tau=40.0, sweeps=800, fluxes=(0, 2), relax_w=120, reps=3, relax_tau=6.0),
         8: dict(n_w=80, tau=12.0, sweeps=400, fluxes=(0,), relax_w=80, reps=3, relax_tau=5.0)}
sector_rows, gap_rows = {}, {}
spread_max, hist = 0, {}
check_w = True
for L, cfg in SIZES.items():
    tL = time.time()
    ice = Ice(L)
    samples = loop_vmc(ice, 0.0, sweeps=cfg["sweeps"], therm=max(60, cfg["sweeps"] // 5), r=rng)
    wind = [ice.winding(s) for s in samples]
    spread_max = max(spread_max, max(sp for _, sp in wind))
    Wx = np.array([W[0] for W, _ in wind])
    hist[L] = (float(np.mean(Wx ** 2) / 4), int(len(samples)))            # <Phi_x^2> of uniform ice, Phi = W/2
    by_sector = {}
    for Wx0 in cfg["fluxes"]:
        seed = ice.sector_state(Wx0 // 2)
        ok_ice = all(len([l for (l, sg) in ice.inc[v] if seed[l] * sg == 1]) == 3 for v in range(ice.nv))
        check_w &= ok_ice and ice.winding_fast(seed) == (Wx0, 0, 0)
        by_sector[Wx0] = loop_vmc(ice, 0.0, sweeps=cfg["sweeps"] // 2, therm=max(40, cfg["sweeps"] // 10), r=rng,
                                  start=seed, fix_winding=True)
        check_w &= all(ice.winding_fast(s) == (Wx0, 0, 0) for s in by_sector[Wx0][::7])
    # ------------------------------------------------ 1. sector energies
    E_sec = {}
    for Wx0 in cfg["fluxes"]:
        if len(cfg["fluxes"]) < 2:
            break                                            # relaxation only on this size
        init = by_sector[Wx0]
        Eb, hops = gfmc(ice, ALPHA, init, n_w=cfg["n_w"], tau_total=cfg["tau"], dtau=0.05, r=rng,
                        E_ref=-0.29 * ice.np_)
        E_sec[Wx0] = stats(Eb[len(Eb) // 3:]) + (len(init), hops)
    sector_rows[L] = E_sec
    # ------------------------------------------------ 2. relaxation from uniform ice in the zero-flux sector
    init0 = by_sector[0]
    curves = []
    for rep in range(cfg["reps"]):
        Eb, hops = gfmc(ice, ALPHA, init0, n_w=cfg["relax_w"], tau_total=cfg["relax_tau"], dtau=0.02, r=rng,
                        E_ref=-0.29 * ice.np_)
        curves.append(Eb)
    curve = np.mean(curves, axis=0)
    noise = np.std(curves, axis=0).mean() / np.sqrt(len(curves))
    taus = (np.arange(len(curve)) + 1) * 0.02
    E0 = curve[taus >= cfg["relax_tau"] - 1.5].mean()
    dE0 = np.std(curve[taus >= cfg["relax_tau"] - 1.5]) / np.sqrt(np.sum(taus >= cfg["relax_tau"] - 1.5))
    excess = curve - E0
    sig = max(noise, dE0)

    def fit(lo, hi):
        mask = (taus >= lo) & (taus <= hi) & (excess > 3 * sig)
        if mask.sum() < 8:
            return np.nan, int(mask.sum())
        slope, intercept = np.polyfit(taus[mask], np.log(excess[mask]), 1)
        return -slope, int(mask.sum())

    D_early, n_early = fit(0.3, 0.7)
    D_late, n_late = fit(1.0, 2.5)
    gap_rows[L] = dict(D_early=D_early, n_early=n_early, D_late=D_late, n_late=n_late, E0=E0 / ice.np_, dE0=dE0 / ice.np_,
                       start=curve[0] / ice.np_, secs=time.time() - tL)

# ------------------------------------------------ report
SEC = [L for L in SIZES if len(SIZES[L]["fluxes"]) >= 2]
ok1 = spread_max == 0 and check_w
parts, dE_ref = [], None
for L in SEC:
    E0s = sector_rows[L]
    e0, d0 = E0s[0][0], E0s[0][1]
    e1, d1 = E0s[2][0], E0s[2][1]
    dE1, ddE1 = e1 - e0, np.sqrt(d0 ** 2 + d1 ** 2)
    txt = f"{L}^3: E0(0) {e0:.3f}+-{d0:.3f}, E0(1) {e1:.3f}+-{d1:.3f}, dE(1) {dE1:.3f}+-{ddE1:.3f}, dE(1) L {dE1 * L:.2f}+-{ddE1 * L:.2f}"
    if E0s.get(4) is not None:
        dE2 = E0s[4][0] - e0
        txt += f", dE(2)/dE(1) {dE2 / dE1:.2f}"
    txt += f" (unconstrained uniform-ice <Phi_x^2> {hist[L][0]:.3f} from {hist[L][1]} samples)"
    parts.append(txt)
    if dE_ref is None:
        dE_ref = dE1
        ok1 &= dE1 > 3 * ddE1                                # the smallest torus resolves the one-quantum splitting
    else:
        ok1 &= ddE1 < 0.5 * dE_ref                           # larger tori are precise enough to see a splitting of that size
check("winding sectors: canonical sector states are ice with the intended flux, fluxes are slab-independent, the one-quantum splitting is resolved on 4^3 and the 6^3 run is precise enough to see it; dE(1) L and dE(2)/dE(1)",
      ok1, "; ".join(parts))
REF = {4: -0.2926, 6: -0.2883, 8: -0.2871}                       # open PR 9148's projector energies per plaquette
ok2 = all(np.isfinite(gap_rows[L]["D_early"]) and gap_rows[L]["D_early"] > 0 and abs(gap_rows[L]["E0"] - REF[L]) < 0.002 for L in SIZES)
check("imaginary-time relaxation from a uniform walker distribution: selected-window fits: early and late effective rates by size, ground energies agreeing with open PR 9148",
      ok2, "; ".join(f"{L}^3: start {v['start']:.4f} -> E0 {v['E0']:.4f}+-{v['dE0']:.4f} per plaquette (open PR 9148: {REF[L]:.4f}); "
                     f"rate on tau in [0.3, 0.7]: {v['D_early']:.2f} ({v['n_early']} points), on [1.0, 2.5]: "
                     f"{('%.2f' % v['D_late']) if np.isfinite(v['D_late']) else 'signal below 3 sigma'} ({v['n_late']} points); {v['secs']:.0f} s"
                     for L, v in gap_rows.items()))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
