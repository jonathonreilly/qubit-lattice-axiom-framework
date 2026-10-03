"""Construct M = 1 + P N0 adj(P), N0=[[0,1],[1,Delta]]; verify det=1, equivariance, trace; convert to z; growth of M^t."""
import sympy as sp
from wsym import construct, equivariant, Mz, P2, W
from cliff_poly import mmul, radius, trace, is_identity

D = sp.Symbol("D")
M, Delta = construct([[sp.Integer(0), sp.Integer(1)], [sp.Integer(1), D]])
det = M[0][0] * M[1][1] + M[0][1] * M[1][0]
print("Delta =", Delta.as_expr())
print("det M == 1 :", (det - P2(1)).is_zero)
tr = M[0][0] + M[1][1]
print("trace M nonzero:", not tr.is_zero, "; equals Delta^2:", (tr - Delta * Delta).is_zero)
print("S3-equivariant:", equivariant(M))
print("w-degrees per entry:", [[M[i][j].degree_list() if not M[i][j].is_zero else None for j in range(2)] for i in range(2)])
Z = Mz(M)
print("z-range (max |v|_inf):", radius(Z), " support sizes:", [len(Z[i][j]) for i in range(2) for j in range(2)])
Pw = Z
for t in range(1, 7):
    print(f"  t={t}: radius(M^t)={radius(Pw)}  identity={is_identity(Pw)}")
    Pw = mmul(Pw, Z)
import pickle
pickle.dump(Z, open("Mz_transport.pkl", "wb"))
