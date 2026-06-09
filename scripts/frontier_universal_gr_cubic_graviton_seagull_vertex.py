"""Finite runner: W-native cubic seagull trace-channel boundary.

This runner checks a bounded finite diagnostic for the third metric variation of
W = log|det(D+J)| in a single two-component Cl(3) fermion model:

   d^3 W = Tr[G d^3 D]  -  3 Tr[G d^2 D G dD]  +  2 Tr[G dD G dD G dD]
           \\____seagull (diamagnetic)______/      \\__triangle (paramagnetic)__/

  T1  The paramagnetic triangle vanishes in the tested channels for the single
      two-component Cl(3) fermion.
  T2  The full determinant third derivative has nonzero trace-containing
      channels, so the nonzero response is in the seagull sector.
  T3  The tested pure transverse-traceless cubic channels vanish in this setup.
  T4  The trace-channel response is stable under the finite-difference step and
      transverse-grid change.

The runner does not claim an Einstein-Hilbert cubic vertex, nonlinear GR
closure, a cubic diffeomorphism Ward identity, or a magnitude normalization.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 420

import numpy as np
from scipy.linalg import sqrtm

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]

results = []
def check(name, ok):
    results.append((name, bool(ok)))

# ---------------------------------------------------------------------------
# T1: paramagnetic triangle <T T T> vanishes (momentum-space, conserved vertex)
# ---------------------------------------------------------------------------
def Gi(q, m):
    return np.linalg.inv(1j * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + m * I2)
def sbar(qi, ki):
    return 0.5 * (np.sin(qi) + np.sin(qi + ki))
def V(q, k, c, d):
    return 1j * 0.5 * (sig[c] * np.cos(q[c] + k[c] / 2) * sbar(q[d], k[d])
                       + sig[d] * np.cos(q[d] + k[d] / 2) * sbar(q[c], k[c]))
def triangle(k1, k2, pol1, pol2, pol3, N, m=1.0):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    k3 = -(k1 + k2)
    t = 0j
    for qx in p:
        for qy in p:
            for qz in p:
                q = np.array([qx, qy, qz])
                G0 = Gi(q, m); G1 = Gi(q + k1, m); G2 = Gi(q + k1 + k2, m)
                t += np.trace(G0 @ V(q, k1, *pol1) @ G1 @ V(q + k1, k2, *pol2) @ G2 @ V(q + k1 + k2, k3, *pol3))
    return t / N ** 3
N = 12
a = 2 * np.pi / N
# collinear (k1,k2 || x) and non-collinear (k1||x, k2||y); several channels
worst = 0.0
for (k1, k2) in [(np.array([a, 0, 0.0]), np.array([a, 0, 0.0])),
                 (np.array([a, 0, 0.0]), np.array([0, a, 0.0]))]:
    for pol in [((1, 2), (1, 2), (1, 2)), ((1, 1), (2, 2), (1, 2)), ((0, 1), (1, 2), (0, 2)),
                ((1, 1), (1, 1), (1, 1))]:
        worst = max(worst, abs(triangle(k1, k2, *pol, N)))
check("T1 paramagnetic triangle <T T T> VANISHES (max over channels+momenta = %.1e) -- 2-comp Cl(3) feature"
      % worst, worst < 1e-6)

# ---------------------------------------------------------------------------
# Vielbein-coupled Dirac on x-ring -> exact 3rd determinant derivative
# ---------------------------------------------------------------------------
def buildD(Lx, m, qy, qz, sources):
    T = np.zeros((Lx, Lx), complex)
    for x in range(Lx):
        T[x, (x + 1) % Lx] = 1.0
    hopx = (T - T.conj().T) / (2j)
    D = np.zeros((2 * Lx, 2 * Lx), complex)
    for x in range(Lx):
        D[2 * x:2 * x + 2, 2 * x:2 * x + 2] += m * I2
    ev = []
    for x in range(Lx):
        h = np.zeros((3, 3))
        for amp, E, k0 in sources:
            h = h + amp * E * np.cos(k0 * x)
        ev.append(sqrtm(np.eye(3) + h).real if np.any(h) else np.eye(3))
    siny = np.sin(qy); sinz = np.sin(qz)
    for aa in range(3):
        for i in range(3):
            ed = np.array([ev[x][aa, i] for x in range(Lx)], complex)
            blk = 0.5 * (np.diag(ed) @ hopx + hopx @ np.diag(ed)) if i == 0 else np.diag(ed * (siny if i == 1 else sinz))
            nz = np.argwhere(np.abs(blk) > 1e-15)
            for xx, yy in nz:
                D[2 * xx:2 * xx + 2, 2 * yy:2 * yy + 2] += 1j * sig[aa] * blk[xx, yy]
    return D
def W(Lx, m, Nyz, sources):
    p = np.linspace(-np.pi, np.pi, Nyz, endpoint=False)
    s = 0.0
    for qy in p:
        for qz in p:
            s += np.linalg.slogdet(buildD(Lx, m, qy, qz, sources))[1]
    return s / Nyz ** 2
def cubic(Lx, m, Nyz, E1, E2, E3, k1, k2, k3, eps=2e-2):
    def Wv(s1, s2, s3):
        return W(Lx, m, Nyz, [(s1, E1, k1), (s2, E2, k2), (s3, E3, k3)])
    tot = 0.0
    for s in (1, -1):
        for t in (1, -1):
            for u in (1, -1):
                tot += s * t * u * Wv(s * eps, t * eps, u * eps)
    return tot / (8 * eps ** 3)

Eyz = np.zeros((3, 3)); Eyz[1, 2] = Eyz[2, 1] = 1.0
Eyymzz = np.zeros((3, 3)); Eyymzz[1, 1] = 1; Eyymzz[2, 2] = -1
Etr = np.zeros((3, 3)); Etr[1, 1] = Etr[2, 2] = 1  # transverse conformal (yy+zz)
Lx = 8; m = 1.0; Nyz = 8
L = 2 * np.pi / Lx
k1, k2, k3 = L, L, -2 * L

# ---------------------------------------------------------------------------
# T2: full cubic vertex nonzero
# ---------------------------------------------------------------------------
c_yz2tr = cubic(Lx, m, Nyz, Eyz, Eyz, Etr, k1, k2, k3)
c_tr3 = cubic(Lx, m, Nyz, Etr, Etr, Etr, k1, k2, k3)
check("T2 trace-containing full determinant third derivative NONZERO (seagull): <yz,yz,trace>=%.4f, <trace^3>=%.4f"
      % (c_yz2tr, c_tr3), abs(c_yz2tr) > 1e-2 and abs(c_tr3) > 1e-2)

# ---------------------------------------------------------------------------
# T3: structure -- pure TT^3 vanishes, conformal-sector nonzero
# ---------------------------------------------------------------------------
c_yz3 = cubic(Lx, m, Nyz, Eyz, Eyz, Eyz, k1, k2, k3)
c_yymzz3 = cubic(Lx, m, Nyz, Eyymzz, Eyymzz, Eyymzz, k1, k2, k3)
c_yymzz2tr = cubic(Lx, m, Nyz, Eyymzz, Eyymzz, Etr, k1, k2, k3)
check("T3 STRUCTURE: pure-TT^3 VANISHES (<yz^3>=%.1e, <(yy-zz)^3>=%.1e) but TT^2-conformal NONZERO (<(yy-zz)^2,trace>=%.4f)"
      % (c_yz3, c_yymzz3, c_yymzz2tr), abs(c_yz3) < 1e-3 and abs(c_yymzz3) < 1e-3 and abs(c_yymzz2tr) > 1e-2)

# ---------------------------------------------------------------------------
# T4: robustness (eps + Nyz independence)
# ---------------------------------------------------------------------------
c_eps1 = cubic(Lx, m, Nyz, Eyz, Eyz, Etr, k1, k2, k3, eps=1e-2)
c_nyz = cubic(Lx, m, 10, Eyz, Eyz, Etr, k1, k2, k3)
rel_eps = abs(c_eps1 - c_yz2tr) / abs(c_yz2tr)
rel_nyz = abs(c_nyz - c_yz2tr) / abs(c_yz2tr)
check("T4 ROBUST: <yz,yz,trace> eps-independent (rel dev %.1e) and Nyz-independent (rel dev %.1e) -- genuine vertex"
      % (rel_eps, rel_nyz), rel_eps < 1e-2 and rel_nyz < 1e-2)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Finite W-native cubic diagnostic: trace-containing full determinant channels are nonzero")
print("(<yz,yz,trace> and <trace^3>), while the tested paramagnetic triangle and pure-TT^3")
print("channels vanish for the single two-component Cl(3) fermion. This is a bounded")
print("seagull/trace-channel result only: no Einstein-Hilbert cubic closure, cubic Ward identity,")
print("pure-TT cubic vertex, or magnitude normalization is claimed here.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
