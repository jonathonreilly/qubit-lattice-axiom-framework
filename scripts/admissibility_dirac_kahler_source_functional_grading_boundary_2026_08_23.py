#!/usr/bin/env python3
"""Block 179: derive the Gaussian source grading and expose its exact boundary.

The normalized complex Gaussian forces its covariance and Wick tower.  On the
two inherited Dirac--Kahler fixtures, the prose reflection convention then
forces a raw one-particle kernel which is non-Hermitian on the full selected
source space.  A parent-supplied rank-two isometry nevertheless gives an exact positive,
Hermitian, transport-sensitive restriction, so this is a selection boundary
and not a universal no-go.

The runner also keeps three categorically different scalars apart: the
normalized vacuum coefficient 1, the unnormalized coefficient Z_Q, and the
doubled partition readout |Z_Q|^2.  The last is not the degree-zero coefficient
of the same Wick tower without a separate gluing/reweighting law.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15 as b107
import admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23 as b177
import admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23 as b178


NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs/audit/data/axiom_premise_nodes.json"
SCALE_PRIMITIVE = ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PRIMITIVE = ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_STATE_PRIMITIVE = ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
B107_NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
B170_NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_TWO_BOUNDED_THEOREM_"
    "NOTE_2026-08-21.md"
)
B170_RUNNER = SCRIPTS / (
    "admissibility_dirac_kahler_closure_audit_two_2026_08_21.py"
)
B176_NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
B177_NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_"
    "THEOREM_NOTE_2026-08-23.md"
)
B178_NOTE = ROOT / (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_"
    "COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

# Complete direct worktree-read surface for content-pinned cache freshness.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCE_FUNCTIONAL_GRADING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_TWO_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_closure_audit_two_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COMPLEX_STRUCTURE_SYNTHESIS_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_complex_structure_synthesis_2026_08_23.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONDITIONAL_SYMMETRIC_POWER_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_conditional_symmetric_power_theorem_2026_08_23.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RANK_TWO_SCALAR_TRANSPORT_COUNTEREXAMPLE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_rank_two_scalar_transport_counterexample_2026_08_23.py",
    "scripts/admissibility_dirac_kahler_pincer_identity_cross_lane_2026_08_22.py",
)

AUDIT_TIMEOUT_SEC = 120

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)

FIXTURES = (("8x4", 8, 4), ("12x4", 12, 4))
DIALS = (ZERO, R(1, 4))
EXPECTED_INERTIA = {
    ("8x4", ZERO): (6, 2, 0),
    ("8x4", R(1, 4)): (6, 2, 0),
    ("12x4", ZERO): (4, 4, 0),
    ("12x4", R(1, 4)): (4, 4, 0),
}
EXPECTED_ACTION_REFLECTION_DEFECT_00 = {
    "8x4": R(-997, 27456),
    "12x4": R(3167, 10560),
}
EXPECTED_HALF_TRACE_GAP = {
    "8x4": R(73977924244224, 1492124486100431),
    "12x4": R(
        150346029799280479942166602650413136160,
        2455275247171512614379752553769527826469,
    ),
}


class Reporter:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    def total(self) -> None:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.expand(a - b) == 0 for a, b in zip(left, right)
    )


def source_functional_checks(report: Reporter) -> None:
    """Differentiate the exact normalized two-source Gaussian."""
    bj0, bj1, j0, j1 = sp.symbols("bar_j0 bar_j1 j0 j1")
    g00, g01, g10, g11 = sp.symbols("g00 g01 g10 g11")
    bar_j = sp.Matrix((bj0, bj1))
    source_j = sp.Matrix((j0, j1))
    covariance = sp.Matrix(((g00, g01), (g10, g11)))
    exponent = (bar_j.T * covariance * source_j)[0]
    normalized = sp.exp(exponent)
    at_zero = {bj0: 0, bj1: 0, j0: 0, j1: 0}

    two_point = sp.Matrix(
        2,
        2,
        lambda i, j: sp.diff(normalized, bar_j[i], source_j[j]).subs(at_zero),
    )
    four_point = sp.diff(normalized, bj0, bj1, j0, j1).subs(at_zero)
    same_type = sp.diff(normalized, bj0, bj1).subs(at_zero)
    report.check(
        "SOURCE_TWO_POINT",
        matrix_equal(two_point, covariance),
        "d_barJ d_J exp(barJ G J)|0 = G exactly",
    )
    report.check(
        "SOURCE_WICK_PERMANENT",
        sp.expand(four_point - (g00 * g11 + g01 * g10)) == 0
        and same_type == 0,
        "degree two is the permanent and same-polarity contractions vanish",
    )
    report.check(
        "NORMALIZED_VACUUM",
        normalized.subs(at_zero) == 1,
        "the degree-zero coefficient of the normalized Wick tower is 1",
    )

    zq, zq_bar = sp.symbols("Z_Q Z_Qbar", nonzero=True)
    unnormalized = zq * normalized
    doubled = zq * zq_bar
    scaled_two_point = sp.Matrix(
        2,
        2,
        lambda i, j: sp.diff(
            doubled * normalized, bar_j[i], source_j[j]
        ).subs(at_zero),
    )
    report.check(
        "VACUUM_CATEGORY_SPLIT",
        unnormalized.subs(at_zero) == zq
        and doubled != zq
        and matrix_equal(scaled_two_point, doubled * covariance),
        "unnormalized vacuum=Z_Q, doubled readout=Z_Q Z_Qbar, and reweighting scales every sector",
    )


def prose_code_orientation_check(report: Reporter) -> None:
    """Exercise the Block-107 prose/code transpose mismatch on generic data."""
    symbols = sp.symbols("g0:16")
    generic = sp.Matrix(4, 4, symbols)

    def site_index(time: int, space: int) -> int:
        assert space == 0
        return time % 4

    code = b107.history_gram(generic, site_index, spatial_extent=1)
    positive = (0, 1)
    reflected = (3, 2)
    prose = sp.Matrix(
        2,
        2,
        lambda a, b: sp.conjugate(generic[positive[b], reflected[a]]),
    )
    report.check(
        "REFLECTION_ORIENTATION_MISMATCH",
        matrix_equal(code, prose.T) and not matrix_equal(code, prose),
        "Block-107 code gives the transpose of its K_ab=conj(G(b,theta a)) prose equation on generic G",
    )


def selection(matrix: sp.MatrixBase, rows: tuple[int, ...]) -> sp.Matrix:
    return sp.Matrix(
        len(rows),
        len(rows),
        lambda a, b: sp.expand(matrix[rows[a], rows[b]]),
    )


def exact_fixture_checks(report: Reporter) -> None:
    """Measure the forced full kernel and the live rank-two restriction."""
    isometry = b178.isometry()
    projector = sp.expand(isometry * isometry.H)
    swap = sp.Matrix(((0, 1), (1, 0)))
    u, v = sp.symbols("u v", real=True)
    weight_family = sp.zeros(8, 2)
    weight_family[0, 0], weight_family[4, 0] = u, v
    weight_family[2, 1], weight_family[6, 1] = u, v
    local_shift_two = sp.zeros(8, 8)
    for time_block in range(2):
        for space in range(4):
            local_shift_two[4 * time_block + (space + 2) % 4,
                            4 * time_block + space] = 1
    report.check(
        "PARENT_RANK_TWO_ISOMETRY",
        matrix_equal(isometry.H * isometry, sp.eye(2)),
        "X=[(4e0+3e4)/5,(4e2+3e6)/5] has X^dag X=I_2",
    )
    report.check(
        "PERIOD_TWO_DOES_NOT_SELECT_WEIGHTS",
        matrix_equal(local_shift_two * weight_family, weight_family * swap),
        "every time-weight pair (u,v), not only (4/5,3/5), intertwines x-translation by two",
    )

    for name, cover_t, width in FIXTURES:
        bench = b177.Bench(f"b179-{name}", cover_t, width)
        injection = sp.zeros(bench.N, len(bench.rows))
        for column, row in enumerate(bench.rows):
            injection[row, column] = 1
        ambient_shift_two = sp.zeros(bench.N, bench.N)
        for time in range(bench.T):
            for space in range(bench.lx):
                ambient_shift_two[
                    bench.lx * time + (space + 2) % bench.lx,
                    bench.lx * time + space,
                ] = 1
        compressed: dict[sp.Expr, sp.Matrix] = {}
        determinants: dict[sp.Expr, sp.Expr] = {}
        for dial in DIALS:
            q_matrix = sp.expand(bench.Q.subs(bench.carrier(st=dial)))
            determinants[dial] = sp.factor(q_matrix.det(method="domain-ge"))
            covariance = sp.expand(q_matrix.inv(method="LU"))
            prose_kernel = selection(bench.r * covariance.T, bench.rows)
            code_kernel = selection(covariance * bench.r, bench.rows)
            anti = sp.expand(prose_kernel - prose_kernel.H)
            hermitian_part = sp.expand((prose_kernel + prose_kernel.H) / 2)
            action_defect = sp.expand(bench.r * q_matrix.H * bench.r - q_matrix)
            restricted = sp.expand(isometry.H * prose_kernel * isometry)
            restricted_code = sp.expand(isometry.H * code_kernel * isometry)
            compressed[dial] = restricted

            local_q = selection(q_matrix, bench.rows)
            action_form = sp.expand(bench.form.subs(bench.carrier(st=dial)))
            residual_r = sp.expand(
                (sp.eye(8) - projector)
                * selection(bench.r, bench.rows)
                * isometry
            )
            residual_q = sp.expand(
                (sp.eye(8) - projector) * local_q * isometry
            )
            residual_form = sp.expand(
                (sp.eye(8) - projector) * action_form * isometry
            )

            report.check(
                f"{name}_{dial}_FULL_SOURCE_BOUNDARY",
                all(sp.im(value) == 0 for value in q_matrix)
                and all(sp.im(value) == 0 for value in covariance)
                and matrix_equal(code_kernel, prose_kernel.H)
                and not matrix_equal(prose_kernel, prose_kernel.H)
                and anti.rank() == 8
                and tuple(b177.b165.real_symmetric_inertia(hermitian_part))
                == EXPECTED_INERTIA[(name, dial)],
                (
                    "real fixture; prose/code kernels are adjoints; raw anti-Hermitian "
                    f"rank=8; Herm-part inertia={EXPECTED_INERTIA[(name, dial)]}"
                ),
            )
            report.check(
                f"{name}_{dial}_REFLECTION_COVARIANCE_DEFECT",
                action_defect[0, 0]
                == EXPECTED_ACTION_REFLECTION_DEFECT_00[name],
                (
                    "(r Q^dag r-Q)[0,0]="
                    f"{EXPECTED_ACTION_REFLECTION_DEFECT_00[name]} != 0"
                ),
            )
            report.check(
                f"{name}_{dial}_POSITIVE_RESTRICTION",
                matrix_equal(restricted, restricted.H)
                and matrix_equal(restricted, restricted_code)
                and restricted[0, 0] > 0
                and restricted.det() > 0,
                "X^dag K X is convention-independent here and positive definite by Sylvester",
            )
            report.check(
                f"{name}_{dial}_X_NOT_SELECTED_BY_INVARIANCE",
                matrix_equal(ambient_shift_two * q_matrix,
                             q_matrix * ambient_shift_two)
                and matrix_equal(ambient_shift_two * bench.r,
                                 bench.r * ambient_shift_two)
                and matrix_equal(
                    ambient_shift_two * injection * isometry,
                    injection * isometry * swap,
                )
                and residual_r.rank() == 2
                and residual_q.rank() == 2
                and residual_form.rank() == 2,
                "period-two symmetry explains the 2x2 shape, but X is not invariant under r, Q or the action form",
            )

        gap = sp.expand(
            sp.trace(compressed[R(1, 4)] - compressed[ZERO]) / 2
        )
        report.check(
            f"{name}_RESTRICTION_TRANSPORT_RESPONSE",
            gap == EXPECTED_HALF_TRACE_GAP[name] and gap > 0,
            f"half-trace gap from s_t=0 to 1/4 is exact and positive: {gap}",
        )
        report.check(
            f"{name}_ONE_COPY_VACUUM_RESPONSE",
            determinants[ZERO] > 0
            and determinants[R(1, 4)] > 0
            and determinants[ZERO] != determinants[R(1, 4)],
            "det(Q) is positive at both dials and changes exactly, so Z_Q is positive and dial-sensitive",
        )


def authority_and_scope_checks(report: Reporter) -> None:
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    scale_primitive = SCALE_PRIMITIVE.read_text(encoding="utf-8")
    kinetic_primitive = KINETIC_PRIMITIVE.read_text(encoding="utf-8")
    realized_state_primitive = REALIZED_STATE_PRIMITIVE.read_text(encoding="utf-8")
    b107_note = B107_NOTE.read_text(encoding="utf-8")
    b170_note = B170_NOTE.read_text(encoding="utf-8")
    b170_runner = B170_RUNNER.read_text(encoding="utf-8")
    b176_note = B176_NOTE.read_text(encoding="utf-8")
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    source_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    floats = [
        node
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    report.check(
        "AUTHORITY_BOUNDARY",
        "Born weight values" in axioms
        and "source/action and physical-observable identification" in axioms
        and "K_ab = conj(G(b, theta a))" in b107_note
        and "Theta(A) = r conj(A) r is a CONSTRUCTION OF THIS BLOCK"
        in b170_runner
        and "PARTITION-FUNCTION level rather than at the level of" in b176_note
        and "field configurations: the bra is the reflection" in b176_note
        and "PREMISE-CLASS PROBES, NOT FRAMEWORK OBJECTS" in b170_note,
        "axioms leave Born/source-observable bridges open; linear Theta and partition-to-field sewing are not supplied",
    )
    report.check(
        "PRIMITIVE_REGISTRY_BOUNDARY",
        all(
            claim_id in registry
            for claim_id in (
                '"minimal_axioms"',
                '"scale_reference_primitive"',
                '"kinetic_isotropy_primitive"',
                '"realized_state_primitive"',
            )
        )
        and "no mass ratio, coupling, mixing angle, phase, selector" in scale_primitive
        and "readout\nbridge" in scale_primitive
        and "angle, phase, selector, readout bridge" in kinetic_primitive
        and "state-selection rule" in realized_state_primitive
        and "weighting, probability rule" in realized_state_primitive,
        "the complete approved primitive registry supplies no event/source selector, readout bridge or probability weighting",
    )
    named = " ".join(b177.NAMED_PREMISES).lower()
    report.check(
        "SECOND_GLUE_PREMISE_ABSENT",
        "vacuum" not in named and "det q" not in named and "z zbar" not in named,
        "Block 177 names a Sym^n premise but no |Z|^2-to-Sym^0 source-sewing premise",
    )
    report.check(
        "EXACT_AST_SURFACE",
        not floats,
        f"float_literals={len(floats)} on the primary runner AST",
    )
    packet_needles = (
        "## No-Go Discipline Gate",
        "### Target contract",
        *(f"### N{i}" for i in range(1, 9)),
        "ATTEMPTED",
        "Pair | Close first implies second?",
        "Classification",
        "Cited witness | Witness residual",
        "Terminal obligation",
        "Gate result: **PASS for the narrowed partial-boundary claim**",
    )
    report.check(
        "NO_GO_PACKET_LANDING_SURFACE",
        all(needle in note for needle in packet_needles)
        and note.count("`ATTEMPTED`") >= 5,
        "N1-N8 tables and narrowed PASS disposition land in the note; this check is structural, not an audit verdict",
    )


def main() -> int:
    report = Reporter()
    try:
        source_functional_checks(report)
        prose_code_orientation_check(report)
        exact_fixture_checks(report)
        authority_and_scope_checks(report)
    except Exception as exc:  # fail closed and preserve the required total line
        report.check("UNCAUGHT_EXCEPTION", False, f"{type(exc).__name__}: {exc}")

    print(
        "per_element: source differentiation fixes G and Wick permanents; normalized, unnormalized and doubled vacuum scalars are distinct"
    )
    print(
        "per_site: the full eight-source reflected kernel is non-Hermitian at four exact cells, while one parent-supplied rank-two restriction is positive"
    )
    print(
        "per_mode: the positive restriction changes exactly with s_t, but no physical source/reflection selector is supplied"
    )
    print(
        "per_block: Block 179 derives the algebraic Wick part of B2b and repairs the one-copy versus doubled vacuum accounting"
    )
    print(
        "lattice_wide: no universal OS no-go, continuum result, Born derivation, axiom retirement, obligation retirement or TOE percentage move is claimed"
    )
    report.total()
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
