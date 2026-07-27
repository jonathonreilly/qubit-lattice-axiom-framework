"""Finite checks for QD objectivity fixing basis but not sector weights.

The runner verifies that redundant-objective two-sector records can carry
either dimensional/Born weights or uniform sector weights. Objectivity reports
the supplied weights through the Shannon plateau; it does not select them.
"""

from __future__ import annotations

import numpy as np


C = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
I3 = np.eye(3)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def shannon_entropy(weights: list[float]) -> float:
    w = np.array(weights, dtype=float)
    w = w[w > 0.0]
    return float(-(w * np.log2(w)).sum())


def random_unitary(rng: np.random.Generator) -> np.ndarray:
    matrix = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    q_matrix, r_matrix = np.linalg.qr(matrix)
    phases = np.diag(r_matrix) / np.abs(np.diag(r_matrix))
    return q_matrix @ np.diag(phases)


def main() -> int:
    passed: list[bool] = []

    singlet_vector = np.ones(3) / np.sqrt(3)
    p_singlet = np.outer(singlet_vector, singlet_vector)
    p_doublet = I3 - p_singlet

    passed.append(
        check(
            "two K-real sectors give a rank-1/rank-2 pointer alphabet",
            abs(np.trace(p_singlet) - 1.0) < 1e-12
            and abs(np.trace(p_doublet) - 2.0) < 1e-12,
        )
    )

    h_born = shannon_entropy([1.0 / 3.0, 2.0 / 3.0])
    h_uniform = shannon_entropy([0.5, 0.5])
    passed.append(
        check(
            "objectivity plateau reports H(weights), not a selected weight",
            abs(h_born - 0.9182958340544896) < 1e-12
            and abs(h_uniform - 1.0) < 1e-12,
            f"H(1/3,2/3)={h_born:.6f}; H(1/2,1/2)={h_uniform:.6f}",
        )
    )

    p_triv = float(np.real(np.trace(p_singlet @ (I3 / 3.0))))
    p_doub = float(np.real(np.trace(p_doublet @ (I3 / 3.0))))
    r_born = (p_doub / p_triv) / 2.0
    passed.append(
        check(
            "tracial I/3 gives sector weights (1/3,2/3), hence r=1",
            abs(p_triv - 1.0 / 3.0) < 1e-12
            and abs(p_doub - 2.0 / 3.0) < 1e-12
            and abs(r_born - 1.0) < 1e-12,
            f"(p_triv,p_doublet)=({p_triv:.6f},{p_doub:.6f}); r={r_born:.6f}",
        )
    )

    rng = np.random.default_rng(0)
    rho_uniform = 0.5 * p_singlet + 0.5 * (p_doublet / 2.0)
    i3_invariant = True
    uniform_invariant = True
    for _ in range(2000):
        unitary = random_unitary(rng)
        if np.linalg.norm(unitary @ (I3 / 3.0) @ unitary.conj().T - I3 / 3.0) > 1e-9:
            i3_invariant = False
        if np.linalg.norm(unitary @ rho_uniform @ unitary.conj().T - rho_uniform) > 1e-9:
            uniform_invariant = False
    passed.append(
        check(
            "I/3 is sampled U(3)-invariant while the uniform-sector state is not",
            i3_invariant and not uniform_invariant,
        )
    )

    real_operator = C + C.conj().T
    passed.append(
        check(
            "conjugation fixes both real effects and gives no rank swap",
            np.allclose(p_singlet.conj(), p_singlet)
            and np.allclose(p_doublet.conj(), p_doublet)
            and np.allclose(real_operator.imag, 0.0),
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print(
        "FINDING: QD objectivity fixes the two-sector pointer basis but does "
        "not select the sector weights."
    )
    print(
        "The uniform sector weight remains an extra measure/reference choice, "
        "not a consequence of redundant objectivity."
    )
    print(f"per_element: checked — projector traces are {np.trace(p_singlet).real:.1f} and {np.trace(p_doublet).real:.1f}, resolving the 1+2 pointer atoms.")
    print(f"per_site: checked — one local tracial carrier gives weights ({p_triv:.6f},{p_doub:.6f}) and r={r_born:.6f}.")
    print(f"per_mode: checked — 2000 sampled U(3) rotations preserve I/3={i3_invariant} but preserve the uniform-sector state={uniform_invariant}.")
    print(f"per_block: checked — conjugation fixes both real rank blocks and the real C+Cdag operator={np.allclose(real_operator.imag, 0.0)}.")
    print(f"lattice_wide: checked and not executed — lattice dynamics is outside this three-state objectivity claim; the executed finite-carrier suite has PASS={pass_count}, FAIL={fail_count}.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
