"""Finite checks for the K-real instrument two-letter localization."""

from __future__ import annotations

import numpy as np


C = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
I3 = np.eye(3)
S = C + C.conj().T
J = 1j * (C - C.conj().T)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def r_from_weights(p_triv: float, p_doublet: float) -> float:
    return (p_doublet / p_triv) / 2.0


def main() -> int:
    passed: list[bool] = []

    passed.append(
        check(
            "S=C+C^2 is K-even Hermitian with spectrum {2,-1,-1}",
            np.allclose(S, S.conj().T)
            and np.allclose(np.sort(np.linalg.eigvalsh(S)), [-1.0, -1.0, 2.0]),
            f"spec(S)={np.sort(np.linalg.eigvalsh(S)).round(6)}",
        )
    )

    passed.append(
        check(
            "J=i(C-C^2) is K-odd Hermitian with spectrum {-sqrt3,0,sqrt3}",
            np.allclose(J, J.conj().T)
            and np.allclose(
                np.sort(np.linalg.eigvalsh(J)),
                [-np.sqrt(3.0), 0.0, np.sqrt(3.0)],
            ),
            f"spec(J)={np.sort(np.linalg.eigvalsh(J)).round(6)}",
        )
    )

    passed.append(
        check(
            "conjugation sends J to -J",
            np.allclose(J.conj(), -J),
        )
    )

    passed.append(
        check(
            "K-even S and K-odd J commute",
            np.allclose(S @ J - J @ S, 0.0),
        )
    )

    a_param, b_param = 1.3, 0.6 + 0.4j
    h_direct = a_param * I3 + b_param * C + np.conj(b_param) * C.conj().T
    h_split = a_param * I3 + b_param.real * S + b_param.imag * J
    passed.append(
        check(
            "H equals the Re(b)S + Im(b)J decomposition",
            np.allclose(h_direct, h_split),
        )
    )

    p_triv, p_doublet = 1.0 / 3.0, 2.0 / 3.0
    von_neumann_entropy = np.log(3.0)
    shannon_entropy = -(
        p_triv * np.log(p_triv) + p_doublet * np.log(p_doublet)
    )
    passed.append(
        check(
            "two-letter record removes exactly the doublet multiplicity entropy",
            abs((von_neumann_entropy - shannon_entropy) - p_doublet * np.log(2.0))
            < 1e-12,
            f"gap={(von_neumann_entropy - shannon_entropy):.6f}",
        )
    )

    passed.append(
        check(
            "dimension count gives r=1 while block count gives r=1/2",
            abs(r_from_weights(1.0 / 3.0, 2.0 / 3.0) - 1.0) < 1e-12
            and abs(r_from_weights(0.5, 0.5) - 0.5) < 1e-12,
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print(
        "FINDING: under a K-real instrument, the record alphabet is the K-even "
        "two-sector split while the Brannen phase lies in the K-odd channel."
    )
    print("The remaining value question is the measure on that two-sector record.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
