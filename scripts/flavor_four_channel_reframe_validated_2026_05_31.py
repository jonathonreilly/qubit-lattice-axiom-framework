#!/usr/bin/env python3
"""Finite C3 circulant coordinate checks for the flavor capstone boundary."""

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    ident = np.eye(3)
    cycle = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    passed = []

    def observables(a, b_abs, delta):
        lambdas = np.array(
            [a + 2 * b_abs * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)]
        )
        return np.array([lambdas.sum() / 3, (lambdas**2).sum() / lambdas.sum() ** 2, delta])

    a0, b0, d0, eps = 1.0, 0.5, 0.7, 1e-6
    base = observables(a0, b0, d0)
    jacobian = np.column_stack(
        [
            (observables(a0 + eps, b0, d0) - base) / eps,
            (observables(a0, b0 + eps, d0) - base) / eps,
            (observables(a0, b0, d0 + eps) - base) / eps,
        ]
    )
    det_j = np.linalg.det(jacobian)
    passed.append(
        check(
            "V1 supplied C3 coordinates are locally independent at the tested point",
            abs(det_j) > 1e-6,
            f"det={det_j:.3f}",
        )
    )

    scalar = 2.5 * ident
    doublet_coeff = np.trace(scalar @ cycle.conj().T) / 3
    passed.append(
        check(
            "V2 supplied scalar G=gI has zero C/C^2 doublet coefficient",
            abs(doublet_coeff) < 1e-12,
            "This is a singlet algebra check, not a physical gauge theorem.",
        )
    )

    q_of_delta = lambda d: observables(1.0, 0.7071, d)[1]
    passed.append(
        check(
            "V3 dispersion Q is delta-independent in the supplied model",
            abs(q_of_delta(0.3) - q_of_delta(1.3)) < 1e-9,
            f"Q(0.3)={q_of_delta(0.3):.4f}=Q(1.3)",
        )
    )

    q_disp = lambda r: 1 / 3 + 2 * r / 3
    q_brannen = lambda r: 1 / (2 * r + 1)
    passed.append(
        check(
            "V4 displayed Q floors are readout-convention dependent",
            abs(q_disp(0) - 1 / 3) < 1e-9 and abs(q_brannen(0) - 1) < 1e-9,
            "dispersion(r=0)=1/3, Brannen(r=0)=1",
        )
    )

    note = (ROOT / "docs/FLAVOR_VALUE_CAMPAIGN_CAPSTONE_FOUR_CHANNEL_2026-05-31.md").read_text()
    compact_note = " ".join(note.split())
    guard_ok = (
        "does not derive this operator from the axiom baseline" in compact_note
        and "does not provide a complete account of charged-lepton flavor" in compact_note
        and "not a physical gauge-sector theorem" in compact_note
        and "does not add an axiom" in compact_note
    )
    passed.append(
        check(
            "source guards keep physical channel, eta, and complete-account bridges open",
            guard_ok,
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: bounded support for finite supplied C3 coordinate algebra only.")
    print("The runner checks local coordinate independence, a scalar singlet fact,")
    print("delta-blindness of dispersion Q, and readout-convention dependence.")
    print("It does not derive the physical carrier, channel identifications,")
    print("eta=2/9, or a complete charged-lepton flavor account.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
