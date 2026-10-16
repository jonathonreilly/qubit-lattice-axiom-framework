"""Exact setup: groups, covariant subspace (Pauli basis), unitarity equations.
A_n = sum_mu a[n][mu] sigma_mu, mu=0..3 (sigma_0 = I).
Conjugation by D(R) acts as (1 (+) R) on (a0, a1, a2, a3): rational, no sign issue.
"""
import itertools, sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]]); SY = sp.Matrix([[0, -sp.I], [sp.I, 0]]); SZ = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, SX, SY, SZ]
NBR = list(itertools.product([-1, 0, 1], repeat=3))
IDX = {n: i for i, n in enumerate(NBR)}

def all_O():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = sp.zeros(3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if M.det() == 1:
                out.append(M)
    return out

def closure(gens):
    G = [sp.eye(3)]
    frontier = [sp.eye(3)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                x = h * g
                if x not in G:
                    G.append(x); new.append(x)
        frontier = new
    return G

Cyc = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])      # e_x->e_y->e_z->e_x
Hz = sp.diag(-1, -1, 1)
Qz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])      # quarter turn about z
Hx = sp.diag(1, -1, -1)
GROUPS = {
    'O': all_O(),
    'T': closure([Cyc, Hz]),
    'D4': closure([Qz, Hx]),
}

def D_of(R):
    """SU(2) lift (exact) via axis-angle; used only for an independent check."""
    tr = R.trace(); c = (tr - 1) / 2
    th = sp.acos(c)
    if sp.simplify(th) == 0:
        return sp.eye(2)
    if sp.simplify(th - sp.pi) == 0:
        # axis from (R+I)/2 = u u^T
        S = (R + sp.eye(3)) / 2
        j = max(range(3), key=lambda i: S[i, i])
        u = sp.Matrix([S[i, j] for i in range(3)]) / sp.sqrt(S[j, j])
    else:
        u = sp.Matrix([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * sp.sin(th))
    return sp.simplify(sp.cos(th / 2) * I2 - sp.I * sp.sin(th / 2) * (u[0] * SX + u[1] * SY + u[2] * SZ))

def covariant_basis(G):
    """Exact basis of covariant coefficient vectors a (27*4 complex) with
    a_{Rn} = (1+R) a_n for all R in G. Equations are real-rational, so the
    complex solution space is the complexification of a rational nullspace."""
    nv = 27 * 4
    rows = []
    for R in G:
        big = sp.diag(1, R)
        for n in NBR:
            Rn = tuple(R * sp.Matrix(n))
            for mu in range(4):
                row = [0] * nv
                row[4 * IDX[Rn] + mu] += 1
                for nu in range(4):
                    row[4 * IDX[n] + nu] -= big[mu, nu]
                rows.append(row)
    M = sp.Matrix(rows)
    return M.nullspace()

def build(G, name='c'):
    basis = covariant_basis(G)
    m = len(basis)
    z = sp.symbols(f'{name}0:{m}')
    vec = sum((z[j] * basis[j] for j in range(m)), sp.zeros(27 * 4, 1))
    A = {n: sum((vec[4 * IDX[n] + mu] * SIG[mu] for mu in range(4)), sp.zeros(2)) for n in NBR}
    return basis, z, A

def conjA(A, z, zb):
    """A^dagger with conj(z_j) replaced by independent symbol zb_j (coeffs are Gaussian rationals)."""
    sub = dict(zip(z, zb))
    return {n: (A[n].T).applyfunc(lambda e: sp.expand(sp.conjugate(e).subs({sp.conjugate(v): sub[v] for v in z}))) for n in A}

def unitarity_eqs(A, Ad):
    """sum_n A_n A_{n-d}^dag = delta_{d0} I for all d in {-2..2}^3 (entries)."""
    eqs = []
    for d in itertools.product(range(-2, 3), repeat=3):
        S = sp.zeros(2)
        for n in NBR:
            m = (n[0] - d[0], n[1] - d[1], n[2] - d[2])
            if m in IDX:
                S += A[n] * Ad[m]
        if d == (0, 0, 0):
            S -= I2
        for e in S:
            e = sp.expand(e)
            if e != 0:
                eqs.append(e)
    return eqs
