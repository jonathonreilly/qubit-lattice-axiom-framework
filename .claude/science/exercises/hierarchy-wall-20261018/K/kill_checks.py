"""KILL-round spot checks (small; numpy/scipy only).

K1  R1 Lemma B: the clockwork mass matrix has a REVERSAL-SYMMETRIC bulk; its
    one-ended zero mode comes from asymmetric end terms only.  R1's "w = 1"
    partner test doubles the bulk and symmetrises the ends at once.
K2  R1 Lemma A wording: a translation + bond-reversal covariant qubit chain
    (Creutz-type) has compact localised eigenstates (flat band) - localised
    modes without a privileged site, inside a degenerate multiplet.
K3  R2 detuning: the two natural D2 = 0 rule classes (XOR-linear, exactly-k
    totalistic) admit NO finite valid flip (GF(2) / real nullity in a box).
K4  R4 Lemma A: equal leading rates with a linear prefactor put the balance
    point at N* ~ ratio of two O(1) amplitudes, outside the stated bound.
K5  R4 spiral / T-SPIRAL criterion: passage time vs Re y and Im y for a
    weak focus with O(1) quadratic terms.
"""
import itertools
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

LSTAR = 38.4

# ---------------- K1 -------------------------------------------------------
N, q = 20, 2.0
M = np.zeros((N, N + 1))
for j in range(N):
    M[j, j], M[j, j + 1] = 1.0, -q
K = M.T @ M
bulk = K[1:-1, 1:-1]
Rev = np.eye(N - 1)[::-1]
print("[K1] clockwork K=M^T M: bulk diag", np.unique(np.round(np.diag(bulk), 12)),
      "offdiag", np.unique(np.round(np.diag(bulk, 1), 12)),
      " bulk reversal-symmetric:", np.allclose(Rev @ bulk @ Rev, bulk))
print(f"[K1] end diagonals: K00={K[0,0]:.3f}, KNN={K[-1,-1]:.3f} (bulk {1+q*q:.3f})")
# symmetric bulk, ends fixed by hand -> exact zero mode q^-j
Kb = (1 + q * q) * np.eye(N + 1) - q * (np.eye(N + 1, k=1) + np.eye(N + 1, k=-1))
for (a, b), lab in [((1.0, q * q), "clockwork ends (1, q^2)"),
                    ((1 + q * q, 1 + q * q), "symmetric ends"),
                    ((1.0, 1.0), "symmetric ends (1, 1)")]:
    Kt = Kb.copy(); Kt[0, 0], Kt[-1, -1] = a, b
    e, V = np.linalg.eigh(Kt)
    z = V[:, 0]
    print(f"[K1] symmetric bulk + {lab:24s}: lambda_min={e[0]:+.3e}, |phi_N/phi_0|={abs(z[-1]/z[0]):.3e}")
# R1's w=1 partner matrix vs 2*bulk
W = np.zeros((N + 1, N + 1))
for j in range(N):
    v = np.zeros(N + 1); v[j], v[j + 1] = 1, -q; W += np.outer(v, v)
    u = np.zeros(N + 1); u[j + 1], u[j] = 1, -q; W += np.outer(u, u)
print("[K1] R1 w=1 matrix: bulk equals 2x clockwork bulk:",
      np.allclose(W[1:-1, 1:-1], 2 * bulk), f"; ends {W[0,0]:.1f},{W[-1,-1]:.1f} (symmetric)")

# ---------------- K2 -------------------------------------------------------
L = 16
T = np.array([[1j, 1], [1, -1j]])
sx = np.array([[0, 1], [1, 0]])
print("[K2] reversal covariance  sx T sx == T^dag:", np.allclose(sx @ T @ sx, T.conj().T))
H = np.zeros((2 * L, 2 * L), complex)
for j in range(L):
    k = (j + 1) % L
    H[2*k:2*k+2, 2*j:2*j+2] += T
    H[2*j:2*j+2, 2*k:2*k+2] += T.conj().T
e, V = np.linalg.eigh(H)
print("[K2] spectrum values:", np.unique(np.round(e, 10)))
P = V[:, e < 0] @ V[:, e < 0].conj().T          # flat band -2 projector
psi = P[:, 2 * 5]                                # project a site-5 orbital
w = np.sum(np.abs(psi.reshape(L, 2)) ** 2, axis=1); w /= w.sum()
print("[K2] projected state weight by site (nonzero):",
      {i: round(x, 3) for i, x in enumerate(w) if x > 1e-12},
      " eigen-residual:", f"{np.linalg.norm(H @ psi + 2 * psi):.1e}")

# ---------------- K3 -------------------------------------------------------
def gf2_rank(A):
    A = A.copy() % 2; r = 0
    rows, cols = A.shape
    for c in range(cols):
        piv = np.nonzero(A[r:, c])[0]
        if piv.size == 0: continue
        p = r + piv[0]; A[[r, p]] = A[[p, r]]
        for i in range(rows):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
        if r == rows: break
    return r

n = 5
box = list(itertools.product(range(n), repeat=3)); bi = {s: i for i, s in enumerate(box)}
shell = list(itertools.product(range(-1, n + 1), repeat=3))
nbr = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
C = np.zeros((len(shell), len(box)), dtype=np.int64)
for r_, x in enumerate(shell):
    for d in nbr:
        y = tuple(x[i] + d[i] for i in range(3))
        if y in bi: C[r_, bi[y]] = 1
print(f"[K3] XOR rule, finite flips inside {n}^3: GF(2) nullity = {len(box) - gf2_rank(C)}")
print(f"[K3] exactly-k totalistic rule, balanced signed flips inside {n}^3: real nullity = "
      f"{len(box) - np.linalg.matrix_rank(C.astype(float))}")

# ---------------- K4 -------------------------------------------------------
for a, b in [(10.0, -0.1), (5.0, -0.125), (3.0, -0.1)]:
    F = lambda x: (a + b * x) * np.exp(-x) + 1.0 * np.exp(-1.5 * x)
    Ns = brentq(lambda x: F(x) * np.exp(x), 2, 400)
    print(f"[K4] F=({a}{b:+}N)e^-N + e^-1.5N: N*={Ns:.2f}, kappa N*={Ns:.1f} "
          f"(R={max(abs(a),1/abs(b)):.0f}; stated bound ln((J-1)R^2)/Delta = "
          f"{np.log(2*max(abs(a),1/abs(b))**2)/0.5:.1f} assumes distinct leading rate)")

# ---------------- K5 -------------------------------------------------------
def passage(sig, om, bq, r0=0.3, r1=3.0, tmax=4000):
    # dz/dt = (sig + i om) z + bq (z^2 + 2 z zbar + zbar^2)/2 ... O(1) generic quadratic part
    def f(t, u):
        z = u[0] + 1j * u[1]
        dz = (sig + 1j * om) * z + bq * (0.7 * z * z + 0.4j * z * np.conj(z) - 0.5 * np.conj(z) ** 2)
        return [dz.real, dz.imag]
    ev = lambda t, u: np.hypot(u[0], u[1]) - r1; ev.terminal = True
    s = solve_ivp(f, (0, tmax), [r0, 0.0], events=ev, rtol=1e-8, atol=1e-10, max_step=0.05)
    return s.t_events[0][0] if s.status == 1 else np.inf

print("[K5] passage time r: 0.3 -> 3 (L* = 38.4); quadratic strength bq = 1")
for sig, om in [(0.03, 0.0), (0.03, 0.3), (0.03, 3.0), (0.03, 30.0),
                (0.5, 20.0), (0.5, 100.0), (0.01, 3.0), (0.06, 3.0)]:
    T_ = passage(sig, om, 1.0)
    print(f"[K5]   Re y={sig:<5} Im y={om:<6} Re/|Im|={(sig/om if om else np.inf):<8.4g} T={T_:8.2f}"
          f"   ln(10)/Re = {np.log(10)/sig:7.1f}")
