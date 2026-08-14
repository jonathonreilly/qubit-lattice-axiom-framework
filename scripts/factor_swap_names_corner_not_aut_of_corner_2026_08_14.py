#!/usr/bin/env python3
"""Exact checks: factor-swap names the corner, not Aut of the corner.

Finite Fraction identities only. No QCD, no SU(3) adoption, no axiom
edit, no cache write, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "FACTOR_SWAP_NAMES_CORNER_NOT_AUT_OF_CORNER_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_CORNER_PATH = ROOT / "docs" / (
    "TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/FACTOR_SWAP_NAMES_CORNER_NOT_AUT_OF_CORNER_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]

QUBIT_QUOTE = (
    "The full one-site possibility domain has algebraic presentation `M_2(C)`."
)
RECORD_LOCK_QUOTE = (
    "When present, a record locks exactly one admissible local possibility."
)
RECORD_UNREAD_QUOTE = "A site with no record cannot be read."
LATTICE_LINE = "Physical sites are the points of the cubic lattice `Z^3`"


def normalize(text: str) -> str:
    return " ".join(text.split())


def eye(n: int) -> Matrix:
    return tuple(tuple(Fraction(int(row == col)) for col in range(n)) for row in range(n))


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * matrix[row][col] for col in range(len(matrix))) for row in range(len(matrix)))


def mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][col] for mid in range(size)), Fraction(0))
            for col in range(size)
        )
        for row in range(size)
    )


def adj(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[col][row] for col in range(size)) for row in range(size))


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def ketbra(left: Vector, right: Vector) -> Matrix:
    return tuple(tuple(left[row] * right[col] for col in range(len(right))) for row in range(len(left)))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[row][col] * vector[col] for col in range(len(vector))), Fraction(0))
        for row in range(len(matrix))
    )


def rank(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    height = len(rows)
    width = len(rows[0]) if rows else 0
    lead = 0
    computed = 0
    for r in range(height):
        if lead >= width:
            return computed
        i = r
        while rows[i][lead] == 0:
            i += 1
            if i == height:
                i = r
                lead += 1
                if lead == width:
                    return computed
        rows[i], rows[r] = rows[r], rows[i]
        pivot = rows[r][lead]
        rows[r] = [value / pivot for value in rows[r]]
        for i in range(height):
            if i == r:
                continue
            factor = rows[i][lead]
            rows[i] = [rows[i][c] - factor * rows[r][c] for c in range(width)]
        computed += 1
        lead += 1
    return computed


def e_unit(n: int, row: int, col: int) -> Matrix:
    data = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    data[row][col] = Fraction(1)
    return tuple(tuple(item) for item in data)


def swap_matrix() -> Matrix:
    data = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for a in (0, 1):
        for b in (0, 1):
            source = 2 * a + b
            target = 2 * b + a
            data[target][source] = Fraction(1)
    return tuple(tuple(item) for item in data)


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_CORNER_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none")
    print("explicit_bounded_inputs: H=C^2⊗C^2, factor-swap F, and the ON chart of im(p)")
    print("framework_context: quoted live Lattice, Qubit, and Record; no axiom edit")
    print("measure_boundary: exact Fraction matrix algebra only")

    identity3 = eye(3)
    identity4 = eye(4)
    swap = swap_matrix()
    projector = scale(Fraction(1, 2), add(identity4, swap))
    displayed_projector = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )

    w0: Vector = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    w1: Vector = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
    w_plus: Vector = (Fraction(0), Fraction(1), Fraction(1), Fraction(0))

    e00_3 = e_unit(3, 0, 0)
    e11_3 = e_unit(3, 1, 1)
    v0 = identity3
    v_omega = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    )
    ad0_e00 = mul(mul(v0, e00_3), adj(v0))
    ad_omega_e00 = mul(mul(v_omega, e00_3), adj(v_omega))

    e00_4 = ketbra(w0, w0)
    e11_4 = ketbra(w1, w1)
    e_plus_plus = scale(Fraction(1, 2), ketbra(w_plus, w_plus))
    on_sum = add(add(e00_4, e11_4), e_plus_plus)

    compressed_units = [
        mul(mul(projector, e_unit(4, row, col)), projector)
        for row in range(4)
        for col in range(4)
    ]

    checks.check(
        "source-qubit",
        "the axiom memo names one-site M_2(C)",
        QUBIT_QUOTE in axiom,
    )
    checks.check(
        "source-record",
        "the axiom memo locks one admissible local possibility",
        RECORD_LOCK_QUOTE in axiom and RECORD_UNREAD_QUOTE in axiom,
    )
    checks.check(
        "source-lattice",
        "the axiom memo names sites of Z^3",
        LATTICE_LINE in axiom,
    )
    checks.check(
        "thm-f-hermitian-involution",
        "F is a Hermitian involution of trace 2",
        adj(swap) == swap and mul(swap, swap) == identity4 and trace(swap) == Fraction(2),
    )
    checks.check(
        "thm-p-projection",
        "p=(I+F)/2 is the displayed rank-3 orthogonal projection",
        projector == displayed_projector
        and mul(projector, projector) == projector
        and adj(projector) == projector
        and rank(projector) == 3
        and projector != identity4,
    )
    checks.check(
        "thm-on-sum",
        "the ON chart sums to p using the integer spanning set",
        on_sum == projector
        and matvec(projector, w0) == w0
        and matvec(projector, w1) == w1
        and matvec(projector, w_plus) == w_plus,
    )
    checks.check(
        "thm-corner-unit",
        "p is the unit of A=p M_4 p",
        all(mul(mul(projector, matrix), projector) == matrix for matrix in compressed_units)
        and mul(mul(projector, identity4), projector) == projector,
    )
    checks.check(
        "thm1-vomega-unitary",
        "Vω is a 3-cycle unitary of M_3 and V0 is the identity",
        v0 == identity3
        and mul(adj(v_omega), v_omega) == identity3
        and mul(mul(v_omega, v_omega), v_omega) == identity3
        and v_omega != identity3
        and matvec(v_omega, (Fraction(1), Fraction(0), Fraction(0)))
        == (Fraction(0), Fraction(1), Fraction(0))
        and matvec(v_omega, (Fraction(0), Fraction(1), Fraction(0)))
        == (Fraction(0), Fraction(0), Fraction(1))
        and matvec(v_omega, (Fraction(0), Fraction(0), Fraction(1)))
        == (Fraction(1), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm1-ad-disagree",
        "Ad_0(E00)=E00 while Ad_ω(E00)=E11, so Ad_0≠Ad_ω",
        ad0_e00 == e00_3 and ad_omega_e00 == e11_3 and ad0_e00 != ad_omega_e00,
    )
    checks.check(
        "thm1-both-fix-p",
        "both Ad maps fix the corner unit",
        mul(mul(v0, identity3), adj(v0)) == identity3
        and mul(mul(v_omega, identity3), adj(v_omega)) == identity3
        and mul(mul(projector, projector), adj(projector)) == projector,
    )
    checks.check(
        "control-f-fixes-im-p",
        "F fixes the spanning set of im(p), so F|im(p)=I",
        matvec(swap, w0) == w0
        and matvec(swap, w1) == w1
        and matvec(swap, w_plus) == w_plus,
    )
    checks.check(
        "control-ad-f-is-id",
        "Ad_F is the identity on the corner",
        all(mul(mul(swap, matrix), swap) == matrix for matrix in compressed_units),
    )
    checks.check(
        "parent-corner-host",
        "the landed swap-corner parent hosts M_3 with unit p",
        PARENT_CORNER_PATH.is_file()
        and "unit `p`" in parent
        and "p M_4" in parent
        and "actual_current_surface_status: bounded-support" in parent,
    )
    checks.check(
        "live-quotes-in-note",
        "the note quotes live Qubit, Record, and Lattice without rewrite",
        QUBIT_QUOTE in note
        and RECORD_LOCK_QUOTE in note
        and RECORD_UNREAD_QUOTE in note
        and "Physical sites are the points of the cubic lattice `Z^3`" in note,
    )
    axiom_lacks_su3_qcd = "SU(3)" not in axiom and "QCD" not in axiom
    checks.check(
        "mutation-ad-equal-fails",
        "predicate Ad_0==Ad_ω fails",
        (ad0_e00 == ad_omega_e00) is False,
    )
    checks.check(
        "mutation-f-equals-vomega-fails",
        "predicate F|im(p) equals Vω fails",
        (v_omega == identity3) is False,
    )
    checks.check(
        "mutation-memo-names-su3-qcd-fails",
        "predicate that the live memo names SU(3) or QCD as axiom content fails",
        axiom_lacks_su3_qcd is True,
    )
    checks.check(
        "scope-no-adoption",
        "the note displays both Ad maps and does not adopt SU(3) or QCD",
        "No `SU(3)` action and no" in note
        and "QCD identification is adopted" in note
        and "Qubit is not rewritten to `M_3`" in note
        and "not a 3-menu" in note
        and "not a pairing table" in note
        and "not a one-site adjoint" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and propose-ratify fields are source-visible",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "trace_class: frontier_discovery",
                "target_claim_id: factor_swap_names_corner_not_aut_of_corner",
                "next_trace_action:",
                "**Type:** bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
                "## Honest-Auditor / Boundary",
            )
        )
        and "FAIL / DO NOT SHIP" not in note
        and "closes the route" not in note.lower()
        and "audit verdict" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not edited toward a color action or two-site Aut",
        all(
            phrase not in axiom
            for phrase in (
                "V_ω",
                "Ad_ω",
                "p M_4 p",
                "SU(3)",
                "QCD",
            )
        ),
    )
    checks.check(
        "no-unmerged-pr-citation",
        "the note reconstructs the carrier locally and cites no unmerged PR",
        "#" not in note.split("claim_id:")[0]
        and "PR #" not in note
        and "unmerged" in note
        and "reconstructed here" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/FACTOR_SWAP_NAMES_CORNER_NOT_AUT_OF_CORNER_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and PARENT_CORNER_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source,
    )
    checks.check(
        "hygiene-no-float-qcd-import",
        "the runner stays on Fraction and does not import a QCD stack",
        ("fl" + "oat(") not in self_source
        and "from fractions import Fraction" in self_source
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )

    print("per_element: F, p, V0, Vω, E00, and the corner units are exact Fraction matrices")
    print("per_site: Record is quoted as a one-site lock; it is not applied to Aut(A)")
    print("per_block: Aut is tested on the displayed two-site corner only")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
