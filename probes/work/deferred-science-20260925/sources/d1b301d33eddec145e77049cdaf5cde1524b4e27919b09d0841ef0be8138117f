#!/usr/bin/env python3
"""Two regulators at the pure-ring point: a region bounded by records against the torus, and the walker population.

Setting (all supplied, none adopted): spin-1/2 link fields sigma = +-1 with the exact vertex Gauss law (cubic ice) and the
covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (landed); the guided continuous-time projector Monte Carlo with
lineage (forward-walking) estimators of open PRs 9148 and 9161. Supplied model, finite diagnostics, no physical reading.

The Lattice axiom's sites are all of Z^3. Every finite computation needs a regulator; open PRs 9161-9171 used the torus.
This runner compares two regulators of the same bulk question. (i) The boundary: the unrecorded interior {1..m}^3 of a
lattice whose other links carry records (a region bounded by records, the framework's own finite object) against the
torus of the same size, in real-space field correlations and block variances. (ii) The population: the number of walkers
at fixed torus size, since the projector's bias grows as the walker weights spread with the system size.

Exact (Theorem 1): a record on a link removes every ring term containing that link (P_q U_p P_q = 0), so the clause on a
region bounded by records is the clause of its unrecorded plaquettes; and by the Gauss law every plane-section flux of the
region equals a sum of recorded values, so the region has no winding sectors: its fluxes are fixed by its records.

Checks: (1) the record identities, exactly and on every state of an exact flip component; (2) the projector with records
against exact diagonalization on a 3^3-interior region; (3) the population regulator: local-energy spread by size and a
walker scan on the 8^3 torus; (4) the boundary regulator: torus against record-bounded boxes at 6 and 8, two frames at 8;
(5) the depth profile of the box. Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 3600

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0
DRY = "--dry" in sys.argv


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




class Region:
    """The unrecorded interior {1..m}^3 of an L_out = m + 2 torus whose other links carry records, or the whole torus (m = None)."""
    def __init__(self, ice, m=None):
        self.ice, self.m, self.L = ice, m, ice.L
        V = np.array(ice.verts)
        if m is None:
            self.vin = np.ones(ice.nv, bool)
            self.rec = np.zeros(ice.nl, bool)
            self.depth = np.full(ice.nv, 10 ** 6)
        else:
            assert ice.L == m + 2
            self.vin = np.all((V >= 1) & (V <= m), axis=1)
            self.rec = ~(self.vin[ice.tail] & self.vin[ice.head])
            self.depth = np.where(self.vin, np.min(np.minimum(V, m + 1 - V), axis=1), 0)
        self.dyn = ~self.rec[ice.plaq].any(axis=1)
        self.dyn_ext = np.append(self.dyn, False)
        self.n_dyn = int(self.dyn.sum())
        self.V = V

    def deltas(self, sigma, C, P):
        ice = self.ice
        Ca = C[ice.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", ice.M[P], sigma[ice.plaq[P]])
        dm = self.dyn_ext[ice.A[P]]
        return Cn, ((np.abs(Cn) == 4) & dm).sum(axis=1) - ((np.abs(Ca) == 4) & dm).sum(axis=1)

    def plane_fluxes(self, sigma):
        """Flux of the unrecorded links through every lattice plane section of the region (all axes, all positions)."""
        ice = self.ice
        out = []
        for a in range(3):
            sel = (ice.axis == a) & ~self.rec
            coords = ice.coord[sel]
            vals = sigma[sel]
            out += [int(vals[coords == c].sum()) for c in np.unique(coords)]
        return np.array(out)


def gfmc_region(reg, alpha, init, n_w, tau_total, dtau, r, E_ref, lag, therm_blocks, measure):
    ice = reg.ice
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    n_hist = lag + 1
    hist = np.zeros((n_w, n_hist, ice.nl), dtype=np.int8)
    anc = np.tile(np.arange(n_w), (n_hist, 1)).T.copy()          # anc[i, s]: index of walker i's ancestor at slot s
    E_blocks, meas, ess, ndist, hops = [], [], [], [], 0
    for b in range(n_blocks):
        w = np.ones(n_w)
        EL = np.zeros(n_w)
        for i in range(n_w):
            sigma, C = walkers[i], Cs[i]
            t = 0.0
            while True:
                P = np.flatnonzero((np.abs(C[:-1]) == 4) & reg.dyn)
                Cn, dN = reg.deltas(sigma, C, P)
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
            hist[i, b % n_hist] = sigma
        anc[:, b % n_hist] = np.arange(n_w)
        W = w.sum()
        E_blocks.append(float((w * EL).sum() / W))
        ess.append(float(W * W / (w * w).sum() / n_w))
        if b >= therm_blocks:
            wn = w / W
            slot = (b - lag) % n_hist
            meas.append(measure(hist[:, slot], wn))
            ndist.append(len(np.unique(anc[:, slot])) / n_w)
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        hist = hist[picks]
        anc = anc[picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), meas, dict(ess=float(np.mean(ess[therm_blocks:])), ndist=float(np.mean(ndist)), hops=hops)


def torus_measure(reg):
    L = reg.L
    def meas(S, wn):
        F = S.reshape(len(wn), L, L, L, 3).astype(float)
        Fk = np.fft.fftn(F, axes=(1, 2, 3))
        circ = (S.astype(float)[:, reg.ice.plaq] * reg.ice.sign).sum(axis=2)
        return dict(P=np.einsum("i,ixyza->axyz", wn, np.abs(Fk) ** 2), nf=float(wn @ (np.abs(circ) == 4).mean(axis=1)))
    return meas


def torus_derived(L, Pbar, r_max=3, ells=(1, 2, 3)):
    """From the averaged P_a(k): connected correlations along (longitudinal, transverse) separations, and block variances."""
    N = L ** 3
    Cr = np.real(np.fft.ifftn(Pbar, axes=(1, 2, 3))) / N                # C_a(r) = (1/N) sum_v s_a(v) s_a(v + r)
    gL = [np.mean([Cr[a][tuple(rr * np.eye(3, dtype=int)[a])] for a in range(3)]) for rr in range(1, r_max + 1)]
    gT = [np.mean([Cr[a][tuple(rr * np.eye(3, dtype=int)[b])] for a in range(3) for b in range(3) if b != a]) for rr in range(1, r_max + 1)]
    chi = []
    ks = 2 * np.pi * np.arange(L) / L
    for ell in ells:
        w1 = np.array([np.sum(np.exp(-1j * k * np.arange(ell))) for k in ks])
        W2 = np.abs(w1[:, None, None] * w1[None, :, None] * w1[None, None, :]) ** 2
        chi.append(float(np.mean([np.sum(Pbar[a] * W2) for a in range(3)]) / N ** 2 / ell ** 3))
    ST = []
    for mm in (1, 2):
        vals = []
        for b in range(3):
            idx = [0, 0, 0]; idx[b] = mm
            vals += [Pbar[a][tuple(idx)] / N for a in range(3) if a != b]
        ST.append(float(np.mean(vals)))
    return dict(gL=np.array(gL), gT=np.array(gT), chi=np.array(chi), ST=np.array(ST))


def box_setup(reg, dcore, r_max=3, ells=(1, 2, 3)):
    """Index arrays for the core of a record-bounded box: link pairs by class and block link sets."""
    ice, m = reg.ice, reg.m
    vid = ice.vid
    core_v = reg.depth >= dcore
    core_link = (~reg.rec) & core_v[ice.tail] & core_v[ice.head]
    E = np.eye(3, dtype=int)
    pairs = {}
    for kind in ("L", "T"):
        for rr in range(1, r_max + 1):
            xs, ys = [], []
            for a in range(3):
                for b in range(3):
                    if (kind == "L") != (b == a):
                        continue
                    for v in ice.verts:
                        x = 3 * vid[v] + a
                        u = tuple(np.array(v) + rr * E[b])
                        if min(u) < 0 or max(u) >= ice.L:
                            continue
                        y = 3 * vid[u] + a
                        if core_link[x] and core_link[y]:
                            xs.append(x); ys.append(y)
            pairs[(kind, rr)] = (np.array(xs), np.array(ys))
    blocks = {}
    for ell in ells:
        pos = []
        for v0 in ice.verts:
            idx = []
            ok = True
            for a in range(3):
                la = []
                for u in itertools.product(range(ell), repeat=3):
                    w = tuple(np.array(v0) + np.array(u))
                    if max(w) >= ice.L:
                        ok = False; break
                    l = 3 * vid[w] + a
                    if not core_link[l]:
                        ok = False; break
                    la.append(l)
                if not ok:
                    break
                idx.append(la)
            if ok:
                pos.append(idx)
        blocks[ell] = np.array(pos)                                    # (npos, 3, ell^3)
    core_links = np.flatnonzero(core_link)
    plaq_depth = np.minimum(np.min(reg.depth[ice.tail[ice.plaq]], axis=1), np.min(reg.depth[ice.head[ice.plaq]], axis=1))
    link_depth = np.minimum(reg.depth[ice.tail], reg.depth[ice.head])
    return dict(pairs=pairs, blocks=blocks, core_links=core_links, plaq_depth=plaq_depth, link_depth=link_depth)


def box_measure(reg, setup):
    ice = reg.ice
    pairs, blocks, core = setup["pairs"], setup["blocks"], setup["core_links"]
    keys = sorted(pairs)
    def meas(S, wn):
        Sf = S.astype(float)
        out = {}
        out["prod"] = np.array([wn @ (Sf[:, pairs[k][0]] * Sf[:, pairs[k][1]]).mean(axis=1) if len(pairs[k][0]) else np.nan for k in keys])
        out["m1"] = wn @ Sf                                               # all links (means), used for connected parts and depth profile
        bl = {}
        for ell, idx in blocks.items():
            if len(idx) == 0:
                continue
            B = Sf[:, idx].sum(axis=3)                                   # (n_w, npos, 3)
            bl[ell] = (np.einsum("i,ipa->pa", wn, B), np.einsum("i,ipa->pa", wn, B * B))
        out["blocks"] = bl
        circ = (Sf[:, ice.plaq] * ice.sign).sum(axis=2)
        out["flip"] = wn @ (np.abs(circ) == 4).astype(float)             # per-plaquette flippable probability
        return out
    return meas, keys


def box_derived(reg, setup, keys, meas_list):
    m1 = np.mean([x["m1"] for x in meas_list], axis=0)
    prod = np.mean([x["prod"] for x in meas_list], axis=0)
    g = {}
    for i, k in enumerate(keys):
        xs, ys = setup["pairs"][k]
        g[k] = prod[i] - (np.mean(m1[xs] * m1[ys]) if len(xs) else np.nan)
    chi = {}
    for ell in setup["blocks"]:
        if len(setup["blocks"][ell]) == 0:
            continue
        e1 = np.mean([x["blocks"][ell][0] for x in meas_list], axis=0)
        e2 = np.mean([x["blocks"][ell][1] for x in meas_list], axis=0)
        chi[ell] = float(np.mean(e2 - e1 ** 2) / ell ** 3)
    flip = np.mean([x["flip"] for x in meas_list], axis=0)
    return dict(g=g, chi=chi, flip=flip, m1=m1)


def section_fluxes(reg, sigma):
    """For each axis a and interior coordinate c < m: the flux of the unrecorded a-links from layer c to c + 1, and the value
    the records fix through the Gauss law summed over the slab of interior vertices with coordinate <= c."""
    ice, m = reg.ice, reg.m
    out = []
    for a in range(3):
        for c in range(1, m):
            inS = reg.vin & (reg.V[:, a] <= c)
            t_in, h_in = inS[ice.tail], inS[ice.head]
            cross = t_in ^ h_in
            sgn = np.where(t_in, 1, -1)
            section = cross & (ice.axis == a) & ~reg.rec & t_in & (reg.V[ice.tail, a] == c)
            others = cross & ~section
            assert reg.rec[others].all()
            out.append((int(sigma[section].sum()), int(-(sgn[others] * sigma[others]).sum())))
    return out


def binned(ml, fn, n=10):
    chunks = np.array_split(np.arange(len(ml)), n)
    vals = np.array([fn([ml[j] for j in c]) for c in chunks], dtype=float)
    return np.asarray(fn(ml), dtype=float), vals.std(axis=0, ddof=1) / np.sqrt(n)


def torus_run(L, n_w, tau, seed_r, init=None):
    ice = Ice(L)
    reg = Region(ice)
    if init is None:
        init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=seed_r, start=ice.sector_state(0), fix_winding=True)
    Eb, ml, info = gfmc_region(reg, ALPHA, init, n_w=n_w, tau_total=tau, dtau=DTAU, r=seed_r, E_ref=-0.29 * ice.np_, lag=LAG,
                               therm_blocks=THERM, measure=torus_measure(reg))
    e0, e0e = stats(Eb[THERM:])
    fn = lambda sub: np.concatenate([[np.mean([x["nf"] for x in sub])],
                                     (lambda d: np.concatenate([d["gL"], d["gT"], d["chi"], d["ST"]]))(torus_derived(L, np.mean([x["P"] for x in sub], axis=0)))])
    v, e = binned(ml, fn)
    return dict(e0=e0 / ice.np_, e0e=e0e / ice.np_, nf=(v[0], e[0]), gL=(v[1:4], e[1:4]), gT=(v[4:7], e[4:7]), chi=(v[7:10], e[7:10]),
                ST=(v[10:12], e[10:12]), init=init, **info)


def box_run(m, frame, n_w, tau, seed_r, dcore=2):
    ice = Ice(m + 2)
    reg = Region(ice, m)
    setup = box_setup(reg, dcore=dcore)
    meas, keys = box_measure(reg, setup)
    Eb, ml, info = gfmc_region(reg, ALPHA, [frame], n_w=n_w, tau_total=tau, dtau=DTAU, r=seed_r, E_ref=-0.29 * reg.n_dyn, lag=LAG,
                               therm_blocks=THERM, measure=meas)
    e0, e0e = stats(Eb[THERM:])
    core_p = reg.dyn & (setup["plaq_depth"] >= dcore)
    def fn(sub):
        d = box_derived(reg, setup, keys, sub)
        return np.concatenate([[np.mean(d["flip"][core_p])], [d["g"][("L", r)] for r in (1, 2, 3)], [d["g"][("T", r)] for r in (1, 2, 3)],
                               [d["chi"].get(ell, np.nan) for ell in (1, 2, 3)]])
    v, e = binned(ml, fn)
    full = box_derived(reg, setup, keys, ml)
    return dict(e0=e0 / reg.n_dyn, e0e=e0e / reg.n_dyn, nf=(v[0], e[0]), gL=(v[1:4], e[1:4]), gT=(v[4:7], e[4:7]), chi=(v[7:10], e[7:10]),
                reg=reg, setup=setup, full=full, frame=frame, **info)


# ------------------------------------------------------------------------------------------------ main
rng = np.random.default_rng(9251)
DTAU, LAG, THERM = 0.05, 40, 160
TAU, NW, SCAN = 24.0, 240, (60, 120, 240, 480)
if DRY:
    TAU, NW, SCAN, LAG, THERM = 3.0, 24, (12, 24), 10, 20

# ---------------------------------------------------------------- 1. the record identities
sp = np.array([[0, 1], [0, 0]], dtype=float)
sm = sp.T
I2 = np.eye(2)
def kron4(ops):
    out = ops[0]
    for o in ops[1:]:
        out = np.kron(out, o)
    return out
U = kron4([sp, sp, sm, sm])
worst = 0.0
for j in range(4):
    for q in (np.diag([1.0, 0.0]), np.diag([0.0, 1.0])):
        Pq = kron4([q if i == j else I2 for i in range(4)])
        worst = max(worst, np.abs(Pq @ U @ Pq).max(), np.abs(Pq @ U.T @ Pq).max())
# an exact flip component of a 3^3 interior bounded by records
ice5 = Ice(5)
frame5 = loop_vmc(ice5, 0.0, sweeps=60, therm=60, r=np.random.default_rng(11))[-1]
reg5 = Region(ice5, 3)
masks5 = [sum(1 << int(l) for l in links) for links in ice5.plaq]
dyn5 = np.flatnonzero(reg5.dyn)
def sig5(c):
    return np.array([1 if (c >> l) & 1 else -1 for l in range(ice5.nl)])
def flip5(s):
    return dyn5[np.abs((s[ice5.plaq[dyn5]] * ice5.sign[dyn5]).sum(axis=1)) == 4]
c0 = int(sum(1 << int(l) for l in np.flatnonzero(frame5 > 0)))
comp, order, q = {c0: 0}, [c0], 0
while q < len(order):
    s = sig5(order[q]); q += 1
    for p in flip5(s):
        c2 = order[q - 1] ^ masks5[p]
        if c2 not in comp:
            comp[c2] = len(order); order.append(c2)
flux_bad = 0
Sg5 = np.array([sig5(c) for c in order], dtype=np.int8)
for s in Sg5:
    flux_bad += sum(a != b for a, b in section_fluxes(reg5, s.astype(int)))
n_sec = len(section_fluxes(reg5, Sg5[0].astype(int)))
check("records remove the ring terms they touch and fix every plane-section flux of the region they bound",
      worst == 0 and flux_bad == 0,
      f"max |P_q U P_q|, |P_q U^dag P_q| over q and the recorded link: {worst:.0e}; exact flip component of a 3^3 interior: {len(order)} states, "
      f"{n_sec} plane sections each, every section flux equal to the value the records fix: {flux_bad == 0}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. the projector with records against exact diagonalization
rows, cols, nfl = [], [], np.zeros(len(order))
for i, s in enumerate(Sg5):
    fp = flip5(s.astype(int)); nfl[i] = len(fp)
    for p in fp:
        rows.append(comp[order[i] ^ masks5[p]]); cols.append(i)
H5 = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(len(order), len(order))).tocsr()
vals5, vecs5 = eigsh(H5, k=1, which="SA")
E0x, pr = float(vals5[0]), np.abs(vecs5[:, 0]) ** 2
setup5 = box_setup(reg5, dcore=1, r_max=2, ells=(1,))
meas5, keys5 = box_measure(reg5, setup5)
m1x = pr @ Sg5.astype(float)
exact = [float(pr @ nfl) / reg5.n_dyn]
for k in (("L", 1), ("T", 1), ("T", 2)):
    xs, ys = setup5["pairs"][k]
    exact.append(float(np.mean(pr @ (Sg5[:, xs].astype(float) * Sg5[:, ys]))) - float(np.mean(m1x[xs] * m1x[ys])))
Eb5, ml5, info5 = gfmc_region(reg5, ALPHA, [frame5], n_w=40 if DRY else 200, tau_total=TAU if DRY else 40.0, dtau=DTAU, r=np.random.default_rng(12),
                              E_ref=E0x, lag=LAG, therm_blocks=THERM if DRY else 240, measure=meas5)
Em5, Ee5 = stats(Eb5[(THERM if DRY else 240):])
def fn5(sub):
    d = box_derived(reg5, setup5, keys5, sub)
    return [float(np.mean(d["flip"][reg5.dyn])), d["g"][("L", 1)], d["g"][("T", 1)], d["g"][("T", 2)]]
v5, e5 = binned(ml5, fn5)
devs = [(Em5 - E0x) / Ee5] + list((v5 - np.array(exact)) / e5)
check("the projector with records against exact diagonalization on the 3^3 interior: energy, flippable density and three connected correlations",
      max(abs(d) for d in devs) <= 3,
      f"component {len(order)} states, E0 {E0x:.5f}, projector {Em5:.4f}+-{Ee5:.4f}; n_f {v5[0]:.4f}+-{e5[0]:.4f} (exact {exact[0]:.4f}); "
      f"g_L(1) {v5[1]:+.4f}+-{e5[1]:.4f} ({exact[1]:+.4f}); g_T(1) {v5[2]:+.4f}+-{e5[2]:.4f} ({exact[2]:+.4f}); g_T(2) {v5[3]:+.4f}+-{e5[3]:.4f} ({exact[3]:+.4f}); "
      f"deviations {', '.join(f'{d:+.1f}' for d in devs)} sigma")

# ---------------------------------------------------------------- 3. the population regulator
spread = []
for L in ((4, 6) if DRY else (4, 6, 8, 12, 16)):
    ice = Ice(L); reg = Region(ice)
    smp = loop_vmc(ice, ALPHA, sweeps=max(20, 1600 // L ** 2 * 4), therm=40, r=rng, start=ice.sector_state(0), fix_winding=True)
    EL = []
    for s in smp:
        C = ice.circ(s); P = np.flatnonzero(np.abs(C[:-1]) == 4)
        _, dN = reg.deltas(s, C, P)
        EL.append(-np.exp(ALPHA * dN).sum())
    sd = float(np.std(EL, ddof=1))
    spread.append((L, sd / np.sqrt(ice.np_), sd * DTAU, float(np.exp(-(sd * DTAU) ** 2))))
L8 = 4 if DRY else 8
scan = {}
init8 = None
for n_w in SCAN:
    res = torus_run(L8, n_w, TAU, rng, init=init8)
    init8 = res["init"]
    scan[n_w] = res
pred8 = [p for p in spread if p[0] == L8][0][3]
x = 1 / np.array(SCAN, dtype=float)
def fit(key, idx=None):
    y = np.array([scan[n][key] if idx is None else scan[n][key][0][idx] for n in SCAN])
    ye = np.array([scan[n][key + "e"] if idx is None else scan[n][key][1][idx] for n in SCAN])
    c, cov = np.polyfit(x, y, 1, w=1 / ye, cov="unscaled") if len(SCAN) > 2 else (np.polyfit(x, y, 1), np.zeros((2, 2)))
    return c[1], float(np.sqrt(cov[1, 1])), c[0]
fe = fit("e0")
fs1, fs2, fgt = fit("ST", 0), fit("ST", 1), fit("gT", 0)
ess_ok = all(abs(scan[n]["ess"] - pred8) <= 0.1 for n in SCAN)
check("the population regulator: the walker weights spread as the square root of the system size, and at fixed torus size the energy and the "
      "structure factors move with the walker number (reported; fits linear in 1/n_w)", ess_ok and np.isfinite(fe[0]),
      "spread: " + "; ".join(f"{L}^3 std(E_L)/sqrt(N_p) {a:.3f}, log-weight spread per block {b:.2f}, predicted ESS {c:.2f}" for L, a, b, c in spread)
      + f" || {L8}^3 scan: " + "; ".join(f"n_w {n}: e0 {scan[n]['e0']:.5f}+-{scan[n]['e0e']:.5f}, S_T(k1) {scan[n]['ST'][0][0]:.3f}+-{scan[n]['ST'][1][0]:.3f}, "
                                        f"S_T(k2) {scan[n]['ST'][0][1]:.3f}+-{scan[n]['ST'][1][1]:.3f}, g_T(1) {scan[n]['gT'][0][0]:+.4f}, ESS {scan[n]['ess']:.2f}, "
                                        f"ancestors {scan[n]['ndist']:.2f}" for n in SCAN)
      + f" || n_w -> infinity: e0 {fe[0]:.5f}+-{fe[1]:.5f} (slope {fe[2]:+.3f}), S_T(k1) {fs1[0]:.3f}+-{fs1[1]:.3f} (slope {fs1[2]:+.1f}), "
        f"S_T(k2) {fs2[0]:.3f}+-{fs2[1]:.3f} (slope {fs2[2]:+.1f}), g_T(1) {fgt[0]:+.4f}+-{fgt[1]:.4f}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. the boundary regulator
sizes = (4,) if DRY else (6, 8)
tor = {L8: scan[NW if NW in scan else SCAN[-1]]}
for L in sizes:
    if L not in tor:
        tor[L] = torus_run(L, NW, TAU, rng)
boxes = {}
for m in sizes:
    ice_f = Ice(m + 2)
    fr = loop_vmc(ice_f, 0.0, sweeps=60, therm=60, r=rng, start=ice_f.sector_state(0), fix_winding=True)[-1]
    boxes[(m, "uniform")] = box_run(m, fr, NW, TAU, rng)
mc = sizes[-1]
boxes[(mc, "canonical")] = box_run(mc, Ice(mc + 2).sector_state(0), NW, TAU, rng)
flux_ok = True
for key, b in boxes.items():
    flux_ok &= all(x == y for x, y in section_fluxes(b["reg"], b["frame"].astype(int)))
def row(name, r, torus=None):
    s = f"{name}: e0 {r['e0']:.4f}, n_f {r['nf'][0]:.4f}+-{r['nf'][1]:.4f}, g_L(1..3) " + "/".join(f"{v:+.4f}" for v in r["gL"][0]) \
        + f" (+-{r['gL'][1][0]:.4f}), g_T(1..3) " + "/".join(f"{v:+.4f}" for v in r["gT"][0]) + f" (+-{r['gT'][1][0]:.4f}), chi(1..3) " \
        + "/".join(f"{v:.3f}" for v in r["chi"][0]) + f" (+-{np.nanmax(r['chi'][1]):.3f}), ESS {r['ess']:.2f}"
    if torus is not None:
        z = lambda a, i: (r[a][0][i] - torus[a][0][i]) / np.hypot(r[a][1][i], torus[a][1][i])
        s += f"; vs torus: n_f {(r['nf'][0] - torus['nf'][0]) / np.hypot(r['nf'][1], torus['nf'][1]):+.1f}, g_L(1) {z('gL', 0):+.1f}, g_T(1) {z('gT', 0):+.1f}, " \
             f"g_T(2) {z('gT', 1):+.1f}, chi(2) {z('chi', 1):+.1f} sigma"
    return s
prec_ok = all(r["gT"][1][0] < 0.01 for r in list(boxes.values()) + list(tor.values()))
check("the boundary regulator: record-bounded boxes (core at depth >= 2) against tori of the same size, real-space correlations, block variances "
      "and flippable density (reported), every box's plane-section fluxes fixed by its records", flux_ok and prec_ok,
      " || ".join([row(f"torus {L}^3", tor[L]) for L in sorted(tor) if L in sizes]
                  + [row(f"box {m} {kind}", b, tor[m]) for (m, kind), b in boxes.items()]) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. the depth profile of the largest box
b = boxes[(mc, "uniform")]
reg, setup, full = b["reg"], b["setup"], b["full"]
prof = []
for d in range(1, mc // 2 + 1):
    pm = reg.dyn & (setup["plaq_depth"] == d)
    lm = (~reg.rec) & (setup["link_depth"] == d)
    prof.append((d, float(np.mean(full["flip"][pm])), float(np.sqrt(np.mean(full["m1"][lm] ** 2)))))
check("the depth profile of the largest box: flippable density and the rms field the records induce, by depth from the recorded boundary "
      "(reported, against the torus flippable density)", all(np.isfinite(p[1]) for p in prof),
      "; ".join(f"depth {d}: n_f {nf:.4f}, rms <sigma> {mf:.3f}" for d, nf, mf in prof) + f"; torus {mc}^3 n_f {tor[mc]['nf'][0]:.4f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
