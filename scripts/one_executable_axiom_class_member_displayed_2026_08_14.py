#!/usr/bin/env python3
"""Exact Q tables for one displayed axiom-class member L0.

Plus-shaped occupancy six-tuple, directed Bloch kernel, formation
predicate, axis-aligned menu, displayed clock and pairing. No axiom
edit, no cache write, no adopted law.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ONE_EXECUTABLE_AXIOM_CLASS_MEMBER_DISPLAYED_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONE_EXECUTABLE_AXIOM_CLASS_MEMBER_DISPLAYED_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

IntMat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Vec3 = tuple[int, int, int]
Bloch = tuple[Fraction, Fraction, Fraction]
Occ = tuple[int, int, int, int, int, int]

DIRECTIONS: tuple[Vec3, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_OF = {vec: index for index, vec in enumerate(DIRECTIONS)}

THIRD = Fraction(1, 3)
ZERO = Fraction(0)
ONE = Fraction(1)
TWO = Fraction(2)

EMPTY: Occ = (0, 0, 0, 0, 0, 0)
PLUS_X: Occ = (1, 0, 0, 0, 0, 0)
MINUS_X: Occ = (0, 1, 0, 0, 0, 0)
PLUS_Y: Occ = (0, 0, 1, 0, 0, 0)
OPP_X: Occ = (1, 1, 0, 0, 0, 0)
PLUS_X_PLUS_Y: Occ = (1, 0, 1, 0, 0, 0)

RZ: IntMat = ((0, -1, 0), (1, 0, 0), (0, 0, 1))


def mat3_mul(left: IntMat, right: IntMat) -> IntMat:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mat3_det(matrix: IntMat) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def apply_intmat(matrix: IntMat, vec: Vec3) -> Vec3:
    return (
        matrix[0][0] * vec[0] + matrix[0][1] * vec[1] + matrix[0][2] * vec[2],
        matrix[1][0] * vec[0] + matrix[1][1] * vec[1] + matrix[1][2] * vec[2],
        matrix[2][0] * vec[0] + matrix[2][1] * vec[1] + matrix[2][2] * vec[2],
    )


def proper_cubic_group() -> tuple[IntMat, ...]:
    group: list[IntMat] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row_index in range(3):
                row = [0, 0, 0]
                row[perm[row_index]] = signs[row_index]
                rows.append(tuple(row))
            matrix = (rows[0], rows[1], rows[2])
            if mat3_det(matrix) == 1:
                group.append(matrix)
    return tuple(group)


def rotate_occupancy(rotation: IntMat, occ: Occ) -> Occ:
    new = [0, 0, 0, 0, 0, 0]
    for old_index, occupied in enumerate(occ):
        if not occupied:
            continue
        new_vec = apply_intmat(rotation, DIRECTIONS[old_index])
        new[SLOT_OF[new_vec]] = 1
    return (new[0], new[1], new[2], new[3], new[4], new[5])


def bloch_of(occ: Occ) -> Bloch:
    """Identity gate: displayed directed kernel with scale 1/3."""
    nx = THIRD * (occ[0] - occ[1])
    ny = THIRD * (occ[2] - occ[3])
    nz = THIRD * (occ[4] - occ[5])
    return (nx, ny, nz)


def bloch_norm2(bloch: Bloch) -> Fraction:
    return bloch[0] * bloch[0] + bloch[1] * bloch[1] + bloch[2] * bloch[2]


def rotate_bloch(rotation: IntMat, bloch: Bloch) -> Bloch:
    vec = (
        rotation[0][0] * bloch[0]
        + rotation[0][1] * bloch[1]
        + rotation[0][2] * bloch[2],
        rotation[1][0] * bloch[0]
        + rotation[1][1] * bloch[1]
        + rotation[1][2] * bloch[2],
        rotation[2][0] * bloch[0]
        + rotation[2][1] * bloch[1]
        + rotation[2][2] * bloch[2],
    )
    return (Fraction(vec[0]), Fraction(vec[1]), Fraction(vec[2]))


def formation_ready(occ: Occ) -> bool:
    """Identity gate: ready iff the directed kernel is nonzero."""
    return bloch_of(occ) != (ZERO, ZERO, ZERO)


def axis_menu(occ: Occ) -> tuple[str, Fraction, Fraction] | None:
    """Axis-aligned restriction of the spectral measure (k=1)."""
    bloch = bloch_of(occ)
    nonzero = [index for index, coord in enumerate(bloch) if coord != 0]
    if len(nonzero) != 1:
        return None
    axis = ("x", "y", "z")[nonzero[0]]
    n_axis = bloch[nonzero[0]]
    plus = (ONE + n_axis) / TWO
    minus = (ONE - n_axis) / TWO
    return (axis, plus, minus)


def directed_k(occ: Occ) -> int:
    bloch = bloch_of(occ)
    coords = (bloch[0] * 3, bloch[1] * 3, bloch[2] * 3)
    return int(coords[0] * coords[0] + coords[1] * coords[1] + coords[2] * coords[2])


def spectral_measure(occ: Occ) -> tuple[int, Bloch] | None:
    """Identity gate: unique covariant spectral measure, or None if n=0."""
    if not formation_ready(occ):
        return None
    return (directed_k(occ), bloch_of(occ))


def formation_prob(occ: Occ) -> Fraction:
    """Identity gate: f=1 iff n≠0, else 0."""
    return ONE if formation_ready(occ) else ZERO


def record_update(occ: Occ, already_locked: bool, draw_plus: bool) -> str:
    """Identity gate: permanence, blank, or spectral lock."""
    if already_locked:
        return "keep"
    if not formation_ready(occ):
        return "blank"
    return "plus" if draw_plus else "minus"


def pairing(left: Fraction | int, right: Fraction | int) -> Fraction:
    """Identity gate: displayed Q-bilinear pairing is multiplication."""
    return Fraction(left) * Fraction(right)


def wick_a() -> Fraction:
    """Identity gate: displayed clock table is the single value 1."""
    return ONE


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def all_occupancies() -> tuple[Occ, ...]:
    return tuple(
        (bits[0], bits[1], bits[2], bits[3], bits[4], bits[5])
        for bits in product((0, 1), repeat=6)
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    group = proper_cubic_group()

    print("external_scientific_inputs: none; L0 tables are displayed member data")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q/Fraction occupancy-to-Bloch tables; no adopted law")
    print("negative_scope: L0 is one member, not the unique member, not axiom text")

    checks.check(
        "gate-bloch-empty",
        "bloch_of(empty)=(0,0,0)",
        bloch_of(EMPTY) == (ZERO, ZERO, ZERO),
    )
    checks.check(
        "gate-bloch-plus-x",
        "bloch_of(+x)=(1/3,0,0)",
        bloch_of(PLUS_X) == (THIRD, ZERO, ZERO),
    )
    checks.check(
        "gate-bloch-minus-x",
        "bloch_of(-x)=(-1/3,0,0)",
        bloch_of(MINUS_X) == (-THIRD, ZERO, ZERO),
    )
    checks.check(
        "gate-bloch-plus-y",
        "bloch_of(+y)=(0,1/3,0)",
        bloch_of(PLUS_Y) == (ZERO, THIRD, ZERO),
    )
    checks.check(
        "thm1-opposite-cancels",
        "opposite +x,-x pair has n=0",
        bloch_of(OPP_X) == (ZERO, ZERO, ZERO),
    )
    checks.check(
        "thm1-two-axis",
        "+x and +y give n=(1/3,1/3,0)",
        bloch_of(PLUS_X_PLUS_Y) == (THIRD, THIRD, ZERO),
    )
    checks.check(
        "thm1-all-states-in-ball",
        "every occupancy six-tuple has |n|^2 <= 1/3",
        all(bloch_norm2(bloch_of(occ)) <= THIRD for occ in all_occupancies()),
    )
    checks.check(
        "thm2-varies-with-nn",
        "empty neighborhood disagrees with lone +x",
        bloch_of(EMPTY) != bloch_of(PLUS_X),
    )
    checks.check(
        "thm3-group-count",
        "|G|=24 and Rz lies in G",
        len(group) == 24 and len(set(group)) == 24 and RZ in group,
    )
    checks.check(
        "thm3-rz-plus-x",
        "Rz sends lone +x occupancy to lone +y",
        rotate_occupancy(RZ, PLUS_X) == PLUS_Y
        and rotate_bloch(RZ, bloch_of(PLUS_X)) == bloch_of(PLUS_Y),
    )
    covariance_ok = all(
        bloch_of(rotate_occupancy(rotation, occ)) == rotate_bloch(rotation, bloch_of(occ))
        for rotation in group
        for occ in all_occupancies()
    )
    checks.check(
        "thm3-full-covariance",
        "n(R·c)=R n(c) for every R in G and every occupancy",
        covariance_ok,
    )
    checks.check(
        "thm4-empty-not-ready",
        "empty neighborhood is not formation-ready",
        not formation_ready(EMPTY),
    )
    checks.check(
        "thm4-plus-x-ready",
        "lone +x is formation-ready",
        formation_ready(PLUS_X),
    )
    checks.check(
        "thm4-opposite-not-ready",
        "opposite pair is not formation-ready",
        not formation_ready(OPP_X),
    )
    checks.check(
        "thm4-two-axis-ready",
        "two-axis occupancy is formation-ready",
        formation_ready(PLUS_X_PLUS_Y),
    )
    plus_x_menu = axis_menu(PLUS_X)
    minus_x_menu = axis_menu(MINUS_X)
    checks.check(
        "thm5-plus-x-menu",
        "lone +x menu is x-axis with probabilities 2/3 and 1/3",
        plus_x_menu == ("x", Fraction(2, 3), Fraction(1, 3)),
    )
    checks.check(
        "thm5-minus-x-menu",
        "lone -x menu swaps the x-axis probabilities",
        minus_x_menu == ("x", Fraction(1, 3), Fraction(2, 3)),
    )
    checks.check(
        "thm6-two-axis-has-measure",
        "two-axis n has a spectral measure with k=2",
        spectral_measure(PLUS_X_PLUS_Y) is not None
        and spectral_measure(PLUS_X_PLUS_Y)[0] == 2
        and axis_menu(PLUS_X_PLUS_Y) is None,
    )
    ready = [occ for occ in all_occupancies() if formation_ready(occ)]
    measured = [occ for occ in all_occupancies() if spectral_measure(occ) is not None]
    zero_n = [occ for occ in all_occupancies() if not formation_ready(occ)]
    checks.check(
        "thm6-total-counts",
        "64 occupancies: 8 with n=0, 56 ready, 56 spectral measures",
        len(list(all_occupancies())) == 64
        and len(zero_n) == 8
        and len(ready) == 56
        and len(measured) == 56
        and all(spectral_measure(occ) is not None for occ in ready)
        and all(spectral_measure(occ) is None for occ in zero_n),
    )
    probs_ok = True
    for occ in ready:
        k = directed_k(occ)
        # p± = (3 ± sqrt(k))/6 sum to 1 and are positive because k in {1,2,3}
        if k not in (1, 2, 3):
            probs_ok = False
    checks.check(
        "thm6-spectral-probs",
        "every ready cell has k in {1,2,3} so p±=(3±√k)/6 is a probability",
        probs_ok,
    )
    checks.check(
        "thm6b-formation-prob",
        "f=1 on ready cells and f=0 on n=0",
        formation_prob(PLUS_X) == ONE
        and formation_prob(EMPTY) == ZERO
        and formation_prob(OPP_X) == ZERO
        and all(formation_prob(occ) == ONE for occ in ready),
    )
    checks.check(
        "thm6b-record-update",
        "draw locks; n=0 stays blank; permanence keeps an existing lock",
        record_update(PLUS_X, False, True) == "plus"
        and record_update(PLUS_X, False, False) == "minus"
        and record_update(EMPTY, False, True) == "blank"
        and record_update(PLUS_X, True, True) == "keep"
        and record_update(PLUS_X, True, False) == "keep",
    )
    checks.check(
        "thm7-wick-a",
        "displayed clock table is a=1",
        wick_a() == ONE,
    )
    checks.check(
        "thm8-pairing-table",
        "displayed pairing is multiplication on the listed pairs",
        pairing(0, 0) == 0
        and pairing(1, 1) == 1
        and pairing(2, 3) == 6
        and pairing(-1, 4) == -4,
    )

    four_axioms = axiom.split("## The Four Framework Axioms", 1)[-1].split(
        "## Qualification", 1
    )[0]
    memo_names_member = (
        "L0" in four_axioms
        or "Wick" in four_axioms
        or "Born" in four_axioms
        or "a = 1" in four_axioms
    )
    checks.check(
        "mutation-empty-equals-plus-x-fails",
        "predicate ρ(empty)==ρ(+x) must fail",
        bloch_of(EMPTY) != bloch_of(PLUS_X),
    )
    checks.check(
        "mutation-opposite-ready-fails",
        "predicate opposite pair is formation-ready must fail",
        not formation_ready(OPP_X),
    )
    checks.check(
        "mutation-two-axis-no-measure-fails",
        "predicate two-axis n has no spectral measure must fail",
        spectral_measure(PLUS_X_PLUS_Y) is not None,
    )
    checks.check(
        "mutation-memo-names-l0-fails",
        "predicate live memo names L0 / Born / Wick a=1 as axiom content must fail",
        not memo_names_member
        and "determined by, and varies with, the nearest-neighbor conditions." in four_axioms
        and "locks exactly one admissible local possibility" in four_axioms,
    )
    checks.check(
        "mutation-note-adopts-fails",
        "predicate note adopts L0 as axiom text must fail",
        "not adopted" in note
        and "we adopt" not in note
        and "L_phys" not in note,
    )
    checks.check(
        "mutation-lattice-named-fails",
        "predicate note claims Lattice-named kernel must fail",
        "Lattice-named" not in note,
    )
    checks.check(
        "quoted-parents",
        "note quotes live Admissibility, Record, and Qubit",
        "determined by, and varies with, the nearest-neighbor conditions." in note
        and "locks exactly one admissible local possibility" in note
        and "Only records are readable." in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note
        and "No possibility is privileged" in note,
    )
    checks.check(
        "one-member-contract",
        "note states L0 is one member and not the unique member",
        "one member" in note
        and "not the unique member" in note
        and "not adopted" in note
        and "spectral measure" in note
        and "disconnected" in note,
    )
    forbidden = (
        "Lattice-named",
        "we adopt",
        "L_phys",
        "Gleason",
        "0.5934",
        "#6219",
        "#6263",
        "#6268",
        "#6272",
        "#6273",
        "#6276",
        "#6277",
        "exhausted",
        "closes the route",
        "only route",
        "therefore Born",
        "pairing-on-J",
        "pairing on J",
        "flip Qubit",
        "Qubit is M_3",
    )
    checks.check(
        "boundary-forbidden-phrases",
        "note omits forbidden adoption and close-the-route phrases",
        all(phrase not in note for phrase in forbidden)
        and "Qubit remains `M_2(C)`" in note
        and "I_2/2" in note
        and "This note authors no audit verdict" in note,
    )
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and no hypothetical axiom adoption",
        "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/ONE_EXECUTABLE_AXIOM_CLASS_MEMBER_DISPLAYED_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source,
    )
    checks.check(
        "identity-gates-present",
        "runner source defines the required identity gates",
        "def bloch_of(" in self_source
        and "def formation_ready(" in self_source
        and "def spectral_measure(" in self_source
        and "def formation_prob(" in self_source
        and "def record_update(" in self_source
        and "def pairing(" in self_source
        and "def wick_a(" in self_source,
    )
    checks.check(
        "not-qcd",
        "QCD appears only as a negation / unused boundary",
        ("QCD is unused" in note or "not QCD" in note or "No color or QCD" in note)
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: checked exactly — each occupancy six-tuple has |n|^2 <= 1/3")
    print("per_site: checked exactly — formation and axis menu live at the plus-shape center")
    print("per_mode: checked exactly — cube covariance of n on all 24 proper cubic matrices")
    print("per_block: checked exactly — L0 tables run; uniqueness of L0 is not claimed")
    print("lattice_wide: checked and not executed — no law is adopted as axiom text")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
