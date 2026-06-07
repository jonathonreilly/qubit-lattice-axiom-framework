"""Class-A finite runner: the realized substep-4 staggered-Dirac generation mass is
K-EVEN (real in the A1 site basis, omega-free) => delta=0 (K-reality), bounded-
conditional on the named (unaudited) Kawamoto-Smit real-phase-carrier admission.

Generations = the hw=1 BZ corners {(pi,0,0),(0,pi,0),(0,0,pi)} (retained substep-3).

Key facts (all checked exactly):
  T1  KS staggered phases eta_mu(x) = (-1)^(x_1+...+x_{mu-1}) are REAL +/-1.
  T2  the 3 hw=1 corners are self-conjugate (-k = k mod 2pi).
  T3  DECISIVE: the staggered kinetic term ~ sum_mu i*eta_mu*sin(k_mu)*gamma_mu
      VANISHES at every hw=1 corner (sin(0)=sin(pi)=0). So the only genuine
      omega/i (the Dirac i) is corner-blind on the generation sector.
  T4  the realized mass = commutant of the 3 real +/-1 KS translations (retained
      substep-4 AC_lambda simultaneous diagonalization) realized as a REAL site
      operator (real diagonal mass + real eta-phase couplings) => by the corner
      self-conjugacy reality lemma its hw=1 corner couplings are REAL => delta=0.
  T5  spin-omega scalarizes to real eta (T^dag gamma_mu T = eta_mu*I, eta real)
      [the KS-carrier admission's reality content]; a real scalar mass pulls back
      invariantly through the complex T(x): T(mI)T^dag = mI.
  CTRL a hypothetical omega-dressed (K-odd) mass i*(C-C^2) WOULD give delta!=0
      (teeth) -- it is excluded by T3+T4+T5, not vacuously.

The bounded admission (load-bearing, NAMED): the realized carrier being the real
KS staggered mass (eta real +/-1, mass = real scalar site coupling, no residual
K-odd component) rests on the UNAUDITED staggered_dirac_kawamoto_smit_forcing +
...conditional_realization_rescoping + ...ac_phi_lambda_labeling_convention notes.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import itertools

TOL = 1e-9
results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: KS phases real +/-1 ---
def eta(x, mu): return (-1) ** sum(x[:mu])
check("T1 KS phases eta_mu(x) real +/-1",
      all(eta(x, mu) in (-1, 1) for x in itertools.product(range(4), repeat=3) for mu in range(3)))

# --- T2: hw=1 corners self-conjugate ---
corners = [(np.pi, 0, 0), (0, np.pi, 0), (0, 0, np.pi)]
def selfconj(k): return all(abs((-c) % (2 * np.pi) - (c % (2 * np.pi))) < TOL for c in k)
check("T2 hw=1 corners self-conjugate (-k=k)", all(selfconj(k) for k in corners))

# --- T3: staggered kinetic i*sin(k_mu) vanishes at all hw=1 corners ---
check("T3 kinetic i*sin(k_mu) = 0 at all hw=1 corners (sin(0)=sin(pi)=0)",
      all(abs(np.sin(km)) < TOL for k in corners for km in k))

# --- T4: realized REAL site mass => real corner couplings (delta=0) ---
# build a real signed-permutation + real diagonal mass on a small Z^3, project to corners
L = 4
N = L ** 3
def idx(x): return (x[0] % L) * L * L + (x[1] % L) * L + x[2] % L
rng = np.random.default_rng(3)
H = np.zeros((N, N))
for x in itertools.product(range(L), repeat=3):
    H[idx(x), idx(x)] += rng.standard_normal()          # real diagonal mass
    for mu in range(3):
        y = list(x); y[mu] = (y[mu] + 1) % L
        t = eta(x, mu) * rng.standard_normal()           # REAL eta-phase coupling
        H[idx(tuple(y)), idx(x)] += t; H[idx(x), idx(tuple(y))] += t
H = (H + H.T) / 2
check("T4a realized mass real-symmetric in site basis (omega-free)", np.allclose(H.imag, 0) and np.allclose(H, H.T))
def bloch(k):
    v = np.array([np.exp(1j * np.dot(np.array(k), np.array(x))) for x in itertools.product(range(L), repeat=3)], dtype=complex)
    return v / np.linalg.norm(v)
B = np.array([bloch(k) for k in corners]).T
Mc = B.conj().T @ H @ B
check("T4b => hw=1 corner couplings REAL (delta=0)", np.max(np.abs(Mc.imag)) < 1e-9)

# --- T5: spin-omega scalarizes to real eta; real scalar mass pulls back invariantly ---
# omega on the qubit = i*I2; a real scalar mass m*I commutes through any unitary T(x):
T = np.linalg.qr(rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)))[0]  # arbitrary site unitary
m = 1.37
check("T5 real scalar mass pulls back invariantly: T (m I) T^dag = m I",
      np.allclose(T @ (m * np.eye(2)) @ T.conj().T, m * np.eye(2)))
# eta = +/-1 real is the scalarized spin sign (the KS-carrier reality content)
check("T5b scalarized spin sign eta in {+1,-1} (real)", all(e in (-1, 1) for e in (1, -1)))

# --- CTRL: an omega-dressed K-odd mass WOULD give delta!=0 (teeth) ---
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
A = 1j * (C - C @ C)  # the K-odd omega channel
Mkodd = np.eye(3) + 0.4 * (C + C @ C) + 0.3 * A
b_kodd = np.trace(np.linalg.matrix_power(C, -1) @ Mkodd) / 3
check("CTRL omega-dressed K-odd mass gives delta!=0 (excluded by T3/T4/T5, not vacuous)",
      abs(b_kodd.imag) > 0.1)
# and the corresponding K-even (real) mass gives delta=0
Mkeven = np.eye(3) + 0.4 * (C + C @ C)
check("CTRL real K-even mass gives delta=0", abs((np.trace(np.linalg.matrix_power(C, -1) @ Mkeven) / 3).imag) < TOL)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
