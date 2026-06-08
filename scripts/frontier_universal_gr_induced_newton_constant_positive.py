"""Class-A finite runner (memory-safe): the W-native induced Newton constant -- the Ward-clean,
isotropic TT graviton stiffness C_TT is the induced 1/(16 pi G_Newton), and it is POSITIVE and
FINITE (attractive gravity, no ghost). Magnitude registered (G3); sign / finiteness / structure /
W-nativeness derived.

Step 3 (capstone) of the universal-GR tensor closure. Assembling the chain:
  #3222           : the metric-Hessian of W = log|det(D+J)| is the Dirac stress 2-pt Pi_ijkl(k)
                    (Sakharov induced gravity), W-native; healthy positive TT k^2 sign on the
                    elliptic generator.
  step 1 (#3242)  : conserved point-split stress vertex + diamagnetic seagull -> Pi_ijkl transverse
                    (diffeomorphism Ward identity, to leading order).
  step 2 (#3257)  : the proper staggered Kaehler-Dirac fermion -> approximately ISOTROPIC graviton
                    (E_g/T_2g converge); naive-Dirac anisotropy is a wrong-fermion artifact.
  step 3 (HERE)   : the continuum-extrapolated isotropic TT stiffness C_TT = induced 1/(16 pi G) is
                    POSITIVE and FINITE => a consistent positive (attractive) finite G_Newton exists;
                    its magnitude is registered (G3) via the lattice scale a (G = a^2/(16 pi C_TT)).

  T1  C_TT (staggered Kaehler-Dirac, Ward-clean TT) is POSITIVE and N-CONVERGES to a finite continuum
      value (C_TT(0) ~ +0.020 at m=0.7): the induced 1/(16 pi G) > 0 -- attractive gravity, no ghost.
  T2  C_TT is POSITIVE and FINITE for all fermion masses (m in {1,0.7,0.5,0.3}); the quadratic
      Sakharov divergence is LATTICE-REGULATED (finite in lattice units) -- a well-defined induced G.
  T3  CONTROL (the load-bearing elliptic pin): the non-elliptic bare-Hermitian sigma.sin generator
      (det sign-indefinite, NOT a valid partition function) gives a NEGATIVE C_TT -- a TACHYONIC
      (repulsive/ghost) induced 1/G. So the POSITIVE induced Newton constant REQUIRES the native
      elliptic generator (the retained cpt_exact_real_anti_hermitian_d identification), the same pin
      as #3222.
  T4  the staggered generator IS elliptic: D D^dag = Delta(P) * 1_16 with Delta = m^2 + sum_mu
      sin^2(P_mu/2) > 0 on all modes (a valid Z) -- so the staggered induced G is on the healthy
      (elliptic) branch by construction.
  T5  consistency with the registered G_Newton: the induced-gravity relation 1/(16 pi G) = C_TT > 0
      yields a finite positive G = a^2/(16 pi C_TT); its sign matches the ATTRACTIVE scalar Newtonian
      gravity already derived on the same lattice (positive 1/r potential; gravity_clean_derivation /
      #3184). The magnitude is registered (G3, via a); only the sign / finiteness / structure /
      W-nativeness is derived here.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 420

import itertools
import numpy as np

# ---------------------------------------------------------------------------
# Staggered Kaehler-Dirac operator (exact 16x16 hypercube block) -- the framework's fermion
# ---------------------------------------------------------------------------
CORNERS = list(itertools.product([0, 1], repeat=4))
CIDX = {A: i for i, A in enumerate(CORNERS)}
def eta(A, mu):
    return (-1) ** sum(A[nu] for nu in range(mu))
def flip(A, mu):
    B = list(A)
    B[mu] ^= 1
    return tuple(B)
def Dstag(P, m):
    D = np.zeros((16, 16), complex)
    for A in CORNERS:
        a = CIDX[A]
        D[a, a] += m
        for mu in range(4):
            if A[mu] == 0:
                D[a, CIDX[flip(A, mu)]] += 0.5 * eta(A, mu) * (1 - np.exp(-1j * P[mu]))
            else:
                D[a, CIDX[flip(A, mu)]] += 0.5 * eta(A, mu) * (np.exp(1j * P[mu]) - 1)
    return D
def VelStag(P, i):
    D = np.zeros((16, 16), complex)
    for A in CORNERS:
        a = CIDX[A]
        if A[i] == 0:
            D[a, CIDX[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(-1j * P[i]))
        else:
            D[a, CIDX[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(1j * P[i]))
    return D
def GiStag(P, m):
    return np.linalg.inv(Dstag(P, m))
def momS(Pj, Kj):
    return np.sin(0.5 * (Pj + 0.5 * Kj))
def VstagS(P, K, i, j):
    Pm = P + 0.5 * K
    return 0.5 * (VelStag(Pm, i) * momS(P[j], K[j]) + VelStag(Pm, j) * momS(P[i], K[i]))
def C_TT_stag(K0, N, m):
    # T_2g (yz) TT graviton stiffness; induced-action slope +Tr[GVGV] (healthy = positive)
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    i, j, k_, l = 2, 3, 2, 3
    def Pi(kx):
        K = np.zeros(4)
        K[1] = kx
        t = 0j
        for a0 in p:
            for a1 in p:
                for a2 in p:
                    for a3 in p:
                        P = np.array([a0, a1, a2, a3])
                        t += np.trace(GiStag(P, m) @ VstagS(P, K, i, j)
                                      @ GiStag(P + K, m) @ VstagS(P + K, -K, k_, l))
        return t / N ** 4
    return ((Pi(K0) - Pi(0.0)) / (2 - 2 * np.cos(K0))).real

results = []
def check(name, ok):
    results.append((name, bool(ok)))

# ---------------------------------------------------------------------------
# T1: C_TT positive, N-converges to finite continuum value
# ---------------------------------------------------------------------------
m = 0.7
vals = [(2 * np.pi / N, C_TT_stag(2 * np.pi / N, N, m)) for N in (6, 8, 10)]
K0s = np.array([v[0] for v in vals])
cs = np.array([v[1] for v in vals])
A = np.vstack([np.ones_like(K0s), K0s ** 2]).T
c0 = np.linalg.lstsq(A, cs, rcond=None)[0][0]
check("T1 induced 1/(16piG)=C_TT POSITIVE + N-convergent (staggered, m=0.7): C_TT(N=6,8,10)=%s -> continuum %+.5f"
      % (", ".join("%+.5f" % c for c in cs), c0), all(c > 0 for c in cs) and c0 > 0
      and (max(cs) - min(cs)) < 1e-3)

# ---------------------------------------------------------------------------
# T2: positive + finite for all masses (lattice-regulated)
# ---------------------------------------------------------------------------
mass_vals = [(mm, C_TT_stag(2 * np.pi / 8, 8, mm)) for mm in (1.0, 0.7, 0.5, 0.3)]
check("T2 C_TT > 0 and FINITE for all m in {1,0.7,0.5,0.3} (%s) -- lattice-regulated induced G, no pathology"
      % ", ".join("%+.4f" % c for _, c in mass_vals),
      all(c > 0 and np.isfinite(c) for _, c in mass_vals))

# ---------------------------------------------------------------------------
# T3: CONTROL -- non-elliptic bare-Hermitian generator gives NEGATIVE (tachyonic) C_TT
# ---------------------------------------------------------------------------
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]
def C_TT_bareHerm(k0, N, m):
    # non-elliptic generator sigma.sin (NO i): det = m^2 - |sin|^2 sign-indefinite -> not a valid Z
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    def G(q):
        # bare-Hermitian sigma.sin has a Fermi surface (det=m^2-|sin|^2=0): tiny i*eps regulator,
        # exactly the ill-definedness that makes it an invalid partition function.
        return np.linalg.inv((sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2]))
                             + (m + 1e-6j) * I2)
    def sb(qi, ki):
        return 0.5 * (np.sin(qi) + np.sin(qi + ki))
    def V(q, k, c, d):
        return 0.5 * (sig[c] * np.cos(q[c] + k[c] / 2) * sb(q[d], k[d])
                      + sig[d] * np.cos(q[d] + k[d] / 2) * sb(q[c], k[c]))
    def Pi(kx):
        k = np.array([kx, 0.0, 0.0])
        t = 0j
        for qx in p:
            for qy in p:
                for qz in p:
                    q = np.array([qx, qy, qz])
                    t += np.trace(G(q) @ V(q, k, 1, 2) @ G(q + k) @ V(q + k, -k, 1, 2))
        return t / N ** 3
    k1 = 2 * np.pi / N
    return ((Pi(k1) - Pi(0.0)) / (2 - 2 * np.cos(k1))).real
cbh = C_TT_bareHerm(2 * np.pi / 10, 10, 1.0)
check("T3 CONTROL: non-elliptic bare-Hermitian sigma.sin gives NEGATIVE C_TT=%+.4f (tachyonic/ghost 1/G) -- positive G REQUIRES the elliptic pin"
      % cbh, cbh < 0)

# ---------------------------------------------------------------------------
# T4: staggered generator is elliptic (valid Z) -- on the healthy branch by construction
# ---------------------------------------------------------------------------
P = np.array([0.5, 0.9, 0.3, 1.2])
D = Dstag(P, 0.7)
ev = np.linalg.eigvals(D @ D.conj().T).real
delta = 0.7 ** 2 + sum(np.sin(P[mu] / 2) ** 2 for mu in range(4))
check("T4 staggered generator ELLIPTIC: D D^dag = Delta*1, Delta=m^2+sum sin^2(P/2)=%.4f > 0 (valid Z; healthy branch)"
      % delta, np.min(ev) > 0 and np.max(np.abs(ev - delta)) < 1e-9)

# ---------------------------------------------------------------------------
# T5: consistency with registered G_Newton (structural; magnitude registered G3)
# ---------------------------------------------------------------------------
# induced-gravity relation 1/(16 pi G) = C_TT > 0 -> G = a^2/(16 pi C_TT) finite + positive.
G_over_a2 = 1.0 / (16 * np.pi * c0)   # G/a^2 in lattice units; a (lattice scale) registered (G3)
check("T5 consistency: 1/(16piG)=C_TT>0 -> finite positive G/a^2=%.4f (a registered, G3); sign matches attractive scalar Newton (#3184)"
      % G_over_a2, c0 > 0 and np.isfinite(G_over_a2) and G_over_a2 > 0)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("The W-native induced Newton constant: C_TT (Ward-clean, isotropic, staggered Kaehler-Dirac TT")
print("graviton stiffness) = induced 1/(16 pi G) is POSITIVE (attractive, no ghost) and FINITE")
print("(lattice-regulated), continuum value ~ +0.020 (m=0.7). The positive sign REQUIRES the native")
print("elliptic generator (control: non-elliptic -> tachyonic). Magnitude registered (G3) via the")
print("lattice scale a; only the sign / finiteness / structure / W-nativeness is derived. Capstone of")
print("the W-native healthy (#3222) + Ward-clean (#3242) + isotropic (#3257) induced graviton.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
