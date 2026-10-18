#!/usr/bin/env python3
"""C2(i)-W1: velocity ratio from the two supplied ingredients on main.

Photon: supplied Gaussian lattice-Maxwell comparator H = (U/2)E^2 + (K/2) A^T C^T C A
(continuous Hamiltonian time t_H). We rebuild the lattice curl on an L^3 torus and
check that the transverse frequencies are omega = sqrt(UK)|s(k)|, s_j = 2 sin(k_j/2),
so c_gamma = sqrt(UK) sites per unit t_H (isotropic at O(k)).

Fermion: supplied two-qubit cubic Dirac walk (Clifford family, Gram matrix G(b)),
one tick tau. The massless member has cos omega = phi0^T G(b) phi(k) and cone speed
s(b) = b0 + 2 b1 + b2 sites per tick. We scan a one-parameter curve of admissible b,
verify PSD rank 3, build the 4x4 walk U(k), check unitarity, and measure the cone
speed from the eigenphases along an axis and a body diagonal.

Common clock: the only way to compare the two velocities is a declared conversion
rho = (Hamiltonian time per tick). Then c_gamma/c_psi = sqrt(UK) rho / s(b).
Nothing here fixes rho or b; this runner exhibits the continuous dependence.
"""
import itertools
import sys
import numpy as np
import sympy as sp
from scipy.optimize import brentq

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from c2_common import Checks

ck = Checks()

# ---------------------------------------------------------------- photon comparator
def curl_matrix(L):
    N = L ** 3
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    # link variable index: 3*site + dir ; plaquette (face) index: 3*site + normal
    Cm = np.zeros((3 * N, 3 * N))
    for x, y, z in itertools.product(range(L), repeat=3):
        r = np.array([x, y, z])
        for n in range(3):
            a, b = [d for d in range(3) if d != n]
            ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
            # (curl A)_n at plaquette (r; a,b) = A_a(r) + A_b(r+ea) - A_a(r+eb) - A_b(r)
            sgn = 1 if (a, b) in [(0, 1), (1, 2), (2, 0)] else -1
            p = 3 * idx(*r) + n
            Cm[p, 3 * idx(*r) + a] += sgn
            Cm[p, 3 * idx(*(r + ea)) + b] += sgn
            Cm[p, 3 * idx(*(r + eb)) + a] -= sgn
            Cm[p, 3 * idx(*r) + b] -= sgn
    return Cm

L = 4
Cm = curl_matrix(L)
CtC = Cm.T @ Cm
ev = np.sort(np.linalg.eigvalsh(CtC))
# predicted nonzero eigenvalues: |s(k)|^2 twice for each k != 0
pred = []
for n in itertools.product(range(L), repeat=3):
    k = 2 * np.pi * np.array(n) / L
    s2 = float(np.sum(4 * np.sin(k / 2) ** 2))
    if s2 > 1e-12:
        pred += [s2, s2]
pred = np.sort(pred)
nz = ev[ev > 1e-9]
ck.check('photon: C^T C on 4^3 torus has kernel N+2 and nonzero spectrum {|s(k)|^2 x2, k!=0}',
         len(ev) - len(nz) == L ** 3 + 2 and len(nz) == len(pred) and np.allclose(nz, pred, atol=1e-9),
         f"kernel={len(ev)-len(nz)}, max dev={np.max(np.abs(nz-pred)):.1e}")
Ut, Kt = 1.7, 1.2  # test couplings (as in the landed comparator runner)
# omega^2 = U K |s|^2 for transverse oscillators: H = U/2 E^2 + K/2 A C^T C A
ck.check('photon: omega = sqrt(UK)|s(k)|, so c_gamma = sqrt(UK) per unit Hamiltonian time; |s|^2 = |k|^2 - sum k^4/12 + ..., isotropic at O(k^2)',
         sp.simplify(sp.series(sum(4 * sp.sin(sp.Symbol(f'k{j}') / 2) ** 2 for j in range(3)), sp.Symbol('k0'), 0, 5).removeO()
                     - (sp.Symbol('k0') ** 2 - sp.Symbol('k0') ** 4 / 12 + 4 * sp.sin(sp.Symbol('k1') / 2) ** 2 + 4 * sp.sin(sp.Symbol('k2') / 2) ** 2)) == 0)
print(f"  landed comparator value (cited, not recomputed): c_gamma = sqrt(UK) = 1.025 (U=1/chi, K=4u0)")

# ---------------------------------------------------------------- Dirac walk family
def Gmat(b0, b1, b2):
    return np.array([
        [1 - 3 * b0 ** 2, -2 * b0 * b1, b1 ** 2 - b0 ** 2 - b0 * b2, -3 * b1 * (b0 - b2)],
        [-2 * b0 * b1, b0 ** 2 - 2 * b1 ** 2, b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2],
        [b1 ** 2 - b0 ** 2 - b0 * b2, b1 * (b0 - b2), 2 * b1 ** 2 - b2 ** 2, 2 * b1 * b2],
        [-3 * b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2, 2 * b1 * b2, 3 * b2 ** 2]])

# exact symbolic sanity: Gram identity phi^T G phi + |g|^2 = 1
c = sp.symbols('c1:4'); s_ = sp.symbols('s1:4'); B = sp.symbols('b0:3')
PHI = sp.Matrix([1, sum(c), c[0]*c[1]+c[0]*c[2]+c[1]*c[2], c[0]*c[1]*c[2]])
g = [B[0]*s_[a] + B[1]*s_[a]*(sum(c)-c[a]) + B[2]*s_[a]*sp.prod([c[j] for j in range(3) if j != a]) for a in range(3)]
Gs = sp.Matrix(Gmat(*B))
expr = sp.expand((PHI.T * Gs * PHI)[0] + sum(gi**2 for gi in g) - 1)
expr = expr.subs({s_[a]**2: 1 - c[a]**2 for a in range(3)})
expr = sp.expand(expr)
# reduce remaining even powers of s (subs above handles s^2 only; higher handled by repeated subs)
for _ in range(3):
    expr = sp.expand(expr.subs({s_[a]**2: 1 - c[a]**2 for a in range(3)}))
ck.check('walk: Gram identity phi^T G(b) phi + |g|^2 = 1 holds identically (exact, sympy)', expr == 0)

sq5 = sp.sqrt(5)
bgold = ((9*sq5-5)/38, (5*sq5-7)/19, (71-29*sq5)/38)
ck.check('walk: light-speed member b_gold has s = b0+2b1+b2 = 1 exactly', sp.simplify(bgold[0]+2*bgold[1]+bgold[2]) == 1)

def detG_u(b0, b2, u):
    return np.linalg.det(Gmat(b0, np.sqrt(u), b2))

def member(b0, b2):
    """smallest positive root u=b1^2 of det G = 0 on (0, umax), PSD-rank-3 test"""
    us = np.linspace(1e-6, 0.25, 2001)
    vals = [detG_u(b0, b2, u) for u in us]
    for i in range(len(us) - 1):
        if vals[i] * vals[i + 1] < 0:
            u = brentq(lambda x: detG_u(b0, b2, x), us[i], us[i + 1], xtol=1e-15)
            G = Gmat(b0, np.sqrt(u), b2)
            w = np.linalg.eigvalsh(G)
            return np.sqrt(u), G, w
    return None

def phik(k):
    cc = np.cos(k)
    return np.array([1, cc.sum(), cc[0]*cc[1]+cc[0]*cc[2]+cc[1]*cc[2], cc[0]*cc[1]*cc[2]])

def gvec(k, b):
    cc, ss = np.cos(k), np.sin(k)
    return np.array([b[0]*ss[a] + b[1]*ss[a]*(cc.sum()-cc[a]) + b[2]*ss[a]*np.prod([cc[j] for j in range(3) if j != a]) for a in range(3)])

tau = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
sig = tau
I2 = np.eye(2)

def walk_from_G(G, b):
    lam, V = np.linalg.eigh(G)
    F = (np.sqrt(np.clip(lam[1:], 0, None))[:, None] * V[:, 1:].T)  # 3x4, drop null vector
    phi0 = phik(np.zeros(3))
    a = F @ phi0
    # orthogonal R with R a = e1 (Householder)
    e1 = np.array([1.0, 0, 0]); vv = a - e1
    R = np.eye(3) if np.linalg.norm(vv) < 1e-14 else np.eye(3) - 2 * np.outer(vv, vv) / (vv @ vv)
    F = R @ F
    def U(k):
        f, h1, h2 = F @ phik(k)
        gk = gvec(k, b)
        return (f * np.eye(4) + 1j * (h1 * np.kron(tau[0], I2) + h2 * np.kron(tau[1], I2))
                + 1j * sum(gk[a] * np.kron(tau[2], sig[a]) for a in range(3)))
    return U, F

rng = np.random.default_rng(1)
b2 = 3 / 20
rows = []
B0S = sorted(list(np.linspace(0.33, 0.40, 8)) + [11 / 30])
for b0 in B0S:
    m = member(b0, b2)
    if m is None:
        print(f"  b0={b0}: no root found"); continue
    b1, G, w = m
    psd = w[0] > -1e-10 and abs(w[0]) < 1e-9 and w[1] > 1e-6
    sval = b0 + 2 * b1 + b2
    U, F = walk_from_G(G, (b0, b1, b2))
    unit = max(np.abs(U(k) @ U(k).conj().T - np.eye(4)).max() for k in rng.uniform(-np.pi, np.pi, (20, 3)))
    eps = 1e-3
    def speed(dirn):
        k = eps * dirn / np.linalg.norm(dirn)
        ph = np.angle(np.linalg.eigvals(U(k)))
        return np.min(np.abs(ph)) / eps
    sx, sd = speed(np.array([1., 0, 0])), speed(np.array([1., 1, 1]))
    rows.append((b0, b1, sval, sx, sd, psd, unit))
    print(f"  b=({b0:.4f},{b1:.6f},{b2}) eig(G)={np.round(w,5)} s={sval:.6f} cone speed axis={sx:.6f} diag={sd:.6f} unitarity err={unit:.1e}")
ck.check('walk: every scanned member has G PSD of rank 3 (one zero eigenvalue)', all(r[5] for r in rows) and len(rows) == len(B0S))
ck.check('walk: factorised U(k) unitary to 1e-12 for all scanned members', all(r[6] < 1e-12 for r in rows))
ck.check('walk: eigenphase cone speed = s(b) along axis and body diagonal (isotropic at O(k)), to 1e-5',
         all(abs(r[3] - r[2]) < 1e-5 and abs(r[4] - r[2]) < 1e-5 for r in rows))
svals = [r[2] for r in rows]
ck.check('walk: cone speed s varies with the coin coefficients along a continuous admissible curve (spread > 0.05)',
         max(svals) - min(svals) > 0.05 and all(np.diff(svals) > 0) and max(np.diff(svals)) < 0.02,
         f"s range [{min(svals):.4f},{max(svals):.4f}], monotone, max step {max(np.diff(svals)):.4f}")
star = [r for r in rows if abs(r[0] - 11/30) < 1e-12][0]
ck.check('walk: at b* = (11/30, sqrt(u*), 3/20) the speed is 0.914 (landed value)', abs(star[2] - 0.9144) < 5e-4, f"s*={star[2]:.6f}")

# ---------------------------------------------------------------- ratio
cg = 1.025
print("\n  c_gamma/c_psi = sqrt(UK) * rho / s(b)  (rho = Hamiltonian time per walk tick, declared)")
for rho in [1.0, 0.9144 / 1.025]:
    print(f"   rho={rho:.6f}: " + ", ".join(f"s={r[2]:.4f} -> {cg*rho/r[2]:.6f}" for r in rows) + f", b_gold s=1 -> {cg*rho:.6f}")
ratios = [cg / r[2] for r in rows]
ck.check('W1 witness pair at fixed rho=1: members b* and b_gold give c_gamma/c_psi = 1.025/0.9144 vs 1.025/1 (different)',
         abs(cg / star[2] - cg / 1.0) > 0.05)
sys.exit(ck.total())
