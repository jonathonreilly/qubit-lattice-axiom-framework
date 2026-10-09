"""B1 check c2: which symmetries can forbid a graviton mass term?

(a) Count independent quadratic invariants ("mass terms") M(h,h) on symmetric tensors h under
    point groups (finite: Reynolds average; Lie: null space of generators), on all of Sym^2 and on
    the 3D traceless (TT-type) subspace.
(b) Show linearized gauge invariance (delta h = q xi + xi q) forces every local mass form to 0.
(c) Fluid lemma: E(g)=f(det g) has zero TT Hessian; a cubic-solid E does not.
"""
import itertools, numpy as np, sympy as sp

def sym_basis(n):
    B = []
    for i in range(n):
        for j in range(i, n):
            E = np.zeros((n, n)); E[i, j] = E[j, i] = 1.0 if i != j else 1.0
            B.append(E / np.linalg.norm(E))
    return B

def rep_on(B, R, lower=True):
    # action h -> R h R^T  (for Lorentz with lower indices use R^{-T} h R^{-1}; passed in already)
    N = len(B); M = np.zeros((N, N))
    for b, E in enumerate(B):
        F = R @ E @ R.T
        for a, G in enumerate(B):
            M[a, b] = np.sum(G * F)
    return M

def count_invariant_forms_finite(B, group):
    N = len(B)
    # invariant symmetric bilinear forms: average of rho^T X rho over group, dimension = rank of Reynolds on Sym(N)
    SB = sym_basis(N)
    P = np.zeros((len(SB), len(SB)))
    for R in group:
        rho = rep_on(B, R)
        for b, X in enumerate(SB):
            Y = rho.T @ X @ rho
            for a, Z in enumerate(SB):
                P[a, b] += np.sum(Z * Y)
    P /= len(group)
    return int(round(np.trace(P)))  # trace of projector = dim of invariant subspace

def count_invariant_forms_lie(B, gens):
    N = len(B); SB = sym_basis(N)
    rows = []
    for T in gens:
        # infinitesimal action on h: delta h = T h + h T^T
        d = np.zeros((N, N))
        for b, E in enumerate(B):
            F = T @ E + E @ T.T
            for a, G in enumerate(B):
                d[a, b] = np.sum(G * F)
        # invariance of X: d^T X + X d = 0
        L = np.zeros((len(SB) * 1, len(SB)))
        cols = []
        for X in SB:
            Y = d.T @ X + X @ d
            cols.append(np.concatenate([Y[np.triu_indices(N)]]))
        rows.append(np.array(cols).T)
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return len(SB) - int(np.sum(s > 1e-9))

def signed_perms(n, proper=None):
    G = []
    for p in itertools.permutations(range(n)):
        for s in itertools.product([1, -1], repeat=n):
            R = np.zeros((n, n))
            for i in range(n): R[i, p[i]] = s[i]
            if proper is None or round(np.linalg.det(R)) == proper: G.append(R)
    return G

def icosahedral():
    phi = (1 + 5 ** 0.5) / 2
    def rot(axis, ang):
        a = np.array(axis, float); a /= np.linalg.norm(a)
        K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
        return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K
    gens = [rot([0, 1, phi], 2 * np.pi / 5), rot([1, 1, 1], 2 * np.pi / 3)]
    G = [np.eye(3)]
    changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                k = g @ h
                if not any(np.allclose(k, x, atol=1e-9) for x in G):
                    G.append(k); changed = True
    return G

def so_gens(n, eta=None):
    gens = []
    for i in range(n):
        for j in range(i + 1, n):
            T = np.zeros((n, n)); T[i, j] = 1; T[j, i] = -1
            if eta is not None:  # Lorentz generators: T = J eta with antisymmetric J
                T = T @ eta
            gens.append(T)
    return gens

B3 = sym_basis(3); B4 = sym_basis(4)
# traceless 3D basis (5-dim)
T3 = []
for E in B3:
    F = E - np.trace(E) / 3 * np.eye(3)
    if np.linalg.norm(F) > 1e-12: T3.append(F)
# orthonormalise
M = np.array([F.ravel() for F in T3]); Q, R = np.linalg.qr(M.T); r = np.sum(np.abs(np.diag(R)) > 1e-9)
TT = [Q[:, k].reshape(3, 3) for k in range(r)]
print(f"traceless subspace dim = {len(TT)}")

Oh = signed_perms(3, proper=1); Ico = icosahedral(); WB4 = signed_perms(4)
print(f"|O (proper cubic)| = {len(Oh)}, |I (icosahedral)| = {len(Ico)}, |W(B4)| = {len(WB4)}")
eta = np.diag([-1.0, 1, 1, 1])
res = {
  "SO(3) on Sym2(R3)": count_invariant_forms_lie(B3, so_gens(3)),
  "O proper cubic (24) on Sym2(R3)": count_invariant_forms_finite(B3, Oh),
  "I icosahedral (60) on Sym2(R3)": count_invariant_forms_finite(B3, Ico),
  "SO(3) on traceless (5)": count_invariant_forms_lie(TT, so_gens(3)),
  "O proper cubic on traceless (5)": count_invariant_forms_finite(TT, Oh),
  "I icosahedral on traceless (5)": count_invariant_forms_finite(TT, Ico),
  "SO(4) on Sym2(R4)": count_invariant_forms_lie(B4, so_gens(4)),
  "W(B4) hypercubic (384) on Sym2(R4)": count_invariant_forms_finite(B4, WB4),
  "SO(3,1) Lorentz on Sym2(R4)": count_invariant_forms_lie(B4, so_gens(4, eta)),
}
for k, v in res.items(): print(f"  {k:40s}: {v} independent mass invariants")
print("  -> no rotation/Lorentz/point group gives 0: tr(h^2) is invariant under every orthogonal group.")

# (b) gauge invariance kills every mass form: the gauge directions q xi + xi q span all of Sym2 as q,xi vary
n = 4; span = []
rng = np.random.default_rng(1)
for _ in range(40):
    q = rng.normal(size=n); xi = rng.normal(size=n)
    span.append((np.outer(q, xi) + np.outer(xi, q))[np.triu_indices(n)])
print(f"(b) rank of span{{q xi + xi q}} = {np.linalg.matrix_rank(np.array(span))} of {n*(n+1)//2}"
      " -> M(h, delta h) = 0 for all h, delta h forces M = 0 (local mass forms are never gauge invariant)")

# (c) fluid lemma
t = sp.symbols('t'); f = sp.Function('f')
h = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])   # E_g traceless
h2 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])   # T_2g traceless
for name, hh in [("E_g", h), ("T_2g", h2)]:
    g = (t * hh).exp()
    Ef = f(g.det())
    Es = sum(g[i, i] ** 2 for i in range(3))           # an O_h-invariant 'solid' energy
    Es2 = (g * g).trace()                              # a rotation-scalar term
    print(f"(c) {name}: d2/dt2 f(det g)|0 = {sp.simplify(sp.diff(Ef, t, 2).subs(t, 0))}; "
          f"cubic solid sum g_ii^2: {sp.simplify(sp.diff(Es, t, 2).subs(t, 0))}; "
          f"tr g^2: {sp.simplify(sp.diff(Es2, t, 2).subs(t, 0))}")
