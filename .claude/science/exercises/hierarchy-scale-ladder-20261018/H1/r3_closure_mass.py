"""R3: does constraint closure (the campaign's fourth tool) see on-site masses?

Own-code check of prior campaign results (B14 E2a scalar; B15 T5/T6a Dirac):
the lattice bracket {H(N), H(M)} of lapse-smeared matter Hamiltonians is
independent of an on-site mass term, so closure can fix cones but not masses.
Scalar: classical Poisson bracket of quadratic forms, {z^T A z/2, z^T B z/2} = z^T A J B z.
Dirac: one-body commutator [h(N), h(M)] (second quantization maps it to the
operator commutator of the quadratic Hamiltonians).
Controls: bond timing t != 1/2, and a Wilson-type hop (commutes with beta).
"""
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(("PASS" if ok else "FAIL"), name, detail)


rng = np.random.default_rng(7)
L = 4
sites = list(itertools.product(range(L), repeat=3))
idx = {s: i for i, s in enumerate(sites)}
V = len(sites)
E = np.eye(3, dtype=int)


def nb(s, e):
    return tuple((np.array(s) + E[e]) % L)


def scalar_A(N, mu, c=1.0, t=0.5):
    A = np.zeros((2 * V, 2 * V))
    for s in sites:
        i = idx[s]
        A[V + i, V + i] += N[i]            # pi^2/2
        A[i, i] += mu * N[i]               # mu phi^2/2
        for e in range(3):
            j = idx[nb(s, e)]
            Nb = (1 - t) * N[i] + t * N[j]
            # (c/2) Nb (phi_j - phi_i)^2
            A[i, i] += c * Nb
            A[j, j] += c * Nb
            A[i, j] -= c * Nb
            A[j, i] -= c * Nb
    return A


J = np.block([[np.zeros((V, V)), np.eye(V)], [-np.eye(V), np.zeros((V, V))]])


def pb(A, B):
    C = A @ J @ B
    return 0.5 * (C + C.T)


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0 + 0j, -1.0])
i2 = np.eye(2)
alpha = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz)]
beta = np.kron(sz, i2)


def dirac_h(N, m, t=0.5, r=0.0):
    h = np.zeros((4 * V, 4 * V), complex)
    for s in sites:
        i = idx[s]
        h[4 * i:4 * i + 4, 4 * i:4 * i + 4] += N[i] * (m * beta + 3 * r * beta)
        for e in range(3):
            j = idx[nb(s, e)]
            Nb = (1 - t) * N[i] + t * N[j]
            T = Nb * (-0.5j * alpha[e] - 0.5 * r * beta)
            h[4 * i:4 * i + 4, 4 * j:4 * j + 4] += T
            h[4 * j:4 * j + 4, 4 * i:4 * i + 4] += T.conj().T
    return h


def comm(a, b):
    return a @ b - b @ a


for trial in range(3):
    N = 1 + 0.3 * rng.standard_normal(V)
    M = 1 + 0.3 * rng.standard_normal(V)
    # scalar
    d = {}
    for t in (0.5, 0.3):
        b0 = pb(scalar_A(N, 0.0, t=t), scalar_A(M, 0.0, t=t))
        b1 = pb(scalar_A(N, 1.7, t=t), scalar_A(M, 1.7, t=t))
        d[t] = np.abs(b1 - b0).max()
    check(f"scalar trial {trial}: on-site mass drops out of {{H(N),H(M)}} (any timing)",
          d[0.5] < 1e-12 and d[0.3] < 1e-12, f"max |diff| t=1/2: {d[0.5]:.1e}, t=0.3: {d[0.3]:.1e}")
    # Dirac, naive hop
    dd = {}
    for t in (0.5, 0.3):
        c0 = comm(dirac_h(N, 0.0, t=t), dirac_h(M, 0.0, t=t))
        c1 = comm(dirac_h(N, 0.9, t=t), dirac_h(M, 0.9, t=t))
        dd[t] = np.abs(c1 - c0).max()
    check(f"Dirac trial {trial}: mass drops out at endpoint-mean timing, not at t=0.3",
          dd[0.5] < 1e-12 and dd[0.3] > 1e-3, f"max |diff| t=1/2: {dd[0.5]:.1e}, t=0.3: {dd[0.3]:.2e}")
    # Wilson-type hop control (hop commutes with beta): mass cross term survives
    w0 = comm(dirac_h(N, 0.0, r=1.0), dirac_h(M, 0.0, r=1.0))
    w1 = comm(dirac_h(N, 0.9, r=1.0), dirac_h(M, 0.9, r=1.0))
    # the r-term itself is beta-proportional, so the check is: is the mass-dependent part zero?
    check(f"Dirac trial {trial}: control, Wilson-type hop keeps a mass-dependent bracket term",
          np.abs(w1 - w0).max() > 1e-3, f"max |diff| {np.abs(w1 - w0).max():.2e}")

# The mass-independent part is NOT zero (the bracket is the momentum constraint): sanity
N = 1 + 0.3 * rng.standard_normal(V)
M = 1 + 0.3 * rng.standard_normal(V)
check("sanity: bracket itself nonzero for nonconstant lapses",
      np.abs(comm(dirac_h(N, 0.9), dirac_h(M, 0.9))).max() > 1e-2 and np.abs(pb(scalar_A(N, 1.0), scalar_A(M, 1.0))).max() > 1e-2)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
