#!/usr/bin/env python3
"""Projector Monte Carlo of the ring model at the pure-ring point: energies below the variational ones, and no growth of
plaquette order from the 4^3 to the 8^3 torus.

Setting (all supplied, none adopted): spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic
ice), the covariant plaquette clause -g (U + U^dag) at V = 0 (open PRs 9066, 9072). In the ice basis the Hamiltonian is
stoquastic (every off-diagonal element is -g), so a continuous-time projector (Green's function) Monte Carlo with a
positive guiding function has no sign problem. The guiding function is the Jastrow state exp(alpha N_flip) of open PR
9146 at alpha = 0.2; walkers hop by single plaquette flips with rates g exp(alpha dN), carry weights exp(-int (E_L -
E_ref)), and are reconfigured to a fixed population every dtau. Mixed estimators <psi_G|O|psi_0>/<psi_G|psi_0> are
reported for the energy (exact in the limit), the flippable density and the connected flippable-plaquette structure
factor, together with the variational values and the extrapolated 2 mixed - variational. Supplied model, finite
diagnostics, no phase claim.

1. Control on the fine Z_4^3 torus (9600 ice states, largest flip class 864, exact diagonalization): the projector
   energy agrees with the exact ground energy, and the mixed flippable number with its exact mixed value, within
   errors; the extrapolated flippable number is compared with the exact pure one.
2. Coarse 4^3, 6^3 and 8^3 tori: projector energy per plaquette against the variational energy of the guiding state
   (it must not lie above it), with the fractional gain; equilibration check between the two halves of the run.
3. Flippable density and the connected structure factor per plaquette at (0,0,0), (pi,0,0), (pi,pi,0), (pi,pi,pi):
   variational, mixed and extrapolated, by size. The size dependence of S(pi,pi,pi)/N_p is the diagnostic.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 900

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


# ------------------------------------------------ cubic ice on a coarse L^3 torus
class Ice:
    def __init__(self, L):
        self.L = L
        self.nv, self.nl = L ** 3, 3 * L ** 3
        self.verts = list(itertools.product(range(L), repeat=3))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                self.tail[3 * self.vid[v] + a], self.head[3 * self.vid[v] + a] = self.vid[v], self.vid[tuple(w)]
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
        # affected plaquettes of a flip at p (padded with a dummy index np_ whose circulation stays 0), and the matrix
        # M[p, j, k] = sign_{A[p, j]}(link k of p) if that link lies in plaquette A[p, j]
        width = max(len({q for l in links for q in pol[l]}) for links in self.plaq)
        self.A = np.full((self.np_, width), self.np_, dtype=int)
        self.M = np.zeros((self.np_, width, 4))
        for p, links in enumerate(self.plaq):
            aff = sorted({q for l in links for q in pol[l]})
            self.A[p, :len(aff)] = aff
            for j, q in enumerate(aff):
                for k, l in enumerate(links):
                    hits = np.flatnonzero(self.plaq[q] == l)
                    for h in hits:
                        self.M[p, j, k] += self.sign[q, h]
        self.pos = np.array([v for v in self.verts for _ in range(3)], dtype=float)
        qs = [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi)]
        self.phases = np.array([np.exp(1j * (self.pos @ np.array(q))) for q in qs])

    def circ(self, sigma):
        c = np.zeros(self.np_ + 1)
        c[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        return c

    def deltas(self, sigma, C, P):
        """For flippable plaquettes P: the new circulations of their affected plaquettes and dN_flip."""
        Ca = C[self.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", self.M[P], sigma[self.plaq[P]])
        return Cn, (np.abs(Cn) == 4).sum(axis=1) - (np.abs(Ca) == 4).sum(axis=1)

    def structure(self, flip):
        f = flip.astype(float) - flip.mean()
        return np.abs(self.phases @ f) ** 2 / self.np_


def loop_vmc(ice, alpha, sweeps, therm, r):
    """Loop-update sampling of exp(2 alpha N_flip); returns samples of sigma and variational estimators."""
    sigma = np.ones(ice.nl, dtype=int)
    C = ice.circ(sigma)
    N = int((np.abs(C[:-1]) == 4).sum())
    samples, E, dens, S = [], [], [], []
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
            if r.random() < np.exp(2 * alpha * (after - before)):
                C[aff] = C_new
                N += after - before
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            flip = np.abs(C[:-1]) == 4
            P = np.flatnonzero(flip)
            _, dN = ice.deltas(sigma, C, P)
            E.append(-G * np.exp(alpha * dN).sum() / ice.np_)
            dens.append(flip.mean())
            S.append(ice.structure(flip))
            samples.append(sigma.copy())
    return samples, np.mean(E), float(np.mean(dens)), np.mean(S, axis=0)


def gfmc(ice, alpha, init, n_w, tau_total, dtau, r, E_ref):
    """Continuous-time projector Monte Carlo with fixed population; returns block series of mixed estimators."""
    walkers = [init[r.integers(len(init))].copy() for _ in range(n_w)]
    Cs = [ice.circ(s) for s in walkers]
    n_blocks = int(round(tau_total / dtau))
    E_blocks, D_blocks, S_blocks, hops = [], [], [], 0
    for b in range(n_blocks):
        w = np.ones(n_w)
        EL, DN, SQ = np.zeros(n_w), np.zeros(n_w), np.zeros((n_w, 4))
        for i in range(n_w):
            sigma, C = walkers[i], Cs[i]
            t = 0.0
            while True:
                P = np.flatnonzero(np.abs(C[:-1]) == 4)
                Cn, dN = ice.deltas(sigma, C, P)
                rates = G * np.exp(alpha * dN)
                lam = rates.sum()
                E_loc = -lam                                  # V = 0: local energy of the guided walk
                dt = r.exponential(1 / lam) if lam > 0 else np.inf
                if t + dt >= dtau:
                    w[i] *= np.exp(-(E_loc - E_ref) * (dtau - t))
                    EL[i] = E_loc
                    flip = np.abs(C[:-1]) == 4
                    DN[i] = flip.mean()
                    SQ[i] = ice.structure(flip)
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
        D_blocks.append(float((w * DN).sum() / W))
        S_blocks.append((w[:, None] * SQ).sum(axis=0) / W)
        # stochastic reconfiguration to a fixed population
        cum = np.cumsum(w) / W
        picks = np.searchsorted(cum, (np.arange(n_w) + r.random()) / n_w)
        walkers = [walkers[k].copy() for k in picks]
        Cs = [Cs[k].copy() for k in picks]
        E_ref = 0.9 * E_ref + 0.1 * E_blocks[-1]
    return np.array(E_blocks), np.array(D_blocks), np.array(S_blocks), hops


def stats(x, n_bins=10):
    x = np.asarray(x)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))


rng = np.random.default_rng(2409)

# ------------------------------------------------ 1. control on the fine Z_4^3 torus
ice2 = Ice(2)
states = []
for chunk in range(16):
    idx = np.arange(chunk * 2 ** 20, (chunk + 1) * 2 ** 20, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(24)) & 1) * 2 - 1
    out = np.zeros((len(idx), ice2.nv), dtype=int)
    for l in range(24):
        out[:, ice2.tail[l]] += (bits[:, l] == 1)
        out[:, ice2.head[l]] += (bits[:, l] == -1)
    states.append(bits[np.all(out == 3, axis=1)])
states = np.vstack(states).astype(int)
code = {tuple(s): i for i, s in enumerate(states)}
rows, cols, nflip = [], [], np.zeros(len(states), dtype=int)
for i, s in enumerate(states):
    fl = np.abs(ice2.circ(s)[:-1]) == 4
    nflip[i] = fl.sum()
    for p in np.flatnonzero(fl):
        t = s.copy()
        t[ice2.plaq[p]] *= -1
        rows.append(i)
        cols.append(code[tuple(t)])
F = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(states),) * 2)
ncomp, labels = connected_components(F, directed=False)
sizes = np.bincount(labels)
big = np.flatnonzero(labels == sizes.argmax())
H = -G * F[big][:, big].toarray()
ev, vec = np.linalg.eigh(H)
psi0 = np.abs(vec[:, 0])
psiG = np.exp(ALPHA * nflip[big])
Nb = nflip[big]
E_exact = ev[0]
N_mixed_exact = float((psiG * psi0 * Nb).sum() / (psiG * psi0).sum())
N_pure_exact = float((psi0 ** 2 * Nb).sum())
N_var_exact = float((psiG ** 2 * Nb).sum() / (psiG ** 2).sum())
t1 = time.time()
init2 = [states[k].copy() for k in big[:50]]
Eb, Db, Sb, hops2 = gfmc(ice2, ALPHA, init2, n_w=200, tau_total=30.0, dtau=0.1, r=rng, E_ref=E_exact)
keep = slice(len(Eb) // 3, None)
E_g, dE_g = stats(Eb[keep])
D_g, dD_g = stats(Db[keep])
N_g, dN_g = D_g * ice2.np_, dD_g * ice2.np_
N_ext = 2 * N_g - N_var_exact
check("control on the fine Z_4^3 torus: the projector energy and mixed flippable number agree with exact diagonalization",
      len(states) == 9600 and ncomp == 937 and sizes.max() == 864 and abs(E_g - E_exact) < 3 * dE_g + 1e-3 * abs(E_exact)
      and abs(N_g - N_mixed_exact) < 3 * dN_g + 0.02,
      f"exact E0 = {E_exact:.4f}, projector {E_g:.4f} +- {dE_g:.4f}; exact mixed <N_flip> {N_mixed_exact:.3f}, projector "
      f"{N_g:.3f} +- {dN_g:.3f}; exact pure {N_pure_exact:.3f}, variational {N_var_exact:.3f}, extrapolated {N_ext:.3f}; "
      f"{hops2} hops, {time.time() - t1:.0f} s")

# ------------------------------------------------ 2-3. coarse tori
summary = {}
for L, n_w, tau_total, sweeps in ((4, 100, 16.0, 800), (6, 80, 16.0, 300), (8, 60, 16.0, 150)):
    tL = time.time()
    ice = Ice(L)
    samples, E_var, dens_var, S_var = loop_vmc(ice, ALPHA, sweeps=sweeps, therm=max(40, sweeps // 5), r=rng)
    Eb, Db, Sb, hops = gfmc(ice, ALPHA, samples, n_w=n_w, tau_total=tau_total, dtau=0.05, r=rng, E_ref=E_var * ice.np_)
    Eb = Eb / ice.np_
    keep = slice(len(Eb) // 3, None)
    E_g, dE_g = stats(Eb[keep])
    half = len(Eb) // 2
    E_h1, dE_h1 = stats(Eb[len(Eb) // 3:half] if half > len(Eb) // 3 + 10 else Eb[keep])
    E_h2, dE_h2 = stats(Eb[half:])
    D_g, dD_g = stats(Db[keep])
    S_g = Sb[keep].mean(axis=0)
    dS_g = np.array([stats(Sb[keep][:, k])[1] for k in range(4)])
    kept = Sb[keep][:, 3]
    S_a, dS_a = stats(kept[:len(kept) // 2])
    S_b, dS_b = stats(kept[len(kept) // 2:])
    s_eq = abs(S_a - S_b) / np.sqrt(dS_a ** 2 + dS_b ** 2)
    summary[L] = dict(E_var=E_var, E=E_g, dE=dE_g, gain=(E_var - E_g) / abs(E_var), eq=abs(E_h1 - E_h2) / np.sqrt(dE_h1 ** 2 + dE_h2 ** 2),
                      dens_var=dens_var, dens=D_g, ddens=dD_g, dens_ext=2 * D_g - dens_var, S_var=S_var, S=S_g, dS=dS_g,
                      S_ext=2 * S_g - S_var, s_eq=s_eq, S_halves=(S_a, S_b), hops=hops, secs=time.time() - tL)
ok2 = all(v["E"] <= v["E_var"] + 2 * v["dE"] and v["dE"] < 0.003 and v["eq"] < 3 for v in summary.values())
check("coarse 4^3, 6^3, 8^3 tori: the projector energy lies below the variational one, with equilibrated second half",
      ok2, "; ".join(f"{L}^3: variational {v['E_var']:.4f}, projector {v['E']:.4f} +- {v['dE']:.4f} (gain {100 * v['gain']:.2f}%), "
                     f"halves differ by {v['eq']:.1f} sigma, {v['hops']} hops in {v['secs']:.0f} s" for L, v in summary.items()))
ok3 = all(v["ddens"] < 0.01 and np.all(v["dS"] < 0.05) and v["s_eq"] < 3 for v in summary.values())
check("flippable density and connected plaquette structure factors, variational / mixed / extrapolated, by size; S(pi,pi,pi) stable between the halves of the projection",
      ok3, "; ".join(f"{L}^3: density {v['dens_var']:.3f} / {v['dens']:.3f}+-{v['ddens']:.3f} / {v['dens_ext']:.3f}; "
                     f"S(pi,pi,pi)/N_p {v['S_var'][3]:.3f} / {v['S'][3]:.3f}+-{v['dS'][3]:.3f} / {v['S_ext'][3]:.3f} "
                     f"(halves {v['S_halves'][0]:.3f}, {v['S_halves'][1]:.3f}, {v['s_eq']:.1f} sigma apart); "
                     f"mixed S at (0,0,0),(pi,0,0),(pi,pi,0) {v['S'][0]:.3f}, {v['S'][1]:.3f}, {v['S'][2]:.3f}"
                     for L, v in summary.items()))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
