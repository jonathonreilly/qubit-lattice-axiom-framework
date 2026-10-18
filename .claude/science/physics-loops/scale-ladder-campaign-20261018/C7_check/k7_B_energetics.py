#!/usr/bin/env python3
"""C7_check B: Majorana half-filling energetics of uniform flux sectors, independently.

B0  Bloch (L = 2 supercell) vs real-space L = 4 spectrum for a random Majorana gauge field (normalisation and
    phases of my Bloch code); Majorana E -> -E symmetry; Majorana ground energy = sum of negative eigenvalues
    checked against a JW many-body diagonalisation of a 6-Majorana ring.
B1  the 16 uniform patterns (sq, tri in {c,s}, pl, tu) at t2 = 0.2, 0.5, 1, 2 on the 2^3 supercell with
    N_K = 6, 8, 12, 16 and a half-shifted N_K = 9 grid; a second, independently drawn gauge (random pure gauge +
    flipped noncontractible holonomies) as a control on the finite-grid error.
B2  wider uniform family: every translation-invariant octant-triangle assignment (+-pi/2 on each of the 8
    triangles, all 2^8 tried; existence decided by GF(2)) x 8 four-cycle bits, at N_K = 6.
B3  period-1 (one-site gauge, 36 independent u's, 12 bands) greedy single-flip search from many random starts.
"""
import itertools, os, sys, time
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_geom import Lat, kgrid, eigs, solve_gauge, maj_targets, maj_amp, e_half, gf2, TYPES

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(99)
L1, L2, L4 = Lat(1), Lat(2), Lat(4)

# ---------------------------------------------------------------- B0
print("B0: normalisation and Bloch checks")
x2 = rng.integers(0, 2, L2.nE).astype(np.uint8)
# lift to L = 4: each L=4 edge has the same type and site mod 2 as an L=2 edge
x4 = np.array([x2[L2.sidx[tuple(c % 2 for c in L4.esite[e])] * 36 + L4.typ[e]] for e in range(L4.nE)], np.uint8)
a2 = maj_amp(L2, x2, 1.0, 0.3); a4 = maj_amp(L4, x4, 1.0, 0.3)
eb = np.sort(eigs(L2, a2, kgrid(2)).ravel()); er = np.sort(np.linalg.eigvalsh(L4.realspace(a4)))
check("Bloch 2^3 supercell on a 2^3 K-grid = real-space L = 4 spectrum (random imaginary gauge field)",
      np.allclose(eb, er, atol=1e-9), f"max dev {np.max(np.abs(eb-er)):.1e}")
check("Majorana hopping spectrum symmetric under E -> -E", np.allclose(eb, -eb[::-1], atol=1e-10))
# many-body check: H = sum_e J u (i c_I c_J) on a 6-ring of Majoranas
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1]).astype(complex)
def kr(ms):
    o = np.eye(1, dtype=complex)
    for m in ms: o = np.kron(o, m)
    return o
gm = [kr([Z] * (m // 2) + [X if m % 2 == 0 else Y] + [np.eye(2)] * (3 - m // 2 - 1)) for m in range(6)]
Jr = rng.uniform(0.5, 1.5, 6); ur = rng.choice([-1, 1], 6)
Hmb = sum(Jr[i] * ur[i] * 1j * gm[i] @ gm[(i + 1) % 6] for i in range(6))
h = np.zeros((6, 6), complex)
for i in range(6):
    j = (i + 1) % 6
    h[j, i] += 1j * Jr[i] * ur[i] * (-1); h[i, j] += np.conj(h[j, i])   # any sign: spectrum is symmetric
e1 = np.linalg.eigvalsh(Hmb)[0]; ev = np.linalg.eigvalsh(h)
check("Majorana many-body ground energy (JW, 6 Majoranas) = sum of negative eigenvalues of the one-body i J u matrix",
      abs(e1 - ev[ev < 0].sum()) < 1e-10, f"{e1:.8f} vs {ev[ev<0].sum():.8f}")

# ---------------------------------------------------------------- uniform patterns
PATS = [(sq, tr, pl, tu) for sq in (0, 1) for tr in ('c+', 's+') for pl in (0, 1) for tu in (0, 1)]
lab = lambda P: f"{P[0]}{P[1][0]}{P[2]}{P[3]}"
base2 = maj_amp(L2, np.zeros(L2.nE, np.uint8), 1, 1)
G2 = {}
okg = True
for P in PATS:
    x = solve_gauge(L2, base2, maj_targets(L2, *P))
    okg &= x is not None
    G2[P] = x
    if x is not None:
        ph = L2.fluxes(maj_amp(L2, x, 1, 0.37))
        okg &= np.allclose(np.exp(1j * ph), np.exp(1j * maj_targets(L2, *P)), atol=1e-9)
check("all 16 uniform patterns are realised on the 2^3 supercell (fluxes re-measured at t2 = 0.37)", okg)
# second gauge: random pure gauge plus flipped holonomy planes (all edges crossing x = 1|0 etc.)
G2b = {}
for P in PATS:
    g = rng.integers(0, 2, L2.n)
    x = (G2[P] + g[L2.I] + g[L2.J]) % 2
    for ax in range(3):
        if rng.integers(0, 2):
            x = (x + (L2.W[:, ax] != 0)) % 2          # flip every edge winding across the boundary along ax
    ph = L2.fluxes(maj_amp(L2, x.astype(np.uint8), 1, 0.37))
    assert np.allclose(np.exp(1j * ph), np.exp(1j * maj_targets(L2, *P)), atol=1e-9)
    G2b[P] = x.astype(np.uint8)
c1 = maj_targets(L2, 1, 'c+', 1, 1); c2 = maj_targets(L2, 1, 'c-', 1, 1)
xa = G2[(1, 'c+', 1, 1)]; xb = solve_gauge(L2, base2, c2)
dc = np.max(np.abs(np.sort(eigs(L2, maj_amp(L2, xa, 1, .4), kgrid(4)).ravel()) -
                   np.sort(eigs(L2, maj_amp(L2, xb, 1, .4), kgrid(4)).ravel())))
check("conjugate chirality 1c-11 has the same spectrum as 1c+11 (control on the 'c+' vs 'c-' reduction)", dc < 1e-9,
      f"{dc:.1e}")

ERES = {}
print(f"\nB1: 16 uniform patterns, E per site (Majorana half filling, |t1| = 1); t = {time.time()-T0:.1f}s")
for t2 in (0.2, 0.5, 1.0, 2.0):
    grids = [('6', kgrid(6)), ('8', kgrid(8)), ('12', kgrid(12))] + ([('16', kgrid(16))] if t2 in (0.2, 1.0) else []) \
            + [('9s', kgrid(9, (0.5, 0.5, 0.5)))]
    E = {}
    for P in PATS:
        a = maj_amp(L2, G2[P], 1, t2)
        E[P] = {g: e_half(eigs(L2, a, K)) for g, K in grids}
        ab = maj_amp(L2, G2b[P], 1, t2)
        E[P]['8b'] = e_half(eigs(L2, ab, kgrid(8)))
    ERES[t2] = E
    gl = [g for g, _ in grids][-2] if t2 in (0.2, 1.0) else '12'
    order = sorted(PATS, key=lambda P: E[P][gl])
    print(f"  t2 = {t2}: ranking on N_K = {gl}")
    for r, P in enumerate(order):
        e = E[P]
        spread = max(e.values()) - min(e.values())
        print(f"   {r+1:2d}. {lab(P)}  E = {e[gl]:.6f}  (+{e[gl]-E[order[0]][gl]:.6f})  spread over grids/gauges {spread:.1e}")
    margins = {g: E[order[1]][g] - E[order[0]][g] for g in E[order[0]]}
    print(f"   winner {lab(order[0])}, runner-up {lab(order[1])}; margin per grid: "
          + ", ".join(f"{g}: {m:.6f}" for g, m in margins.items()))
    stable = all(min(PATS, key=lambda P: E[P][g]) == order[0] for g in E[order[0]])
    ERES[t2]['_order'] = order
    if t2 in (0.2, 1.0):
        check(f"t2 = {t2}: 1c+11 is the lowest of the 16 on every grid (N_K = 6, 8, 12, 16, shifted 9) and in the second gauge",
              stable and order[0] == (1, 'c+', 1, 1), f"min margin {min(margins.values()):.6f}")
    else:
        print(f"   (t2 = {t2}: winner stable on all grids: {stable}, winner {lab(order[0])})")
print(f"  t = {time.time()-T0:.1f}s")

# ---------------------------------------------------------------- B2: all translation-invariant triangle assignments
print(f"\nB2: wider uniform family: 2^8 triangle assignments x 8 four-cycle bits (N_K = 6, 2^3 supercell)")
TRI_LABS = [lab_ for k, _, (v, lab_) in L2.faces if k == 'triangle' and v == (0, 0, 0)]
best = {}
nexist = 0
for t2 in (0.2, 1.0):
    E0 = ERES[t2][(1, 'c+', 1, 1)]['6']
    lower = []; cnt = 0
    for tri in itertools.product((1, -1), repeat=8):
        if tri[0] == -1:
            continue                         # global conjugation (h -> h*, same spectrum)
        tmap = dict(zip(TRI_LABS, tri))
        for sq, pl, tu in itertools.product((0, 1), repeat=3):
            tg = np.zeros(len(L2.faces))
            for f, (k, _, (v, lab_)) in enumerate(L2.faces):
                tg[f] = {'square': np.pi * sq, 'plaquette': np.pi * pl, 'tube': np.pi * tu}.get(k, 0)
                if k == 'triangle':
                    tg[f] = tmap[lab_] * np.pi / 2
            x = solve_gauge(L2, base2, tg)
            if x is None:
                continue
            cnt += 1
            e = e_half(eigs(L2, maj_amp(L2, x, 1, t2), kgrid(6)))
            if e < E0 - 1e-9:
                lower.append((e, tri, (sq, pl, tu)))
    nexist = cnt
    print(f"  t2 = {t2}: {cnt} consistent patterns (of 128 x 8 up to conjugation); below 1c+11 ({E0:.6f}): {len(lower)}"
          + (f"; best {min(lower)}" if lower else ''))
    best[t2] = lower
    check(f"t2 = {t2}: no translation-invariant pattern with uniform 4-cycles and any +-pi/2 triangle assignment beats 1c+11",
          not lower)
print(f"  t = {time.time()-T0:.1f}s")

# ---------------------------------------------------------------- B3: period-1 greedy search over all 36 u's
print(f"\nB3: period-1 sectors (12 bands, 36 independent u's): greedy single-flip descent from random starts (N_K = 8)")
K8 = kgrid(8)


def E1(x, t2):
    return e_half(np.linalg.eigvalsh(L1.bloch(maj_amp(L1, x, 1, t2), K8)))


base1 = maj_amp(L1, np.zeros(L1.nE, np.uint8), 1, 1)
x1c = solve_gauge(L1, base1, maj_targets(L1, 1, 'c+', 1, 1))
print(f"  1c+11 period-1 gauge exists: {x1c is not None}")
for t2 in (0.2, 1.0):
    eref = E1(x1c, t2)
    found = []
    for st in range(150):
        x = rng.integers(0, 2, L1.nE).astype(np.uint8)
        e = E1(x, t2); improved = True
        while improved:
            improved = False
            for k in rng.permutation(L1.nE):
                x[k] ^= 1
                e2 = E1(x, t2)
                if e2 < e - 1e-10:
                    e = e2; improved = True
                else:
                    x[k] ^= 1
        found.append((e, x.copy()))
    es = np.array([f[0] for f in found])
    eb_, xb_ = min(found, key=lambda f: f[0])
    ph = L1.fluxes(maj_amp(L1, xb_, 1, t2))
    tgt = maj_targets(L1, 1, 'c+', 1, 1); tgt2 = maj_targets(L1, 1, 'c-', 1, 1)
    same = np.allclose(np.exp(1j * ph), np.exp(1j * tgt), atol=1e-8) or np.allclose(np.exp(1j * ph), np.exp(1j * tgt2), atol=1e-8)
    print(f"  t2 = {t2}: 1c+11 E = {eref:.6f}; 150 greedy runs: best {eb_:.6f}, fraction reaching 1c+-11 energy "
          f"{np.mean(np.abs(es - eref) < 1e-8):.2f}; best sector has 1c+-11 fluxes: {same}; distinct minima "
          f"{len(np.unique(np.round(es, 6)))}")
    check(f"t2 = {t2}: no period-1 sector found below 1c+11 (150 random greedy descents)", eb_ > eref - 1e-8,
          f"best - ref = {eb_-eref:+.2e}")
print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
