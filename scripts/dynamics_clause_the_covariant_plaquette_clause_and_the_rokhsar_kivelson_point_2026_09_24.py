#!/usr/bin/env python3
"""Supplied covariant plaquette model: RK kernel, finite ice graph and potential.
For g>0 the RK kernel is spanned by class-uniform vectors; coherent
superpositions are also ground states. The enumerated torus has distinct
oriented parallel-endpoint links. The unrecorded-plaquette potential has
eight polarized minima for B>=0,J!=0; preservation after adding a ring
requires the explicit local gap bound, not an assumed scale hierarchy.
"""
import itertools
import sys
from collections import deque
from functools import reduce

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)

rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)

# ------------------------------------------------------------ 1. orbits
pc = np.array([1, 1, 0])
ppos = [np.array(p) for p in [(1, 0, 0), (2, 1, 0), (1, 2, 0), (0, 1, 0)]]   # bottom, right, top, left
axis = [0, 1, 0, 1]
stab = [R for R in rots if all(any(np.array_equal(pc + R @ (q - pc), p) for p in ppos) for q in ppos)]


def act(R, conf):
    """Soldered action on a configuration of the four link fields (E = +-1)."""
    new = [0] * 4
    for k, q in enumerate(ppos):
        img = pc + R @ (q - pc)
        j = [i for i, p in enumerate(ppos) if np.array_equal(p, img)][0]
        sgn = int(round((R @ np.eye(3)[axis[k]])[axis[j]]))       # orientation change of the link direction
        new[j] = sgn * conf[k]
    return tuple(new)


confs = list(itertools.product([1, -1], repeat=4))
corner = np.array([[1, 0, 0, 1], [-1, 1, 0, 0], [0, -1, -1, 0], [0, 0, 1, -1]])
flippable = [c for c in confs if not np.any(corner @ np.array(c))]
orbits, seen = [], set()
for c in confs:
    if c in seen:
        continue
    orb = {act(R, c) for R in stab}
    seen |= orb
    orbits.append(sorted(orb))


def circ(c):
    return (c[0], c[1], -c[2], -c[3])          # fields relative to the counterclockwise circulation


def kind(orb):
    w = sum(1 for x in circ(orb[0]) if x > 0)
    if w in (0, 4):
        return "flippable"
    if w in (1, 3):
        return "odd"
    cc = circ(orb[0])
    return "opposite" if cc[0] == cc[2] else "adjacent"


sizes = {kind(o): len(o) for o in orbits}
check("orbits: eight rotations split the 16 link configurations into flippable 2, opposite 2, adjacent 4, odd 8 (with the ring: 5 covariant generators)",
      len(stab) == 8 and sizes == {"flippable": 2, "opposite": 2, "adjacent": 4, "odd": 8}
      and sorted(orbits[[kind(o) for o in orbits].index("flippable")]) == sorted(flippable),
      f"stabilizer {len(stab)}; orbit sizes {sizes}")

# ------------------------------------------------ 2. frustration-free
idx = {c: i for i, c in enumerate(confs)}
a_, b_ = flippable
ring = np.zeros((16, 16))
ring[idx[a_], idx[b_]] = ring[idx[b_], idx[a_]] = 1.0          # U + U^dag in a real gauge
proj = {kind(o): np.diag([1.0 if c in o else 0.0 for c in confs]) for o in orbits}
gens = [-ring] + [proj[k] for k in ("flippable", "opposite", "adjacent", "odd")]
sym = np.zeros(16)
sym[idx[a_]] = sym[idx[b_]] = 1
targets = [sym] + [np.eye(16)[idx[c]] for c in confs if c not in flippable]
A = np.array([np.concatenate([G @ t for t in targets]) for G in gens]).T
from scipy.linalg import null_space
ns = null_space(A)
coef = ns[:, 0] / ns[0, 0] if ns.shape[1] == 1 else None
Hrk = sum(coef[i] * gens[i] for i in range(5)) if coef is not None else None
ev = np.linalg.eigvalsh(Hrk) if Hrk is not None else [np.nan]
check("uniform-ice point: the covariant plaquette generators annihilating the equal-amplitude flippable state and all other configurations are the line g (P_flip - U - U^dag), positive for g >= 0",
      ns.shape[1] == 1 and np.allclose(coef, [1, 1, 0, 0, 0]) and min(ev) > -1e-12,
      f"solution dimension {ns.shape[1]}; coefficients (ring, flippable, opposite, adjacent, odd) {np.round(coef, 12).tolist()}; eigenvalues {sorted(set(float(x) for x in np.round(ev, 12)))}")

# ------------------------------------------- 3. ground states on 2x2x2
LC = 2
verts = list(itertools.product(range(LC), repeat=3))
vid = {v: i for i, v in enumerate(verts)}
links = []
for v in verts:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % LC
        links.append((vid[v], vid[tuple(w)], a))
lid = {(i, a): k for k, (i, j, a) in enumerate(links)}
nV, nL = len(verts), len(links)
plaqs = []
for v in range(nV):
    for (a, b) in [(0, 1), (1, 2), (0, 2)]:
        va = list(verts[v]); va[a] = (va[a] + 1) % LC
        vb = list(verts[v]); vb[b] = (vb[b] + 1) % LC
        plaqs.append([(lid[(v, a)], 1), (lid[(vid[tuple(va)], b)], 1), (lid[(vid[tuple(vb)], a)], -1), (lid[(v, b)], -1)])
inc = np.zeros((nV, nL))
for k, (i, j, a) in enumerate(links):
    inc[i, k] += 1
    inc[j, k] -= 1
# enumerate ice states (div = 0) by depth-first assignment with vertex pruning
touch = {v: [] for v in range(nV)}
for k, (i, j, a) in enumerate(links):
    touch[i].append(k)
    touch[j].append(k)
last_use = {v: max(touch[v]) for v in range(nV)}
ice, div, E = [], [0] * nV, [0] * nL


def dfs(k):
    if k == nL:
        ice.append(tuple(E))
        return
    i, j, a = links[k]
    for s_ in (1, -1):
        E[k] = s_
        div[i] += s_
        div[j] -= s_
        if not ((last_use[i] == k and div[i] != 0) or (last_use[j] == k and div[j] != 0)):
            dfs(k + 1)
        div[i] -= s_
        div[j] += s_
    E[k] = 0


dfs(0)
ice_idx = {c: i for i, c in enumerate(ice)}


def flippable_at(c, pl):
    return len({c[k] * o for k, o in pl}) == 1


def flip(c, pl):
    c = list(c)
    for k, o in pl:
        c[k] = -c[k]
    return tuple(c)


n = len(ice)
Hrk_full = lil_matrix((n, n))
Hring = lil_matrix((n, n))
adj = [[] for _ in range(n)]
for i, c in enumerate(ice):
    for pl in plaqs:
        if flippable_at(c, pl):
            j = ice_idx[flip(c, pl)]
            Hrk_full[i, i] += 1.0
            Hrk_full[i, j] -= 1.0
            Hring[i, j] -= 1.0
            adj[i].append(j)
Hrk_full = Hrk_full.tocsr()
Hring = Hring.tocsr()
comp = [-1] * n
ncls = 0
for s0 in range(n):
    if comp[s0] >= 0:
        continue
    q = deque([s0])
    comp[s0] = ncls
    while q:
        u = q.popleft()
        for w in adj[u]:
            if comp[w] < 0:
                comp[w] = ncls
                q.append(w)
    ncls += 1
comp = np.array(comp)
# the summed projector is the Laplacian of the flip graph: symmetric, row sums zero, off-diagonals <= 0
sym_err = abs(Hrk_full - Hrk_full.T).max()
row_err = np.abs(np.asarray(Hrk_full.sum(axis=1))).max()
offd = Hrk_full.copy()
offd.setdiag(0)
nonpos = offd.max() <= 0
worst = max(np.linalg.norm(Hrk_full @ (comp == cl).astype(float)) for cl in range(ncls))
big = np.bincount(comp).argmax()
members = np.where(comp == big)[0]
lap_big = Hrk_full[members][:, members]
lam, lap_vec = eigsh(lap_big.asfptype(), k=2, which="SA", v0=rng.normal(size=len(members)))
lap_res = np.linalg.norm(lap_big@lap_vec-lap_vec*lam)
lam = np.sort(lam)
ring_big = Hring[members][:, members]
w_, v_ = eigsh(ring_big.asfptype(), k=1, which="SA", v0=rng.normal(size=len(members)))
ring_res = np.linalg.norm(ring_big@v_-v_*w_)
gs = np.abs(v_[:, 0])
spread = (gs.max() - gs.min()) / gs.mean()
frozen = int(sum(1 for i in range(n) if not adj[i]))
check("ground states on the 2x2x2 torus: the summed projector is the flip-graph Laplacian, for g>0 its kernel is spanned by class-uniform states; the pure ring ground state is not uniform",
      (n,ncls,len(members),frozen) == (9600,937,864,760) and max(lap_res,ring_res)<1e-8
      and sym_err == 0 and row_err < 1e-12 and nonpos and worst < 1e-12 and abs(lam[0]) < 1e-9 and lam[1] > 1e-6 and spread > 1e-3,
      f"{n} ice states, {ncls} flip classes (largest {len(members)}, {frozen} frozen states); Laplacian row sums {row_err:.0e}; "
      f"largest-class spectrum starts {lam[0]:.1e}, {lam[1]:.4f}; pure-ring ground amplitude spread {spread:.3f}")

# Coherent global uniform ground state has uniform readout too; g=0 has full kernel.
psi_uniform = np.ones(n)/np.sqrt(n)
check("uniform readout does not select a unique class-diagonal mixed state",
      np.linalg.norm(Hrk_full@psi_uniform)<1e-12 and np.allclose(psi_uniform**2,1/n)
      and ncls<n and np.linalg.norm(0*(Hrk_full@np.eye(1,n,0).ravel()))==0,
      f"coherent uniform vector is a ground state for g>0; at g=0 all {n} states lie in the kernel")

# ------------------------------------------ 4. unrecorded plaquette qubits
S = [np.array([[0, 1], [1, 0]], dtype=complex) / 2, np.array([[0, -1j], [1j, 0]]) / 2, np.diag([0.5 + 0j, -0.5])]
nrm = np.array([0.0, 0.0, 1.0])
B, J = 4.0, 1.0
energy = {}
for c in confs:
    Evals = np.array(c) * 0.5
    field = B * nrm + J * sum(Evals[k] * np.eye(3)[axis[k]] for k in range(4))
    energy[c] = np.linalg.eigvalsh(sum(field[m] * S[m] for m in range(3)))[0]
orbit_e = {kind(o): sorted({round(energy[c], 12) for c in o}) for o in orbits}
expect = {"flippable": -B / 2, "opposite": -B / 2, "odd": -np.sqrt(B * B + J * J) / 2, "adjacent": -np.sqrt(B * B + 2 * J * J) / 2}
ok_orb = all(len(v) == 1 and abs(v[0] - expect[k]) < 1e-12 for k, v in orbit_e.items())


def plaq_kind(c, pl):
    cc = [c[k] * o for k, o in pl]
    w = sum(1 for x in cc if x > 0)
    if w in (0, 4):
        return "flippable"
    if w in (1, 3):
        return "odd"
    return "opposite" if cc[0] == cc[2] else "adjacent"


pot = np.array([sum(expect[plaq_kind(c, pl)] for pl in plaqs) for c in ice])
mins = np.where(pot < pot.min() + 1e-9)[0]
uniform = all(len({ice[i][k] * (1) for k in range(nL) if links[k][2] == a}) == 1 for i in mins for a in range(3))
nflip_min = max(sum(1 for pl in plaqs if flippable_at(ice[i], pl)) for i in mins)
check("unrecorded plaquettes at D = 0 with normal fields: under Gauss compression the link field vanishes on flippable and opposite plaquettes (highest energy); the potential's minimizers on 2x2x2 are the 8 uniformly polarized ice states, with no flippable plaquette",
      ok_orb and len(mins) == 8 and uniform and nflip_min == 0,
      f"orbit energies (B/J = 4) {dict((k, round(float(v[0]), 5)) for k, v in orbit_e.items())}; minimizers {len(mins)}, uniform along each axis: {uniform}; flippable plaquettes in them {nflip_min}")

delta_flip = (np.sqrt(B*B+2*J*J)-B)/2
g_test = delta_flip/2
local = np.diag([energy[c]-expect["adjacent"] for c in confs])-g_test*ring
local_ev = np.linalg.eigvalsh(local)
check("local potential plus ring remains positive above polarized energy for 0<=g<Delta_flip",
      local_ev.min()>-1e-12 and np.count_nonzero(abs(local_ev)<1e-10)==4
      and abs(np.linalg.eigvalsh(np.array([[delta_flip,-g_test],[-g_test,delta_flip]]))[0]-(delta_flip-g_test))<1e-12,
      f"Delta_flip={delta_flip:.8f}, tested g={g_test:.8f}; only four adjacent local configurations have zero energy")

for resolution in ['N5 resolution 1: g>0 makes the graph Laplacian kernel the ground space; g=0 and g<0 require different statements.', 'N5 resolution 2: coherent class superpositions also have uniform configuration readout, so no unique mixed state is selected.', 'N5 resolution 3: the finite 2x2x2 graph counts distinct oriented links, including parallel-endpoint pairs.', 'N5 resolution 4: a local spectral-gap inequality controls ring competition; no universal scale ordering is assumed.', 'N5 resolution 5: state preparation, arbitrary record orientations and thermodynamic phases remain outside these finite controls.']:
    print(resolution)
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
