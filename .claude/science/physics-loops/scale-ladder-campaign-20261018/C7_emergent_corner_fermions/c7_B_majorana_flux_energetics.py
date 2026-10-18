#!/usr/bin/env python3
"""C7 part B: which Z2 flux sector does a Kitaev-type (Majorana, half filling) corner-graph model select?

In the Gamma-matrix model of part A the exact ground state in a static gauge sector u is the free
Majorana ground state of H = sum_e J_e u_e (i c_I c_J); its energy is the sum of the negative
eigenvalues of the purely imaginary hopping matrix (c7_common docstring).  Gauge-invariantly the
octant triangles carry flux +-pi/2 (odd loops, Yao-Kivelson), the 4-cycles (squares, plaquettes,
edge tubes) 0 or pi.  The corner model's pattern (standard flux pi on every face) is therefore NOT
available; its closest analogue is square = plaquette = tube = pi with triangles +-pi/2.

Uniform patterns: 'sq tri pl tu' with sq, pl, tu in {0,1} (1 = pi) and tri in
  c+ / c- : all 8 octant triangles outward flux +pi/2 / -pi/2 (O-symmetric, breaks T and mirrors),
  s+ / s- : outward flux alternating with the octant parity s0 s1 s2 (staggered).
The pairs (c+, c-) and (s+, s-) are complex conjugates; since h* = -h for Majorana hopping their
spectra are identical (exact), so 16 distinct uniform patterns are compared.

Parts
 B0  Bloch 2^3 supercell vs real-space L = 4 spectrum (random gauge field, imaginary amplitudes).
 B1  exact identities checked: spec(h) = -spec(h) (Majorana PH), conjugate-pattern degeneracy.
 B2  16 uniform patterns, |t1| = 1, |t2| in {0.2, 0.5, 1, 2}; ranks; K-grid convergence 6 vs 8 vs 10.
 B3  single-edge-flip search over all period-2 sectors: is the best uniform pattern a local minimum;
     greedy descent from random period-2 starts.
 B4  comparison: the real-hopping (cross-flavour parton) model at its natural mu = 0 filling.
"""
import itertools, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c7_common import Lattice, per_site, majorana_amp, real_amp, uniform_targets, flux_summary, TYPES

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(7)
L2 = Lattice(2)
L4 = Lattice(4)
Z = np.zeros(L2.nE, np.uint8)

# ------------------------------------------------------------------ B0
print("B0: Bloch supercell (2^3 cell) vs real-space L = 4 torus, purely imaginary amplitudes")
u2 = rng.integers(0, 2, L2.nE).astype(np.uint8)
desc2 = {}
for k, (v, c, disp, c2) in enumerate(L2.G.edesc):
    desc2[(v, c, disp, c2)] = (k, 1)
    w = tuple((a + b) % 2 for a, b in zip(v, disp))
    desc2[(w, c2, tuple(-x for x in disp), c)] = (k, -1)
u4 = np.zeros(L4.nE, np.uint8); s4 = np.ones(L4.nE)
for k4, (v, c, disp, c2) in enumerate(L4.G.edesc):
    k2, s = desc2[(tuple(x % 2 for x in v), c, disp, c2)]
    u4[k4] = u2[k2]; s4[k4] = s          # orientation of the L=4 edge relative to the L=2 edge
a2 = majorana_amp(L2, u2, 1.0, 0.3)
a4 = majorana_amp(L4, u4, 1.0, 0.3) * s4   # imaginary amplitude is odd under reversal
e_b = L2.spectrum(a2, 2)
e_r = L4.spectrum(a4, 1)
check("Bloch supercell spectrum equals real-space L = 4 spectrum (random u, imaginary hopping)",
      np.allclose(e_b, e_r, atol=1e-9), f"max dev {np.max(np.abs(e_b-e_r)):.1e}")

# ------------------------------------------------------------------ uniform gauges
TRI = ('c+', 'c-', 's+', 's-')
PATS = [(sq, tr, pl, tu) for sq in (0, 1) for tr in TRI for pl in (0, 1) for tu in (0, 1)]
lab = lambda P: f"{P[0]}{P[1]}{P[2]}{P[3]}"
base = majorana_amp(L2, Z, 1.0, 1.0)
gauges = {}
okg = True
for P in PATS:
    u = L2.solve_u(base, uniform_targets(L2, *P, 'maj'), rng=rng)
    okg &= u is not None
    if u is not None:
        ph = L2.face_phases(majorana_amp(L2, u, 1.0, 0.7))
        okg &= np.allclose(np.exp(1j * ph), np.exp(1j * uniform_targets(L2, *P, 'maj')), atol=1e-9)
    gauges[P] = u
check("all 32 uniform Majorana patterns (16 x conjugate pairs) exist on the 2^3 supercell; fluxes re-measured",
      okg)

# ------------------------------------------------------------------ B1
print("\nB1: exact identities")
ev = L2.spectrum(majorana_amp(L2, u2, 1.0, 0.3), 4)
check("Majorana particle-hole symmetry: the full spectrum is symmetric under E -> -E (h* = -h)",
      np.allclose(ev, -ev[::-1], atol=1e-10))
dev = 0.0
for P in PATS:
    if P[1][1] == '+':
        Q = (P[0], P[1][0] + '-', P[2], P[3])
        dev = max(dev, np.max(np.abs(L2.spectrum(majorana_amp(L2, gauges[P], 1, .4), 3)
                                     - L2.spectrum(majorana_amp(L2, gauges[Q], 1, .4), 3))))
check("conjugate patterns (tri c+ vs c-, s+ vs s-) have identical spectra", dev < 1e-9, f"max dev {dev:.1e}")

# ------------------------------------------------------------------ B2
UP = [P for P in PATS if P[1][1] == '+']
E2 = {}
for t2 in (0.2, 0.5, 1.0, 2.0):
    E = {P: per_site(L2.spectrum(majorana_amp(L2, gauges[P], 1.0, t2), 6), 6) for P in UP}
    E2[t2] = E
    order = sorted(UP, key=lambda P: E[P])
    print(f"\nB2: Majorana half filling, |t1| = 1, |t2| = {t2}, 6^3 K-grid on the 2^3 cell (energy per site; "
          f"one Majorana per corner, E0 = sum of negative eigenvalues of the imaginary hopping matrix)")
    for r, P in enumerate(order):
        print(f"   {r+1:2d}. {lab(P):>7}  E = {E[P]:10.5f}   (+{E[P]-E[order[0]]:.5f})")
    rc = order.index((1, 'c+', 1, 1)) + 1
    print(f"   corner analogue 1c11 (square = plaquette = tube = pi, chiral triangles) rank {rc}/16;"
          f" winner {lab(order[0])}, margin to second {E[order[1]]-E[order[0]]:.5f}")
print(f"  t = {time.time()-T0:.1f}s")

print("\n  K-grid convergence of the ranking (N_K = 6, 8, 10) for the top three at each t2:")
conv_ok = True
for t2 in (0.2, 0.5, 1.0, 2.0):
    top = sorted(UP, key=lambda P: E2[t2][P])[:3]
    rows = []
    for nk in (6, 8, 10):
        rows.append([per_site(L2.spectrum(majorana_amp(L2, gauges[P], 1.0, t2), nk), 6) for P in top])
    rows = np.array(rows)
    order_same = all(np.argsort(r).tolist() == [0, 1, 2] for r in rows)
    d = np.abs(np.diff(rows - rows[:, :1], axis=0)).max()
    conv_ok &= order_same
    print(f"   t2={t2}: {[lab(P) for P in top]}  E(nk=10) = {np.round(rows[-1], 5).tolist()}; "
          f"order stable: {order_same}; max change of differences {d:.1e}")
check("top-3 ordering of uniform patterns stable under N_K = 6, 8, 10 for all four t2", conv_ok)

# ------------------------------------------------------------------ B3: period-2 local search
NKS = 4


def energy(u, t2, nk=NKS):
    return per_site(L2.spectrum(majorana_amp(L2, u, 1.0, t2), nk), 6)


def flip_scan(u, t2):
    e0 = energy(u, t2)
    dE = np.empty(L2.nE)
    for k in range(L2.nE):
        u[k] ^= 1
        dE[k] = energy(u, t2) - e0
        u[k] ^= 1
    return e0, dE


def greedy(u, t2, max_sweeps=6):
    u = u.copy(); e = energy(u, t2); sweeps = 0; improved = True
    while improved and sweeps < max_sweeps:
        improved = False; sweeps += 1
        for k in rng.permutation(L2.nE):
            u[k] ^= 1
            e2 = energy(u, t2)
            if e2 < e - 1e-10:
                e = e2; improved = True
            else:
                u[k] ^= 1
    return u, e, sweeps, (not improved)


print(f"\nB3: single-edge flips over period-2 sectors (2^3 cell, 288 edges, {NKS}^3 K-grid); t = {time.time()-T0:.1f}s")
B3 = {}
for t2 in (0.2, 1.0):
    best = min(UP, key=lambda P: E2[t2][P])
    ub = gauges[best].copy()
    e0, dE = flip_scan(ub, t2)
    nneg = int((dE < -1e-10).sum())
    kmin = int(np.argmin(dE))
    print(f"  t2={t2}: best uniform {lab(best)} E = {e0:.5f}; single flips: min dE = {dE.min():+.5f} "
          f"({'onsite' if L2.onsite[kmin] else 'link'}), #dE<0: {nneg}/288; "
          f"min dE onsite {dE[L2.onsite].min():+.5f}, link {dE[~L2.onsite].min():+.5f}; t = {time.time()-T0:.1f}s")
    res = []
    for trial in range(3):
        u0 = rng.integers(0, 2, L2.nE).astype(np.uint8)
        ur, er, sw, conv = greedy(u0, t2)
        fs = flux_summary(L2, majorana_amp(L2, ur, 1.0, t2))
        res.append((er, ur, fs, conv))
        print(f"    random start {trial}: E = {er:.5f} after {sw} sweeps (converged: {conv}); fluxes {fs}; t = {time.time()-T0:.1f}s")
    B3[t2] = (best, e0, nneg, res)

for t2, (best, e0, nneg, res) in B3.items():
    ebest_rand = min(r[0] for r in res)
    print(f"FINDING B3 t2={t2}: uniform winner {lab(best)} is {'a' if nneg == 0 else 'NOT a'} single-flip local minimum"
          f" among period-2 sectors; best random-start greedy {ebest_rand:.5f} vs {e0:.5f}"
          f" ({'uniform winner lower or equal' if ebest_rand >= e0 - 1e-6 else 'NON-UNIFORM LOWER'})")
    if ebest_rand < e0 + 1e-6:
        er, ur, fs, _ = min(res, key=lambda r: r[0])
        e8 = per_site(L2.spectrum(majorana_amp(L2, ur, 1.0, t2), 8), 6)
        e8u = per_site(L2.spectrum(majorana_amp(L2, gauges[best], 1.0, t2), 8), 6)
        print(f"   recheck on 8^3 grid: greedy {e8:.5f}, uniform winner {e8u:.5f}")
        np.save(os.path.join(HERE, f"c7_B3_u_t2_{t2}.npy"), ur)

# ------------------------------------------------------------------ B4: real hopping at mu = 0
print(f"\nB4: comparison, cross-flavour parton = real hopping (C6's problem) at its natural mu = 0 filling; t = {time.time()-T0:.1f}s")
baseR = real_amp(L2, Z, 1.0, 1.0)
for t2 in (0.2, 1.0):
    ER = {}
    for F in itertools.product((0, 1), repeat=4):
        u = L2.solve_u(baseR, uniform_targets(L2, *F, 'real'))
        ev = L2.spectrum(real_amp(L2, u, 1.0, t2), 6)
        nsite = len(ev) / 12
        ER[F] = (ev[ev < 0].sum() / nsite, (ev < 0).sum() / nsite)
    order = sorted(ER, key=lambda F: ER[F][0])
    lr = lambda F: ''.join(map(str, F))
    print(f"  t2={t2}: best {lr(order[0])} E = {ER[order[0]][0]:.4f} (nu = {ER[order[0]][1]:.3f}); second {lr(order[1])}"
          f" {ER[order[1]][0]:.4f}; corner 1111 rank {order.index((1,1,1,1))+1}/16 (E = {ER[(1,1,1,1)][0]:.4f},"
          f" nu = {ER[(1,1,1,1)][1]:.3f})")

print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
