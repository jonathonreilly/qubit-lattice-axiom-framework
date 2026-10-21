"""Independent exact check of Prop S4 (4-site collinear segment).  Own construction: integer
structure tensors from kron-embedded matrices, exact row reduction, sympy Groebner (f5b)."""
import itertools, time, numpy as np, sympy as sp
from rv_common import check, total
n = 4
def P(b): return np.diag([1, 0]) if b == 0 else np.diag([0, 1])
sp_ = np.array([[0, 1], [0, 0]]); sm = sp_.T   # sigma+ raises |0>->|1>? (convention irrelevant)
basis, names = [], []
for c in itertools.product((0, 1), repeat=4):
    M = np.zeros((16, 16), dtype=np.int64); i = int("".join(map(str, c)), 2); M[i, i] = 1
    basis.append(M); names.append("D" + "".join(map(str, c)))
for k0, k3 in itertools.product((0, 1), repeat=2):
    basis.append(np.kron(np.kron(P(k0), np.kron(sp_, sm)), P(k3)).astype(np.int64)); names.append(f"a{k0}{k3}")
    basis.append(np.kron(np.kron(P(k0), np.kron(sm, sp_)), P(k3)).astype(np.int64)); names.append(f"b{k0}{k3}")
syms = sp.symbols(names); m = len(basis)
check("24 unknowns (16 diagonal + 8 hop)", m == 24)
monos = [(i, j) for i in range(m) for j in range(i, m)]
rows = []
for t in (1, 2, 3):
    I = np.eye(2**t, dtype=np.int64)
    L = [np.kron(E, I) for E in basis]; R = [np.kron(I, E) for E in basis]
    C = {}
    for i in range(m):
        for j in range(m):
            X = L[i] @ R[j] - R[j] @ L[i]
            if X.any(): C[(i, j)] = X.ravel()
    size = (2**(n+t))**2
    coef = np.zeros((size, len(monos)), dtype=np.int64)
    for col, (i, j) in enumerate(monos):
        v = np.zeros(size, dtype=np.int64)
        if (i, j) in C: v += C[(i, j)]
        if i != j and (j, i) in C: v += C[(j, i)]
        coef[:, col] = v
    nz = coef[np.any(coef != 0, axis=1)]
    rows.extend({tuple(r) for r in nz})
rows = sorted(set(rows)); print("distinct nonzero coefficient rows:", len(rows))
Mrow = sp.Matrix(rows); rref, piv = Mrow.T.rref()   # independent rows = pivot columns of transpose
indep = [rows[p] for p in piv]; print("independent quadratic equations:", len(indep))
eqs = [sp.expand(sum(c * syms[i] * syms[j] for c, (i, j) in zip(r, monos) if c)) for r in indep]
check("equations homogeneous of degree 2", all(sp.Poly(e, *syms).is_homogeneous and sp.Poly(e, *syms).total_degree() == 2 for e in eqs))
for k in ("00", "01", "10", "11"):
    a, b = syms[names.index("a" + k)], syms[names.index("b" + k)]
    t0 = time.time(); G = sp.groebner(eqs + [a * b - 1], *syms, order="grevlex", method="f5b")
    check(f"Groebner(f5b) of commutator ideal + <a{k} b{k} - 1> is [1]", list(G.exprs) == [1], f"{time.time()-t0:.1f}s")
# stronger: even a single non-Hermitian hop is excluded? (informational)
a = syms[names.index("a00")]
G = sp.groebner(eqs + [a - 1], *syms, order="grevlex", method="f5b")
print("informational: ideal + <a00 - 1> Groebner basis length", len(G.exprs), "(1 means even a lone hop is impossible)")
# control: drop t=3 equations? no -- control: diagonal h solves all equations
check("control: all-diagonal assignment (random D, hops 0) solves the system",
      all(sp.simplify(e.subs({s: (np.random.randint(1, 9) if str(s).startswith('D') else 0) for s in syms})) == 0 for e in eqs))
total()
