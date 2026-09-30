#!/usr/bin/env python3
"""T26 test: does the actual nearest-neighbour hopping / lattice covariance select or even
admit the graph-first factorwise gauge algebra on the 8-state taste cube?

Operator definitions copied from scripts/frontier_graph_first_su3_integration.py (main, read only).
Pre-registration: PREREGISTER.md (same folder).
"""
import itertools, math
import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=140)
I8 = np.eye(8, dtype=complex)
idx = {x: i for i, x in enumerate(itertools.product((0, 1), repeat=3))}


def shift_op(axis):
    op = np.zeros((8, 8), dtype=complex)
    for x, i in idx.items():
        y = list(x); y[axis] = 1 - y[axis]
        op[idx[tuple(y)], i] = 1
    return op


def parity_op(axis):
    op = np.zeros((8, 8), dtype=complex)
    for x, i in idx.items():
        op[i, i] = 1.0 if x[axis] == 0 else -1.0
    return op


def swap_axes(a, b):
    op = np.zeros((8, 8), dtype=complex)
    for x, i in idx.items():
        y = list(x); y[a], y[b] = y[b], y[a]
        op[idx[tuple(y)], i] = 1
    return op


def comm(a, b):
    return a @ b - b @ a


# ---------- linear algebra helpers over the reals for anti-Hermitian matrices ----------
def vec(M):
    return np.concatenate([M.real.ravel(), M.imag.ravel()])


class Span:
    def __init__(self, n=8):
        self.n = n
        self.Q = np.zeros((0, 2 * n * n))
        self.mats = []

    def add(self, M, tol=1e-9):
        v = vec(M)
        if self.Q.shape[0]:
            v = v - self.Q.T @ (self.Q @ v)
            v = v - self.Q.T @ (self.Q @ v)
        nv = np.linalg.norm(v)
        if nv < tol:
            return False
        self.Q = np.vstack([self.Q, v / nv])
        self.mats.append(M)
        return True

    @property
    def dim(self):
        return self.Q.shape[0]

    def contains(self, M, tol=1e-8):
        v = vec(M)
        if self.dim == 0:
            return np.linalg.norm(v) < tol
        r = v - self.Q.T @ (self.Q @ v)
        return np.linalg.norm(r) < tol


def close(gens, conj_by=(), maxit=50):
    """Lie closure of the real span of anti-Hermitian matrices `gens`, also closed under
    conjugation by the unitaries in conj_by (group generators)."""
    S = Span()
    for g in gens:
        S.add(g)
    for _ in range(maxit):
        n0 = S.dim
        cur = list(S.mats)
        for a, b in itertools.combinations(cur, 2):
            S.add(comm(a, b))
        for U in conj_by:
            for a in cur:
                S.add(U @ a @ U.conj().T)
        if S.dim == n0:
            break
    return S


def commutant_dim(ops, n=8):
    """complex dimension of {A : [A,h]=0 for all h}; returns (dim, list of basis matrices)."""
    rows = [np.kron(np.eye(n), h) - np.kron(h.T, np.eye(n)) for h in ops]
    M = np.vstack(rows)
    u, s, vh = np.linalg.svd(M)
    rank = int(np.sum(s > 1e-9))
    null = vh[rank:].conj().T
    return null.shape[1], [null[:, k].reshape(n, n) for k in range(null.shape[1])]


# ---------- the graph-first algebra (selected axis 0) ----------
axis = 0
X = [shift_op(a) for a in range(3)]
Z = [parity_op(a) for a in range(3)]
Yp = -1j * Z[0] @ X[0]
weak = [X[0] / 2, Yp / 2, Z[0] / 2]
tau = swap_axes(1, 2)

# basis change as in the repo: fibre (axis 0) (x) base (axes 1,2) ordered (b1,b2)
cols = []
for f in (0, 1):
    for b1 in (0, 1):
        for b2 in (0, 1):
            col = np.zeros(8, dtype=complex); col[idx[(f, b1, b2)]] = 1; cols.append(col)
U = np.column_stack(cols)
e0, e1 = np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)
U4 = np.column_stack([np.kron(e0, e0), (np.kron(e0, e1) + np.kron(e1, e0)) / math.sqrt(2),
                      np.kron(e1, e1), (np.kron(e0, e1) - np.kron(e1, e0)) / math.sqrt(2)])
U8 = np.kron(np.eye(2), U4)
lam = [np.array(m, dtype=complex) for m in [
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]]]
lam.append(np.diag([1, 1, -2]).astype(complex) / math.sqrt(3))
su3 = []
for l in lam:
    l4 = np.zeros((4, 4), dtype=complex); l4[:3, :3] = l / 2
    su3.append(U @ U8 @ np.kron(np.eye(2), l4) @ U8.conj().T @ U.conj().T)
swp = tau
Pp, Pm = (I8 + swp) / 2, (I8 - swp) / 2
Yhyp = Pp / 3 - Pm
# sanity: repo facts
assert all(np.linalg.norm(comm(t, w)) < 1e-9 for t in su3 for w in weak)
assert all(np.linalg.norm(comm(t, tau)) < 1e-9 for t in su3)

A = lambda M: 1j * M  # anti-Hermitian version of a Hermitian generator
g_su3 = [A(t) for t in su3]
g_su2 = [A(w) for w in weak]
g_u1 = [A(Yhyp)]
g8 = g_su3 + g_su2 + g_u1
S8 = close(g8)
print("== sanity: graph-first algebra g8 = su(3)+su(2)+u(1)_Y on C^8, real dim of span+closure:", S8.dim, "(expect 12)")

report = {}
report["dim_g8"] = S8.dim

# ------------- TEST A: hopping commutant (strict R1a) -------------
print("\n== TEST A: symmetry algebra of the actual cube-edge hopping")
G1 = X[0]
G2 = Z[0] @ X[1]
G3 = Z[0] @ Z[1] @ X[2]
Gam = [G1, G2, G3]
assert all(np.linalg.norm(G1 @ G2 + G2 @ G1) < 1e-9 for _ in [0])
sets = {
    "S_i = X_i (cube-edge shifts, graph-first H(phi)=sum phi_i S_i)": X,
    "S_1, S_2+S_3 (tau-symmetrised base hopping)": [X[0], X[1] + X[2]],
    "S_1, S_2+S_3 and tau": [X[0], X[1] + X[2], tau],
    "Cl(3) Gamma_i (Jordan-Wigner)": Gam,
    "Cl(3) Gamma_i and tau": Gam + [tau],
}
report["A"] = {}
for name, ops in sets.items():
    d, basis = commutant_dim(ops)
    # centre dimension of the commutant algebra (to read off block structure): dim of {A in C: [A,B]=0 for all B in C}
    if d > 0:
        dd, _ = commutant_dim(basis)
    else:
        dd = 0
    # intersection of g8 with commutant
    cs = Span()
    for M in basis:
        cs.add(1j * (M + M.conj().T) / 2); cs.add(M - M.conj().T)
    inter = 0
    # dimension of g8 ∩ commutant: solve for coefficients c with sum c_k g8_k in commutant
    G = np.array([np.concatenate([vec(comm(g, h)) for h in ops]) for g in g8]).T  # columns = images
    sv = np.linalg.svd(G, compute_uv=False)
    inter = len(g8) - int(np.sum(sv > 1e-9))
    G3_ = np.array([np.concatenate([vec(comm(g, h)) for h in ops]) for g in g_su3]).T
    sv3 = np.linalg.svd(G3_, compute_uv=False)
    inter3 = len(g_su3) - int(np.sum(sv3 > 1e-9))
    G2_ = np.array([np.concatenate([vec(comm(g, h)) for h in ops]) for g in g_su2]).T
    sv2 = np.linalg.svd(G2_, compute_uv=False)
    inter2 = len(g_su2) - int(np.sum(sv2 > 1e-9))
    print(f"  hopping set: {name}\n     commutant dim = {d}, centre of commutant dim = {dd}"
          f"  (abelian iff equal); dim(g8 ∩ commutant)={inter}; dim(su(3) ∩ commutant)={inter3}; dim(su(2)_weak ∩ commutant)={inter2}")
    report["A"][name] = dict(commutant=d, centre=dd, g8_cap=inter, su3_cap=inter3, su2_cap=inter2)

# norms of [lambda_a, S_2], [lambda_a, S_2+S_3]
mx2 = max(np.linalg.norm(comm(t, X[1])) for t in su3)
mx23 = max(np.linalg.norm(comm(t, X[1] + X[2])) for t in su3)
print(f"  max_a ||[T_a, S_2]|| = {mx2:.3f};  max_a ||[T_a, S_2+S_3]|| = {mx23:.3f};  (both nonzero => su(3) is not a symmetry of the hopping)")
report["A"]["norms"] = dict(S2=float(mx2), S23=float(mx23))

# ------------- TEST B: lattice covariance closure (R1b) -------------
print("\n== TEST B: covariance closure of the graph-first algebra under the lattice's internal action")
Perm = {"P12": swap_axes(0, 1), "P13": swap_axes(0, 2), "P23": swap_axes(1, 2)}
groups = {
    "translations <X1,X2,X3>": X,
    "translations + tau(2<->3)": X + [tau],
    "single translation <X2> only": [X[1]],
    "single translation <X1> only": [X[0]],
    "translations + all axis perms (full cube-graph automorphism group B3)": X + list(Perm.values()),
    "tau only (residual swap; selector's stabiliser part)": [tau],
    "<X1, X2X3, tau> (elements that commute with the Sym/Anti split)": [X[0], X[1] @ X[2], tau],
}
report["B"] = {}
for name, gens in groups.items():
    r = {}
    for label, start in [("g8", g8), ("su(3) part", g_su3), ("su(2)_weak part", g_su2)]:
        S = close(start, gens)
        r[label] = S.dim
    print(f"  group {name}:  closure dims  g8 -> {r['g8']}, su(3)-part -> {r['su(3) part']}, su(2)_weak -> {r['su(2)_weak part']}")
    report["B"][name] = r

# what is the closure of g8 under translations? is it u(8) (64) or su(8)+? contains identity?
S_T = close(g8, X)
ident_in = S_T.contains(1j * I8)
print(f"  closure(g8, translations): dim {S_T.dim}; contains i*identity: {ident_in}")
report["B_closure_T"] = dict(dim=S_T.dim, contains_identity=bool(ident_in))
S_T3 = close(g_su3, X)
tr_in = S_T3.contains(1j * I8)
print(f"  closure(su(3), translations): dim {S_T3.dim}; contains i*identity: {tr_in}")

# proper rotation subgroup of the cube acting on the corners, with translations
def rot_generators():
    # 90-degree rotation about axis 0: (x0,x1,x2)-> (x0, x2, 1-x1) as corner map; rotation about axis1 and 2 similarly
    def perm_from_map(f):
        op = np.zeros((8, 8), dtype=complex)
        for x, i in idx.items():
            y = f(x); op[idx[tuple(y)], i] = 1
        return op
    R0 = perm_from_map(lambda x: (x[0], x[2], 1 - x[1]))
    R1 = perm_from_map(lambda x: (1 - x[2], x[1], x[0]))
    R2 = perm_from_map(lambda x: (x[1], 1 - x[0], x[2]))
    return [R0, R1, R2]
Rg = rot_generators()
S_rot = close(g8, X + Rg)
print(f"  closure(g8, translations + proper cube rotations): dim {S_rot.dim}")
S_rot_only = close(g8, Rg)
print(f"  closure(g8, proper cube rotations only): dim {S_rot_only.dim}")
report["B_rot"] = dict(T_plus_rot=S_rot.dim, rot_only=S_rot_only.dim)

# ------------- controls -------------
print("\n== CONTROLS")
S_w = close(g_su2, X + list(Perm.values()))
print(f"  control: weak su(2)_1 closed under translations + axis perms -> dim {S_w.dim} (expect 9 = su(2)^3, covariant)")
report["control_weak"] = S_w.dim
# covariant su(3) does exist on the 3-dim 'linear function' subspace V3 = span{(-1)^{x_i}}
V3 = np.column_stack([np.array([1.0 if x[a] == 0 else -1.0 for x in idx]) for a in range(3)]) / math.sqrt(8)
su3_V = []
for l in lam:
    su3_V.append(1j * (V3 @ (l / 2) @ V3.T).astype(complex))
S_V = close(su3_V, X + list(Perm.values()))
print(f"  su(3) on V3=span{{(-1)^x_i}} closed under translations + axis perms: dim {S_V.dim} (=8: covariant), "
      f"but the lattice group then acts INSIDE U(3): translations act on V3 as diag signs (nontrivial).")
tr_act = [np.round(V3.T @ x @ V3, 3) for x in X]
print("     X_1 restricted to V3 =", np.diag(tr_act[0]))
report["control_V3_su3"] = S_V.dim

# ------------- lemma: irreducible carrier, commutant, maximality -------------
print("\n== LEMMA CHECKS on C^6 = C^3 (x) C^2")
def gm(n):
    ms = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex); m[i, j] = m[j, i] = 1; ms.append(m)
            m = np.zeros((n, n), dtype=complex); m[i, j] = -1j; m[j, i] = 1j; ms.append(m)
    for k in range(1, n):
        m = np.zeros((n, n), dtype=complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        ms.append(m / math.sqrt(k * (k + 1) / 2))
    return ms
G3m, G2m = gm(3), gm(2)
I3, I2 = np.eye(3), np.eye(2)
g6 = [1j * np.kron(m, I2) for m in G3m] + [1j * np.kron(I3, m) for m in G2m] + [1j * np.eye(6)]
S6 = Span(6)
for m in g6: S6.add(m)
def close6(gens):
    S = Span(6)
    for g in gens: S.add(g)
    for _ in range(30):
        n0 = S.dim; cur = list(S.mats)
        for a, b in itertools.combinations(cur, 2): S.add(comm(a, b))
        if S.dim == n0: break
    return S
S6c = close6(g6)
print(f"  dim g6 = {S6c.dim} (expect 12)")
c6, _ = commutant_dim([-1j * m for m in g6], n=6)
print(f"  commutant of g6 in M_6: dim {c6} (scalars only => irreducible)")
cu6, _ = commutant_dim([-1j * np.eye(6)] + [np.zeros((6, 6))], n=6)
# commutant of all of u(6): scalars only
full = []
for i in range(6):
    for j in range(6):
        m = np.zeros((6, 6), dtype=complex); m[i, j] = 1; full.append(m)
cf, _ = commutant_dim(full, n=6)
print(f"  commutant of u(6): dim {cf}  => constant hopping matrices commuting with g6 are scalars, which commute with all of u(6): no separation")
rng = np.random.default_rng(1)
cross = []
for a in range(8):
    for b in range(3):
        cross.append(np.kron(G3m[a], G2m[b]))
jump = []
for k in range(0, 24, 5):
    S = close6(g6 + [1j * cross[k]])
    jump.append(S.dim)
print(f"  adding ONE cross-factor generator (su(3)(x)su(2)) to g6 and closing: dims {jump} (expect 36 = u(6): g6 is maximal; the wall is one bit about the 24 cross generators)")
report["lemma"] = dict(dim_g6=S6c.dim, comm_g6=c6, comm_u6=cf, jump=jump)

import json
json.dump(report, open(__file__.replace("test_T26.py", "test_T26_results.json"), "w"), indent=1, default=str)
print("\nwritten results json")
