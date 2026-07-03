"""Scalar Green tail and tensor stiffness shared-Laplacian diagnostic.

This runner checks a bounded shape comparison only:

* the scalar Z^3 graph Green function has a 1/(4 pi r) tail;
* the sampled tensor-channel response has positive finite stiffness;
* the sampled tensor response is approximately proportional to the one-axis
  lattice Laplacian symbol 2 - 2 cos(k).

It does not derive the absolute Newton constant, a GR tensor/source factor, an
observed value, or a physical tensor/scalar equality theorem.
"""

AUDIT_TIMEOUT_SEC = 360

import numpy as np
from scipy.integrate import quad
from scipy.special import ive


sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
sig = [sx, sy, sz]
I2 = np.eye(2, dtype=complex)

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))


def green(x):
    x = [abs(v) for v in x]
    f = lambda t: ive(x[0], 2 * t) * ive(x[1], 2 * t) * ive(x[2], 2 * t)
    val, _ = quad(f, 0, np.inf, limit=400)
    return val


def t1_scalar():
    g0 = green((0, 0, 0))
    tails = [4 * np.pi * r * green((r, 0, 0)) for r in (8, 16, 32)]
    check(
        "T1 scalar Z^3 graph Green function has 1/(4 pi r) tail",
        abs(g0 - 0.252731) < 1e-4 and all(abs(v - 1.0) < 0.02 for v in tails),
        f"G(0)={g0:.6f}; 4*pi*r*G(r)=" + ", ".join(f"{v:.4f}" for v in tails),
    )


def D(q, m):
    return 1j * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + m * I2


def Gi(q, m):
    return np.linalg.inv(D(q, m))


def u(q, k, i):
    return 1j * sig[i] * np.cos(q[i] + k[i] / 2)


def sbar(q, k, j):
    return 0.5 * (np.sin(q[j]) + np.sin(q[j] + k[j]))


def Vstress(q, k, i, j):
    return 0.5 * (u(q, k, i) * sbar(q, k, j) + u(q, k, j) * sbar(q, k, i))


def Pi_yz(kx, N, m=0.7):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    k = np.array([kx, 0.0, 0.0])
    total = 0j
    for qx in p:
        for qy in p:
            for qz in p:
                q = np.array([qx, qy, qz])
                Gq = Gi(q, m)
                Gqk = Gi(q + k, m)
                total += np.trace(Gq @ Vstress(q, k, 1, 2) @ Gqk @ Vstress(q + k, -k, 1, 2))
    return (total / N**3).real


def t2_t3_tensor():
    N = 10
    m = 0.7
    Pi0 = Pi_yz(0.0, N, m)
    k1 = 2 * np.pi / N
    C_TT = (Pi_yz(k1, N, m) - Pi0) / (2 - 2 * np.cos(k1))
    check(
        "T2 sampled tensor-channel stiffness is positive",
        C_TT > 0,
        f"C_TT={C_TT:+.5f} on N={N}, m={m}",
    )

    kin = []
    ratios = []
    for n in (1, 2):
        kx = n * 2 * np.pi / N
        delta = Pi_yz(kx, N, m) - Pi0
        lap = 2 - 2 * np.cos(kx)
        kin.append(delta)
        ratios.append(delta / lap)
    spread = abs(ratios[1] - ratios[0]) / abs(ratios[0])
    check(
        "T3 sampled tensor response follows the lattice-Laplacian shape",
        all(delta > 0 for delta in kin) and ratios[0] > 0 and spread < 0.25,
        f"ratios={ratios[0]:+.5f}, {ratios[1]:+.5f}; finite-grid spread={100 * spread:.1f}%",
    )


t1_scalar()
t2_t3_tensor()

n_pass = sum(1 for _, ok, _ in results if ok)
n_fail = sum(1 for _, ok, _ in results if not ok)
for name, ok, detail in results:
    print(("PASS" if ok else "FAIL"), name)
    print(f"     {detail}")
print()
print("Boundary: shared graph-Laplacian shape diagnostic only. This runner does not")
print("derive absolute G, a GR tensor/source factor, observed equality, or nonlinear closure.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
