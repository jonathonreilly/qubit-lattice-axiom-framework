#!/usr/bin/env python3
"""Covariant nearest-neighbour two-qubit generators on Z^3 under the four proper-cubic actions.

The axioms supply no dynamics: Admissibility "is not a dynamics axiom" and does
not "choose a Hamiltonian or transfer operator". Every lane that moves content
supplies its own generator. This runner classifies the smallest candidate
dynamics clause, recorded as a decision point and not adopted: a time-independent
Hermitian generator that is a sum of two-site terms on nearest-neighbour bonds,
covariant under lattice translations and proper cubic rotations, for each of the
four actions of the rotations on qubit possibilities listed by the landed
soldering-menu note (trivial, sign twist, axis soldering, full soldering).

A bond term is written h = c + a.s_x + b.s_y + s_x^T M s_y for the bond (x, y=x+e).
Covariance sends the data at direction f to the data at R f by
(a, b, M) -> (rho(R) a, rho(R) b, rho(R) M rho(R)^T); reading the same bond from
its other end swaps a and b and transposes M.

Checks:

A. The four actions are homomorphisms into SO(3) with kernel orders 24, 12, 4, 1
   and kernel orbit counts 1, 1, 3, 6 on the six bond directions (the landed
   soldering-menu values), and fixed-subspace dimensions 3, 1, 0, 0.
B. Exact rational nullspaces: covariant bond data have one-site parts of
   dimension 3, 1, 1, 1 and two-site couplings of dimension 6, 4, 4, 3.
C. The net one-site field at a site (sum of the one-site parts of its six bonds)
   vanishes identically for axis and full soldering and is a uniform field on
   the invariant internal axes for the trivial action and the sign twist.
D. With possibility covariance (invariance under every internal rotation as
   well), every action leaves exactly the Heisenberg coupling M = J I and no
   one-site part.
E. Full soldering: the three couplings are J I, K e e^T and the Moriya term
   D e.(s_x x s_y) (the antisymmetric part), exactly.
F. Lattice-level covariance on the 3x3x3 torus: every basis element of every
   family is invariant under all 24 rotations about a site; a stabiliser-
   invariant datum that breaks the reversal rule is not; under the improper
   inversion (spins axial) J and K are fixed and the Moriya term changes sign.
G. Operator-level covariance on the seven-qubit star with SU(2) lifts of the
   actions: every covariant star generator commutes with all 24 rotations; a
   random non-covariant bond term does not; the Heisenberg bond term is
   J (2 SWAP - 1).

Star terms of three or more sites, time dependence and non-Hermitian
generators are not classified. The generator is a supplied decision point.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np
import sympy as sp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- the group
def cubic_rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            R = sp.zeros(3, 3)
            for i in range(3):
                R[i, p[i]] = s[i]
            if R.det() == 1:
                out.append(sp.ImmutableMatrix(R))
    return out


O = cubic_rotations()
I3 = sp.eye(3)


def absmat(R):
    return sp.ImmutableMatrix(R.applyfunc(abs))


ACTIONS = {
    "trivial": lambda R: sp.ImmutableMatrix(I3),
    "sign twist": lambda R: sp.ImmutableMatrix(sp.diag(1, absmat(R).det(), absmat(R).det())),
    "axis soldering": lambda R: sp.ImmutableMatrix(absmat(R).det() * absmat(R)),
    "full soldering": lambda R: sp.ImmutableMatrix(R),
}
NAMES = list(ACTIONS)

DIRS = [sp.ImmutableMatrix(v) for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1])]
EZ = sp.ImmutableMatrix([0, 0, 1])


def dir_index(v):
    for i, d in enumerate(DIRS):
        if d == v:
            return i
    raise ValueError(v)


# ------------------------------------------------------------- A: actions
print("A. the four actions of the proper cubic rotations")
kern, orbits, fixdim, homo = [], [], [], True
for name in NAMES:
    rho = ACTIONS[name]
    for A in O:
        for B in O:
            if rho(A * B) != rho(A) * rho(B):
                homo = False
        r = rho(A)
        if r * r.T != I3 or r.det() != 1:
            homo = False
    K = [R for R in O if rho(R) == I3]
    kern.append(len(K))
    seen, count = set(), 0
    for i in range(6):
        if i in seen:
            continue
        count += 1
        for R in K:
            seen.add(dir_index(sp.ImmutableMatrix(R * DIRS[i])))
    orbits.append(count)
    P = sum((rho(R) for R in O), sp.zeros(3, 3)) / 24
    fixdim.append(P.rank())
check("each action is a homomorphism into SO(3)", homo, "24 x 24 products, orthogonal, determinant one")
check("kernel orders 24, 12, 4, 1 and kernel orbits 1, 1, 3, 6 on the six directions (landed soldering menu)",
      kern == [24, 12, 4, 1] and orbits == [1, 1, 3, 6], f"kernels {kern}, orbits {orbits}")
check("fixed internal subspace dimensions 3, 1, 0, 0", fixdim == [3, 1, 0, 0], f"{fixdim}")

# ----------------------------------------------- B: covariant bond data at +z
print("B. covariant bond data for the bond (x, x + e_z)")
STAB = [R for R in O if R * EZ == EZ]
FLIP = [R for R in O if R * EZ == -EZ][0]
syms = sp.symbols("a0:3 b0:3 m0:9")
a_v = sp.Matrix(syms[0:3])
b_v = sp.Matrix(syms[3:6])
M_v = sp.Matrix(3, 3, syms[6:15])


def constraints(rho, internal_all=False):
    eqs = []
    for R in STAB:
        r = rho(R)
        eqs += list(r * a_v - a_v) + list(r * b_v - b_v) + list(r * M_v * r.T - M_v)
    r = rho(FLIP)
    eqs += list(r * a_v - b_v) + list(r * b_v - a_v) + list(r * M_v * r.T - M_v.T)
    if internal_all:
        gens = [sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
                sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
                sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]
        for L in gens:
            eqs += list(L * a_v) + list(L * b_v) + list(L * M_v - M_v * L)
    A = sp.Matrix([[sp.diff(e, s) for s in syms] for e in eqs])
    return A


def nullspace_split(A):
    ns = A.nullspace()
    one = [v for v in ns if any(v[i] != 0 for i in range(6))]
    two = [v for v in ns if all(v[i] == 0 for i in range(6))]
    mixed = [v for v in one if any(v[i] != 0 for i in range(6, 15))]
    # the constraints do not couple (a,b) with M, so the nullspace splits
    return ns, one, two, mixed


BASIS = {}
dims_one, dims_two = [], []
n_mixed = 0
for name in NAMES:
    ns, one, two, mixed = nullspace_split(constraints(ACTIONS[name]))
    BASIS[name] = ns
    dims_one.append(len(one))
    dims_two.append(len(two))
    n_mixed += len(mixed)
check("the constraints decouple: no basis vector mixes one-site and two-site parts", n_mixed == 0, f"{n_mixed} mixed")
check("one-site parts of covariant bond data have dimensions 3, 1, 1, 1", dims_one == [3, 1, 1, 1], f"{dims_one}")
check("two-site couplings M have dimensions 6, 4, 4, 3", dims_two == [6, 4, 4, 3], f"{dims_two}")

# ------------------------------------------------------ C: net one-site field
print("C. the net one-site field at a site")
net_ok, net_detail = True, []
for name in NAMES:
    rho = ACTIONS[name]
    R_to = {}
    for R in O:
        R_to.setdefault(dir_index(sp.ImmutableMatrix(R * EZ)), R)
    fields = []
    for v in BASIS[name]:
        a0 = sp.Matrix(v[0:3])
        if all(x == 0 for x in a0):
            continue
        U = sum((rho(R_to[i]) * a0 for i in range(6)), sp.zeros(3, 1))
        fields.append(U)
    rank = sp.Matrix.hstack(*fields).rank() if fields else 0
    net_detail.append(f"{name} rank {rank}")
    want = {"trivial": 3, "sign twist": 1, "axis soldering": 0, "full soldering": 0}[name]
    net_ok &= rank == want
check("net field vanishes for axis and full soldering; uniform on the invariant axes otherwise",
      net_ok, "; ".join(net_detail))

# ------------------------------------------------ D: possibility covariance
print("D. possibility covariance (every internal rotation as well)")
pc_ok, pc_detail = True, []
for name in NAMES:
    ns = constraints(ACTIONS[name], internal_all=True).nullspace()
    ok = len(ns) == 1 and all(ns[0][i] == 0 for i in range(6))
    if ok:
        M = sp.Matrix(3, 3, list(ns[0][6:15]))
        ok = M == M[0, 0] * I3 and M[0, 0] != 0
    pc_ok &= ok
    pc_detail.append(f"{name}: {len(ns)}")
check("every action leaves exactly the Heisenberg coupling M = J I and no one-site part",
      pc_ok, "nullspace dims " + ", ".join(pc_detail))

# ------------------------------------------------------------ E: full soldering
print("E. full soldering: Heisenberg, compass and Moriya couplings")
full_two = [sp.Matrix(3, 3, list(v[6:15])) for v in BASIS["full soldering"] if all(v[i] == 0 for i in range(6))]
Jm, Km = I3, EZ * EZ.T
Dm = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])   # s_x^T Dm s_y = e_z . (s_x x s_y)
span_given = sp.Matrix.hstack(*[sp.Matrix(list(m)) for m in full_two])
span_named = sp.Matrix.hstack(*[sp.Matrix(list(m)) for m in (Jm, Km, Dm)])
same = span_given.rank() == 3 and span_named.rank() == 3 and sp.Matrix.hstack(span_given, span_named).rank() == 3
sx = sp.Matrix(sp.symbols("p0:3"))
sy = sp.Matrix(sp.symbols("q0:3"))
dm_form = sp.expand((sx.T * Dm * sy)[0] - EZ.dot(sx.cross(sy))) == 0
check("full-soldering couplings are exactly span{J I, K e e^T, D e.(s_x x s_y)}",
      same and dm_form, "Moriya term = the antisymmetric part of M")

# ------------------------------------------- F: lattice covariance on 3x3x3
print("F. lattice-level covariance on the 3x3x3 torus")
L = 3
SITES = list(itertools.product(range(L), repeat=3))


def mod(v):
    return tuple(int(c) % L for c in v)


def hamiltonian_tensor(a, b, M, rho):
    """Coefficient tensor {(x,i):c} and {(x,i,y,j):c} of sum over bonds (x, x+e), e>0."""
    one, two = {}, {}
    R_to = {}
    for R in O:
        R_to.setdefault(dir_index(sp.ImmutableMatrix(R * EZ)), R)
    for x in SITES:
        for ei in (0, 2, 4):  # +x, +y, +z
            R = R_to[ei]
            r = np.array(rho(R), dtype=float)
            af, bf, Mf = r @ a, r @ b, r @ M @ r.T
            y = mod(np.array(x) + np.array(DIRS[ei], dtype=int).ravel())
            for i in range(3):
                one[(x, i)] = one.get((x, i), 0.0) + af[i]
                one[(y, i)] = one.get((y, i), 0.0) + bf[i]
                for j in range(3):
                    if x < y:
                        key, val = (x, i, y, j), Mf[i, j]
                    else:
                        key, val = (y, j, x, i), Mf[i, j]
                    two[key] = two.get(key, 0.0) + val
    return one, two


def transform(tensor, R, rho, axial_inversion=False):
    one, two = tensor
    Rn = -np.eye(3) if axial_inversion else np.array(R, dtype=float)
    r = np.eye(3) if axial_inversion else np.array(rho(R), dtype=float)
    n1, n2 = {}, {}
    for (x, i), c in one.items():
        xr = mod(Rn @ np.array(x))
        for k in range(3):
            n1[(xr, k)] = n1.get((xr, k), 0.0) + r[k, i] * c
    for (x, i, y, j), c in two.items():
        xr, yr = mod(Rn @ np.array(x)), mod(Rn @ np.array(y))
        for k in range(3):
            for l in range(3):
                val = r[k, i] * r[l, j] * c
                key = (xr, k, yr, l) if xr < yr else (yr, l, xr, k)
                n2[key] = n2.get(key, 0.0) + val
    return n1, n2


def dist(t1, t2):
    d = 0.0
    for part in (0, 1):
        keys = set(t1[part]) | set(t2[part])
        d = max([d] + [abs(t1[part].get(k, 0.0) - t2[part].get(k, 0.0)) for k in keys])
    return d


lat_ok, worst = True, 0.0
for name in NAMES:
    rho = ACTIONS[name]
    for v in BASIS[name]:
        a = np.array(v[0:3], dtype=float).ravel()
        b = np.array(v[3:6], dtype=float).ravel()
        M = np.array(v[6:15], dtype=float).reshape(3, 3)
        T = hamiltonian_tensor(a, b, M, rho)
        for R in O:
            d = dist(transform(T, R, rho), T)
            worst = max(worst, d)
            lat_ok &= d < 1e-12
check("every basis element of every family is invariant under all 24 rotations", lat_ok, f"max deviation {worst:.1e}")

rho = ACTIONS["trivial"]
Manti = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], dtype=float)  # stabiliser-invariant, breaks reversal
T = hamiltonian_tensor(np.zeros(3), np.zeros(3), Manti, rho)
broken = max(dist(transform(T, R, rho), T) for R in O)
check("negative control: a stabiliser-invariant antisymmetric datum breaks covariance (reversal rule)",
      broken > 0.5, f"max deviation {broken:.2f}")

rho = ACTIONS["full soldering"]
inv = {}
for label, M in (("J", np.eye(3)), ("K", np.diag([0.0, 0.0, 1.0])), ("D", np.array(Dm, dtype=float))):
    T = hamiltonian_tensor(np.zeros(3), np.zeros(3), M, rho)
    Ti = transform(T, None, rho, axial_inversion=True)
    neg = ({k: -v for k, v in T[0].items()}, {k: -v for k, v in T[1].items()})
    inv[label] = ("even" if dist(Ti, T) < 1e-12 else "odd" if dist(Ti, neg) < 1e-12 else "neither")
check("improper inversion (spins axial): J and K even, Moriya odd",
      inv == {"J": "even", "K": "even", "D": "odd"}, f"{inv}")

# ------------------------------------------- G: operator level, 7-qubit star
print("G. operator-level covariance on the seven-qubit star")
PAULI = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
ID2 = np.eye(2, dtype=complex)


def su2_lift(r):
    r = np.array(r, dtype=float)
    # V s_a V^dag = sum_b r[b, a] s_b ; build V from the adjoint action
    best = None
    for V in candidate_unitaries(r):
        err = max(np.abs(V @ PAULI[a] @ V.conj().T - sum(r[b, a] * PAULI[b] for b in range(3))).max() for a in range(3))
        if best is None or err < best[0]:
            best = (err, V)
    return best


def candidate_unitaries(r):
    tr = np.trace(r)
    ang = np.arccos(np.clip((tr - 1) / 2, -1, 1))
    if abs(ang) < 1e-12:
        return [ID2]
    if abs(ang - np.pi) < 1e-9:
        axes = []
        for i in range(3):
            n = (r[:, i] + np.eye(3)[:, i])
            if np.linalg.norm(n) > 1e-9:
                axes.append(n / np.linalg.norm(n))
        cands = []
        for n in axes:
            cands.append(-1j * sum(n[k] * PAULI[k] for k in range(3)))
        return cands
    n = np.array([r[2, 1] - r[1, 2], r[0, 2] - r[2, 0], r[1, 0] - r[0, 1]]) / (2 * np.sin(ang))
    out = []
    for sgn in (1, -1):
        out.append(np.cos(ang / 2) * ID2 - 1j * sgn * np.sin(ang / 2) * sum(n[k] * PAULI[k] for k in range(3)))
    return out


def op_on(site_ops, n=7):
    out = np.array([[1.0 + 0j]])
    for k in range(n):
        out = np.kron(out, site_ops.get(k, ID2))
    return out


def star_generator(a, b, M, rho):
    """Centre qubit 0, neighbour f on qubit 1 + dir_index(f)."""
    H = np.zeros((128, 128), dtype=complex)
    R_to = {}
    for R in O:
        R_to.setdefault(dir_index(sp.ImmutableMatrix(R * EZ)), R)
    for fi in range(6):
        r = np.array(rho(R_to[fi]), dtype=float)
        af, bf, Mf = r @ a, r @ b, r @ M @ r.T
        q = 1 + fi
        for i in range(3):
            H += af[i] * op_on({0: PAULI[i]}) + bf[i] * op_on({q: PAULI[i]})
            for j in range(3):
                H += Mf[i, j] * op_on({0: PAULI[i], q: PAULI[j]})
    return H


def star_rotation(R, rho):
    V = su2_lift(rho(R))
    perm = [0] + [1 + dir_index(sp.ImmutableMatrix(R * DIRS[fi])) for fi in range(6)]
    # qubit k moves to qubit perm[k]
    dim = 128
    P = np.zeros((dim, dim))
    for s in range(dim):
        bits = [(s >> (6 - k)) & 1 for k in range(7)]
        nb = [0] * 7
        for k in range(7):
            nb[perm[k]] = bits[k]
        t = sum(nb[k] << (6 - k) for k in range(7))
        P[t, s] = 1
    return P @ op_on({k: V[1] for k in range(7)}), V[0]


rng = np.random.default_rng(20260924)
star_ok, lift_err, star_worst = True, 0.0, 0.0
for name in NAMES:
    rho = ACTIONS[name]
    coeffs = rng.normal(size=len(BASIS[name]))
    vec = sum(c * np.array(v, dtype=float).ravel() for c, v in zip(coeffs, BASIS[name]))
    H = star_generator(vec[0:3], vec[3:6], vec[6:15].reshape(3, 3), rho)
    for R in O:
        U, e = star_rotation(R, rho)
        lift_err = max(lift_err, e)
        d = np.abs(U @ H @ U.conj().T - H).max()
        star_worst = max(star_worst, d)
        star_ok &= d < 1e-10
check("every covariant star generator commutes with the 24 lifted rotations", star_ok and lift_err < 1e-12,
      f"max commutator entry {star_worst:.1e}; SU(2) lift error {lift_err:.1e}")

rho = ACTIONS["full soldering"]
Hbad = star_generator(rng.normal(size=3), rng.normal(size=3), rng.normal(size=(3, 3)), rho)
bad = max(np.abs(star_rotation(R, rho)[0] @ Hbad @ star_rotation(R, rho)[0].conj().T - Hbad).max() for R in O)
check("negative control: a random bond datum is not covariant", bad > 1e-2, f"max commutator entry {bad:.2f}")

SWAP = np.zeros((4, 4))
for i in range(2):
    for j in range(2):
        SWAP[2 * j + i, 2 * i + j] = 1
heis = sum(np.kron(PAULI[k], PAULI[k]) for k in range(3))
check("the Heisenberg bond term is 2 SWAP - 1", np.abs(heis - (2 * SWAP - np.eye(4))).max() < 1e-12,
      "s.s = 2 SWAP - 1 exchanges neighbouring possibilities")

print('per_element: Pauli coefficients and exact bond covariance constraints are tested.')
print('per_site: One-site endpoint fields and their summed ranks are tested.')
print('per_mode: checked and not executed — no normal-mode or continuum classification is claimed.')
print('per_block: Finite periodic coefficient and recorded-star controls are tested.')
print('lattice_wide: checked and not executed — finite covariance is not a physical thermodynamic derivation.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
