"""Shared library for block C4: cubic-covariant one-qubit Clifford QCAs on Z^3.

Conventions (adopted from
docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_..._2026-10-17.md and its runner,
and docs/THE_SOLDERING_MENU_FOUR_ACTIONS_..._2026-09-22.md):
  * O = the 24 signed 3x3 permutation matrices of determinant +1, acting on Z^3 about the origin.
  * A soldering action is a homomorphism Q: O -> SO(3); a Pauli label sigma_a (a=1,2,3 = X,Y,Z)
    at site r is sent to sum_b Q(R)[b,a] sigma_b at site R r.  The menu: trivial, sign
    diag(1,s,s), axis s|R|, full R  (s = sign of the axis permutation of R).
  * Because Q(R) is a signed permutation matrix of det 1, it is an on-site Clifford automorphism
    (conjugation by an SU(2) lift), so the composite beta_R is a Clifford automorphism.

Symplectic representation: a Pauli string (mod phase) supported on the 27-cell is a vector in
F2^54 = (x-bits[27], z-bits[27]); X=(1,0), Z=(0,1), Y=(1,1).
"""
from __future__ import annotations

import itertools
import numpy as np

# ------------------------------------------------------------------ group O
def build_O():
    O = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[p[i], i] = s[i]
            if round(np.linalg.det(M)) == 1:
                O.append(M)
    return O


O = build_O()
OKEY = {M.tobytes(): i for i, M in enumerate(O)}


def gidx(M):
    return OKEY[np.asarray(M, int).tobytes()]


MUL = np.array([[gidx(O[i] @ O[j]) for j in range(24)] for i in range(24)])
INV = np.array([gidx(O[i].T) for i in range(24)])
ID = gidx(np.eye(3, dtype=int))


def perm_sign(M):
    return int(round(np.linalg.det(np.abs(M))))


def menu_Q(M, action):
    if action == 'trivial':
        return np.eye(3, dtype=int)
    if action == 'sign':
        s = perm_sign(M)
        return np.diag([1, s, s])
    if action == 'axis':
        return perm_sign(M) * np.abs(M)
    if action == 'full':
        return M.copy()
    raise ValueError(action)


def menu_hom(action):
    """Homomorphism as a list of 24 target indices into O."""
    return [gidx(menu_Q(M, action)) for M in O]


def is_hom(h, H=None):
    H = range(24) if H is None else H
    Hs = set(H)
    for i in H:
        for j in H:
            k = MUL[i, j]
            if k in Hs and h[k] != MUL[h[i], h[j]]:
                return False
    return True


def all_homs():
    """All homomorphisms O -> O, by generator images + closure (exhaustive over 24x24 pairs)."""
    a = gidx(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))  # quarter turn about z
    b = gidx(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]))  # threefold about (1,1,1)
    homs = set()
    for A in range(24):
        for B in range(24):
            h = {ID: ID}
            frontier = [ID]
            ok = True
            while frontier and ok:
                nxt = []
                for g in frontier:
                    for gen, im in ((a, A), (b, B)):
                        k = MUL[g, gen]
                        v = MUL[h[g], im]
                        if k in h:
                            if h[k] != v:
                                ok = False
                                break
                        else:
                            h[k] = v
                            nxt.append(k)
                    if not ok:
                        break
                frontier = nxt
            if ok and len(h) == 24:
                hh = tuple(h[i] for i in range(24))
                if is_hom(hh):
                    homs.add(hh)
    return sorted(homs)


def conj_class_of_hom(h):
    return frozenset(tuple(MUL[MUL[c, h[i]], INV[c]] for i in range(24)) for c in range(24))


# ------------------------------------------------------------------ subgroups used
def subgroup(gens):
    S = {ID}
    frontier = [ID]
    while frontier:
        nxt = []
        for g in frontier:
            for x in gens:
                k = MUL[g, x]
                if k not in S:
                    S.add(k)
                    nxt.append(k)
        frontier = nxt
    return sorted(S)


def G(m):
    return gidx(np.array(m))


R4z = G([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
R2x = G([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
R2y = G([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])
R3d = G([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
R2f = G([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])  # half-turn about (1,-1,0)
SUBGROUPS = {
    'O': list(range(24)),
    'T': subgroup([R3d, R2x, R2y]),
    'D4': subgroup([R4z, R2x]),
    'D3': subgroup([R3d, R2f]),
    'D2': subgroup([R2x, R2y]),
}

# ------------------------------------------------------------------ cell geometry
import os
RADIUS = int(os.environ.get('C4_RADIUS', '1'))  # Chebyshev radius of the neighbourhood (1 = 27-cell)
CELL = [tuple(p) for p in itertools.product(range(-RADIUS, RADIUS + 1), repeat=3)]
CIDX = {p: i for i, p in enumerate(CELL)}
NC = len(CELL)
D = 2 * NC  # length of a symplectic cell vector
SHIFTS = [tuple(t) for t in itertools.product(range(-2 * RADIUS, 2 * RADIUS + 1), repeat=3)]
T0 = SHIFTS.index((0, 0, 0))

# pairs for translate form: <v, T_t v'> = sum_r v_x(r) v'_z(r-t) + v_z(r) v'_x(r-t)
SHIFT_PAIRS = []
for t in SHIFTS:
    I, J = [], []
    for i, r in enumerate(CELL):
        q = (r[0] - t[0], r[1] - t[1], r[2] - t[2])
        if q in CIDX:
            I.append(i)
            J.append(CIDX[q])
    SHIFT_PAIRS.append((np.array(I, int), np.array(J, int)))

LABEL_BITS = {1: (1, 0), 2: (1, 1), 3: (0, 1)}
BITS_LABEL = {v: k for k, v in LABEL_BITS.items()}


def label_map(Qm):
    """unsigned label permutation and sign: a -> (b, sign) with Q[b,a] = sign."""
    out = {}
    for a in (1, 2, 3):
        col = Qm[:, a - 1]
        b = int(np.nonzero(col)[0][0])
        out[a] = (b + 1, int(col[b]))
    return out


def B_matrix(Ridx, Qm):
    """54x54 F2 matrix of beta_R (unsigned) on cell vectors (cell is O-stable)."""
    R = O[Ridx]
    lm = label_map(Qm)
    B = np.zeros((D, D), np.uint8)
    # image of x-bit at site i (label X=1) and z-bit (label Z=3)
    for i, r in enumerate(CELL):
        j = CIDX[tuple(int(v) for v in R @ np.array(r))]
        for a, col in ((1, i), (3, NC + i)):
            bx, bz = LABEL_BITS[lm[a][0]]
            if bx:
                B[j, col] ^= 1
            if bz:
                B[NC + j, col] ^= 1
    return B


# ------------------------------------------------------------------ F2 linear algebra
def f2_rref(A):
    A = (np.array(A, dtype=np.uint8) % 2).copy()
    m, n = A.shape
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i, c]:
                p = i
                break
        if p is None:
            continue
        if p != r:
            A[[r, p]] = A[[p, r]]
        rows = np.nonzero(A[:, c])[0]
        for i in rows:
            if i != r:
                A[i] ^= A[r]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A[:r], piv


def f2_nullspace(A):
    A = np.array(A, dtype=np.uint8) % 2
    m, n = A.shape
    Rr, piv = f2_rref(A)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(n, np.uint8)
        v[f] = 1
        for row, pc in zip(Rr, piv):
            if row[f]:
                v[pc] = 1
        basis.append(v)
    return np.array(basis, dtype=np.uint8).reshape(len(basis), n)


def covariance_space(hin, hout, H):
    """Basis of the F2 subspace of (u, w) in F2^108 (u = v_X, w = v_Z) satisfying the unsigned
    covariance  v_{rho_in(R) a} = B^{out}_R v_a  for a in {X, Z}, R in H."""
    rows = []
    E = np.eye(D, dtype=np.uint8)
    Zr = np.zeros((D, D), np.uint8)
    sel = {1: np.hstack([E, Zr]), 3: np.hstack([Zr, E]), 2: np.hstack([E, E])}  # v_X, v_Z, v_Y
    for R in H:
        Qin = O[hin[R]]
        Bout = B_matrix(R, O[hout[R]])
        lm = label_map(Qin)
        for a in (1, 3):
            b = lm[a][0]
            rows.append((sel[b] + Bout @ sel[a]) % 2)
    A = np.vstack(rows)
    return f2_nullspace(A)


def forms_batch(U, W):
    """U, W: (N,54) uint8 arrays. Returns (N,125) array of <U, T_t W> over F2."""
    Ux, Uz = U[:, :NC], U[:, NC:]
    Wx, Wz = W[:, :NC], W[:, NC:]
    out = np.zeros((U.shape[0], len(SHIFTS)), np.uint8)
    for k, (I, J) in enumerate(SHIFT_PAIRS):
        if len(I) == 0:
            continue
        out[:, k] = ((Ux[:, I] & Wz[:, J]).sum(1) + (Uz[:, I] & Wx[:, J]).sum(1)) & 1
    return out


DELTA0 = np.zeros(len(SHIFTS), np.uint8)
DELTA0[T0] = 1


def enumerate_solutions(basis, chunk_bits=16):
    """Exhaustive enumeration of all (u,w) in span(basis) satisfying the symplectic conditions
    <u,T_t u> = 0, <w,T_t w> = 0, <u,T_t w> = delta_{t0} for every shift t in {-2..2}^3.
    Returns list of 2D-vectors.  Exhaustive over 2^d combinations (d = dim)."""
    d = basis.shape[0]
    sols = []
    if d == 0:
        return sols
    bas = basis.astype(np.uint8)
    lo = min(d, chunk_bits)
    nlo = 1 << lo
    coeff_lo = ((np.arange(nlo)[:, None] >> np.arange(lo)[None, :]) & 1).astype(np.uint8)
    span_lo = (coeff_lo @ bas[:lo]) & 1  # (nlo,108)
    for hi in range(1 << (d - lo)):
        hv = np.zeros(2 * D, np.uint8)
        for k in range(d - lo):
            if (hi >> k) & 1:
                hv ^= bas[lo + k]
        V = span_lo ^ hv
        U, Wv = V[:, :D], V[:, D:]
        f_uw = forms_batch(U, Wv)
        ok = np.all(f_uw == DELTA0, axis=1)
        if not ok.any():
            continue
        idx = np.nonzero(ok)[0]
        f_uu = forms_batch(U[idx], U[idx])
        f_ww = forms_batch(Wv[idx], Wv[idx])
        ok2 = (~f_uu.any(1)) & (~f_ww.any(1))
        for i in idx[ok2]:
            sols.append(V[i].copy())
    return sols


# ------------------------------------------------------------------ signed Pauli strings
# A Pauli string: (k, dict site->label) meaning i^k * prod_site sigma_label (Hermitian labels).
# single-site products: sigma_a sigma_b = delta + i eps_abc sigma_c
def _mul1(a, b):
    if a == 0:
        return 0, b
    if b == 0:
        return 0, a
    if a == b:
        return 0, 0
    c = 6 - a - b
    eps = 1 if (a, b) in ((1, 2), (2, 3), (3, 1)) else -1
    return (1 if eps == 1 else 3), c


def pmul(P, Qp):
    k = (P[0] + Qp[0]) % 4
    d = dict(P[1])
    for s, b in Qp[1].items():
        a = d.get(s, 0)
        dk, c = _mul1(a, b)
        k = (k + dk) % 4
        if c:
            d[s] = c
        else:
            d.pop(s, None)
    return (k, d)


def pstr_from_vec(v, sign=1):
    d = {}
    for i, r in enumerate(CELL):
        bx, bz = int(v[i]), int(v[NC + i])
        if bx or bz:
            d[r] = BITS_LABEL[(bx, bz)]
    return (0 if sign == 1 else 2, d)


def peq(P, Qp):
    return P[0] % 4 == Qp[0] % 4 and P[1] == Qp[1]


def beta(Ridx, Qm, P):
    R = O[Ridx]
    k = P[0]
    d = {}
    for s, a in P[1].items():
        col = Qm[:, a - 1]
        b = int(np.nonzero(col)[0][0])
        if col[b] < 0:
            k = (k + 2) % 4
        d[tuple(int(x) for x in R @ np.array(s))] = b + 1
    return (k, d)


def translate(P, t):
    return (P[0], {(s[0] + t[0], s[1] + t[1], s[2] + t[2]): a for s, a in P[1].items()})


def images(PX, PZ):
    """alpha on single-site Paulis at origin: X->PX, Z->PZ, Y = iXZ -> i PX PZ."""
    PY = pmul((1, {}), pmul(PX, PZ))
    return {1: PX, 2: PY, 3: PZ}


def signed_covariant(PX, PZ, hin, hout, H):
    """Check alpha(beta^in_R(sigma_a,0)) = beta^out_R(alpha(sigma_a,0)) with phases, a in {X,Z}."""
    im = images(PX, PZ)
    for R in H:
        Qin, Qout = O[hin[R]], O[hout[R]]
        for a in (1, 3):
            col = Qin[:, a - 1]
            b = int(np.nonzero(col)[0][0])
            lhs = im[b + 1]
            if col[b] < 0:
                lhs = ((lhs[0] + 2) % 4, lhs[1])
            rhs = beta(R, Qout, im[a])
            if not peq(lhs, rhs):
                return False
    return True


# ------------------------------------------------------------------ Laurent polynomials over F2
# polynomial = frozenset of exponent tuples (coefficients in F2)
def padd(*ps):
    out = set()
    for p in ps:
        out ^= set(p)
    return frozenset(out)


def pmulL(p, q):
    out = set()
    for a in p:
        for b in q:
            e = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
            out ^= {e}
    return frozenset(out)


def pbar(p):
    return frozenset((-a[0], -a[1], -a[2]) for a in p)


ONE = frozenset({(0, 0, 0)})
ZERO = frozenset()


def vec_to_poly(v):
    """symplectic cell vector -> (x-part poly, z-part poly); site r <-> monomial x^r."""
    px = frozenset(CELL[i] for i in range(NC) if v[i])
    pz = frozenset(CELL[i] for i in range(NC) if v[NC + i])
    return px, pz


def matrix_of(sol):
    """M = [[a, b], [c, d]] with columns = images of X and Z: (x-part; z-part)."""
    a, c = vec_to_poly(sol[:D])
    b, d = vec_to_poly(sol[D:])
    return [[a, b], [c, d]]


def mat_mul(A, B):
    return [[padd(pmulL(A[i][0], B[0][j]), pmulL(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def mat_dagger(A):
    return [[pbar(A[0][0]), pbar(A[1][0])], [pbar(A[0][1]), pbar(A[1][1])]]


LAM = [[ZERO, ONE], [ONE, ZERO]]


def is_symplectic(M):
    L = mat_mul(mat_dagger(M), mat_mul(LAM, M))
    return L[0][0] == ZERO and L[1][1] == ZERO and L[0][1] == ONE and L[1][0] == ONE


def det(M):
    return padd(pmulL(M[0][0], M[1][1]), pmulL(M[0][1], M[1][0]))


def trace(M):
    return padd(M[0][0], M[1][1])


def poly_str(p):
    if not p:
        return '0'
    return ' + '.join('x^' + str(e) for e in sorted(p))


def f2_solve_all(A, b):
    """All solutions x of A x = b over F2: returns (x0, nullbasis) or None if inconsistent."""
    A = np.array(A, np.uint8) % 2
    m, n = A.shape
    Aug = np.hstack([A, np.array(b, np.uint8).reshape(m, 1) % 2])
    Rr, piv = f2_rref(Aug)
    if n in piv:
        return None
    x0 = np.zeros(n, np.uint8)
    for row, pc in zip(Rr, piv):
        x0[pc] = row[n]
    N = f2_nullspace(A) if n else np.zeros((0, 0), np.uint8)
    return x0, N


def enumerate_solutions_split(basis, ubatch_bits=16):
    """Second, structurally different exhaustive enumerator: loop over the u-projection (filtered
    by <u,T_t u> = 0), solve the *linear* system <u, T_t w> = delta_t0 for w exactly, then filter
    <w, T_t w> = 0 over the whole affine solution set."""
    d = basis.shape[0]
    if d == 0:
        return []
    # rref with u-columns first
    Rr, piv = f2_rref(basis)
    urows = [r for r, p in zip(Rr, piv) if p < D]
    krows = [r for r, p in zip(Rr, piv) if p >= D]
    Ub = np.array(urows, np.uint8).reshape(len(urows), 2 * D)
    Kb = np.array([r[D:] for r in krows], np.uint8).reshape(len(krows), D)
    dU, dK = Ub.shape[0], Kb.shape[0]
    sols = []
    total = 1 << dU
    step = 1 << min(dU, ubatch_bits)
    for start in range(0, total, step):
        cs = np.arange(start, min(total, start + step))
        C = ((cs[:, None] >> np.arange(dU)[None, :]) & 1).astype(np.uint8)
        V0 = (C @ Ub) & 1
        Uu = V0[:, :D]
        fuu = forms_batch(Uu, Uu)
        good = np.nonzero(~fuu.any(1))[0]
        for i in good:
            u = Uu[i]
            w0 = V0[i, D:]
            uu = np.repeat(u[None, :], max(dK, 1), 0)
            rhs = DELTA0 ^ forms_batch(u[None, :], w0[None, :])[0]
            if dK:
                Lcols = forms_batch(uu, Kb)  # (dK,125): column j = <u, T_t k_j>
                res = f2_solve_all(Lcols.T, rhs)
            else:
                res = (np.zeros(0, np.uint8), np.zeros((0, 0), np.uint8)) if not rhs.any() else None
            if res is None:
                continue
            x0, N = res
            nN = N.shape[0] if N.size else 0
            if nN > 22:
                raise RuntimeError('affine fibre too large: %d' % nN)
            coeffs = ((np.arange(1 << nN)[:, None] >> np.arange(nN)[None, :]) & 1).astype(np.uint8)
            X = (x0[None, :] ^ ((coeffs @ N) & 1)) if nN else x0[None, :]
            Wv = ((X @ Kb) & 1) ^ w0[None, :] if dK else np.repeat(w0[None, :], 1, 0)
            fww = forms_batch(Wv, Wv)
            for j in np.nonzero(~fww.any(1))[0]:
                sols.append(np.concatenate([u, Wv[j]]))
    return sols


def sol_key(s):
    return np.asarray(s, np.uint8).tobytes()
