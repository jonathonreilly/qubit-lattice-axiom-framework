"""T03 Test 1e: sign of J.  Possibility covariance leaves H = J sum sigma.sigma (dynamics-clause note, 2026-09-24).
J > 0 (antiferro): unique entangled ground state, lock costs 3.213 J (test 1).  J < 0 (ferro): degenerate ground manifold (S = 4, 9 states).
Pre-registered here (before running): (i) fully polarised state, lock along its axis: cost 0 exactly;
(ii) same state, lock along a perpendicular axis: cost > 0; (iii) M = 0 member of the multiplet, lock along z: cost > 0;
(iv) equal mixture of the 9 ground states, lock along z: cost > 0.  So the cost is not forced by covariance: it depends on the sign of J
and on WHICH ground state history supplied (realized-state primitive).
"""
import numpy as np, sys
sys.argv=['x']
exec(open('t03_test1_cost.py').read().split('# ---------------------------------------------------------------- 1a')[0].replace('J = 1.0','J = -1.0'))
# after exec: H is the ferro cube, SX/SY/SZ, Pup/Pdn defined below in the original; rebuild projectors here
d = 2**NS
Pup=[(np.eye(d)+SZ[s])/2 for s in range(NS)]; Pdn=[(np.eye(d)-SZ[s])/2 for s in range(NS)]
w, V = np.linalg.eigh(H)
deg = int((abs(w - w[0]) < 1e-9).sum())
print(f"ferro cube: E0 = {w[0]:.6f}, ground degeneracy = {deg}")
x = 0
def lock_cost(psi, axis):
    A = {'z': SZ[x], 'x': SX[x], 'y': SY[x]}[axis]
    Pp = (np.eye(d) + A) / 2; Pm = (np.eye(d) - A) / 2
    r = np.outer(psi, psi.conj()); r2 = Pp @ r @ Pp + Pm @ r @ Pm
    return (np.trace(r2 @ H) - np.trace(r @ H)).real
up = np.zeros(d, complex); up[0] = 1.0             # |up...up>, index 0 = all bits 0 = sigma_z=+1 on every site (kron ordering)
print("check |up^8> is a ground state:", abs((up.conj() @ H @ up).real - w[0]) < 1e-9)
Sz = sum(SZ) / 2
G = V[:, :deg]
# M = 0 state of the multiplet: eigenvector of Sz with eigenvalue 0 inside the ground space
Mz = G.conj().T @ Sz @ G
mw, mv = np.linalg.eigh(Mz)
m0 = G @ mv[:, np.argmin(abs(mw))]
c1 = lock_cost(up, 'z'); c2 = lock_cost(up, 'x'); c3 = lock_cost(m0, 'z')
rmix = G @ G.conj().T / deg
r2 = Pup[x] @ rmix @ Pup[x] + Pdn[x] @ rmix @ Pdn[x]
c4 = (np.trace(r2 @ H) - np.trace(rmix @ H)).real
print(f"(i) polarised, lock along its axis: {c1:.9f}\n(ii) polarised, lock perpendicular: {c2:.6f}\n(iii) M=0 Dicke-like ground state, lock z: {c3:.6f}\n(iv) uniform mixture of ground states, lock z: {c4:.6f}")
ok = abs(c1) < 1e-10 and c2 > 1e-3 and c3 > 1e-3 and c4 > 1e-3
print("[%s] state- and sign-dependence as pre-registered" % ("PASS" if ok else "FAIL"))
print("TOTAL: PASS=%d FAIL=%d" % (int(ok), int(not ok)))
