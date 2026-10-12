"""C5 R4-2 (4): Lemma G for a site stress tensor T^{mu nu}(0) (Sym^2 of the vector rep).

Gamma-invariant real symmetric (= Hermitian, real generators) forms C on Sym^2(R^4) under
g1, Rz, Rx (all in Gamma).  Expected: span{ (tr_G h)^2 , tr(G h G h) } (2-dim, Lorentz).
Then: the cone of positive-semidefinite invariant forms.  Lemma G says the vacuum Gram
matrix of finite-variance site operators T^{mu nu}(0) Omega is such a form; we check that
every psd invariant form vanishes on the traceless (spin-2) part, so T_tl(0) Omega = 0.
Index convention: T^{mu nu} transforms as g T g^T (upper indices); traces use G7 (lower metric).
"""
import sympy as sp
import itertools

G7 = sp.diag(-7, 1, 1, 1)
Gi = G7.inv()


def emb(a, b, c, d, i, j):
    M = sp.eye(4)
    M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d
    return M


g1 = emb(8, 3, 21, 8, 0, 1)
Rz = sp.Matrix([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
Rx = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
# basis of Sym^2: E_ab (a<=b)
pairs = [(a, b) for a in range(4) for b in range(a, 4)]


def basis(a, b):
    E = sp.zeros(4)
    E[a, b] = 1
    E[b, a] = 1
    return E


def vec(S):
    return sp.Matrix([S[a, b] for (a, b) in pairs])


def rep(g):
    # T -> g T g^T on upper-index symmetric tensors
    cols = [vec(g * basis(a, b) * g.T) / (1 if a == b else 1) for (a, b) in pairs]
    # express in coordinates: vec uses S[a,b] which for off-diagonal basis = 1
    M = sp.Matrix.hstack(*cols)
    # correct: coordinates of S in basis {basis(a,b)}: diag coeff = S[a,a]/2? basis(a,a) has 2 on diag
    return M


# use coordinates x_ab with S = sum_{a<=b} x_ab * B_ab, B_aa = diag one, B_ab offdiag sym
def Bm(a, b):
    E = sp.zeros(4)
    E[a, b] = 1
    E[b, a] = 1
    if a == b:
        E[a, a] = 1
    return E


def coords(S):
    return sp.Matrix([S[a, b] for (a, b) in pairs])


def rep2(g):
    return sp.Matrix.hstack(*[coords(g * Bm(a, b) * g.T) for (a, b) in pairs])


gens = [rep2(g) for g in (g1, Rz, Rx)]
n = len(pairs)
cs = sp.symbols(f"c0:{n*n}")
C = sp.Matrix(n, n, cs)
eqs = list(C - C.T)
for M in gens:
    eqs += list(M.T * C * M - C)
sol = sp.solve(eqs, cs, dict=True)[0]
Cg = C.subs(sol)
free = sorted(Cg.free_symbols, key=str)
print("dimension of Gamma-invariant symmetric forms on Sym^2(R^4):", len(free))
# trace functional and traceless subspace
trace = sp.Matrix([[(G7 * Bm(a, b)).trace() for (a, b) in pairs]])
print("trace functional (tr G7 T) in coords:", trace)
tl_basis = (trace).nullspace()
print("dim traceless subspace:", len(tl_basis))
P = sp.Matrix.hstack(*tl_basis)
# restriction of the general invariant form to the traceless subspace
R = sp.simplify(P.T * Cg * P)
# R must be psd for a psd C; show it is (multiple of) an indefinite form for every params
params = free
for vals in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 3)]:
    sub = dict(zip(params, vals))
    ev = [complex(e).real for e in R.subs(sub).evalf().eigenvals(multiple=True)] if R.subs(sub) != sp.zeros(*R.shape) else [0.0]
    print(f"  params {vals}: restriction to traceless part: eig min {min(ev):+.4f}, max {max(ev):+.4f}")
# general: R depends on params only through one combination? find its parameter dependence
Rs = [sp.simplify(sp.diff(R, p)) for p in params]
print("rank of d(restriction)/d(param):", [M.rank() for M in Rs])
print("Is restriction to traceless part of the form (trace)^2 zero?",
      sp.simplify(P.T * (trace.T * trace) * P) == sp.zeros(len(tl_basis)))

print("--- exact inertia check (numpy on exact rational matrices) ---")
import numpy as np
for vals in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 3)]:
    sub = dict(zip(params, vals))
    Rn = np.array(R.subs(sub).evalf(), dtype=float)
    Cn = np.array(Cg.subs(sub).evalf(), dtype=float)
    er = np.linalg.eigvalsh(0.5 * (Rn + Rn.T))
    ec = np.linalg.eigvalsh(0.5 * (Cn + Cn.T))
    tol = 1e-9 * max(1, abs(er).max())
    print(f"  params {vals}: traceless restriction inertia (+,0,-) = "
          f"({(er > tol).sum()},{(abs(er) <= tol).sum()},{(er < -tol).sum()}); "
          f"full form inertia = ({(ec > 1e-9*abs(ec).max()).sum()},"
          f"{(abs(ec) <= 1e-9*abs(ec).max()).sum()},{(ec < -1e-9*abs(ec).max()).sum()})")
# identify the two Lorentz invariants explicitly
def Smat(x):
    S = sp.zeros(4)
    for (a, b), xv in zip(pairs, x):
        S[a, b] = xv
        S[b, a] = xv
    return S
xs = sp.symbols("x0:10")
S = Smat(xs)
trS = (G7 * S).trace()
contr = (G7 * S * G7 * S).trace()
Ctr = sp.hessian(trS**2, xs) / 2
Ccon = sp.hessian(contr, xs) / 2
for name, Cx in [("tr^2", Ctr), ("contraction", Ccon)]:
    inv = all(sp.simplify(M.T * Cx * M - Cx) == sp.zeros(n) for M in gens)
    Rr = np.array((P.T * Cx * P).evalf(), dtype=float)
    er = np.linalg.eigvalsh(0.5 * (Rr + Rr.T))
    tol = 1e-9 * max(1, abs(er).max())
    print(f"  {name}: invariant={inv}; traceless inertia (+,0,-) = "
          f"({(er > tol).sum()},{(abs(er) <= tol).sum()},{(er < -tol).sum()})")
print("Conclusion: an invariant form psd on Sym^2 must have zero contraction coefficient "
      "(contraction is indefinite on the traceless part), so it vanishes on the traceless part.")
