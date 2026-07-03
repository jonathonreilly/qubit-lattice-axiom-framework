"""Finite W-native conformal-mode sign diagnostic.

This memory-safe runner constructs the finite Brillouin-zone stress-bubble
kinetic matrix

    M_(mu nu),(rho sigma) = [Pi_mu nu,rho sigma(k) - Pi_mu nu,rho sigma(0)] / k^2

for the staggered Kahler-Dirac stress vertex over all ten symmetric metric
components. It tests a narrow finite-matrix statement:

  T1  the normalized pure-trace quadratic form is positive in the tested
      finite setup. This shows that the one-vector trace probe is not a
      decisive substitute for diagonalizing the coupled matrix.
  T2  the metric-weighted 10x10 matrix at N=6 has exactly one eigenvalue below
      -1e-4. Its eigenvector has nontrivial trace/conformal overlap and
      negligible overlap against the tested yz transverse-traceless vector.
  T3  the lowest eigenvalue magnitude shrinks from N=4 to N=6, and the
      runner-defined transverse projected 6x6 block has no eigenvalue below
      -5e-3.

BOUNDED: this runner does not prove a continuum Hamiltonian constraint, exact
two-DOF graviton counting, scalar-tensor exclusion, fifth-force exclusion, or
any cosmological-constant coupling theorem. It supplies a finite sign/character
diagnostic for later continuum and Ward-identity work.

prints TOTAL: PASS=N FAIL=0
"""

AUDIT_TIMEOUT_SEC = 360

import numpy as np
import itertools

corners = list(itertools.product([0, 1], repeat=4))
idx = {A: i for i, A in enumerate(corners)}
def eta(A, mu):
    return (-1) ** sum(A[nu] for nu in range(mu))
def flip(A, mu):
    B = list(A); B[mu] ^= 1; return tuple(B)
def Dstag(P, m):
    D = np.zeros((16, 16), complex)
    for A in corners:
        a = idx[A]; D[a, a] += m
        for mu in range(4):
            if A[mu] == 0:
                D[a, idx[flip(A, mu)]] += 0.5 * eta(A, mu) * (1 - np.exp(-1j * P[mu]))
            else:
                D[a, idx[flip(A, mu)]] += 0.5 * eta(A, mu) * (np.exp(1j * P[mu]) - 1)
    return D
def Vel(P, i):
    D = np.zeros((16, 16), complex)
    for A in corners:
        a = idx[A]
        if A[i] == 0:
            D[a, idx[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(-1j * P[i]))
        else:
            D[a, idx[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(1j * P[i]))
    return D
def Gi(P, m):
    return np.linalg.inv(Dstag(P, m))
def momk(P, K, nu):
    return np.sin(P[nu] + 0.5 * K[nu])
def Vst(P, K, mu, nu):
    return 0.5 * (Vel(P + 0.5 * K, mu) * momk(P, K, nu) + Vel(P + 0.5 * K, nu) * momk(P, K, mu))

pairs = [(mu, nu) for mu in range(4) for nu in range(mu, 4)]

results = []
def check(name, ok):
    results.append((name, bool(ok)))

def PiMat(K, N, m=0.7):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    M = np.zeros((10, 10), complex)
    for P0 in p:
        for P1 in p:
            for P2 in p:
                for P3 in p:
                    P = np.array([P0, P1, P2, P3]); G0 = Gi(P, m); G1 = Gi(P + K, m)
                    Vs = [G0 @ Vst(P, K, a, b) @ G1 for (a, b) in pairs]
                    Vsm = [Vst(P + K, -K, a, b) for (a, b) in pairs]
                    for I in range(10):
                        for J in range(10):
                            M[I, J] += np.trace(Vs[I] @ Vsm[J])
    return (M / N ** 4).real

def kinmat(N, m=0.7):
    k0 = 2 * np.pi / N; K = np.array([0, k0, 0, 0.0])
    M = (PiMat(K, N, m) - PiMat(np.zeros(4), N, m)) / k0 ** 2
    w = np.array([1.0 if a == b else np.sqrt(2.0) for (a, b) in pairs])
    Mw = M * np.outer(w, w)
    return 0.5 * (Mw + Mw.T), w

# ---------------------------------------------------------------------------
# T1: the isolated pure-trace quadratic form is positive.
Mw6, w = kinmat(6)
trace_dir = np.array([1.0 if a == b else 0.0 for (a, b) in pairs]) * w
trace_dir /= np.linalg.norm(trace_dir)
naive_trace_kin = trace_dir @ Mw6 @ trace_dir
check("T1 finite pure-trace probe: <trace|M|trace> = %+.4f POSITIVE (single-vector trace probe is not decisive for the coupled 10x10 matrix)"
      % naive_trace_kin, naive_trace_kin > 0)

# T2: coupled-matrix diagonalization finds one negative eigenvalue.
ev, vec = np.linalg.eigh(Mw6)
nneg = int(np.sum(ev < -1e-4))
v = vec[:, 0]
tt_dir = np.array([1.0 if (a, b) == (2, 3) else 0.0 for (a, b) in pairs]) * w; tt_dir /= np.linalg.norm(tt_dir)
ov_trace = abs(v @ trace_dir); ov_tt = abs(v @ tt_dir)
check("T2 finite 10x10 diagonalization: exactly %d negative eigenvalue below -1e-4 (ev=%.4f), |overlap with trace/conformal|=%.2f, |overlap with TT-yz|=%.3f"
      % (nneg, ev[0], ov_trace, ov_tt), nneg == 1 and ov_trace > 0.3 and ov_tt < 0.05)

# T3: the lowest eigenvalue magnitude shrinks, while the tested transverse block stays nonnegative.
Mw4, w4 = kinmat(4)
ev4 = np.linalg.eigvalsh(Mw4)
shrinks = abs(ev[0]) < abs(ev4[0])
gauge_idx = [i for i, (a, b) in enumerate(pairs) if a == 1 or b == 1]
trans_idx = [i for i in range(10) if i not in gauge_idx]
evt = np.linalg.eigvalsh(Mw6[np.ix_(trans_idx, trans_idx)])
trans_allpos = int(np.sum(evt < -5e-3)) == 0
check("T3 lowest eigenvalue magnitude shrinks from N=4 to N=6 (N=4:%.4f -> N=6:%.4f) and the runner-defined transverse 6x6 sector has no eigenvalue below -5e-3 (%s)"
      % (ev4[0], ev[0], np.array2string(np.round(np.sort(evt), 3))), shrinks and trans_allpos)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("Finite diagnostic: the normalized pure-trace probe is positive, but the full metric-weighted")
print("10x10 matrix has exactly one opposite-signed eigen-direction with nontrivial trace/conformal")
print("character and negligible tested yz TT overlap. Its magnitude shrinks from N=4 to N=6, while")
print("the runner-defined transverse projected block has no eigenvalue below the stated threshold.")
print("This is finite sign/character support only. It is not a continuum Hamiltonian-constraint")
print("theorem, exact two-DOF theorem, scalar-tensor exclusion, fifth-force statement, or")
print("cosmological-constant coupling theorem.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
