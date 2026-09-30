"""Kill check T49: independent matrix-level verification of the attack's massive invariants.
For each candidate Delta (from the attack's all_invariants), check U Delta U^T == Delta for every generator of the reduced
group AND for the full-group generators (tx,ty,tz), where U[perm[v],v]=s_v. Also check hopping invariance of U, and antisymmetry."""
import sys, numpy as np
sys.argv = ['x', '8']
exec(open('massive_bdg.py').read().split('h = np.zeros((N, N))')[0])
Hop = np.zeros((N, N))
for (i, j), e in hop.items(): Hop[i, j] = e
eps = np.array([(-1) ** (sum(coords(i))) for i in range(N)], dtype=float)
def U_of(g):
    perm, s = g
    U = np.zeros((N, N)); U[perm, np.arange(N)] = s
    return U
allg = dict(gens); allg.update(mg)
for name, g in allg.items():
    U = U_of(g)
    assert np.allclose(U @ Hop @ U.T, Hop), name           # hopping invariant
    inv_eps = np.allclose(U @ np.diag(eps) @ U.T, np.diag(eps))
    flip_eps = np.allclose(U @ np.diag(eps) @ U.T, -np.diag(eps))
    print(f"generator {name:5s}: hop-invariant; mass term {'kept' if inv_eps else ('reversed' if flip_eps else '???')}")
for d in [(1,0,0),(1,1,1),(3,1,1),(3,1,0)]:
    for ci, val in enumerate(all_invariants(d)):
        Dl = np.zeros((N, N))
        for (i, j), x in val.items(): Dl[i, j] = x; Dl[j, i] = -x
        red = all(np.allclose(U_of(g) @ Dl @ U_of(g).T, Dl) for g in mg.values())
        full = all(np.allclose(U_of(gens[k]) @ Dl @ U_of(gens[k]).T, Dl) for k in ["tx", "ty", "tz", "c4z", "c4x", "c3"])
        print(f"d={d} inv#{ci}: antisym={np.allclose(Dl, -Dl.T)}, invariant under reduced group={red}, under FULL group (incl. one-step translations)={full}, nnz={int((Dl!=0).sum())}")
