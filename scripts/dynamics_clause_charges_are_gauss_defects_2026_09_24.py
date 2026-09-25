#!/usr/bin/env python3
"""Supplied Gauss-defect model: covariance, hopping channels and basis phases.
Role stabilizers forbid a nonconstant fully soldered one-qubit scalar charge.
The displayed two-defect T-junction channel has equal nonzero hop products.
Arbitrary on-link phase removal is a unitary basis change, generally not a
Gauss-generated vertex gauge transformation. Finite-h ring ED tests its
fourth-order asymptote. Physical statistics and a selected phase remain open.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_CHARGES_ARE_GAUSS_DEFECTS_NO_QUBIT_CARRIES_A_COVARIANT_CHARGE_UNDER_FULL_SOLDERING_DEFECTS_ARE_BOSONS_AND_RECORD_PHASES_ARE_PURE_GAUGE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md']

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
ok2 = flip_dims == [0, 0, 0, 2] and all(t is None or t < 1e-9 for t in transfer)
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
check("bare distinct-link flips satisfy the algebraic T-junction relation; a projected nonzero channel is checked separately",
      lw < 1e-12, f"|t1 t2^dag t3 - t3 t2^dag t1| = {lw:.1e}")

# Explicit two-positive-defect channel, with negative partners away from the junction.
center = 0
def far_end(link,vertex):
    i,j,_ = links[link]
    return j if i == vertex else i
def outward(field,link,vertex):
    return field[link] if links[link][0] == vertex else -field[link]
incoming = [q for q in inc[center] if outward(E,q,center)<0]
outgoing = [q for q in inc[center] if outward(E,q,center)>0]
jlink,llink = incoming[:2]
klink = outgoing[0]
j,l,k = [far_end(q,center) for q in (jlink,llink,klink)]
initial = E.copy()
used = {center,j,l,k}
for leaf in (j,l):
    candidates = [q for q in inc[leaf] if outward(initial,q,leaf)<0 and far_end(q,leaf) not in used]
    assert candidates
    q = candidates[0]
    used.add(far_end(q,leaf))
    initial[q] *= -1
assert energy(initial)==4 and div(initial)[j]==div(initial)[l]==1 and div(initial)[center]==0
finals = []
for sequence in [(jlink,klink,llink),(llink,klink,jlink)]:
    state = initial.copy()
    for q in sequence:
        source = far_end(q,center) if q != klink else center
        target = center if q != klink else k
        charges = div(state)
        assert charges[source]==1 and charges[target]==0 and outward(state,q,source)>0
        state[q] *= -1
        assert energy(state)==4
    finals.append(state)
check("nonzero projected two-defect T-junction channel has equal unit-amplitude products",
      np.array_equal(*finals) and div(finals[0])[center]==div(finals[0])[k]==1,
      "both three-hop orders remain at energy 4U with two fixed negative partners and give the identical electric configuration")

# ------------------------------------------------- 5. link-basis phases
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
unit_fields = []                                  # one random transverse field set, scaled by h below
for k in range(4):
    d = np.cross(np.eye(3)[ppos_axis[k]], rng.normal(size=3))
    unit_fields.append((0.6 + 0.8 * rng.random()) * d / np.linalg.norm(d))
for h in [0.03, 0.015]:
    fields = [h * f for f in unit_fields]
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
check("fourth-order ring asymptote includes the flip phases; their lattice curl has zero cube sum but need not vanish",
      abs(ratios[-1] - 1) < 1e-3 and abs(ratios[-1] - 1) < abs(ratios[0] - 1) and phase_err[-1] < 1e-3 and cube_err < 1e-9,
      f"ratio {ratios[0]:.5f}, {ratios[1]:.5f} at h/U = 0.03, 0.015; phase error {phase_err[-1]:.1e} rad; max cube sum {cube_err:.1e}")

# Local unitary phase removal is exact for H0 plus the stated fields.
phase_unitary_error = 0.0
for alpha0 in (0.2,1.1,-0.7):
    raising = (X+1j*Y)/2
    Uphase = expm(-1j*alpha0*S[2])
    field = np.exp(1j*alpha0)*raising+np.exp(-1j*alpha0)*raising.conj().T
    phase_unitary_error = max(phase_unitary_error,np.linalg.norm(Uphase@field@Uphase.conj().T-X))
check("on-link unitary removes transverse phases, even when their plaquette curl is nonzero",
      phase_unitary_error<1e-12 and abs(np.angle(np.exp(1j*ring_phase(0,0,1))))>1e-3,
      f"local conjugation error {phase_unitary_error:.2e}; nonzero sample curl rules out a vertex-gradient interpretation")

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

for resolution in ['N5 resolution 1: Full-soldering scalar charge obstruction is scoped to one-qubit role stabilizers, not composite matter.', 'N5 resolution 2: An explicit projected two-defect T-junction channel realizes equal nonzero hop products; a universal quasiparticle phase is not inferred.', 'N5 resolution 3: On-link phase conjugation gives exact model equivalence but nonzero curl disproves a general vertex-gauge interpretation.', 'N5 resolution 4: The ring coefficient is fourth-order perturbation theory; finite-h diagonalization is an asymptotic diagnostic.', 'N5 resolution 5: Unequal transverse magnitudes can split ice configurations; neither constant diagonal shifts nor auxiliary fermions select physical matter.']:
    print(resolution)
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
