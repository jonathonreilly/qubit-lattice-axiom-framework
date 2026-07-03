#!/usr/bin/env python3
"""C3 reference-state cone does not force trace.

This runner verifies only the finite statement:

    given the explicit C3 generation-factor symmetry,
    the reference-state cone remains open and does not select trace.

It deliberately does not decide whether the repo baseline supplies only C3,
whether full U(3)/PRR is accepted elsewhere, or which physical mass readout is
selected by the full framework.
"""
from pathlib import Path

import numpy as np
import numpy.linalg as la
import sympy as sp


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    I3 = np.eye(3)
    J = np.ones((3, 3))
    Ps = J / 3
    Pd = I3 - J / 3
    rho11 = 0.5 * Ps + 0.25 * Pd
    rho_tau = I3 / 3
    passed = []

    block_masses_11 = (np.trace(rho11 @ Ps), np.trace(rho11 @ Pd))
    block_masses_tau = (np.trace(rho_tau @ Ps), np.trace(rho_tau @ Pd))
    passed.append(check(
        "C1/C2 rho_(1:1) is PSD, trace-one, C3-invariant, and has equal block masses",
        (
            np.all(np.linalg.eigvalsh(rho11) >= -1e-12)
            and abs(np.trace(rho11) - 1) < 1e-12
            and np.allclose(rho11 @ C - C @ rho11, 0)
            and abs(block_masses_11[0] - block_masses_11[1]) < 1e-12
        ),
        f"eigs={np.round(np.linalg.eigvalsh(rho11), 3)}; tau block masses={np.round(block_masses_tau, 3)}"))

    devs_t = []
    devs_1 = []
    for k in range(500):
        A = np.array([
            [np.cos(0.01 * k + i + j) + 1j * np.sin(0.013 * k + 2 * i + j) for j in range(3)]
            for i in range(3)
        ])
        Qm, _ = la.qr(A)
        devs_t.append(la.norm(Qm @ rho_tau @ Qm.conj().T - rho_tau))
        devs_1.append(la.norm(Qm @ rho11 @ Qm.conj().T - rho11))
    passed.append(check(
        "C3 full U(3) conjugation preserves trace but not rho_(1:1), so it is a stronger selector than C3",
        max(devs_t) < 1e-12 and max(devs_1) > 0.05,
        f"U(3) dev: tau={max(devs_t):.1e}, (1:1)={max(devs_1):.3f}"))

    a, b = sp.symbols("a b", positive=True)
    q_formula = sp.simplify(((a + 2 * b) ** 2 + 2 * (a - b) ** 2) / ((a + 2 * b) + 2 * (a - b)) ** 2)
    passed.append(check(
        "C4 displayed Q formula depends on spectral parameter r=|b|^2/a^2, not on rho",
        sp.simplify(q_formula - (sp.Rational(1, 3) + sp.Rational(2, 3) * (b / a) ** 2)) == 0,
        "any bridge from block masses to r is additional structure outside this packet"))

    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md").read_text()
    banned = [
        "framework's honest default",
        "framework baseline do **not** force",
        "unaudited PRR premise",
        "user-approval-required",
        "DEFAULT-pending-PRR",
        "decisive, decidable, no-import next step",
        "already-retained",
    ]
    required = [
        "does not decide",
        "Given only the explicit `C3`",
        "No new axiom is introduced.",
    ]
    passed.append(check(
        "C5 source boundary guard: no repo-baseline or PRR-status conclusion is promoted by this packet",
        all(term not in note for term in banned) and all(term in note for term in required),
        "the packet closes only the stipulated-C3 cone no-go"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: bounded-support negative route pruning.")
    print("Given only the stipulated C3 generation symmetry, the invariant reference-state cone")
    print("contains both the tracial 1:2 weighting and an admissible non-tracial 1:1 weighting.")
    print("Full U(3) conjugation is a stronger selector, but this runner does not decide its")
    print("repo-baseline status. The displayed Q formula is a spectral readout and does not use rho.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
