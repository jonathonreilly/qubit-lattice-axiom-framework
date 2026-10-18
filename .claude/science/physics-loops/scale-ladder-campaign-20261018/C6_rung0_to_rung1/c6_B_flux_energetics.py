#!/usr/bin/env python3
"""C6 part B: does the energy of a hop-only qubit Hamiltonian select the corner model's flux?

In the BKSF code every loop operator commutes with every encoded hop, so a qubit Hamiltonian
built only from encoded hops, H_q = sum_e tau_e hop_e (+ the chiral triangle terms), is block
diagonal over flux sectors; its ground state at fixed particle number lies in the sector that
minimizes the free-fermion ground energy (the Kitaev / Lieb mechanism).  The minimum over
sectors does not depend on the hop-sign dictionary (a sign change only relabels sectors), so the
selected holonomy pattern is a convention-free function of |t1|, |t2|, lambda and the filling nu.

Conventions.  'Standard' holonomy: H = -sum tau c^dag c, a face has flux pi when the product of
tau around it is negative.  The corner model (repo: t1 = -1, u-flux square = plaquette = tube = pi,
triangle = 0) is flux pi through EVERY face in the standard convention ('1111' below).

Parts
 B0  implementation cross-check: Bloch supercell vs direct real-space diagonalization.
 B1  exact expectation: diamagnetic inequality (Perron-Frobenius) -> the flux-free pattern has the
     lowest one-particle energy, strictly.
 B2  ground energy per site E(nu) for all 16 uniform patterns, |t1| = 1, |t2| in {0.2, 1}, nu = 1..11;
     which pattern wins at each filling; is the corner pattern ever the minimum?
 B3  local search over all period-2 flux sectors (single-edge u flips, 288 edges per 2^3 cell)
     from the corner pattern and from random starts, at selected fillings: is the corner pattern a
     local minimum among period-2 sectors?
 B4  with the chiral triangle term (repo convention t1 = -1, lambda = -0.5, t2 = 0.2): the same
     uniform comparison at the node filling nu = 1.
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c6_corner_graph import CornerGraph, gf2_solve, neg

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


TYPES = ('square', 'triangle', 'plaquette', 'tube')
T0 = time.time()


class Model:
    def __init__(self, Ls):
        self.G = G = CornerGraph(Ls)
        self.Ls = Ls
        self.n = G.nV
        self.I = np.array([e[0] for e in G.edges]); self.J = np.array([e[1] for e in G.edges])
        self.kind = np.array([0 if e[2] == 'onsite' else 1 for e in G.edges])
        self.W = np.array([e[3] for e in G.edges], float)
        self.fl = G.face_list()
        # oriented triangle hops (q -> r), each an on-site edge
        self.tri = []
        for v in G.sites:
            for s in itertools.product((1, -1), repeat=3):
                x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
                cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
                if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
                for a in range(3):
                    q, r = (v, cy[a]), (v, cy[(a + 1) % 3])
                    e = G.edge_between(q, (0, 0, 0), cy[(a + 1) % 3])
                    self.tri.append((G.vid[q], G.vid[r], e))

    def gauge(self, F):
        return gf2_solve([f for _, f in self.fl], [F[k] for k, _ in self.fl], self.G.nE)

    def fluxes(self, u):
        out = {k: [] for k in TYPES}
        for k, f in self.fl:
            out[k].append(int(u[f].sum() % 2))
        return {k: float(np.mean(v)) for k, v in out.items()}

    def blochH(self, u, Ks, t1, t2, lam):
        n = self.n
        amp = -np.where(self.kind == 0, t1, t2) * (-1.0) ** u            # c^dag_j c_i amplitude, i -> j
        ph = np.exp(1j * Ks @ self.W.T)                                   # (nK, nE)
        H = np.zeros((len(Ks), n, n), complex)
        A = amp[None, :] * ph
        np.add.at(H, (slice(None), self.J, self.I), A)
        np.add.at(H, (slice(None), self.I, self.J), np.conj(A))
        if lam:
            for q, r, e in self.tri:
                a = 1j * lam * (-1.0) ** u[e]
                H[:, r, q] += a; H[:, q, r] += np.conj(a)
        return H

    def spectrum(self, u, nk, t1, t2, lam=0.0):
        g = 2 * np.pi * np.arange(nk) / nk
        Ks = np.array(list(itertools.product(g, repeat=3)))
        return np.sort(np.linalg.eigvalsh(self.blochH(u, Ks, t1, t2, lam)).ravel())

    def energies(self, ev, nus):
        nsites = len(ev) / 12.0
        return {nu: float(ev[:int(round(nu * nsites))].sum() / nsites) for nu in nus}


# ------------------------------------------------------------------ B0
print("B0: Bloch supercell (2^3 cell, K in {0,pi}^3) vs real-space L = 4 torus with the periodically extended gauge field")
M2 = Model(2)
M4 = Model(4)
rng = np.random.default_rng(11)
u2 = rng.integers(0, 2, M2.G.nE).astype(np.uint8)
# extend u2 to L = 4 by matching edge descriptors mod 2
desc2 = {}
for k, (v, c, disp, c2) in enumerate(M2.G.edesc):
    desc2[(v, c, disp, c2)] = k
    w = tuple((a + b) % 2 for a, b in zip(v, disp))
    desc2[(w, c2, tuple(-x for x in disp), c)] = k
u4 = np.array([u2[desc2[(tuple(x % 2 for x in v), c, disp, c2)]] for (v, c, disp, c2) in M4.G.edesc], np.uint8)
ok = True
for lam in (0.0, -0.5):
    e_b = M2.spectrum(u2, 2, 1.0, 0.3, lam)
    e_r = M4.spectrum(u4, 1, 1.0, 0.3, lam)
    ok &= np.allclose(e_b, e_r, atol=1e-9)
check("Bloch supercell spectrum equals direct L = 4 real-space spectrum (random gauge field, lambda = 0 and -0.5)", ok)

# ------------------------------------------------------------------ B1, B2
NK = 6
NUS = list(range(1, 12))
PATS = list(itertools.product((0, 1), repeat=4))
gauges = {}
for Fb in PATS:
    u = M2.gauge(dict(zip(TYPES, Fb)))
    assert u is not None, Fb
    assert all(abs(M2.fluxes(u)[k] - Fb[i]) < 1e-12 for i, k in enumerate(TYPES))
    gauges[Fb] = u
print(f"\n  gauge fields for all 16 uniform patterns found on the 2^3 supercell (fluxes re-measured); t = {time.time()-T0:.1f}s")

lab = lambda Fb: ''.join(map(str, Fb))
results = {}
for t2 in (0.2, 1.0):
    E = {}; E1 = {}
    for Fb in PATS:
        ev = M2.spectrum(gauges[Fb], NK, 1.0, t2)
        E[Fb] = M2.energies(ev, NUS); E1[Fb] = ev[0]
    results[t2] = E
    if t2 == 0.2:
        others = [E1[F] for F in PATS if F != (0, 0, 0, 0)]
        check("B1 diamagnetic inequality: the flux-free pattern 0000 has the strictly lowest one-particle energy (t2 = 0.2)",
              E1[(0, 0, 0, 0)] < min(others) - 1e-9, f"E1(0000) = {E1[(0,0,0,0)]:.6f}, next = {min(others):.6f}")
    print(f"\nB2: ground energy per site, standard convention (H = -sum |t| u c^dag c), |t1| = 1, |t2| = {t2}, {NK}^3 K-grid on the 2^3 cell")
    print("   nu  " + "  ".join(f"{lab(F):>8}" for F in PATS))
    for nu in NUS:
        print(f"   {nu:2d}  " + "  ".join(f"{E[F][nu]:8.4f}" for F in PATS))
    print("   winners (pattern = square triangle plaquette tube; 1 = pi):")
    for nu in NUS:
        order = sorted(PATS, key=lambda F: E[F][nu])
        rank_corner = order.index((1, 1, 1, 1)) + 1
        print(f"   nu = {nu:2d}: best {lab(order[0])} ({E[order[0]][nu]:.4f}), second {lab(order[1])} ({E[order[1]][nu]:.4f});"
              f" corner 1111 rank {rank_corner}/16, excess {E[(1,1,1,1)][nu]-E[order[0]][nu]:+.4f}")

# grid convergence for the winners
print("\n  K-grid convergence (N_K = 6 vs 8) of the energy differences at t2 = 0.2:")
maxdev = 0.0
for nu in NUS:
    pair = sorted(PATS, key=lambda F: results[0.2][F][nu])[:2] + [(1, 1, 1, 1)]
    d6 = [results[0.2][F][nu] for F in pair]
    d8 = [M2.energies(M2.spectrum(gauges[F], 8, 1.0, 0.2), [nu])[nu] for F in pair]
    dev = max(abs((d8[i] - d8[0]) - (d6[i] - d6[0])) for i in range(1, 3))
    gap6 = d6[1] - d6[0]
    maxdev = max(maxdev, dev)
    print(f"   nu={nu:2d}: winner {lab(pair[0])}; margin to second {gap6:.4f}; change of differences {dev:.1e}")
check("K-grid changes of the reported differences are below 5e-3 per site", maxdev < 5e-3, f"max {maxdev:.1e}")

# ------------------------------------------------------------------ B3: local search over period-2 sectors
print(f"\nB3: greedy single-edge flips over all period-2 sectors (2^3 cell, 288 edges), {4}^3 K-grid; t = {time.time()-T0:.1f}s")


def energy(u, nu, nk=4, t1=1.0, t2=0.2, lam=0.0):
    ev = M2.spectrum(u, nk, t1, t2, lam)
    return M2.energies(ev, [nu])[nu]


def greedy(u, nu, max_sweeps=4, **kw):
    u = u.copy(); e = energy(u, nu, **kw); improved = True; sweeps = 0
    while improved and sweeps < max_sweeps:
        improved = False; sweeps += 1
        for k in rng.permutation(M2.G.nE):
            u[k] ^= 1
            e2 = energy(u, nu, **kw)
            if e2 < e - 1e-9:
                e = e2; improved = True
            else:
                u[k] ^= 1
    return u, e, sweeps


search = {}
for nu in (1, 6):
    ucorner = gauges[(1, 1, 1, 1)]
    e_corner = energy(ucorner, nu)
    best_uni = min(PATS, key=lambda F: energy(gauges[F], nu))
    uc, ec, sw = greedy(ucorner, nu, max_sweeps=1)
    print(f"  nu={nu}: corner 1111 E = {e_corner:.4f}; one sweep of single flips from it -> E = {ec:.4f} (fluxes {M2.fluxes(uc)}); "
          f"best uniform {lab(best_uni)} E = {energy(gauges[best_uni], nu):.4f}")
    search[nu] = (e_corner, ec)
    rs = []
    for trial in range(2):
        u0 = rng.integers(0, 2, M2.G.nE).astype(np.uint8)
        ur, er, sw = greedy(u0, nu, max_sweeps=3)
        rs.append((er, M2.fluxes(ur)))
        print(f"    random start {trial}: E = {er:.4f} after {sw} sweeps, fluxes {M2.fluxes(ur)}; t = {time.time()-T0:.1f}s")
    search[nu] += (rs,)
for nu, (e0, e1, rs) in search.items():
    print(f"FINDING B3 nu={nu}: corner sector {'is NOT' if e1 < e0 - 1e-6 else 'is'} a single-flip local minimum among period-2 sectors"
          f" ({e0:.4f} -> {e1:.4f}); best random-start greedy result {min(r[0] for r in rs):.4f}")

# ------------------------------------------------------------------ B4: with the chiral triangle term, repo convention
print(f"\nB4: repo convention t1 = -1, t2 = 0.2, chiral lambda = -0.5 (the long-wavelength note's family); node filling nu = 1; t = {time.time()-T0:.1f}s")
E4 = {}
for Fb in PATS:
    ev = M2.spectrum(gauges[Fb], NK, -1.0, 0.2, -0.5)
    E4[Fb] = M2.energies(ev, NUS)
for nu in (1, 2, 6):
    order = sorted(PATS, key=lambda F: E4[F][nu])
    print(f"   nu={nu}: best u-pattern {lab(order[0])} ({E4[order[0]][nu]:.4f}); corner 1011 rank {order.index((1,0,1,1))+1}/16"
          f" (E = {E4[(1,0,1,1)][nu]:.4f}, excess {E4[(1,0,1,1)][nu]-E4[order[0]][nu]:+.4f})")

print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
