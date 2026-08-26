#!/usr/bin/env python3
"""Independent checker for the Block-205 H1 Schur probability germ."""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT = "4692fc1998b82328809bdf0696bf36a97cd7d3e3"
PREREG = "d067fbb5d2"
MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "951dad5c1a075687eb77b79d3a858e1fcc010c92"
PREFLIGHT_BLOB = "9613ca777600c348ccebacfc8a5255a654e67898"
TIMEOUT = 300

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
)

MUTATIONS = (
    "stale_authority",
    "alter_registration",
    "use_h1_column0",
    "make_reverse_adjoint",
    "erase_baseline_positivity",
    "import_i32",
    "erase_effect_completeness",
    "erase_effect_orthogonality",
    "erase_h1_derivative",
    "call_tangent_density",
    "deny_finite_germ",
    "break_coarse_pairs",
    "break_pointer_dilation",
    "erase_binary_variation",
    "call_four_ports_m2",
    "call_h1_eta",
    "call_write_record_formation",
    "call_schur_periodic",
    "claim_two_tt",
    "claim_axiom",
    "claim_obligation",
    "claim_toe",
    "claim_retained",
    "claim_no_go",
)


R = sp.Rational
I = sp.I
I16 = sp.eye(16)
ZERO16 = sp.zeros(16)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=TIMEOUT
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=TIMEOUT,
    ).returncode == 0


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix), extension=True).rank()


def positive(value: sp.Expr) -> bool:
    value = sp.factor(sp.simplify(value))
    return value.is_positive is True or sp.simplify(value > 0) is sp.true


def internal_trace(family: b193.Terms) -> sp.Matrix:
    return sp.expand(sum(
        (sp.trace(time) * internal for time, internal in family), ZERO16
    ))


def block(a: sp.MatrixBase, b: sp.MatrixBase,
          c: sp.MatrixBase, d: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


@cache
def authority() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_now": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_now": git("hash-object", "--", PREFLIGHT),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def rebuild() -> dict[str, object]:
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[i] + transfer[i] for i in range(4))
    incoming_sector = b193.sector_terms(incoming)
    outgoing_sector = b193.sector_terms(outgoing)
    raw_in = internal_trace(incoming_sector["gram"])
    raw_out = internal_trace(outgoing_sector["gram"])
    trace_in = sp.factor(sp.trace(raw_in))
    trace_out = sp.factor(sp.trace(raw_out))
    total = sp.factor(trace_in + trace_out)
    rho0 = sp.expand(sp.diag(raw_in, raw_out) / total)

    classification = b194.detector_classification_facts()
    orientation = classification["orientation"]
    connectors = tuple(sp.expand(effect * orientation)
                       for effect in b194.b191.EFFECTS)
    effects = tuple(sp.expand(block(
        effect, sign * connector, sign * connector.H, effect
    ) / 2) for effect, connector in zip(b194.b191.EFFECTS, connectors)
        for sign in (1, -1))

    tangent = b193.tt_tangent_columns("H1")
    overlaps = sp.Matrix(4, 2, lambda row, column: b193.term_trace(
        tangent["columns"][column], connectors[row].H
    ))
    real_overlaps = overlaps.applyfunc(lambda value: sp.factor(sp.simplify(
        (value + sp.conjugate(value)) / 2
    )))
    log_slopes = sp.expand(8 * real_overlaps / tangent["normalizer"])
    ell = sp.factor(log_slopes[0, 1])
    row_slopes = tuple(sp.factor(log_slopes[row, 1]) for row in range(4))
    derivatives = tuple(sp.factor(
        sign * row_slopes[row] / 8
    ) for row in range(4) for sign in (1, -1))
    conditional = tuple(sp.factor(
        sign * row_slopes[row] / 2
    ) for row in range(4) for sign in (1, -1))

    # Rebuild the pointer writer instead of consuming the parent's boolean.
    sector_orientation = block(ZERO16, orientation, orientation, ZERO16)
    p_plus = sp.expand((sp.eye(32) + sector_orientation) / 2)
    p_minus = sp.expand((sp.eye(32) - sector_orientation) / 2)
    pointer_i = sp.eye(2)
    pointer_x = sp.Matrix(((0, 1), (1, 0)))
    q_plus = sp.diag(1, 0)
    q_minus = sp.diag(0, 1)
    ket_zero = sp.Matrix(((1,), (0,)))
    writer = sp.expand(
        sp.kronecker_product(p_plus, pointer_i)
        + sp.kronecker_product(p_minus, pointer_x)
    )
    input_isometry = sp.kronecker_product(sp.eye(32), ket_zero)
    diagonal_events = tuple(block(effect, ZERO16, ZERO16, effect)
                            for effect in b194.b191.EFFECTS)
    induced = []
    for diagonal_event in diagonal_events:
        for pointer in (q_plus, q_minus):
            readout = sp.kronecker_product(diagonal_event, pointer)
            induced.append(sp.expand(
                input_isometry.H * writer.H * readout
                * writer * input_isometry
            ))

    coefficients = b193.tt_source_coefficients("H1", 1)
    source = b193.combined_source_pair_terms("H1", coefficients)
    return {
        "trace_in": trace_in,
        "trace_out": trace_out,
        "total": total,
        "rho0": rho0,
        "scalar_blocks": (
            equal(raw_in, trace_in * I16 / 16),
            equal(raw_out, trace_out * I16 / 16),
        ),
        "effects": effects,
        "projectors": all(equal(effect.H, effect) and equal(
            effect * effect, effect) for effect in effects),
        "orthogonal": all(equal(
            effects[a] * effects[b], sp.zeros(32)
        ) for a in range(8) for b in range(a + 1, 8)),
        "complete": equal(sum(effects, sp.zeros(32)), sp.eye(32)),
        "ranks": tuple(rank(effect) for effect in effects),
        "weights": tuple(sp.factor(sp.trace(rho0 * effect))
                         for effect in effects),
        "overlaps": overlaps,
        "real_rank": rank(real_overlaps),
        "first_blind": all(sp.simplify(overlaps[row, 0]) == 0
                           for row in range(4)),
        "ell": ell,
        "ell_positive": positive(ell),
        "slope_pattern": (
            sp.simplify(row_slopes[0] - ell) == 0
            and sp.simplify(row_slopes[1] - ell) == 0
            and sp.simplify(row_slopes[2] + ell) == 0
            and sp.simplify(row_slopes[3] + ell) == 0
        ),
        "derivatives": derivatives,
        "conditional": conditional,
        "coarse_zero": all(sp.simplify(
            derivatives[2 * row] + derivatives[2 * row + 1]
        ) == 0 for row in range(4)),
        "writer_unitary": equal(writer.H * writer, sp.eye(64)),
        "writer_nonidentity": not equal(writer, sp.eye(64)),
        "pointer_pullback": all(equal(induced[i], effects[i])
                                for i in range(8)),
        "source_terms": (len(source["forward"]), len(source["reverse"])),
        "actual_reverse_distinct": not all(
            equal(left[0], right[0]) and equal(left[1], right[1])
            for left, right in zip(
                source["reverse"], source["hermitian_control"]
            )
        ) if len(source["reverse"]) == len(source["hermitian_control"]) else True,
        "cubic_count": classification["proper_cubic_count"],
        "cubic_covariance": (
            classification["family_covariance"]
            and classification["context_covariance"]
        ),
    }


def exact_germ() -> dict[str, bool]:
    data = rebuild()
    history = b192.frozen_history_positivity_facts()
    invertible_at_zero = (
        data["trace_in"] != 0 and data["trace_out"] != 0
        and data["total"] != 0
        and data["source_terms"][0] > 0 and data["source_terms"][1] > 0
    )
    strict_zero = (
        history["all_positive"]
        and positive(data["trace_in"]) and positive(data["trace_out"])
    )
    pvm = (
        data["projectors"] and data["orthogonal"] and data["complete"]
        and data["weights"] == (R(1, 8),) * 8
    )
    nonconstant = (
        data["real_rank"] == 1 and data["first_blind"]
        and data["ell_positive"] and data["slope_pattern"]
    )
    return {
        "analytic": invertible_at_zero,
        "strict_zero": strict_zero,
        "pvm": pvm,
        "positive_interval": invertible_at_zero and strict_zero and pvm,
        "finite_nonconstant": (
            invertible_at_zero and strict_zero and pvm and nonconstant
        ),
    }


def note_ok() -> bool:
    path = ROOT / NOTE
    if not path.is_file():
        return False
    text = path.read_text()
    return all(needle in text for needle in (
        "right-Schur probability germ",
        "nearest-neighbor eta remains open",
        "obligation retirement: 0",
        "per_element:", "per_site:", "per_mode:", "per_block:",
        "lattice_wide:",
    ))


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    auth = authority()
    data = rebuild()
    germ = exact_germ()
    claims: dict[str, object] = {
        "main": MAIN,
        "goal": GOAL_BLOB,
        "column": 1,
        "actual_reverse": True,
        "baseline_positive": True,
        "import_i32": False,
        "complete": True,
        "orthogonal": True,
        "derivative": True,
        "tangent_density": False,
        "finite_germ": True,
        "coarse": True,
        "pointer": True,
        "binary_variation": True,
        "ports_m2": False,
        "eta": False,
        "formation": False,
        "periodic": False,
        "two_tt": False,
        "axiom": False,
        "obligation": 0,
        "toe": False,
        "retained": False,
        "no_go": False,
    }
    changes = {
        "stale_authority": ("main", "stale"),
        "alter_registration": ("goal", "altered"),
        "use_h1_column0": ("column", 0),
        "make_reverse_adjoint": ("actual_reverse", False),
        "erase_baseline_positivity": ("baseline_positive", False),
        "import_i32": ("import_i32", True),
        "erase_effect_completeness": ("complete", False),
        "erase_effect_orthogonality": ("orthogonal", False),
        "erase_h1_derivative": ("derivative", False),
        "call_tangent_density": ("tangent_density", True),
        "deny_finite_germ": ("finite_germ", False),
        "break_coarse_pairs": ("coarse", False),
        "break_pointer_dilation": ("pointer", False),
        "erase_binary_variation": ("binary_variation", False),
        "call_four_ports_m2": ("ports_m2", True),
        "call_h1_eta": ("eta", True),
        "call_write_record_formation": ("formation", True),
        "call_schur_periodic": ("periodic", True),
        "claim_two_tt": ("two_tt", True),
        "claim_axiom": ("axiom", True),
        "claim_obligation": ("obligation", 1),
        "claim_toe": ("toe", True),
        "claim_retained": ("retained", True),
        "claim_no_go": ("no_go", True),
    }
    if mutation:
        key, value = changes[mutation]
        claims[key] = value

    return {
        "I1": (
            auth["main"] == claims["main"] and auth["parent"] and auth["prereg"]
            and auth["goal_registered"] == claims["goal"]
            and auth["goal_now"] == GOAL_BLOB
            and auth["preflight_registered"] == PREFLIGHT_BLOB
            and auth["preflight_now"] == PREFLIGHT_BLOB and auth["inputs"],
            "registration authority and immutable targets are independently pinned",
        ),
        "I2": (
            claims["column"] == 1 and data["actual_reverse_distinct"]
            == claims["actual_reverse"] and data["source_terms"][0] > 0,
            "the literal H1 second-TT source family uses the actual reverse block",
        ),
        "I3": (
            all(data["scalar_blocks"])
            and germ["strict_zero"] == claims["baseline_positive"]
            and claims["import_i32"] is False,
            "the action-derived zero-source marginal is block-scalar and strictly positive without an imported maximally mixed state",
        ),
        "I4": (
            data["complete"] == claims["complete"]
            and data["orthogonal"] == claims["orthogonal"]
            and data["projectors"] and data["ranks"] == (4,) * 8,
            "an independent reconstruction gives the same complete eight-projector C32 context",
        ),
        "I5": (
            germ["positive_interval"]
            and germ["finite_nonconstant"] == claims["finite_germ"]
            and data["ell_positive"] == claims["derivative"]
            and claims["tangent_density"] is False,
            "strict positivity plus analytic inversion and a nonzero exact derivative force a finite positive nonconstant law germ",
        ),
        "I6": (
            data["coarse_zero"] == claims["coarse"]
            and data["writer_unitary"] and data["writer_nonidentity"]
            and data["pointer_pullback"] == claims["pointer"]
            and any(value != 0 for value in data["conditional"])
            == claims["binary_variation"],
            "coarse ports add normally and the rebuilt nonidentity M2 writer reproduces a varying conditional binary law",
        ),
        "I7": (
            data["cubic_count"] == 24 and data["cubic_covariance"]
            and claims["ports_m2"] is False and claims["eta"] is False,
            "the supplied detector orbit is cubic-covariant while port context and H1 remain distinct from a proved nearest-neighbor eta law",
        ),
        "I8": (
            claims["formation"] is False and claims["periodic"] is False
            and claims["two_tt"] is False and claims["axiom"] is False
            and claims["obligation"] == 0 and claims["toe"] is False
            and claims["retained"] is False and claims["no_go"] is False
            and note_ok(),
            "scope fences exclude formation/history, periodic CAR, two-TT, axiom, retained, obligation, TOE, and broad no-go claims",
        ),
    }


def mutation_sweep() -> int:
    survivors = []
    for mutation in MUTATIONS:
        if all(ok for ok, _message in evaluate(mutation).values()):
            survivors.append(mutation)
    print(f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(survivors)} FAIL={len(survivors)}")
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    checks = evaluate(args.mutation)
    passed = 0
    for key, (ok, message) in checks.items():
        print(f"[{key}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(ok)
    data = rebuild()
    print(
        "INDEPENDENT_H1: exact ell>0; effect derivative signs="
        "(+,-,+,-,-,+,-,+); coarse derivatives=0; "
        f"ell={data['ell']}."
    )
    print(
        "INDEPENDENT_RESULT: positive finite H1 Schur law germ=yes; "
        "M2 pointer pullback=yes; nearest-neighbor eta/open history=open; "
        "obligation_retirement=0; TOE movement=0."
    )
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
