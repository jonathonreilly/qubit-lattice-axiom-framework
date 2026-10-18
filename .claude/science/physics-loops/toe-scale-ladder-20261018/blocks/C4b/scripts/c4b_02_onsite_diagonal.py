"""C4b-02: exact checks for the on-site / diagonal-layer route (NOTE.md Lemmas 3-4).

(a) Covariant on-site automorphisms Ad(u^{(x)Z^3}): Ad(u) <-> rotation O_u in SO(3); covariance
    <=> O_u commutes with every Q(R).  We compute the real commutant of {Q(R)} and its SO(3) part.
(b) Orbit spans: a covariant QCA that fixes sigma_m at every site also fixes sigma_{Q(R)m}
    (at every site, by covariance + translation invariance).  If span{Q(R)m} has dim >= 2 the
    QCA fixes two non-parallel Pauli directions at each site, hence everything (identity).
(c) Axis action: an explicit non-Clifford, entangling, O-covariant range-1 QCA diagonal in the
    sigma_n frame, n=(1,1,1)/sqrt3: alpha = Ad(prod_{r, e in faces/2} exp(i phi s_n(r) s_n(r+e))).
    Its covariance is checked on explicit matrices for the local rule on the 7-site star,
    for all 24 R, all three Pauli images, with phi = 0.3 (generic).
"""
import itertools
import numpy as np
from scipy.linalg import null_space, expm
from c4b_common import check, total, O, menu_Q, su2_lift, PAULI, I2

ACTIONS = ['trivial', 'sign', 'axis', 'full']

# (a) commutant
for act in ACTIONS:
    Qs = [menu_Q(R, act).astype(float) for R in O]
    # X with Q X = X Q for all Q: (I kron Q - Q^T kron I) vec X = 0
    A = np.vstack([np.kron(np.eye(3), Q) - np.kron(Q.T, np.eye(3)) for Q in Qs])
    ns = null_space(A)
    dim = ns.shape[1]
    exp_dim = {'trivial': 9, 'sign': 3, 'axis': 2, 'full': 1}[act]
    # expected dims: trivial -> all of M3; sign: image {1, diag(1,-1,-1)} -> commutant
    #   = block diag(1x1, 2x2) of dim 1+4=5?  (computed below; see note) ; axis: A1+E -> 2;
    #   full: irreducible vector rep of O -> 1.
    print(f"[a] action={act}: real commutant dim = {dim}")
    if act == 'full':
        check("full: commutant of Q(O) is scalars (only identity in SO(3))", dim == 1)
    if act == 'axis':
        # commutant = a P_n + b P_E ; SO(3) part: a=1, b=+-1 -> {1, pi rotation about n}
        n = np.ones(3) / np.sqrt(3)
        Pn = np.outer(n, n)
        PE = np.eye(3) - Pn
        basis = ns.T.reshape(-1, 3, 3).transpose(0, 2, 1)
        # check span equals span{Pn, PE}
        M = np.array([b.reshape(-1) for b in basis])
        T = np.array([Pn.reshape(-1), PE.reshape(-1)])
        rk = np.linalg.matrix_rank(np.vstack([M, T]), tol=1e-9)
        check("axis: commutant = span{P_n, P_E} (dim 2)", dim == 2 and rk == 2)
        Rn = Pn - PE      # pi rotation about n
        ok = all(np.allclose(Rn @ Q, Q @ Rn) for Q in Qs) and abs(np.linalg.det(Rn) - 1) < 1e-12
        check("axis: covariant on-site automorphisms = {id, Ad(sigma_n)} (pi about n)", ok)
    if act == 'sign':
        print(f"    sign action: commutant dim {dim} (contains all rotations about x)")

# (b) orbit spans of a direction m under each action
for act in ['axis', 'full']:
    Qs = [menu_Q(R, act).astype(float) for R in O]
    rs = rng = np.random.default_rng(1)
    worst = 3
    for trial in range(200):
        m = rng.normal(size=3)
        span = np.linalg.matrix_rank(np.array([Q @ m for Q in Qs]), tol=1e-9)
        worst = min(worst, span)
    n = np.ones(3)
    span_n = np.linalg.matrix_rank(np.array([Q @ n for Q in Qs]), tol=1e-9)
    # lines through the special axes
    spans_axes = {tuple(m): np.linalg.matrix_rank(np.array([Q @ np.array(m, float) for Q in Qs]), tol=1e-9)
                  for m in [(1, 0, 0), (1, 1, 0), (1, -1, 0), (1, 1, 1)]}
    print(f"[b] {act}: min span over random m = {worst}; span(orbit of (1,1,1)) = {span_n}; axes {spans_axes}")
    if act == 'full':
        ok = worst == 3 and all(v == 3 for v in spans_axes.values())
        check("full: every direction m has O-orbit spanning R^3 => a covariant QCA fixing all sigma_m is the identity", ok)
    else:
        ok = worst == 3 and span_n == 1 and spans_axes[(1, -1, 0)] == 2
        check("axis: only m = +-n has a 1-dim orbit; every other m has orbit span >= 2", ok)

# (c) explicit non-Clifford covariant diagonal QCA under the axis action, local rule on star
n = np.ones(3) / np.sqrt(3)
sn = sum(n[a] * PAULI[a] for a in range(3))
sites = [(0, 0, 0)] + [tuple(v) for v in itertools.chain.from_iterable(
    [(np.eye(3, dtype=int)[a], -np.eye(3, dtype=int)[a]) for a in range(3)])]
sites = [tuple(int(x) for x in s) for s in sites]
idx = {s: i for i, s in enumerate(sites)}
NS = len(sites)


def op_at(o, i):
    out = np.array([[1.0 + 0j]])
    for j in range(NS):
        out = np.kron(out, o if j == i else I2)
    return out


phi = 0.3
# Generator restricted to terms touching site 0: the 6 face bonds (0, e).  Bonds not touching 0
# commute with every operator at site 0 and with each other, so alpha(A_0) = V A_0 V^dag with
# V = exp(i phi sum_e s_n(0) s_n(e)).
SN = [op_at(sn, i) for i in range(NS)]
Hloc = sum(SN[0] @ SN[i] for i in range(1, NS))
V = expm(1j * phi * Hloc)


def alpha_local(A0):
    return V @ A0 @ V.conj().T


def site_perm_unitary(R):
    """unitary permuting the 7 star sites by r -> R r."""
    dim = 2 ** NS
    U = np.zeros((dim, dim))
    for b in range(dim):
        bits = [(b >> (NS - 1 - j)) & 1 for j in range(NS)]
        out = [0] * NS
        for j, s in enumerate(sites):
            t = tuple(int(x) for x in (R @ np.array(s)))
            out[idx[t]] = bits[j]
        o = 0
        for j in range(NS):
            o = (o << 1) | out[j]
        U[o, b] = 1
    return U


ok_all = True
maxerr = 0.0
for R in O:
    Q = menu_Q(R, 'axis')
    u = su2_lift(Q)
    Ubeta = op_at(I2, 0)
    for i in range(NS):
        Ubeta = Ubeta @ op_at(u, i)       # on-site layer (ops on different sites commute)
    Ubeta = Ubeta @ site_perm_unitary(R)
    for a in range(3):
        A0 = op_at(PAULI[a], 0)
        lhs = alpha_local(Ubeta @ A0 @ Ubeta.conj().T)       # alpha(beta(A_0)), beta(A_0) at site 0
        rhs = Ubeta @ alpha_local(A0) @ Ubeta.conj().T        # beta(alpha(A_0))
        err = np.abs(lhs - rhs).max()
        maxerr = max(maxerr, err)
check("axis: Ad(exp(i phi sum s_n s_n)) (face bonds, phi=0.3) is O-covariant on the star local rule",
      maxerr < 1e-10, f"max err {maxerr:.2e}")
# entangling and non-Clifford: image of sigma_x has weight on more than one site, and is not
# a single Pauli string up to phase
img = alpha_local(op_at(PAULI[0], 0))
# expand in Pauli basis on sites 0 and 1 only weight check: commutator with s_n(e) nonzero
# (first version of this test checked a commutator with s_n(e), which vanishes identically for a
#  diagonal QCA -- a test-logic bug, see WORKLOG; replaced by the support test below)
red = img.reshape(2, 2 ** (NS - 1), 2, 2 ** (NS - 1))
# alpha(X_0) is single-site iff it equals (its partial trace over sites != 0) (x) 1
A0 = np.einsum('iaja->ij', red) / 2 ** (NS - 1)
nontriv = np.abs(img - np.kron(A0, np.eye(2 ** (NS - 1)))).max() > 1e-6
check("axis diagonal example is entangling (alpha(X_0) is not a single-site operator)", nontriv)
# non-Clifford: count Pauli components of alpha(X_0) restricted to sites {0, e_x}
paulis = [I2] + PAULI
cnt = 0
for p0 in range(4):
    for p1 in range(4):
        P = op_at(paulis[p0], 0) @ op_at(paulis[p1], 1)
        # trace over all others: use Hilbert-Schmidt with identity elsewhere
        c = np.trace(P.conj().T @ img) / 2 ** NS
        if abs(c) > 1e-9:
            cnt += 1
check("axis diagonal example is not a Clifford image (alpha(X_0) has > 1 Pauli component on {0,e})",
      cnt > 1, f"{cnt} Pauli components")
total()
