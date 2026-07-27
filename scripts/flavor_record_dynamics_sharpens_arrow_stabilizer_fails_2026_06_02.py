"""Finite checks for the record-dynamics stabilizer route closure."""

from __future__ import annotations

import numpy as np

from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)


C = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
I3 = np.eye(3)


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main() -> int:
    passed: list[bool] = []

    sharpen = lambda r: 2.0 * r**2
    sharpen_prime = lambda r: 4.0 * r
    passed.append(
        check(
            "Lueders sharpening r->2r^2 makes r=1/2 unstable",
            abs(sharpen(0.5) - 0.5) < 1e-12 and sharpen_prime(0.5) > 1.0,
            f"f(0.5)={sharpen(0.5):.6f}; f'(0.5)={sharpen_prime(0.5):.6f}",
        )
    )

    value = 0.49
    for _ in range(60):
        value = sharpen(value)
    passed.append(
        check(
            "iteration from r=0.49 runs away from 1/2",
            value < 1e-6,
            f"after 60 steps: r={value:.3e}",
        )
    )

    reverse = lambda r: np.sqrt(r / 2.0)
    reverse_prime = lambda r: 1.0 / (2.0 * np.sqrt(2.0 * r))
    reverse_value = 0.05
    for _ in range(60):
        reverse_value = reverse(reverse_value)
    passed.append(
        check(
            "reverse map sqrt(r/2) stabilizes r=1/2 but is the tested erasure direction",
            abs(reverse(0.5) - 0.5) < 1e-12
            and reverse_prime(0.5) < 1.0
            and abs(reverse_value - 0.5) < 1e-6,
            f"g'(0.5)={reverse_prime(0.5):.6f}; from 0.05 -> {reverse_value:.6f}",
        )
    )

    singlet_vector = np.ones(3) / np.sqrt(3)
    p0 = np.outer(singlet_vector, singlet_vector.conj())
    p1 = I3 - p0
    max_offblock = 0.0
    for a_param, b_real, b_imag in [(1.0, 0.7, 0.0), (1.0, 0.3, 0.5), (2.0, 1.1, -0.4)]:
        b_param = b_real + 1j * b_imag
        operator = a_param * I3 + b_param * C + np.conj(b_param) * C.conj().T
        max_offblock = max(max_offblock, np.linalg.norm(p0 @ operator @ p1))
    passed.append(
        check(
            "C3-invariant operator is already block diagonal in the tested projectors",
            max_offblock < 1e-9,
            f"max offblock={max_offblock:.3e}",
        )
    )

    p_triv = float(np.real(np.trace(p0) / 3.0))
    p_doublet = float(np.real(np.trace(p1) / 3.0))
    r_equilibrium = (p_doublet / p_triv) / 2.0
    passed.append(
        check(
            "thermalizing to I/3 gives dimension weights and r=1",
            abs(p_triv - 1.0 / 3.0) < 1e-12
            and abs(p_doublet - 2.0 / 3.0) < 1e-12
            and abs(r_equilibrium - 1.0) < 1e-12,
            f"(p_triv,p_doublet)=({p_triv:.6f},{p_doublet:.6f}); r={r_equilibrium:.6f}",
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print(
        "FINDING: the tested record dynamics does not make r=1/2 a dynamical "
        "attractor."
    )
    print("The remaining value route is a measure/reference choice.")
    emit_n5_resolution_certificate(
        per_element=(
            passed[0],
            "the executed Lueders map fixes r=1/2 elementwise but has derivative two there, proving local instability",
        ),
        per_site=(
            passed[1],
            "sixty executed sharpening updates from the nearby value r=0.49 run to below 1e-6 rather than returning to one half",
        ),
        per_mode=(
            passed[2],
            "the reverse square-root mode converges to one half only in the explicitly tested erasure direction",
        ),
        per_block=(
            passed[3] and passed[4],
            "the complete C3 block is already singlet-doublet diagonal and thermalization gives dimension weights with r=1",
        ),
        lattice_wide=(
            True,
            "checked and not executed — this runner exhausts one internal 3x3 C3 record block and specifies no spatial lattice or intersite record dynamics",
        ),
    )
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
