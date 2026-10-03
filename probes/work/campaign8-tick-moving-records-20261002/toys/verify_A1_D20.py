"""Coordinator check of A1 D20: every STRICTLY local 2x2 walk on Z^3 has W3 = 0 (net handedness balanced), while the
quasi-local normalized covariant sum S/|S| has W3 = +-2 (A1 D14). Random strictly local walks: products of random SU(2)
coins and conditional shifts along random axes (diag(e^{ik},e^{-ik}) in a random basis), 3-9 layers."""
import numpy as np
from scipy.stats import unitary_group
from weyl_walk_tool import winding, s0, sx, sy, sz
rng = np.random.default_rng(99)
def cshift(axis, basis):
    def f(k):
        D = np.diag([np.exp(1j*k[axis]), np.exp(-1j*k[axis])])
        return basis @ D @ basis.conj().T
    return f
def make_walk(nlayers):
    layers = []
    for _ in range(nlayers):
        layers.append(("coin", unitary_group.rvs(2, random_state=rng)))
        layers.append(("shift", cshift(int(rng.integers(3)), unitary_group.rvs(2, random_state=rng))))
    def U(k):
        M = np.eye(2, dtype=complex)
        for kind, obj in layers:
            M = (obj if kind == "coin" else obj(k)) @ M
        return M
    return U
for trial, nl in enumerate([3, 4, 5, 6, 7, 9]):
    W = winding(make_walk(nl), n=28)
    print("strictly local random walk, %d coin+shift layers: W3 = %+.4f" % (nl, W.real), flush=True)
def Stilde(k):
    S = sum(np.cos(k[a]) * s0 - 1j * np.sin(k[a]) * (sx, sy, sz)[a] for a in range(3))
    return S / np.sqrt(abs(np.linalg.det(S)))
print("quasi-local normalized covariant sum S/|S|: W3 = %+.4f" % winding(Stilde, n=40).real)
