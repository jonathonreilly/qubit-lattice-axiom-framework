"""A44 igg: invariant gauge group of the hopping family at mean field (algebra check, no heavy numerics).
A bond term f_x^dag M f_y + h.c. commutes with eta^+ = sum_x f_xu^dag f_xd^dag iff M eps + eps M^* = 0
(eps = i s^y; derived in the report).  After the staggered U(1) gauge f_x -> i^{|x|} f_x, a nearest-
neighbour M becomes i M (|y| = |x| + 1); a same-sublattice hop (|y| = |x| + 2) becomes -M."""
import numpy as np, itertools
from a44lib import SIG
eps = np.array([[0, 1], [-1, 0]], complex)
def defect(M): return np.abs(M @ eps + eps @ M.conj()).max()
rng = np.random.default_rng(1)
worst = 0.
for a in range(3):
    for t, lam in rng.normal(size=(20, 2)):
        M = t * np.eye(2) + 1j * lam * SIG[a]
        worst = max(worst, defect(1j * M))
print(f"(t + i lam s^a), staggered-gauged (x i): max |M eps + eps M*| over 60 random (t,lam,a) = {worst:.1e}  -> eta-SU(2) invariant")
print(f"same without the staggered gauge, t=0, lam=1: {defect(1j * SIG[2]):.1f} (not invariant in this gauge)")
print(f"KS pi-flux scalar hop +-1, staggered-gauged: {defect(1j * np.eye(2)):.1e}")
print(f"second-neighbour real hop t'=1 (same sublattice, gauged factor -1): {defect(-np.eye(2)):.1f}  -> breaks SU(2) to U(1)")
# commutator check with explicit operators on two sites (4 modes): [eta^+, H_bond] = 0 ?
def ops(nm):
    # Jordan-Wigner on 4 modes: (x up, x dn, y up, y dn)
    I2 = np.eye(2); Zm = np.diag([1., -1.]); a_ = np.array([[0, 1], [0, 0.]])
    out = []
    for k in range(nm):
        m = np.array([[1.]])
        for l in range(nm):
            m = np.kron(m, Zm if l < k else (a_ if l == k else I2))
        out.append(m)
    return out
c = ops(4); cd = [m.T.conj() for m in c]
eta = cd[0] @ cd[1] + cd[2] @ cd[3]
for lab, M in (("i*(t + i lam s^z), t=.3 lam=1", 1j * (0.3 * np.eye(2) + 1j * SIG[2])), ("(t + i lam s^z) ungauged", 0.3 * np.eye(2) + 1j * SIG[2])):
    H = sum(M[s, sp] * cd[s] @ c[2 + sp] for s in range(2) for sp in range(2)); H = H + H.conj().T
    print(f"explicit 2-site Fock check, {lab}: |[eta+, H]| = {np.abs(eta @ H - H @ eta).max():.1e}")
