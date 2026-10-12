"""C5 R5-4 (1): Lemma N. Timelike links of L7 carry finite, Gamma x L7-covariant neighbourhoods.

Q7(n) = -7 n0^2 + n1^2 + n2^2 + n3^2 (lattice coords), bilinear B = G7.
For a future-timelike link vector d, E_d(z) = 2 B(d,z)^2 / (-Q(d)) + Q(z) is the rest-frame
Euclidean norm of z in the frame u = d/sqrt(-Q(d)); it is positive definite and E_{g d}(g z) = E_d(z).
Neighbourhood of the link (x, d):
   N_R(x,d) = {(x+a, d') : E_d(a) <= R^2, Q(d') = Q(d), d'_0 > 0, E_d(d'-d) <= R^2}.
Checks (exact integers): |N_R(0, g d)| = |N_R(0, d)| and g N_R(0,d) = N_R(0, g d) as sets, with N_R(0, g d)
enumerated independently (bounding box of the ellipsoid E_{gd} <= R^2), for several g in Gamma.
"""
import itertools, numpy as np
G7 = np.diag([-7, 1, 1, 1])
def emb(a, b, c, d, i, j):
    M = np.eye(4, dtype=np.int64); M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d; return M
B1, B2, B3 = emb(8, 3, 21, 8, 0, 1), emb(8, 3, 21, 8, 0, 2), emb(8, 3, 21, 8, 0, 3)
B1i, B2i = emb(8, -3, -21, 8, 0, 1), emb(8, -3, -21, 8, 0, 2)
R = np.array([[1,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,1]], dtype=np.int64)  # cubic rotation about n3
def inG(M): return (M.T @ G7 @ M == G7).all() and round(np.linalg.det(M)) == 1 and M[0,0] > 0
gs = {"B1": B1, "B2^-1": B2i, "B1 R B2^-1": B1 @ R @ B2i, "B3 B1": B3 @ B1, "R B2 R": R @ B2 @ R}
for k, g in gs.items(): assert inG(g), k
def Q(z): return -7*z[...,0]**2 + z[...,1]**2 + z[...,2]**2 + z[...,3]**2
def Bf(y, z): return -7*y[...,0]*z[...,0] + y[...,1]*z[...,1] + y[...,2]*z[...,2] + y[...,3]*z[...,3]
def ball(d, R2):
    """all integer z with E_d(z) <= R2 (exact integer test: 2 B(d,z)^2 + Q(z)(-Q(d)) <= R2 (-Q(d)))."""
    qd = -int(Q(np.array(d)))
    M = 2*np.outer(G7 @ d, G7 @ d)/qd + G7          # E_d(z) = z^T M z
    Minv = np.linalg.inv(M.astype(float))
    h = [int(np.floor(np.sqrt(R2*Minv[i,i]) + 1e-9)) for i in range(4)]
    axes = [np.arange(-hi, hi+1, dtype=np.int64) for hi in h]
    Z = np.stack(np.meshgrid(*axes, indexing="ij"), -1).reshape(-1, 4)
    dd = np.array(d, dtype=np.int64)
    val = 2*Bf(Z, dd[None, :])**2 + Q(Z)*qd
    return Z[val <= R2*qd], h
def nbhd(d, R2):
    Z, h = ball(d, R2); dd = np.array(d, dtype=np.int64)
    Dp = dd[None, :] + Z
    Dp = Dp[(Q(Dp) == Q(dd)) & (Dp[:, 0] > 0)]
    return {(tuple(a), tuple(b)) for a in Z for b in Dp}, len(Z), len(Dp), h
R2 = 6
d0 = np.array([1, 0, 0, 0], dtype=np.int64)
N0, nz0, nd0, h0 = nbhd(d0, R2)
print(f"R^2 = {R2}; base link d0 = e0: |ball| = {nz0}, #d' = {nd0}, |N_R| = {len(N0)} (box half-widths {h0})")
for name, g in gs.items():
    d = g @ d0
    N, nz, nd, h = nbhd(d, R2)
    img = {(tuple(g @ np.array(a)), tuple(g @ np.array(b))) for a, b in N0}
    print(f"g = {name:12s} d = g e0 = {tuple(int(x) for x in d)}  Q = {int(Q(d))}  box {h}: |ball| = {nz}, #d' = {nd}, |N_R| = {len(N)}, g N(e0) == N(g e0): {img == N}")
d1 = np.array([2, 4, 2, 1], dtype=np.int64)   # another Q = -7 vector
N1, nz1, nd1, h1 = nbhd(d1, R2)
print(f"d1 = (2,4,2,1), Q = {int(Q(d1))}: |ball| = {nz1}, #d' = {nd1}, |N_R| = {len(N1)}")
