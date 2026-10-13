"""R17-4 (a), structure: the P,T-even degree-2 on-shell TT space under O_h.
A general O_h-invariant form X(n,e) = e_ij e_kl n_m n_n T_{ijkl,mn} (T symmetric in (ij),(kl),(ij)<->(kl),(mn)).
Functionals: axis (001) Eg = diag(1,-1,0), T2g = xy+yx; face (110) e1 = aa-bb, e2 = ab+ba (a=(1,-1,0)/r2, b=z);
body (111) e1, e2 (a=(1,-1,0)/r2, b=(1,1,-2)/r6). All normalized e:e = 2.
Find the rank of the map T -> (functionals over all n, e) and the linear relation among the 5 named functionals."""
import numpy as np, itertools
rng = np.random.default_rng(1)
# the 48 elements of O_h as signed permutation matrices
G = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3))
        for i in range(3): M[i, p[i]] = s[i]
        G.append(M)
def sym_inv(T):
    # symmetrize over index symmetries and average over O_h
    T = (T + T.transpose(1,0,2,3,4,5))/2; T = (T + T.transpose(0,1,3,2,4,5))/2
    T = (T + T.transpose(2,3,0,1,4,5))/2; T = (T + T.transpose(0,1,2,3,5,4))/2
    out = np.zeros_like(T)
    for R in G: out += np.einsum('ia,jb,kc,ld,me,nf,abcdef->ijklmn', R, R, R, R, R, R, T)
    return out/len(G)
def tt_pols(n):
    n = n/np.linalg.norm(n)
    a = np.cross(n, [0.3, 0.7, 0.2]); a /= np.linalg.norm(a); b = np.cross(n, a)
    return n, [np.outer(a,a)-np.outer(b,b), np.outer(a,b)+np.outer(b,a)]
def X(T, n, e): return np.einsum('ij,kl,m,n,ijklmn->', e, e, n, n, T)
r2, r3, r6 = np.sqrt(2), np.sqrt(3), np.sqrt(6)
z = np.array([0,0,1.]); fd = np.array([1,1,0])/r2; bd = np.array([1,1,1])/r3
Eg = np.diag([1., -1, 0]); T2 = np.zeros((3,3)); T2[0,1] = T2[1,0] = 1
a = np.array([1,-1,0])/r2; bz = z; bb = np.array([1,1,-2])/r6
F1 = np.outer(a,a)-np.outer(bz,bz); F2 = np.outer(a,bz)+np.outer(bz,a)
B1 = np.outer(a,a)-np.outer(bb,bb); B2 = np.outer(a,bb)+np.outer(bb,a)
named = [(z, Eg), (z, T2), (fd, F1), (fd, F2), (bd, B1), (bd, B2)]
for (n, e) in named: assert abs(np.einsum('ij,j->i', e, n)).max() < 1e-12 and abs(np.trace(e)) < 1e-12 and abs((e*e).sum()-2) < 1e-12
rows, full = [], []
dirs = [rng.normal(size=3) for _ in range(12)]
for _ in range(14):
    T = sym_inv(rng.normal(size=(3,)*6))
    rows.append([X(T, n, e) for (n, e) in named] + [X(T, fd, (F1+F2)/r2) - (X(T, fd, F1)+X(T, fd, F2))/2])
    vals = []
    for d in dirs:
        n, (p1, p2) = tt_pols(d)
        vals += [X(T, n, p1), X(T, n, p2), X(T, n, (p1+p2)/r2)]
    full.append(vals)
R = np.array(rows); Fm = np.array(full)
print('rank of full on-shell TT map over random directions/pols (P,T-even, O_h):', np.linalg.matrix_rank(Fm, tol=1e-9*np.abs(Fm).max()))
print('rank of the 5 named functionals [Eg, T2g, face1, face2, body]:', np.linalg.matrix_rank(R[:, :5], tol=1e-9*np.abs(R).max()))
print('face off-diagonal (mixing) max |.|:', np.abs(R[:, 6]).max(), ' body e1 - e2 max |.|:', np.abs(R[:, 4]-R[:, 5]).max())
u, s, vt = np.linalg.svd(R[:, :5]); nv = vt[-1]/vt[-1][np.argmax(np.abs(vt[-1]))]
print('singular values:', s)
print('null relation coefficients on [Eg, T2g, face1, face2, body]:', np.round(nv, 10))
# check with rational guess
for cand in [np.array([1, 2, -2, 2, -3])]:
    print('candidate', cand, 'residual', np.abs(R[:, :5] @ cand).max())
