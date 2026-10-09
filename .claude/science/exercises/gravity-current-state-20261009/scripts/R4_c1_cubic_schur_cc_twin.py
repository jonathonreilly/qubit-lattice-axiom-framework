"""C1: cubic decomposition of the constant-metric vacuum energy E(g).

Questions:
 (a) How many independent quadratic invariants on symmetric h (and on traceless h)
     under the 24 proper cubic rotations O, and under SO(3)?  Any trace x traceless mixing?
 (b) Fluid lemma: if E depends on g only through det g, the traceless (TT, q=0)
     Hessian vanishes exactly in the volume-preserving chart g = exp(h), and in the
     linear chart g = 1 + h it equals -(tau/2) tr h^2 (isotropic, proportional to tadpole).
 (c) Chart change exp <-> linear and any SO(3)-scalar term shift the E and T2
     coefficients (unit-Frobenius normalisation) by the SAME amount, so
     delta = mu_E - mu_T is invariant.
 (d) Apply to the refereed K3a'' numbers.
Exact (sympy) where marked; numeric linear algebra for the invariant counts.
"""
import itertools
import numpy as np
import sympy as sp

# ---------- (a) invariant counts ----------
def proper_cubic_group():
    G = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3))
            for i, p in enumerate(perm):
                M[i, p] = signs[i]
            if round(np.linalg.det(M)) == 1:
                G.append(M)
    return G

def sym_basis(traceless):
    B = []
    for i in range(3):
        for j in range(i, 3):
            E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1.0
            B.append(E / np.linalg.norm(E))
    B = np.array(B)  # 6 x 3 x 3 orthonormal (Frobenius)
    if traceless:
        I = np.eye(3) / np.sqrt(3)
        V = np.array([b.flatten() for b in B])
        t = np.array([np.sum(b * I) for b in B])
        # project out identity direction, orthonormalise
        P = V - np.outer(t, I.flatten())
        U, S, Wt = np.linalg.svd(P, full_matrices=False)
        rows = Wt[S > 1e-9]
        B = rows.reshape(-1, 3, 3)
    return B

def rep_matrices(G, B):
    n = len(B)
    mats = []
    for R in G:
        M = np.zeros((n, n))
        for b in range(n):
            img = R @ B[b] @ R.T
            for a in range(n):
                M[a, b] = np.sum(B[a] * img)
        mats.append(M)
    return mats

def count_invariant_forms(mats):
    n = mats[0].shape[0]
    # unknown symmetric Q: constraints M^T Q M - Q = 0
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    rows = []
    for M in mats:
        for (p, q) in idx:
            row = np.zeros(len(idx))
            for k, (i, j) in enumerate(idx):
                Qij = np.zeros((n, n)); Qij[i, j] = Qij[j, i] = 1.0
                row[k] = (M.T @ Qij @ M - Qij)[p, q]
            rows.append(row)
    A = np.array(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9)) + max(0, len(idx) - len(s))

def random_rotations(k, seed=1):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(k):
        Q, R = np.linalg.qr(rng.normal(size=(3, 3)))
        Q = Q @ np.diag(np.sign(np.diag(R)))
        if np.linalg.det(Q) < 0:
            Q[:, 0] *= -1
        out.append(Q)
    return out

O = proper_cubic_group()
print("(a) |O| =", len(O))
for name, G in [("O (24 proper cubic)", O), ("SO(3) (random sample)", random_rotations(12))]:
    for tl in (False, True):
        B = sym_basis(tl)
        n_inv = count_invariant_forms(rep_matrices(G, B))
        print(f"    {name:24s} on {'traceless' if tl else 'all'} Sym(3) (dim {len(B)}): "
              f"{n_inv} invariant quadratic forms")
print("    => O: 3 on Sym(3) = 1 (trace^2) + 2 (traceless); no trace x traceless mixing (3 = 1 + 2).")
print("       SO(3): 2 = 1 (trace^2) + 1 (isotropic shear).")

# ---------- (b) fluid lemma (exact) ----------
e = sp.symbols('epsilon', real=True)
f = sp.Function('f')
a1, a2, b = sp.symbols('a1 a2 b', real=True)
def tt_polarisations():
    PE = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / sp.sqrt(2)       # E channel (axis), |P|_F = 1
    PT = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / sp.sqrt(2)       # T2 channel (face), |P|_F = 1
    return PE, PT
PE, PT = tt_polarisations()
print("\n(b) fluid lemma, E = f(det g):")
for name, P in [("E ", PE), ("T2", PT)]:
    g_exp = (e * P).exp()
    g_lin = sp.eye(3) + e * P
    E_exp = f(sp.simplify(g_exp.det()))
    E_lin = f(sp.expand(g_lin.det()))
    h_exp = sp.simplify(sp.diff(E_exp, e, 2).subs(e, 0))
    h_lin = sp.simplify(sp.diff(E_lin, e, 2).subs(e, 0))
    print(f"    {name}: det(exp(eP)) = {sp.simplify(g_exp.det())};  d2E/de2|0 exp chart = {h_exp};"
          f"  linear chart = {h_lin}")
print("    tadpole: dE/dh_ij at 0 = f'(1) delta_ij  => linear-chart TT Hessian = -tau (unit-Frobenius, d2/de2),"
      " isotropic; zero iff tadpole zero.")

# ---------- (c) chart change and SO(3)-scalar terms shift E and T2 equally ----------
print("\n(c) general cubic E in exp chart: E = tau*tr(h) + 1/2[lam (tr h)^2 + mE*|h_E|^2 + mT*|h_T|^2]")
tau, lam, mE, mT, s = sp.symbols('tau lambda mu_E mu_T s', real=True)
H = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'h{min(i,j)}{max(i,j)}', real=True))
trh = H.trace()
hE2 = sum((H[i, i] - trh / 3) ** 2 for i in range(3))
hT2 = sum(H[i, j] ** 2 for i in range(3) for j in range(3) if i != j)
E_exp_chart = tau * trh + sp.Rational(1, 2) * (lam * trh ** 2 + mE * hE2 + mT * hT2)
# linear chart: g = 1 + k  <=>  h = log(1 + k) = k - k^2/2 + ...
K = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'k{min(i,j)}{max(i,j)}', real=True))
h_of_k = K - K * K / 2
subsd = {H[i, j]: h_of_k[i, j] for i in range(3) for j in range(i, 3)}
E_lin_chart = sp.expand(E_exp_chart.subs(subsd, simultaneous=True))
def hess_along(Eexpr, sym_mat, P):
    sub = {sym_mat[i, j]: e * P[i, j] for i in range(3) for j in range(i, 3)}
    return sp.simplify(sp.diff(Eexpr.subs(sub, simultaneous=True), e, 2).subs(e, 0))
for name, P in [("E ", PE), ("T2", PT)]:
    print(f"    {name}: exp chart d2E = {hess_along(E_exp_chart, H, P)};  linear chart d2E = {hess_along(E_lin_chart, K, P)}")
# an arbitrary SO(3)-scalar term: F(tr g, tr g^2, det g) in exp chart
F = sp.Function('F')
G = (H).exp() if False else None
I1, I2, I3 = sp.symbols('I1 I2 I3')
def scalar_term_hessian(P):
    g = (e * P).exp()
    expr = F(sp.simplify(g.trace()), sp.simplify((g * g).trace()), sp.simplify(g.det()))
    return sp.simplify(sp.diff(expr, e, 2).subs(e, 0))
hsE, hsT = scalar_term_hessian(PE), scalar_term_hessian(PT)
print("    SO(3)-scalar F(tr g, tr g^2, det g): E-Hessian - T2-Hessian =", sp.simplify(hsE - hsT))
print("    => any chart change or rotation-scalar mechanism shifts (mu_E, mu_T) by (c, c); delta = mu_E - mu_T invariant.")

# ---------- (d) refereed numbers ----------
print("\n(d) refereed K3a'' c2/e^2 per cell (TEST_LOG.md:414) and W1 E-block (TEST_LOG.md:488):")
for label, mu_E, mu_T in [("K3a'' natural ", -0.0130346, 0.0124652),
                          ("K3a'' universal", -0.0130346, 0.0133654)]:
    d = mu_E - mu_T
    best = abs(d) / 2
    print(f"    {label}: mu_E={mu_E:+.7f} mu_T={mu_T:+.7f}  delta={d:+.7f}  "
          f"opposite signs={mu_E*mu_T<0};  best common shift leaves max|mu| = {best:.7f}"
          f" (= {best/abs(mu_E):.2f} of |mu_E|)")
print("    No real c zeroes both (signs differ). A trace-only (A1) mechanism shifts neither at zero tadpole"
      " (Schur: no A1 x E or A1 x T2 bilinear under O).")
