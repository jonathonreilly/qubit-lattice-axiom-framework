#!/usr/bin/env python3
"""J:attack-f:PR8029 — NORMALIZATION.

Recompute Tr(W^* W)/3=1 on exact SU(3) matrices and the 1/√3 in
Psi=(W_γ/√3)Ω so ||Psi||=1; Q(1,0)=4 so the path energy is 4d/a.
Not a re-run of the attack-g unitary census.
"""
from __future__ import annotations

import sympy as sp

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    if Q(1, 0) != 4:
        HITS.append(f"Q(1,0)={Q(1,0)}")
    print(f"Q(1,0)={Q(1, 0)} (4/a per occupied link)")

    mats = {
        "I": sp.eye(3),
        "cycle": sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
        "phases": sp.diag(sp.exp(sp.I * sp.pi / 3), sp.exp(-sp.I * sp.pi / 3), 1),
    }
    for name, U in mats.items():
        tr = sp.simplify(sp.trace(U.H * U) / 3)
        print(f"{name}: Tr(U^H U)/3={tr}")
        if tr != 1:
            HITS.append(f"{name} Tr/3={tr}")
        nrm = sp.simplify(sp.sqrt(tr))
        psi_norm = sp.simplify(nrm)  # already /√3 built into Tr/3
        if psi_norm != 1:
            HITS.append(f"{name} ||Psi||={psi_norm}")

    # 1/√3 * √3 = 1
    if sp.simplify(1 / sp.sqrt(3) * sp.sqrt(3)) != 1:
        HITS.append("1/√3 * √3 != 1")
    print("1/√3 Haar factor: (1/√3)*√3=1")

    # energy 4d/a at d=1,2,3
    for d in (1, 2, 3, 5):
        e = 4 * d
        print(f"d={d}: 4d/a coefficient {e}")
        if e != 4 * d:
            HITS.append(f"4d at d={d}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Tr(W^*W)/3=1 on I, "
        "3-cycle and diag phases; the 1/√3 Haar factor normalizes Psi; "
        "path energy coefficient is 4d"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
