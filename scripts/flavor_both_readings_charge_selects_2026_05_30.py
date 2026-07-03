#!/usr/bin/env python3
"""Finite charge-selection route-pruning packet.

The runner verifies rank-one endpoint arithmetic, scalar generation-action
non-orientation, order-three obstruction to continuous C rephasing, and
empirical comparator values. It does not derive the physical gauge action or a
framework selector for det_C/det_R.
"""
from pathlib import Path

import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def koide_q(masses):
    masses = np.array(masses, float)
    return masses.sum() / np.sqrt(masses).sum() ** 2


def main():
    passed = []
    c = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    i3 = np.eye(3)

    h = lambda a, b: a * i3 + b * c + np.conj(b) * c.T
    ev = np.sort(np.linalg.eigvals(h(1, 1)).real)
    passed.append(check(
        "R1 r=1 endpoint gives eigenvalues {0,0,3a}, the rank-one/democratic point",
        np.allclose(ev, [0, 0, 3]),
        f"eig={np.round(ev, 4)}"))

    scalar_action = 1j * i3
    passed.append(check(
        "R2 a scalar generation U(1) action commutes with C and cannot orient the doublet",
        np.allclose(scalar_action @ c - c @ scalar_action, 0),
        "[iI,C]=0; this is conditional on the physical charge acting scalar on generation"))

    allowed = [0.0, 2 * np.pi / 3, 4 * np.pi / 3]
    probe = 0.41
    passed.append(check(
        "R3 C^3=I blocks continuous C rephasing except the discrete C3 phases",
        all(abs(np.exp(1j * a) ** 3 - 1) < 1e-12 for a in allowed)
        and abs(np.exp(1j * probe) ** 3 - 1) > 1e-3,
        "generic alpha fails order three"))

    leptons = [0.51099895e-3, 0.1056583755, 1.77686]
    up = [2.16e-3, 1.27, 172.69]
    down = [4.67e-3, 93.4e-3, 4.18]
    ql, qd, qu = koide_q(leptons), koide_q(down), koide_q(up)
    passed.append(check(
        "R4 embedded mass comparator orders charged sectors leptons < down < up < rank-one",
        ql < qd < qu < 1.0 and abs(ql - 2 / 3) < 2e-3,
        f"leptons={ql:.4f}, down={qd:.4f}, up={qu:.4f}; empirical comparator only"))

    d21, d31 = 7.5e-5, 2.5e-3
    def qnu(m1):
        masses = np.array([m1, np.sqrt(m1 ** 2 + d21), np.sqrt(m1 ** 2 + d31)])
        return masses.sum() / np.sqrt(masses).sum() ** 2

    qnu_max = max(qnu(x) for x in np.linspace(0, 0.5, 3000))
    passed.append(check(
        "R5 neutrino positive-root normal-ordering comparator stays below 2/3 in the tested range",
        qnu_max < 0.6,
        f"max Q_nu={qnu_max:.4f} < 2/3"))

    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30.md").read_text()
    banned = [
        "framework's gauge U(1)s are generation-blind",
        "NEW POSITIVE",
        "the det_C/det_R axis organizes ALL charged fermion sectors",
        "charge-selection FAILS as a mechanism",
        "derived continuous *flavor/horizontal* U(1)",
    ]
    required = [
        "If a physical charge `U(1)` acts as a scalar",
        "empirical\n   comparators only",
        "No new axiom is introduced.",
    ]
    passed.append(check(
        "R6 source boundary guard: no physical gauge-action or sector-ordering theorem promoted",
        all(term not in note for term in banned) and all(term in note for term in required),
        "the packet closes only finite/conditional route pruning"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: bounded-support route pruning. Scalar generation charge cannot orient")
    print("the doublet, and continuous C rephasing is blocked by C^3=I. The mass table is")
    print("comparator evidence only; this runner does not derive a physical det_C/det_R selector.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
