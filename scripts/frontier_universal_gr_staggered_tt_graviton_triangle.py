"""Finite TT-projected staggered stress-triangle support.

This runner tests a narrow, bounded claim:

* for non-collinear lattice momenta, the staggered Kaehler-Dirac fermion has
  nonzero paramagnetic stress three-point functions after all three external
  tensor legs are projected to transverse-traceless (TT) polarizations;
* selected two-component Cl(3) control channels vanish on the same TT-projected
  kinematics; and
* this runner does not establish all-same-helicity vanishing, a quantitative
  Einstein-Hilbert cubic match, or the cubic diffeomorphism Ward identity.

The result is support for a pure-TT cubic ingredient on the proper staggered
fermion, not a full cubic Einstein-Hilbert closure.
"""

from __future__ import annotations

import itertools

import numpy as np

AUDIT_TIMEOUT_SEC = 480

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ---------------------------------------------------------------------------
# Staggered Kaehler-Dirac (16x16 hypercube/spin-taste block)
# ---------------------------------------------------------------------------
CORNERS = list(itertools.product([0, 1], repeat=4))
CIDX = {A: i for i, A in enumerate(CORNERS)}


def eta(A: tuple[int, ...], mu: int) -> int:
    return (-1) ** sum(A[nu] for nu in range(mu))


def flip(A: tuple[int, ...], mu: int) -> tuple[int, ...]:
    B = list(A)
    B[mu] ^= 1
    return tuple(B)


def Dstag(P: np.ndarray, m: float) -> np.ndarray:
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


def Vel(P: np.ndarray, i: int) -> np.ndarray:
    D = np.zeros((16, 16), complex)
    for A in CORNERS:
        a = CIDX[A]
        if A[i] == 0:
            D[a, CIDX[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(-1j * P[i]))
        else:
            D[a, CIDX[flip(A, i)]] += 0.5 * eta(A, i) * (1j * np.exp(1j * P[i]))
    return D


def GiS(P: np.ndarray, m: float) -> np.ndarray:
    return np.linalg.inv(Dstag(P, m))


def momS(Pj: float, Kj: float) -> float:
    return np.sin(0.5 * (Pj + 0.5 * Kj))


def epsVst(P: np.ndarray, K: np.ndarray, Emat: np.ndarray) -> np.ndarray:
    Pm = P + 0.5 * K
    M = np.zeros((16, 16), complex)
    for i in range(1, 4):
        for j in range(1, 4):
            if abs(Emat[i - 1, j - 1]) < 1e-15:
                continue
            M += Emat[i - 1, j - 1] * 0.5 * (
                Vel(Pm, i) * momS(P[j], K[j]) + Vel(Pm, j) * momS(P[i], K[i])
            )
    return M


def tri_stag(K1: np.ndarray, K2: np.ndarray, E1: np.ndarray, E2: np.ndarray, E3: np.ndarray,
             N: int, m: float = 0.7) -> complex:
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    K3 = -(K1 + K2)
    t = 0j
    for a0 in p:
        for a1 in p:
            for a2 in p:
                for a3 in p:
                    P = np.array([a0, a1, a2, a3])
                    t += np.trace(
                        GiS(P, m)
                        @ epsVst(P, K1, E1)
                        @ GiS(P + K1, m)
                        @ epsVst(P + K1, K2, E2)
                        @ GiS(P + K1 + K2, m)
                        @ epsVst(P + K1 + K2, K3, E3)
                    )
    return t / N ** 4


# ---------------------------------------------------------------------------
# 2-component Cl(3) control, with the same TT tensor contractions
# ---------------------------------------------------------------------------
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
sig = [sx, sy, sz]


def Gi2(q: np.ndarray, m: float) -> np.ndarray:
    return np.linalg.inv(1j * (sig[0] * np.sin(q[0]) + sig[1] * np.sin(q[1]) + sig[2] * np.sin(q[2])) + m * I2)


def sb(qi: float, ki: float) -> float:
    return 0.5 * (np.sin(qi) + np.sin(qi + ki))


def epsV2(q: np.ndarray, k: np.ndarray, Emat: np.ndarray) -> np.ndarray:
    M = np.zeros((2, 2), complex)
    for c in range(3):
        for d in range(3):
            if abs(Emat[c, d]) < 1e-15:
                continue
            M += Emat[c, d] * 1j * 0.5 * (
                sig[c] * np.cos(q[c] + k[c] / 2) * sb(q[d], k[d])
                + sig[d] * np.cos(q[d] + k[d] / 2) * sb(q[c], k[c])
            )
    return M


def tri_2c(k1: np.ndarray, k2: np.ndarray, E1: np.ndarray, E2: np.ndarray, E3: np.ndarray,
           N: int, m: float = 0.7) -> complex:
    p = np.linspace(-np.pi, np.pi, N, endpoint=False)
    k3 = -(k1 + k2)
    t = 0j
    for qx in p:
        for qy in p:
            for qz in p:
                q = np.array([qx, qy, qz])
                t += np.trace(
                    Gi2(q, m)
                    @ epsV2(q, k1, E1)
                    @ Gi2(q + k1, m)
                    @ epsV2(q + k1, k2, E2)
                    @ Gi2(q + k1 + k2, m)
                    @ epsV2(q + k1 + k2, k3, E3)
                )
    return t / N ** 3


def tt_polarizations(k: np.ndarray) -> dict[str, np.ndarray]:
    khat = np.asarray(k, dtype=float)
    khat = khat / np.linalg.norm(khat)
    seed = np.array([0.0, 0.0, 1.0]) if abs(khat[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    u = seed - np.dot(seed, khat) * khat
    u = u / np.linalg.norm(u)
    v = np.cross(khat, u)
    v = v / np.linalg.norm(v)
    plus = np.outer(u, u) - np.outer(v, v)
    cross = np.outer(u, v) + np.outer(v, u)
    return {
        "plus": plus,
        "cross": cross,
        "right": plus + 1j * cross,
        "left": plus - 1j * cross,
    }


def tt_ok(k: np.ndarray, E: np.ndarray) -> bool:
    return np.allclose(np.trace(E), 0, atol=1e-12) and np.allclose(k @ E, np.zeros(3), atol=1e-12)


def main() -> int:
    print("TT-PROJECTED STAGGERED STRESS-TRIANGLE SUPPORT")
    print("=" * 72)

    N6 = 6
    a6 = 2 * np.pi / N6
    K1 = np.zeros(4)
    K2 = np.zeros(4)
    K1[1] = a6
    K2[2] = a6
    k1 = K1[1:4]
    k2 = K2[1:4]
    k3 = -(k1 + k2)
    P1 = tt_polarizations(k1)
    P2 = tt_polarizations(k2)
    P3 = tt_polarizations(k3)

    all_tt = all(
        tt_ok(k, E)
        for k, pols in [(k1, P1), (k2, P2), (k3, P3)]
        for E in [pols["plus"], pols["cross"]]
    )
    check(
        "T1 all tested external legs are genuine TT tensors for their own momenta",
        all_tt,
        "trace(E)=0 and k.E=0 for plus/cross bases on k1, k2, and k3=-(k1+k2)",
    )

    channels = [
        ("plus,cross,cross", P1["plus"], P2["cross"], P3["cross"]),
        ("cross,plus,cross", P1["cross"], P2["plus"], P3["cross"]),
        ("cross,cross,plus", P1["cross"], P2["cross"], P3["plus"]),
    ]
    stag6 = {name: tri_stag(K1, K2, E1, E2, E3, N6).real for name, E1, E2, E3 in channels}
    check(
        "T2 staggered TT-projected mixed channels are nonzero at N=6",
        min(abs(v) for v in stag6.values()) > 1e-2,
        ", ".join(f"{name}={value:+.5f}" for name, value in stag6.items()),
    )

    N8 = 8
    a8 = 2 * np.pi / N8
    K1b = np.zeros(4)
    K2b = np.zeros(4)
    K1b[1] = a8
    K2b[2] = a8
    P1b = tt_polarizations(K1b[1:4])
    P2b = tt_polarizations(K2b[1:4])
    P3b = tt_polarizations(-(K1b[1:4] + K2b[1:4]))
    channels8 = [
        ("plus,cross,cross", P1b["plus"], P2b["cross"], P3b["cross"]),
        ("cross,plus,cross", P1b["cross"], P2b["plus"], P3b["cross"]),
        ("cross,cross,plus", P1b["cross"], P2b["cross"], P3b["plus"]),
    ]
    stag8 = {name: tri_stag(K1b, K2b, E1, E2, E3, N8).real for name, E1, E2, E3 in channels8}
    check(
        "T3 nonzero TT support persists under one Brillouin-zone refinement",
        min(abs(v) for v in stag8.values()) > 1e-2,
        ", ".join(f"{name}={value:+.5f}" for name, value in stag8.items()),
    )

    control = {
        name: tri_2c(k1, k2, E1, E2, E3, N6)
        for name, E1, E2, E3 in channels
    }
    check(
        "T4 selected two-component Cl(3) TT control channels vanish while staggered channels do not",
        max(abs(v) for v in control.values()) < 1e-10
        and min(abs(v) for v in stag6.values()) > 1e-2,
        ", ".join(f"{name}: 2c={value.real:+.2e}" for name, value in control.items()),
    )

    same_helicity = tri_stag(K1, K2, P1["right"], P2["right"], P3["right"], N6)
    check(
        "T5 guardrail: this runner does not prove all-same-helicity vanishing",
        abs(same_helicity) > 1e-2,
        f"right,right,right at N=6 has |amplitude|={abs(same_helicity):.5f}",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the proper staggered Kaehler-Dirac fermion has nonzero finite-momentum, "
        "TT-projected paramagnetic stress three-point channels, with selected two-component "
        "controls vanishing on the same TT kinematics. This supports a W-native pure-TT cubic "
        "ingredient. It does not establish all-same-helicity vanishing, a quantitative "
        "Einstein-Hilbert cubic match, the cubic diffeomorphism Ward identity, or nonlinear GR closure."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
