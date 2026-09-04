"""INDEPENDENT AUDIT of the parallel lane's Block 214 headline claims.
Built from scratch on the b209 D3 conventions; imports nothing of theirs.
CLAIM A: with Gamma_d = eps_d + eps_d^dagger (D3-adjoint), Gamma(q)^2 =
         (q^T g^-1 q) I8.
CLAIM B: the degree-2->1 adjoint carries the factor det(g)/V^2, so full
         closure holds iff V^2 = det(g) — a SELECTOR fixing the volume."""
import sympy as sp
from itertools import combinations
c_tx, c_ty, c_xy, V = sp.symbols("c_tx c_ty c_xy V", positive=False)
g = sp.Matrix([[1, c_tx, c_ty], [c_tx, 1, c_xy], [c_ty, c_xy, 1]])
ginv = sp.together(g.inv()); detg = sp.expand(g.det())
E = sp.diag(1, -1, 1)
# basis: subsets in b209 corner order {}, {0},{1},{2}, {1,2},{0,2},{0,1}, {0,1,2}
BASIS = [(), (0,), (1,), (2,), (1, 2), (0, 2), (0, 1), (0, 1, 2)]
IDX = {b: i for i, b in enumerate(BASIS)}
D3 = sp.zeros(8, 8)
D3[0, 0] = V
for a in range(3):
    for b in range(3):
        D3[IDX[(a,)], IDX[(b,)]] = V * ginv[a, b]
two = [(1, 2), (0, 2), (0, 1)]
W2 = sp.expand(E * g * E) / V
for a in range(3):
    for b in range(3):
        D3[IDX[two[a]], IDX[two[b]]] = W2[a, b]
D3[7, 7] = 1 / V
def eps(d):
    M = sp.zeros(8, 8)
    for S in BASIS:
        if d in S: continue
        T = tuple(sorted(S + (d,)))
        sign = (-1) ** sum(1 for i in S if i < d)
        M[IDX[T], IDX[S]] = sign
    return M
D3inv = sp.together(D3.inv())
q = sp.symbols("q0 q1 q2")
Gamma = sp.zeros(8, 8)
for d in range(3):
    e = eps(d)
    Gamma += q[d] * (e + D3inv * e.T * D3)
Gsq = sp.Matrix(8, 8, lambda i, j: sp.cancel(sp.together(sp.expand((Gamma * Gamma)[i, j]))))
target = sp.cancel(sp.expand((sp.Matrix([q]) * ginv * sp.Matrix([q]).T)[0, 0]))
R = sp.Matrix(8, 8, lambda i, j: sp.cancel(Gsq[i, j] - (target if i == j else 0)))
generic_ok = R.is_zero_matrix
print(f"CLAIM A at GENERIC V (independent of det g): Gamma(q)^2 == (q^T g^-1 q) I8 : {generic_ok}", flush=True)
if not generic_ok:
    nz = [(i, j) for i in range(8) for j in range(8) if R[i, j] != 0]
    print(f"  residual nonzero at {len(nz)} entries; sample factored:", flush=True)
    for i, j in nz[:3]:
        print(f"   [{i},{j}] = {sp.factor(sp.simplify(R[i,j]))}", flush=True)
    # test the selector locus V^2 = det g
    Vsel = sp.sqrt(detg)
    Rsel = sp.Matrix(8, 8, lambda i, j: sp.cancel(sp.simplify(R[i, j].subs(V, Vsel))))
    print(f"CLAIM B: on the locus V = sqrt(det g), residual vanishes identically: {Rsel.is_zero_matrix}", flush=True)
    Rneg = sp.Matrix(8, 8, lambda i, j: sp.cancel(sp.simplify(R[i, j].subs(V, -Vsel))))
    print(f"  (and at V = -sqrt(det g): {Rneg.is_zero_matrix})", flush=True)
    # exhibit the factor det(g)/V^2 in the deg2->1 sector
    e0 = eps(0); adj0 = sp.together(D3inv * e0.T * D3)
    ent = [(i, j) for i in range(8) for j in range(8)
           if len(BASIS[j]) == 2 and len(BASIS[i]) == 1 and adj0[i, j] != 0]
    if ent:
        i, j = ent[0]
        print(f"  deg2->1 adjoint entry [{BASIS[i]}<-{BASIS[j]}] = {sp.factor(sp.simplify(adj0[i,j]))}", flush=True)
        ratio = sp.factor(sp.simplify(adj0[i, j] / (detg / V**2)))
        print(f"    divided by det(g)/V^2 -> {ratio}", flush=True)
