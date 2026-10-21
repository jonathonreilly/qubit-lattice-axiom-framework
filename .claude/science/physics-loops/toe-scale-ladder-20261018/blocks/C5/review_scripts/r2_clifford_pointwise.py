"""Reviewer check of Lemma C: pointwise vanishing of Phi^* tr(theta^3) on S^5, via random points and random
tangent 3-frames (numerical, independent of the worker's sympy routine); existence of C with Gamma_j^T = C Gamma_j C^-1;
S^3 control nonzero; and a Clifford-family member built from a range-1 finite-range unit vector field."""
import sys, itertools, numpy as np
from rlib import S, Ck, EPS
ck = Ck(); rng = np.random.default_rng(11)
k = np.kron
G = [k(S[1],S[0]), k(S[2],S[0]), k(S[3],S[1]), k(S[3],S[2]), k(S[3],S[3])]
ck('Gamma pairwise anticommuting Hermitian involutions',
   all(np.allclose(G[a]@G[b]+G[b]@G[a], 2*np.eye(4)*(a==b)) for a in range(5) for b in range(5)) and all(np.allclose(g,g.conj().T) for g in G))
prod = G[0]@G[1]@G[2]@G[3]@G[4]
print('Gamma1..Gamma5 =', np.round(prod[0,0],12), '* 1 ; transposes product =', np.round((G[0].T@G[1].T@G[2].T@G[3].T@G[4].T)[0,0],12))
# solve C Gamma_j = Gamma_j^T C (linear system) for C
Asys = np.vstack([np.kron(np.eye(4), g.T) - np.kron(g.T, np.eye(4)).T*0 for g in G])
L = np.vstack([np.kron(g.T, np.eye(4)) - np.kron(np.eye(4), g.T) for g in G])  # vec(C g) - vec(g^T C) with column-major? use brute force below
def resid(Cv):
    C = Cv.reshape(4,4); return np.concatenate([(C@g - g.T@C).ravel() for g in G])
Mlin = np.array([resid(e) for e in np.eye(16)]).T
_, sv, vh = np.linalg.svd(Mlin)
C = vh[-1].conj().reshape(4,4)
print('smallest singular values of C-system:', np.round(sv[-3:],12))
ck('nullspace of {C Gamma_j = Gamma_j^T C} is 1-dimensional and C invertible (=> Phi^T = C Phi C^-1)',
   sv[-1] < 1e-12 and sv[-2] > 1e-6 and abs(np.linalg.det(C)) > 1e-6 and np.allclose(C@G[2]@np.linalg.inv(C), G[2].T))
def Phi(x, gam): return x[0]*np.eye(gam[0].shape[0]) + 1j*sum(x[j+1]*gam[j] for j in range(len(gam)))
def form(x, tang, gam):
    U = Phi(x, gam); Ui = np.linalg.inv(U)
    A = [Ui @ (1j*sum(t[j+1]*gam[j] for j in range(len(gam))) + t[0]*np.eye(U.shape[0])) for t in tang]
    return sum(s*np.trace(A[a]@A[b]@A[c]) for (a,b,c),s in EPS)
mx = 0
for _ in range(2000):
    x = rng.normal(size=6); x /= np.linalg.norm(x)
    T = rng.normal(size=(3,6)); T -= np.outer(T@x, x)
    mx = max(mx, abs(form(x, T, G)))
ck(f'S^5: max |tr(theta^3)(t1,t2,t3)| over 2000 random points/frames = {mx:.1e} < 1e-12', mx < 1e-12)
# also off the sphere (scale invariance): x not unit
mx2 = max(abs(form(rng.normal(size=6)*3, rng.normal(size=(3,6)), G)) for _ in range(500))
ck(f'R^6\\0 (unnormalised, arbitrary tangent vectors): max = {mx2:.1e} < 1e-11', mx2 < 1e-11)
mn = min(abs(form((lambda y: y/np.linalg.norm(y))(rng.normal(size=4)), (lambda T: T)(rng.normal(size=(3,4))), S[1:])) for _ in range(200))
vals = [abs(form((lambda y: y/np.linalg.norm(y))(rng.normal(size=4)), rng.normal(size=(3,4)), S[1:])) for _ in range(200)]
ck(f'control S^3 -> SU(2): form nonzero at random points (median {np.median(vals):.2f})', np.median(vals) > 1e-2)
sys.exit(ck.total())
