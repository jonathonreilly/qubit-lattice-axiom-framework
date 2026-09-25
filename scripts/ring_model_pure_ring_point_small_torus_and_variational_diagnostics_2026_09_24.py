#!/usr/bin/env python3
"""Finite flip spectra and a sampled variational family.
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
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24.md']

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    # Labels describe finite diagnostics; limits in the source note govern interpretation.
    label = "finite diagnostic: " + label
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(1924)


# ------------------------------------------------ cubic ice on a coarse L^3 torus: links, vertices, plaquettes
class Ice:
    def __init__(self, L):
        self.L = L
        self.nv = L ** 3
        self.nl = 3 * L ** 3
        self.vid = {v: i for i, v in enumerate(itertools.product(range(L), repeat=3))}
        self.verts = list(itertools.product(range(L), repeat=3))
        # link (v, a) from v to v + e_a; sigma = +1 means the arrow points from v to v + e_a
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                l = 3 * self.vid[v] + a
                w = list(v)
                w[a] = (w[a] + 1) % L
                self.tail[l], self.head[l] = self.vid[v], self.vid[tuple(w)]
        # incident links per vertex with the sign s such that sigma * s = +1 means "points away from the vertex"
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        # plaquettes (v, a, b): links (v,a) +, (v+e_a, b) +, (v+e_b, a) -, (v, b) -; circulation = sum of signed sigma
        self.plaq, self.plaq_sign = [], []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % L
                vb[b] = (vb[b] + 1) % L
                links = [3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b]
                self.plaq.append(links)
                self.plaq_sign.append([1, 1, -1, -1])
        self.plaq = np.array(self.plaq)
        self.plaq_sign = np.array(self.plaq_sign)
        self.np_ = len(self.plaq)
        self.plaq_of_link = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                self.plaq_of_link[l].append(p)
        self.plaq_pos = np.array([v for v in self.verts for _ in range(3)], dtype=float)

    def out_count(self, sigma):
        """Number of outgoing arrows at each vertex (ice: 3)."""
        out = np.zeros(self.nv, dtype=int)
        np.add.at(out, self.tail, (sigma == 1).astype(int))
        np.add.at(out, self.head, (sigma == -1).astype(int))
        return out

    def flippable(self, sigma):
        return np.abs((sigma[self.plaq] * self.plaq_sign).sum(axis=1)) == 4


# ------------------------------------------------ 1. the fine Z_4^3 torus exactly
ice2 = Ice(2)
states = []
for chunk in range(16):                                   # 2^24 configurations in chunks of 2^20
    idx = np.arange(chunk * 2 ** 20, (chunk + 1) * 2 ** 20, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(24)) & 1) * 2 - 1  # sigma in {-1, +1}
    out = np.zeros((len(idx), ice2.nv), dtype=int)
    for l in range(24):
        out[:, ice2.tail[l]] += (bits[:, l] == 1)
        out[:, ice2.head[l]] += (bits[:, l] == -1)
    states.append(bits[np.all(out == 3, axis=1)])
states = np.vstack(states).astype(np.int8)
n_ice = len(states)
code = {tuple(s): i for i, s in enumerate(states)}
flip_rows, flip_cols = [], []
nflip = np.zeros(n_ice, dtype=int)
for i, s in enumerate(states):
    fl = ice2.flippable(s)
    nflip[i] = fl.sum()
    for p in np.flatnonzero(fl):
        t = s.copy()
        t[ice2.plaq[p]] *= -1
        flip_rows.append(i)
        flip_cols.append(code[tuple(t)])
F = csr_matrix((np.ones(len(flip_rows)), (flip_rows, flip_cols)), shape=(n_ice, n_ice))
ncomp, labels = connected_components(F, directed=False)
sizes = np.bincount(labels)
big = np.flatnonzero(labels == sizes.argmax())
Fb = F[big][:, big].toarray()
Nb = nflip[big].astype(float)
rows1, fid_rk, e0s = [], [], []
uniform = np.ones(len(big)) / np.sqrt(len(big))
for V in (0.0, 0.25, 0.5, 0.75, 1.0):
    H = -Fb + V * np.diag(Nb)
    ev, vec = np.linalg.eigh(H)
    gs = vec[:, 0]
    prob = gs ** 2
    tv = 0.5 * np.abs(prob - 1 / len(big)).sum()
    rows1.append((V, ev[0] / ice2.np_, ev[1] - ev[0], float(np.dot(gs, uniform) ** 2), float(prob @ Nb), tv))
    e0s.append(ev[0])
# the global ground state at V = 0 over all classes
E_all = min((np.linalg.eigvalsh((-F[np.flatnonzero(labels == c)][:, np.flatnonzero(labels == c)]).toarray())[0], sizes[c])
            for c in range(ncomp) if sizes[c] > 1)
check("the fine Z_4^3 torus: 9600 ice states, 937 flip classes, largest 864; ground-state diagnostics along V/g",
      n_ice == 9600 and ncomp == 937 and sizes.max() == 864 and abs(rows1[-1][1]) < 1e-12 and rows1[-1][3] > 1 - 1e-12
      and E_all[1] == 864 and abs(E_all[0] - e0s[0]) < 1e-12,
      f"{n_ice} states, {ncomp} classes, largest {sizes.max()}; global V = 0 ground state in the class of size {E_all[1]}; "
      + "; ".join(f"V/g = {V}: E0/plaquette {e:.4f}, gap {gp:.4f}, RK fidelity {fd:.3f}, <N_flip> {nf:.2f}, TV from uniform {tv:.3f}"
                  for V, e, gp, fd, nf, tv in rows1))

# ------------------------------------------------ 2. the Jastrow family on the same class, exactly
def jastrow_exact(alpha, V=0.0):
    w = np.exp(alpha * Nb)
    psi = w / np.linalg.norm(w)
    H = -Fb + V * np.diag(Nb)
    return float(psi @ H @ psi), psi


alphas = np.linspace(0, 1.0, 101)
curve = np.array([jastrow_exact(a)[0] for a in alphas])
a_star = alphas[curve.argmin()]
E_var, psi_var = jastrow_exact(a_star)
ev0, vec0 = np.linalg.eigh(-Fb)
fid_var = float(np.dot(psi_var, vec0[:, 0]) ** 2)
check("the Jastrow family on the largest class at V = 0: grid-minimizing alpha, variational energy against the exact one, fidelity",
      0 < a_star < 1 and E_var >= ev0[0] - 1e-12 and fid_var > 0.9,
      f"alpha* = {a_star:.2f}; E_var/plaquette {E_var / ice2.np_:.4f} vs exact {ev0[0] / ice2.np_:.4f} "
      f"(relative excess {(E_var - ev0[0]) / abs(ev0[0]):.4f}); fidelity with the exact ground state {fid_var:.4f}; "
      f"uniform state energy {curve[0] / ice2.np_:.4f}")


# ------------------------------------------------ 3. loop-update variational Monte Carlo at V = 0 on coarse tori
def vmc(L, alpha, sweeps, therm, seed):
    ice = Ice(L)
    r = np.random.default_rng(seed)
    # start from a uniformly polarized ice state (all arrows along +x, +y, +z is 3 out / 3 in)
    sigma = np.ones(ice.nl, dtype=int)
    assert np.all(ice.out_count(sigma) == 3)
    fl = ice.flippable(sigma)
    nflip = int(fl.sum())
    inc, plaq, ps, pol = ice.inc, ice.plaq, ice.plaq_sign, ice.plaq_of_link
    accepted, tried = 0, 0
    energies, densities, sq = [], [], []
    qs = [(0, 0, 0), (np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi)]
    phases = [np.exp(1j * (ice.plaq_pos @ np.array(q))) for q in qs]
    loops_per_sweep = max(1, ice.nl // 20)
    for sweep in range(therm + sweeps):
        for _ in range(loops_per_sweep):
            v = r.integers(ice.nv)
            path_v, path_l, seen = [v], [], {v: 0}
            while True:
                outs = [l for (l, s) in inc[v] if sigma[l] * s == 1]
                l = outs[r.integers(3)]
                v = ice.head[l] if ice.tail[l] == v else ice.tail[l]
                path_l.append(l)
                if v in seen:
                    cyc = path_l[seen[v]:]
                    break
                seen[v] = len(path_v)
                path_v.append(v)
            affected = sorted({p for l in cyc for p in pol[l]})
            before = int((np.abs((sigma[plaq[affected]] * ps[affected]).sum(axis=1)) == 4).sum())
            sigma[cyc] *= -1
            after = int((np.abs((sigma[plaq[affected]] * ps[affected]).sum(axis=1)) == 4).sum())
            tried += 1
            if r.random() < np.exp(2 * alpha * (after - before)):
                accepted += 1
                nflip += after - before
            else:
                sigma[cyc] *= -1
        if sweep >= therm and sweep % 2 == 0:
            fl = ice.flippable(sigma)
            # kinetic estimator: sum over flippable p of exp(alpha (N(c_p) - N(c)))
            kin = 0.0
            for p in np.flatnonzero(fl):
                aff = sorted({q for l in plaq[p] for q in pol[l]})
                b = int((np.abs((sigma[plaq[aff]] * ps[aff]).sum(axis=1)) == 4).sum())
                sigma[plaq[p]] *= -1
                a_ = int((np.abs((sigma[plaq[aff]] * ps[aff]).sum(axis=1)) == 4).sum())
                sigma[plaq[p]] *= -1
                kin += np.exp(alpha * (a_ - b))
            energies.append(-kin / ice.np_)
            densities.append(fl.mean())
            f = fl.astype(float) - fl.mean()
            sq.append([abs(np.dot(f, ph)) ** 2 / ice.np_ for ph in phases])
    energies, sq = np.array(energies), np.array(sq)
    nb = 10
    bins = energies[:len(energies) // nb * nb].reshape(nb, -1).mean(axis=1)
    return dict(E=energies.mean(), dE=bins.std(ddof=1) / np.sqrt(nb), dens=float(np.mean(densities)),
                sq=sq.mean(axis=0), acc=accepted / tried)


t3 = time.time()
alpha_grid = [0.0, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.6]
res4 = {a: vmc(4, a, sweeps=2400, therm=300, seed=10 + i) for i, a in enumerate(alpha_grid)}
a4 = min(res4, key=lambda a: res4[a]["E"])
res6 = {a: vmc(6, a, sweeps=900, therm=150, seed=50 + i) for i, a in enumerate((0.0, 0.2, a4, 0.4))}
a6 = min(res6, key=lambda a: res6[a]["E"])
res8 = {a: vmc(8, a, sweeps=400, therm=80, seed=90 + i) for i, a in enumerate((0.0, a4))}
sq_pi = {L: (r[0.0]["sq"][3], r[a4]["sq"][3]) for L, r in ((4, res4), (6, res6), (8, res8))}
ok3 = all(v["dE"] < 0.01 for v in res4.values()) and all(v["dE"] < 0.02 for v in list(res6.values()) + list(res8.values())) \
    and 0 < a4 < 0.6 and abs(res4[0.0]["E"] + res4[0.0]["dens"]) < 3 * res4[0.0]["dE"] + 3e-3 \
    and abs(res6[0.0]["E"] + res6[0.0]["dens"]) < 3 * res6[0.0]["dE"] + 3e-3
check("loop-update variational Monte Carlo at V = 0 on the 4^3, 6^3 and 8^3 coarse tori: energies against alpha, the sampled-grid minimum, and flippable-plaquette structure factors",
      ok3,
      f"4^3: " + ", ".join(f"alpha {a}: E {v['E']:.4f} +- {v['dE']:.4f}" for a, v in res4.items())
      + f"; optimum alpha {a4}; 6^3: " + ", ".join(f"alpha {a}: E {v['E']:.4f} +- {v['dE']:.4f}" for a, v in res6.items())
      + f" (optimum {a6}); 8^3: " + ", ".join(f"alpha {a}: E {v['E']:.4f} +- {v['dE']:.4f}" for a, v in res8.items())
      + f"; flippable density at alpha 0 / optimum: 4^3 {res4[0.0]['dens']:.3f} / {res4[a4]['dens']:.3f}, 8^3 {res8[0.0]['dens']:.3f} / {res8[a4]['dens']:.3f}; "
      f"configuration-centered S(q)/N_p at (0,0,0), (pi,0,0), (pi,pi,0), (pi,pi,pi) on 8^3: alpha 0 {np.round(res8[0.0]['sq'], 3).tolist()}, "
      f"optimum {np.round(res8[a4]['sq'], 3).tolist()}; S(pi,pi,pi)/N_p at alpha 0 / optimum by size: "
      + ", ".join(f"{L}^3 {a0:.3f} / {a1:.3f}" for L, (a0, a1) in sq_pi.items())
      + f"; loop acceptance at the sampled-grid minimum {res4[a4]['acc']:.2f}; Monte Carlo time {time.time() - t3:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
