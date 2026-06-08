"""Class-A finite runner: the lattice Green function asymptotic G(r) -> 1/(4 pi |r|)
(existence + value + isotropy = the accepted-premise import P1) is DERIVED framework-
internally from the A1 graph-Laplacian RESOLVENT via its heat kernel, not imported.

Chain (all framework-internal except standard Bessel/Gaussian asymptotics, reconstructed):
  L = -Delta_lat = the A1 Z^3 6-NN graph Laplacian (eigenvalue lambda(k)=6-2 sum cos k_mu).
  G = L^{-1}, and G(x) = (L^{-1})_{0x} = int_0^inf (e^{-tL})_{0x} dt   [resolvent identity].
  e^{-tL} factorizes over axes (L = sum_mu L_mu, [L_mu,L_nu]=0):
      (e^{-tL})_{0x} = prod_mu (e^{-t L_mu})_{0,x_mu} = prod_mu e^{-2t} I_{x_mu}(2t)
  where (e^{-tL_1})_{0n} = e^{-2t} I_n(2t) is the EXACT 1D NN heat kernel (I_n modified Bessel).
  => G(x) = int_0^inf prod_mu e^{-2t} I_{x_mu}(2t) dt   [framework-internal, A1 resolvent].
  Large-r asymptotic from the large-t CONTINUUM limit of the heat kernel:
      e^{-2t} I_n(2t) -> (4 pi t)^{-1/2} e^{-n^2/(4t)}  (large t)  [standard Bessel asymptotic]
   => prod_mu -> (4 pi t)^{-3/2} e^{-|x|^2/(4t)}  (the 3D continuum heat kernel)
   => G(x) -> int_0^inf (4 pi t)^{-3/2} e^{-|x|^2/(4t)} dt = 1/(4 pi |x|).
  The leading term is ISOTROPIC (depends only on |x|), value 4 pi fixed; lattice corrections
  are subleading. This SUPPLIES P1 (existence + uniqueness of the isotropic 1/r asymptotic)
  via the heat-kernel route, retiring the accepted-premise textbook import.

  T1  1D NN heat kernel (e^{-t L_1})_{0n} = e^{-2t} I_n(2t) (exact, vs matrix exp).
  T2  factorization (e^{-tL})_{0x} = prod_mu (e^{-t L_mu})_{0,x_mu} ([L_mu,L_nu]=0).
  T3  G(x) = int prod e^{-2t} I_{x_mu}(2t) dt: 4 pi |x| G(x) -> 1, ISOTROPIC (axis & diagonal).
  T4  G(0) = Watson integral = 0.252731... (validates the representation).
  T5  large-t Gaussian limit: e^{-2t} I_n(2t) / [(4 pi t)^{-1/2} e^{-n^2/4t}] -> 1.
  T6  continuum Green identity: int_0^inf (4 pi t)^{-3/2} e^{-r^2/4t} dt = 1/(4 pi r).
  CTRL anisotropy of the leading term is ZERO (axis vs diagonal 4 pi r G agree at large r);
       a wrong normalization (e.g. 1/(2 pi r)) fails.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.special import ive, iv

TOL = 1e-6
results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: 1D NN heat kernel (e^{-t L_1})_{0n} = e^{-2t} I_n(2t) ---
M = 41; c = M // 2
L1 = 2 * np.eye(M) - np.eye(M, k=1) - np.eye(M, k=-1)   # 1D graph Laplacian (open, large)
t = 0.7
HK = expm(-t * L1)
ok = True
for n in range(0, 8):
    lhs = HK[c, c + n]
    rhs = np.exp(-2 * t) * iv(n, 2 * t)
    if abs(lhs - rhs) > 1e-6:
        ok = False
check("T1 1D NN heat kernel (e^{-tL1})_{0n} = e^{-2t} I_n(2t)", ok)

# --- T2: factorization e^{-tL} = prod_mu e^{-t L_mu} (commuting axes) ---
# verify on a small 3D lattice that (e^{-tL})_{0x} = prod (e^{-tL1})_{0,x_mu}
m = 7; cc = m // 2
L1s = 2 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1)
I = np.eye(m)
# 3D Laplacian = L1 x I x I + I x L1 x I + I x I x L1
L3 = np.kron(np.kron(L1s, I), I) + np.kron(np.kron(I, L1s), I) + np.kron(np.kron(I, I), L1s)
HK3 = expm(-0.6 * L3)
HK1 = expm(-0.6 * L1s)
def lin(a, b, cz): return (a * m + b) * m + cz
o = lin(cc, cc, cc)
okf = True
for x in [(1, 0, 0), (1, 1, 0), (2, 1, 1)]:
    lhs = HK3[o, lin(cc + x[0], cc + x[1], cc + x[2])]
    rhs = HK1[cc, cc + x[0]] * HK1[cc, cc + x[1]] * HK1[cc, cc + x[2]]
    if abs(lhs - rhs) > 1e-9:
        okf = False
check("T2 e^{-tL} factorizes over axes (commuting L_mu)", okf)

# --- T3: G(x) via the Bessel resolvent integral; 4pi|x| G -> 1 isotropically ---
def G(x, y, z):
    f = lambda tt: ive(x, 2 * tt) * ive(y, 2 * tt) * ive(z, 2 * tt)  # ive = e^{-|.|}I; product = e^{-6t} prod I
    val, _ = quad(f, 0, np.inf, limit=400)
    return val
ax = {n: 4 * np.pi * n * G(n, 0, 0) for n in [8, 16, 32, 64]}
dg = {n: 4 * np.pi * (n * np.sqrt(3)) * G(n, n, n) for n in [8, 16, 32]}
check("T3 axis 4pi r G(r) -> 1 (within 1% by r=16, 0.1% by r=64)",
      abs(ax[16] - 1) < 0.01 and abs(ax[64] - 1) < 1e-3)
check("T3b diagonal 4pi r G(r) -> 1 (isotropic)", abs(dg[16] - 1) < 0.01 and abs(dg[32] - 1) < 5e-3)

# --- T4: G(0) = Watson integral 0.252731 ---
check("T4 G(0,0,0) = Watson integral 0.252731", abs(G(0, 0, 0) - 0.2527310) < 1e-4)

# --- T5: large-t Gaussian limit of the 1D heat kernel ---
okg = True
for tt in [50, 200, 800]:
    for n in [0, 5, 10]:
        bessel = ive(n, 2 * tt)   # = e^{-2t} I_n(2t), overflow-safe
        gauss = (4 * np.pi * tt) ** (-0.5) * np.exp(-n ** 2 / (4 * tt))
        if not np.isfinite(bessel / gauss) or abs(bessel / gauss - 1) > 0.02:
            okg = False
check("T5 e^{-2t} I_n(2t) -> (4 pi t)^{-1/2} e^{-n^2/4t} (large-t continuum heat kernel)", okg)

# --- T6: continuum Green identity int (4 pi t)^{-3/2} e^{-r^2/4t} dt = 1/(4 pi r) ---
okc = True
for r in [1.0, 2.5, 7.0]:
    val, _ = quad(lambda tt: (4 * np.pi * tt) ** (-1.5) * np.exp(-r ** 2 / (4 * tt)), 0, np.inf, limit=400)
    if abs(val - 1 / (4 * np.pi * r)) > 1e-6:
        okc = False
check("T6 int (4 pi t)^{-3/2} e^{-r^2/4t} dt = 1/(4 pi r) (continuum Green from heat kernel)", okc)

# --- CTRL: isotropy + wrong normalization fails ---
check("CTRL leading term isotropic: |axis - diagonal| 4pi r G -> 0 at r=32",
      abs(ax[32] - 4 * np.pi * (32 * np.sqrt(3)) * G(32, 32, 32)) < 5e-3)
check("CTRL wrong normalization 1/(2 pi r) is rejected (2pi r G !-> 1)", abs(2 * np.pi * 64 * G(64, 0, 0) - 1) > 0.4)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
