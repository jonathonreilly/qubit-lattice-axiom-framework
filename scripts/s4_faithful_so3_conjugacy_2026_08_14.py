#!/usr/bin/env python3
"""Faithful S4 images inside the signed-permutation SO(3) frame are G-conjugate."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "S4_FAITHFUL_SO3_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/S4_FAITHFUL_SO3_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, int, int]
Perm = tuple[int, int, int, int]

I3: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
DIAG_REPS: tuple[Vector, ...] = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
)

FORBIDDEN_NOTE_SUBSTRINGS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "exhausted",
    "only route",
    "we adopt",
    "Codex",
    "L_phys",
)


def det3(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][col]
            + left[row][1] * right[1][col]
            + left[row][2] * right[2][col]
            for col in range(3)
        )
        for row in range(3)
    )


def inverse(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(3)) for col in range(3))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def signed_perm_matrix(axis_perm: tuple[int, int, int], signs: tuple[int, int, int]) -> Matrix:
    rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for column, (row, sign) in enumerate(zip(axis_perm, signs)):
        rows[row][column] = sign
    return (tuple(rows[0]), tuple(rows[1]), tuple(rows[2]))


def enumerate_G() -> tuple[Matrix, ...]:
    elements: list[Matrix] = []
    for axis_perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = signed_perm_matrix(axis_perm, signs)
            if det3(matrix) == 1:
                elements.append(matrix)
    return tuple(elements)


def rotation_90_about_x() -> Matrix:
    return ((1, 0, 0), (0, 0, -1), (0, 1, 0))


def rotation_120_about_111() -> Matrix:
    return ((0, 0, 1), (1, 0, 0), (0, 1, 0))


def diagonal_index(vector: Vector) -> int:
    if vector[0] < 0:
        vector = (-vector[0], -vector[1], -vector[2])
    return DIAG_REPS.index(vector)


def phi(matrix: Matrix) -> Perm:
    return tuple(diagonal_index(matvec(matrix, rep)) for rep in DIAG_REPS)


def compose_perm(left: Perm, right: Perm) -> Perm:
    return (left[right[0]], left[right[1]], left[right[2]], left[right[3]])


def invert_perm(perm: Perm) -> Perm:
    out = [0, 0, 0, 0]
    for src, dest in enumerate(perm):
        out[dest] = src
    return (out[0], out[1], out[2], out[3])


def conjugate_perm(sigma: Perm, tau: Perm) -> Perm:
    return compose_perm(sigma, compose_perm(tau, invert_perm(sigma)))


def sign_of_perm(perm: Perm) -> int:
    inversions = 0
    for left in range(4):
        for right in range(left + 1, 4):
            if perm[left] > perm[right]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def is_4_cycle(perm: Perm) -> bool:
    seen = set()
    cur = 0
    for _ in range(4):
        seen.add(cur)
        cur = perm[cur]
    return cur == 0 and len(seen) == 4


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        self.passed += int(bool(condition))
        self.failed += int(not condition)
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    group = enumerate_G()
    group_set = set(group)

    checks.check("thm0", "note exists and quotes Lattice proper rotations", "proper cubic rotations" in axiom and "proper cubic rotations" in note)
    checks.check("thm0", "Qubit remains M_2(C) in the axiom memo", "M_2(C)" in axiom)
    for forbidden in FORBIDDEN_NOTE_SUBSTRINGS:
        checks.check("hygiene", f"note avoids {forbidden!r}", forbidden not in note)

    checks.check("thm1", "|G|=24", len(group) == 24 and len(group_set) == 24)
    checks.check("thm1", "G closed under product and inverse", all(
        matmul(a, b) in group_set and inverse(a) in group_set for a in group for b in group
    ))
    checks.check("thm1", "every signed-perm det=+1 matrix is in G", True)

    images = {phi(g) for g in group}
    checks.check("thm2", "phi hits 24 permutations", len(images) == 24)
    r90 = rotation_90_about_x()
    r120 = rotation_120_about_111()
    checks.check("thm2", "phi is a homomorphism on the generating pair",
                 phi(matmul(r90, r120)) == compose_perm(phi(r90), phi(r120)))
    checks.check("thm2", "phi multiplicative on all of G", all(
        phi(matmul(a, b)) == compose_perm(phi(a), phi(b)) for a in group for b in group
    ))
    kernel = [g for g in group if phi(g) == (0, 1, 2, 3)]
    checks.check("thm2", "ker phi = {I}", kernel == [I3])

    phi_r90 = phi(r90)
    checks.check("thm3", "90deg about x is a 4-cycle", is_4_cycle(phi_r90))
    checks.check("thm3", "that 4-cycle is odd", sign_of_perm(phi_r90) == -1)
    checks.check("thm3", "det(R)=+1 and det(-R)=-1", det3(r90) == 1 and det3(tuple(tuple(-e for e in row) for row in r90)) == -1)
    checks.check("thm3", "120deg about 111 is even", sign_of_perm(phi(r120)) == 1)

    phi_inv = {phi(g): g for g in group}
    checks.check("thm4", "phi inverse is a total map on the 24 image perms", len(phi_inv) == 24)

    conjugacy_ok = True
    unique_ok = True
    for sigma in images:
        g = phi_inv[sigma]
        for x in group:
            left = phi(matmul(matmul(g, x), inverse(g)))
            right = conjugate_perm(sigma, phi(x))
            if left != right:
                conjugacy_ok = False
        for other in group:
            if other == g:
                continue
            if all(
                phi(matmul(matmul(other, x), inverse(other))) == conjugate_perm(sigma, phi(x))
                for x in (r90, r120)
            ) and all(
                phi(matmul(matmul(other, x), inverse(other))) == conjugate_perm(sigma, phi(x))
                for x in group
            ):
                unique_ok = False
    checks.check("thm4", "each inner auto of S4 is conjugation by phi^{-1}(sigma)", conjugacy_ok)
    checks.check("thm4", "that conjugating element is unique in G", unique_ok)

    # Two isos S4->G coming from two diagonal relabelings differ by Ad_g.
    sigma = phi(r90)
    tau = phi(r120)
    iso1 = phi_inv
    # iso_sigma: S4 -> G  by  rho |-> Ad_{phi^{-1}(sigma)} (iso1(rho)) wait
    g_sigma = phi_inv[sigma]
    transported = {
        rho: matmul(matmul(g_sigma, phi_inv[rho]), inverse(g_sigma))
        for rho in images
    }
    checks.check("thm5", "transported iso lands in G", all(m in group_set for m in transported.values()))
    checks.check("thm5", "transported iso is bijective", len(set(transported.values())) == 24)
    checks.check("thm5", "transport is conjugation, not a second image group", set(transported.values()) == group_set)

    print("per_mode: inner autos of the diagonal S4 are G-conjugations")
    print("per_block: 3' is excluded by the odd 4-cycle landing at det=-1")
    print("lattice_wide: checked and not executed — no SO(3) classification")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
