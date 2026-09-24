#!/usr/bin/env python3
"""Charges are Gauss defects: where U(1) charge can live under the clause.

Doubled coordinates (vertex, link, plaquette, cube sites have 0, 1, 2, 3 odd
coordinates). Oriented link fields are covariant under full soldering alone
(open PR 9066), so links are soldered here. The runner certifies (supplied
models, finite diagnostics, no physical reading):

1. No covariant one-qubit charge: under full soldering the stabilizers of the
   four roles (orders 24, 8, 8, 24) fix no Bloch axis.
2. No two-site charge transfer: a vertex-link bond is fixed by the four
   quarter-turns about the link axis. With the link soldered, a covariant
   two-site term flips the link only when the vertex is fully soldered too
   (flip dimensions 0, 0, 0, >0 for trivial, sign twist, axis, full at the
   vertex), and a fully soldered vertex has no covariant charge.
3. Defects: with the soft Gauss energy U sum_v (div E_v)^2 on the coarse
   L = 6 torus, flipping one link of an ice state costs 2U and leaves charges
   +1 and -1 at its ends; every flip of a link that carries the +1 defect's
   field onward to a neutral vertex keeps the energy 2U and moves the defect
   by one link.
4. Bosons: the defect hops are single-link flips on distinct qubits; the
   Levin-Wen T-junction commutator t1 t2^dag t3 - t3 t2^dag t1 vanishes, so
   the exchange phase is 1.
5. Record phases are pure gauge: for random complex transverse fields on one
   plaquette, the exact effective ring element equals -5/(2U^3) times the
   product of the four flip amplitudes along the ring, to O(h^6); its phase
   is a lattice curl of the link amplitude phases, so on the torus the ring
   phases have zero sum over every cube and a link rephasing makes every
   ring element negative real.
6. Magnitudes matter: with unequal transverse field sizes the fourth-order
   diagonal energy differs between ice configurations.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 600

import numpy as np
from scipy.linalg import expm, null_space, sqrtm

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(924)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0 + 0j, -1.0])
PAULI = [I2, X, Y, Z]
S = [X / 2, Y / 2, Z / 2]


def kron(*ops):
    return reduce(np.kron, ops)


def site_op(single, k, n):
    return kron(*[single if i == k else I2 for i in range(n)])


def sdot(v):
    return sum(v[k] * S[k] for k in range(3))


rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)


def lift(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(ang, 0):
        return I2.copy()
    if np.isclose(ang, np.pi):
        w, v = np.linalg.eig(R)
        nvec = np.real(v[:, np.argmin(abs(w - 1))])
    else:
        nvec = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    nvec = nvec / np.linalg.norm(nvec)
    return expm(-1j * ang * sum(nvec[k] * PAULI[k + 1] for k in range(3)) / 2)


def perm_sign(R):
    return round(np.linalg.det(np.abs(R)))


ACTIONS = {
    "trivial": lambda R: np.eye(3),
    "sign twist": lambda R: np.diag([1.0, perm_sign(R), perm_sign(R)]),
    "axis": lambda R: perm_sign(R) * np.abs(R),
    "full": lambda R: R,
}


def role(x):
    return sum(int(c) % 2 for c in x)


# ------------------------------------------------ 1. no covariant charge
WIN = [np.array(p) for p in itertools.product(range(-3, 4), repeat=3)]


def stabilizer(c):
    c = np.array(c)
    out = []
    for R in rots:
        if all(role(c + R @ (p - c)) == role(p) for p in WIN):
            out.append(R)
    return out


orders, axes = [], []
for c in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]:
    st = stabilizer(c)
    orders.append(len(st))
    axes.append(null_space(np.vstack([R - np.eye(3) for R in st])).shape[1])
check("no covariant one-qubit charge: under full soldering no role's stabilizer fixes a Bloch axis",
      orders == [24, 8, 8, 24] and axes == [0, 0, 0, 0],
      f"stabilizer orders (vertex, link, plaquette, cube) {orders}; fixed axes {axes}")

# ------------------------------------------ 2. no two-site charge transfer
bond_stab = [R for R in rots if np.allclose(R @ np.array([1, 0, 0]), [1, 0, 0])]
E_link = site_op(S[0], 1, 2)            # the link runs along x: E = s^x
basis2 = [np.kron(PAULI[a], PAULI[b]) for a in range(4) for b in range(4)]
flip_dims, transfer = [], []
for name, rho in ACTIONS.items():
    rows = []
    for R in bond_stab:
        Uv = lift(rho(R))
        V = np.kron(Uv, lift(R))
        rows.append(np.array([(V @ B @ V.conj().T).ravel() for B in basis2]).T - np.array([B.ravel() for B in basis2]).T)
    ns = null_space(np.vstack(rows))
    ops = [sum(ns[k, c] * basis2[k] for k in range(16)) for c in range(ns.shape[1])]
    flips = [O @ E_link - E_link @ O for O in ops]
    flip_dims.append(int(np.linalg.matrix_rank(np.array([f.ravel() for f in flips]), tol=1e-9)) if flips else 0)
    # charge axes: every invariant axis of the vertex action (trivial: all of x, y, z and a random one)
    fixed = null_space(np.vstack([rho(R) - np.eye(3) for R in rots]))
    cand = [fixed[:, k] for k in range(fixed.shape[1])]
    if name == "trivial":
        cand.append(rng.normal(size=3))
    worst = 0.0
    for q in cand:
        Qv = site_op(sdot(q / np.linalg.norm(q)), 0, 2)
        for O in ops:
            # a term transfers charge if it changes both Q_v and E_l
            both = (O @ Qv - Qv @ O) @ E_link - E_link @ (O @ Qv - Qv @ O)
            worst = max(worst, np.linalg.norm(both))
    transfer.append(float(worst) if cand else None)
ok2 = flip_dims[:3] == [0, 0, 0] and flip_dims[3] > 0 and all(t is None or t < 1e-9 for t in transfer)
check("no two-site charge transfer: a soldered link is flipped by a covariant vertex-link term only when the vertex is fully soldered, which has no charge",
      ok2, f"bond stabilizer {len(bond_stab)}; link-flip dims (trivial, sign twist, axis, full) {flip_dims}; charge-transfer norms (no charge axis: -) {['-' if t is None else f'{t:.1e}' for t in transfer]}")

# ------------------------------------------------------- 3. defects
LC = 6
verts = list(itertools.product(range(LC), repeat=3))
vid = {v: i for i, v in enumerate(verts)}
links = []
for v in verts:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % LC
        links.append((vid[v], vid[tuple(w)], a))
nV, nL = len(verts), len(links)
inc = {i: [] for i in range(nV)}
for k, (i, j, a) in enumerate(links):
    inc[i].append(k)
    inc[j].append(k)


def div(E):
    d = np.zeros(nV)
    for k, (i, j, a) in enumerate(links):
        d[i] += E[k]
        d[j] -= E[k]
    return d


def energy(E):
    return float(np.sum(div(E) ** 2))


E = np.array([0.5 * (-1) ** [verts[i][1], verts[i][0] + 1, verts[i][0]][a] for (i, j, a) in links])
assert not np.any(div(E))
k0 = int(rng.integers(nL))
E1 = E.copy()
E1[k0] *= -1
d1 = div(E1)
pair_ok = abs(energy(E1) - 2) < 1e-12 and sorted(d1[d1 != 0]) == [-1, 1]
plus = int(np.where(d1 == 1)[0][0])
moves, moves_ok = 0, True
for k in inc[plus]:
    i, j, a = links[k]
    out = E1[k] if i == plus else -E1[k]          # outward field from the +1 defect
    far = j if i == plus else i
    if out > 0 and d1[far] == 0:
        E2 = E1.copy()
        E2[k] *= -1
        d2 = div(E2)
        moves += 1
        moves_ok &= abs(energy(E2) - 2) < 1e-12 and d2[plus] == 0 and d2[far] == 1
check("defects: one flip from ice costs 2U and leaves charges +1, -1; flips carrying the +1 defect's field onward keep 2U and move it one link",
      pair_ok and moves > 0 and moves_ok, f"pair energy {energy(E1):.0f} U; hop moves from the +1 defect {moves}, all at 2U and moving the charge: {moves_ok}")

# --------------------------------------------------------- 4. bosons
dirs = [rng.normal(size=3) for _ in range(3)]
t = [site_op(sdot(np.cross(np.eye(3)[k], dirs[k])), k, 3) for k in range(3)]   # transverse flips on three links
lw = np.linalg.norm(t[0] @ t[1].conj().T @ t[2] - t[2] @ t[1].conj().T @ t[0])
check("bosons: the Levin-Wen T-junction commutator of the defect hops vanishes (exchange phase 1)",
      lw < 1e-12, f"|t1 t2^dag t3 - t3 t2^dag t1| = {lw:.1e}")

# ------------------------------------------------- 5. pure-gauge phases
ppos_axis = [0, 1, 0, 1]                       # bottom (x), right (y), top (x), left (y)
corner_rows = np.array([[1, 0, 0, 1], [-1, 1, 0, 0], [0, -1, -1, 0], [0, 0, 1, -1]], dtype=float)


def plaquette_model(fields):
    Es = [site_op(S[ppos_axis[k]], k, 4) for k in range(4)]
    C = [sum(corner_rows[c, k] * Es[k] for k in range(4)) for c in range(4)]
    H0 = sum(Cc @ Cc for Cc in C)
    V = sum(site_op(sdot(fields[k]), k, 4) for k in range(4))
    return Es, H0, V


def e_basis(axis):
    w, v = np.linalg.eigh(S[axis])
    return v[:, 1], v[:, 0]                    # (+1/2, -1/2) eigenvectors


def config_state(vals):
    vecs = []
    for k, sgn in enumerate(vals):
        plus_v, minus_v = e_basis(ppos_axis[k])
        vecs.append(plus_v if sgn > 0 else minus_v)
    return kron(*vecs)


a_vals, b_vals = (1, 1, -1, -1), (-1, -1, 1, 1)
ratios, phase_err = [], []
for h in [0.03, 0.015]:
    fields = []
    for k in range(4):
        d = np.cross(np.eye(3)[ppos_axis[k]], rng.normal(size=3))
        fields.append(h * (0.6 + 0.8 * rng.random()) * d / np.linalg.norm(d))
    Es, H0, V = plaquette_model(fields)
    ev, vec = np.linalg.eigh(H0 + V)
    A, B = config_state(a_vals), config_state(b_vals)
    Bm = np.array([A, B]).T
    Phi = Bm.conj().T @ vec[:, :2]
    Sm = Phi @ Phi.conj().T
    Sinv = np.linalg.inv(sqrtm(Sm))
    Heff = Sinv @ Phi @ np.diag(ev[:2]) @ Phi.conj().T @ Sinv
    amps = []
    for k in range(4):
        plus_v, minus_v = e_basis(ppos_axis[k])
        frm = plus_v if a_vals[k] > 0 else minus_v
        to = plus_v if b_vals[k] > 0 else minus_v
        amps.append(to.conj() @ sdot(fields[k]) @ frm)
    pred = -2.5 * np.prod(amps)
    ratios.append(Heff[1, 0] / pred)
    phase_err.append(abs(np.angle(Heff[1, 0] / pred)))
# on the torus: ring phases from random link amplitude phases sum to zero over every cube
alpha = rng.uniform(-np.pi, np.pi, size=nL)
lid = {(i, a): k for k, (i, j, a) in enumerate(links)}


def ring_phase(v, a, b):
    # plaquette at vertex v spanned by axes a < b, circulation a then b
    va = list(verts[v]); va[a] = (va[a] + 1) % LC
    vb = list(verts[v]); vb[b] = (vb[b] + 1) % LC
    return alpha[lid[(v, a)]] + alpha[lid[(vid[tuple(va)], b)]] - alpha[lid[(vid[tuple(vb)], a)]] - alpha[lid[(v, b)]]


cube_err = 0.0
for v in range(nV):
    tot = 0.0
    for (a, b) in [(0, 1), (1, 2), (2, 0)]:
        lo, hi = min(a, b), max(a, b)
        sgn = 1 if (a, b) == (lo, hi) else -1
        c = [x for x in range(3) if x not in (a, b)][0]
        up = list(verts[v]); up[c] = (up[c] + 1) % LC
        tot += sgn * (ring_phase(vid[tuple(up)], lo, hi) - ring_phase(v, lo, hi))
    cube_err = max(cube_err, abs(np.angle(np.exp(1j * tot))))
check("record phases are pure gauge: exact ring element = -5/(2U^3) x product of flip amplitudes (phase included); ring phases are a lattice curl, zero over every cube",
      abs(ratios[-1] - 1) < 1e-3 and abs(ratios[-1] - 1) < abs(ratios[0] - 1) and phase_err[-1] < 1e-3 and cube_err < 1e-9,
      f"ratio {ratios[0]:.5f}, {ratios[1]:.5f} at h/U = 0.03, 0.015; phase error {phase_err[-1]:.1e} rad; max cube sum {cube_err:.1e}")

# ------------------------------------------------ 6. magnitudes matter
mag = 0.5 + rng.random(nL)                       # unequal transverse field sizes |t_l| ~ h |t|


def fourth_diag(Ec, w):
    e1 = 2.0
    tot = 0.0
    for v in range(nV):
        for k1, k2 in itertools.permutations(inc[v], 2):
            i1, j1, _ = links[k1]
            i2, j2, _ = links[k2]
            o1 = Ec[k1] if i1 == v else -Ec[k1]
            o2 = Ec[k2] if i2 == v else -Ec[k2]
            e12 = 2.0 if o1 * o2 < 0 else 6.0
            tot += w[k1] * w[k2] * (1 / (e1 * e12 * e1) + 1 / (e1 * e1 * e12))
    return -tot / 16


plaqs = []
for v in range(nV):
    for (a, b) in [(0, 1), (1, 2), (0, 2)]:
        va = list(verts[v]); va[a] = (va[a] + 1) % LC
        vb = list(verts[v]); vb[b] = (vb[b] + 1) % LC
        plaqs.append([(lid[(v, a)], 1), (lid[(vid[tuple(va)], b)], 1), (lid[(vid[tuple(vb)], a)], -1), (lid[(v, b)], -1)])


def flippable(Ec, pl):
    s = [np.sign(Ec[k]) * o for k, o in pl]
    return len(set(s)) == 1


confs = [E.copy()]
Ec = E.copy()
for _ in range(3):
    for _ in range(3000):
        pl = plaqs[rng.integers(len(plaqs))]
        if flippable(Ec, pl):
            for k, o in pl:
                Ec[k] *= -1
    assert not np.any(div(Ec))
    confs.append(Ec.copy())
uni = [fourth_diag(c, np.ones(nL)) for c in confs]
une = [fourth_diag(c, mag ** 2) for c in confs]
check("magnitudes matter: equal field sizes give one fourth-order diagonal energy on all ice states; unequal sizes do not (the disjoint-pair and renormalization parts are configuration independent)",
      max(uni) - min(uni) < 1e-9 and max(une) - min(une) > 1e-6,
      f"shared-vertex part, equal sizes: spread {max(uni) - min(uni):.1e}; unequal sizes: spread {max(une) - min(une):.4f} (units h^4/U^3)")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
