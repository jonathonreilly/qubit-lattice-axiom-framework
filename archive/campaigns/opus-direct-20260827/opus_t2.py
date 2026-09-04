"""T1b (d=4, the physical dimension) + T1c (Kahler-Dirac identification)
 + T2 (the dispersion), all exact."""
import sympy as sp
from itertools import combinations

def basis(d):
    out = []
    for k in range(d + 1):
        out += [tuple(c) for c in combinations(range(d), k)]
    return out
def lam(ginv, I, J):
    if len(I) == 0: return sp.Integer(1)
    return sp.Matrix(len(I), len(I), lambda a, b: ginv[I[a], J[b]]).det()
def carrier(d, g, rho):
    B = basis(d); n = len(B); idx = {b: i for i, b in enumerate(B)}
    ginv = sp.together(g.inv())
    D = sp.zeros(n, n)
    for I in B:
        for J in B:
            if len(I) == len(J):
                D[idx[I], idx[J]] = sp.cancel(rho[len(I)] * lam(ginv, I, J))
    def eps(a):
        M = sp.zeros(n, n)
        for S in B:
            if a in S: continue
            T = tuple(sorted(S + (a,)))
            M[idx[T], idx[S]] = (-1) ** sum(1 for i in S if i < a)
        return M
    return B, idx, D, ginv, eps

# ---- T1b: d = 4, does 'all rho equal' still fall out?
print("=== T1b  d = 4 (physical dimension)", flush=True)
a1, a2, a3, off = sp.symbols("a1 a2 a3 w")
g4 = sp.diag(1, a1, a2, a3); g4[0, 1] = off; g4[1, 0] = off   # one shear, rest diagonal
rho4 = sp.symbols("r0:5", positive=True)
B, idx, D4, gi4, eps4 = carrier(4, g4, rho4)
D4inv = sp.together(D4.inv())
G = [sp.Matrix(sp.expand(eps4(a) + D4inv * eps4(a).T * D4)) for a in range(4)]
facs = set()
n = len(B)
for a in range(4):
    for b in range(a, 4):
        AC = sp.expand(G[a] * G[b] + G[b] * G[a])
        tgt = sp.expand(2 * gi4[a, b] * sp.eye(n))
        for i in range(n):
            for j in range(n):
                r = sp.cancel(sp.together(AC[i, j] - tgt[i, j]))
                if r != 0:
                    for f, _ in sp.factor_list(sp.numer(r))[1]:
                        if f.free_symbols & set(rho4):
                            facs.add(sp.expand(f))
print(f"  rho-conditions in d=4: {sorted({str(f) for f in facs})}", flush=True)
uniform = {rho4[k]: rho4[0] for k in range(5)}
resid = {sp.simplify(f.subs(uniform)) for f in facs}
print(f"  all-equal rho kills every condition: {resid == {sp.Integer(0)} or resid == set()}", flush=True)

# ---- T1c: at uniform rho the adjoint IS the interior product (Kahler-Dirac)
print("\n=== T1c  the uniform carrier is the Kahler-Dirac structure", flush=True)
ctx, cty, cxy = sp.symbols("c_tx c_ty c_xy"); V = sp.Symbol("V", positive=True)
g3 = sp.Matrix([[1, ctx, cty], [ctx, 1, cxy], [cty, cxy, 1]])
r = [V] * 4
B3, idx3, D3u, gi3, eps3 = carrier(3, g3, r)
D3inv = sp.together(D3u.inv())
def iota(a):  # interior product with the vector g^-1 e_a
    M = sp.zeros(8, 8)
    for S in B3:
        for pos, i in enumerate(S):
            T = tuple(x for x in S if x != i)
            M[idx3[T], idx3[S]] += (-1) ** pos * gi3[a, i]
    return M
ok = all(sp.expand(D3inv * eps3(a).T * D3u - iota(a)).is_zero_matrix for a in range(3))
print(f"  eps_a^dagger == iota_{{g^-1 e_a}} exactly, all a: {ok}", flush=True)

# ---- T2: the dispersion, exactly, on the selector curve in d = 2
print("\n=== T2  the dispersion", flush=True)
c = sp.Rational(3, 5); v = sp.Rational(4, 5)      # v^2 = 1 - c^2 : on the selector curve
g2 = sp.Matrix([[1, c], [c, 1]])
print(f"  d=2 point c={c}, v={v};  v^2 - det g = {sp.simplify(v**2 - g2.det())}", flush=True)
B2, idx2, D2, gi2, eps2 = carrier(2, g2, [v] * 3)
D2inv = D2.inv()
Gam = [sp.Matrix(sp.expand(eps2(a) + D2inv * eps2(a).T * D2)) for a in range(2)]
L = 4
N = L * L
def site(x, y): return (x % L) * L + (y % L)
def shift(axis, s):
    M = sp.zeros(N, N)
    for x in range(L):
        for y in range(L):
            tx, ty = (x + s, y) if axis == 0 else (x, y + s)
            M[site(tx, ty), site(x, y)] = 1
    return M
nab = [sp.Rational(1, 2) * (shift(a, 1) - shift(a, -1)) for a in range(2)]
kron = lambda A, B_: sp.Matrix(sp.kronecker_product(A, B_))
K = sum((kron(Gam[a], nab[a]) for a in range(2)), sp.zeros(4 * N, 4 * N))
K2 = sp.expand(K * K)
Lap = sum((sp.expand(gi2[a, b] * nab[a] * nab[b]) for a in range(2) for b in range(2)),
          sp.zeros(N, N))
claim = kron(sp.eye(4), Lap)
print(f"  K^2 == (Laplace-Beltrami) (x) I_fiber  exactly: {sp.expand(K2 - claim).is_zero_matrix}", flush=True)
m = sp.Symbol("m", positive=True)
Dop = m * sp.eye(4 * N) + K
Dfull = kron(D2, sp.eye(N))
adj = sp.expand(Dfull.inv() * Dop.T * Dfull)
DdD = sp.expand(adj * Dop)
pred = sp.expand(m**2 * sp.eye(4 * N) - K2)
print(f"  D^dagger D == m^2 - K^2  exactly: {sp.expand(DdD - pred).is_zero_matrix}", flush=True)
ev = (-Lap).eigenvals()
pred_vals = {}
for nx in range(L):
    for ny in range(L):
        s = sp.Matrix([sp.sin(2 * sp.pi * nx / L), sp.sin(2 * sp.pi * ny / L)])
        val = sp.nsimplify(sp.simplify((s.T * gi2 * s)[0, 0]))
        pred_vals[val] = pred_vals.get(val, 0) + 1
got = {sp.nsimplify(sp.simplify(k)): v_ for k, v_ in ev.items()}
print(f"  spectrum of -K^2 (per fiber) == {{ sin(k)^T g^-1 sin(k) }} with multiplicities: {got == pred_vals}", flush=True)
print(f"    values/mult: {sorted((str(k), v_) for k, v_ in got.items())}", flush=True)
