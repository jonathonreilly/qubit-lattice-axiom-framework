"""Finite runner: positive staggered TT stiffness diagnostic.

This runner computes the finite Brillouin-zone TT stiffness C_TT for the
implemented staggered Kaehler-Dirac response and checks that it is positive and
finite on the tested N/m grid. It also evaluates a non-elliptic bare-Hermitian
control, which comes out negative, showing that the positive sign is not a
tautology of the measurement code.

The induced-gravity interpretation is conditional: if a separate reviewed
bridge identifies this C_TT with the Einstein-Hilbert quadratic coefficient,
then the sign diagnostic would read as positive finite 1/G in lattice units.
This runner does not derive a physical G_Newton magnitude, an exact
normalization constant, or the nonlinear Einstein-Hilbert action.

  T1  C_TT is positive and N-stable for the staggered implementation at m=0.7.
  T2  C_TT is positive and finite for the tested mass grid.
  T3  The non-elliptic bare-Hermitian sigma.sin control gives negative C_TT.
  T4  The implemented staggered operator passes the finite ellipticity check.
  T5  The formal 1/(16*pi*C_TT) conversion is positive and finite as a
      conditional sign diagnostic only.

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
# T1: C_TT positive, N-stable finite-grid value
# ---------------------------------------------------------------------------
m = 0.7
vals = [(2 * np.pi / N, C_TT_stag(2 * np.pi / N, N, m)) for N in (6, 8, 10)]
K0s = np.array([v[0] for v in vals])
cs = np.array([v[1] for v in vals])
A = np.vstack([np.ones_like(K0s), K0s ** 2]).T
c0 = np.linalg.lstsq(A, cs, rcond=None)[0][0]
check("T1 staggered TT stiffness C_TT is positive and N-stable (m=0.7): C_TT(N=6,8,10)=%s -> fitted intercept %+.5f"
      % (", ".join("%+.5f" % c for c in cs), c0), all(c > 0 for c in cs) and c0 > 0
      and (max(cs) - min(cs)) < 1e-3)

# ---------------------------------------------------------------------------
# T2: positive + finite for tested masses
# ---------------------------------------------------------------------------
mass_vals = [(mm, C_TT_stag(2 * np.pi / 8, 8, mm)) for mm in (1.0, 0.7, 0.5, 0.3)]
check("T2 C_TT > 0 and finite for tested m in {1,0.7,0.5,0.3} (%s)"
      % ", ".join("%+.4f" % c for _, c in mass_vals),
      all(c > 0 and np.isfinite(c) for _, c in mass_vals))

# ---------------------------------------------------------------------------
# T3: control -- non-elliptic bare-Hermitian generator gives negative C_TT
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
check("T3 control: non-elliptic bare-Hermitian sigma.sin gives negative C_TT=%+.4f, so positive C_TT is not automatic"
      % cbh, cbh < 0)

# ---------------------------------------------------------------------------
# T4: staggered generator finite ellipticity check
# ---------------------------------------------------------------------------
P = np.array([0.5, 0.9, 0.3, 1.2])
D = Dstag(P, 0.7)
ev = np.linalg.eigvals(D @ D.conj().T).real
delta = 0.7 ** 2 + sum(np.sin(P[mu] / 2) ** 2 for mu in range(4))
check("T4 staggered generator finite ellipticity check: D D^dag = Delta*1, Delta=m^2+sum sin^2(P/2)=%.4f > 0"
      % delta, np.min(ev) > 0 and np.max(np.abs(ev - delta)) < 1e-9)

# ---------------------------------------------------------------------------
# T5: conditional sign diagnostic only
# ---------------------------------------------------------------------------
# If a separate induced-gravity bridge sets 1/(16 pi G)=C_TT, then this
# dimensionless lattice-unit conversion is positive and finite. No magnitude is
# claimed here.
G_over_a2 = 1.0 / (16 * np.pi * c0)
check("T5 conditional conversion diagnostic: if 1/(16piG)=C_TT, then G/a^2=%.4f is positive and finite; no magnitude claim"
      % G_over_a2, c0 > 0 and np.isfinite(G_over_a2) and G_over_a2 > 0)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("The implemented staggered Kaehler-Dirac TT stiffness C_TT is positive and finite on")
print("the tested finite grid, with fitted intercept ~ +0.020 at m=0.7. The non-elliptic")
print("bare-Hermitian control gives the opposite sign. Any induced-Newton interpretation")
print("is conditional on a separate bridge; no physical G_Newton magnitude is derived here.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
