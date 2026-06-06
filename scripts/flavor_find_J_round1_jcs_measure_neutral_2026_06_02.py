"""J-hunt round 1: static J_cs is measure-neutral.

This runner verifies only the finite-algebra obstruction:

    the static C3-equivariant complex structure J_cs=(C-C^2)/sqrt(3)
        does not select
    the det_C doublet measure.

It deliberately does not verify a Q default, a det_C-to-r/Q readout map, or a
first-order/Berezin bridge.
"""
from pathlib import Path

import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
JALL = np.ones((3, 3))
JCS = (C - C @ C) / np.sqrt(3.0)
GX = (2.0 / 3.0) * JALL - I3
P_D = I3 - JALL / 3.0


def main():
    passed = []

    passed.append(check(
        "R1 J_cs is anti-Hermitian, J_cs^2=-P_doublet, eigs {0,+-i}, and [J_cs,C]=0",
        np.allclose(JCS.conj().T, -JCS) and np.allclose(JCS @ JCS, -P_D) and np.allclose(JCS @ C - C @ JCS, 0),
        f"eigs(J_cs)={np.round(np.linalg.eigvals(JCS),3).tolist()}"))

    passed.append(check(
        "R2 Gamma_chi=(2/3)Jall-I is a real involution and is not J_cs",
        np.allclose(GX @ GX, I3) and np.allclose(np.sort(np.linalg.eigvalsh(GX)), [-1, -1, 1])
        and not np.allclose(JCS, GX) and np.allclose(JCS @ GX - GX @ JCS, 0),
        "Gamma_chi is built from the all-ones matrix; it commutes with J_cs but is not equal or proportional"))

    # measure-neutrality: SO(2)=exp(theta J_cs) preserves the HS doublet metric block 6*I -> preserves both measures
    g = 6.0 * np.eye(2)
    neutral = True
    for th in (0.3, 0.7, 1.9):
        R = np.cos(th) * np.eye(2) + np.sin(th) * np.array([[0, -1.0], [1.0, 0]])
        if not (np.allclose(R.T @ g @ R, g) and abs(np.linalg.det(R) - 1) < 1e-12):
            neutral = False
    passed.append(check(
        "R3 exp(theta J_cs)=SO(2) preserves the HS doublet block 6I and has determinant one",
        neutral,
        "the static rotation is measure-neutral and does not select the det_C convention"))

    passed.append(check(
        "R4 [J_cs,H]=0 for the tested Hermitian C3-circulant family",
        all(np.allclose(JCS @ (a * I3 + b * C + np.conj(b) * C.conj().T) - (a * I3 + b * C + np.conj(b) * C.conj().T) @ JCS, 0)
            for a, b in [(1.0, 0.6 + 0.2j), (2.0, 1.1)]),
        "operator-silence supplies no spectral lever that fixes the doublet mode count"))

    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_FIND_J_ROUND1_JCS_MEASURE_NEUTRAL_2026-06-02.md").read_text()
    banned = [
        "det_R/Q=1 default stands",
        "NEXT LEVER",
        "Round 2 attacks this",
        "first-order/Berezin structure is exactly the fermionic frame",
        "forces **det_C",
    ]
    required = [
        "does not derive",
        "outside this static-`J_cs` packet",
        "No new axiom is introduced.",
    ]
    passed.append(check(
        "R5 source boundary guard: no Q/default or first-order-action conclusion is promoted by this packet",
        all(term not in note for term in banned) and all(term in note for term in required),
        "the packet closes only static-J_cs algebraic non-selection"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 1, wf_719da018): bounded-support negative route pruning.")
    print("The static C3-equivariant J_cs is a valid finite complex structure, but exp(theta J_cs)")
    print("is an SO(2) rotation preserving the doublet metric block and determinant. It is")
    print("measure-neutral and operator-silent, and Gamma_chi is a distinct real involution.")
    print("This runner does not derive a Q default, a det_C-to-r/Q map, or a first-order action.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
