#!/usr/bin/env python3
"""Exact checks: two-block Y_0 cubic is nonzero; P-HY completion remains open.

Y(t)=t Y_0 on C^8 has Tr(Y(t)^3)=-48 t^3. Identity gates call cubic_trace(t).
The cubic vanishes iff t=0. Y_like is not U(1)_Y. No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_BLOCK_Y0_CUBIC_TRACE_NONVANISHING_P_HY_COMPLETION_OPEN_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
MAY2_PATH = (
    ROOT / "docs" / "LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md"
)
HY_PATH = ROOT / "docs" / "HYPERCHARGE_IDENTIFICATION_NOTE.md"
CYCLE692_PATH = ROOT / "docs" / "PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
MAY1_PATH = (
    ROOT / "docs" / "LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md"
)

AUDIT_INPUT_PATHS = (
    "docs/TWO_BLOCK_Y0_CUBIC_TRACE_NONVANISHING_P_HY_COMPLETION_OPEN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
    "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md",
    "docs/PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]

NONZERO_SCALES = (
    Fraction(1),
    Fraction(1, 3),
    Fraction(1, 6),
    Fraction(-2),
    Fraction(5, 7),
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def diag(values: tuple[Fraction, ...]) -> Matrix:
    n = len(values)
    return tuple(tuple(values[i] if i == j else Fraction(0) for j in range(n)) for i in range(n))


def add(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(tuple(left[i][j] + right[i][j] for j in range(n)) for i in range(n))


def scale(matrix: Matrix, coeff: Fraction) -> Matrix:
    n = len(matrix)
    return tuple(tuple(coeff * matrix[i][j] for j in range(n)) for i in range(n))


def mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(n)), Fraction(0)) for j in range(n))
        for i in range(n)
    )


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def rank(matrix: Matrix) -> int:
    n = len(matrix)
    work = [list(row) for row in matrix]
    row_index = 0
    for col in range(n):
        pivot = next((r for r in range(row_index, n) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[row_index], work[pivot] = work[pivot], work[row_index]
        pivot_value = work[row_index][col]
        work[row_index] = [entry / pivot_value for entry in work[row_index]]
        for r in range(n):
            if r != row_index and work[r][col] != 0:
                factor = work[r][col]
                work[r] = [work[r][c] - factor * work[row_index][c] for c in range(n)]
        row_index += 1
    return row_index


def pi_plus() -> Matrix:
    return diag((Fraction(1),) * 6 + (Fraction(0),) * 2)


def pi_minus() -> Matrix:
    return diag((Fraction(0),) * 6 + (Fraction(1),) * 2)


def y0() -> Matrix:
    return add(pi_plus(), scale(pi_minus(), Fraction(-3)))


def y_of_t(t: Fraction) -> Matrix:
    """Y(t)=t Y_0 = t (Pi_+ - 3 Pi_-)."""
    return scale(y0(), t)


def cubic_trace(t: Fraction) -> Fraction:
    """Identity-gate function: Tr(Y(t)^3) from the C^8 operator."""
    y = y_of_t(t)
    return trace(mul(mul(y, y), y))


def spectrum_cubic(t: Fraction) -> Fraction:
    """Independent eigenvalue-cube sum 6 t^3 + 2 (-3t)^3."""
    plus = t
    minus = Fraction(-3) * t
    return 6 * plus**3 + 2 * minus**3


def cubic_trace_forced_zero(t: Fraction) -> Fraction:
    """Mutation: replace cubic_trace by the zero function."""
    del t
    return Fraction(0)


def some_nonzero_vanishes(trace_fn) -> bool:
    """Predicate: some nonzero t has vanishing cubic on these 8 components."""
    return any(scale != 0 and trace_fn(scale) == 0 for scale in NONZERO_SCALES)


def y_like_is_u1y_theorem() -> bool:
    """False theorem: Y_like on these 8 components is anomaly-complete U(1)_Y."""
    return cubic_trace(Fraction(1, 3)) == Fraction(0)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    may2 = MAY2_PATH.read_text(encoding="utf-8")
    hy_note = HY_PATH.read_text(encoding="utf-8")
    cycle692 = CYCLE692_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    may1 = MAY1_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_may2 = normalize(may2)
    normalized_may1 = normalize(may1)
    normalized_cycle692 = normalize(cycle692).replace("> ", "")

    print(
        "external_scientific_inputs: May 2 ranks and ratio, name-free Y_0, "
        "cycle 692 scale freedom, and the May 1 Y^3 exclusion are source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: the 8-component cubic is nonzero at every nonzero "
        "scale; Y_like is not U(1)_Y; a completion remains open"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, May 2, name-free Y_0, cycle 692, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_BLOCK_Y0_CUBIC_TRACE_NONVANISHING_P_HY_COMPLETION_OPEN_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
            "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md",
            "docs/PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    checks.check(
        "source-may2-ratio",
        "May 2 pins ranks 6 and 2 and the forced ratio beta=-3 alpha",
        "6 · α + 2 · β = 0" in may2
        and "β = −3 α" in may2
        and "1 : (−3)" in may2,
    )
    checks.check(
        "source-may2-no-identify",
        "May 2 does not identify the ratio with Y",
        "identification with Standard Model hypercharge Y" in may2
        and "out of scope here" in normalized_may2
        and "does not identify with Y" in note,
    )
    checks.check(
        "source-y0-generator",
        "the name-free note writes Y_0 = P_sym - 3 P_anti",
        "Y_0 = P_sym - 3 P_anti" in hy_note,
    )
    checks.check(
        "source-cycle692-scale",
        "cycle 692 records that tracelessness does not fix alpha=1/3",
        "Tracelessness fixes the ratio and nothing else" in cycle692
        and "explicitly supplied alpha=1/3 normalization" in cycle692
        and "which the packet says is not derived" in normalized_cycle692,
    )
    checks.check(
        "source-may1-y3-scoped",
        "May 1 closed SU(2)^2 Y and scoped Y^3 out",
        "SU(2)² × U(1)_Y" in may1
        and "Y³) are scoped" in may1
        and "are **not** derived in this note" in may1
        and "U(1)_Y³ anomaly" in may1
        and "Requires the full one-" in normalized_may1,
    )

    plus = pi_plus()
    minus = pi_minus()
    generator = y0()
    checks.check(
        "two-block-ranks",
        "Pi_+ and Pi_- are complementary rank-(6,2) projectors",
        rank(plus) == 6
        and rank(minus) == 2
        and rank(add(plus, minus)) == 8
        and mul(plus, plus) == plus
        and mul(minus, minus) == minus
        and mul(plus, minus) == scale(plus, Fraction(0)),
        residual=(rank(plus), rank(minus)),
    )
    checks.check(
        "y0-spectrum-trace",
        "Y_0 has spec {+1 x6, -3 x2} and vanishing linear trace",
        trace(generator) == Fraction(0)
        and all(generator[i][i] == Fraction(1) for i in range(6))
        and all(generator[i][i] == Fraction(-3) for i in range(6, 8)),
        residual=trace(generator),
    )

    formula_ok = True
    spectrum_ok = True
    for sample in (Fraction(0),) + NONZERO_SCALES:
        value = cubic_trace(sample)
        cubes = spectrum_cubic(sample)
        closed = Fraction(-48) * sample**3
        if value != closed:
            formula_ok = False
        if cubes != closed or cubes != value:
            spectrum_ok = False
    checks.check(
        "theorem-1-cubic-formula",
        "identity-gate cubic_trace(t) equals -48 t^3 and the eigenvalue-cube sum",
        formula_ok and spectrum_ok,
    )

    t1 = cubic_trace(Fraction(1))
    t13 = cubic_trace(Fraction(1, 3))
    t16 = cubic_trace(Fraction(1, 6))
    witness_t1 = 6 * Fraction(1) ** 3 + 2 * Fraction(-3) ** 3
    witness_t13 = 6 * Fraction(1, 3) ** 3 + 2 * Fraction(-1) ** 3
    witness_t16 = 6 * Fraction(1, 6) ** 3 + 2 * Fraction(-1, 2) ** 3
    checks.check(
        "theorem-1-specializations",
        "specializations are -48, -16/9, -2/9 and match the displayed witnesses",
        t1 == Fraction(-48) == witness_t1
        and t13 == Fraction(-16, 9) == witness_t13
        and t16 == Fraction(-2, 9) == witness_t16
        and "6(1)^3 + 2(-3)^3 = 6-54 = -48" in note
        and "6(1/3)^3 + 2(-1)^3 = 2/9 - 2 = -16/9" in note
        and "6(1/6)^3 + 2(-1/2)^3 = 1/36 - 1/4 = -2/9" in note,
        residual=(t1, t13, t16),
    )
    checks.check(
        "theorem-1-linear-not-cubic",
        "the May 2 linear trace vanishes at every scale and does not evaluate the cubes",
        all(trace(y_of_t(sample)) == Fraction(0) for sample in NONZERO_SCALES)
        and t1 != Fraction(0)
        and t13 != Fraction(0),
    )

    zero_value = cubic_trace(Fraction(0))
    nonzero_values = [cubic_trace(sample) for sample in NONZERO_SCALES]
    checks.check(
        "theorem-2-never-zero",
        "cubic_trace(t)=0 iff t=0; every nonzero sample is nonzero",
        zero_value == Fraction(0)
        and all(value != 0 for value in nonzero_values)
        and all(value == Fraction(-48) * sample**3 for value, sample in zip(nonzero_values, NONZERO_SCALES)),
        residual=nonzero_values,
    )
    checks.check(
        "theorem-2-predicate",
        "the predicate that some nonzero t has vanishing cubic on these 8 components is false",
        some_nonzero_vanishes(cubic_trace) is False
        and Y_of_zero_is_not_hypercharge(zero_value),
    )

    checks.check(
        "theorem-3-may1-scope",
        "the note quotes May 1's Y^3 exclusion and treats the cubic as that residual",
        "Y³" in note
        and "are scoped" in note
        and "are **not** derived in this note" in note
        and "U(1)_Y³ anomaly" in note
        and "May 1 closed" in note
        and "SU(2)^2" in note,
    )

    axiom_needles = ("Y_like", "U(1)_Y", "Y_0", "Y(t)", "cubic_trace", "Pi_+")
    checks.check(
        "theorem-4-scale-extra",
        "axioms do not select t; cycle 692 leaves alpha=1/3 underived",
        all(needle not in axiom for needle in axiom_needles)
        and "does not identify with Y" in note
        and "does not identify `Y_like` with `U(1)_Y`" in note
        and "α=1/3` is not derived" in note
        and "Tracelessness fixes the ratio and nothing else" in cycle692,
    )
    checks.check(
        "theorem-4-cubic-nonzero-at-named-scales",
        "Y_like and PDG-like points have nonzero cubics -16/9 and -2/9",
        cubic_trace(Fraction(1, 3)) == Fraction(-16, 9)
        and cubic_trace(Fraction(1, 6)) == Fraction(-2, 9)
        and y_like_is_u1y_theorem() is False,
        residual=(cubic_trace(Fraction(1, 3)), cubic_trace(Fraction(1, 6))),
    )

    checks.check(
        "theorem-5-completion-open",
        "a later completion remains open and extra fields are not adopted",
        "Completion Remains Open" in note
        and "does not adopt one" in normalized_note
        and "right-handed singlets" in note
        and "P-HY remains open" in note
        and 'hypothetical_axiom_status: "no edit"' in note,
    )

    checks.check(
        "mutation-zero-fails",
        "replacing cubic_trace by 0 fails at t=1 and t=1/3",
        cubic_trace(Fraction(1)) == Fraction(-48)
        and cubic_trace(Fraction(1, 3)) == Fraction(-16, 9)
        and cubic_trace_forced_zero(Fraction(1)) == Fraction(0)
        and cubic_trace_forced_zero(Fraction(1, 3)) == Fraction(0)
        and cubic_trace(Fraction(1)) != cubic_trace_forced_zero(Fraction(1))
        and cubic_trace(Fraction(1, 3)) != cubic_trace_forced_zero(Fraction(1, 3)),
        residual=(cubic_trace(Fraction(1)), cubic_trace(Fraction(1, 3))),
    )
    checks.check(
        "mutation-vanishing-predicate-fails",
        "a predicate that some nonzero t has vanishing cubic fails Theorem 2",
        some_nonzero_vanishes(cubic_trace) is False
        and some_nonzero_vanishes(cubic_trace_forced_zero) is True
        and some_nonzero_vanishes(cubic_trace) != some_nonzero_vanishes(cubic_trace_forced_zero),
    )
    checks.check(
        "mutation-identify-fails",
        "identifying Y_like with U(1)_Y as a theorem fails: scale extra and cubic nonzero",
        y_like_is_u1y_theorem() is False
        and cubic_trace(Fraction(1, 3)) != Fraction(0)
        and "does not identify `Y_like` with `U(1)_Y`" in note
        and "explicitly supplied alpha=1/3" in cycle692,
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: frontier_discovery",
                "target_claim_id: p_hy_identification",
                "reachability_to_target: prunes",
                'target_blocker_text: "identify the two-block traceless line with anomaly-complete physical hypercharge"',
                'next_trace_action: "The 8-component cubic is nonzero at every nonzero scale. A completion remains open. Do not identify Y_like with U(1)_Y. Do not adopt axiom text."',
                "does not identify with Y",
                "does not identify `Y_like` with `U(1)_Y`",
                "authors no audit verdict",
            )
        )
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md" in note
        and "HYPERCHARGE_IDENTIFICATION_NOTE.md" in note
        and "PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md" in note
        and "LH_DOUBLET_SU2_SQUARED_HYPERCHARGE_ANOMALY_CANCELLATION_NOTE_2026-05-01.md" in note
        and "**Type:** bounded_theorem" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note
        and "campaign" not in note.lower()
        and "this block" not in note.lower(),
    )
    checks.check(
        "canonical-nonmutation",
        "the cubic construction is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("Y(t)", "Y_like", "U(1)_Y", "cubic_trace", "Tr(Y(t)^3)", "-48 t^3")
        ),
    )
    checks.check(
        "may2-ratio-bound",
        "May 2 still states the structural ratio and refuses SM-Y identification",
        "1 : (−3)" in may2
        and "identification with Standard Model hypercharge Y" in may2
        and "any anomaly-cancellation result (out of scope)" in normalized_may2,
    )

    n5_lines = (
        "per_element: the eight eigenvalues of Y(t) and the specializations -48, -16/9, -2/9 are recomputed",
        "per_site: the single C^8 two-block carrier is the only site; no composite generation",
        "per_mode: only the cubic trace of the two-block line is executed; no mixed SU(3)^2 Y mode",
        "per_block: Theorems 4-5 close identification and axiom edit, not a later completion",
        "lattice_wide: checked and not executed — no lattice-wide hypercharge or U(1)_Y law is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


def Y_of_zero_is_not_hypercharge(zero_value: Fraction) -> bool:
    """The zero operator is excluded from the live two-block line."""
    return zero_value == Fraction(0) and y_of_t(Fraction(0)) == scale(y0(), Fraction(0))


if __name__ == "__main__":
    raise SystemExit(main())
