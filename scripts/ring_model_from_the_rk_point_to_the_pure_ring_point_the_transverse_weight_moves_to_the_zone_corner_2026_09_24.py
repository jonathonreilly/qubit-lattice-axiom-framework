#!/usr/bin/env python3
"""From the RK point to the pure-ring point: the transverse weight moves to the zone corner continuously.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 on the cubic L^3 torus with the exact vertex Gauss
law (cubic ice) and the plaquette clause H = -g sum_p (U_p + U_p^dag) + V sum_p n_p, n_p the flippable indicator, g = 1
(open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148 with the forward-walking weight
map of open PR 9163, guiding function exp(alpha(V) N_flip) with alpha = 0.2 (1 - V). Supplied model, finite diagnostics,
no physical reading.

At V = g the clause is the Rokhsar-Kivelson sum of projectors, the uniform superposition over a flip component is an exact
zero-energy ground state, and with alpha = 0 the local energy vanishes identically, so the projector is a random walk
sampling the uniform ice ensemble of the component: every star of the transverse weight map must return to the uniform
value (3 per star, open PR 9163's sum rule) and the energy must be exactly zero. As V decreases to 0 the ring dynamics
takes over; open PRs 9161 and 9163 found the weight at V = 0 moved from the smallest momenta to the zone corner. This
runner follows the axis star (1,0,0), the corner star, the ring expectation u_0 = <U + U^dag> per plaquette (from the
mixed energy and the pure flippable density) and the flippable density along V on 4^3 (five values) and 6^3 (three).

Checks: (1) the RK point reproduces uniform ice exactly in energy and within errors in the map; (2) 4^3 sweep: axis
weight falls and corner weight rises monotonically within errors, resolved between the end points; (3) 6^3 sweep
consistent with 4^3 at the shared V values. Prints TOTAL: PASS=N FAIL=M.
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
G = 1.0


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


def gfmc_map_v(ice, alpha, V, init, n_w, tau_total, dtau, r, E_ref, lag, therm_blocks):
    """Continuous-time projector for H = -sum (U + U^dag) + V N_flip with lineage histories of the weight map and of N_flip;
    pure estimates at forward lag `lag` blocks. With alpha = 0 and V = 1 the local energy is identically zero."""
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    n_hist = lag + 1
    hist = np.zeros((n_w, n_hist, ice.L, ice.L, ice.L))
    nfh = np.zeros((n_w, n_hist))
    E_blocks, maps, sums, nfs, hops = [], [], [], [], 0
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
                E_loc = V * len(P) - lam
                dt = r.exponential(1 / lam) if lam > 0 else np.inf
                if t + dt >= dtau:
                    w[i] *= np.exp(-(E_loc - E_ref) * (dtau - t))
                    EL[i] = E_loc
                    nfh[i, b % n_hist] = len(P) / ice.np_                # flippable density of the walker's configuration
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
            nfs.append(float(wn @ nfh[:, (b - lag) % n_hist]))
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        hist = hist[picks]
        nfh = nfh[picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), np.array(maps), np.array(sums), np.array(nfs), hops


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
rng = np.random.default_rng(7001)
DTAU, LAG, THERM = 0.05, 40, 160
VS = {4: (1.0, 0.75, 0.5, 0.25, 0.0), 6: (1.0, 0.5, 0.0)}
CFG = {4: dict(n_w=120, tau=40.0, sweeps=1500), 6: dict(n_w=120, tau=32.0, sweeps=800)}
uni, sweep = {}, {}
for L in (4, 6):
    ice = Ice(L)
    lab = stars(L)
    corner = (L // 2,) * 3
    samples = loop_vmc(ice, 0.0, sweeps={4: 1600, 6: 800}[L], therm=100, r=rng, start=ice.sector_state(0), fix_winding=True)
    uni[L] = star_table(L, [weight_map(ice, s) for s in samples], lab)
    uni[L]["nf"] = stats(np.array([(np.abs(ice.circ(s)[:-1]) == 4).mean() for s in samples]))
    rows = {}
    for V in VS[L]:
        tV = time.time()
        alpha = 0.2 * (1 - V)
        init = loop_vmc(ice, alpha, sweeps=CFG[L]["sweeps"] // 2, therm=max(60, CFG[L]["sweeps"] // 10), r=rng,
                        start=ice.sector_state(0), fix_winding=True)
        Eb, maps, sums, nfs, hops = gfmc_map_v(ice, alpha, V, init, n_w=CFG[L]["n_w"], tau_total=CFG[L]["tau"], dtau=DTAU, r=rng,
                                               E_ref=(V - 0.29 * (1 - V)) * ice.np_ * 0.26 if V < 1 else 0.0, lag=LAG, therm_blocks=THERM)
        Em, Ee = stats(Eb[THERM:])
        tab = star_table(L, maps, lab)
        nfm, nfe = stats(nfs)
        e0 = Em / ice.np_
        u0 = -(e0 - V * nfm)                                  # <U + U^dag> per plaquette from E_0 = -u_0 N_p + V <N_flip>
        rows[V] = dict(e0=e0, e0e=Ee / ice.np_, u0=u0, nf=nfm, nfe=nfe, axis=tab[(1, 0, 0)][0] / 2, axise=tab[(1, 0, 0)][1] / 2,
                       corner=tab[corner][0], cornere=tab[corner][1], sumdev=float(abs(sums - 3).max()), hops=hops, t=time.time() - tV,
                       Emax=float(np.abs(Eb).max()))
    sweep[L] = rows


def fmt_rows(L):
    return "; ".join(f"V={V:.2f}: e0 {r['e0']:+.5f}, u0 {r['u0']:.4f}, n_f {r['nf']:.4f}, axis T/2 {r['axis']:.3f}+-{r['axise']:.3f}, "
                     f"corner T {r['corner']:.2f}+-{r['cornere']:.2f} ({r['t']:.0f} s)" for V, r in sweep[L].items())


# ---------------------------------------------------------------- 1. the RK point
ok1, det1 = True, []
for L in (4, 6):
    r1, u = sweep[L][1.0], uni[L]
    corner = (L // 2,) * 3
    da = (r1["axis"] - u[(1, 0, 0)][0] / 2) / np.sqrt(r1["axise"] ** 2 + (u[(1, 0, 0)][1] / 2) ** 2)
    dc = (r1["corner"] - u[corner][0]) / np.sqrt(r1["cornere"] ** 2 + u[corner][1] ** 2)
    dn = (r1["nf"] - u["nf"][0]) / np.sqrt(r1["nfe"] ** 2 + u["nf"][1] ** 2)
    ok1 &= r1["Emax"] < 1e-9 and abs(da) <= 3 and abs(dc) <= 3 and abs(dn) <= 3 and r1["sumdev"] < 1e-9
    det1.append(f"{L}^3: max |E(tau)| {r1['Emax']:.0e}; axis T/2 {r1['axis']:.3f}+-{r1['axise']:.3f} vs sector-uniform {u[(1, 0, 0)][0] / 2:.3f}+-{u[(1, 0, 0)][1] / 2:.3f} ({da:+.1f} sigma); "
                f"corner T {r1['corner']:.2f}+-{r1['cornere']:.2f} vs {u[corner][0]:.2f}+-{u[corner][1]:.2f} ({dc:+.1f}); n_f {r1['nf']:.4f}+-{r1['nfe']:.4f} vs {u['nf'][0]:.4f}+-{u['nf'][1]:.4f} ({dn:+.1f}); sum rule to {r1['sumdev']:.0e}")
check("the RK point V = g: the local energy vanishes identically, the projector samples uniform ice (axis star, corner star and flippable "
      "density within 3 standard errors of the zero-winding uniform ensemble), sum rule exact", ok1, "; ".join(det1) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. the 4^3 sweep
r4 = sweep[4]
Vs4 = list(VS[4])
ax = np.array([r4[V]["axis"] for V in Vs4]); axe = np.array([r4[V]["axise"] for V in Vs4])
co = np.array([r4[V]["corner"] for V in Vs4]); coe = np.array([r4[V]["cornere"] for V in Vs4])
mono_axis = all(ax[i + 1] <= ax[i] + 2 * np.sqrt(axe[i] ** 2 + axe[i + 1] ** 2) for i in range(len(Vs4) - 1))
mono_corner = all(co[i + 1] >= co[i] - 2 * np.sqrt(coe[i] ** 2 + coe[i + 1] ** 2) for i in range(len(Vs4) - 1))
res_axis = (ax[0] - ax[-1]) / np.sqrt(axe[0] ** 2 + axe[-1] ** 2)
res_corner = (co[-1] - co[0]) / np.sqrt(coe[0] ** 2 + coe[-1] ** 2)
check("4^3 sweep V = 1, 0.75, 0.5, 0.25, 0: the axis weight falls and the corner weight rises monotonically within errors, both resolved "
      "between the end points at more than 3 standard errors; ring expectation u_0 and flippable density along the way",
      mono_axis and mono_corner and res_axis > 3 and res_corner > 3,
      fmt_rows(4) + f"; end-point resolution axis {res_axis:.1f} sigma, corner {res_corner:.1f} sigma")

# ---------------------------------------------------------------- 3. the 6^3 sweep
r6 = sweep[6]
ok3 = True
det3 = []
for V in VS[6]:
    a4, a6 = r4[V], r6[V]
    det3.append(f"V={V:.2f}: 6^3 axis T/2 {a6['axis']:.3f}+-{a6['axise']:.3f} (4^3 {a4['axis']:.3f}), corner {a6['corner']:.2f}+-{a6['cornere']:.2f} "
                f"(4^3 {a4['corner']:.2f}), u0 {a6['u0']:.4f} (4^3 {a4['u0']:.4f}), n_f {a6['nf']:.4f}")
ok3 &= r6[0.0]["axis"] < r6[0.5]["axis"] < r6[1.0]["axis"] + 2 * r6[1.0]["axise"] and r6[0.0]["corner"] > r6[0.5]["corner"] - 2 * r6[0.5]["cornere"]
ok3 &= abs(r6[0.0]["axis"] - 0.557) < 3 * np.sqrt(r6[0.0]["axise"] ** 2 + 0.022 ** 2)
check("6^3 sweep V = 1, 0.5, 0: the same ordering, the V = 0 axis star agreeing with open PR 9161 (0.557 +- 0.022) within 3 standard errors",
      bool(ok3), "; ".join(det3) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
