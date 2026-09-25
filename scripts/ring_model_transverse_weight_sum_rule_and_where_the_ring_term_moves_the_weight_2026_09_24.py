#!/usr/bin/env python3
"""The transverse weight sum rule of ice, and where the ring term moves the weight at the pure-ring point.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss
law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided
continuous-time projector Monte Carlo of open PR 9148 with the forward-walking (lineage) estimator of open PR 9161.
Supplied model, finite diagnostics, no physical reading.

Exact (Theorem 1): with O_a(k) = N^{-1/2} sum_v e^{-ik.v} sigma_a(v) the link field's Fourier modes, Parseval gives
(1/N) sum_k sum_a |O_a(k)|^2 = 3 for every configuration, and the Gauss law makes the longitudinal combination
sum_a (1 - e^{-ik_a}) O_a(k) vanish identically, so the two transverse polarisations carry all the weight: the zone
average of the transverse weight T(k) = sum_a |O_a(k)|^2 is exactly 3 (3/2 per polarisation) in every ice state and
every state supported on ice. Open PR 9161 found the pure-ring ground state at a third of the uniform-ice value at the
smallest axis momentum; the sum rule says the missing weight sits elsewhere in the zone. Here the full map T(k) is
measured, star by star of the cubic group, for uniform ice and for the pure-ring ground state (forward lag 2), on the 4^3
and 6^3 tori, and the star that receives the weight is identified.

Checks: (1) the identities on samples; (2) uniform-ice star map; (3) pure-ring star map on 4^3 (axis star agrees with
open PR 9161, sum rule exact per block, the receiving star); (4) the same on 6^3. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 900

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


def stats(x, n_bins=10):
    x = np.asarray(x, dtype=float)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))




def fields(ice, sigma):
    """The three link-field components on the vertex grid, component a on the link leaving v along +a."""
    L = ice.L
    return sigma.reshape(L, L, L, 3).transpose(3, 0, 1, 2)


def modes(ice, sigma):
    return np.fft.fftn(fields(ice, sigma), axes=(1, 2, 3)) / np.sqrt(ice.nv)          # O_a(k), shape (3, L, L, L)


def weight_map(ice, sigma):
    return (np.abs(modes(ice, sigma)) ** 2).sum(axis=0)                                # T(k) = sum_a |O_a(k)|^2


def longitudinal_max(ice, sigma):
    F = modes(ice, sigma)
    d = 1 - np.exp(-2j * np.pi * np.arange(ice.L) / ice.L)
    Dx, Dy, Dz = np.meshgrid(d, d, d, indexing="ij")
    return float(np.abs(Dx * F[0] + Dy * F[1] + Dz * F[2]).max())


def stars(L):
    """Cubic-group stars of the torus momenta, labelled by the sorted reduced integers (m1 >= m2 >= m3)."""
    lab = {}
    for m in itertools.product(range(L), repeat=3):
        red = tuple(sorted((min(x, L - x) for x in m), reverse=True))
        lab.setdefault(red, []).append(m)
    return lab


def gfmc_map(ice, alpha, init, n_w, tau_total, dtau, r, E_ref, lag, therm_blocks):
    """Continuous-time projector with lineage histories of the full weight map; pure estimate at forward lag `lag` blocks."""
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    n_hist = lag + 1
    hist = np.zeros((n_w, n_hist, ice.L, ice.L, ice.L))
    E_blocks, maps, sums, hops = [], [], [], 0
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
            hist[i, b % n_hist] = weight_map(ice, sigma)
        W = w.sum()
        E_blocks.append(float((w * EL).sum() / W))
        if b >= therm_blocks:
            wn = w / W
            est = np.einsum("i,ixyz->xyz", wn, hist[:, (b - lag) % n_hist])
            maps.append(est)
            sums.append(float(est.mean()))
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        hist = hist[picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), np.array(maps), np.array(sums), hops


def star_table(L, maps, lab):
    """Star averages of a stack of maps (blocks, L, L, L): mean and ten-bin error per star, and the star size."""
    out = {}
    for red, ms in lab.items():
        per_block = np.array([np.mean([mp[m] for m in ms]) for mp in maps])
        out[red] = stats(per_block) + (len(ms),)
    return out


def fmt_star(red):
    return "(" + ",".join(str(x) for x in red) + ")"


# ------------------------------------------------------------------------------------------------ main
rng = np.random.default_rng(6001)
DTAU, LAG, THERM = 0.05, 40, 160
B4 = {4: (0.692, 0.013), 6: (0.557, 0.022)}          # open PR 9161: pure S_T(k_min) per polarisation (T(k_min)/2)

# ---------------------------------------------------------------- 1. identities
worst_sum, worst_long = 0.0, 0.0
for L in (4, 6):
    ice = Ice(L)
    for s in loop_vmc(ice, 0.0, sweeps=40, therm=20, r=rng) + loop_vmc(ice, ALPHA, sweeps=40, therm=20, r=rng, start=ice.sector_state(0), fix_winding=True):
        worst_sum = max(worst_sum, abs(weight_map(ice, s).mean() - 3))
        worst_long = max(worst_long, longitudinal_max(ice, s))
check("identities on uniform and guided ice samples of 4^3 and 6^3: zone average of the weight map is 3 (Parseval) and the "
      "longitudinal combination sum_a (1 - e^{-ik_a}) O_a(k) vanishes (Gauss law)", worst_sum < 1e-10 and worst_long < 1e-10,
      f"max |mean_k T - 3| {worst_sum:.1e}; max longitudinal amplitude {worst_long:.1e}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. uniform ice
uni = {}
for L in (4, 6):
    ice = Ice(L)
    lab = stars(L)
    samples = loop_vmc(ice, 0.0, sweeps={4: 1600, 6: 800}[L], therm=100, r=rng)
    uni[L] = star_table(L, [weight_map(ice, s) for s in samples], lab)
axis_ok = all(abs(uni[L][(1, 0, 0)][0] / 2 - 1.5) < 0.12 for L in (4, 6))
check("uniform-ice star map on 4^3 and 6^3: the axis star (1,0,0) carries 3/2 per polarisation within 0.12; the map by star (T summed over "
      "the two transverse polarisations; 3 is the zone average)", axis_ok,
      "; ".join(f"{L}^3: " + " ".join(f"{fmt_star(red)}:{uni[L][red][0]:.2f}" for red in sorted(uni[L], reverse=True)) for L in (4, 6))
      + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3./4. pure-ring point
CFG = {4: dict(n_w=120, tau=40.0, sweeps=1500), 6: dict(n_w=120, tau=40.0, sweeps=800)}
pure = {}
for L, cfg in CFG.items():
    tL = time.time()
    ice = Ice(L)
    lab = stars(L)
    init = loop_vmc(ice, ALPHA, sweeps=cfg["sweeps"], therm=max(60, cfg["sweeps"] // 5), r=rng, start=ice.sector_state(0), fix_winding=True)
    var = star_table(L, [weight_map(ice, s) for s in init], lab)
    Eb, maps, sums, hops = gfmc_map(ice, ALPHA, init, n_w=cfg["n_w"], tau_total=cfg["tau"], dtau=DTAU, r=rng, E_ref=-0.29 * ice.np_,
                                    lag=LAG, therm_blocks=THERM)
    Em, Ee = stats(Eb[THERM:])
    tab = star_table(L, maps, lab)
    pure[L] = tab
    ax, axe, _ = tab[(1, 0, 0)]
    dev = (ax / 2 - B4[L][0]) / np.sqrt((axe / 2) ** 2 + B4[L][1] ** 2)
    ratios = {red: tab[red][0] / uni[L][red][0] for red in tab if red != (0, 0, 0)}
    top = max(ratios, key=ratios.get)
    low = min(ratios, key=ratios.get)
    above = sorted([red for red in ratios if tab[red][0] - 2 * tab[red][1] > uni[L][red][0]], reverse=True)
    check(f"pure-ring point on {L}^3: sum rule exact per block, the axis star agrees with open PR 9161, and the star that receives the weight",
          abs(sums - 3).max() < 1e-9 and abs(dev) <= 3 and ratios[top] > 1,
          f"e0 {Em / ice.np_:.5f}+-{Ee / ice.np_:.5f}; mean_k T = 3 to {abs(sums - 3).max():.0e}; axis star T/2 = {ax / 2:.3f}+-{axe / 2:.3f} "
          f"(open PR 9161 {B4[L][0]}+-{B4[L][1]}, {dev:+.1f} sigma); variational axis T/2 {var[(1, 0, 0)][0] / 2:.3f}; "
          f"ratio pure/uniform by star: " + " ".join(f"{fmt_star(red)}:{ratios[red]:.2f}" for red in sorted(ratios, reverse=True))
          + f"; lowest {fmt_star(low)} {ratios[low]:.2f}, highest {fmt_star(top)} {ratios[top]:.2f} "
          f"(pure {tab[top][0]:.2f}+-{tab[top][1]:.2f} vs uniform {uni[L][top][0]:.2f}); stars above uniform at 2 sigma: "
          + (" ".join(fmt_star(red) for red in above) if above else "none") + f"; {hops} hops, {time.time() - tL:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
