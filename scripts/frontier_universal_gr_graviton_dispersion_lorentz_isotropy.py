"""Finite-grid induced-gravity TT-stiffness anisotropy diagnostic.

This runner checks a bounded, numerical surface only. It evaluates the
staggered Kahler-Dirac finite Brillouin-zone stress two-point function with a
fixed yz transverse-traceless polarization and compares:

* axis samples Khat=e0 and Khat=e1;
* the t-x diagonal sample against the axis sample;
* the finite-grid coefficient (C_diag/C_axis - 1) / k0^2 over N=6,8,10.

It does not establish a physical graviton dispersion relation, GR recovery,
observational gravitational-wave constraints, a Planck-suppressed prediction,
or an all-channel continuum theorem.
"""

AUDIT_TIMEOUT_SEC = 600

import itertools
import math

import numpy as np


corners = list(itertools.product([0, 1], repeat=4))
idx = {A: i for i, A in enumerate(corners)}


def eta(A, mu):
    return (-1) ** sum(A[nu] for nu in range(mu))


def flip(A, mu):
    B = list(A)
    B[mu] ^= 1
    return tuple(B)


def Dstag(P, m):
    D = np.zeros((16, 16), complex)
    for A in corners:
        a = idx[A]
        D[a, a] += m
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


def mom(P, K, nu):
    return np.sin(P[nu] + 0.5 * K[nu])


def Vst(P, K, mu, nu):
    return 0.5 * (
        Vel(P + 0.5 * K, mu) * mom(P, K, nu)
        + Vel(P + 0.5 * K, nu) * mom(P, K, mu)
    )


def epsV(P, K):
    return Vst(P, K, 2, 3) + Vst(P, K, 3, 2)


def Pi(K, N, m=0.7):
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    total = 0j
    for P0 in p:
        for P1 in p:
            for P2 in p:
                for P3 in p:
                    P = np.array([P0, P1, P2, P3])
                    G0 = Gi(P, m)
                    G1 = Gi(P + K, m)
                    total += np.trace(G0 @ epsV(P, K) @ G1 @ epsV(P + K, -K))
    return (total / N**4).real


def stiffnesses(N, m=0.7):
    """Return C_time, C_space, C_diag at k0=2*pi/N."""
    k0 = 2 * np.pi / N
    Pi0 = Pi(np.zeros(4), N, m)
    Kt = np.array([k0, 0, 0, 0.0])
    Ks = np.array([0, k0, 0, 0.0])
    Kd = np.array([k0, k0, 0, 0.0]) / np.sqrt(2)
    C_time = (Pi(Kt, N, m) - Pi0) / k0**2
    C_space = (Pi(Ks, N, m) - Pi0) / k0**2
    C_diag = (Pi(Kd, N, m) - Pi0) / k0**2
    return C_time, C_space, C_diag, k0


def check(results, name, ok, detail):
    results.append((name, bool(ok), detail))


def main():
    print("Finite-grid induced-gravity TT-stiffness anisotropy diagnostic")
    print("=" * 78)
    print("surface: staggered Kahler-Dirac 16x16 block, yz TT polarization, m=0.7")
    print("grids: N=6,8,10")
    print()

    data = {}
    for N in (6, 8, 10):
        data[N] = stiffnesses(N)

    print(f"{'N':>3s} {'k0':>8s} {'C_time':>12s} {'C_space':>12s} {'C_diag':>12s} {'diag/axis-1':>14s}")
    for N, (C_time, C_space, C_diag, k0) in data.items():
        aniso = C_diag / C_space - 1.0
        print(f"{N:3d} {k0:8.5f} {C_time:12.8f} {C_space:12.8f} {C_diag:12.8f} {aniso:14.8f}")
    print()

    results = []
    rel_axis = {
        N: abs(values[0] - values[1]) / max(abs(values[0]), 1e-30)
        for N, values in data.items()
    }
    check(
        results,
        "T1 axis samples agree on the tested grids",
        max(rel_axis.values()) < 1e-3,
        "relative diffs: " + ", ".join(f"N={N}:{rel_axis[N]:.2e}" for N in (6, 8, 10)),
    )

    aniso = {N: data[N][2] / data[N][1] - 1.0 for N in (6, 8, 10)}
    ks = [data[N][3] for N in (6, 8, 10)]
    av = [aniso[N] for N in (6, 8, 10)]
    power = math.log(av[2] / av[0]) / math.log(ks[2] / ks[0])
    check(
        results,
        "T2 diagonal excess is positive and decreases over the sampled grids",
        all(v > 0 for v in av) and av[2] < av[1] < av[0] and 1.6 < power < 2.4,
        "excess="
        + ", ".join(f"{v:.5f}" for v in av)
        + "; k0="
        + ", ".join(f"{k:.3f}" for k in ks)
        + f"; fitted power={power:.2f}",
    )

    coeffs = [aniso[N] / data[N][3] ** 2 for N in (6, 8, 10)]
    mean_coeff = float(np.mean(coeffs))
    spread = (max(coeffs) - min(coeffs)) / abs(mean_coeff)
    check(
        results,
        "T3 finite-grid anisotropy coefficient is stable on this sample",
        spread < 0.10,
        "coeffs="
        + ", ".join(f"{c:.5f}" for c in coeffs)
        + f"; mean={mean_coeff:.5f}; spread={100 * spread:.1f}%",
    )

    for name, ok, detail in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
        print(f"     {detail}")

    n_pass = sum(1 for _, ok, _ in results if ok)
    n_fail = sum(1 for _, ok, _ in results if not ok)
    print()
    print("Boundary: finite-grid channel diagnostic only. This runner does not decide")
    print("physical dispersion, GR recovery, GW-speed bounds, Planck suppression,")
    print("all-polarization closure, or an analytic continuum theorem.")
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
